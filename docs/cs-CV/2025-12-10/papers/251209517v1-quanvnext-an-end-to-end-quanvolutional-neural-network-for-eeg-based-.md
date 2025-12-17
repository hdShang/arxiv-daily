---
layout: default
title: QuanvNeXt: An end-to-end quanvolutional neural network for EEG-based detection of major depressive disorder
---

# QuanvNeXt: An end-to-end quanvolutional neural network for EEG-based detection of major depressive disorder

**arXiv**: [2512.09517v1](https://arxiv.org/abs/2512.09517) | [PDF](https://arxiv.org/pdf/2512.09517.pdf)

**作者**: Nabil Anan Orka, Ehtashamul Haque, Maftahul Jannat, Md Abdul Awal, Mohammad Ali Moni

---

## 💡 一句话要点

**提出QuanvNeXt全量子卷积模型，用于基于EEG的抑郁症检测。**

**关键词**: `量子卷积神经网络` `EEG信号处理` `抑郁症检测` `残差块设计` `不确定性分析` `可解释AI`

## 📋 核心要点

1. 核心问题：基于EEG的抑郁症诊断，需高效模型处理脑电信号。
2. 方法要点：引入Cross Residual块，减少特征同质性并增强跨特征关系。
3. 实验或效果：在两个开源数据集上平均准确率93.1%，AUC-ROC 97.2%，优于基线。

## 📄 摘要（原文）

> This study presents QuanvNeXt, an end-to-end fully quanvolutional model for EEG-based depression diagnosis. QuanvNeXt incorporates a novel Cross Residual block, which reduces feature homogeneity and strengthens cross-feature relationships while retaining parameter efficiency. We evaluated QuanvNeXt on two open-source datasets, where it achieved an average accuracy of 93.1% and an average AUC-ROC of 97.2%, outperforming state-of-the-art baselines such as InceptionTime (91.7% accuracy, 95.9% AUC-ROC). An uncertainty analysis across Gaussian noise levels demonstrated well-calibrated predictions, with ECE scores remaining low (0.0436, Dataset 1) to moderate (0.1159, Dataset 2) even at the highest perturbation (ε = 0.1). Additionally, a post-hoc explainable AI analysis confirmed that QuanvNeXt effectively identifies and learns spectrotemporal patterns that distinguish between healthy controls and major depressive disorder. Overall, QuanvNeXt establishes an efficient and reliable approach for EEG-based depression diagnosis.

