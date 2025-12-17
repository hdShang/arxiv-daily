---
layout: default
title: SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction
---

# SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction

**arXiv**: [2511.14633v1](https://arxiv.org/abs/2511.14633) | [PDF](https://arxiv.org/pdf/2511.14633.pdf)

**作者**: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai

---

## 💡 一句话要点

**提出SparseSurf方法以解决稀疏视图下3D高斯溅射的表面重建过拟合问题**

**关键词**: `稀疏视图重建` `3D高斯溅射` `表面重建` `几何一致性` `视图合成`

## 📋 核心要点

1. 核心问题：稀疏视图导致高斯溅射优化过拟合，重建质量下降
2. 方法要点：引入立体几何-纹理对齐和伪特征增强几何一致性，联合优化重建与渲染
3. 实验或效果：在DTU等数据集上实现最先进性能，提升表面细节和视图合成质量

## 📄 摘要（原文）

> Recent advances in optimizing Gaussian Splatting for scene geometry have enabled efficient reconstruction of detailed surfaces from images. However, when input views are sparse, such optimization is prone to overfitting, leading to suboptimal reconstruction quality. Existing approaches address this challenge by employing flattened Gaussian primitives to better fit surface geometry, combined with depth regularization to alleviate geometric ambiguities under limited viewpoints. Nevertheless, the increased anisotropy inherent in flattened Gaussians exacerbates overfitting in sparse-view scenarios, hindering accurate surface fitting and degrading novel view synthesis performance. In this paper, we propose \net{}, a method that reconstructs more accurate and detailed surfaces while preserving high-quality novel view rendering. Our key insight is to introduce Stereo Geometry-Texture Alignment, which bridges rendering quality and geometry estimation, thereby jointly enhancing both surface reconstruction and view synthesis. In addition, we present a Pseudo-Feature Enhanced Geometry Consistency that enforces multi-view geometric consistency by incorporating both training and unseen views, effectively mitigating overfitting caused by sparse supervision. Extensive experiments on the DTU, BlendedMVS, and Mip-NeRF360 datasets demonstrate that our method achieves the state-of-the-art performance.

