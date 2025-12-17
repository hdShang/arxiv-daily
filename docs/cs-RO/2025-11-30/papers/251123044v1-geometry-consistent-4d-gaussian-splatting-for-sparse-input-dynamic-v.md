---
layout: default
title: Geometry-Consistent 4D Gaussian Splatting for Sparse-Input Dynamic View Synthesis
---

# Geometry-Consistent 4D Gaussian Splatting for Sparse-Input Dynamic View Synthesis

**arXiv**: [2511.23044v1](https://arxiv.org/abs/2511.23044) | [PDF](https://arxiv.org/pdf/2511.23044.pdf)

**作者**: Yiwei Li, Jiannong Cao, Penghui Ruan, Divya Saxena, Songye Zhu, Yinfeng Cao

---

## 💡 一句话要点

**提出GC-4DGS框架，通过几何一致性增强解决稀疏输入动态视图合成质量下降问题**

**关键词**: `动态视图合成` `4D高斯泼溅` `几何一致性` `稀疏输入优化` `深度正则化` `边缘计算`

## 📋 核心要点

1. 核心问题：稀疏输入时4D高斯泼溅方法几何学习不连贯，导致渲染质量显著下降
2. 方法要点：引入动态一致性检查策略和全局-局部深度正则化，从单目深度中提取时空一致的几何信息
3. 实验效果：在N3DV和Technicolor数据集上PSNR指标优于RF-DeRF和原始4DGS，可在资源受限设备部署

## 📄 摘要（原文）

> Gaussian Splatting has been considered as a novel way for view synthesis of dynamic scenes, which shows great potential in AIoT applications such as digital twins. However, recent dynamic Gaussian Splatting methods significantly degrade when only sparse input views are available, limiting their applicability in practice. The issue arises from the incoherent learning of 4D geometry as input views decrease. This paper presents GC-4DGS, a novel framework that infuses geometric consistency into 4D Gaussian Splatting (4DGS), offering real-time and high-quality dynamic scene rendering from sparse input views. While learning-based Multi-View Stereo (MVS) and monocular depth estimators (MDEs) provide geometry priors, directly integrating these with 4DGS yields suboptimal results due to the ill-posed nature of sparse-input 4D geometric optimization. To address these problems, we introduce a dynamic consistency checking strategy to reduce estimation uncertainties of MVS across spacetime. Furthermore, we propose a global-local depth regularization approach to distill spatiotemporal-consistent geometric information from monocular depths, thereby enhancing the coherent geometry and appearance learning within the 4D volume. Extensive experiments on the popular N3DV and Technicolor datasets validate the effectiveness of GC-4DGS in rendering quality without sacrificing efficiency. Notably, our method outperforms RF-DeRF, the latest dynamic radiance field tailored for sparse-input dynamic view synthesis, and the original 4DGS by 2.62dB and 1.58dB in PSNR, respectively, with seamless deployability on resource-constrained IoT edge devices.

