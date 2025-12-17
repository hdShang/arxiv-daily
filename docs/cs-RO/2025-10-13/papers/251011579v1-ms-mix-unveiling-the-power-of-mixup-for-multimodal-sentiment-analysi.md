---
layout: default
title: MS-Mix: Unveiling the Power of Mixup for Multimodal Sentiment Analysis
---

# MS-Mix: Unveiling the Power of Mixup for Multimodal Sentiment Analysis

**arXiv**: [2510.11579v1](https://arxiv.org/abs/2510.11579) | [PDF](https://arxiv.org/pdf/2510.11579.pdf)

**作者**: Hongyu Zhu, Lin Chen, Mounim A. El-Yacoubi, Mingsheng Shang

---

## 💡 一句话要点

**提出MS-Mix以解决多模态情感分析中数据稀缺和混合增强的语义不一致问题**

**关键词**: `多模态情感分析` `数据增强` `情感感知混合` `模态对齐` `注意力机制` `KL损失`

## 📋 核心要点

1. 核心问题：多模态情感分析中数据稀缺，且直接应用Mixup增强导致标签模糊和语义不一致
2. 方法要点：引入情感感知样本选择、强度引导混合比和情感对齐损失，优化多模态混合
3. 实验或效果：在三个基准数据集和六个先进骨干网络上验证，MS-Mix一致优于现有方法

## 📄 摘要（原文）

> Multimodal Sentiment Analysis (MSA) aims to identify and interpret human
> emotions by integrating information from heterogeneous data sources such as
> text, video, and audio. While deep learning models have advanced in network
> architecture design, they remain heavily limited by scarce multimodal annotated
> data. Although Mixup-based augmentation improves generalization in unimodal
> tasks, its direct application to MSA introduces critical challenges: random
> mixing often amplifies label ambiguity and semantic inconsistency due to the
> lack of emotion-aware mixing mechanisms. To overcome these issues, we propose
> MS-Mix, an adaptive, emotion-sensitive augmentation framework that
> automatically optimizes sample mixing in multimodal settings. The key
> components of MS-Mix include: (1) a Sentiment-Aware Sample Selection (SASS)
> strategy that effectively prevents semantic confusion caused by mixing samples
> with contradictory emotions. (2) a Sentiment Intensity Guided (SIG) module
> using multi-head self-attention to compute modality-specific mixing ratios
> dynamically based on their respective emotional intensities. (3) a Sentiment
> Alignment Loss (SAL) that aligns the prediction distributions across
> modalities, and incorporates the Kullback-Leibler-based loss as an additional
> regularization term to train the emotion intensity predictor and the backbone
> network jointly. Extensive experiments on three benchmark datasets with six
> state-of-the-art backbones confirm that MS-Mix consistently outperforms
> existing methods, establishing a new standard for robust multimodal sentiment
> augmentation. The source code is available at:
> https://github.com/HongyuZhu-s/MS-Mix.

