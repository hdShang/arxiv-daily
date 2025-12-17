---
layout: default
title: MRI Embeddings Complement Clinical Predictors for Cognitive Decline Modeling in Alzheimer's Disease Cohorts
---

# MRI Embeddings Complement Clinical Predictors for Cognitive Decline Modeling in Alzheimer's Disease Cohorts

**arXiv**: [2511.14601v1](https://arxiv.org/abs/2511.14601) | [PDF](https://arxiv.org/pdf/2511.14601.pdf)

**作者**: Nathaniel Putera, Daniel Vilet Rodríguez, Noah Videcrantz, Julia Machnio, Mostafa Mehdipour Ghazi

---

## 💡 一句话要点

**提出MRI嵌入与临床特征互补建模阿尔茨海默病认知衰退**

**关键词**: `阿尔茨海默病建模` `MRI嵌入` `3D视觉Transformer` `认知衰退预测` `多模态融合`

## 📋 核心要点

1. 核心问题：准确建模阿尔茨海默病认知衰退，以支持早期分层和个性化管理。
2. 方法要点：使用轨迹感知标签和3D ViT无监督学习获取MRI嵌入，结合临床特征。
3. 实验效果：临床特征预测极端衰退AUC约0.70，MRI嵌入识别稳定个体AUC达0.71。

## 📄 摘要（原文）

> Accurate modeling of cognitive decline in Alzheimer's disease is essential for early stratification and personalized management. While tabular predictors provide robust markers of global risk, their ability to capture subtle brain changes remains limited. In this study, we evaluate the predictive contributions of tabular and imaging-based representations, with a focus on transformer-derived Magnetic Resonance Imaging (MRI) embeddings. We introduce a trajectory-aware labeling strategy based on Dynamic Time Warping clustering to capture heterogeneous patterns of cognitive change, and train a 3D Vision Transformer (ViT) via unsupervised reconstruction on harmonized and augmented MRI data to obtain anatomy-preserving embeddings without progression labels. The pretrained encoder embeddings are subsequently assessed using both traditional machine learning classifiers and deep learning heads, and compared against tabular representations and convolutional network baselines. Results highlight complementary strengths across modalities. Clinical and volumetric features achieved the highest AUCs of around 0.70 for predicting mild and severe progression, underscoring their utility in capturing global decline trajectories. In contrast, MRI embeddings from the ViT model were most effective in distinguishing cognitively stable individuals with an AUC of 0.71. However, all approaches struggled in the heterogeneous moderate group. These findings indicate that clinical features excel in identifying high-risk extremes, whereas transformer-based MRI embeddings are more sensitive to subtle markers of stability, motivating multimodal fusion strategies for AD progression modeling.

