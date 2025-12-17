---
layout: default
title: Pooling Attention: Evaluating Pretrained Transformer Embeddings for Deception Classification
---

# Pooling Attention: Evaluating Pretrained Transformer Embeddings for Deception Classification

**arXiv**: [2511.22977v1](https://arxiv.org/abs/2511.22977) | [PDF](https://arxiv.org/pdf/2511.22977.pdf)

**作者**: Sumit Mamtani, Abhijeet Bhure

---

## 💡 一句话要点

**评估预训练Transformer嵌入用于欺骗分类，通过池化注意力方法验证BERT等模型作为稳健基础。**

**关键词**: `假新闻检测` `Transformer嵌入` `池化注意力` `欺骗分类` `预训练模型评估` `轻量级分类器`

## 📋 核心要点

1. 核心问题：研究假新闻检测作为Transformer表示的下游评估任务，聚焦欺骗分类。
2. 方法要点：使用冻结的编码器-仅和解码器-仅预训练模型（如BERT、GPT-2）作为嵌入器，结合轻量级分类器，比较池化与填充策略。
3. 实验或效果：在LIAR数据集上，BERT嵌入与逻辑回归组合优于神经网络基线，池化方法对截断鲁棒且有效。

## 📄 摘要（原文）

> This paper investigates fake news detection as a downstream evaluation of Transformer representations, benchmarking encoder-only and decoder-only pre-trained models (BERT, GPT-2, Transformer-XL) as frozen embedders paired with lightweight classifiers. Through controlled preprocessing comparing pooling versus padding and neural versus linear heads, results demonstrate that contextual self-attention encodings consistently transfer effectively. BERT embeddings combined with logistic regression outperform neural baselines on LIAR dataset splits, while analyses of sequence length and aggregation reveal robustness to truncation and advantages from simple max or average pooling. This work positions attention-based token encoders as robust, architecture-centric foundations for veracity tasks, isolating Transformer contributions from classifier complexity.

