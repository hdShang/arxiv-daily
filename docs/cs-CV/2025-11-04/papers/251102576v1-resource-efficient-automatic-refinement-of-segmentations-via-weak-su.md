---
layout: default
title: Resource-efficient Automatic Refinement of Segmentations via Weak Supervision from Light Feedback
---

# Resource-efficient Automatic Refinement of Segmentations via Weak Supervision from Light Feedback

**arXiv**: [2511.02576v1](https://arxiv.org/abs/2511.02576) | [PDF](https://arxiv.org/pdf/2511.02576.pdf)

**作者**: Alix de Langlais, Benjamin Billot, Théo Aguilar Vidal, Marc-Olivier Gauci, Hervé Delingette

---

## 💡 一句话要点

**提出SCORE框架，通过弱监督从轻量反馈中自动优化医学图像分割**

**关键词**: `医学图像分割` `弱监督学习` `分割优化` `资源效率` `CT扫描`

## 📋 核心要点

1. 医学图像分割依赖手动标注，耗时且易变，自动方法常需重监督或用户交互
2. SCORE引入基于区域质量评分和过/欠分割误差的弱监督损失，减少训练标注需求
3. 在肱骨CT扫描中，SCORE显著提升初始分割，性能媲美现有方法，降低监督成本

## 📄 摘要（原文）

> Delineating anatomical regions is a key task in medical image analysis.
> Manual segmentation achieves high accuracy but is labor-intensive and prone to
> variability, thus prompting the development of automated approaches. Recently,
> a breadth of foundation models has enabled automated segmentations across
> diverse anatomies and imaging modalities, but these may not always meet the
> clinical accuracy standards. While segmentation refinement strategies can
> improve performance, current methods depend on heavy user interactions or
> require fully supervised segmentations for training. Here, we present SCORE
> (Segmentation COrrection from Regional Evaluations), a weakly supervised
> framework that learns to refine mask predictions only using light feedback
> during training. Specifically, instead of relying on dense training image
> annotations, SCORE introduces a novel loss that leverages region-wise quality
> scores and over/under-segmentation error labels. We demonstrate SCORE on
> humerus CT scans, where it considerably improves initial predictions from
> TotalSegmentator, and achieves performance on par with existing refinement
> methods, while greatly reducing their supervision requirements and annotation
> time. Our code is available at: https://gitlab.inria.fr/adelangl/SCORE.

