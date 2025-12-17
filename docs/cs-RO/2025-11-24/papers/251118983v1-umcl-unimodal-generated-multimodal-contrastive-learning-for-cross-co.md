---
layout: default
title: UMCL: Unimodal-generated Multimodal Contrastive Learning for Cross-compression-rate Deepfake Detection
---

# UMCL: Unimodal-generated Multimodal Contrastive Learning for Cross-compression-rate Deepfake Detection

**arXiv**: [2511.18983v1](https://arxiv.org/abs/2511.18983) | [PDF](https://arxiv.org/pdf/2511.18983.pdf)

**作者**: Ching-Yi Lai, Chih-Yu Jian, Pei-Cheng Chuang, Chia-Ming Lee, Chih-Chung Hsu, Chiou-Ting Hsu, Chia-Wen Lin

---

## 💡 一句话要点

**提出UMCL框架以解决社交媒体压缩下深度伪造检测的泛化问题**

**关键词**: `深度伪造检测` `多模态对比学习` `压缩鲁棒性` `特征对齐` `跨压缩率检测`

## 📋 核心要点

1. 社交媒体压缩导致深度伪造检测模型泛化性差，现有方法难以应对压缩变化
2. 从单模态生成多模态特征，通过对比学习对齐压缩鲁棒信号、动态和语义嵌入
3. 实验显示方法在多种压缩率和伪造类型下性能优越，提供可解释特征关系

## 📄 摘要（原文）

> In deepfake detection, the varying degrees of compression employed by social media platforms pose significant challenges for model generalization and reliability. Although existing methods have progressed from single-modal to multimodal approaches, they face critical limitations: single-modal methods struggle with feature degradation under data compression in social media streaming, while multimodal approaches require expensive data collection and labeling and suffer from inconsistent modal quality or accessibility in real-world scenarios. To address these challenges, we propose a novel Unimodal-generated Multimodal Contrastive Learning (UMCL) framework for robust cross-compression-rate (CCR) deepfake detection. In the training stage, our approach transforms a single visual modality into three complementary features: compression-robust rPPG signals, temporal landmark dynamics, and semantic embeddings from pre-trained vision-language models. These features are explicitly aligned through an affinity-driven semantic alignment (ASA) strategy, which models inter-modal relationships through affinity matrices and optimizes their consistency through contrastive learning. Subsequently, our cross-quality similarity learning (CQSL) strategy enhances feature robustness across compression rates. Extensive experiments demonstrate that our method achieves superior performance across various compression rates and manipulation types, establishing a new benchmark for robust deepfake detection. Notably, our approach maintains high detection accuracy even when individual features degrade, while providing interpretable insights into feature relationships through explicit alignment.

