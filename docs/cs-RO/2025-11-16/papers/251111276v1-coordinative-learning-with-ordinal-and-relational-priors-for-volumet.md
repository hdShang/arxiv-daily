---
layout: default
title: Coordinative Learning with Ordinal and Relational Priors for Volumetric Medical Image Segmentation
---

# Coordinative Learning with Ordinal and Relational Priors for Volumetric Medical Image Segmentation

**arXiv**: [2511.11276v1](https://arxiv.org/abs/2511.11276) | [PDF](https://arxiv.org/pdf/2511.11276.pdf)

**作者**: Haoyi Wang

---

## 💡 一句话要点

**提出CORAL方法以解决体医学图像分割中解剖结构建模不足的问题**

**关键词**: `体医学图像分割` `对比学习` `序数学习` `解剖结构建模` `有限标注学习`

## 📋 核心要点

1. 核心问题：现有方法依赖硬阈值定义样本，忽略连续解剖相似性和全局方向一致性
2. 方法要点：结合对比排序和序数目标，学习局部和全局解剖结构关系
3. 实验或效果：在有限标注下，基准数据集上达到先进性能，代码已开源

## 📄 摘要（原文）

> Volumetric medical image segmentation presents unique challenges due to the inherent anatomical structure and limited availability of annotations. While recent methods have shown promise by contrasting spatial relationships between slices, they rely on hard binary thresholds to define positive and negative samples, thereby discarding valuable continuous information about anatomical similarity. Moreover, these methods overlook the global directional consistency of anatomical progression, resulting in distorted feature spaces that fail to capture the canonical anatomical manifold shared across patients. To address these limitations, we propose Coordinative Ordinal-Relational Anatomical Learning (CORAL) to capture both local and global structure in volumetric images. First, CORAL employs a contrastive ranking objective to leverage continuous anatomical similarity, ensuring relational feature distances between slices are proportional to their anatomical position differences. In addition, CORAL incorporates an ordinal objective to enforce global directional consistency, aligning the learned feature distribution with the canonical anatomical progression across patients. Learning these inter-slice relationships produces anatomically informed representations that benefit the downstream segmentation task. Through this coordinative learning framework, CORAL achieves state-of-the-art performance on benchmark datasets under limited-annotation settings while learning representations with meaningful anatomical structure. Code is available at https://github.com/haoyiwang25/CORAL.

