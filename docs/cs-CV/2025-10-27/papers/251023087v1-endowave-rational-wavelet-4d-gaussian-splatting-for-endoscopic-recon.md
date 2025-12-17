---
layout: default
title: EndoWave: Rational-Wavelet 4D Gaussian Splatting for Endoscopic Reconstruction
---

# EndoWave: Rational-Wavelet 4D Gaussian Splatting for Endoscopic Reconstruction

**arXiv**: [2510.23087v1](https://arxiv.org/abs/2510.23087) | [PDF](https://arxiv.org/pdf/2510.23087.pdf)

**作者**: Taoyu Wu, Yiyi Miao, Jiaxin Guo, Ziyan Chen, Sihang Zhao, Zhuoxiao Li, Zhe Tang, Baoru Huang, Limin Yu

---

## 💡 一句话要点

**提出EndoWave框架，结合光流与多分辨率小波监督，优化内窥镜4D重建。**

**关键词**: `内窥镜重建` `4D高斯溅射` `光流约束` `多分辨率小波` `时空一致性`

## 📋 核心要点

1. 内窥镜场景存在光度不一致、非刚性运动和视点高光，误导3DGS优化。
2. 采用4D高斯表示，引入光流几何约束和多分辨率有理小波监督。
3. 在EndoNeRF和StereoMIS数据集上，实现SOTA重建质量和视觉精度。

## 📄 摘要（原文）

> In robot-assisted minimally invasive surgery, accurate 3D reconstruction from
> endoscopic video is vital for downstream tasks and improved outcomes. However,
> endoscopic scenarios present unique challenges, including photometric
> inconsistencies, non-rigid tissue motion, and view-dependent highlights. Most
> 3DGS-based methods that rely solely on appearance constraints for optimizing
> 3DGS are often insufficient in this context, as these dynamic visual artifacts
> can mislead the optimization process and lead to inaccurate reconstructions. To
> address these limitations, we present EndoWave, a unified spatio-temporal
> Gaussian Splatting framework by incorporating an optical flow-based geometric
> constraint and a multi-resolution rational wavelet supervision. First, we adopt
> a unified spatio-temporal Gaussian representation that directly optimizes
> primitives in a 4D domain. Second, we propose a geometric constraint derived
> from optical flow to enhance temporal coherence and effectively constrain the
> 3D structure of the scene. Third, we propose a multi-resolution rational
> orthogonal wavelet as a constraint, which can effectively separate the details
> of the endoscope and enhance the rendering performance. Extensive evaluations
> on two real surgical datasets, EndoNeRF and StereoMIS, demonstrate that our
> method EndoWave achieves state-of-the-art reconstruction quality and visual
> accuracy compared to the baseline method.

