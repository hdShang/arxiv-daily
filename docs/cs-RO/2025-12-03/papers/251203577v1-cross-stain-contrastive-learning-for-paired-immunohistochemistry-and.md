---
layout: default
title: Cross-Stain Contrastive Learning for Paired Immunohistochemistry and Histopathology Slide Representation Learning
---

# Cross-Stain Contrastive Learning for Paired Immunohistochemistry and Histopathology Slide Representation Learning

**arXiv**: [2512.03577v1](https://arxiv.org/abs/2512.03577) | [PDF](https://arxiv.org/pdf/2512.03577.pdf)

**作者**: Yizhi Zhang, Lei Fan, Zhulin Tao, Donglin Di, Yang Song, Sidong Liu, Cong Cong

---

## 💡 一句话要点

**提出跨染色对比学习框架，利用对齐多染色数据集提升全切片图像表示质量。**

**关键词**: `计算病理学` `全切片图像表示` `对比学习` `多染色融合` `多实例学习`

## 📋 核心要点

1. 核心问题：多染色数据对齐不足导致特征不一致，限制病理图像表示学习。
2. 方法要点：两阶段预训练，包括补丁级对比对齐和切片级多实例学习融合模块。
3. 实验效果：在癌症亚型分类、生物标志物状态分类和生存预测任务中表现提升。

## 📄 摘要（原文）

> Universal, transferable whole-slide image (WSI) representations are central to computational pathology. Incorporating multiple markers (e.g., immunohistochemistry, IHC) alongside H&E enriches H&E-based features with diverse, biologically meaningful information. However, progress is limited by the scarcity of well-aligned multi-stain datasets. Inter-stain misalignment shifts corresponding tissue across slides, hindering consistent patch-level features and degrading slide-level embeddings. To address this, we curated a slide-level aligned, five-stain dataset (H&E, HER2, KI67, ER, PGR) to enable paired H&E-IHC learning and robust cross-stain representation. Leveraging this dataset, we propose Cross-Stain Contrastive Learning (CSCL), a two-stage pretraining framework with a lightweight adapter trained using patch-wise contrastive alignment to improve the compatibility of H&E features with corresponding IHC-derived contextual cues, and slide-level representation learning with Multiple Instance Learning (MIL), which uses a cross-stain attention fusion module to integrate stain-specific patch features and a cross-stain global alignment module to enforce consistency among slide-level embeddings across different stains. Experiments on cancer subtype classification, IHC biomarker status classification, and survival prediction show consistent gains, yielding high-quality, transferable H&E slide-level representations. The code and data are available at https://github.com/lily-zyz/CSCL.

