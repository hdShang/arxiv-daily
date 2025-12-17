#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
arXiv 论文日报抓取工具

用法:
    python main.py                           # 基础抓取（使用兴趣筛选）
    python main.py --no-filter               # 不使用兴趣筛选
    python main.py --thumbnails              # 抓取并获取缩略图
    python main.py --max-results 500         # 限制最大论文数
    python main.py --concurrency 16          # 提高AI分析并发数
"""

from utils.scrapy import load_tags, get_today_arxiv, filter_by_interests
from utils.analyser import update_ai_summary_async

import argparse
import asyncio
import json
import os


def main():
    parser = argparse.ArgumentParser(description="arXiv 论文日报抓取工具")
    parser.add_argument("--max-results", type=int, default=1000, 
                        help="最大抓取论文数 (默认: 1000)")
    parser.add_argument("--thumbnails", action="store_true",
                        help="抓取论文预览缩略图 (较慢)")
    parser.add_argument("--concurrency", type=int, default=8,
                        help="AI分析并发数 (默认: 8)")
    parser.add_argument("--temperature", type=float, default=0.2,
                        help="AI生成温度 (默认: 0.2)")
    parser.add_argument("--tags-file", default="tags.json",
                        help="分类配置文件 (默认: tags.json)")
    parser.add_argument("--interests-file", default="interests.json",
                        help="兴趣配置文件 (默认: interests.json)")
    parser.add_argument("--no-filter", action="store_true",
                        help="不使用兴趣筛选，抓取所有论文")
    parser.add_argument("--skip-ai", action="store_true",
                        help="跳过AI分析，仅抓取论文")
    args = parser.parse_args()

    # 加载分类标签
    tags = load_tags(args.tags_file)
    print(f"[INFO] 目标分类: {tags}")

    # 抓取论文
    print(f"\n📥 正在抓取 arXiv 论文...")
    result, label_date = get_today_arxiv(
        tags, 
        max_results=args.max_results,
        fetch_thumbnails=args.thumbnails
    )
    
    metas = result.get("papers", [])
    print(f"[INFO] 共抓取 {len(metas)} 篇论文")
    
    # 兴趣筛选
    if not args.no_filter:
        print(f"\n🎯 正在根据兴趣筛选论文...")
        metas = filter_by_interests(metas, args.interests_file)
        result["papers"] = metas
        result["count"] = len(metas)
        result["filtered"] = True
    
    # 保存原始数据
    os.makedirs(f'data/{label_date}', exist_ok=True)
    arxiv_path = f'data/{label_date}/arxiv.json'
    with open(arxiv_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[OK] 保存原始数据: {arxiv_path}")
    
    # 统计代码链接
    papers_with_code = sum(1 for p in metas if p.get("code_links"))
    if papers_with_code:
        print(f"[INFO] 其中 {papers_with_code} 篇论文包含代码链接")
    
    if args.thumbnails:
        papers_with_thumb = sum(1 for p in metas if p.get("thumbnail"))
        print(f"[INFO] 成功获取 {papers_with_thumb} 篇论文的预览图")
    
    if args.skip_ai:
        print("[INFO] 跳过AI分析")
        return
    
    if len(metas) == 0:
        print("[WARN] 没有匹配兴趣的论文，跳过AI分析")
        return
    
    # AI 分析（自动选择 API，支持故障转移）
    print(f"\n🤖 正在进行 AI 分析...")
    print(f"[INFO] 并发数: {args.concurrency}, 温度: {args.temperature}")
    
    results = asyncio.run(update_ai_summary_async(
        metas=metas, 
        concurrency=args.concurrency, 
        temperature=args.temperature
    ))
    
    # 保存AI分析结果
    ai_path = f'data/{label_date}/ai_summary.json'
    with open(ai_path, 'w', encoding='utf-8') as f:
        json.dump({"papers": results}, f, ensure_ascii=False, indent=4)
    print(f"[OK] 保存AI分析: {ai_path}")
    
    # 统计结果
    ok_count = sum(1 for r in results if "_model_error" not in r and "_parse_error" not in r)
    err_count = len(results) - ok_count
    
    print(f"\n✅ 完成！")
    print(f"   📄 论文数: {len(results)}")
    print(f"   ✓ 成功分析: {ok_count}")
    if err_count:
        print(f"   ✗ 分析失败: {err_count}")
    print(f"\n📁 数据目录: data/{label_date}/")
    print(f"   - arxiv.json       (原始数据)")
    print(f"   - ai_summary.json  (AI分析结果)")
    print(f"\n👉 运行 'python build_page.py' 生成网站页面")


if __name__ == '__main__':
    main()
