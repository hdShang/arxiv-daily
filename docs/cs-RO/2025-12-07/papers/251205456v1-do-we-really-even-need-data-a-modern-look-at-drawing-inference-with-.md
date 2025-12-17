---
layout: default
title: Do We Really Even Need Data? A Modern Look at Drawing Inference with Predicted Data
---

# Do We Really Even Need Data? A Modern Look at Drawing Inference with Predicted Data

**arXiv**: [2512.05456v1](https://arxiv.org/abs/2512.05456) | [PDF](https://arxiv.org/pdf/2512.05456.pdf)

**作者**: Stephen Salerno, Kentaro Hoffman, Awan Afiaz, Anna Neufeld, Tyler H. McCormick, Jeffrey T. Leek

---

## 💡 一句话要点

**分析预测数据推断的统计挑战，提出偏差与方差框架以指导科学应用。**

**关键词**: `预测数据推断` `统计偏差` `方差分析` `机器学习应用` `科学数据收集`

## 📋 核心要点

1. 核心问题：使用预测数据替代真实数据可能导致推断偏差，高预测精度不保证有效推断。
2. 方法要点：将问题归结为偏差和方差，偏差源于预测系统偏移，方差源于忽略预测不确定性。
3. 实验或效果：回顾现有方法，基于经典统计理论，讨论透明且统计原则的应用指南。

## 📄 摘要（原文）

> As artificial intelligence and machine learning tools become more accessible, and scientists face new obstacles to data collection (e.g., rising costs, declining survey response rates), researchers increasingly use predictions from pre-trained algorithms as substitutes for missing or unobserved data. Though appealing for financial and logistical reasons, using standard tools for inference can misrepresent the association between independent variables and the outcome of interest when the true, unobserved outcome is replaced by a predicted value. In this paper, we characterize the statistical challenges inherent to drawing inference with predicted data (IPD) and show that high predictive accuracy does not guarantee valid downstream inference. We show that all such failures reduce to statistical notions of (i) bias, when predictions systematically shift the estimand or distort relationships among variables, and (ii) variance, when uncertainty from the prediction model and the intrinsic variability of the true data are ignored. We then review recent methods for conducting IPD and discuss how this framework is deeply rooted in classical statistical theory. We then comment on some open questions and interesting avenues for future work in this area, and end with some comments on how to use predicted data in scientific studies that is both transparent and statistically principled.

