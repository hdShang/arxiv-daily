---
layout: default
title: Credal and Interval Deep Evidential Classifications
---

# Credal and Interval Deep Evidential Classifications

**arXiv**: [2512.05526v1](https://arxiv.org/abs/2512.05526) | [PDF](https://arxiv.org/pdf/2512.05526.pdf)

**作者**: Michele Caprio, Shireen K. Manchingal, Fabio Cuzzolin

---

## 💡 一句话要点

**提出CDEC和IDEC以解决分类任务中的不确定性量化问题**

**关键词**: `不确定性量化` `证据深度学习` `分类任务` `认知不确定性` `随机不确定性` `OoD检测`

## 📋 核心要点

1. 核心问题：分类任务中不确定性量化对决策和模型可靠性至关重要
2. 方法要点：利用信度集和证据预测分布区间，系统评估认知和随机不确定性
3. 实验或效果：在MNIST等数据集上实现竞争性预测精度和先进OoD检测

## 📄 摘要（原文）

> Uncertainty Quantification (UQ) presents a pivotal challenge in the field of Artificial Intelligence (AI), profoundly impacting decision-making, risk assessment and model reliability. In this paper, we introduce Credal and Interval Deep Evidential Classifications (CDEC and IDEC, respectively) as novel approaches to address UQ in classification tasks. CDEC and IDEC leverage a credal set (closed and convex set of probabilities) and an interval of evidential predictive distributions, respectively, allowing us to avoid overfitting to the training data and to systematically assess both epistemic (reducible) and aleatoric (irreducible) uncertainties. When those surpass acceptable thresholds, CDEC and IDEC have the capability to abstain from classification and flag an excess of epistemic or aleatoric uncertainty, as relevant. Conversely, within acceptable uncertainty bounds, CDEC and IDEC provide a collection of labels with robust probabilistic guarantees. CDEC and IDEC are trained using standard backpropagation and a loss function that draws from the theory of evidence. They overcome the shortcomings of previous efforts, and extend the current evidential deep learning literature. Through extensive experiments on MNIST, CIFAR-10 and CIFAR-100, together with their natural OoD shifts (F-MNIST/K-MNIST, SVHN/Intel, TinyImageNet), we show that CDEC and IDEC achieve competitive predictive accuracy, state-of-the-art OoD detection under epistemic and total uncertainty, and tight, well-calibrated prediction regions that expand reliably under distribution shift. An ablation over ensemble size further demonstrates that CDEC attains stable uncertainty estimates with only a small ensemble.

