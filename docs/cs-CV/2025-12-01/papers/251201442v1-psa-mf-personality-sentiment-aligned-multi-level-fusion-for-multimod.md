---
layout: default
title: PSA-MF: Personality-Sentiment Aligned Multi-Level Fusion for Multimodal Sentiment Analysis
---

# PSA-MF: Personality-Sentiment Aligned Multi-Level Fusion for Multimodal Sentiment Analysis

**arXiv**: [2512.01442v1](https://arxiv.org/abs/2512.01442) | [PDF](https://arxiv.org/pdf/2512.01442.pdf)

**作者**: Heng Xie, Kang Zhu, Zhengqi Wen, Jianhua Tao, Xuefei Liu, Ruibo Fu, Changsheng Li

---

## 💡 一句话要点

**提出PSA-MF框架，通过个性-情感对齐和多级融合解决多模态情感分析中的特征提取与融合问题。**

**关键词**: `多模态情感分析` `个性-情感对齐` `多级融合` `特征提取` `情感识别` `多模态融合`

## 📋 核心要点

1. 核心问题：现有方法在单模态特征提取中忽略个性差异，多模态融合中未考虑特征层级差异，影响识别性能。
2. 方法要点：引入个性特征，提出个性-情感对齐方法获取个性化情感嵌入；采用多级融合策略，通过预融合和增强融合逐步整合多模态信息。
3. 实验或效果：在两个常用数据集上实验，达到最先进结果，验证了框架的有效性。

## 📄 摘要（原文）

> Multimodal sentiment analysis (MSA) is a research field that recognizes human sentiments by combining textual, visual, and audio modalities. The main challenge lies in integrating sentiment-related information from different modalities, which typically arises during the unimodal feature extraction phase and the multimodal feature fusion phase. Existing methods extract only shallow information from unimodal features during the extraction phase, neglecting sentimental differences across different personalities. During the fusion phase, they directly merge the feature information from each modality without considering differences at the feature level. This ultimately affects the model's recognition performance. To address this problem, we propose a personality-sentiment aligned multi-level fusion framework. We introduce personality traits during the feature extraction phase and propose a novel personality-sentiment alignment method to obtain personalized sentiment embeddings from the textual modality for the first time. In the fusion phase, we introduce a novel multi-level fusion method. This method gradually integrates sentimental information from textual, visual, and audio modalities through multimodal pre-fusion and a multi-level enhanced fusion strategy. Our method has been evaluated through multiple experiments on two commonly used datasets, achieving state-of-the-art results.

