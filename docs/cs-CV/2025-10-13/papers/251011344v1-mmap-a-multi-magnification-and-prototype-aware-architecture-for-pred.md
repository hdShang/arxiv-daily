---
layout: default
title: MMAP: A Multi-Magnification and Prototype-Aware Architecture for Predicting Spatial Gene Expression
---

# MMAP: A Multi-Magnification and Prototype-Aware Architecture for Predicting Spatial Gene Expression

**arXiv**: [2510.11344v1](https://arxiv.org/abs/2510.11344) | [PDF](https://arxiv.org/pdf/2510.11344.pdf)

**作者**: Hai Dang Nguyen, Nguyen Dang Huy Pham, The Minh Duc Nguyen, Dac Thai Nguyen, Hang Thi Nguyen, Duong M. Nguyen

---

## 💡 一句话要点

**提出MMAP架构，通过多放大率和原型增强预测空间基因表达。**

**关键词**: `空间转录组学` `基因表达预测` `多放大率学习` `原型嵌入` `深度学习` `组织学图像分析`

## 📋 核心要点

1. 核心问题：组织学图像与分子信号间模态差距大，现有方法局部特征粒度不足、全局上下文覆盖不充分。
2. 方法要点：利用多放大率补丁增强局部特征，学习原型嵌入捕获全局空间上下文。
3. 实验或效果：在MAE、MSE和PCC等指标上优于现有方法，验证了有效性。

## 📄 摘要（原文）

> Spatial Transcriptomics (ST) enables the measurement of gene expression while
> preserving spatial information, offering critical insights into tissue
> architecture and disease pathology. Recent developments have explored the use
> of hematoxylin and eosin (H&E)-stained whole-slide images (WSIs) to predict
> transcriptome-wide gene expression profiles through deep neural networks. This
> task is commonly framed as a regression problem, where each input corresponds
> to a localized image patch extracted from the WSI. However, predicting spatial
> gene expression from histological images remains a challenging problem due to
> the significant modality gap between visual features and molecular signals.
> Recent studies have attempted to incorporate both local and global information
> into predictive models. Nevertheless, existing methods still suffer from two
> key limitations: (1) insufficient granularity in local feature extraction, and
> (2) inadequate coverage of global spatial context. In this work, we propose a
> novel framework, MMAP (Multi-MAgnification and Prototype-enhanced
> architecture), that addresses both challenges simultaneously. To enhance local
> feature granularity, MMAP leverages multi-magnification patch representations
> that capture fine-grained histological details. To improve global contextual
> understanding, it learns a set of latent prototype embeddings that serve as
> compact representations of slide-level information. Extensive experimental
> results demonstrate that MMAP consistently outperforms all existing
> state-of-the-art methods across multiple evaluation metrics, including Mean
> Absolute Error (MAE), Mean Squared Error (MSE), and Pearson Correlation
> Coefficient (PCC).

