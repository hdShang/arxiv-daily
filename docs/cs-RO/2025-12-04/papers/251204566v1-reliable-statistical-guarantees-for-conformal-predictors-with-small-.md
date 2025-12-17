---
layout: default
title: Reliable Statistical Guarantees for Conformal Predictors with Small Datasets
---

# Reliable Statistical Guarantees for Conformal Predictors with Small Datasets

**arXiv**: [2512.04566v1](https://arxiv.org/abs/2512.04566) | [PDF](https://arxiv.org/pdf/2512.04566.pdf)

**作者**: Miguel Sánchez-Domínguez, Lucas Lacasa, Javier de Vicente, Gonzalo Rubio, Eusebio Valero

---

## 💡 一句话要点

**提出新统计保证以解决小数据集下共形预测器覆盖可靠性问题**

**关键词**: `共形预测` `不确定性量化` `小数据集` `统计保证` `机器学习` `安全关键应用`

## 📋 核心要点

1. 核心问题：小校准集导致共形预测覆盖分布分散，影响不确定性模型可靠性。
2. 方法要点：提出新统计保证，提供单共形预测器覆盖概率信息，适用于小数据。
3. 实验或效果：验证方法在示例中有效，提供开源软件实现，兼容现有库。

## 📄 摘要（原文）

> Surrogate models (including deep neural networks and other machine learning algorithms in supervised learning) are capable of approximating arbitrarily complex, high-dimensional input-output problems in science and engineering, but require a thorough data-agnostic uncertainty quantification analysis before these can be deployed for any safety-critical application. The standard approach for data-agnostic uncertainty quantification is to use conformal prediction (CP), a well-established framework to build uncertainty models with proven statistical guarantees that do not assume any shape for the error distribution of the surrogate model. However, since the classic statistical guarantee offered by CP is given in terms of bounds for the marginal coverage, for small calibration set sizes (which are frequent in realistic surrogate modelling that aims to quantify error at different regions), the potentially strong dispersion of the coverage distribution around its average negatively impacts the reliability of the uncertainty model, often obtaining coverages below the expected value, resulting in a less applicable framework. After providing a gentle presentation of uncertainty quantification for surrogate models for machine learning practitioners, in this paper we bridge the gap by proposing a new statistical guarantee that offers probabilistic information for the coverage of a single conformal predictor. We show that the proposed framework converges to the standard solution offered by CP for large calibration set sizes and, unlike the classic guarantee, still offers reliable information about the coverage of a conformal predictor for small data sizes. We illustrate and validate the methodology in a suite of examples, and implement an open access software solution that can be used alongside common conformal prediction libraries to obtain uncertainty models that fulfil the new guarantee.

