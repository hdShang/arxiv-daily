---
layout: default
title: RainDiff: End-to-end Precipitation Nowcasting Via Token-wise Attention Diffusion
---

# RainDiff: End-to-end Precipitation Nowcasting Via Token-wise Attention Diffusion

**arXiv**: [2510.14962v1](https://arxiv.org/abs/2510.14962) | [PDF](https://arxiv.org/pdf/2510.14962.pdf)

**作者**: Thao Nguyen, Jiaqi Ma, Fahad Shahbaz Khan, Souhaib Ben Taieb, Salman Khan

---

## 💡 一句话要点

**提出RainDiff方法，通过令牌注意力扩散模型解决降水临近预报中的可扩展性问题。**

**关键词**: `降水临近预报` `扩散模型` `令牌注意力` `时空编码` `U-Net架构` `多尺度建模`

## 📋 核心要点

1. 降水临近预报面临混沌时空动态和可扩展性挑战，如潜在空间方法复杂、像素空间方法计算密集。
2. 方法将令牌注意力集成到U-Net扩散模型和时空编码器中，动态捕获多尺度时空依赖，无需额外模块。
3. 实验显示在多个数据集上优于现有方法，提升局部保真度、泛化性和鲁棒性。

## 📄 摘要（原文）

> Precipitation nowcasting, predicting future radar echo sequences from current
> observations, is a critical yet challenging task due to the inherently chaotic
> and tightly coupled spatio-temporal dynamics of the atmosphere. While recent
> advances in diffusion-based models attempt to capture both large-scale motion
> and fine-grained stochastic variability, they often suffer from scalability
> issues: latent-space approaches require a separately trained autoencoder,
> adding complexity and limiting generalization, while pixel-space approaches are
> computationally intensive and often omit attention mechanisms, reducing their
> ability to model long-range spatio-temporal dependencies. To address these
> limitations, we propose a Token-wise Attention integrated into not only the
> U-Net diffusion model but also the spatio-temporal encoder that dynamically
> captures multi-scale spatial interactions and temporal evolution. Unlike prior
> approaches, our method natively integrates attention into the architecture
> without incurring the high resource cost typical of pixel-space diffusion,
> thereby eliminating the need for separate latent modules. Our extensive
> experiments and visual evaluations across diverse datasets demonstrate that the
> proposed method significantly outperforms state-of-the-art approaches, yielding
> superior local fidelity, generalization, and robustness in complex
> precipitation forecasting scenarios.

