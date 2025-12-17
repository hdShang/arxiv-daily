---
layout: default
title: Guiding Visual Autoregressive Models through Spectrum Weakening
---

# Guiding Visual Autoregressive Models through Spectrum Weakening

**arXiv**: [2511.22991v1](https://arxiv.org/abs/2511.22991) | [PDF](https://arxiv.org/pdf/2511.22991.pdf)

**作者**: Chaoyang Wang, Tianmeng Yang, Jingdong Wang, Yunhai Tong

---

## 💡 一句话要点

**提出频谱弱化框架以增强视觉自回归模型的无条件和条件生成质量**

**关键词**: `视觉自回归模型` `频谱弱化` `无条件生成` `条件对齐` `谱域变换` `引导机制`

## 📋 核心要点

1. 核心问题：现有引导方法依赖扩散模型假设，不适用于视觉自回归模型
2. 方法要点：在谱域构建可控弱模型，通过通道维度频谱选择和重归一化实现信息控制
3. 实验或效果：在离散和连续自回归模型上验证，提升无条件生成质量并保持条件对齐

## 📄 摘要（原文）

> Classifier-free guidance (CFG) has become a widely adopted and practical approach for enhancing generation quality and improving condition alignment. Recent studies have explored guidance mechanisms for unconditional generation, yet these approaches remain fundamentally tied to assumptions specific to diffusion models. In this work, we propose a spectrum-weakening framework for visual autoregressive (AR) models. This method works without the need for re-training, specific conditions, or any architectural modifications. It achieves this by constructing a controllable weak model in the spectral domain. We theoretically show that invertible spectral transformations preserve information, while selectively retaining only a subset of spectrum introduces controlled information reduction. Based on this insight, we perform spectrum selection along the channel dimension of internal representations, which avoids the structural constraints imposed by diffusion models. We further introduce two spectrum renormalization strategies that ensures numerical stability during the weakening process. Extensive experiments were conducted on both discrete and continuous AR models, with text or class conditioning. The results demonstrate that our method enables high-quality unconditional generation while maintaining strong prompt alignment for conditional generation.

