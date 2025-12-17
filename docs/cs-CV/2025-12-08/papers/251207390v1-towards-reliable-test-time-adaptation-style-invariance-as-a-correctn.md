---
layout: default
title: Towards Reliable Test-Time Adaptation: Style Invariance as a Correctness Likelihood
---

# Towards Reliable Test-Time Adaptation: Style Invariance as a Correctness Likelihood

**arXiv**: [2512.07390v1](https://arxiv.org/abs/2512.07390) | [PDF](https://arxiv.org/pdf/2512.07390.pdf)

**作者**: Gilhyun Nam, Taewon Kim, Joonhyun Jeong, Eunho Yang

---

## 💡 一句话要点

**提出SICL框架，利用风格不变性提升测试时自适应中的不确定性校准可靠性。**

**关键词**: `测试时自适应` `不确定性校准` `风格不变性` `预测一致性` `实例级估计`

## 📋 核心要点

1. 核心问题：测试时自适应导致预测不确定性校准不佳，在动态测试条件下性能下降。
2. 方法要点：通过测量风格变换变体间的预测一致性，估计实例级正确性似然，无需反向传播。
3. 实验或效果：在多种基线、TTA方法和场景下，平均降低校准误差13个百分点。

## 📄 摘要（原文）

> Test-time adaptation (TTA) enables efficient adaptation of deployed models, yet it often leads to poorly calibrated predictive uncertainty - a critical issue in high-stakes domains such as autonomous driving, finance, and healthcare. Existing calibration methods typically assume fixed models or static distributions, resulting in degraded performance under real-world, dynamic test conditions. To address these challenges, we introduce Style Invariance as a Correctness Likelihood (SICL), a framework that leverages style-invariance for robust uncertainty estimation. SICL estimates instance-wise correctness likelihood by measuring prediction consistency across style-altered variants, requiring only the model's forward pass. This makes it a plug-and-play, backpropagation-free calibration module compatible with any TTA method. Comprehensive evaluations across four baselines, five TTA methods, and two realistic scenarios with three model architecture demonstrate that SICL reduces calibration error by an average of 13 percentage points compared to conventional calibration approaches.

