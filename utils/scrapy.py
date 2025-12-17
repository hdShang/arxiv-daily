from typing import List, Tuple, Dict, Optional
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import re
import json
import arxiv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

US_EASTERN = ZoneInfo("US/Eastern")

def load_tags(tags_file: str) -> List[str]:
    with open(tags_file, 'r', encoding='utf-8') as f:
        tags = json.load(f)
    return tags['tags']


def load_interests(interests_file: str) -> Dict:
    """加载用户感兴趣的领域配置"""
    try:
        with open(interests_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def _keyword_match(keyword: str, text: str) -> bool:
    """
    智能关键词匹配：
    - 短关键词（<=4字符）使用词边界匹配，避免误匹配
    - 长关键词使用子串匹配
    - 支持连字符和空格的变体匹配
    """
    kw = keyword.lower()
    
    # 生成变体：连字符 <-> 空格
    variants = [kw]
    if '-' in kw:
        variants.append(kw.replace('-', ' '))
        variants.append(kw.replace('-', ''))
    if ' ' in kw:
        variants.append(kw.replace(' ', '-'))
        variants.append(kw.replace(' ', ''))
    
    for variant in variants:
        # 短关键词使用词边界匹配（避免 "VO" 匹配 "evolution"）
        if len(variant) <= 4:
            pattern = r'\b' + re.escape(variant) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                return True
        else:
            # 长关键词使用子串匹配
            if variant in text:
                return True
    
    return False


def _check_negative_keywords(title: str, abstract: str, negative_keywords: List[str]) -> Tuple[bool, List[str]]:
    """
    检查论文是否匹配负面关键词（一票否决）
    返回: (是否排除, 匹配到的负面关键词列表)
    """
    if not negative_keywords:
        return False, []
    
    text = f"{title} {abstract}".lower()
    matched_negatives = []
    
    for kw in negative_keywords:
        if _keyword_match(kw, text):
            matched_negatives.append(kw)
    
    return len(matched_negatives) > 0, matched_negatives


def _calculate_combination_bonus(title: str, abstract: str, combination_bonuses: List[Dict]) -> float:
    """
    计算组合加分
    如果论文同时匹配多个相关条件，给予额外加分
    """
    if not combination_bonuses:
        return 0.0
    
    text = f"{title} {abstract}".lower()
    total_bonus = 0.0
    
    for combo in combination_bonuses:
        conditions = combo.get("conditions", [])
        bonus = combo.get("bonus", 0.0)
        
        # 检查所有条件组是否都至少匹配一个关键词
        all_matched = True
        for condition_group in conditions:
            group_matched = False
            for kw in condition_group:
                if _keyword_match(kw, text):
                    group_matched = True
                    break
            if not group_matched:
                all_matched = False
                break
        
        if all_matched:
            total_bonus += bonus
    
    return total_bonus


def match_interests(paper: Dict, interests_config: Dict) -> Dict:
    """
    加权打分匹配系统
    
    特点：
    1. 标题匹配权重高于摘要
    2. 不同兴趣领域有不同权重
    3. 组合关键词可获得额外加分
    4. 负面关键词一票否决（除非正面分数很高）
    """
    if not interests_config:
        return {
            "matched_interests": [], 
            "relevance_score": 0.0, 
            "excluded": False, 
            "exclusion_keywords": [],
            "combination_bonus": 0.0
        }
    
    title = paper.get("title", "").lower()
    abstract = paper.get("summary", "").lower()
    
    # 获取配置参数
    scoring_config = interests_config.get("scoring", {})
    title_multiplier = scoring_config.get("title_multiplier", 3.0)
    abstract_multiplier = scoring_config.get("abstract_multiplier", 1.0)
    min_threshold = scoring_config.get("min_score_threshold", 2.0)
    
    interests = interests_config.get("interests", [])
    negative_keywords = interests_config.get("negative_keywords", [])
    combination_bonuses = interests_config.get("combination_bonuses", [])
    
    # 1. 检查负面关键词
    is_negative, matched_negatives = _check_negative_keywords(title, abstract, negative_keywords)
    
    # 2. 计算各兴趣领域的加权得分
    matched = []
    total_score = 0.0
    
    for interest in interests:
        if not interest.get("enabled", True):
            continue
        
        name = interest.get("name", "")
        keywords = interest.get("keywords", [])
        weight = interest.get("weight", 1.0)
        
        category_score = 0.0
        matched_keywords = []
        title_matches = []
        abstract_matches = []
        
        for kw in keywords:
            # 标题匹配：高权重
            if _keyword_match(kw, title):
                category_score += title_multiplier * weight
                title_matches.append(kw)
                matched_keywords.append(f"[T]{kw}")
            # 摘要匹配：基础权重
            elif _keyword_match(kw, abstract):
                category_score += abstract_multiplier * weight
                abstract_matches.append(kw)
                matched_keywords.append(kw)
        
        if category_score > 0:
            matched.append({
                "name": name,
                "matched_keywords": matched_keywords,
                "title_matches": title_matches,
                "abstract_matches": abstract_matches,
                "score": round(category_score, 2),
                "weight": weight
            })
            total_score += category_score
    
    # 3. 计算组合加分
    combo_bonus = _calculate_combination_bonus(title, abstract, combination_bonuses)
    total_score += combo_bonus
    
    # 4. 判断是否排除
    # 负面关键词否决逻辑：
    # - 如果有正面匹配且分数 >= 3倍阈值（6.0），正面匹配覆盖负面
    # - 如果没有正面匹配或分数太低，负面关键词生效
    should_exclude = False
    if is_negative:
        # 只有当正面分数足够高（>= 3倍阈值）时才能覆盖负面关键词
        if total_score < min_threshold * 3:
            should_exclude = True
    
    return {
        "matched_interests": matched,
        "relevance_score": round(total_score, 2),
        "excluded": should_exclude,
        "exclusion_keywords": matched_negatives,
        "combination_bonus": round(combo_bonus, 2)
    }


def filter_by_interests(papers: List[Dict], interests_file: str = "interests.json") -> List[Dict]:
    """
    根据加权打分系统筛选论文
    
    特点：
    1. 标题匹配权重 3x，摘要匹配权重 1x
    2. 不同兴趣领域有不同权重（1.0-2.0）
    3. 组合匹配可获得额外加分
    4. 负面关键词一票否决（除非正面分数很高）
    """
    interests_config = load_interests(interests_file)
    
    if not interests_config:
        print("[INFO] 未找到 interests.json，跳过兴趣筛选")
        return papers
    
    # 获取阈值配置
    scoring_config = interests_config.get("scoring", {})
    min_threshold = scoring_config.get("min_score_threshold", 2.0)
    
    filtered = []
    excluded_count = 0
    below_threshold_count = 0
    
    for paper in papers:
        match_info = match_interests(paper, interests_config)
        paper["matched_interests"] = match_info["matched_interests"]
        paper["relevance_score"] = match_info["relevance_score"]
        paper["combination_bonus"] = match_info.get("combination_bonus", 0)
        
        # 检查是否被负面关键词排除
        if match_info.get("excluded", False):
            excluded_count += 1
            continue
        
        # 检查是否达到分数阈值
        if match_info["relevance_score"] >= min_threshold:
            filtered.append(paper)
        else:
            below_threshold_count += 1
    
    # 按相关性分数排序
    filtered.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)
    
    # 打印统计信息
    print(f"\n{'='*50}")
    print(f"📊 筛选统计")
    print(f"{'='*50}")
    print(f"   原始论文数: {len(papers)}")
    print(f"   ✅ 通过筛选: {len(filtered)} 篇 (分数 ≥ {min_threshold})")
    print(f"   ❌ 负面排除: {excluded_count} 篇")
    print(f"   ⚪ 未达阈值: {below_threshold_count} 篇")
    
    # 显示各领域匹配统计
    interest_counts = {}
    interest_scores = {}
    for p in filtered:
        for m in p.get("matched_interests", []):
            name = m["name"]
            interest_counts[name] = interest_counts.get(name, 0) + 1
            interest_scores[name] = interest_scores.get(name, 0) + m.get("score", 0)
    
    if interest_counts:
        print(f"\n📈 各领域命中统计:")
        for name, count in sorted(interest_counts.items(), key=lambda x: -x[1]):
            avg_score = interest_scores[name] / count if count > 0 else 0
            print(f"   {name}: {count} 篇 (平均分: {avg_score:.1f})")
    
    # 显示 Top 5 高分论文
    if filtered:
        print(f"\n🏆 Top 5 高分论文:")
        for i, p in enumerate(filtered[:5], 1):
            title = p.get("title", "")[:50]
            score = p.get("relevance_score", 0)
            bonus = p.get("combination_bonus", 0)
            interests = [m["name"].split("(")[0].strip() for m in p.get("matched_interests", [])[:2]]
            bonus_str = f" (+{bonus}组合)" if bonus > 0 else ""
            print(f"   {i}. [{score:.1f}分{bonus_str}] {title}...")
            print(f"      领域: {', '.join(interests)}")
    
    print(f"{'='*50}\n")
    
    return filtered

