---
layout: default
title: SAND Challenge: Four Approaches for Dysartria Severity Classification
---

# SAND Challenge: Four Approaches for Dysartria Severity Classification

**arXiv**: [2512.02669v1](https://arxiv.org/abs/2512.02669) | [PDF](https://arxiv.org/pdf/2512.02669.pdf)

**作者**: Gauri Deshpande, Harish Battula, Ashish Panda, Sunil Kumar Kopparapu

---

## 💡 一句话要点

**提出四种建模方法以解决SAND挑战中的构音障碍严重程度分类问题**

**关键词**: `构音障碍分类` `语音分析` `深度学习模型` `集成学习` `SAND挑战`

## 📋 核心要点

1. 核心问题：基于语音录音数据集，对构音障碍严重程度进行五分类任务。
2. 方法要点：包括ViT-OF、1D-CNN、BiLSTM-OF和分层XGBoost集成四种不同建模策略。
3. 实验或效果：在53名说话者的验证集上，XGBoost集成获得最高宏F1分数0.86，深度学习模型F1分数为0.70。

## 📄 摘要（原文）

> This paper presents a unified study of four distinct modeling approaches for classifying dysarthria severity in the Speech Analysis for Neurodegenerative Diseases (SAND) challenge. All models tackle the same five class classification task using a common dataset of speech recordings. We investigate: (1) a ViT-OF method leveraging a Vision Transformer on spectrogram images, (2) a 1D-CNN approach using eight 1-D CNN's with majority-vote fusion, (3) a BiLSTM-OF approach using nine BiLSTM models with majority vote fusion, and (4) a Hierarchical XGBoost ensemble that combines glottal and formant features through a two stage learning framework. Each method is described, and their performances on a validation set of 53 speakers are compared. Results show that while the feature-engineered XGBoost ensemble achieves the highest macro-F1 (0.86), the deep learning models (ViT, CNN, BiLSTM) attain competitive F1-scores (0.70) and offer complementary insights into the problem.

