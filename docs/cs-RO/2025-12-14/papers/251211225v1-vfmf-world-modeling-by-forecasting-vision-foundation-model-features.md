---
layout: default
title: VFMF: World Modeling by Forecasting Vision Foundation Model Features
---

# VFMF: World Modeling by Forecasting Vision Foundation Model Features

**arXiv**: [2512.11225v1](https://arxiv.org/abs/2512.11225) | [PDF](https://arxiv.org/pdf/2512.11225.pdf)

**作者**: Gabrijel Boduljak, Yushi Lan, Christian Rupprecht, Andrea Vedaldi

---

## 💡 一句话要点

**提出VFMF方法，通过预测视觉基础模型特征进行世界建模，以解决确定性回归中不确定性捕获不足的问题。**

**关键词**: `世界建模` `特征预测` `生成式模型` `视觉基础模型` `不确定性捕获` `多模态输出`

## 📋 核心要点

1. 核心问题：确定性回归在预测视觉基础模型特征时平均化多种可能未来，导致不确定性捕获不足，影响预测准确性。
2. 方法要点：采用自回归流匹配在视觉基础模型特征空间进行生成式预测，将特征编码到紧凑潜在空间以支持扩散模型。
3. 实验或效果：在匹配架构和计算下，相比回归方法，在所有输出模态（如语义分割、深度）上产生更清晰和准确的预测。

## 📄 摘要（原文）

> Forecasting from partial observations is central to world modeling. Many recent methods represent the world through images, and reduce forecasting to stochastic video generation. Although such methods excel at realism and visual fidelity, predicting pixels is computationally intensive and not directly useful in many applications, as it requires translating RGB into signals useful for decision making. An alternative approach uses features from vision foundation models (VFMs) as world representations, performing deterministic regression to predict future world states. These features can be directly translated into actionable signals such as semantic segmentation and depth, while remaining computationally efficient. However, deterministic regression averages over multiple plausible futures, undermining forecast accuracy by failing to capture uncertainty. To address this crucial limitation, we introduce a generative forecaster that performs autoregressive flow matching in VFM feature space. Our key insight is that generative modeling in this space requires encoding VFM features into a compact latent space suitable for diffusion. We show that this latent space preserves information more effectively than previously used PCA-based alternatives, both for forecasting and other applications, such as image generation. Our latent predictions can be easily decoded into multiple useful and interpretable output modalities: semantic segmentation, depth, surface normals, and even RGB. With matched architecture and compute, our method produces sharper and more accurate predictions than regression across all modalities. Our results suggest that stochastic conditional generation of VFM features offers a promising and scalable foundation for future world models.

