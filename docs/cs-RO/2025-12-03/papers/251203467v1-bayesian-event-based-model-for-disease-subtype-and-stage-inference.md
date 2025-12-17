---
layout: default
title: Bayesian Event-Based Model for Disease Subtype and Stage Inference
---

# Bayesian Event-Based Model for Disease Subtype and Stage Inference

**arXiv**: [2512.03467v1](https://arxiv.org/abs/2512.03467) | [PDF](https://arxiv.org/pdf/2512.03467.pdf)

**作者**: Hongtao Hao, Joseph L. Austerweil

---

## 💡 一句话要点

**提出贝叶斯事件模型BEBMS，用于疾病亚型与分期推断，提升鲁棒性。**

**关键词**: `疾病亚型推断` `贝叶斯建模` `事件模型` `横断面数据分析` `阿尔茨海默病`

## 📋 核心要点

1. 核心问题：慢性疾病进展存在亚型异质性，需从横断面数据推断亚型与分期顺序。
2. 方法要点：基于事件模型，引入贝叶斯框架处理模型误设，优化亚型数量、进展顺序和患者分配。
3. 实验或效果：在合成数据中BEBMS优于SuStaIn，应用于阿尔茨海默病数据更符合科学共识。

## 📄 摘要（原文）

> Chronic diseases often progress differently across patients. Rather than randomly varying, there are typically a small number of subtypes for how a disease progresses across patients. To capture this structured heterogeneity, the Subtype and Stage Inference Event-Based Model (SuStaIn) estimates the number of subtypes, the order of disease progression for each subtype, and assigns each patient to a subtype from primarily cross-sectional data. It has been widely applied to uncover the subtypes of many diseases and inform our understanding of them. But how robust is its performance? In this paper, we develop a principled Bayesian subtype variant of the event-based model (BEBMS) and compare its performance to SuStaIn in a variety of synthetic data experiments with varied levels of model misspecification. BEBMS substantially outperforms SuStaIn across ordering, staging, and subtype assignment tasks. Further, we apply BEBMS and SuStaIn to a real-world Alzheimer's data set. We find BEBMS has results that are more consistent with the scientific consensus of Alzheimer's disease progression than SuStaIn.

