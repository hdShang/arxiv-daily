---
layout: default
title: Equivariant Diffusion for Crystal Structure Prediction
---

# Equivariant Diffusion for Crystal Structure Prediction

**arXiv**: [2512.07289v1](https://arxiv.org/abs/2512.07289) | [PDF](https://arxiv.org/pdf/2512.07289.pdf)

**作者**: Peijia Lin, Pin Chen, Rui Jiao, Qing Mo, Jianhuan Cen, Wenbing Huang, Yang Liu, Dan Huang, Yutong Lu

---

## 💡 一句话要点

**提出EquiCSP扩散模型以解决晶体结构预测中的对称性保持问题**

**关键词**: `晶体结构预测` `等变扩散模型` `对称性保持` `条件生成` `周期平移等变性`

## 📋 核心要点

1. 现有晶体结构预测模型在扩散过程中未能完全保证置换、旋转和周期平移等变性
2. 提出EquiCSP模型，通过独特加噪算法严格保持周期平移等变性，并解决晶格置换等变性
3. 实验表明模型在生成准确结构和训练收敛速度方面显著优于现有方法

## 📄 摘要（原文）

> In addressing the challenge of Crystal Structure Prediction (CSP), symmetry-aware deep learning models, particularly diffusion models, have been extensively studied, which treat CSP as a conditional generation task. However, ensuring permutation, rotation, and periodic translation equivariance during diffusion process remains incompletely addressed. In this work, we propose EquiCSP, a novel equivariant diffusion-based generative model. We not only address the overlooked issue of lattice permutation equivariance in existing models, but also develop a unique noising algorithm that rigorously maintains periodic translation equivariance throughout both training and inference processes. Our experiments indicate that EquiCSP significantly surpasses existing models in terms of generating accurate structures and demonstrates faster convergence during the training process.

