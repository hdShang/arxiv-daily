"""
从 arXiv HTML 版本 (ar5iv) 提取论文图片
使用同步请求，避免 asyncio 事件循环冲突
"""
import re
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Optional
from tqdm import tqdm


# ar5iv 基础 URL
AR5IV_BASE = "https://ar5iv.labs.arxiv.org/html/"

# 请求超时
TIMEOUT = 30


def fetch_html(url: str) -> Optional[str]:
    """获取 HTML 内容（同步）"""
    try:
        resp = requests.get(url, timeout=TIMEOUT)
        if resp.status_code == 200:
            return resp.text
        return None
    except Exception as e:
        return None


def extract_arxiv_id(arxiv_id: str) -> str:
    """提取纯净的 arXiv ID (去掉版本号)"""
    # 2512.14689v1 -> 2512.14689
    match = re.match(r'(\d+\.\d+)', arxiv_id)
    return match.group(1) if match else arxiv_id.split('v')[0]


def parse_images_from_html(html: str, arxiv_id: str) -> List[Dict]:
    """
    从 ar5iv HTML 中解析图片
    返回: [{"url": "...", "caption": "...", "figure_id": "figure1"}, ...]
    """
    images = []
    base_url = f"{AR5IV_BASE}{arxiv_id}/"
    
    # 方法1: 匹配 figure 标签中的图片
    figure_pattern = re.compile(
        r'<figure[^>]*id=["\']([^"\']*)["\'][^>]*>.*?'
        r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>.*?'
        r'(?:<figcaption[^>]*>(.*?)</figcaption>)?.*?</figure>',
        re.DOTALL | re.IGNORECASE
    )
    
    for match in figure_pattern.finditer(html):
        fig_id = match.group(1)
        img_src = match.group(2)
        caption = match.group(3) or ""
        
        # 清理 caption 中的 HTML 标签
        caption = re.sub(r'<[^>]+>', '', caption).strip()
        caption = ' '.join(caption.split())[:200]
        
        # 构建完整 URL
        if img_src.startswith('http'):
            img_url = img_src
        elif img_src.startswith('/'):
            img_url = f"https://ar5iv.labs.arxiv.org{img_src}"
        else:
            img_url = base_url + img_src
        
        # 过滤掉太小的图片
        if any(skip in img_src.lower() for skip in ['icon', 'logo', 'badge', 'button']):
            continue
            
        images.append({
            "url": img_url,
            "caption": caption,
            "figure_id": fig_id
        })
    
    # 方法2: 如果 figure 匹配少，尝试直接匹配主要图片
    if len(images) < 2:
        img_pattern = re.compile(r'<img[^>]*src=["\']([^"\']*x\d+\.(png|jpg|jpeg|gif|svg))["\']', re.IGNORECASE)
        seen_urls = {img["url"] for img in images}
        
        for match in img_pattern.finditer(html):
            img_src = match.group(1)
            if img_src.startswith('http'):
                img_url = img_src
            elif img_src.startswith('/'):
                img_url = f"https://ar5iv.labs.arxiv.org{img_src}"
            else:
                img_url = base_url + img_src
            
            if img_url not in seen_urls:
                images.append({
                    "url": img_url,
                    "caption": "",
                    "figure_id": f"img_{len(images)}"
                })
                seen_urls.add(img_url)
    
    return images


def extract_paper_images(arxiv_id: str, max_images: int = 5) -> List[Dict]:
    """
    提取单篇论文的图片（同步）
    
    Args:
        arxiv_id: arXiv ID (如 2512.14689 或 2512.14689v1)
        max_images: 最多提取几张图片
    
    Returns:
        图片列表 [{"url": "...", "caption": "...", "figure_id": "..."}, ...]
    """
    clean_id = extract_arxiv_id(arxiv_id)
    html_url = f"{AR5IV_BASE}{clean_id}"
    
    html = fetch_html(html_url)
    if not html:
        return []
    
    images = parse_images_from_html(html, clean_id)
    
    # 优先选择有 caption 的图片
    images_with_caption = [img for img in images if img["caption"]]
    images_without_caption = [img for img in images if not img["caption"]]
    sorted_images = images_with_caption + images_without_caption
    
    return sorted_images[:max_images]


def batch_extract_images(
    papers: List[Dict],
    max_images_per_paper: int = 3,
    concurrency: int = 5,
    show_progress: bool = True
) -> Dict[str, List[Dict]]:
    """
    批量提取多篇论文的图片（使用线程池，同步方式）
    
    Args:
        papers: 论文列表，每个需要有 arxiv_id 字段
        max_images_per_paper: 每篇论文最多提取几张图片
        concurrency: 并发数
        show_progress: 是否显示进度条
    
    Returns:
        {arxiv_id: [图片列表], ...}
    """
    results = {}
    
    # 过滤出有 arxiv_id 的论文
    valid_papers = [p for p in papers if p.get("arxiv_id")]
    
    if not valid_papers:
        return results
    
    def extract_one(paper):
        arxiv_id = paper.get("arxiv_id", "")
        images = extract_paper_images(arxiv_id, max_images_per_paper)
        return arxiv_id, images
    
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {executor.submit(extract_one, p): p for p in valid_papers}
        
        iterator = as_completed(futures)
        if show_progress:
            iterator = tqdm(iterator, total=len(futures), desc="提取图片", unit="篇")
        
        for future in iterator:
            try:
                arxiv_id, images = future.result()
                if arxiv_id:
                    results[arxiv_id] = images
            except Exception as e:
                pass  # 静默忽略单篇论文的错误
    
    return results


# 测试函数
def test_extract():
    """测试图片提取"""
    test_id = "2512.14689"
    print(f"测试提取: {test_id}")
    images = extract_paper_images(test_id)
    print(f"找到 {len(images)} 张图片:")
    for img in images:
        print(f"  - {img['figure_id']}: {img['url'][:60]}...")
        if img['caption']:
            print(f"    Caption: {img['caption'][:80]}...")
    return images


if __name__ == "__main__":
    test_extract()
