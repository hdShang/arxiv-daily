---
layout: default
title: When Refusals Fail: Unstable Safety Mechanisms in Long-Context LLM Agents
---

# When Refusals Fail: Unstable Safety Mechanisms in Long-Context LLM Agents

**arXiv**: [2512.02445v1](https://arxiv.org/abs/2512.02445) | [PDF](https://arxiv.org/pdf/2512.02445.pdf)

**作者**: Tsimur Hadeliya, Mohammad Ali Jauhar, Nidhi Sakpal, Diogo Cruz

---

## 💡 一句话要点

**揭示长上下文LLM代理中安全机制的不稳定性及其对任务性能的影响**

**关键词**: `长上下文LLM代理` `安全机制不稳定性` `任务性能评估` `拒绝率分析` `多步任务安全`

## 📋 核心要点

1. 核心问题：长上下文LLM代理在任务性能和安全拒绝率上表现出不可预测的波动，现有评估范式存在局限
2. 方法要点：通过实验分析上下文长度、类型和位置对代理行为和拒绝率的影响
3. 实验或效果：在100K-200K令牌下，性能下降超50%，拒绝率变化显著，如GPT-4.1-nano从5%增至40%

## 📄 摘要（原文）

> Solving complex or long-horizon problems often requires large language models (LLMs) to use external tools and operate over a significantly longer context window. New LLMs enable longer context windows and support tool calling capabilities. Prior works have focused mainly on evaluation of LLMs on long-context prompts, leaving agentic setup relatively unexplored, both from capability and safety perspectives. Our work addresses this gap. We find that LLM agents could be sensitive to length, type, and placement of the context, exhibiting unexpected and inconsistent shifts in task performance and in refusals to execute harmful requests. Models with 1M-2M token context windows show severe degradation already at 100K tokens, with performance drops exceeding 50\% for both benign and harmful tasks. Refusal rates shift unpredictably: GPT-4.1-nano increases from $\sim$5\% to $\sim$40\% while Grok 4 Fast decreases from $\sim$80\% to $\sim$10\% at 200K tokens. Our work shows potential safety issues with agents operating on longer context and opens additional questions on the current metrics and paradigm for evaluating LLM agent safety on long multi-step tasks. In particular, our results on LLM agents reveal a notable divergence in both capability and safety performance compared to prior evaluations of LLMs on similar criteria.

