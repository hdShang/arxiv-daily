---
layout: default
title: Region-CAM: Towards Accurate Object Regions in Class Activation Maps for Weakly Supervised Learning Tasks
---

# Region-CAM: Towards Accurate Object Regions in Class Activation Maps for Weakly Supervised Learning Tasks

**arXiv**: [2510.25134v1](https://arxiv.org/abs/2510.25134) | [PDF](https://arxiv.org/pdf/2510.25134.pdf)

**作者**: Qingdong Cai, Charith Abhayaratne

---

## 💡 一句话要点

**提出Region-CAM以解决弱监督学习中类激活图覆盖不全和边界不准的问题**

**关键词**: `类激活图` `弱监督学习` `语义分割` `对象定位` `语义信息传播`

## 📋 核心要点

1. 传统CAM方法仅突出目标最具区分性区域，导致覆盖不全和边界错位，影响弱监督语义分割性能
2. Region-CAM通过提取语义信息图和语义信息传播，结合梯度和特征，生成更完整且边界精确的激活图
3. 在PASCAL VOC和MS COCO数据集上，mIoU显著提升；在ILSVRC2012上，定位准确率优于LayerCAM

## 📄 摘要（原文）

> Class Activation Mapping (CAM) methods are widely applied in weakly
> supervised learning tasks due to their ability to highlight object regions.
> However, conventional CAM methods highlight only the most discriminative
> regions of the target. These highlighted regions often fail to cover the entire
> object and are frequently misaligned with object boundaries, thereby limiting
> the performance of downstream weakly supervised learning tasks, particularly
> Weakly Supervised Semantic Segmentation (WSSS), which demands pixel-wise
> accurate activation maps to get the best results. To alleviate the above
> problems, we propose a novel activation method, Region-CAM. Distinct from
> network feature weighting approaches, Region-CAM generates activation maps by
> extracting semantic information maps (SIMs) and performing semantic information
> propagation (SIP) by considering both gradients and features in each of the
> stages of the baseline classification model. Our approach highlights a greater
> proportion of object regions while ensuring activation maps to have precise
> boundaries that align closely with object edges. Region-CAM achieves 60.12% and
> 58.43% mean intersection over union (mIoU) using the baseline model on the
> PASCAL VOC training and validation datasets, respectively, which are
> improvements of 13.61% and 13.13% over the original CAM (46.51% and 45.30%). On
> the MS COCO validation set, Region-CAM achieves 36.38%, a 16.23% improvement
> over the original CAM (20.15%). We also demonstrate the superiority of
> Region-CAM in object localization tasks, using the ILSVRC2012 validation set.
> Region-CAM achieves 51.7% in Top-1 Localization accuracy Loc1. Compared with
> LayerCAM, an activation method designed for weakly supervised object
> localization, Region-CAM achieves 4.5% better performance in Loc1.

