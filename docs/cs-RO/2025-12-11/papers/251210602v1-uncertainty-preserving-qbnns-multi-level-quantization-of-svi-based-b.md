---
layout: default
title: Uncertainty-Preserving QBNNs: Multi-Level Quantization of SVI-Based Bayesian Neural Networks for Image Classification
---

# Uncertainty-Preserving QBNNs: Multi-Level Quantization of SVI-Based Bayesian Neural Networks for Image Classification

**arXiv**: [2512.10602v1](https://arxiv.org/abs/2512.10602) | [PDF](https://arxiv.org/pdf/2512.10602.pdf)

**作者**: Hendrik Borras, Yong Wu, Bernhard Klein, Holger Fröning

---

## 💡 一句话要点

**提出多级量化框架以在资源受限设备上部署贝叶斯神经网络，保持不确定性估计**

**关键词**: `贝叶斯神经网络` `不确定性量化` `多级量化` `随机变分推断` `边缘设备部署` `低精度计算`

## 📋 核心要点

1. 贝叶斯神经网络提供不确定性量化，但计算和内存开销大，量化应用不足
2. 引入三种量化策略：变分参数量化、采样参数量化和联合量化，使用对数量化保护分布结构
3. 在Dirty-MNIST上实验，4位量化实现8倍内存减少，分类准确性和不确定性估计保持良好

## 📄 摘要（原文）

> Bayesian Neural Networks (BNNs) provide principled uncertainty quantification but suffer from substantial computational and memory overhead compared to deterministic networks. While quantization techniques have successfully reduced resource requirements in standard deep learning models, their application to probabilistic models remains largely unexplored. We introduce a systematic multi-level quantization framework for Stochastic Variational Inference based BNNs that distinguishes between three quantization strategies: Variational Parameter Quantization (VPQ), Sampled Parameter Quantization (SPQ), and Joint Quantization (JQ). Our logarithmic quantization for variance parameters, and specialized activation functions to preserve the distributional structure are essential for calibrated uncertainty estimation. Through comprehensive experiments on Dirty-MNIST, we demonstrate that BNNs can be quantized down to 4-bit precision while maintaining both classification accuracy and uncertainty disentanglement. At 4 bits, Joint Quantization achieves up to 8x memory reduction compared to floating-point implementations with minimal degradation in epistemic and aleatoric uncertainty estimation. These results enable deployment of BNNs on resource-constrained edge devices and provide design guidelines for future analog "Bayesian Machines" operating at inherently low precision.

