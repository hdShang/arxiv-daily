#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
历史数据获取脚本

用法:
    python fetch_history.py --months-ago 1              # 获取1个月前的数据
    python fetch_history.py --months-ago 3              # 获取3个月前的数据
    python fetch_history.py --months-ago 6 --days 7     # 获取6个月前一周的数据
    python fetch_history.py --date 2024-06-15           # 获取指定日期的数据
    python fetch_history.py --month 2024-06              # 获取整个月的数据
    python fetch_history.py --months-ago 1 --skip-ai    # 跳过AI分析
    
注意:
    - arXiv 对历史查询有速率限制，建议每次获取不超过7天的数据
    - 周末和节假日 arXiv 不更新，会自动跳过
"""

import argparse
import asyncio
import json
import os
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
from typing import List, Tuple, Dict
from calendar import monthrange

from utils.scrapy import load_tags, query_arxiv, filter_by_interests
from utils.analyser import update_ai_summary_async

US_EASTERN = ZoneInfo("US/Eastern")


def get_month_date_range(year: int, month: int) -> Tuple[datetime, datetime]:
    """获取指定月份的起止日期"""
    start = datetime(year, month, 1, 0, 0, 0, tzinfo=US_EASTERN)
    days_in_month = monthrange(year, month)[1]
    end = datetime(year, month, days_in_month, 23, 59, 59, tzinfo=US_EASTERN)
    return start, end


def get_date_range_from_months_ago(months_ago: int, days: int = 7) -> Tuple[datetime, datetime, str]:
    """
    获取 N 个月前的日期范围
    
    Args:
        months_ago: 几个月前
        days: 获取多少天的数据（默认7天）
    
    Returns:
        (start_date, end_date, label_date)
    """
    now = datetime.now(US_EASTERN)
    
    # 计算目标月份
    target_year = now.year
    target_month = now.month - months_ago
    
    while target_month <= 0:
        target_month += 12
        target_year -= 1
    
    # 默认取该月中旬（避开月初月末的边界问题）
    target_day = min(15, monthrange(target_year, target_month)[1])
    
    # 计算日期范围
    end_date = datetime(target_year, target_month, target_day, 20, 0, 0, tzinfo=US_EASTERN)
    start_date = end_date - timedelta(days=days)
    
    label_date = end_date.strftime("%Y-%m-%d")
    
    return start_date, end_date, label_date


def get_date_range_from_date(date_str: str, days: int = 1) -> Tuple[datetime, datetime, str]:
    """
    从指定日期获取日期范围
    
    Args:
        date_str: 日期字符串 (YYYY-MM-DD)
        days: 获取多少天的数据
    
    Returns:
        (start_date, end_date, label_date)
    """
    target_date = datetime.strptime(date_str, "%Y-%m-%d")
    target_date = target_date.replace(hour=20, minute=0, second=0, tzinfo=US_EASTERN)
    
    end_date = target_date
    start_date = target_date - timedelta(days=days)
    
    label_date = target_date.strftime("%Y-%m-%d")
    
    return start_date, end_date, label_date


def get_month_weeks(year: int, month: int) -> List[Tuple[datetime, datetime, str]]:
    """
    获取指定月份的所有周（用于分批获取整月数据）
    
    Returns:
        List of (start_date, end_date, label_date)
    """
    start, end = get_month_date_range(year, month)
    
    weeks = []
    current_start = start
    
    while current_start <= end:
        current_end = min(current_start + timedelta(days=6), end)
        label = current_end.strftime("%Y-%m-%d")
        weeks.append((current_start, current_end, label))
        current_start = current_end + timedelta(days=1)
    
    return weeks


def format_arxiv_query_range(start: datetime, end: datetime) -> Tuple[str, str]:
    """格式化为 arXiv 查询格式"""
    fmt = "%Y%m%d%H%M"
    start_utc = start.astimezone(timezone.utc)
    end_utc = end.astimezone(timezone.utc)
    return start_utc.strftime(fmt), end_utc.strftime(fmt)


def fetch_papers_for_range(tags: List[str], start: datetime, end: datetime, 
                          max_results: int = 2000) -> Dict:
    """获取指定日期范围的论文"""
    start_str, end_str = format_arxiv_query_range(start, end)
    print(f"\n📅 查询日期范围: {start.strftime('%Y-%m-%d')} 至 {end.strftime('%Y-%m-%d')}")
    print(f"   UTC 时间: {start_str} 至 {end_str}")
    
    # 0 表示不限制，使用一个很大的数
    effective_max = max_results if max_results > 0 else 100000
    
    return query_arxiv(tags, (start_str, end_str), max_results=effective_max)


def main():
    parser = argparse.ArgumentParser(description="arXiv 历史数据获取工具")
    
    # 日期选择参数（互斥）
    date_group = parser.add_mutually_exclusive_group(required=True)
    date_group.add_argument("--months-ago", type=int, 
                           help="获取几个月前的数据 (1-24)")
    date_group.add_argument("--date", type=str,
                           help="获取指定日期的数据 (格式: YYYY-MM-DD)")
    date_group.add_argument("--month", type=str,
                           help="获取整个月的数据 (格式: YYYY-MM)")
    
    # 其他参数
    parser.add_argument("--days", type=int, default=7,
                       help="获取多少天的数据 (默认: 7)")
    parser.add_argument("--max-results", type=int, default=2000,
                       help="每次查询最大论文数 (默认: 2000，设为0表示不限制)")
    parser.add_argument("--tags-file", default="tags.json",
                       help="分类配置文件 (默认: tags.json)")
    parser.add_argument("--interests-file", default="interests.json",
                       help="兴趣配置文件 (默认: interests.json)")
    parser.add_argument("--no-filter", action="store_true",
                       help="不使用兴趣筛选")
    parser.add_argument("--skip-ai", action="store_true",
                       help="跳过AI分析")
    parser.add_argument("--concurrency", type=int, default=8,
                       help="AI分析并发数 (默认: 8)")
    parser.add_argument("--temperature", type=float, default=0.2,
                       help="AI生成温度 (默认: 0.2)")
    
    args = parser.parse_args()
    
    # 加载分类标签
    tags = load_tags(args.tags_file)
    print(f"[INFO] 目标分类: {tags}")
    
    # 确定日期范围
    if args.months_ago:
        if not 1 <= args.months_ago <= 24:
            print("❌ --months-ago 必须在 1-24 之间")
            return
        start, end, label_date = get_date_range_from_months_ago(args.months_ago, args.days)
        date_ranges = [(start, end, label_date)]
        print(f"\n📆 目标: {args.months_ago} 个月前，获取 {args.days} 天数据")
        
    elif args.date:
        start, end, label_date = get_date_range_from_date(args.date, args.days)
        date_ranges = [(start, end, label_date)]
        print(f"\n📆 目标: {args.date}，获取 {args.days} 天数据")
        
    elif args.month:
        try:
            year, month = map(int, args.month.split("-"))
            date_ranges = get_month_weeks(year, month)
            print(f"\n📆 目标: {args.month} 整月，分 {len(date_ranges)} 周获取")
        except ValueError:
            print("❌ --month 格式错误，应为 YYYY-MM")
            return
    
    # 获取论文
    all_papers = []
    
    for start, end, label_date in date_ranges:
        result = fetch_papers_for_range(tags, start, end, args.max_results)
        papers = result.get("papers", [])
        print(f"[INFO] 获取到 {len(papers)} 篇论文")
        all_papers.extend(papers)
    
    # 去重
    seen_ids = set()
    unique_papers = []
    for p in all_papers:
        arxiv_id = p.get("arxiv_id", "")
        if arxiv_id not in seen_ids:
            seen_ids.add(arxiv_id)
            unique_papers.append(p)
    
    print(f"\n[INFO] 总计获取 {len(unique_papers)} 篇唯一论文")
    
    if len(unique_papers) == 0:
        print("[WARN] 没有获取到论文，退出")
        return
    
    # 兴趣筛选
    if not args.no_filter:
        print(f"\n🎯 正在根据兴趣筛选论文...")
        unique_papers = filter_by_interests(unique_papers, args.interests_file)
    
    if len(unique_papers) == 0:
        print("[WARN] 筛选后没有匹配的论文，退出")
        return
    
    # 确定保存目录
    if args.month:
        save_label = args.month
    elif args.date:
        save_label = args.date
    else:
        save_label = label_date
    
    # 保存原始数据
    os.makedirs(f'data/{save_label}', exist_ok=True)
    arxiv_path = f'data/{save_label}/arxiv.json'
    
    save_data = {
        "count": len(unique_papers),
        "papers": unique_papers,
        "query_info": {
            "tags": tags,
            "date_ranges": [(s.isoformat(), e.isoformat(), l) for s, e, l in date_ranges],
            "filtered": not args.no_filter
        }
    }
    
    with open(arxiv_path, 'w', encoding='utf-8') as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)
    print(f"[OK] 保存原始数据: {arxiv_path}")
    
    # AI 分析
    if args.skip_ai:
        print("[INFO] 跳过AI分析")
        print(f"\n✅ 完成！数据保存在: data/{save_label}/")
        return
    
    print(f"\n🤖 正在进行 AI 分析...")
    print(f"[INFO] 并发数: {args.concurrency}, 温度: {args.temperature}")
    
    results = asyncio.run(update_ai_summary_async(
        metas=unique_papers,
        concurrency=args.concurrency,
        temperature=args.temperature
    ))
    
    # 保存AI分析结果
    ai_path = f'data/{save_label}/ai_summary.json'
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
    print(f"\n📁 数据目录: data/{save_label}/")
    print(f"   - arxiv.json       (原始数据)")
    print(f"   - ai_summary.json  (AI分析结果)")
    print(f"\n👉 运行 'python build_page.py' 生成网站页面")


if __name__ == '__main__':
    main()

