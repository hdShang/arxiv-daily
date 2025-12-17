---
layout: default
title: Contrastive Integrated Gradients: A Feature Attribution-Based Method for Explaining Whole Slide Image Classification
---

# Contrastive Integrated Gradients: A Feature Attribution-Based Method for Explaining Whole Slide Image Classification

**arXiv**: [2511.08464v1](https://arxiv.org/abs/2511.08464) | [PDF](https://arxiv.org/pdf/2511.08464.pdf)

**作者**: Anh Mai Vu, Tuan L. Vo, Ngoc Lam Quang Bui, Nam Nguyen Le Binh, Akash Awasthi, Huy Quoc Vo, Thanh-Huy Nguyen, Zhu Han, Chandra Mohan, Hien Van Nguyen

---

## 💡 一句话要点

**提出对比集成梯度方法以增强全切片图像分类的可解释性**

**关键词**: `全切片图像分析` `特征归因方法` `对比集成梯度` `可解释性` `计算病理学` `弱监督学习`

## 📋 核心要点

1. 全切片图像分析中，现有归因方法可能忽略类间判别信号，影响肿瘤亚型区分。
2. CIG在logit空间计算对比梯度，突出类判别区域，满足集成归因公理。
3. 在多个癌症数据集上验证，CIG提供更信息化的归因，定量和定性评估均优于基线。

## 📄 摘要（原文）

> Interpretability is essential in Whole Slide Image (WSI) analysis for computational pathology, where understanding model predictions helps build trust in AI-assisted diagnostics. While Integrated Gradients (IG) and related attribution methods have shown promise, applying them directly to WSIs introduces challenges due to their high-resolution nature. These methods capture model decision patterns but may overlook class-discriminative signals that are crucial for distinguishing between tumor subtypes. In this work, we introduce Contrastive Integrated Gradients (CIG), a novel attribution method that enhances interpretability by computing contrastive gradients in logit space. First, CIG highlights class-discriminative regions by comparing feature importance relative to a reference class, offering sharper differentiation between tumor and non-tumor areas. Second, CIG satisfies the axioms of integrated attribution, ensuring consistency and theoretical soundness. Third, we propose two attribution quality metrics, MIL-AIC and MIL-SIC, which measure how predictive information and model confidence evolve with access to salient regions, particularly under weak supervision. We validate CIG across three datasets spanning distinct cancer types: CAMELYON16 (breast cancer metastasis in lymph nodes), TCGA-RCC (renal cell carcinoma), and TCGA-Lung (lung cancer). Experimental results demonstrate that CIG yields more informative attributions both quantitatively, using MIL-AIC and MIL-SIC, and qualitatively, through visualizations that align closely with ground truth tumor regions, underscoring its potential for interpretable and trustworthy WSI-based diagnostics

