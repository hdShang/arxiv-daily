---
layout: default
title: A Multi-Criteria Automated MLOps Pipeline for Cost-Effective Cloud-Based Classifier Retraining in Response to Data Distribution Shifts
---

# A Multi-Criteria Automated MLOps Pipeline for Cost-Effective Cloud-Based Classifier Retraining in Response to Data Distribution Shifts

**arXiv**: [2512.11541v1](https://arxiv.org/abs/2512.11541) | [PDF](https://arxiv.org/pdf/2512.11541.pdf)

**作者**: Emmanuel K. Katalay, David O. Dimandja, Jordan F. Masakuna

---

## 💡 一句话要点

**提出多标准自动化MLOps管道，以应对数据分布漂移，实现云端分类器高效重训练。**

**关键词**: `MLOps自动化` `数据分布漂移检测` `分类器重训练` `云端资源优化` `多标准统计方法` `异常检测`

## 📋 核心要点

1. 核心问题：数据分布漂移导致机器学习模型性能下降，传统MLOps依赖人工触发重训练。
2. 方法要点：采用多标准统计技术检测分布变化，仅在必要时自动触发模型更新，优化计算资源。
3. 实验或效果：在多个异常检测数据集上验证，相比传统策略，模型准确性和鲁棒性显著提升。

## 📄 摘要（原文）

> The performance of machine learning (ML) models often deteriorates when the underlying data distribution changes over time, a phenomenon known as data distribution drift. When this happens, ML models need to be retrained and redeployed. ML Operations (MLOps) is often manual, i.e., humans trigger the process of model retraining and redeployment. In this work, we present an automated MLOps pipeline designed to address neural network classifier retraining in response to significant data distribution changes. Our MLOps pipeline employs multi-criteria statistical techniques to detect distribution shifts and triggers model updates only when necessary, ensuring computational efficiency and resource optimization. We demonstrate the effectiveness of our framework through experiments on several benchmark anomaly detection data sets, showing significant improvements in model accuracy and robustness compared to traditional retraining strategies. Our work provides a foundation for deploying more reliable and adaptive ML systems in dynamic real-world settings, where data distribution changes are common.

