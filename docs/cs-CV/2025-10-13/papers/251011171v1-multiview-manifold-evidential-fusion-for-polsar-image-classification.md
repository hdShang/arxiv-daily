---
layout: default
title: Multiview Manifold Evidential Fusion for PolSAR Image Classification
---

# Multiview Manifold Evidential Fusion for PolSAR Image Classification

**arXiv**: [2510.11171v1](https://arxiv.org/abs/2510.11171) | [PDF](https://arxiv.org/pdf/2510.11171.pdf)

**作者**: Junfei Shi, Haojia Zhang, Haiyan Jin, Junhuai Li, Xiaogang Song, Yuanfan Guo, Haonan Su, Weisi Lin

---

## 💡 一句话要点

**提出多流形证据融合方法以提升PolSAR图像分类的可靠性和可解释性**

**关键词**: `PolSAR图像分类` `多视图融合` `流形学习` `证据理论` `不确定性量化` `深度学习`

## 📋 核心要点

1. 传统融合方法忽略多视图的几何差异和不确定性，导致分类不可靠
2. 构建HPD和Grassmann流形表示，结合证据融合估计置信度和不确定性
3. 在三个真实数据集上验证，方法在精度、鲁棒性和可解释性上优于现有方法

## 📄 摘要（原文）

> Polarimetric Synthetic Aperture Radar (PolSAR) covariance matrices and their
> extracted multi-features - such as scattering angle, entropy, texture, and
> boundary descriptors - provide complementary and physically interpretable
> information for image classification. Traditional fusion strategies typically
> concatenate these features or employ deep learning networks to combine them.
> However, the covariance matrices and multi-features, as two complementary
> views, lie on different manifolds with distinct geometric structures. Existing
> fusion methods also overlook the varying importance of different views and
> ignore uncertainty, often leading to unreliable predictions. To address these
> issues, we propose a Multiview Manifold Evidential Fusion (MMEFnet) method to
> effectively fuse these two views. It gives a new framework to integrate PolSAR
> manifold learning and evidence fusion into a unified architecture.
> Specifically, covariance matrices are represented on the Hermitian Positive
> Definite (HPD) manifold, while multi-features are modeled on the Grassmann
> manifold. Two different kernel metric learning networks are constructed to
> learn their manifold representations. Subsequently, a trusted multiview
> evidence fusion, replacing the conventional softmax classifier, estimates
> belief mass and quantifies the uncertainty of each view from the learned deep
> features. Finally, a Dempster-Shafer theory-based fusion strategy combines
> evidence, enabling a more reliable and interpretable classification. Extensive
> experiments on three real-world PolSAR datasets demonstrate that the proposed
> method consistently outperforms existing approaches in accuracy, robustness,
> and interpretability.

