---
layout: default
title: Decoupled Entropy Minimization
---

# Decoupled Entropy Minimization

**arXiv**: [2511.03256v1](https://arxiv.org/abs/2511.03256) | [PDF](https://arxiv.org/pdf/2511.03256.pdf)

**作者**: Jing Ma, Hanlin Li, Xiang Xiang

---

## 💡 一句话要点

**提出自适应解耦熵最小化以解决经典熵最小化在噪声和动态环境中的局限性**

**关键词**: `熵最小化` `解耦学习` `自适应校准` `噪声环境学习` `不完美监督学习`

## 📋 核心要点

1. 核心问题：经典熵最小化存在奖励崩溃和易类偏差，限制其在机器学习任务中的潜力
2. 方法要点：将熵最小化解耦为聚类聚合驱动因子和梯度缓解校准器，并引入自适应归一化和边际熵校准器
3. 实验或效果：在噪声和动态环境的不完美监督学习任务中，性能优于经典熵最小化上界变体

## 📄 摘要（原文）

> Entropy Minimization (EM) is beneficial to reducing class overlap, bridging
> domain gap, and restricting uncertainty for various tasks in machine learning,
> yet its potential is limited. To study the internal mechanism of EM, we
> reformulate and decouple the classical EM into two parts with opposite effects:
> cluster aggregation driving factor (CADF) rewards dominant classes and prompts
> a peaked output distribution, while gradient mitigation calibrator (GMC)
> penalizes high-confidence classes based on predicted probabilities.
> Furthermore, we reveal the limitations of classical EM caused by its coupled
> formulation: 1) reward collapse impedes the contribution of high-certainty
> samples in the learning process, and 2) easy-class bias induces misalignment
> between output distribution and label distribution. To address these issues, we
> propose Adaptive Decoupled Entropy Minimization (AdaDEM), which normalizes the
> reward brought from CADF and employs a marginal entropy calibrator (MEC) to
> replace GMC. AdaDEM outperforms DEM*, an upper-bound variant of classical EM,
> and achieves superior performance across various imperfectly supervised
> learning tasks in noisy and dynamic environments.

