---
layout: default
title: AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers
---

# AMS-KV: Adaptive KV Caching in Multi-Scale Visual Autoregressive Transformers

**arXiv**: [2511.16047v1](https://arxiv.org/abs/2511.16047) | [PDF](https://arxiv.org/pdf/2511.16047.pdf)

**作者**: Boxun Xu, Yu Wang, Zihu Wang, Peng Li

---

## 💡 一句话要点

**提出AMS-KV自适应KV缓存策略以优化多尺度视觉自回归模型的扩展性**

**关键词**: `视觉自回归建模` `KV缓存优化` `多尺度图像生成` `自注意力机制` `计算效率提升`

## 📋 核心要点

1. 多尺度视觉自回归模型中KV缓存内存随尺度增加而过度增长，限制扩展性
2. 基于局部尺度和凝聚尺度优先存储KV，并通过层间相似性分析优化缓存利用
3. 实验显示KV缓存使用减少84.83%，自注意力延迟降低60.48，支持更大批次生成

## 📄 摘要（原文）

> Visual autoregressive modeling (VAR) via next-scale prediction has emerged as a scalable image generation paradigm. While Key and Value (KV) caching in large language models (LLMs) has been extensively studied, next-scale prediction presents unique challenges, and KV caching design for next-scale based VAR transformers remains largely unexplored. A major bottleneck is the excessive KV memory growth with the increasing number of scales-severely limiting scalability. Our systematic investigation reveals that: (1) Attending to tokens from local scales significantly contributes to generation quality (2) Allocating a small amount of memory for the coarsest scales, termed as condensed scales, stabilizes multi-scale image generation (3) Strong KV similarity across finer scales is predominantly observed in cache-efficient layers, whereas cache-demanding layers exhibit weaker inter-scale similarity. Based on the observations, we introduce AMS-KV, a scale-adaptive KV caching policy for next-scale prediction in VAR models. AMS-KV prioritizes storing KVs from condensed and local scales, preserving the most relevant tokens to maintain generation quality. It further optimizes KV cache utilization and computational efficiency identifying cache-demanding layers through inter-scale similarity analysis. Compared to the vanilla next-scale prediction-based VAR models, AMS-KV reduces KV cache usage by up to 84.83% and self-attention latency by 60.48%. Moreover, when the baseline VAR-d30 model encounters out-of-memory failures at a batch size of 128, AMS-KV enables stable scaling to a batch size of 256 with improved throughput.

