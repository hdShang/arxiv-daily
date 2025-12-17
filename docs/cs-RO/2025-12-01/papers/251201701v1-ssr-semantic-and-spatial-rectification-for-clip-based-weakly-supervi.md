---
layout: default
title: SSR: Semantic and Spatial Rectification for CLIP-based Weakly Supervised Segmentation
---

# SSR: Semantic and Spatial Rectification for CLIP-based Weakly Supervised Segmentation

**arXiv**: [2512.01701v1](https://arxiv.org/abs/2512.01701) | [PDF](https://arxiv.org/pdf/2512.01701.pdf)

**作者**: Xiuli Bi, Die Xiao, Junchao Fan, Bin Xiao

---

## 💡 一句话要点

**提出语义与空间校正方法以解决CLIP弱监督分割中的过激活问题**

**关键词**: `弱监督语义分割` `CLIP模型` `跨模态对齐` `超像素引导` `语义校正` `空间校正`

## 📋 核心要点

1. 针对CLIP弱监督分割中非目标前景和背景区域的过激活问题
2. 通过跨模态原型对齐和超像素引导校正进行语义与空间校正
3. 在PASCAL VOC和MS COCO数据集上取得领先的mIoU分数

## 📄 摘要（原文）

> In recent years, Contrastive Language-Image Pretraining (CLIP) has been widely applied to Weakly Supervised Semantic Segmentation (WSSS) tasks due to its powerful cross-modal semantic understanding capabilities. This paper proposes a novel Semantic and Spatial Rectification (SSR) method to address the limitations of existing CLIP-based weakly supervised semantic segmentation approaches: over-activation in non-target foreground regions and background areas. Specifically, at the semantic level, the Cross-Modal Prototype Alignment (CMPA) establishes a contrastive learning mechanism to enforce feature space alignment across modalities, reducing inter-class overlap while enhancing semantic correlations, to rectify over-activation in non-target foreground regions effectively; at the spatial level, the Superpixel-Guided Correction (SGC) leverages superpixel-based spatial priors to precisely filter out interference from non-target regions during affinity propagation, significantly rectifying background over-activation. Extensive experiments on the PASCAL VOC and MS COCO datasets demonstrate that our method outperforms all single-stage approaches, as well as more complex multi-stage approaches, achieving mIoU scores of 79.5% and 50.6%, respectively.

