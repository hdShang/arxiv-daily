---
layout: default
title: Semantic4Safety: Causal Insights from Zero-shot Street View Imagery Segmentation for Urban Road Safety
---

# Semantic4Safety: Causal Insights from Zero-shot Street View Imagery Segmentation for Urban Road Safety

**arXiv**: [2510.15434v1](https://arxiv.org/abs/2510.15434) | [PDF](https://arxiv.org/pdf/2510.15434.pdf)

**作者**: Huan Chen, Ting Han, Siyu Chen, Zhihao Guo, Yiping Chen, Meiliu Wu

---

## 💡 一句话要点

**提出Semantic4Safety框架，通过零样本分割和因果推断提升城市道路安全分析。**

**关键词**: `零样本语义分割` `因果推断` `街景图像分析` `道路安全` `XGBoost分类` `SHAP解释`

## 📋 核心要点

1. 核心问题：如何从街景图像构建事故相关指标并量化其因果影响。
2. 方法要点：使用零样本语义分割提取指标，结合XGBoost和SHAP进行预测与解释。
3. 实验或效果：分析3万起事故，发现场景复杂度和几何特征主导风险，支持针对性干预。

## 📄 摘要（原文）

> Street-view imagery (SVI) offers a fine-grained lens on traffic risk, yet two
> fundamental challenges persist: (1) how to construct street-level indicators
> that capture accident-related features, and (2) how to quantify their causal
> impacts across different accident types. To address these challenges, we
> propose Semantic4Safety, a framework that applies zero-shot semantic
> segmentation to SVIs to derive 11 interpretable streetscape indicators, and
> integrates road type as contextual information to analyze approximately 30,000
> accident records in Austin. Specifically, we train an eXtreme Gradient Boosting
> (XGBoost) multi-class classifier and use Shapley Additive Explanations (SHAP)
> to interpret both global and local feature contributions, and then apply
> Generalized Propensity Score (GPS) weighting and Average Treatment Effect (ATE)
> estimation to control confounding and quantify causal effects. Results uncover
> heterogeneous, accident-type-specific causal patterns: features capturing scene
> complexity, exposure, and roadway geometry dominate predictive power; larger
> drivable area and emergency space reduce risk, whereas excessive visual
> openness can increase it. By bridging predictive modeling with causal
> inference, Semantic4Safety supports targeted interventions and high-risk
> corridor diagnosis, offering a scalable, data-informed tool for urban road
> safety planning.

