---
layout: default
title: LM-CartSeg: Automated Segmentation of Lateral and Medial Cartilage and Subchondral Bone for Radiomics Analysis
---

# LM-CartSeg: Automated Segmentation of Lateral and Medial Cartilage and Subchondral Bone for Radiomics Analysis

**arXiv**: [2512.03449v1](https://arxiv.org/abs/2512.03449) | [PDF](https://arxiv.org/pdf/2512.03449.pdf)

**作者**: Tongxu Zhang

---

## 💡 一句话要点

**提出LM-CartSeg自动分割膝关节软骨与骨，用于放射组学分析**

**关键词**: `膝关节MRI分割` `放射组学分析` `nnU-Net模型` `几何后处理` `质量控制` `骨关节炎研究`

## 📋 核心要点

1. 核心问题：膝关节MRI放射组学需稳健、解剖学意义的ROI，现有方法依赖手动且缺乏质量控制。
2. 方法要点：使用两个3D nnU-Net模型进行零样本预测，结合几何规则后处理实现自动分割与内外侧分室。
3. 实验或效果：在OAIZIB-CM测试集上，后处理显著提升分割精度，DSC达0.91，放射组学特征显示超越形态学的判别信息。

## 📄 摘要（原文）

> Background and Objective: Radiomics of knee MRI requires robust, anatomically meaningful regions of interest (ROIs) that jointly capture cartilage and subchondral bone. Most existing work relies on manual ROIs and rarely reports quality control (QC). We present LM-CartSeg, a fully automatic pipeline for cartilage/bone segmentation, geometric lateral/medial (L/M) compartmentalisation and radiomics analysis. Methods: Two 3D nnU-Net models were trained on SKM-TEA (138 knees) and OAIZIB-CM (404 knees). At test time, zero-shot predictions were fused and refined by simple geometric rules: connected-component cleaning, construction of 10 mm subchondral bone bands in physical space, and a data-driven tibial L/M split based on PCA and k-means. Segmentation was evaluated on an OAIZIB-CM test set (103 knees) and on SKI-10 (100 knees). QC used volume and thickness signatures. From 10 ROIs we extracted 4 650 non-shape radiomic features to study inter-compartment similarity, dependence on ROI size, and OA vs. non-OA classification on OAIZIB-CM Results: Post-processing improved macro ASSD on OAIZIB-CM from 2.63 to 0.36 mm and HD95 from 25.2 to 3.35 mm, with DSC 0.91; zero-shot DSC on SKI-10 was 0.80. The geometric L/M rule produced stable compartments across datasets, whereas a direct L/M nnU-Net showed domain-dependent side swaps. Only 6 to 12 percent of features per ROI were strongly correlated with volume or thickness. Radiomics-based models models restricted to size-linked features. Conclusions: LM-CartSeg yields automatic, QCd ROIs and radiomic features that carry discriminative information beyond simple morphometry, providing a practical foundation for multi-centre knee OA radiomics studies.

