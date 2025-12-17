---
layout: default
title: Multi-Modal Opinion Integration for Financial Sentiment Analysis using Cross-Modal Attention
---

# Multi-Modal Opinion Integration for Financial Sentiment Analysis using Cross-Modal Attention

**arXiv**: [2512.03464v1](https://arxiv.org/abs/2512.03464) | [PDF](https://arxiv.org/pdf/2512.03464.pdf)

**作者**: Yujing Liu, Chen Yang

---

## 💡 一句话要点

**提出跨模态注意力框架以整合金融意见的时效性与流行性模态，提升情感分析准确性。**

**关键词**: `金融情感分析` `跨模态注意力` `多模态整合` `BERT` `时效性模态` `流行性模态`

## 📋 核心要点

1. 核心问题：现有方法难以有效整合金融意见的多样模态并捕捉细粒度跨模态交互。
2. 方法要点：使用BERT嵌入特征，通过金融多头跨注意力机制整合时效性与流行性模态，结合变换器层和多模态双线性池化进行分类。
3. 实验或效果：在837家公司数据集上达到83.5%准确率，比BERT+Transformer基线提升21%。

## 📄 摘要（原文）

> In recent years, financial sentiment analysis of public opinion has become increasingly important for market forecasting and risk assessment. However, existing methods often struggle to effectively integrate diverse opinion modalities and capture fine-grained interactions across them. This paper proposes an end-to-end deep learning framework that integrates two distinct modalities of financial opinions: recency modality (timely opinions) and popularity modality (trending opinions), through a novel cross-modal attention mechanism specifically designed for financial sentiment analysis. While both modalities consist of textual data, they represent fundamentally different information channels: recency-driven market updates versus popularity-driven collective sentiment. Our model first uses BERT (Chinese-wwm-ext) for feature embedding and then employs our proposed Financial Multi-Head Cross-Attention (FMHCA) structure to facilitate information exchange between these distinct opinion modalities. The processed features are optimized through a transformer layer and fused using multimodal factored bilinear pooling for classification into negative, neutral, and positive sentiment. Extensive experiments on a comprehensive dataset covering 837 companies demonstrate that our approach achieves an accuracy of 83.5%, significantly outperforming baselines including BERT+Transformer by 21 percent. These results highlight the potential of our framework to support more accurate financial decision-making and risk management.

