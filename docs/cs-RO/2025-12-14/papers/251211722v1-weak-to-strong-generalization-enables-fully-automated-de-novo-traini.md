---
layout: default
title: Weak-to-Strong Generalization Enables Fully Automated De Novo Training of Multi-head Mask-RCNN Model for Segmenting Densely Overlapping Cell Nuclei in Multiplex Whole-slice Brain Images
---

# Weak-to-Strong Generalization Enables Fully Automated De Novo Training of Multi-head Mask-RCNN Model for Segmenting Densely Overlapping Cell Nuclei in Multiplex Whole-slice Brain Images

**arXiv**: [2512.11722v1](https://arxiv.org/abs/2512.11722) | [PDF](https://arxiv.org/pdf/2512.11722.pdf)

**作者**: Lin Bai, Xiaoyang Li, Liqiang Huang, Quynh Nguyen, Hien Van Nguyen, Saurabh Prasad, Dragan Maric, John Redell, Pramod Dash, Badrinath Roysam

---

## 💡 一句话要点

**提出弱到强泛化方法，实现全自动训练多头Mask-RCNN，用于分割多重全切片脑图像中密集重叠细胞核。**

**关键词**: `细胞核分割` `弱到强泛化` `多头Mask-RCNN` `全切片图像` `自动化训练` `伪标签校正`

## 📋 核心要点

1. 核心问题：多重全切片脑图像中密集重叠细胞核的自动化分割，无需人工标注。
2. 方法要点：基于弱到强泛化，结合多头Mask-RCNN与高效通道注意力，支持伪标签校正和覆盖扩展。
3. 实验或效果：在基准测试中优于五种现有方法，提供代码和样本供社区使用。

## 📄 摘要（原文）

> We present a weak to strong generalization methodology for fully automated training of a multi-head extension of the Mask-RCNN method with efficient channel attention for reliable segmentation of overlapping cell nuclei in multiplex cyclic immunofluorescent (IF) whole-slide images (WSI), and present evidence for pseudo-label correction and coverage expansion, the key phenomena underlying weak to strong generalization. This method can learn to segment de novo a new class of images from a new instrument and/or a new imaging protocol without the need for human annotations. We also present metrics for automated self-diagnosis of segmentation quality in production environments, where human visual proofreading of massive WSI images is unaffordable. Our method was benchmarked against five current widely used methods and showed a significant improvement. The code, sample WSI images, and high-resolution segmentation results are provided in open form for community adoption and adaptation.

