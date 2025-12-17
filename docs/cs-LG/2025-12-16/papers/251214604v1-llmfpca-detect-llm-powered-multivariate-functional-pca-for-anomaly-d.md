---
layout: default
title: LLmFPCA-detect: LLM-powered Multivariate Functional PCA for Anomaly Detection in Sparse Longitudinal Texts
---

# LLmFPCA-detect: LLM-powered Multivariate Functional PCA for Anomaly Detection in Sparse Longitudinal Texts

**arXiv**: [2512.14604v1](https://arxiv.org/abs/2512.14604) | [PDF](https://arxiv.org/pdf/2512.14604.pdf)

**作者**: Prasanjit Dubey, Aritra Guha, Zhengyi Zhou, Qiong Wu, Xiaoming Huo, Paromita Dubey

**分类**: stat.ML, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出LLmFPCA-detect框架，结合LLM文本嵌入与稀疏多元函数主成分分析，用于稀疏纵向文本数据的异常检测与聚类分析。**

**关键词**: `稀疏纵向文本` `异常检测` `函数主成分分析` `大语言模型嵌入` `无监督学习` `时序数据分析` `文本聚类` `多变量函数分析`

## 📋 核心要点

1. 核心问题：稀疏纵向文本数据缺乏专用分析方法，噪声大、异质性强，导致异常检测和模式推断困难。
2. 方法要点：结合LLM文本嵌入与稀疏多元函数主成分分析，构建灵活框架以检测聚类和异常。
3. 实验或效果：在亚马逊和维基百科数据集上验证，性能优于基线方法，并提升下游预测任务表现。

## 📝 摘要（中文）

稀疏纵向（SL）文本数据指个体随时间重复生成文本（如客户评论、社交媒体帖子、电子病历），但观测频率和时间点因人而异。这些复杂数据集虽具潜力，但因缺乏专用方法、噪声大、异质性强且易含异常，检测和推断关键模式面临挑战。本文引入LLmFPCA-detect，一个灵活框架，将基于LLM的文本嵌入与函数数据分析结合，以检测大型SL文本数据集中的聚类和异常。首先，LLmFPCA-detect使用LLM提示将每段文本嵌入到应用特定的数值空间。在数值空间中进行稀疏多元函数主成分分析（mFPCA），作为恢复主要群体特征的核心工具，并生成个体级分数，这些分数与基线静态协变量一起，促进数据分割、无监督异常检测与推断，并支持其他下游任务。特别地，我们利用LLM在LLmFPCA-detect发现的数据段和异常指导下进行动态关键词分析，并展示LLmFPCA-detect产生的聚类特定函数主成分分数作为现有流程的特征，有助于提升预测性能。通过实验支持LLmFPCA-detect的稳定性，并在两个公共数据集（亚马逊客户评论轨迹和维基百科讨论页评论流）上评估，证明其跨领域实用性并优于最先进的基线方法。

## 🔬 方法详解

LLmFPCA-detect框架首先使用LLM提示将文本嵌入到数值空间，然后应用稀疏多元函数主成分分析（mFPCA）处理这些嵌入，以恢复群体特征并生成个体级分数。关键创新在于将LLM的语义理解能力与函数数据分析的时序建模相结合，解决了稀疏纵向文本数据的异质性和噪声问题。与现有方法相比，它专门针对稀疏纵向文本设计，通过mFPCA处理时间变化，而传统方法多依赖静态分析或忽略文本时序特性。

## 📊 实验亮点

在亚马逊客户评论和维基百科评论数据集上，LLmFPCA-detect在异常检测和聚类任务中优于最先进基线，同时其生成的函数主成分分数作为特征能显著提升下游预测性能。

## 🎯 应用场景

该研究可应用于客户评论分析、社交媒体监控、电子病历异常检测等领域，为政策制定和个性化推荐提供数据支持，具有跨领域的实际价值。

## 📄 摘要（原文）

> Sparse longitudinal (SL) textual data arises when individuals generate text repeatedly over time (e.g., customer reviews, occasional social media posts, electronic medical records across visits), but the frequency and timing of observations vary across individuals. These complex textual data sets have immense potential to inform future policy and targeted recommendations. However, because SL text data lack dedicated methods and are noisy, heterogeneous, and prone to anomalies, detecting and inferring key patterns is challenging. We introduce LLmFPCA-detect, a flexible framework that pairs LLM-based text embeddings with functional data analysis to detect clusters and infer anomalies in large SL text datasets. First, LLmFPCA-detect embeds each piece of text into an application-specific numeric space using LLM prompts. Sparse multivariate functional principal component analysis (mFPCA) conducted in the numeric space forms the workhorse to recover primary population characteristics, and produces subject-level scores which, together with baseline static covariates, facilitate data segmentation, unsupervised anomaly detection and inference, and enable other downstream tasks. In particular, we leverage LLMs to perform dynamic keyword profiling guided by the data segments and anomalies discovered by LLmFPCA-detect, and we show that cluster-specific functional PC scores from LLmFPCA-detect, used as features in existing pipelines, help boost prediction performance. We support the stability of LLmFPCA-detect with experiments and evaluate it on two different applications using public datasets, Amazon customer-review trajectories, and Wikipedia talk-page comment streams, demonstrating utility across domains and outperforming state-of-the-art baselines.

