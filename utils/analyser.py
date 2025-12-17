import asyncio
import json, re, time, random, os
from typing import List, Dict, Any, Optional
from openai import AsyncOpenAI
from tqdm import tqdm

SYSTEM_PROMPT = open("utils/prompts/system.txt", "r", encoding="utf-8").read()
USER_TEMPLATE = open("utils/prompts/user.txt", "r", encoding="utf-8").read()

# ============== API 配置 ==============
# 支持多 API 配置，主 API 失败时自动切换到备用 API

API_CONFIGS = {
    "gemini": {
        "name": "Gemini",
        "env_key": "GEMINI_API_KEY",
        "env_base_url": "GEMINI_BASE_URL",
        "env_model": "GEMINI_MODEL",
        "default_base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "default_model": "gemini-2.0-flash",
        "supports_json_mode": False,  # Gemini OpenAI 兼容模式不支持 response_format
    },
    "openai": {
        "name": "OpenAI",
        "env_key": "OPENAI_API_KEY",
        "env_base_url": "OPENAI_BASE_URL",
        "env_model": "OPENAI_MODEL",
        "default_base_url": "https://api.openai.com/v1",
        "default_model": "gpt-4o-mini",
        "supports_json_mode": True,
    },
    "deepseek": {
        "name": "DeepSeek",
        "env_key": "DEEPSEEK_API_KEY",
        "env_base_url": "DEEPSEEK_BASE_URL",
        "env_model": "DEEPSEEK_MODEL",
        "default_base_url": "https://api.deepseek.com",
        "default_model": "deepseek-chat",
        "supports_json_mode": True,
    },
}

# 默认 API 优先级：Gemini -> OpenAI -> DeepSeek
DEFAULT_API_PRIORITY = ["gemini", "openai", "deepseek"]


def get_api_config(api_name: str) -> Optional[Dict[str, Any]]:
    """获取 API 配置"""
    config = API_CONFIGS.get(api_name)
    if not config:
        return None
    
    api_key = os.getenv(config["env_key"])
    if not api_key:
        return None
    
    return {
        "name": config["name"],
        "api_key": api_key,
        "base_url": os.getenv(config.get("env_base_url", ""), config["default_base_url"]),
        "model": os.getenv(config.get("env_model", ""), config["default_model"]),
        "supports_json_mode": config["supports_json_mode"],
    }


def get_available_apis(priority: List[str] = None) -> List[Dict[str, Any]]:
    """获取所有可用的 API 配置，按优先级排序"""
    priority = priority or DEFAULT_API_PRIORITY
    available = []
    for api_name in priority:
        config = get_api_config(api_name)
        if config:
            config["api_name"] = api_name
            available.append(config)
    return available


def create_client(config: Dict[str, Any]) -> AsyncOpenAI:
    """创建 API 客户端"""
    return AsyncOpenAI(
        api_key=config["api_key"],
        base_url=config["base_url"]
    )


# ============== 兼容旧接口 ==============

def get_client(api_key: str = None, base_url: str = None):
    """
    兼容旧接口：创建 OpenAI 兼容的异步客户端。
    优先使用环境变量 LLM_API_KEY/LLM_BASE_URL，
    否则按优先级自动选择可用的 API。
    """
    # 优先使用显式传入的参数或 LLM_ 环境变量
    api_key = api_key or os.getenv("LLM_API_KEY") or os.getenv("DEEPSEEK_API_KEY")
    base_url = base_url or os.getenv("LLM_BASE_URL")
    
    if api_key and base_url:
        return AsyncOpenAI(api_key=api_key, base_url=base_url)
    
    # 自动选择可用的 API
    available = get_available_apis()
    if not available:
        raise RuntimeError(
            "未找到可用的 API Key。请设置以下任一环境变量:\n"
            "  GEMINI_API_KEY, OPENAI_API_KEY, DEEPSEEK_API_KEY\n"
            "或使用 LLM_API_KEY + LLM_BASE_URL"
        )
    
    config = available[0]
    print(f"[INFO] 自动选择 API: {config['name']} ({config['model']})")
    return create_client(config)


def get_model() -> str:
    """获取模型名称"""
    # 优先使用 LLM_MODEL
    model = os.getenv("LLM_MODEL")
    if model:
        return model
    
    # 自动选择
    available = get_available_apis()
    if available:
        return available[0]["model"]
    
    return "deepseek-chat"


# ============== 核心函数 ==============

def get_prompt(user_prompt: str, meta: dict) -> str:
    title = (meta.get("title") or "No Title").strip()
    authors_list = meta.get("authors", [])
    if isinstance(authors_list, list):
        authors = ", ".join(a.strip() for a in authors_list) or "No Authors"
    else:
        authors = str(authors_list).strip() or "No Authors"
    summary = (meta.get("summary") or "No Summary").strip()
    prompt = (user_prompt
              .replace("{title}", title)
              .replace("{authors}", authors)
              .replace("{summary}", summary))
    return prompt


