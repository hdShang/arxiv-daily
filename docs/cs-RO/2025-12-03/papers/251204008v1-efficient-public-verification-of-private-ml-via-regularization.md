---
layout: default
title: Efficient Public Verification of Private ML via Regularization
---

# Efficient Public Verification of Private ML via Regularization

**arXiv**: [2512.04008v1](https://arxiv.org/abs/2512.04008) | [PDF](https://arxiv.org/pdf/2512.04008.pdf)

**作者**: Zoë Ruha Bell, Anvith Thudi, Olive Franzese-McLaughlin, Nicolas Papernot, Shafi Goldwasser

---

## 💡 一句话要点

**提出基于正则化的差分隐私算法，以降低隐私保证验证的计算成本**

**关键词**: `差分隐私` `隐私验证` `正则化优化` `随机凸优化` `计算效率`

## 📋 核心要点

1. 核心问题：差分隐私训练后，公众难以高效验证模型是否满足隐私保证，验证成本与训练成本相当
2. 方法要点：通过私有最小化一系列正则化目标，使用标准DP组合界实现紧隐私-效用权衡
3. 实验或效果：验证计算成本显著低于训练成本，适用于大规模数据集，隐私-效用接近最优

## 📄 摘要（原文）

> Training with differential privacy (DP) provides a guarantee to members in a dataset that they cannot be identified by users of the released model. However, those data providers, and, in general, the public, lack methods to efficiently verify that models trained on their data satisfy DP guarantees. The amount of compute needed to verify DP guarantees for current algorithms scales with the amount of compute required to train the model. In this paper we design the first DP algorithm with near optimal privacy-utility trade-offs but whose DP guarantees can be verified cheaper than training. We focus on DP stochastic convex optimization (DP-SCO), where optimal privacy-utility trade-offs are known. Here we show we can obtain tight privacy-utility trade-offs by privately minimizing a series of regularized objectives and only using the standard DP composition bound. Crucially, this method can be verified with much less compute than training. This leads to the first known DP-SCO algorithm with near optimal privacy-utility whose DP verification scales better than training cost, significantly reducing verification costs on large datasets.

