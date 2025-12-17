---
layout: default
title: Non-Parametric Probabilistic Robustness: A Conservative Metric with Optimized Perturbation Distributions
---

# Non-Parametric Probabilistic Robustness: A Conservative Metric with Optimized Perturbation Distributions

**arXiv**: [2511.17380v1](https://arxiv.org/abs/2511.17380) | [PDF](https://arxiv.org/pdf/2511.17380.pdf)

**作者**: Zheng Wang, Yi Zhang, Siddartha Khastgir, Carsten Maple, Xingyu Zhao

---

## 💡 一句话要点

**提出非参数概率鲁棒性以解决扰动分布未知的深度学习模型鲁棒性评估问题**

**关键词**: `概率鲁棒性` `非参数学习` `深度学习安全` `扰动分布优化` `鲁棒性评估`

## 📋 核心要点

1. 现有概率鲁棒性假设固定扰动分布，不切实际
2. NPPR从数据学习优化扰动分布，提供保守鲁棒性评估
3. 实验在多个数据集和模型上验证NPPR更保守实用

## 📄 摘要（原文）

> Deep learning (DL) models, despite their remarkable success, remain vulnerable to small input perturbations that can cause erroneous outputs, motivating the recent proposal of probabilistic robustness (PR) as a complementary alternative to adversarial robustness (AR). However, existing PR formulations assume a fixed and known perturbation distribution, an unrealistic expectation in practice. To address this limitation, we propose non-parametric probabilistic robustness (NPPR), a more practical PR metric that does not rely on any predefined perturbation distribution. Following the non-parametric paradigm in statistical modeling, NPPR learns an optimized perturbation distribution directly from data, enabling conservative PR evaluation under distributional uncertainty. We further develop an NPPR estimator based on a Gaussian Mixture Model (GMM) with Multilayer Perceptron (MLP) heads and bicubic up-sampling, covering various input-dependent and input-independent perturbation scenarios. Theoretical analyses establish the relationships among AR, PR, and NPPR. Extensive experiments on CIFAR-10, CIFAR-100, and Tiny ImageNet across ResNet18/50, WideResNet50 and VGG16 validate NPPR as a more practical robustness metric, showing up to 40\% more conservative (lower) PR estimates compared to assuming those common perturbation distributions used in state-of-the-arts.