def _parse_json_safely(text: str) -> Dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        m = re.search(r'(\{[\s\S]*\})', text)
        if m:
            try:
                return json.loads(m.group(1))
            except json.JSONDecodeError:
                return {"_parse_error": "failed to decode extracted JSON", "_raw": text[:500]}
        else:
            return {"_parse_error": "no json object found", "_raw": text[:500]}


async def _call_single_api(
    config: Dict[str, Any],
    prompt: str,
    temperature: float = 0.2,
    timeout: int = 120,
) -> Dict[str, Any]:
    """调用单个 API，返回结果或错误"""
    client = create_client(config)
    
    request_params = {
        "model": config["model"],
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
        "timeout": timeout,
    }
    
    if config["supports_json_mode"]:
        request_params["response_format"] = {"type": "json_object"}
    
    resp = await client.chat.completions.create(**request_params)
    text = resp.choices[0].message.content
    if not isinstance(text, str):
        text = str(text)
    
    return _parse_json_safely(text)


async def _one_call_with_fallback(
    meta: Dict[str, Any],
    sem: asyncio.Semaphore,
    idx: int,
    available_apis: List[Dict[str, Any]],
    max_retries: int = 2,
    temperature: float = 0.2,
    request_timeout: int = 120,
) -> Dict[str, Any]:
    """
    调用 API，支持自动故障转移。
    主 API 失败后自动尝试备用 API。
    """
    prompt = get_prompt(USER_TEMPLATE, meta)
    last_error = None
    used_api = None
    
    for api_config in available_apis:
        api_name = api_config.get("api_name", api_config["name"])
        backoff = 1.0
        
        for attempt in range(1, max_retries + 1):
            async with sem:
                try:
                    result = await _call_single_api(
                        api_config, prompt, temperature, request_timeout
                    )
                    
                    # 检查是否解析成功
                    if "_parse_error" not in result:
                        merged = {**meta, **result, "_index": idx, "_used_api": api_name}
                        return merged
                    else:
                        last_error = f"{api_name}: JSON解析失败"
                        # 解析失败，尝试下一个 API
                        break
                        
                except Exception as e:
                    last_error = f"{api_name}: {type(e).__name__}: {str(e)[:100]}"
                    if attempt == max_retries:
                        # 当前 API 重试次数用完，尝试下一个 API
                        break
                    await asyncio.sleep(backoff + random.uniform(0, 0.5))
                    backoff *= 1.5
    
    # 所有 API 都失败
    return {**meta, "_index": idx, "_model_error": last_error or "All APIs failed"}


async def update_ai_summary_async(
    client: AsyncOpenAI = None,  # 保留兼容性，但不再使用
    metas: List[Dict[str, Any]] = None,
    concurrency: int = 8,
    temperature: float = 0.2,
    model: str = None,  # 保留兼容性
) -> List[Dict[str, Any]]:
    """
    并发调用 LLM API，显示 tqdm 进度。
    自动选择可用 API，主 API 失败时自动切换到备用 API。
    """
    if metas is None:
        metas = []
    
    # 获取可用 API
    available_apis = get_available_apis()
    if not available_apis:
        raise RuntimeError("未找到可用的 API Key")
    
    primary_api = available_apis[0]
    print(f"[INFO] 主 API: {primary_api['name']} ({primary_api['model']})")
    if len(available_apis) > 1:
        fallback_names = [a['name'] for a in available_apis[1:]]
        print(f"[INFO] 备用 API: {', '.join(fallback_names)}")
    
    sem = asyncio.Semaphore(concurrency)
    tasks = [
        asyncio.create_task(
            _one_call_with_fallback(
                meta, sem, idx=i, 
                available_apis=available_apis,
                temperature=temperature
            )
        )
        for i, meta in enumerate(metas)
    ]

    results = [None] * len(metas)
    ok = err = 0
    api_usage = {}  # 统计各 API 使用次数
    t0 = time.time()

    desc = f"LLM ({primary_api['name']})"
    for fut in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc=desc, unit="paper"):
        try:
            item = await fut
            i = item.get("_index", None)
            if i is not None and 0 <= i < len(results):
                results[i] = item
            else:
                results.append(item)
            
            # 统计
            if "_model_error" in item or "_parse_error" in item:
                err += 1
            else:
                ok += 1
                used = item.get("_used_api", "unknown")
                api_usage[used] = api_usage.get(used, 0) + 1
                
        except Exception as e:
            err += 1

    for i, v in enumerate(results):
        if v is None:
            results[i] = {**metas[i], "_index": i, "_model_error": "TaskMissing"}

    # 打印统计
    print(f"\n[统计] 成功: {ok}, 失败: {err}")
    if api_usage:
        usage_str = ", ".join([f"{k}: {v}" for k, v in api_usage.items()])
        print(f"[统计] API 使用分布: {usage_str}")

    return results


if __name__ == '__main__':
    # 测试
    print("=== API 配置检查 ===")
    available = get_available_apis()
    if available:
        for api in available:
            print(f"  ✅ {api['name']}: {api['model']} @ {api['base_url']}")
    else:
        print("  ❌ 未找到可用的 API Key")
