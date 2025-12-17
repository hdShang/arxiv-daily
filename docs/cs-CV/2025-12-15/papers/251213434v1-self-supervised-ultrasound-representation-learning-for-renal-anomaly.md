---
layout: default
title: Self-Supervised Ultrasound Representation Learning for Renal Anomaly Prediction in Prenatal Imaging
---

# Self-Supervised Ultrasound Representation Learning for Renal Anomaly Prediction in Prenatal Imaging

**arXiv**: [2512.13434v1](https://arxiv.org/abs/2512.13434) | [PDF](https://arxiv.org/pdf/2512.13434.pdf)

**作者**: Youssef Megahed, Inok Lee, Robin Ducharme, Kevin Dick, Adrian D. C. Chan, Steven Hawken, Mark C. Walker

---

## 💡 一句话要点

**提出自监督超声基础模型USF-MAE，用于产前超声图像中胎儿肾脏异常的自动分类。**

**关键词**: `自监督学习` `超声图像分析` `产前诊断` `肾脏异常分类` `基础模型` `可解释性`

## 📋 核心要点

1. 核心问题：产前超声诊断肾脏异常受操作者依赖和成像条件限制，需自动化辅助。
2. 方法要点：使用掩码自编码预训练的超声基础模型USF-MAE，微调进行二分类和多分类任务。
3. 实验或效果：USF-MAE在验证集和独立测试集上性能优于DenseNet-169基线，多分类提升显著，并通过Score-CAM增强可解释性。

## 📄 摘要（原文）

> Prenatal ultrasound is the cornerstone for detecting congenital anomalies of the kidneys and urinary tract, but diagnosis is limited by operator dependence and suboptimal imaging conditions. We sought to assess the performance of a self-supervised ultrasound foundation model for automated fetal renal anomaly classification using a curated dataset of 969 two-dimensional ultrasound images. A pretrained Ultrasound Self-Supervised Foundation Model with Masked Autoencoding (USF-MAE) was fine-tuned for binary and multi-class classification of normal kidneys, urinary tract dilation, and multicystic dysplastic kidney. Models were compared with a DenseNet-169 convolutional baseline using cross-validation and an independent test set. USF-MAE consistently improved upon the baseline across all evaluation metrics in both binary and multi-class settings. USF-MAE achieved an improvement of about 1.87% (AUC) and 7.8% (F1-score) on the validation set, 2.32% (AUC) and 4.33% (F1-score) on the independent holdout test set. The largest gains were observed in the multi-class setting, where the improvement in AUC was 16.28% and 46.15% in F1-score. To facilitate model interpretability, Score-CAM visualizations were adapted for a transformer architecture and show that model predictions were informed by known, clinically relevant renal structures, including the renal pelvis in urinary tract dilation and cystic regions in multicystic dysplastic kidney. These results show that ultrasound-specific self-supervised learning can generate a useful representation as a foundation for downstream diagnostic tasks. The proposed framework offers a robust, interpretable approach to support the prenatal detection of renal anomalies and demonstrates the promise of foundation models in obstetric imaging.

