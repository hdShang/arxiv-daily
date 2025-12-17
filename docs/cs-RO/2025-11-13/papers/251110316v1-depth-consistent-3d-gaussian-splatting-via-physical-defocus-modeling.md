---
layout: default
title: Depth-Consistent 3D Gaussian Splatting via Physical Defocus Modeling and Multi-View Geometric Supervision
---

# Depth-Consistent 3D Gaussian Splatting via Physical Defocus Modeling and Multi-View Geometric Supervision

**arXiv**: [2511.10316v1](https://arxiv.org/abs/2511.10316) | [PDF](https://arxiv.org/pdf/2511.10316.pdf)

**作者**: Yu Deng, Baozhu Zhao, Junyan Su, Xiaohan Zhang, Qi Liu

---

## 💡 一句话要点

**提出深度一致3D高斯泼溅方法，通过物理散焦建模和多视角几何监督解决极端深度变化场景重建问题**

**关键词**: `3D重建` `高斯泼溅` `深度估计` `多视角几何` `物理散焦建模` `城市环境`

## 📋 核心要点

1. 核心问题：极端深度变化场景中，近场和远场区域深度估计不一致导致重建质量下降
2. 方法要点：结合景深监督和多视角一致性监督，提升3D高斯泼溅的深度保真度
3. 实验或效果：在Waymo数据集上PSNR提升0.8 dB，优于现有方法

## 📄 摘要（原文）

> Three-dimensional reconstruction in scenes with extreme depth variations remains challenging due to inconsistent supervisory signals between near-field and far-field regions. Existing methods fail to simultaneously address inaccurate depth estimation in distant areas and structural degradation in close-range regions. This paper proposes a novel computational framework that integrates depth-of-field supervision and multi-view consistency supervision to advance 3D Gaussian Splatting. Our approach comprises two core components: (1) Depth-of-field Supervision employs a scale-recovered monocular depth estimator (e.g., Metric3D) to generate depth priors, leverages defocus convolution to synthesize physically accurate defocused images, and enforces geometric consistency through a novel depth-of-field loss, thereby enhancing depth fidelity in both far-field and near-field regions; (2) Multi-View Consistency Supervision employing LoFTR-based semi-dense feature matching to minimize cross-view geometric errors and enforce depth consistency via least squares optimization of reliable matched points. By unifying defocus physics with multi-view geometric constraints, our method achieves superior depth fidelity, demonstrating a 0.8 dB PSNR improvement over the state-of-the-art method on the Waymo Open Dataset. This framework bridges physical imaging principles and learning-based depth regularization, offering a scalable solution for complex depth stratification in urban environments.

