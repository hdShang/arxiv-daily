---
layout: default
title: SVRecon: Sparse Voxel Rasterization for Surface Reconstruction
---

# SVRecon: Sparse Voxel Rasterization for Surface Reconstruction

**arXiv**: [2511.17364v1](https://arxiv.org/abs/2511.17364) | [PDF](https://arxiv.org/pdf/2511.17364.pdf)

**作者**: Seunghun Oh, Jaesung Choe, Dongjae Lee, Daeun Lee, Seunghoon Jeong, Yu-Chiang Frank Wang, Jaesik Park

---

## 💡 一句话要点

**提出SVRecon方法，通过稀疏体素光栅化实现高保真表面重建**

**关键词**: `表面重建` `稀疏体素光栅化` `符号距离函数` `几何优化` `体素平滑性`

## 📋 核心要点

1. 核心问题：稀疏体素在优化中易陷入局部极小，且难以保持跨体素的平滑性。
2. 方法要点：结合SDF，采用几何初始化和空间平滑损失促进体素间一致性。
3. 实验或效果：在多个基准测试中实现高重建精度和快速收敛。

## 📄 摘要（原文）

> We extend the recently proposed sparse voxel rasterization paradigm to the task of high-fidelity surface reconstruction by integrating Signed Distance Function (SDF), named SVRecon. Unlike 3D Gaussians, sparse voxels are spatially disentangled from their neighbors and have sharp boundaries, which makes them prone to local minima during optimization. Although SDF values provide a naturally smooth and continuous geometric field, preserving this smoothness across independently parameterized sparse voxels is nontrivial. To address this challenge, we promote coherent and smooth voxel-wise structure through (1) robust geometric initialization using a visual geometry model and (2) a spatial smoothness loss that enforces coherent relationships across parent-child and sibling voxel groups. Extensive experiments across various benchmarks show that our method achieves strong reconstruction accuracy while having consistently speedy convergence. The code will be made public.

