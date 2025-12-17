---
layout: default
title: Predictive Sample Assignment for Semantically Coherent Out-of-Distribution Detection
---

# Predictive Sample Assignment for Semantically Coherent Out-of-Distribution Detection

**arXiv**: [2512.12906v1](https://arxiv.org/abs/2512.12906) | [PDF](https://arxiv.org/pdf/2512.12906.pdf)

**作者**: Zhimao Peng, Enguang Wang, Xialei Liu, Ming-Ming Cheng

---

## 💡 一句话要点

**提出基于预测样本分配的语义一致分布外检测框架，以解决训练中噪声样本问题**

**关键词**: `语义一致分布外检测` `预测样本分配` `三元样本分配` `概念对比学习` `分布外检测` `表示学习`

## 📋 核心要点

1. 核心问题：现有语义一致分布外检测方法通过聚类过滤引入大量噪声样本，影响模型性能
2. 方法要点：采用双阈值三元样本分配策略提升样本集纯度，并结合概念对比表示学习损失增强分布内外样本区分
3. 实验或效果：在两个标准基准上显著超越现有方法，验证了框架的有效性

## 📄 摘要（原文）

> Semantically coherent out-of-distribution detection (SCOOD) is a recently proposed realistic OOD detection setting: given labeled in-distribution (ID) data and mixed in-distribution and out-of-distribution unlabeled data as the training data, SCOOD aims to enable the trained model to accurately identify OOD samples in the testing data. Current SCOOD methods mainly adopt various clustering-based in-distribution sample filtering (IDF) strategies to select clean ID samples from unlabeled data, and take the remaining samples as auxiliary OOD data, which inevitably introduces a large number of noisy samples in training. To address the above issue, we propose a concise SCOOD framework based on predictive sample assignment (PSA). PSA includes a dual-threshold ternary sample assignment strategy based on the predictive energy score that can significantly improve the purity of the selected ID and OOD sample sets by assigning unconfident unlabeled data to an additional discard sample set, and a concept contrastive representation learning loss to further expand the distance between ID and OOD samples in the representation space to assist ID/OOD discrimination. In addition, we also introduce a retraining strategy to help the model fully fit the selected auxiliary ID/OOD samples. Experiments on two standard SCOOD benchmarks demonstrate that our approach outperforms the state-of-the-art methods by a significant margin.

