---
layout: default
title: DRBD-Mamba for Robust and Efficient Brain Tumor Segmentation with Analytical Insights
---

# DRBD-Mamba for Robust and Efficient Brain Tumor Segmentation with Analytical Insights

**arXiv**: [2510.14383v1](https://arxiv.org/abs/2510.14383) | [PDF](https://arxiv.org/pdf/2510.14383.pdf)

**作者**: Danish Ali, Ajmal Mian, Naveed Akhtar, Ghulam Mubashar Hassan

---

## 💡 一句话要点

**提出DRBD-Mamba模型以高效鲁棒地分割脑肿瘤**

**关键词**: `脑肿瘤分割` `状态空间模型` `多尺度依赖` `计算效率` `鲁棒性评估`

## 📋 核心要点

1. 脑肿瘤分割因肿瘤亚区异质性而具挑战性，且现有Mamba模型计算开销大、鲁棒性未知
2. 采用双分辨率双向Mamba捕获多尺度长程依赖，结合空间填充曲线和门控融合模块提升效率与特征表示
3. 在BraTS2023上验证，模型在肿瘤核心和增强肿瘤上Dice提升，效率提高15倍，保持高精度

## 📄 摘要（原文）

> Accurate brain tumor segmentation is significant for clinical diagnosis and
> treatment. It is challenging due to the heterogeneity of tumor subregions.
> Mamba-based State Space Models have demonstrated promising performance.
> However, they incur significant computational overhead due to sequential
> feature computation across multiple spatial axes. Moreover, their robustness
> across diverse BraTS data partitions remains largely unexplored, leaving a
> critical gap in reliable evaluation. To address these limitations, we propose
> dual-resolution bi-directional Mamba (DRBD-Mamba), an efficient 3D segmentation
> model that captures multi-scale long-range dependencies with minimal
> computational overhead. We leverage a space-filling curve to preserve spatial
> locality during 3D-to-1D feature mapping, thereby reducing reliance on
> computationally expensive multi-axial feature scans. To enrich feature
> representation, we propose a gated fusion module that adaptively integrates
> forward and reverse contexts, along with a quantization block that discretizes
> features to improve robustness. In addition, we propose five systematic folds
> on BraTS2023 for rigorous evaluation of segmentation techniques under diverse
> conditions and present detailed analysis of common failure scenarios. On the
> 20\% test set used by recent methods, our model achieves Dice improvements of
> 0.10\% for whole tumor, 1.75\% for tumor core, and 0.93\% for enhancing tumor.
> Evaluations on the proposed systematic five folds demonstrate that our model
> maintains competitive whole tumor accuracy while achieving clear average Dice
> gains of 0.86\% for tumor core and 1.45\% for enhancing tumor over existing
> state-of-the-art. Furthermore, our model attains 15 times improvement in
> efficiency while maintaining high segmentation accuracy, highlighting its
> robustness and computational advantage over existing approaches.

