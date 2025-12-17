---
layout: default
title: SuperQuadricOcc: Multi-Layer Gaussian Approximation of Superquadrics for Real-Time Self-Supervised Occupancy Estimation
---

# SuperQuadricOcc: Multi-Layer Gaussian Approximation of Superquadrics for Real-Time Self-Supervised Occupancy Estimation

**arXiv**: [2511.17361v1](https://arxiv.org/abs/2511.17361) | [PDF](https://arxiv.org/pdf/2511.17361.pdf)

**作者**: Seamie Hayes, Reenu Mohandas, Tim Brophy, Alexandre Boulch, Ganesh Sistu, Ciaran Eising

---

## 💡 一句话要点

**提出SuperQuadricOcc以解决自动驾驶中实时语义占据估计的内存和速度问题**

**关键词**: `语义占据估计` `超二次曲面` `高斯近似` `自监督学习` `实时推理` `自动驾驶`

## 📋 核心要点

1. 高斯表示在自监督占据估计中内存需求高，不适合实时推理
2. 使用超二次曲面减少基元数量，并通过多层高斯近似实现监督训练
3. 在Occ3D数据集上内存减少75%，推理加速124%，mIoU提升5.9%

## 📄 摘要（原文）

> Semantic occupancy estimation enables comprehensive scene understanding for automated driving, providing dense spatial and semantic information essential for perception and planning. While Gaussian representations have been widely adopted in self-supervised occupancy estimation, the deployment of a large number of Gaussian primitives drastically increases memory requirements and is not suitable for real-time inference. In contrast, superquadrics permit reduced primitive count and lower memory requirements due to their diverse shape set. However, implementation into a self-supervised occupancy model is nontrivial due to the absence of a superquadric rasterizer to enable model supervision. Our proposed method, SuperQuadricOcc, employs a superquadric-based scene representation. By leveraging a multi-layer icosphere-tessellated Gaussian approximation of superquadrics, we enable Gaussian rasterization for supervision during training. On the Occ3D dataset, SuperQuadricOcc achieves a 75\% reduction in memory footprint, 124\% faster inference, and a 5.9\% improvement in mIoU compared to previous Gaussian-based methods, without the use of temporal labels. To our knowledge, this is the first occupancy model to enable real-time inference while maintaining competitive performance. The use of superquadrics reduces the number of primitives required for scene modeling by 84\% relative to Gaussian-based approaches. Finally, evaluation against prior methods is facilitated by our fast superquadric voxelization module. The code will be released as open source.

