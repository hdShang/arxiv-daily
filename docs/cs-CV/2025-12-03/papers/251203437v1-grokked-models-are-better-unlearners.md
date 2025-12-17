---
layout: default
title: Grokked Models are Better Unlearners
---

# Grokked Models are Better Unlearners

**arXiv**: [2512.03437v1](https://arxiv.org/abs/2512.03437) | [PDF](https://arxiv.org/pdf/2512.03437.pdf)

**作者**: Yuanbang Liang, Yang Li

---

## 💡 一句话要点

**发现Grokked模型作为起点能提升机器遗忘效率与稳定性，无需修改算法。**

**关键词**: `机器遗忘` `Grokking` `模型鲁棒性` `选择性遗忘` `特征模块化`

## 📋 核心要点

1. 核心问题：Grokking训练机制是否有助于机器遗忘，即选择性移除数据影响。
2. 方法要点：比较标准遗忘方法在Grokking过渡前后的应用，分析特征与曲率。
3. 实验或效果：Grokked检查点带来更高效遗忘、更少副作用和更稳定更新。

## 📄 摘要（原文）

> Grokking-delayed generalization that emerges well after a model has fit the training data-has been linked to robustness and representation quality. We ask whether this training regime also helps with machine unlearning, i.e., removing the influence of specified data without full retraining. We compare applying standard unlearning methods before versus after the grokking transition across vision (CNNs/ResNets on CIFAR, SVHN, and ImageNet) and language (a transformer on a TOFU-style setup). Starting from grokked checkpoints consistently yields (i) more efficient forgetting (fewer updates to reach a target forget level), (ii) less collateral damage (smaller drops on retained and test performance), and (iii) more stable updates across seeds, relative to early-stopped counterparts under identical unlearning algorithms. Analyses of features and curvature further suggest that post-grokking models learn more modular representations with reduced gradient alignment between forget and retain subsets, which facilitates selective forgetting. Our results highlight when a model is trained (pre- vs. post-grokking) as an orthogonal lever to how unlearning is performed, providing a practical recipe to improve existing unlearning methods without altering their algorithms.

