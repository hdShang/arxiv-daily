---
layout: default
title: From Points to Clouds: Learning Robust Semantic Distributions for Multi-modal Prompts
---

# From Points to Clouds: Learning Robust Semantic Distributions for Multi-modal Prompts

**arXiv**: [2511.22897v1](https://arxiv.org/abs/2511.22897) | [PDF](https://arxiv.org/pdf/2511.22897.pdf)

**作者**: Weiran Li, Yeqiang Liu, Yijie Wei, Mina Han, Xin Liu, Zhenbo Li

---

## 💡 一句话要点

**提出Points-to-Clouds框架，通过语义分布学习解决多模态提示学习中的泛化脆弱性问题。**

**关键词**: `多模态提示学习` `语义分布学习` `去噪机制` `视觉语言模型` `泛化性能`

## 📋 核心要点

1. 核心问题：现有方法基于静态点表示，易过拟合且泛化差。
2. 方法要点：引入双去噪机制，将提示学习重构为动态去噪任务。
3. 实验或效果：在11个数据集上验证，基类到新类泛化性能提升1.4%。

## 📄 摘要（原文）

> Multimodal Prompt Learning (MPL) has emerged as a pivotal technique for adapting large-scale Visual Language Models (VLMs). However, current MPL methods are fundamentally limited by their optimization of a single, static point representation. This paradigm is inherently brittle, leads to overfitting on base classes, and generalizes poorly to novel or ambiguous categories. We challenge this point paradigm, proposing that robust generalization requires learning a semantic cloud (i.e., a distribution over the embedding space). To achieve this, we introduce Points-to-Clouds (P2C), a novel framework inspired by diffusion models that reframes prompt learning as a dynamic denoising task. At the core of P2C is a dual denoising mechanism: a Dynamic Prompt Denoising (DPD) mechanism perturbs text prompts with sophisticated, annealed noise to learn a smoother semantic landscape, while an auxiliary V-L Mapper denoising loss re-tasks the mapper as a denoising autoencoder. This forces the mapper to reconstruct clean visual prompts from noisy text inputs, ensuring robust cross-modal alignment. Extensive experiments across 11 datasets demonstrate that P2C consistently outperforms strong baselines. On the base-to-novel generalization benchmark, our method achieves a Harmonic Mean of 79.7%, representing a relative improvement of 1.4% over the baseline. The code and models are available at https://vranlee.github.io/P2C/.

