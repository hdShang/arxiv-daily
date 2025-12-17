---
layout: default
title: Frequency-Aware Token Reduction for Efficient Vision Transformer
---

# Frequency-Aware Token Reduction for Efficient Vision Transformer

**arXiv**: [2511.21477v1](https://arxiv.org/abs/2511.21477) | [PDF](https://arxiv.org/pdf/2511.21477.pdf)

**作者**: Dong-Jae Lee, Jiwan Hur, Jaehyun Choi, Jaemyung Yu, Junmo Kim

---

## 💡 一句话要点

**提出频率感知令牌缩减策略以提升视觉Transformer效率并缓解秩崩溃**

**关键词**: `视觉Transformer` `令牌缩减` `频率感知` `计算效率` `秩崩溃缓解`

## 📋 核心要点

1. 核心问题：视觉Transformer的二次计算复杂性和自注意力中的秩崩溃与过平滑现象。
2. 方法要点：将令牌分为高频和低频，保留高频令牌，聚合低频令牌为紧凑直流令牌。
3. 实验或效果：显著提高准确性，减少计算开销，并缓解秩崩溃与过平滑。

## 📄 摘要（原文）

> Vision Transformers have demonstrated exceptional performance across various computer vision tasks, yet their quadratic computational complexity concerning token length remains a significant challenge. To address this, token reduction methods have been widely explored. However, existing approaches often overlook the frequency characteristics of self-attention, such as rank collapsing and over-smoothing phenomenon. In this paper, we propose a frequency-aware token reduction strategy that improves computational efficiency while preserving performance by mitigating rank collapsing. Our method partitions tokens into high-frequency tokens and low-frequency tokens. high-frequency tokens are selectively preserved, while low-frequency tokens are aggregated into a compact direct current token to retain essential low-frequency components. Through extensive experiments and analysis, we demonstrate that our approach significantly improves accuracy while reducing computational overhead and mitigating rank collapsing and over smoothing. Furthermore, we analyze the previous methods, shedding light on their implicit frequency characteristics and limitations.

