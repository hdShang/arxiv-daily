---
layout: default
title: Artemis: Structured Visual Reasoning for Perception Policy Learning
---

# Artemis: Structured Visual Reasoning for Perception Policy Learning

**arXiv**: [2512.01988v1](https://arxiv.org/abs/2512.01988) | [PDF](https://arxiv.org/pdf/2512.01988.pdf)

**作者**: Wei Tang, Yanpeng Sun, Shan Zhang, Xiaofan Li, Piotr Koniusz, Wei Li, Na Zhao, Zechao Li

---

## 💡 一句话要点

**提出Artemis框架，通过结构化视觉推理增强感知策略学习**

**关键词**: `视觉感知策略` `结构化推理` `提议学习` `空间表示` `多模态大语言模型` `泛化能力`

## 📋 核心要点

1. 核心问题：基于自然语言的中间推理链在视觉感知任务中常降低性能，因语义推理与空间对象中心推理不匹配
2. 方法要点：采用结构化提议推理，以（标签，边界框）对表示中间步骤，支持状态跟踪和直接监督
3. 实验或效果：在Qwen2.5-VL-3B上实现，在定位和检测任务表现强，并泛化至计数和几何感知任务

## 📄 摘要（原文）

> Recent reinforcement-learning frameworks for visual perception policy have begun to incorporate intermediate reasoning chains expressed in natural language. Empirical observations indicate that such purely linguistic intermediate reasoning often reduces performance on perception tasks. We argue that the core issue lies not in reasoning per se but in the form of reasoning: while these chains perform semantic reasoning in an unstructured linguistic space, visual perception requires reasoning in a spatial and object-centric space. In response, we introduce Artemis, a perception-policy learning framework that performs structured proposal-based reasoning, where each intermediate step is represented as a (label, bounding-box) pair capturing a verifiable visual state. This design enables explicit tracking of intermediate states, direct supervision for proposal quality, and avoids ambiguity introduced by language-based reasoning. Artemis is built on Qwen2.5-VL-3B, achieves strong performance on grounding and detection task and exhibits substantial generalization to counting and geometric-perception tasks. The consistent improvements across these diverse settings confirm that aligning reasoning with spatial representations enhances perception-policy learning. Owing to its strengthened visual reasoning, Artemis also achieves competitive performance on general MLLM benchmarks, illustrating that spatially grounded reasoning provides a principled route toward scalable and general perception policies.

