---
layout: default
title: FUSER: Feed-Forward MUltiview 3D Registration Transformer and SE(3)$^N$ Diffusion Refinement
---

# FUSER: Feed-Forward MUltiview 3D Registration Transformer and SE(3)$^N$ Diffusion Refinement

**arXiv**: [2512.09373v1](https://arxiv.org/abs/2512.09373) | [PDF](https://arxiv.org/pdf/2512.09373.pdf)

**作者**: Haobo Jiang, Jin Xie, Jian Yang, Liang Yu, Jianmin Zheng

---

## 💡 一句话要点

**提出FUSER，首个前馈多视角点云配准Transformer，直接预测全局位姿，无需成对匹配。**

**关键词**: `多视角点云配准` `Transformer模型` `SE(3)扩散` `几何注意力` `前馈网络` `3D计算机视觉`

## 📋 核心要点

1. 多视角点云配准依赖成对匹配构建位姿图，计算昂贵且缺乏整体几何约束。
2. FUSER通过稀疏3D CNN编码超点特征，使用几何交替注意力模块进行高效推理，并引入SE(3)^N扩散框架FUSER-DF进行精炼。
3. 在3DMatch、ScanNet和ArkitScenes数据集上验证了优越的配准精度和计算效率。

## 📄 摘要（原文）

> Registration of multiview point clouds conventionally relies on extensive pairwise matching to build a pose graph for global synchronization, which is computationally expensive and inherently ill-posed without holistic geometric constraints. This paper proposes FUSER, the first feed-forward multiview registration transformer that jointly processes all scans in a unified, compact latent space to directly predict global poses without any pairwise estimation. To maintain tractability, FUSER encodes each scan into low-resolution superpoint features via a sparse 3D CNN that preserves absolute translation cues, and performs efficient intra- and inter-scan reasoning through a Geometric Alternating Attention module. Particularly, we transfer 2D attention priors from off-the-shelf foundation models to enhance 3D feature interaction and geometric consistency. Building upon FUSER, we further introduce FUSER-DF, an SE(3)$^N$ diffusion refinement framework to correct FUSER's estimates via denoising in the joint SE(3)$^N$ space. FUSER acts as a surrogate multiview registration model to construct the denoiser, and a prior-conditioned SE(3)$^N$ variational lower bound is derived for denoising supervision. Extensive experiments on 3DMatch, ScanNet and ArkitScenes demonstrate that our approach achieves the superior registration accuracy and outstanding computational efficiency.

