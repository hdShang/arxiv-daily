---
layout: default
title: KeyPointDiffuser: Unsupervised 3D Keypoint Learning via Latent Diffusion Models
---

# KeyPointDiffuser: Unsupervised 3D Keypoint Learning via Latent Diffusion Models

**arXiv**: [2512.03450v1](https://arxiv.org/abs/2512.03450) | [PDF](https://arxiv.org/pdf/2512.03450.pdf)

**作者**: Rhys Newbury, Juyan Zhang, Tin Tran, Hanna Kurniawati, Dana Kulić

---

## 💡 一句话要点

**提出KeyPointDiffuser，通过潜在扩散模型无监督学习3D关键点以增强生成能力**

**关键词**: `无监督学习` `3D关键点检测` `扩散模型` `点云处理` `生成式AI`

## 📋 核心要点

1. 核心问题：现有无监督关键点方法不适用于无条件生成场景，限制在3D生成流程中的应用
2. 方法要点：从点云数据学习空间结构化3D关键点，作为紧凑表示条件化扩散模型重建完整形状
3. 实验或效果：在多样对象类别上表现优异，关键点一致性比先前方法提升6个百分点

## 📄 摘要（原文）

> Understanding and representing the structure of 3D objects in an unsupervised manner remains a core challenge in computer vision and graphics. Most existing unsupervised keypoint methods are not designed for unconditional generative settings, restricting their use in modern 3D generative pipelines; our formulation explicitly bridges this gap. We present an unsupervised framework for learning spatially structured 3D keypoints from point cloud data. These keypoints serve as a compact and interpretable representation that conditions an Elucidated Diffusion Model (EDM) to reconstruct the full shape. The learned keypoints exhibit repeatable spatial structure across object instances and support smooth interpolation in keypoint space, indicating that they capture geometric variation. Our method achieves strong performance across diverse object categories, yielding a 6 percentage-point improvement in keypoint consistency compared to prior approaches.

