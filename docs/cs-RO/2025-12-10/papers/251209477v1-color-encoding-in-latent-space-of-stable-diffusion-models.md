---
layout: default
title: Color encoding in Latent Space of Stable Diffusion Models
---

# Color encoding in Latent Space of Stable Diffusion Models

**arXiv**: [2512.09477v1](https://arxiv.org/abs/2512.09477) | [PDF](https://arxiv.org/pdf/2512.09477.pdf)

**作者**: Guillem Arias, Ariadna Solà, Martí Armengod, Maria Vanrell

---

## 💡 一句话要点

**分析Stable Diffusion潜在空间中的颜色编码机制，揭示其与高效编码表示的对齐结构**

**关键词**: `Stable Diffusion` `潜在空间分析` `颜色编码` `生成模型` `高效编码`

## 📋 核心要点

1. 研究扩散生成模型中颜色等感知属性的内部表示机制，以Stable Diffusion为例
2. 通过合成数据集、PCA和相似性度量，发现颜色信息在潜在通道c_3和c_4中以圆形对立轴编码
3. 实验表明潜在空间具有可解释结构，为模型理解和编辑应用提供基础

## 📄 摘要（原文）

> Recent advances in diffusion-based generative models have achieved remarkable visual fidelity, yet a detailed understanding of how specific perceptual attributes - such as color and shape - are internally represented remains limited. This work explores how color is encoded in a generative model through a systematic analysis of the latent representations in Stable Diffusion. Through controlled synthetic datasets, principal component analysis (PCA) and similarity metrics, we reveal that color information is encoded along circular, opponent axes predominantly captured in latent channels c_3 and c_4, whereas intensity and shape are primarily represented in channels c_1 and c_2. Our findings indicate that the latent space of Stable Diffusion exhibits an interpretable structure aligned with a efficient coding representation. These insights provide a foundation for future work in model understanding, editing applications, and the design of more disentangled generative frameworks.

