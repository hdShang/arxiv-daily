---
layout: default
title: Machine Learning Approaches to Clinical Risk Prediction: Multi-Scale Temporal Alignment in Electronic Health Records
---

# Machine Learning Approaches to Clinical Risk Prediction: Multi-Scale Temporal Alignment in Electronic Health Records

**arXiv**: [2511.21561v1](https://arxiv.org/abs/2511.21561) | [PDF](https://arxiv.org/pdf/2511.21561.pdf)

**作者**: Wei-Chen Chang, Lu Dai, Ting Xu

---

## 💡 一句话要点

**提出多尺度时序对齐网络以解决电子健康记录中的时序不规则和动态依赖问题**

**关键词**: `时序对齐` `多尺度特征提取` `电子健康记录` `风险预测` `注意力机制`

## 📋 核心要点

1. 核心问题：电子健康记录存在时序不规则、采样间隔差异和多尺度动态依赖挑战
2. 方法要点：引入可学习时序对齐机制和多尺度卷积结构建模长短期特征
3. 实验或效果：在公开数据集上准确率、召回率等指标优于主流基线模型

## 📄 摘要（原文）

> This study proposes a risk prediction method based on a Multi-Scale Temporal Alignment Network (MSTAN) to address the challenges of temporal irregularity, sampling interval differences, and multi-scale dynamic dependencies in Electronic Health Records (EHR). The method focuses on temporal feature modeling by introducing a learnable temporal alignment mechanism and a multi-scale convolutional feature extraction structure to jointly model long-term trends and short-term fluctuations in EHR sequences. At the input level, the model maps multi-source clinical features into a unified high-dimensional semantic space and employs temporal embedding and alignment modules to dynamically weight irregularly sampled data, reducing the impact of temporal distribution differences on model performance. The multi-scale feature extraction module then captures key patterns across different temporal granularities through multi-layer convolution and hierarchical fusion, achieving a fine-grained representation of patient states. Finally, an attention-based aggregation mechanism integrates global temporal dependencies to generate individual-level risk representations for disease risk prediction and health status assessment. Experiments conducted on publicly available EHR datasets show that the proposed model outperforms mainstream baselines in accuracy, recall, precision, and F1-Score, demonstrating the effectiveness and robustness of multi-scale temporal alignment in complex medical time-series analysis. This study provides a new solution for intelligent representation of high-dimensional asynchronous medical sequences and offers important technical support for EHR-driven clinical risk prediction.

