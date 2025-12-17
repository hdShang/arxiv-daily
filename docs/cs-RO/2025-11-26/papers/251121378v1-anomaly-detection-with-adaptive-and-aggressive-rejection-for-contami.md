---
layout: default
title: Anomaly Detection with Adaptive and Aggressive Rejection for Contaminated Training Data
---

# Anomaly Detection with Adaptive and Aggressive Rejection for Contaminated Training Data

**arXiv**: [2511.21378v1](https://arxiv.org/abs/2511.21378) | [PDF](https://arxiv.org/pdf/2511.21378.pdf)

**作者**: Jungi Lee, Jungkwon Kim, Chi Zhang, Kwangsun Yoo, Seok-Joo Byun

---

## 💡 一句话要点

**提出自适应激进拒绝方法以解决污染训练数据中的异常检测问题**

**关键词**: `异常检测` `污染数据` `自适应拒绝` `高斯混合模型` `性能提升`

## 📋 核心要点

1. 核心问题：传统方法依赖固定污染比，实际与假设不符时性能下降
2. 方法要点：结合修正z分数和高斯混合模型阈值，动态排除异常
3. 实验或效果：在图像和表格数据集上AUROC提升0.041，优于现有方法

## 📄 摘要（原文）

> Handling contaminated data poses a critical challenge in anomaly detection, as traditional models assume training on purely normal data. Conventional methods mitigate contamination by relying on fixed contamination ratios, but discrepancies between assumed and actual ratios can severely degrade performance, especially in noisy environments where normal and abnormal data distributions overlap. To address these limitations, we propose Adaptive and Aggressive Rejection (AAR), a novel method that dynamically excludes anomalies using a modified z-score and Gaussian mixture model-based thresholds. AAR effectively balances the trade-off between preserving normal data and excluding anomalies by integrating hard and soft rejection strategies. Extensive experiments on two image datasets and thirty tabular datasets demonstrate that AAR outperforms the state-of-the-art method by 0.041 AUROC. By providing a scalable and reliable solution, AAR enhances robustness against contaminated datasets, paving the way for broader real-world applications in domains such as security and healthcare.

