---
layout: default
title: How to Correctly Report LLM-as-a-Judge Evaluations
---

# How to Correctly Report LLM-as-a-Judge Evaluations

**arXiv**: [2511.21140v1](https://arxiv.org/abs/2511.21140) | [PDF](https://arxiv.org/pdf/2511.21140.pdf)

**作者**: Chungpa Lee, Thomas Zeng, Jongwon Jeong, Jy-yong Sohn, Kangwook Lee

---

## 💡 一句话要点

**提出插件框架以解决LLM作为评估者时的偏差和置信区间构建问题**

**关键词**: `大语言模型评估` `偏差校正` `置信区间构建` `校准样本分配` `统计方法`

## 📋 核心要点

1. 核心问题：LLM作为评估者时，因特异性和敏感性不完美导致准确度估计偏差和不确定性
2. 方法要点：开发插件框架进行偏差校正，并构建反映测试和校准数据集不确定性的置信区间
3. 实验或效果：引入自适应算法优化校准样本分配，降低准确度估计的不确定性

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used as evaluators in lieu of humans. While scalable, their judgments are noisy due to imperfect specificity and sensitivity of LLMs, leading to biased accuracy estimates. Although bias-correction methods exist, they are underutilized in LLM research and typically assume exact knowledge of the model's specificity and sensitivity. Furthermore, in general we only have estimates of these values and it is not well known how to properly construct confidence intervals using only estimates. This work presents a simple plug-in framework that corrects such bias and constructs confidence intervals reflecting uncertainty from both test and calibration dataset, enabling practical and statistically sound LLM-based evaluation. Additionally, to reduce uncertainty in the accuracy estimate, we introduce an adaptive algorithm that efficiently allocates calibration sample sizes.

