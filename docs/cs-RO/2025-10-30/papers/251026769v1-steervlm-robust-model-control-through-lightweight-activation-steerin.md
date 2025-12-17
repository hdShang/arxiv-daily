---
layout: default
title: SteerVLM: Robust Model Control through Lightweight Activation Steering for Vision Language Models
---

# SteerVLM: Robust Model Control through Lightweight Activation Steering for Vision Language Models

**arXiv**: [2510.26769v1](https://arxiv.org/abs/2510.26769) | [PDF](https://arxiv.org/pdf/2510.26769.pdf)

**作者**: Anushka Sivakumar, Andrew Zhang, Zaber Hakim, Chris Thomas

---

## 💡 一句话要点

**提出SteerVLM轻量激活引导模块，以增强视觉语言模型的指令遵循能力。**

**关键词**: `视觉语言模型` `激活引导` `轻量控制` `推理时干预` `多模态数据集`

## 📋 核心要点

1. 核心问题：视觉语言模型输出难以精确遵循复杂指令，需轻量控制方法。
2. 方法要点：学习配对提示嵌入，动态调整激活，实现推理时细粒度语义控制。
3. 实验或效果：在引导和幻觉缓解基准上优于现有方法，参数仅占原模型0.14%。

## 📄 摘要（原文）

> This work introduces SteerVLM, a lightweight steering module designed to
> guide Vision-Language Models (VLMs) towards outputs that better adhere to
> desired instructions. Our approach learns from the latent embeddings of paired
> prompts encoding target and converse behaviors to dynamically adjust
> activations connecting the language modality with image context. This allows
> for fine-grained, inference-time control over complex output semantics without
> modifying model weights while preserving performance on off-target tasks. Our
> steering module requires learning parameters equal to 0.14% of the original
> VLM's size. Our steering module gains model control through dimension-wise
> activation modulation and adaptive steering across layers without requiring
> pre-extracted static vectors or manual tuning of intervention points.
> Furthermore, we introduce VNIA (Visual Narrative Intent Alignment), a
> multimodal dataset specifically created to facilitate the development and
> evaluation of VLM steering techniques. Our method outperforms existing
> intervention techniques on steering and hallucination mitigation benchmarks for
> VLMs and proposes a robust solution for multimodal model control through
> activation engineering.

