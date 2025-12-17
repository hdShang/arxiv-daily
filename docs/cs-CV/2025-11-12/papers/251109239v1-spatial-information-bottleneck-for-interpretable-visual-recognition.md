---
layout: default
title: Spatial Information Bottleneck for Interpretable Visual Recognition
---

# Spatial Information Bottleneck for Interpretable Visual Recognition

**arXiv**: [2511.09239v1](https://arxiv.org/abs/2511.09239) | [PDF](https://arxiv.org/pdf/2511.09239.pdf)

**作者**: Kaixiang Shu, Kai Meng, Junqin Luo

---

## 💡 一句话要点

**提出空间信息瓶颈以提升视觉识别的可解释性和鲁棒性**

**关键词**: `可解释视觉识别` `信息瓶颈` `梯度归因` `空间解缠` `向量-雅可比积` `互信息优化`

## 📋 核心要点

1. 深度网络学习空间纠缠表示，混淆前景与背景特征，损害可解释性
2. 基于信息论，优化向量-雅可比积空间结构，最大化前景互信息并最小化背景互信息
3. 在五个基准测试中，六种解释方法均获改进，前景集中且分类精度提升

## 📄 摘要（原文）

> Deep neural networks typically learn spatially entangled representations that conflate discriminative foreground features with spurious background correlations, thereby undermining model interpretability and robustness. We propose a novel understanding framework for gradient-based attribution from an information-theoretic perspective. We prove that, under mild conditions, the Vector-Jacobian Products (VJP) computed during backpropagation form minimal sufficient statistics of input features with respect to class labels. Motivated by this finding, we propose an encoding-decoding perspective : forward propagation encodes inputs into class space, while VJP in backpropagation decodes this encoding back to feature space. Therefore, we propose Spatial Information Bottleneck (S-IB) to spatially disentangle information flow. By maximizing mutual information between foreground VJP and inputs while minimizing mutual information in background regions, S-IB encourages networks to encode information only in class-relevant spatial regions. Since post-hoc explanation methods fundamentally derive from VJP computations, directly optimizing VJP's spatial structure during training improves visualization quality across diverse explanation paradigms. Experiments on five benchmarks demonstrate universal improvements across six explanation methods, achieving better foreground concentration and background suppression without method-specific tuning, alongside consistent classification accuracy gains.