def get_UTC_range() -> Tuple[str, str, str]:
    fmt = "%Y%m%d%H%M"
    
    now_utc = datetime.now(timezone.utc)
    now_et = now_utc.astimezone(US_EASTERN)
    today_et = now_et.date()
    t2000_et = datetime(today_et.year, today_et.month, today_et.day, 20, 0, 0, tzinfo=US_EASTERN)
    
    if now_et < t2000_et:
        end_et = t2000_et - timedelta(days=1, minutes=1)
    else:
        end_et = t2000_et
    if end_et.weekday() in (4, 5):  # Friday or Saturday
        end_et -= timedelta(days=end_et.weekday() - 3, minutes=1)  # Move to Thursday
    
    if end_et.weekday() == 6:
        start_et = end_et - timedelta(days=3, minutes=-1)
    else:
        start_et = end_et - timedelta(days=1, minutes=-1)
    
    return (start_et.astimezone(timezone.utc).strftime(fmt),
            end_et.astimezone(timezone.utc).strftime(fmt),
            end_et.strftime("%Y-%m-%d"))


def extract_code_links(text: str) -> List[Dict[str, str]]:
    """从文本中提取代码仓库链接（GitHub, GitLab, Hugging Face 等）"""
    patterns = [
        # GitHub
        (r'https?://github\.com/[\w\-\.]+/[\w\-\.]+(?:/[\w\-\.]*)?', 'github'),
        # GitLab
        (r'https?://gitlab\.com/[\w\-\.]+/[\w\-\.]+(?:/[\w\-\.]*)?', 'gitlab'),
        # Hugging Face
        (r'https?://huggingface\.co/[\w\-\.]+(?:/[\w\-\.]+)?', 'huggingface'),
        # 项目主页（常见模式）
        (r'https?://[\w\-\.]+\.github\.io/[\w\-\.]+/?', 'project_page'),
    ]
    
    links = []
    seen = set()
    for pattern, link_type in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for url in matches:
            # 清理 URL（移除末尾的标点）
            url = re.sub(r'[.,;:!?)}\]]+$', '', url)
            if url not in seen:
                seen.add(url)
                links.append({"url": url, "type": link_type})
    return links


