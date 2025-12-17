---
layout: default
title: A Novel Multi-branch ConvNeXt Architecture for Identifying Subtle Pathological Features in CT Scans
---

# A Novel Multi-branch ConvNeXt Architecture for Identifying Subtle Pathological Features in CT Scans

**arXiv**: [2510.09107v1](https://arxiv.org/abs/2510.09107) | [PDF](https://arxiv.org/pdf/2510.09107.pdf)

**作者**: Irash Perera, Uthayasanker Thayasivam

---

## 💡 一句话要点

**提出多分支ConvNeXt架构以识别CT扫描中的细微病理特征**

**关键词**: `多分支架构` `ConvNeXt` `CT扫描分析` `医学图像分类` `注意力机制` `COVID-19诊断`

## 📋 核心要点

1. 核心问题：医学图像中细微病理特征的识别，应用于COVID-19诊断等场景。
2. 方法要点：集成全局平均池化、全局最大池化和注意力加权池化的多分支架构。
3. 实验或效果：在验证集上ROC-AUC达0.9937，准确率0.9757，优于现有模型。

## 📄 摘要（原文）

> Intelligent analysis of medical imaging plays a crucial role in assisting
> clinical diagnosis, especially for identifying subtle pathological features.
> This paper introduces a novel multi-branch ConvNeXt architecture designed
> specifically for the nuanced challenges of medical image analysis. While
> applied here to the specific problem of COVID-19 diagnosis, the methodology
> offers a generalizable framework for classifying a wide range of pathologies
> from CT scans. The proposed model incorporates a rigorous end-to-end pipeline,
> from meticulous data preprocessing and augmentation to a disciplined two-phase
> training strategy that leverages transfer learning effectively. The
> architecture uniquely integrates features extracted from three parallel
> branches: Global Average Pooling, Global Max Pooling, and a new
> Attention-weighted Pooling mechanism. The model was trained and validated on a
> combined dataset of 2,609 CT slices derived from two distinct datasets.
> Experimental results demonstrate a superior performance on the validation set,
> achieving a final ROC-AUC of 0.9937, a validation accuracy of 0.9757, and an
> F1-score of 0.9825 for COVID-19 cases, outperforming all previously reported
> models on this dataset. These findings indicate that a modern, multi-branch
> architecture, coupled with careful data handling, can achieve performance
> comparable to or exceeding contemporary state-of-the-art models, thereby
> proving the efficacy of advanced deep learning techniques for robust medical
> diagnostics.

