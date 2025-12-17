---
layout: default
title: SymGS : Leveraging Local Symmetries for 3D Gaussian Splatting Compression
---

# SymGS : Leveraging Local Symmetries for 3D Gaussian Splatting Compression

**arXiv**: [2511.13264v1](https://arxiv.org/abs/2511.13264) | [PDF](https://arxiv.org/pdf/2511.13264.pdf)

**作者**: Keshav Gupta, Akshat Sanghvi, Shreyas Reddy Palley, Astitva Srivastava, Charu Sharma, Avinash Sharma

---

## 💡 一句话要点

**提出SymGS框架，利用局部对称性压缩3D高斯泼溅场景**

**关键词**: `3D高斯泼溅` `场景压缩` `对称性利用` `可学习镜像` `渲染优化`

## 📋 核心要点

1. 3D高斯泼溅内存占用高，随场景复杂度快速增加
2. 引入可学习镜像，消除局部和全局反射冗余以压缩
3. 在基准数据集上平均实现108倍压缩，保持渲染质量

## 📄 摘要（原文）

> 3D Gaussian Splatting has emerged as a transformative technique in novel view synthesis, primarily due to its high rendering speed and photorealistic fidelity. However, its memory footprint scales rapidly with scene complexity, often reaching several gigabytes. Existing methods address this issue by introducing compression strategies that exploit primitive-level redundancy through similarity detection and quantization. We aim to surpass the compression limits of such methods by incorporating symmetry-aware techniques, specifically targeting mirror symmetries to eliminate redundant primitives. We propose a novel compression framework, \textbf{\textit{SymGS}}, introducing learnable mirrors into the scene, thereby eliminating local and global reflective redundancies for compression. Our framework functions as a plug-and-play enhancement to state-of-the-art compression methods, (e.g. HAC) to achieve further compression. Compared to HAC, we achieve $1.66 \times$ compression across benchmark datasets (upto $3\times$ on large-scale scenes). On an average, SymGS enables $\bf{108\times}$ compression of a 3DGS scene, while preserving rendering quality. The project page and supplementary can be found at \textbf{\color{cyan}{symgs.github.io}}