def fetch_arxiv_thumbnail(arxiv_id: str, timeout: int = 10) -> Optional[str]:
    """
    从 arXiv 页面抓取论文预览缩略图
    返回图片 URL 或 None
    """
    base_id = arxiv_id.split('v')[0]
    abs_url = f"https://arxiv.org/abs/{base_id}"
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; ArxivDailyBot/1.0)'
        }
        resp = requests.get(abs_url, headers=headers, timeout=timeout)
        if resp.status_code != 200:
            return None
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # 方式1: 查找 og:image meta 标签
        og_image = soup.find('meta', property='og:image')
        if og_image and og_image.get('content'):
            return og_image['content']
        
        # 方式2: 查找论文缩略图 (通常在 arXiv 页面的特定位置)
        # arXiv 使用 https://arxiv.org/html/{id}/extracted/figure1.png 格式
        # 或者 https://static.arxiv.org/static/browse/0.3.4/images/...
        
        # 查找页面中的第一张相关图片
        for img in soup.find_all('img'):
            src = img.get('src', '')
            # 排除图标和装饰图片
            if any(x in src.lower() for x in ['icon', 'logo', 'button', 'arrow', 'social']):
                continue
            # 找到有意义的图片
            if 'arxiv' in src or src.startswith('/'):
                if src.startswith('/'):
                    src = f"https://arxiv.org{src}"
                return src
        
        return None
    except Exception:
        return None


