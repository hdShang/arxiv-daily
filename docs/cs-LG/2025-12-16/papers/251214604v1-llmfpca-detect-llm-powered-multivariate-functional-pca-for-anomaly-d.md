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

**提出LLmFPCA-detect框架，结合LLM文本嵌入与功能数据分析，解决稀疏纵向文本数据中的异常检测问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `稀疏纵向文本` `异常检测` `大语言模型嵌入` `功能数据分析` `多元功能主成分分析` `无监督学习` `文本聚类` `动态关键词分析`

## 📋 核心要点

1. 稀疏纵向文本数据缺乏专门分析方法，面临噪声、异质性和异常检测的挑战。
2. 结合LLM文本嵌入与稀疏多元功能主成分分析，构建灵活框架以恢复群体特征并检测异常。
3. 在亚马逊评论和维基百科评论数据集上验证，性能优于现有基线，提升预测任务表现。

## 📝 摘要（中文）

稀疏纵向（SL）文本数据出现在个体随时间重复生成文本的场景中（如客户评论、偶尔的社交媒体帖子、跨次就诊的电子病历），但观测频率和时间在个体间存在差异。这些复杂的文本数据集具有巨大潜力，可为未来政策和针对性推荐提供信息。然而，由于SL文本数据缺乏专门方法，且具有噪声、异质性和易出现异常的特点，检测和推断关键模式具有挑战性。我们引入了LLmFPCA-detect，这是一个灵活的框架，将基于LLM的文本嵌入与功能数据分析相结合，以检测大型SL文本数据集中的聚类并推断异常。首先，LLmFPCA-detect使用LLM提示将每段文本嵌入到特定应用的数值空间中。在数值空间中进行的稀疏多元功能主成分分析（mFPCA）是恢复主要群体特征的核心工具，并生成个体级分数，这些分数与基线静态协变量一起，促进数据分割、无监督异常检测和推断，并支持其他下游任务。特别是，我们利用LLM在LLmFPCA-detect发现的数据段和异常指导下进行动态关键词分析，并展示LLmFPCA-detect生成的聚类特定功能PC分数作为现有流程中的特征，有助于提升预测性能。我们通过实验支持LLmFPCA-detect的稳定性，并使用公共数据集（亚马逊客户评论轨迹和维基百科讨论页评论流）在两个不同应用中评估它，展示了跨领域的实用性并优于最先进的基线方法。

## 🔬 方法详解

LLmFPCA-detect框架首先使用LLM提示将稀疏纵向文本嵌入到数值空间，然后应用稀疏多元功能主成分分析（mFPCA）恢复群体特征并生成个体级分数。关键创新在于将LLM的语义理解能力与功能数据分析的时序建模相结合，处理文本的稀疏性和异质性。与现有方法相比，它专门针对稀疏纵向文本设计，避免了传统方法对密集数据的依赖，并通过LLM增强嵌入质量。

## 📊 实验亮点

在亚马逊客户评论和维基百科评论数据集上，LLmFPCA-detect在异常检测和聚类任务中优于最先进基线，实验显示其稳定性和跨领域泛化能力，功能PC分数作为特征能显著提升下游预测性能。

## 🎯 应用场景

该研究适用于客户评论分析、社交媒体监控、电子病历异常检测等领域，能帮助企业和机构从稀疏文本数据中提取模式、发现异常并优化推荐系统，具有广泛的实际应用价值。

## 📄 摘要（原文）

> Sparse longitudinal (SL) textual data arises when individuals generate text repeatedly over time (e.g., customer reviews, occasional social media posts, electronic medical records across visits), but the frequency and timing of observations vary across individuals. These complex textual data sets have immense potential to inform future policy and targeted recommendations. However, because SL text data lack dedicated methods and are noisy, heterogeneous, and prone to anomalies, detecting and inferring key patterns is challenging. We introduce LLmFPCA-detect, a flexible framework that pairs LLM-based text embeddings with functional data analysis to detect clusters and infer anomalies in large SL text datasets. First, LLmFPCA-detect embeds each piece of text into an application-specific numeric space using LLM prompts. Sparse multivariate functional principal component analysis (mFPCA) conducted in the numeric space forms the workhorse to recover primary population characteristics, and produces subject-level scores which, together with baseline static covariates, facilitate data segmentation, unsupervised anomaly detection and inference, and enable other downstream tasks. In particular, we leverage LLMs to perform dynamic keyword profiling guided by the data segments and anomalies discovered by LLmFPCA-detect, and we show that cluster-specific functional PC scores from LLmFPCA-detect, used as features in existing pipelines, help boost prediction performance. We support the stability of LLmFPCA-detect with experiments and evaluate it on two different applications using public datasets, Amazon customer-review trajectories, and Wikipedia talk-page comment streams, demonstrating utility across domains and outperforming state-of-the-art baselines.

