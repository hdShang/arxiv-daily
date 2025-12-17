---
layout: default
title: Multi-Loss Learning for Speech Emotion Recognition with Energy-Adaptive Mixup and Frame-Level Attention
---

# Multi-Loss Learning for Speech Emotion Recognition with Energy-Adaptive Mixup and Frame-Level Attention

**arXiv**: [2512.04551v1](https://arxiv.org/abs/2512.04551) | [PDF](https://arxiv.org/pdf/2512.04551.pdf)

**作者**: Cong Wang, Yizhong Geng, Yuhua Wen, Qifei Li, Yingming Gao, Ruimin Wang, Chunfeng Wang, Hao Li, Ya Li, Wei Chen

---

## 💡 一句话要点

**提出多损失学习框架，集成能量自适应混合与帧级注意力，以提升语音情感识别性能。**

**关键词**: `语音情感识别` `多损失学习` `数据增强` `注意力机制` `特征提取`

## 📋 核心要点

1. 核心问题：语音情感识别面临情感复杂性和标注数据稀缺的挑战。
2. 方法要点：采用能量自适应混合增强数据多样性，结合帧级注意力模块优化特征提取。
3. 实验或效果：在四个常用数据集上验证，实现先进性能，显示方法的有效性和鲁棒性。

## 📄 摘要（原文）

> Speech emotion recognition (SER) is an important technology in human-computer interaction. However, achieving high performance is challenging due to emotional complexity and scarce annotated data. To tackle these challenges, we propose a multi-loss learning (MLL) framework integrating an energy-adaptive mixup (EAM) method and a frame-level attention module (FLAM). The EAM method leverages SNR-based augmentation to generate diverse speech samples capturing subtle emotional variations. FLAM enhances frame-level feature extraction for multi-frame emotional cues. Our MLL strategy combines Kullback-Leibler divergence, focal, center, and supervised contrastive loss to optimize learning, address class imbalance, and improve feature separability. We evaluate our method on four widely used SER datasets: IEMOCAP, MSP-IMPROV, RAVDESS, and SAVEE. The results demonstrate our method achieves state-of-the-art performance, suggesting its effectiveness and robustness.

