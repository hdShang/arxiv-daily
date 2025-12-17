---
layout: default
title: Equivariant Symmetry-Aware Head Pose Estimation for Fetal MRI
---

# Equivariant Symmetry-Aware Head Pose Estimation for Fetal MRI

**arXiv**: [2512.04890v1](https://arxiv.org/abs/2512.04890) | [PDF](https://arxiv.org/pdf/2512.04890.pdf)

**作者**: Ramya Muthukrishnan, Borjan Gagoski, Aryn Lee, P. Ellen Grant, Elfar Adalsteinsson, Polina Golland, Benjamin Billot

---

## 💡 一句话要点

**提出E(3)-Pose方法，通过建模旋转等变性和对象对称性，解决胎儿MRI中头部姿态估计的挑战。**

**关键词**: `姿态估计` `旋转等变性` `对象对称性` `胎儿MRI` `6自由度估计` `临床翻译`

## 📋 核心要点

1. 核心问题：胎儿MRI扫描中头部运动导致姿态模糊，现有方法因解剖对称性、低分辨率、噪声和伪影而泛化困难。
2. 方法要点：E(3)-Pose显式建模旋转等变性和解剖对称性，构建稳健的6自由度头部姿态估计框架。
3. 实验或效果：在公开和临床胎儿MRI数据集上验证，E(3)-Pose展现优越的鲁棒性和跨域泛化能力，达到临床MRI体积上的先进精度。

## 📄 摘要（原文）

> We present E(3)-Pose, a novel fast pose estimation method that jointly and explicitly models rotation equivariance and object symmetry. Our work is motivated by the challenging problem of accounting for fetal head motion during a diagnostic MRI scan. We aim to enable automatic adaptive prescription of 2D diagnostic MRI slices with 6-DoF head pose estimation, supported by 3D MRI volumes rapidly acquired before each 2D slice. Existing methods struggle to generalize to clinical volumes, due to pose ambiguities induced by inherent anatomical symmetries, as well as low resolution, noise, and artifacts. In contrast, E(3)-Pose captures anatomical symmetries and rigid pose equivariance by construction, and yields robust estimates of the fetal head pose. Our experiments on publicly available and representative clinical fetal MRI datasets demonstrate the superior robustness and generalization of our method across domains. Crucially, E(3)-Pose achieves state-of-the-art accuracy on clinical MRI volumes, paving the way for clinical translation. Our implementation is available at github.com/ramyamut/E3-Pose.

