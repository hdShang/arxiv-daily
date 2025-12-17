---
layout: default
title: Chain-of-Image Generation: Toward Monitorable and Controllable Image Generation
---

# Chain-of-Image Generation: Toward Monitorable and Controllable Image Generation

**arXiv**: [2512.08645v1](https://arxiv.org/abs/2512.08645) | [PDF](https://arxiv.org/pdf/2512.08645.pdf)

**作者**: Young Kyung Kim, Oded Schlesinger, Yuzhou Zhao, J. Matias Di Martino, Guillermo Sapiro

---

## 💡 一句话要点

**提出链式图像生成框架以增强图像生成的可监控性和可控性**

**关键词**: `图像生成` `可监控性` `可控性` `链式推理` `语义分解` `模型无关框架`

## 📋 核心要点

1. 核心问题：现有图像生成模型内部过程不透明，限制监控、干预和可靠性。
2. 方法要点：利用大语言模型分解提示为逐步指令，实现语义序列化生成。
3. 实验或效果：通过新指标评估监控性，提升组合鲁棒性，框架模型无关。

## 📄 摘要（原文）

> While state-of-the-art image generation models achieve remarkable visual quality, their internal generative processes remain a "black box." This opacity limits human observation and intervention, and poses a barrier to ensuring model reliability, safety, and control. Furthermore, their non-human-like workflows make them difficult for human observers to interpret. To address this, we introduce the Chain-of-Image Generation (CoIG) framework, which reframes image generation as a sequential, semantic process analogous to how humans create art. Similar to the advantages in monitorability and performance that Chain-of-Thought (CoT) brought to large language models (LLMs), CoIG can produce equivalent benefits in text-to-image generation. CoIG utilizes an LLM to decompose a complex prompt into a sequence of simple, step-by-step instructions. The image generation model then executes this plan by progressively generating and editing the image. Each step focuses on a single semantic entity, enabling direct monitoring. We formally assess this property using two novel metrics: CoIG Readability, which evaluates the clarity of each intermediate step via its corresponding output; and Causal Relevance, which quantifies the impact of each procedural step on the final generated image. We further show that our framework mitigates entity collapse by decomposing the complex generation task into simple subproblems, analogous to the procedural reasoning employed by CoT. Our experimental results indicate that CoIG substantially enhances quantitative monitorability while achieving competitive compositional robustness compared to established baseline models. The framework is model-agnostic and can be integrated with any image generation model.

