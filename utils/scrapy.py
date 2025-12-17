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


def _match_concept_groups(title: str, abstract: str, concept_groups: List[Dict], 
                          title_multiplier: float = 3.0, abstract_multiplier: float = 1.0) -> Dict:
    """
    匹配概念组，返回命中的组及其得分
    """
    hit_groups = {}  # group_id -> {name, score, keywords}
    
    for group in concept_groups:
        group_id = group.get("id", "")
        group_name = group.get("name", "")
        keywords = group.get("keywords", [])
        weight = group.get("weight", 1.0)
        
        group_score = 0.0
        matched_keywords = []
        
        for kw in keywords:
            # 标题匹配：高权重
            if _keyword_match(kw, title):
                group_score += title_multiplier * weight
                matched_keywords.append(f"[T]{kw}")
            # 摘要匹配：基础权重
            elif _keyword_match(kw, abstract):
                group_score += abstract_multiplier * weight
                matched_keywords.append(kw)
        
        if group_score > 0:
            hit_groups[group_id] = {
                "name": group_name,
                "score": group_score,
                "matched_keywords": matched_keywords
            }
    
    return hit_groups


def _cross_validate(hit_groups: Dict, rules: List[Dict]) -> Tuple[bool, List[str]]:
    """
    交叉验证：检查命中的概念组是否满足至少一条规则
    返回: (是否通过验证, 满足的规则名称列表)
    
    规则类型：
    1. 交叉规则：required + any_of，需要多个概念组
    2. 单独规则：required + 空的 any_of，单个概念组即可通过
    """
    hit_group_ids = set(hit_groups.keys())
    satisfied_rules = []
    
    for rule in rules:
        rule_name = rule.get("name", "")
        required = set(rule.get("required", []))
        any_of = set(rule.get("any_of", []))
        
        # 检查 required 组是否都命中
        if not required.issubset(hit_group_ids):
            continue
        
        # 如果 any_of 为空，则只需要 required 命中即可（单独规则）
        if not any_of:
            satisfied_rules.append(rule_name)
            continue
        
        # 检查 any_of 组是否至少命中一个（交叉规则）
        if any_of.intersection(hit_group_ids):
            satisfied_rules.append(rule_name)
    
    return len(satisfied_rules) > 0, satisfied_rules


def match_interests(paper: Dict, interests_config: Dict) -> Dict:
    """
    五大支柱匹配系统
    
    核心逻辑：
    1. 负面关键词一票否决（严格过滤）
    2. 匹配五大支柱（OR逻辑）：命中任意一个支柱即可
    3. 计算加权得分
    
    五大支柱：
    - 支柱一：机器人控制（移动、操作、Sim2Real）
    - 支柱二：前沿算法（RL、世界模型、网络架构）
    - 支柱三：感知与SLAM（深度估计、里程计、建图）
    - 支柱四：动作来源（重定向、生成、匹配）
    - 支柱五：物理动画（Character Control、AMP）
    """
    if not interests_config:
        return {
            "matched_interests": [], 
            "relevance_score": 0.0, 
            "excluded": False, 
            "exclusion_keywords": [],
            "hit_pillars": []
        }
    
    title = paper.get("title", "").lower()
    abstract = paper.get("summary", "").lower()
    
    # 获取配置参数
    filter_settings = interests_config.get("filter_settings", {})
    title_multiplier = filter_settings.get("title_multiplier", 3.0)
    abstract_multiplier = filter_settings.get("abstract_multiplier", 1.0)
    
    concept_groups = interests_config.get("concept_groups", [])
    negative_keywords = interests_config.get("negative_keywords", [])
    
    # 1. 严格的负面关键词过滤
    is_negative, matched_negatives = _check_negative_keywords(title, abstract, negative_keywords)
    
    # 2. 匹配五大支柱（OR逻辑）
    hit_groups = _match_concept_groups(title, abstract, concept_groups, 
                                       title_multiplier, abstract_multiplier)
    
    # 3. 计算总分
    total_score = sum(g["score"] for g in hit_groups.values())
    
    # 4. 构建匹配结果
    matched = []
    for group_id, group_info in hit_groups.items():
        matched.append({
            "name": group_info["name"],
            "id": group_id,
            "matched_keywords": group_info["matched_keywords"],
            "score": round(group_info["score"], 2)
        })
    
    # 5. 判断是否排除
    # 负面关键词严格否决，除非分数极高（>=3倍阈值）
    should_exclude = False
    if is_negative:
        min_threshold = filter_settings.get("min_relevance_score", 1.5)
        if total_score < min_threshold * 3:
            should_exclude = True
    
    return {
        "matched_interests": matched,
        "relevance_score": round(total_score, 2),
        "excluded": should_exclude,
        "exclusion_keywords": matched_negatives,
        "hit_pillars": list(hit_groups.keys())
    }


