---
layout: default
title: UCDSC: Open Set UnCertainty aware Deep Simplex Classifier for Medical Image Datasets
---

# UCDSC: Open Set UnCertainty aware Deep Simplex Classifier for Medical Image Datasets

**arXiv**: [2511.08196v1](https://arxiv.org/abs/2511.08196) | [PDF](https://arxiv.org/pdf/2511.08196.pdf)

**作者**: Arnav Aditya, Nitin Kumar, Saurabh Shigwan

---

## 💡 一句话要点

**提出UCDSC方法以解决医学图像开放集识别问题**

**关键词**: `开放集识别` `医学图像分析` `深度单纯形分类器` `不确定性建模`

## 📋 核心要点

1. 医学图像诊断中数据有限且存在未知类别识别挑战
2. 基于深度神经网络特征聚类于正则单纯形顶点设计损失函数
3. 在多个MedMNIST数据集上性能优于现有技术

## 📄 摘要（原文）

> Driven by advancements in deep learning, computer-aided diagnoses have made remarkable progress. However, outside controlled laboratory settings, algorithms may encounter several challenges. In the medical domain, these difficulties often stem from limited data availability due to ethical and legal restrictions, as well as the high cost and time required for expert annotations-especially in the face of emerging or rare diseases. In this context, open-set recognition plays a vital role by identifying whether a sample belongs to one of the known classes seen during training or should be rejected as an unknown. Recent studies have shown that features learned in the later stages of deep neural networks are observed to cluster around their class means, which themselves are arranged as individual vertices of a regular simplex [32]. The proposed method introduces a loss function designed to reject samples of unknown classes effectively by penalizing open space regions using auxiliary datasets. This approach achieves significant performance gain across four MedMNIST datasets-BloodMNIST, OCTMNIST, DermaMNIST, TissueMNIST and a publicly available skin dataset [29] outperforming state-of-the-art techniques.

