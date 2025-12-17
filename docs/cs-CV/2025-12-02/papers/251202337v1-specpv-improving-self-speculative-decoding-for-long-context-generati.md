---
layout: default
title: SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification
---

# SpecPV: Improving Self-Speculative Decoding for Long-Context Generation via Partial Verification

**arXiv**: [2512.02337v1](https://arxiv.org/abs/2512.02337) | [PDF](https://arxiv.org/pdf/2512.02337.pdf)

**作者**: Zhendong Tan, Xingjun Zhang, Chaoyi Hu, Junjie Peng, Kun Xia

---

## 💡 一句话要点

**提出SpecPV自推测解码方法，通过部分验证加速长上下文生成中的推测解码。**

**关键词**: `长上下文生成` `推测解码` `自推测解码` `部分验证` `键值状态` `解码加速`

## 📋 核心要点

1. 长上下文生成中推测解码的验证步骤成为主要瓶颈。
2. 采用部分键值状态进行快速验证，并定期全验证以纠正累积错误。
3. 在LLaMA-3.1-8B-Instruct等模型上实现最高6倍解码加速，性能略有下降。

## 📄 摘要（原文）

> Growing demands from tasks like code generation, deep reasoning, and long-document understanding have made long-context generation a crucial capability for large language models (LLMs). Speculative decoding is one of the most direct and effective approaches for accelerating generation. It follows a draft-verify paradigm, where a lightweight draft model proposes several candidate tokens and the target model verifies them. However, we find that as the context length grows, verification becomes the dominant bottleneck. To further accelerate speculative decoding in long-context generation, we introduce SpecPV, a self-speculative decoding approach that performs fast verification using partial key-value states (KV) and periodically applies full verification to eliminate accumulated errors. We validate SpecPV across multiple long-context benchmarks and models, including LLaMA-3.1-8B-Instruct and Qwen3-series. Experimental results show that SpecPV achieves up to 6x decoding speedup over standard autoregressive decoding with minor degradation.

