---
layout: default
title: Deep Unsupervised Anomaly Detection in Brain Imaging: Large-Scale Benchmarking and Bias Analysis
---

# Deep Unsupervised Anomaly Detection in Brain Imaging: Large-Scale Benchmarking and Bias Analysis

**arXiv**: [2512.01534v1](https://arxiv.org/abs/2512.01534) | [PDF](https://arxiv.org/pdf/2512.01534.pdf)

**作者**: Alexander Frotscher, Christian F. Baumgartner, Thomas Wolfers

---

## 💡 一句话要点

**提出大规模多中心基准以评估脑成像深度无监督异常检测，分析算法性能与偏差。**

**关键词**: `脑成像异常检测` `无监督学习` `多中心基准` `算法偏差分析` `病变分割`

## 📋 核心要点

1. 核心问题：脑成像无监督异常检测因评估碎片化、数据集异质和指标不一致阻碍临床转化。
2. 方法要点：基于重建方法（如扩散启发式）在病变分割中表现最佳，特征方法在分布偏移下更稳健。
3. 实验或效果：测试显示Dice分数0.03-0.65，算法存在扫描仪、病变大小和人口统计学相关偏差。

## 📄 摘要（原文）

> Deep unsupervised anomaly detection in brain magnetic resonance imaging offers a promising route to identify pathological deviations without requiring lesion-specific annotations. Yet, fragmented evaluations, heterogeneous datasets, and inconsistent metrics have hindered progress toward clinical translation. Here, we present a large-scale, multi-center benchmark of deep unsupervised anomaly detection for brain imaging. The training cohort comprised 2,976 T1 and 2,972 T2-weighted scans from healthy individuals across six scanners, with ages ranging from 6 to 89 years. Validation used 92 scans to tune hyperparameters and estimate unbiased thresholds. Testing encompassed 2,221 T1w and 1,262 T2w scans spanning healthy datasets and diverse clinical cohorts. Across all algorithms, the Dice-based segmentation performance varied between 0.03 and 0.65, indicating substantial variability. To assess robustness, we systematically evaluated the impact of different scanners, lesion types and sizes, as well as demographics (age, sex). Reconstruction-based methods, particularly diffusion-inspired approaches, achieved the strongest lesion segmentation performance, while feature-based methods showed greater robustness under distributional shifts. However, systematic biases, such as scanner-related effects, were observed for the majority of algorithms, including that small and low-contrast lesions were missed more often, and that false positives varied with age and sex. Increasing healthy training data yields only modest gains, underscoring that current unsupervised anomaly detection frameworks are limited algorithmically rather than by data availability. Our benchmark establishes a transparent foundation for future research and highlights priorities for clinical translation, including image native pretraining, principled deviation measures, fairness-aware modeling, and robust domain adaptation.

