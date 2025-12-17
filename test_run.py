#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本：抓取少量论文并测试 AI 分析功能
用于验证整个流程是否正常工作
"""

import asyncio
import json
import os
import sys

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from utils.scrapy import load_tags, query_arxiv, get_UTC_range, extract_code_links
from utils.analyser import get_client, get_model, get_prompt, _parse_json_safely, SYSTEM_PROMPT, USER_TEMPLATE


def test_scraper():
    """测试论文抓取功能"""
    print("=" * 60)
    print("🔍 测试 1: 论文抓取")
    print("=" * 60)
    
    tags = load_tags('tags.json')
    print(f"📋 分类标签: {tags}")
    
    # 获取时间范围
    start, end, label_date = get_UTC_range()
    print(f"📅 日期范围: {label_date}")
    print(f"   UTC: {start} - {end}")
    
    # 只抓取 3 篇论文用于测试
    print(f"\n🌐 正在从 arXiv 抓取论文 (限制 3 篇)...")
    result = query_arxiv(tags, (start, end), max_results=3, fetch_thumbnails=False)
    
    papers = result.get("papers", [])
    print(f"✅ 成功抓取 {len(papers)} 篇论文\n")
    
    if not papers:
        print("❌ 没有抓取到论文，可能是时间范围内没有新论文")
        print("   尝试扩大时间范围或检查网络连接")
        return None
    
    # 显示第一篇论文的详情
    p = papers[0]
    print("📄 示例论文:")
    print(f"   标题: {p['title'][:70]}...")
    print(f"   arXiv ID: {p['arxiv_id']}")
    print(f"   作者: {', '.join(p['authors'][:3])}{'...' if len(p['authors']) > 3 else ''}")
    print(f"   分类: {p.get('categories', [])}")
    print(f"   主分类: {p.get('primary_category', '')}")
    print(f"   发布日期: {p.get('published', 'N/A')}")
    print(f"   代码链接: {p.get('code_links', [])}")
    print(f"   摘要: {p['summary'][:150]}...")
    
    return papers


def test_code_extraction():
    """测试代码链接提取"""
    print("\n" + "=" * 60)
    print("🔗 测试 2: 代码链接提取")
    print("=" * 60)
    
    test_texts = [
        "Code is available at https://github.com/user/repo",
        "Our model is on https://huggingface.co/org/model-name",
        "Project page: https://project-name.github.io/demo/",
        "No code link here, just regular text.",
    ]
    
    for text in test_texts:
        links = extract_code_links(text)
        status = "✅" if links else "➖"
        print(f"{status} 输入: {text[:50]}...")
        if links:
            for l in links:
                print(f"   → {l['type']}: {l['url']}")


async def test_ai_analysis(papers):
    """测试 AI 分析功能"""
    print("\n" + "=" * 60)
    print("🤖 测试 3: AI 分析")
    print("=" * 60)
    
    # 检查 API 配置
    api_key = os.getenv("LLM_API_KEY") or os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("LLM_BASE_URL", "https://api.deepseek.com")
    model = get_model()
    
    print(f"📡 API 配置:")
    print(f"   Base URL: {base_url}")
    print(f"   Model: {model}")
    print(f"   API Key: {'✅ 已设置' if api_key else '❌ 未设置'}")
    
    if not api_key:
        print("\n❌ 未设置 API Key，跳过 AI 分析测试")
        print("   请设置环境变量: export LLM_API_KEY=your-api-key")
        return None
    
    if not papers:
        print("\n❌ 没有论文数据，跳过 AI 分析测试")
        return None
    
    # 只分析第一篇论文
    paper = papers[0]
    print(f"\n📝 正在分析论文: {paper['title'][:50]}...")
    
    try:
        client = get_client()
        prompt = get_prompt(USER_TEMPLATE, paper)
        
        print(f"   发送请求到 {model}...")
        
        resp = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            response_format={"type": "json_object"},
            timeout=120,
        )
        
        text = resp.choices[0].message.content
        result = _parse_json_safely(text)
        
        if "_parse_error" in result:
            print(f"❌ JSON 解析错误: {result.get('_parse_error')}")
            print(f"   原始响应: {text[:200]}...")
            return None
        
        print("\n✅ AI 分析成功！\n")
        print("📊 分析结果:")
        print("-" * 40)
        
        if "headline_zh" in result:
            print(f"💡 一句话要点:\n   {result['headline_zh']}")
        
        if "summary_zh" in result:
            print(f"\n📝 中文摘要:\n   {result['summary_zh'][:200]}...")
        
        if "intro_zh" in result:
            print(f"\n📋 核心要点:")
            for i, point in enumerate(result['intro_zh'], 1):
                print(f"   {i}. {point}")
        
        if "method_zh" in result:
            print(f"\n🔬 方法详解:\n   {result['method_zh'][:150]}...")
        
        if "application_zh" in result:
            print(f"\n🎯 应用场景:\n   {result['application_zh']}")
        
        if "highlight_zh" in result:
            print(f"\n📊 实验亮点:\n   {result['highlight_zh']}")
        
        if "tags_zh" in result:
            print(f"\n🏷️ 关键词: {', '.join(result['tags_zh'])}")
        
        return result
        
    except Exception as e:
        print(f"\n❌ AI 分析失败: {type(e).__name__}: {e}")
        return None


def test_page_build():
    """测试页面生成功能"""
    print("\n" + "=" * 60)
    print("🌐 测试 4: 页面生成")
    print("=" * 60)
    
    try:
        from build_page import slugify, render_paper_md, load_tags
        
        # 测试 slugify
        test_title = "Test Paper: A Novel Approach! (2024)"
        slug = slugify(test_title)
        print(f"✅ slugify 测试: '{test_title}' → '{slug}'")
        
        # 测试论文渲染
        test_paper = {
            "title": "Test Paper Title",
            "authors": ["Author One", "Author Two"],
            "arxiv_id": "2412.12345v1",
            "summary": "This is a test abstract.",
            "categories": ["cs.CV", "cs.AI"],
            "headline_zh": "这是一个测试标题",
            "intro_zh": ["要点1", "要点2", "要点3"],
            "tags_zh": ["测试", "示例"],
            "summary_zh": "这是中文摘要翻译。",
            "method_zh": "这是方法描述。",
            "code_links": [{"url": "https://github.com/test/repo", "type": "github"}],
        }
        
        md = render_paper_md(test_paper)
        print(f"✅ render_paper_md 测试: 生成 {len(md)} 字符的 Markdown")
        print(f"   包含标题: {'# Test Paper Title' in md}")
        print(f"   包含代码链接: {'GITHUB' in md}")
        print(f"   包含中文摘要: {'中文摘要' in md or '摘要（中文）' in md}")
        
    except Exception as e:
        print(f"❌ 页面生成测试失败: {e}")


async def main():
    print("\n" + "🚀" * 20)
    print("      arXiv Daily 功能测试")
    print("🚀" * 20 + "\n")
    
    # 测试 1: 论文抓取
    papers = test_scraper()
    
    # 测试 2: 代码链接提取
    test_code_extraction()
    
    # 测试 3: AI 分析
    await test_ai_analysis(papers)
    
    # 测试 4: 页面生成
    test_page_build()
    
    print("\n" + "=" * 60)
    print("🎉 测试完成!")
    print("=" * 60)
    print("\n如果所有测试通过，你可以运行完整流程:")
    print("  python main.py          # 抓取并分析今日论文")
    print("  python build_page.py    # 生成网站页面")


if __name__ == "__main__":
    asyncio.run(main())

