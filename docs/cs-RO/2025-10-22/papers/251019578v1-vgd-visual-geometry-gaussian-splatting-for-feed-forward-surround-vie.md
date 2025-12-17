---
layout: default
title: VGD: Visual Geometry Gaussian Splatting for Feed-Forward Surround-view Driving Reconstruction
---

# VGD: Visual Geometry Gaussian Splatting for Feed-Forward Surround-view Driving Reconstruction

**arXiv**: [2510.19578v1](https://arxiv.org/abs/2510.19578) | [PDF](https://arxiv.org/pdf/2510.19578.pdf)

**作者**: Junhong Lin, Kangli Wang, Shunzhou Wang, Songlin Fan, Ge Li, Wei Gao

---

## 💡 一句话要点

**提出VGD框架以解决环视驾驶场景重建中的几何一致性与新视图质量问题**

**关键词**: `环视驾驶重建` `几何一致性` `高斯渲染` `多尺度特征融合` `前馈学习`

## 📋 核心要点

1. 环视驾驶场景重建中，视图重叠少导致几何一致性与新视图质量难以保证
2. 采用轻量VGGT变体提取几何先验，并设计高斯头融合多尺度几何特征预测渲染参数
3. 在nuScenes数据集上验证，VGD在客观指标和主观质量上优于现有方法

## 📄 摘要（原文）

> Feed-forward surround-view autonomous driving scene reconstruction offers
> fast, generalizable inference ability, which faces the core challenge of
> ensuring generalization while elevating novel view quality. Due to the
> surround-view with minimal overlap regions, existing methods typically fail to
> ensure geometric consistency and reconstruction quality for novel views. To
> tackle this tension, we claim that geometric information must be learned
> explicitly, and the resulting features should be leveraged to guide the
> elevating of semantic quality in novel views. In this paper, we introduce
> \textbf{Visual Gaussian Driving (VGD)}, a novel feed-forward end-to-end
> learning framework designed to address this challenge. To achieve generalizable
> geometric estimation, we design a lightweight variant of the VGGT architecture
> to efficiently distill its geometric priors from the pre-trained VGGT to the
> geometry branch. Furthermore, we design a Gaussian Head that fuses multi-scale
> geometry tokens to predict Gaussian parameters for novel view rendering, which
> shares the same patch backbone as the geometry branch. Finally, we integrate
> multi-scale features from both geometry and Gaussian head branches to jointly
> supervise a semantic refinement model, optimizing rendering quality through
> feature-consistent learning. Experiments on nuScenes demonstrate that our
> approach significantly outperforms state-of-the-art methods in both objective
> metrics and subjective quality under various settings, which validates VGD's
> scalability and high-fidelity surround-view reconstruction.

