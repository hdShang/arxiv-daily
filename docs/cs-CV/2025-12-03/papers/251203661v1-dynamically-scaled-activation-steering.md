---
layout: default
title: Dynamically Scaled Activation Steering
---

# Dynamically Scaled Activation Steering

**arXiv**: [2512.03661v1](https://arxiv.org/abs/2512.03661) | [PDF](https://arxiv.org/pdf/2512.03661.pdf)

**作者**: Alex Ferrando, Xavier Suau, Jordi Gonzàlez, Pau Rodriguez

---

## 💡 一句话要点

**提出动态缩放激活引导框架，以自适应调节生成模型中的引导强度，优化毒性缓解与效用保持的权衡。**

**关键词**: `激活引导` `毒性缓解` `动态缩放` `生成模型` `上下文自适应` `帕累托优化`

## 📋 核心要点

1. 核心问题：现有激活引导方法对所有输入统一干预，在不必要时降低模型性能。
2. 方法要点：DSAS解耦何时引导与如何引导，通过上下文相关缩放因子动态调整引导强度。
3. 实验或效果：结合现有方法改善帕累托前沿，应用于文本到图像扩散模型，展示概念调制能力。

## 📄 摘要（原文）

> Activation steering has emerged as a powerful method for guiding the behavior of generative models towards desired outcomes such as toxicity mitigation. However, most existing methods apply interventions uniformly across all inputs, degrading model performance when steering is unnecessary. We introduce Dynamically Scaled Activation Steering (DSAS), a method-agnostic steering framework that decouples when to steer from how to steer. DSAS adaptively modulates the strength of existing steering transformations across layers and inputs, intervening strongly only when undesired behavior is detected. At generation time, DSAS computes context-dependent scaling factors that selectively adjust the strength of any steering method. We also show how DSAS can be jointly optimized end-to-end together with the steering function. When combined with existing steering methods, DSAS consistently improves the Pareto front with respect to steering alone, achieving a better trade-off between toxicity mitigation and utility preservation. We further demonstrate DSAS's generality by applying it to a text-to-image diffusion model, showing how adaptive steering allows the modulation of specific concepts. Finally, DSAS introduces minimal computational overhead while improving interpretability, pinpointing which tokens require steering and by how much.

