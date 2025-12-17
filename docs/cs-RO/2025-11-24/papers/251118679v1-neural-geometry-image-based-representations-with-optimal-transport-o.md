---
layout: default
title: Neural Geometry Image-Based Representations with Optimal Transport (OT)
---

# Neural Geometry Image-Based Representations with Optimal Transport (OT)

**arXiv**: [2511.18679v1](https://arxiv.org/abs/2511.18679) | [PDF](https://arxiv.org/pdf/2511.18679.pdf)

**作者**: Xiang Gao, Yuanpeng Liu, Xinmu Wang, Jiazhi Li, Minghao Guo, Yu Guo, Xiyun Song, Heather Yu, Zhiqiang Lao, Xianfeng David Gu

---

## 💡 一句话要点

**提出基于最优传输的神经几何图像表示，以高效存储和恢复3D网格。**

**关键词**: `神经表示` `几何图像` `最优传输` `3D网格压缩` `细节层次`

## 📋 核心要点

1. 核心问题：现有3D网格神经表示依赖复杂解码，计算成本高且结构不规则。
2. 方法要点：利用最优传输构建几何图像，实现单次前向解码和连续细节层次。
3. 实验或效果：在压缩比、Chamfer距离和Hausdorff距离上达到先进水平。

## 📄 摘要（原文）

> Neural representations for 3D meshes are emerging as an effective solution for compact storage and efficient processing. Existing methods often rely on neural overfitting, where a coarse mesh is stored and progressively refined through multiple decoder networks. While this can restore high-quality surfaces, it is computationally expensive due to successive decoding passes and the irregular structure of mesh data. In contrast, images have a regular structure that enables powerful super-resolution and restoration frameworks, but applying these advantages to meshes is difficult because their irregular connectivity demands complex encoder-decoder architectures. Our key insight is that a geometry image-based representation transforms irregular meshes into a regular image grid, making efficient image-based neural processing directly applicable. Building on this idea, we introduce our neural geometry image-based representation, which is decoder-free, storage-efficient, and naturally suited for neural processing. It stores a low-resolution geometry-image mipmap of the surface, from which high-quality meshes are restored in a single forward pass. To construct geometry images, we leverage Optimal Transport (OT), which resolves oversampling in flat regions and undersampling in feature-rich regions, and enables continuous levels of detail (LoD) through geometry-image mipmapping. Experimental results demonstrate state-of-the-art storage efficiency and restoration accuracy, measured by compression ratio (CR), Chamfer distance (CD), and Hausdorff distance (HD).

