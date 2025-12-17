#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API 效果对比测试脚本
对比 DeepSeek、OpenAI、Gemini 三个 API 的论文分析效果
"""

import asyncio
import json
import os
import time
from pathlib import Path
from typing import Dict, Any, List
from openai import AsyncOpenAI

# 加载 prompts
SYSTEM_PROMPT = open("utils/prompts/system.txt", "r", encoding="utf-8").read()
USER_TEMPLATE = open("utils/prompts/user.txt", "r", encoding="utf-8").read()

# API 配置
# 支持环境变量覆盖：
#   {API}_API_KEY  - API 密钥
#   {API}_BASE_URL - API 地址（可选）
#   {API}_MODEL    - 模型名称（可选）
API_CONFIGS = {
    "deepseek": {
        "name": "DeepSeek",
        "default_base_url": "https://api.deepseek.com",
        "default_model": "deepseek-chat",
        "env_key": "DEEPSEEK_API_KEY",
        "env_base_url": "DEEPSEEK_BASE_URL",
        "env_model": "DEEPSEEK_MODEL",
        "supports_json_mode": True,
    },
    "openai": {
        "name": "OpenAI",
        "default_base_url": "https://api.openai.com/v1",
        "default_model": "gpt-4o-mini",
        "env_key": "OPENAI_API_KEY",
        "env_base_url": "OPENAI_BASE_URL",
        "env_model": "OPENAI_MODEL",
        "supports_json_mode": True,
    },
    "gemini": {
        "name": "Gemini",
        "default_base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "default_model": "gemini-2.0-flash",
        "env_key": "GEMINI_API_KEY",
        "env_base_url": "GEMINI_BASE_URL",
        "env_model": "GEMINI_MODEL",
        "supports_json_mode": False,  # Gemini OpenAI 兼容模式不支持
    },
}


def get_api_config(api_name: str) -> dict:
    """获取 API 配置，支持环境变量覆盖"""
    config = API_CONFIGS.get(api_name, {})
    if not config:
        return {}
    
    return {
        "name": config["name"],
        "api_key": os.getenv(config["env_key"]),
        "base_url": os.getenv(config.get("env_base_url", ""), config["default_base_url"]),
        "model": os.getenv(config.get("env_model", ""), config["default_model"]),
        "supports_json_mode": config["supports_json_mode"],
        "env_key": config["env_key"],
    }


def get_prompt(meta: dict) -> str:
    """构建 prompt"""
    title = (meta.get("title") or "No Title").strip()
    authors_list = meta.get("authors", [])
    if isinstance(authors_list, list):
        authors = ", ".join(a.strip() for a in authors_list) or "No Authors"
    else:
        authors = str(authors_list).strip() or "No Authors"
    summary = (meta.get("summary") or "No Summary").strip()
    prompt = (USER_TEMPLATE
              .replace("{title}", title)
              .replace("{authors}", authors)
              .replace("{summary}", summary))
    return prompt


def parse_json_safely(text: str) -> Dict[str, Any]:
    """安全解析 JSON"""
    import re
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r'(\{[\s\S]*\})', text)
        if m:
            try:
                return json.loads(m.group(1))
            except json.JSONDecodeError:
                return {"_parse_error": "failed", "_raw": text[:500]}
        return {"_parse_error": "no json", "_raw": text[:500]}


async def call_api(
    api_name: str,
    paper: dict,
    timeout: int = 60
) -> Dict[str, Any]:
    """调用单个 API 分析论文"""
    config = get_api_config(api_name)
    
    if not config.get("api_key"):
        return {
            "api": api_name,
            "success": False,
            "error": f"Missing API key: {config.get('env_key', 'unknown')}",
            "time": 0,
        }
    
    client = AsyncOpenAI(
        api_key=config["api_key"],
        base_url=config["base_url"]
    )
    
    prompt = get_prompt(paper)
    
    start_time = time.time()
    try:
        request_params = {
            "model": config["model"],
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
            "timeout": timeout,
        }
        
        if config["supports_json_mode"]:
            request_params["response_format"] = {"type": "json_object"}
        
        resp = await client.chat.completions.create(**request_params)
        text = resp.choices[0].message.content
        elapsed = time.time() - start_time
        
        result = parse_json_safely(text)
        
        is_success = "_parse_error" not in result
        response = {
            "api": api_name,
            "model": config["model"],
            "base_url": config["base_url"],
            "success": is_success,
            "time": round(elapsed, 2),
            "result": result,
        }
        
        # 如果解析失败，设置错误信息
        if not is_success:
            response["error"] = f"JSON解析失败: {result.get('_parse_error', 'unknown')}"
        
        return response
    except Exception as e:
        elapsed = time.time() - start_time
        return {
            "api": api_name,
            "model": config["model"],
            "base_url": config["base_url"],
            "success": False,
            "error": f"{type(e).__name__}: {str(e)[:200]}",
            "time": round(elapsed, 2),
        }


async def compare_apis(paper: dict, apis: List[str] = None) -> Dict[str, Any]:
    """对比多个 API 的分析结果"""
    if apis is None:
        apis = list(API_CONFIGS.keys())
    
    tasks = []
    for api_name in apis:
        if api_name in API_CONFIGS:
            tasks.append(call_api(api_name, paper))
    
    results = await asyncio.gather(*tasks)
    return {r["api"]: r for r in results}


def print_comparison(paper: dict, results: Dict[str, Any]):
    """打印对比结果"""
    print("\n" + "="*80)
    print(f"📄 论文: {paper.get('title', 'Unknown')[:70]}...")
    print(f"   arXiv: {paper.get('arxiv_id', 'Unknown')}")
    print("="*80)
    
    for api_name, result in results.items():
        config = get_api_config(api_name)
        print(f"\n{'─'*40}")
        print(f"🔹 {config.get('name', api_name)} ({result.get('model', 'unknown')})")
        print(f"   🌐 {result.get('base_url', 'unknown')}")
        print(f"   ⏱️  耗时: {result.get('time', 0):.2f}s")
        
        if result.get("success"):
            r = result.get("result", {})
            print(f"   ✅ 成功")
            print(f"\n   📌 一句话要点:")
            print(f"      {r.get('headline_zh', 'N/A')}")
            
            intro = r.get("intro_zh", [])
            if intro:
                print(f"\n   📋 核心要点:")
                for i, point in enumerate(intro[:3], 1):
                    print(f"      {i}. {point[:80]}...")
            
            tags = r.get("tags_zh", [])
            if tags:
                print(f"\n   🏷️  标签: {', '.join(tags[:5])}")
        else:
            error_msg = result.get('error', 'Unknown error')
            print(f"   ❌ 失败: {error_msg}")
            # 显示解析错误详情
            r = result.get("result", {})
            if r.get("_parse_error"):
                print(f"   📝 解析错误: {r.get('_parse_error')}")
                raw = r.get("_raw", "")
                if raw:
                    print(f"   📝 原始响应: {raw[:200]}...")
    
    print("\n" + "="*80)


def load_sample_papers(data_dir: str = "data", num_papers: int = 3) -> List[dict]:
    """加载示例论文"""
    data_path = Path(data_dir)
    
    # 找最新的日期目录
    date_dirs = sorted(data_path.glob("*/ai_summary.json"), reverse=True)
    if not date_dirs:
        date_dirs = sorted(data_path.glob("*/arxiv.json"), reverse=True)
    
    if not date_dirs:
        print("❌ 未找到数据文件")
        return []
    
    json_path = date_dirs[0]
    print(f"📂 加载数据: {json_path}")
    
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    papers = data.get("papers", [])
    if not papers:
        print("❌ 未找到论文数据")
        return []
    
    # 返回指定数量的论文
    return papers[:num_papers]


async def main():
    """主函数"""
    import argparse
    
    parser = argparse.ArgumentParser(description="对比不同 API 的论文分析效果")
    parser.add_argument("--apis", nargs="+", default=["deepseek", "openai", "gemini"],
                        help="要测试的 API 列表")
    parser.add_argument("--num", type=int, default=2,
                        help="测试论文数量 (默认 2)")
    parser.add_argument("--output", type=str, default=None,
                        help="输出 JSON 文件路径")
    args = parser.parse_args()
    
    print("\n" + "🚀"*20)
    print("      API 效果对比测试")
    print("🚀"*20 + "\n")
    
    # 检查 API Keys
    print("📋 API 配置检查:")
    available_apis = []
    for api_name in args.apis:
        if api_name not in API_CONFIGS:
            print(f"   ❌ {api_name}: 未知 API")
            continue
        
        config = get_api_config(api_name)
        if config.get("api_key"):
            print(f"   ✅ {config['name']}:")
            print(f"      Key: {config['env_key']} ✓")
            print(f"      URL: {config['base_url']}")
            print(f"      Model: {config['model']}")
            available_apis.append(api_name)
        else:
            print(f"   ⚠️  {config['name']}: {API_CONFIGS[api_name]['env_key']} 未设置")
    
    if not available_apis:
        print("\n❌ 没有可用的 API，请设置至少一个 API Key")
        print("\n示例:")
        print("  export DEEPSEEK_API_KEY='sk-xxx'")
        print("  export OPENAI_API_KEY='sk-xxx'")
        print("  export GEMINI_API_KEY='xxx'")
        return
    
    # 加载论文
    papers = load_sample_papers(num_papers=args.num)
    if not papers:
        return
    
    print(f"\n📄 将测试 {len(papers)} 篇论文，使用 {len(available_apis)} 个 API\n")
    
    all_results = []
    
    for i, paper in enumerate(papers, 1):
        print(f"\n[{i}/{len(papers)}] 正在分析...")
        results = await compare_apis(paper, available_apis)
        print_comparison(paper, results)
        
        all_results.append({
            "paper": {
                "title": paper.get("title"),
                "arxiv_id": paper.get("arxiv_id"),
            },
            "results": results
        })
    
    # 统计汇总
    print("\n" + "📊"*20)
    print("      统计汇总")
    print("📊"*20)
    
    for api_name in available_apis:
        config = API_CONFIGS[api_name]
        api_results = [r["results"].get(api_name, {}) for r in all_results]
        success_count = sum(1 for r in api_results if r.get("success"))
        avg_time = sum(r.get("time", 0) for r in api_results) / max(len(api_results), 1)
        
        print(f"\n{config['name']}:")
        print(f"   成功率: {success_count}/{len(api_results)}")
        print(f"   平均耗时: {avg_time:.2f}s")
    
    # 保存结果
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(all_results, f, ensure_ascii=False, indent=2)
        print(f"\n💾 结果已保存到: {args.output}")
    
    print("\n✅ 测试完成!")


if __name__ == "__main__":
    asyncio.run(main())

