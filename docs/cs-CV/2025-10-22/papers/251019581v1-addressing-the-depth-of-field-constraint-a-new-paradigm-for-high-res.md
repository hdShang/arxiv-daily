---
layout: default
title: Addressing the Depth-of-Field Constraint: A New Paradigm for High Resolution Multi-Focus Image Fusion
---

# Addressing the Depth-of-Field Constraint: A New Paradigm for High Resolution Multi-Focus Image Fusion

**arXiv**: [2510.19581v1](https://arxiv.org/abs/2510.19581) | [PDF](https://arxiv.org/pdf/2510.19581.pdf)

**作者**: Luca Piano, Peng Huanwen, Radu Ciprian Bilcu

---

## 💡 一句话要点

**提出VAEEDOF方法以解决多焦点图像融合中的深度限制问题**

**关键词**: `多焦点图像融合` `变分自编码器` `景深限制` `合成数据集` `图像重建` `蒸馏训练`

## 📋 核心要点

1. 核心问题：光学镜头景深限制导致图像部分区域模糊，传统方法存在数据不足和域差距问题。
2. 方法要点：使用蒸馏变分自编码器进行高效图像重建，融合模块可同时处理多张图像。
3. 实验或效果：引入MattingMFIF数据集，实现无伪影融合，在合成与真实场景中表现优异。

## 📄 摘要（原文）

> Multi-focus image fusion (MFIF) addresses the depth-of-field (DOF)
> limitations of optical lenses, where only objects within a specific range
> appear sharp. Although traditional and deep learning methods have advanced the
> field, challenges persist, including limited training data, domain gaps from
> synthetic datasets, and difficulties with regions lacking information. We
> propose VAEEDOF, a novel MFIF method that uses a distilled variational
> autoencoder for high-fidelity, efficient image reconstruction. Our fusion
> module processes up to seven images simultaneously, enabling robust fusion
> across diverse focus points. To address data scarcity, we introduce
> MattingMFIF, a new syntetic 4K dataset, simulating realistic DOF effects from
> real photographs. Our method achieves state-of-the-art results, generating
> seamless artifact-free fused images and bridging the gap between synthetic and
> real-world scenarios, offering a significant step forward in addressing complex
> MFIF challenges. The code, and weights are available here:

