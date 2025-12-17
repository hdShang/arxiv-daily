---
layout: default
title: Subjective Depth and Timescale Transformers: Learning Where and When to Compute
---

# Subjective Depth and Timescale Transformers: Learning Where and When to Compute

**arXiv**: [2511.21408v1](https://arxiv.org/abs/2511.21408) | [PDF](https://arxiv.org/pdf/2511.21408.pdf)

**作者**: Frederico Wieser, Martin Benfeghoul, Haitham Bou Ammar, Jun Wang, Zafeirios Fountas

---

## 💡 一句话要点

**提出主观深度与时间尺度Transformer，通过动态路由计算提升Transformer效率。**

**关键词**: `Transformer架构` `动态计算路由` `贝叶斯惊喜` `KV缓存优化` `条件计算` `效率提升`

## 📋 核心要点

1. 标准Transformer计算分配僵化，限制大模型和长序列效率。
2. SDT和STT利用贝叶斯惊喜信号动态路由，学习计算位置和时间。
3. 实验显示自注意力计算减少75%，KV缓存需求降低50%。

## 📄 摘要（原文）

> The rigid, uniform allocation of computation in standard Transformer (TF) architectures can limit their efficiency and scalability, particularly for large-scale models and long sequences. Addressing this, we introduce Subjective Depth Transformers (SDT) and Subjective Timescale Transformers (STT), two distinct architectures that leverage Bayesian surprise signals to dynamically route computation, learning where and when to compute within decoder-only TFs. SDT augments a decoder-only stack with alternating Decision and Dynamic layers: a Decision layer computes a full block 'posterior' and a lightweight 'prior,' while a Dynamic layer employs fixed-capacity Top-K routing based on Bayesian surprise (Expected and Unexpected Change), maintaining a static compute graph. STT extends this conditional computation to the temporal domain: a transition network predicts residual updates, forming a temporal 'change hypothesis' that informs a router to dynamically execute or bypass TF blocks for each token, managing KV-cache contributions. Both architectures exhibit the predicted shift from novelty to prediction driven gating over training, suggesting alignment with surprise based principles. While operating at reduced capacity, they offer preliminary insights into the compute-accuracy trade-offs of conditional computation. The proposed architectures establish a flexible framework for efficiency, reducing self-attention computation by 75% and KV-cache requirements by 50% within each compute skipping layer, setting a pathway for more efficient models.

