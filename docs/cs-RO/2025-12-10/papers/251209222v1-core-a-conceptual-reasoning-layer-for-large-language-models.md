---
layout: default
title: CORE: A Conceptual Reasoning Layer for Large Language Models
---

# CORE: A Conceptual Reasoning Layer for Large Language Models

**arXiv**: [2512.09222v1](https://arxiv.org/abs/2512.09222) | [PDF](https://arxiv.org/pdf/2512.09222.pdf)

**作者**: Vishwas Hegde, Vindhya Shigehalli

---

## 💡 一句话要点

**提出CORE概念推理层以解决大语言模型多轮交互中的状态漂移问题**

**关键词**: `多轮交互` `概念推理` `状态管理` `模型无关机制` `提示优化`

## 📋 核心要点

1. 核心问题：大语言模型在多轮交互中依赖令牌历史导致状态漂移和推理不一致
2. 方法要点：引入持久本地概念和认知操作符，分离概念推理与语言生成
3. 实验或效果：原型模拟显示累计提示令牌减少约42%，但非真实性能估计

## 📄 摘要（原文）

> Large language models handle single-turn generation well, but multi-turn interactions still require the model to reconstruct user intent and task state from an expanding token history because internal representations do not persist across turns. This token-first paradigm leads to drift, inconsistent reasoning modes, and growing prompts as conversations deepen. We propose CORE, a concept-first interaction layer that improves multi-turn stability without modifying model weights. CORE combines a small library of universal cognitive operators with a persistent Local Concept - a compact semantic state capturing the task, constraints, preferences, and intermediate results. Each model call receives only this concept state, the user's latest instruction, and the selected operator, eliminating the need to replay full history. A preliminary prototype simulating CORE's behavior shows about 42% reduction in cumulative prompt tokens, though this number reflects prototype conditions and should not be interpreted as a real-world performance estimate. CORE offers a model-agnostic mechanism that separates conceptual reasoning from language generation, suggesting a scalable direction for more stable multi-turn systems.

