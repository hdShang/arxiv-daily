---
layout: default
title: R2MF-Net: A Recurrent Residual Multi-Path Fusion Network for Robust Multi-directional Spine X-ray Segmentation
---

# R2MF-Net: A Recurrent Residual Multi-Path Fusion Network for Robust Multi-directional Spine X-ray Segmentation

**arXiv**: [2512.07576v1](https://arxiv.org/abs/2512.07576) | [PDF](https://arxiv.org/pdf/2512.07576.pdf)

**作者**: Xuecheng Li, Weikuan Jia, Komildzhon Sharipov, Sharipov Hotam Beknazarovich, Farzona S. Ataeva, Qurbonaliev Alisher, Yuanjie Zheng

---

## 💡 一句话要点

**提出R2MF-Net以解决多方向脊柱X光图像分割中的低对比度和噪声干扰问题。**

**关键词**: `脊柱X光分割` `多方向图像处理` `级联网络` `语义对齐` `特征融合`

## 📋 核心要点

1. 核心问题：脊柱X光图像分割在低对比度、肋骨阴影和组织重叠下困难，手动分割耗时且不可重复。
2. 方法要点：采用级联网络，结合改进的Inception多分支特征提取器、R2-Jump模块和MC-Skip机制增强语义对齐和稳定性。
3. 实验或效果：在包含228组多视图X光图像的临床数据集上评估，未知具体性能指标。

## 📄 摘要（原文）

> Accurate segmentation of spinal structures in X-ray images is a prerequisite for quantitative scoliosis assessment, including Cobb angle measurement, vertebral translation estimation and curvature classification. In routine practice, clinicians acquire coronal, left-bending and right-bending radiographs to jointly evaluate deformity severity and spinal flexibility. However, the segmentation step remains heavily manual, time-consuming and non-reproducible, particularly in low-contrast images and in the presence of rib shadows or overlapping tissues. To address these limitations, this paper proposes R2MF-Net, a recurrent residual multi-path encoder--decoder network tailored for automatic segmentation of multi-directional spine X-ray images. The overall design consists of a coarse segmentation network and a fine segmentation network connected in cascade. Both stages adopt an improved Inception-style multi-branch feature extractor, while a recurrent residual jump connection (R2-Jump) module is inserted into skip paths to gradually align encoder and decoder semantics. A multi-scale cross-stage skip (MC-Skip) mechanism allows the fine network to reuse hierarchical representations from multiple decoder levels of the coarse network, thereby strengthening the stability of segmentation across imaging directions and contrast conditions. Furthermore, a lightweight spatial-channel squeeze-and-excitation block (SCSE-Lite) is employed at the bottleneck to emphasize spine-related activations and suppress irrelevant structures and background noise. We evaluate R2MF-Net on a clinical multi-view radiograph dataset comprising 228 sets of coronal, left-bending and right-bending spine X-ray images with expert annotations.

