---
layout: default
title: Top2Ground: A Height-Aware Dual Conditioning Diffusion Model for Robust Aerial-to-Ground View Generation
---

# Top2Ground: A Height-Aware Dual Conditioning Diffusion Model for Robust Aerial-to-Ground View Generation

**arXiv**: [2511.08258v1](https://arxiv.org/abs/2511.08258) | [PDF](https://arxiv.org/pdf/2511.08258.pdf)

**作者**: Jae Joong Lee, Bedrich Benes

---

## 💡 一句话要点

**提出Top2Ground扩散模型，从航拍图像生成地面视图，解决视角差异和遮挡问题。**

**关键词**: `航拍图像生成` `扩散模型` `视图转换` `几何约束` `语义一致性`

## 📋 核心要点

1. 核心问题：航拍到地面视图生成因视角差异、遮挡和视野限制而困难。
2. 方法要点：使用VAE空间特征和CLIP语义嵌入联合调节扩散过程，无需中间表示。
3. 实验或效果：在三个数据集上平均SSIM提升7.3%，展示强泛化能力。

## 📄 摘要（原文）

> Generating ground-level images from aerial views is a challenging task due to extreme viewpoint disparity, occlusions, and a limited field of view. We introduce Top2Ground, a novel diffusion-based method that directly generates photorealistic ground-view images from aerial input images without relying on intermediate representations such as depth maps or 3D voxels. Specifically, we condition the denoising process on a joint representation of VAE-encoded spatial features (derived from aerial RGB images and an estimated height map) and CLIP-based semantic embeddings. This design ensures the generation is both geometrically constrained by the scene's 3D structure and semantically consistent with its content. We evaluate Top2Ground on three diverse datasets: CVUSA, CVACT, and the Auto Arborist. Our approach shows 7.3% average improvement in SSIM across three benchmark datasets, showing Top2Ground can robustly handle both wide and narrow fields of view, highlighting its strong generalization capabilities.

