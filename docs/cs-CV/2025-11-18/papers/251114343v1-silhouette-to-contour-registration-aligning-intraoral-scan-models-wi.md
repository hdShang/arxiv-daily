---
layout: default
title: Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs
---

# Silhouette-to-Contour Registration: Aligning Intraoral Scan Models with Cephalometric Radiographs

**arXiv**: [2511.14343v1](https://arxiv.org/abs/2511.14343) | [PDF](https://arxiv.org/pdf/2511.14343.pdf)

**作者**: Yiyi Miao, Taoyu Wu, Ji Jiang, Tong Chen, Zhe Tang, Zhengyong Jiang, Angelos Stefanidis, Limin Yu, Jionglong Su

---

## 💡 一句话要点

**提出DentalSCR框架，通过轮廓配准解决口腔扫描模型与头影测量X光片的3D-2D对齐问题。**

**关键词**: `轮廓配准` `3D-2D对齐` `口腔扫描` `头影测量X光片` `Chamfer距离` `UMDA坐标系`

## 📋 核心要点

1. 核心问题：传统强度配准方法在真实临床条件下不稳定，易因投影放大、几何失真等因素导致对齐失败。
2. 方法要点：构建UMDA坐标系稳定初始化，使用表面DRR生成投影，优化双向Chamfer距离实现轮廓配准。
3. 实验或效果：在34例临床数据上评估，显著降低标志点误差，提高对齐精度和鲁棒性。

## 📄 摘要（原文）

> Reliable 3D-2D alignment between intraoral scan (IOS) models and lateral cephalometric radiographs is critical for orthodontic diagnosis, yet conventional intensity-driven registration methods struggle under real clinical conditions, where cephalograms exhibit projective magnification, geometric distortion, low-contrast dental crowns, and acquisition-dependent variation. These factors hinder the stability of appearance-based similarity metrics and often lead to convergence failures or anatomically implausible alignments. To address these limitations, we propose DentalSCR, a pose-stable, contour-guided framework for accurate and interpretable silhouette-to-contour registration. Our method first constructs a U-Midline Dental Axis (UMDA) to establish a unified cross-arch anatomical coordinate system, thereby stabilizing initialization and standardizing projection geometry across cases. Using this reference frame, we generate radiograph-like projections via a surface-based DRR formulation with coronal-axis perspective and Gaussian splatting, which preserves clinical source-object-detector magnification and emphasizes external silhouettes. Registration is then formulated as a 2D similarity transform optimized with a symmetric bidirectional Chamfer distance under a hierarchical coarse-to-fine schedule, enabling both large capture range and subpixel-level contour agreement. We evaluate DentalSCR on 34 expert-annotated clinical cases. Experimental results demonstrate substantial reductions in landmark error-particularly at posterior teeth-tighter dispersion on the lower jaw, and low Chamfer and controlled Hausdorff distances at the curve level. These findings indicate that DentalSCR robustly handles real-world cephalograms and delivers high-fidelity, clinically inspectable 3D--2D alignment, outperforming conventional baselines.

