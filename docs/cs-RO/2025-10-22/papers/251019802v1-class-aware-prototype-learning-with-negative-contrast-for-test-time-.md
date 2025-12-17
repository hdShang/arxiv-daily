---
layout: default
title: Class-Aware Prototype Learning with Negative Contrast for Test-Time Adaptation of Vision-Language Models
---

# Class-Aware Prototype Learning with Negative Contrast for Test-Time Adaptation of Vision-Language Models

**arXiv**: [2510.19802v1](https://arxiv.org/abs/2510.19802) | [PDF](https://arxiv.org/pdf/2510.19802.pdf)

**作者**: Xiaozhen Qiao, Jingkai Zhao, Yuqiu Jiang, Xianda Guo, Zhe Sun, Hongyuan Zhang, Xuelong Li

---

## 💡 一句话要点

**提出类感知原型学习与负对比方法，以增强视觉语言模型在测试时分布偏移下的泛化能力。**

**关键词**: `测试时适应` `视觉语言模型` `原型学习` `负对比学习` `分布偏移` `类感知缓存`

## 📋 核心要点

1. 核心问题：视觉语言模型在分布偏移时性能下降，原型退化和类间混淆是主要挑战。
2. 方法要点：动态调整类原型缓存，结合负对比学习机制提升类可分性。
3. 实验或效果：在15个基准测试中优于现有方法，适用于ResNet-50和ViT-B/16骨干网络。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) demonstrate impressive zero-shot generalization
> through large-scale image-text pretraining, yet their performance can drop once
> the deployment distribution diverges from the training distribution. To address
> this, Test-Time Adaptation (TTA) methods update models using unlabeled target
> data. However, existing approaches often ignore two key challenges: prototype
> degradation in long-tailed distributions and confusion between semantically
> similar classes. To tackle these issues, we propose \textbf{C}lass-Aware
> \textbf{P}rototype \textbf{L}earning with \textbf{N}egative
> \textbf{C}ontrast(\textbf{CPL-NC}), a lightweight TTA framework designed
> specifically for VLMs to enhance generalization under distribution shifts.
> CPL-NC introduces a \textit{Class-Aware Prototype Cache} Module that
> dynamically adjusts per-class capacity based on test-time frequency and
> activation history, with a rejuvenation mechanism for inactive classes to
> retain rare-category knowledge. Additionally, a \textit{Negative Contrastive
> Learning} Mechanism identifies and constrains hard visual-textual negatives to
> improve class separability. The framework employs asymmetric optimization,
> refining only textual prototypes while anchoring on stable visual features.
> Experiments on 15 benchmarks show that CPL-NC consistently outperforms prior
> TTA methods across both ResNet-50 and ViT-B/16 backbones.