def filter_by_interests(papers: List[Dict], interests_file: str = "interests.json") -> List[Dict]:
    """
    五大支柱筛选系统
    
    核心逻辑：
    1. 负面关键词严格过滤（医学/金融/NLP等）
    2. 五大支柱 OR 逻辑：命中任意一个支柱即保留
    3. 分数阈值过滤
    
    五大支柱：
    - 支柱一：机器人控制（移动、操作、Sim2Real）
    - 支柱二：前沿算法（RL、世界模型、网络架构）  
    - 支柱三：感知与SLAM（深度估计、里程计、建图）
    - 支柱四：动作来源（重定向、生成、匹配）
    - 支柱五：物理动画（Character Control、AMP）
    """
    interests_config = load_interests(interests_file)
    
    if not interests_config:
        print("[INFO] 未找到 interests.json，跳过兴趣筛选")
        return papers
    
    # 获取阈值配置
    filter_settings = interests_config.get("filter_settings", {})
    min_threshold = filter_settings.get("min_relevance_score", 1.5)
    
    filtered = []
    excluded_count = 0
    below_threshold_count = 0
    no_match_count = 0
    
    for paper in papers:
        match_info = match_interests(paper, interests_config)
        paper["matched_interests"] = match_info["matched_interests"]
        paper["relevance_score"] = match_info["relevance_score"]
        paper["hit_pillars"] = match_info.get("hit_pillars", [])
        
        # 检查是否被负面关键词排除
        if match_info.get("excluded", False):
            excluded_count += 1
            continue
        
        # 检查是否达到分数阈值（任意支柱命中即可）
        if match_info["relevance_score"] >= min_threshold:
            filtered.append(paper)
        elif len(match_info.get("hit_pillars", [])) > 0:
            below_threshold_count += 1
        else:
            no_match_count += 1
    
    # 按相关性分数排序
    filtered.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)
    
    # 打印统计信息
    print(f"\n{'='*60}")
    print(f"📊 五大支柱筛选统计 (OR逻辑)")
    print(f"{'='*60}")
    print(f"   原始论文数: {len(papers)}")
    print(f"   ✅ 通过筛选: {len(filtered)} 篇 (命中支柱 + 分数 ≥ {min_threshold})")
    print(f"   ❌ 负面排除: {excluded_count} 篇 (医学/金融/NLP等)")
    print(f"   ⚪ 分数不足: {below_threshold_count} 篇")
    print(f"   ⬜ 无匹配: {no_match_count} 篇")
    
    # 显示各支柱命中统计
    pillar_counts = {}
    pillar_scores = {}
    for p in filtered:
        for m in p.get("matched_interests", []):
            name = m["name"]
            pillar_counts[name] = pillar_counts.get(name, 0) + 1
            pillar_scores[name] = pillar_scores.get(name, 0) + m.get("score", 0)
    
    if pillar_counts:
        print(f"\n📈 五大支柱命中统计:")
        for name, count in sorted(pillar_counts.items(), key=lambda x: -x[1]):
            avg_score = pillar_scores[name] / count if count > 0 else 0
            print(f"   {name}: {count} 篇 (平均分: {avg_score:.1f})")
    
    # 显示 Top 5 高分论文
    if filtered:
        print(f"\n🏆 Top 5 高分论文:")
        for i, p in enumerate(filtered[:5], 1):
            title = p.get("title", "")[:48]
            score = p.get("relevance_score", 0)
            pillars = p.get("hit_pillars", [])
            pillar_names = [name.split("：")[1].split(" ")[0] if "：" in name else name 
                          for name in [m["name"] for m in p.get("matched_interests", [])[:2]]]
            pillar_str = f" [{len(pillars)}个支柱]" if len(pillars) > 1 else ""
            print(f"   {i}. [{score:.1f}分{pillar_str}] {title}...")
            print(f"      支柱: {', '.join(pillar_names)}")
    
    print(f"{'='*60}\n")
    
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
