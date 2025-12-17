---
layout: default
title: Weighted Conformal Prediction Provides Adaptive and Valid Mask-Conditional Coverage for General Missing Data Mechanisms
---

# Weighted Conformal Prediction Provides Adaptive and Valid Mask-Conditional Coverage for General Missing Data Mechanisms

**arXiv**: [2512.14221v1](https://arxiv.org/abs/2512.14221) | [PDF](https://arxiv.org/pdf/2512.14221.pdf)

**作者**: Jiarong Fan, Juhyun Park. Thi Phuong Thuy Vo, Nicolas Brunel

**分类**: stat.ML, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出加权共形预测方法，为一般缺失数据机制提供自适应且有效的掩码条件覆盖保证**

**关键词**: `共形预测` `缺失数据处理` `不确定性量化` `掩码条件覆盖` `加权校正` `多重填补` `预测区间` `统计学习`

## 📋 核心要点

1. 共形预测在处理缺失协变量时无法保证覆盖，现有方法难以应对缺失模式异质性。
2. 提出预填补-掩码-校正框架，通过加权共形预测校正填补后的预测集，兼容标准填补流程。
3. 在合成和真实数据集上验证，显著减少预测区间宽度，同时维持边际和掩码条件覆盖保证。

## 📝 摘要（中文）

共形预测（CP）为不确定性量化提供了原则性框架，但在面对缺失协变量时无法保证覆盖。针对不同缺失模式引起的异质性，掩码条件有效（MCV）覆盖已成为比边际覆盖更理想的属性。本研究通过提出一个预填补-掩码-校正框架来适应分割CP处理缺失值，能够提供有效覆盖。我们证明该方法为一般缺失数据机制提供了保证的边际覆盖和掩码条件有效性。方法的关键组成部分是一个重新加权的共形预测过程，在校准数据集的分布填补（多重填补）后校正预测集，使我们的方法与标准填补流程兼容。我们推导出两种算法，并证明它们近似边际有效和MCV。我们在合成和真实世界数据集上进行了评估。与标准MCV方法相比，该方法显著减少了预测区间的宽度，同时保持了目标保证。

## 🔬 方法详解

论文提出预填补-掩码-校正框架处理缺失数据。整体流程包括：先对校准数据集进行分布填补（如多重填补），然后应用加权共形预测校正预测集。关键创新是引入重新加权的共形预测过程，通过权重调整来适应不同缺失模式，确保掩码条件有效性。与现有方法的主要区别在于：该方法不依赖特定缺失机制假设，能处理一般缺失数据，且与标准填补方法（如多重填补）无缝集成，提高了实用性和灵活性。

## 📊 实验亮点

实验表明，与标准掩码条件有效方法相比，该方法在合成和真实数据集上显著减少了预测区间宽度（具体数值未知），同时保持了目标覆盖保证，验证了其有效性和效率提升。

## 🎯 应用场景

该方法适用于医疗诊断、金融风险评估和工业质量控制等领域，其中数据常存在缺失值。通过提供可靠的预测区间，能增强模型在不确定性环境下的决策支持，提升实际应用中的鲁棒性和可信度。

## 📄 摘要（原文）

> Conformal prediction (CP) offers a principled framework for uncertainty quantification, but it fails to guarantee coverage when faced with missing covariates. In addressing the heterogeneity induced by various missing patterns, Mask-Conditional Valid (MCV) Coverage has emerged as a more desirable property than Marginal Coverage. In this work, we adapt split CP to handle missing values by proposing a preimpute-mask-then-correct framework that can offer valid coverage. We show that our method provides guaranteed Marginal Coverage and Mask-Conditional Validity for general missing data mechanisms. A key component of our approach is a reweighted conformal prediction procedure that corrects the prediction sets after distributional imputation (multiple imputation) of the calibration dataset, making our method compatible with standard imputation pipelines. We derive two algorithms, and we show that they are approximately marginally valid and MCV. We evaluate them on synthetic and real-world datasets. It reduces significantly the width of prediction intervals w.r.t standard MCV methods, while maintaining the target guarantees.