def fetch_thumbnails_batch(papers: List[Dict], max_workers: int = 10) -> List[Dict]:
    """批量抓取论文缩略图"""
    print(f"[INFO] 正在抓取 {len(papers)} 篇论文的预览图...")
    
    def fetch_one(paper: Dict) -> Tuple[str, Optional[str]]:
        arxiv_id = paper.get('arxiv_id', '')
        thumb = fetch_arxiv_thumbnail(arxiv_id)
        return arxiv_id, thumb
    
    thumbnails = {}
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_one, p): p for p in papers}
        for future in tqdm(as_completed(futures), total=len(futures), desc="抓取缩略图"):
            arxiv_id, thumb = future.result()
            if thumb:
                thumbnails[arxiv_id] = thumb
    
    # 更新论文数据
    for paper in papers:
        arxiv_id = paper.get('arxiv_id', '')
        if arxiv_id in thumbnails:
            paper['thumbnail'] = thumbnails[arxiv_id]
    
    print(f"[INFO] 成功获取 {len(thumbnails)}/{len(papers)} 篇论文的预览图")
    return papers


def _result_to_minimal(r: arxiv.Result) -> Dict:
    arxiv_id = r.get_short_id() if hasattr(r, "get_short_id") else r.entry_id.split("/abs/")[-1]
    authors = [a.name for a in r.authors] if r.authors else []
    
    # 获取分类信息
    categories = list(r.categories) if r.categories else []
    primary_category = r.primary_category if hasattr(r, "primary_category") and r.primary_category else (categories[0] if categories else "")
    
    # 获取更多元数据
    summary = (r.summary or "").strip()
    
    # 提取代码链接
    code_links = extract_code_links(summary)
    
    # 发布和更新日期
    published = r.published.strftime("%Y-%m-%d") if r.published else ""
    updated = r.updated.strftime("%Y-%m-%d") if r.updated else ""
    
    # 评论信息（通常包含页数、会议等）
    comment = (r.comment or "").strip() if hasattr(r, 'comment') and r.comment else ""
    
    # DOI 和期刊引用
    doi = r.doi if hasattr(r, 'doi') and r.doi else ""
    journal_ref = (r.journal_ref or "").strip() if hasattr(r, 'journal_ref') and r.journal_ref else ""
    
    # PDF URL
    pdf_url = r.pdf_url if hasattr(r, 'pdf_url') else f"https://arxiv.org/pdf/{arxiv_id.split('v')[0]}.pdf"
    
    return {
        "title": (r.title or "").strip().replace("\n", " "),
        "authors": authors,
        "arxiv_id": arxiv_id,
        "summary": summary,
        "categories": categories,
        "primary_category": primary_category,
        "published": published,
        "updated": updated,
        "comment": comment,
        "doi": doi,
        "journal_ref": journal_ref,
        "pdf_url": pdf_url,
        "code_links": code_links,
    }


def query_arxiv(tags: List[str], time_range: Tuple[str, str], max_results: int = 500, fetch_thumbnails: bool = False) -> Dict:
    start, end = time_range
    tag_clause = " OR ".join(f"cat:{t}" for t in tags)
    query = f"({tag_clause}) AND submittedDate:[{start} TO {end}]"

    client = arxiv.Client(page_size=200, delay_seconds=1.0, num_retries=3)

    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    seen = set()
    papers = []
    print(f"[INFO] 正在从 arXiv 抓取论文...")
    for r in tqdm(client.results(search), desc="抓取论文", unit="paper"):
        item = _result_to_minimal(r)
        if item["arxiv_id"] in seen:
            continue
        seen.add(item["arxiv_id"])
        papers.append(item)
    
    # 可选：批量抓取缩略图
    if fetch_thumbnails and papers:
        papers = fetch_thumbnails_batch(papers)
    
    return {"count": len(papers), "papers": papers}


def get_today_arxiv(tags: List[str], max_results: int = 500, fetch_thumbnails: bool = False) -> Tuple[Dict, str]:
    start, end, label_date = get_UTC_range()
    return query_arxiv(tags, (start, end), max_results=max_results, fetch_thumbnails=fetch_thumbnails), label_date


if __name__ == "__main__":
    tags = load_tags('../tags.json')
    result, label_date = get_today_arxiv(tags, fetch_thumbnails=True)
    print(f'Tags: {tags}')
    print(f"Date: {label_date}, Found {result['count']} papers")
    
    # 显示一些示例
    if result['papers']:
        p = result['papers'][0]
        print(f"\n示例论文:")
        print(f"  标题: {p['title'][:60]}...")
        print(f"  发布: {p['published']}")
        print(f"  代码: {p['code_links']}")
        print(f"  缩略图: {p.get('thumbnail', 'N/A')}")
