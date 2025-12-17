---
layout: default
title: SKEL-CF: Coarse-to-Fine Biomechanical Skeleton and Surface Mesh Recovery
---

# SKEL-CF: Coarse-to-Fine Biomechanical Skeleton and Surface Mesh Recovery

**arXiv**: [2511.20157v1](https://arxiv.org/abs/2511.20157) | [PDF](https://arxiv.org/pdf/2511.20157.pdf)

**作者**: Da Li, Ji-Ping Jin, Xuanlong Yu, Wei Liu, Xiaodong Cun, Kai Chen, Rui Fan, Jiangang Kong, Shen Xi

---

## 💡 一句话要点

**提出SKEL-CF框架以解决SKEL参数估计中的挑战，提升人体运动分析的生物力学真实性。**

**关键词**: `人体姿态估计` `生物力学骨架` `粗到细框架` `transformer架构` `相机建模` `4DHuman-SKEL数据集`

## 📋 核心要点

1. 核心问题：SKEL模型参数估计困难，源于训练数据不足、视角模糊和人体关节复杂性。
2. 方法要点：采用粗到细的transformer架构，编码器预测粗略参数，解码器逐层精炼。
3. 实验或效果：在MOYO数据集上，MPJPE达85.0，显著优于先前方法HSMR。

## 📄 摘要（原文）

> Parametric 3D human models such as SMPL have driven significant advances in human pose and shape estimation, yet their simplified kinematics limit biomechanical realism. The recently proposed SKEL model addresses this limitation by re-rigging SMPL with an anatomically accurate skeleton. However, estimating SKEL parameters directly remains challenging due to limited training data, perspective ambiguities, and the inherent complexity of human articulation. We introduce SKEL-CF, a coarse-to-fine framework for SKEL parameter estimation. SKEL-CF employs a transformer-based encoder-decoder architecture, where the encoder predicts coarse camera and SKEL parameters, and the decoder progressively refines them in successive layers. To ensure anatomically consistent supervision, we convert the existing SMPL-based dataset 4DHuman into a SKEL-aligned version, 4DHuman-SKEL, providing high-quality training data for SKEL estimation. In addition, to mitigate depth and scale ambiguities, we explicitly incorporate camera modeling into the SKEL-CF pipeline and demonstrate its importance across diverse viewpoints. Extensive experiments validate the effectiveness of the proposed design. On the challenging MOYO dataset, SKEL-CF achieves 85.0 MPJPE / 51.4 PA-MPJPE, significantly outperforming the previous SKEL-based state-of-the-art HSMR (104.5 / 79.6). These results establish SKEL-CF as a scalable and anatomically faithful framework for human motion analysis, bridging the gap between computer vision and biomechanics. Our implementation is available on the project page: https://pokerman8.github.io/SKEL-CF/.

