---
layout: default
title: Adaptive Residual-Update Steering for Low-Overhead Hallucination Mitigation in Large Vision Language Models
---

# Adaptive Residual-Update Steering for Low-Overhead Hallucination Mitigation in Large Vision Language Models

**arXiv**: [2511.10292v1](https://arxiv.org/abs/2511.10292) | [PDF](https://arxiv.org/pdf/2511.10292.pdf)

**作者**: Zhengtao Zou, Ya Gao, Jiarui Guan, Bin Li, Pekka Marttinen

---

## 💡 一句话要点

**提出RUDDER框架以低开销缓解大视觉语言模型中的物体幻觉问题**

**关键词**: `大视觉语言模型` `物体幻觉缓解` `低开销推理` `自适应门控` `视觉证据提取`

## 📋 核心要点

1. 核心问题：大视觉语言模型常产生与视觉输入不一致的物体幻觉，影响可靠性。
2. 方法要点：通过CARD向量和自适应门控，在单次前向传播中注入视觉证据。
3. 实验或效果：在POPE和CHAIR基准上性能媲美SOTA，计算延迟可忽略。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) often suffer from object hallucination, generating text inconsistent with visual inputs, which can critically undermine their reliability. Existing inference-time interventions to mitigate this issue present a challenging trade-off: while methods that steer internal states or adjust output logits can be effective, they often incur substantial computational overhead, typically requiring extra forward passes. This efficiency bottleneck can limit their practicality for real-world, latency-sensitive deployments. In this work, we aim to address this trade-off with Residual-Update Directed DEcoding Regulation (RUDDER), a low-overhead framework that steers LVLMs towards visually-grounded generation. RUDDER is built on two key innovations: (1) Contextual Activation Residual Direction (CARD) vector, a per-sample visual evidence vector extracted from the residual update of a self-attention layer during a single, standard forward pass. (2) A Bayesian-inspired adaptive gate that performs token-wise injection, applying a corrective signal whose strength is conditioned on the model's deviation from the visual context. Extensive experiments on key hallucination benchmarks, including POPE and CHAIR, indicate that RUDDER achieves performance comparable to state-of-the-art methods while introducing negligible computational latency, validating RUDDER as a pragmatic and effective approach for improving LVLMs' reliability without a significant compromise on efficiency.

