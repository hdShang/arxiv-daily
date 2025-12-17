---
layout: default
title: Insert In Style: A Zero-Shot Generative Framework for Harmonious Cross-Domain Object Composition
---

# Insert In Style: A Zero-Shot Generative Framework for Harmonious Cross-Domain Object Composition

**arXiv**: [2511.15197v1](https://arxiv.org/abs/2511.15197) | [PDF](https://arxiv.org/pdf/2511.15197.pdf)

**作者**: Raghu Vamsi Chittersu, Yuvraj Singh Rathore, Pranav Adlinge, Kunal Swami

---

## 💡 一句话要点

**提出零样本生成框架Insert In Style，解决真实对象插入风格化域时的和谐组合问题。**

**关键词**: `零样本生成` `对象组合` `风格化域` `解耦表示` `掩码注意力` `生成框架`

## 📋 核心要点

1. 核心问题：现有方法在真实对象插入风格化域时，缺乏生成保真度或需不切实际的在线微调。
2. 方法要点：采用多阶段训练协议和掩码注意力架构，实现身份、风格和组合的解耦。
3. 实验或效果：在公共基准上实现最先进性能，身份和风格指标显著优于现有方法。

## 📄 摘要（原文）

> Reference-based object composition methods fail when inserting real-world objects into stylized domains. This under-explored problem is currently split between practical "blenders" that lack generative fidelity and "generators" that require impractical, per-subject online finetuning. In this work, we introduce Insert In Style, the first zero-shot generative framework that is both practical and high-fidelity. Our core contribution is a unified framework with two key innovations: (i) a novel multi-stage training protocol that disentangles representations for identity, style, and composition, and (ii) a specialized masked-attention architecture that surgically enforces this disentanglement during generation. This approach prevents the concept interference common in general-purpose, unified-attention models. Our framework is trained on a new 100k sample dataset, curated from a novel data pipeline. This pipeline couples large-scale generation with a rigorous, two-stage filtering process to ensure both high-fidelity semantic identity and style coherence. Unlike prior work, our model is truly zero-shot and requires no text prompts. We also introduce a new public benchmark for stylized composition. We demonstrate state-of-the-art performance, significantly outperforming existing methods on both identity and style metrics, a result strongly corroborated by user studies.

