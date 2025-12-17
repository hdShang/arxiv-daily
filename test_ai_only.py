import asyncio
import os
from openai import AsyncOpenAI

async def test():
    client = AsyncOpenAI(
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")
    )
    
    print("🤖 测试 AI 分析功能...")
    print(f"   模型: {os.getenv('LLM_MODEL', 'gpt-4o-mini')}")
    
    # 简单的测试论文
    test_paper = {
        "title": "Attention Is All You Need",
        "summary": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms."
    }
    
    prompt = f"""请分析这篇论文，用中文输出JSON:
标题: {test_paper['title']}
摘要: {test_paper['summary']}

输出格式:
{{"headline_zh": "一句话总结", "tags_zh": ["关键词1", "关键词2"]}}"""

    resp = await client.chat.completions.create(
        model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        timeout=60,
    )
    
    print("\n✅ AI 分析成功！")
    print(f"\n📊 响应:\n{resp.choices[0].message.content}")

asyncio.run(test())
