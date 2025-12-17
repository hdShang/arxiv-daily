---
layout: default
title: Improving Cross-Patient Generalization in Parkinson's Disease Detection through Chunk-Based Analysis of Hand-Drawn Patterns
---

# Improving Cross-Patient Generalization in Parkinson's Disease Detection through Chunk-Based Analysis of Hand-Drawn Patterns

**arXiv**: [2510.17703v1](https://arxiv.org/abs/2510.17703) | [PDF](https://arxiv.org/pdf/2510.17703.pdf)

**作者**: Mhd Adnan Albani, Riad Sonbol

---

## 💡 一句话要点

**提出基于图像分块的帕金森病检测方法以提升跨患者泛化能力**

**关键词**: `帕金森病检测` `图像分块分析` `跨患者泛化` `手绘图识别` `集成学习`

## 📋 核心要点

1. 核心问题：现有方法在未见患者数据上泛化能力不足且数据集有限。
2. 方法要点：采用2x2分块策略，分阶段分类绘图类型并提取特征，使用集成方法融合决策。
3. 实验或效果：在NewHandPD数据集上，未见患者准确率达94.91%，泛化差距仅2.17个百分点。

## 📄 摘要（原文）

> Parkinson's disease (PD) is a neurodegenerative disease affecting about 1% of
> people over the age of 60, causing motor impairments that impede hand
> coordination activities such as writing and drawing. Many approaches have tried
> to support early detection of Parkinson's disease based on hand-drawn images;
> however, we identified two major limitations in the related works: (1) the lack
> of sufficient datasets, (2) the robustness when dealing with unseen patient
> data. In this paper, we propose a new approach to detect Parkinson's disease
> that consists of two stages: The first stage classifies based on their drawing
> type(circle, meander, spiral), and the second stage extracts the required
> features from the images and detects Parkinson's disease. We overcame the
> previous two limitations by applying a chunking strategy where we divide each
> image into 2x2 chunks. Each chunk is processed separately when extracting
> features and recognizing Parkinson's disease indicators. To make the final
> classification, an ensemble method is used to merge the decisions made from
> each chunk. Our evaluation shows that our proposed approach outperforms the top
> performing state-of-the-art approaches, in particular on unseen patients. On
> the NewHandPD dataset our approach, it achieved 97.08% accuracy for seen
> patients and 94.91% for unseen patients, our proposed approach maintained a gap
> of only 2.17 percentage points, compared to the 4.76-point drop observed in
> prior work.

