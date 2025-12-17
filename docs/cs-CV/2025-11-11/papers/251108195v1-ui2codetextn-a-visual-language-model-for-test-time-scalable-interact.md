---
layout: default
title: UI2Code$^\text{N}$: A Visual Language Model for Test-Time Scalable Interactive UI-to-Code Generation
---

# UI2Code$^\text{N}$: A Visual Language Model for Test-Time Scalable Interactive UI-to-Code Generation

**arXiv**: [2511.08195v1](https://arxiv.org/abs/2511.08195) | [PDF](https://arxiv.org/pdf/2511.08195.pdf)

**作者**: Zhen Yang, Wenyi Hong, Mingde Xu, Xinyue Fan, Weihan Wang, Jiele Cheng, Xiaotao Gu, Jie Tang

---

## 💡 一句话要点

**提出UI2Code^N视觉语言模型，通过交互式UI到代码生成解决多模态编码不足问题。**

**关键词**: `视觉语言模型` `UI到代码生成` `多模态编码` `交互式生成` `测试时扩展` `强化学习`

## 📋 核心要点

1. 核心问题：UI编程复杂，现有视觉语言模型多模态编码能力弱且缺乏迭代反馈。
2. 方法要点：采用分阶段预训练、微调和强化学习，统一UI生成、编辑和优化能力。
3. 实验效果：在UI到代码和优化基准上达到开源模型最优，性能接近闭源领先模型。

## 📄 摘要（原文）

> User interface (UI) programming is a core yet highly complex part of modern software development. Recent advances in visual language models (VLMs) highlight the potential of automatic UI coding, but current approaches face two key limitations: multimodal coding capabilities remain underdeveloped, and single-turn paradigms make little use of iterative visual feedback. We address these challenges with an interactive UI-to-code paradigm that better reflects real-world workflows and raises the upper bound of achievable performance. Under this paradigm, we present UI2Code$^\text{N}$, a visual language model trained through staged pretraining, fine-tuning, and reinforcement learning to achieve foundational improvements in multimodal coding. The model unifies three key capabilities: UI-to-code generation, UI editing, and UI polishing. We further explore test-time scaling for interactive generation, enabling systematic use of multi-turn feedback. Experiments on UI-to-code and UI polishing benchmarks show that UI2Code$^\text{N}$ establishes a new state of the art among open-source models and achieves performance comparable to leading closed-source models such as Claude-4-Sonnet and GPT-5. Our code and models are available at https://github.com/zai-org/UI2Code_N.

