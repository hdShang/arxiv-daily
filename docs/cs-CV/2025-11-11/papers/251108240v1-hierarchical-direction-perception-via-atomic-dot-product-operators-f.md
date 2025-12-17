---
layout: default
title: Hierarchical Direction Perception via Atomic Dot-Product Operators for Rotation-Invariant Point Clouds Learning
---

# Hierarchical Direction Perception via Atomic Dot-Product Operators for Rotation-Invariant Point Clouds Learning

**arXiv**: [2511.08240v1](https://arxiv.org/abs/2511.08240) | [PDF](https://arxiv.org/pdf/2511.08240.pdf)

**作者**: Chenyu Hu, Xiaotong Li, Hao Zhu, Biao Hou

---

## 💡 一句话要点

**提出DiPVNet以解决点云旋转不变性学习中的方向感知问题**

**关键词**: `点云处理` `旋转不变性` `方向感知` `原子点积算子` `球形傅里叶变换`

## 📋 核心要点

1. 点云旋转导致方向特征破坏，影响表示学习
2. 使用原子点积算子实现旋转不变性和自适应方向感知
3. 在噪声和大角度旋转场景下实现SOTA分类与分割性能

## 📄 摘要（原文）

> Point cloud processing has become a cornerstone technology in many 3D vision tasks. However, arbitrary rotations introduce variations in point cloud orientations, posing a long-standing challenge for effective representation learning. The core of this issue is the disruption of the point cloud's intrinsic directional characteristics caused by rotational perturbations. Recent methods attempt to implicitly model rotational equivariance and invariance, preserving directional information and propagating it into deep semantic spaces. Yet, they often fall short of fully exploiting the multiscale directional nature of point clouds to enhance feature representations. To address this, we propose the Direction-Perceptive Vector Network (DiPVNet). At its core is an atomic dot-product operator that simultaneously encodes directional selectivity and rotation invariance--endowing the network with both rotational symmetry modeling and adaptive directional perception. At the local level, we introduce a Learnable Local Dot-Product (L2DP) Operator, which enables interactions between a center point and its neighbors to adaptively capture the non-uniform local structures of point clouds. At the global level, we leverage generalized harmonic analysis to prove that the dot-product between point clouds and spherical sampling vectors is equivalent to a direction-aware spherical Fourier transform (DASFT). This leads to the construction of a global directional response spectrum for modeling holistic directional structures. We rigorously prove the rotation invariance of both operators. Extensive experiments on challenging scenarios involving noise and large-angle rotations demonstrate that DiPVNet achieves state-of-the-art performance on point cloud classification and segmentation tasks. Our code is available at https://github.com/wxszreal0/DiPVNet.

