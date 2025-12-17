---
layout: default
title: General OOD Detection via Model-aware and Subspace-aware Variable Priority
---

# General OOD Detection via Model-aware and Subspace-aware Variable Priority

**arXiv**: [2512.13003v1](https://arxiv.org/abs/2512.13003) | [PDF](https://arxiv.org/pdf/2512.13003.pdf)

**作者**: Min Lu, Hemant Ishwaran

---

## 💡 一句话要点

**提出模型感知与子空间感知的变量优先级框架，用于通用OOD检测，适用于回归和生存分析。**

**关键词**: `OOD检测` `回归分析` `生存分析` `随机森林` `变量优先级` `模型感知`

## 📋 核心要点

1. 核心问题：回归和生存分析中OOD检测因缺乏离散标签和量化预测不确定性而受限。
2. 方法要点：利用拟合预测器构建局部邻域，强调驱动模型关系的特征，并嵌入变量优先级。
3. 实验或效果：在合成和真实数据基准测试中，针对功能偏移显示优于现有方法的性能提升。

## 📄 摘要（原文）

> Out-of-distribution (OOD) detection is essential for determining when a supervised model encounters inputs that differ meaningfully from its training distribution. While widely studied in classification, OOD detection for regression and survival analysis remains limited due to the absence of discrete labels and the challenge of quantifying predictive uncertainty. We introduce a framework for OOD detection that is simultaneously model aware and subspace aware, and that embeds variable prioritization directly into the detection step. The method uses the fitted predictor to construct localized neighborhoods around each test case that emphasize the features driving the model's learned relationship and downweight directions that are less relevant to prediction. It produces OOD scores without relying on global distance metrics or estimating the full feature density. The framework is applicable across outcome types, and in our implementation we use random forests, where the rule structure yields transparent neighborhoods and effective scoring. Experiments on synthetic and real data benchmarks designed to isolate functional shifts show consistent improvements over existing methods. We further demonstrate the approach in an esophageal cancer survival study, where distribution shifts related to lymphadenectomy identify patterns relevant to surgical guidelines.

