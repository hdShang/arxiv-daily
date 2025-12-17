---
layout: default
title: Dual Randomized Smoothing: Beyond Global Noise Variance
---

# Dual Randomized Smoothing: Beyond Global Noise Variance

**arXiv**: [2512.01782v1](https://arxiv.org/abs/2512.01782) | [PDF](https://arxiv.org/pdf/2512.01782.pdf)

**作者**: Chenhao Sun, Yuhao Mao, Martin Vechev

---

## 💡 一句话要点

**提出双随机平滑框架，通过输入依赖噪声方差突破全局方差限制，提升认证鲁棒性。**

**关键词**: `随机平滑` `认证鲁棒性` `输入依赖噪声` `对抗防御` `神经网络安全`

## 📋 核心要点

1. 标准随机平滑中全局噪声方差无法同时在小半径和大半径下实现强性能。
2. 双随机平滑框架包含方差估计器和分类器，允许输入依赖噪声方差，并确保局部常数性。
3. 在CIFAR-10和ImageNet上实验显示，该方法在多个半径下优于先前方法，计算开销仅增加60%。

## 📄 摘要（原文）

> Randomized Smoothing (RS) is a prominent technique for certifying the robustness of neural networks against adversarial perturbations. With RS, achieving high accuracy at small radii requires a small noise variance, while achieving high accuracy at large radii requires a large noise variance. However, the global noise variance used in the standard RS formulation leads to a fundamental limitation: there exists no global noise variance that simultaneously achieves strong performance at both small and large radii. To break through the global variance limitation, we propose a dual RS framework which enables input-dependent noise variances. To achieve that, we first prove that RS remains valid with input-dependent noise variances, provided the variance is locally constant around each input. Building on this result, we introduce two components which form our dual RS framework: (i) a variance estimator first predicts an optimal noise variance for each input, (ii) this estimated variance is then used by a standard RS classifier. The variance estimator is independently smoothed via RS to ensure local constancy, enabling flexible design. We also introduce training strategies to iteratively optimize the two components. Extensive experiments on CIFAR-10 show that our dual RS method provides strong performance for both small and large radii-unattainable with global noise variance-while incurring only a 60% computational overhead at inference. Moreover, it consistently outperforms prior input-dependent noise approaches across most radii, with particularly large gains at radii 0.5, 0.75, and 1.0, achieving relative improvements of 19%, 24%, and 21%, respectively. On ImageNet, dual RS remains effective across all radii. Additionally, the dual RS framework naturally provides a routing perspective for certified robustness, improving the accuracy-robustness trade-off with off-the-shelf expert RS models.

