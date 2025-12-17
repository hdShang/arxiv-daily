---
layout: default
title: Revisiting the Scaling Properties of Downstream Metrics in Large Language Model Training
---

# Revisiting the Scaling Properties of Downstream Metrics in Large Language Model Training

**arXiv**: [2512.08894v1](https://arxiv.org/abs/2512.08894) | [PDF](https://arxiv.org/pdf/2512.08894.pdf)

**作者**: Jakub Krajewski, Amitis Shidani, Dan Busbridge, Sam Wiseman, Jason Ramapuram

---

## 💡 一句话要点

**提出直接框架以建模大语言模型训练预算与下游任务性能的缩放关系**

**关键词**: `大语言模型缩放定律` `下游任务性能预测` `幂律建模` `训练预算优化` `基准评估`

## 📋 核心要点

1. 核心问题：传统缩放定律依赖预训练损失等代理指标，预测下游任务性能不可靠
2. 方法要点：基于固定token-参数比，用幂律直接建模下游任务准确率的对数缩放
3. 实验或效果：验证模型达17B参数和350B tokens，直接方法外推优于两阶段方法，减少误差

## 📄 摘要（原文）

> While scaling laws for Large Language Models (LLMs) traditionally focus on proxy metrics like pretraining loss, predicting downstream task performance has been considered unreliable. This paper challenges that view by proposing a direct framework to model the scaling of benchmark performance from the training budget. We find that for a fixed token-to-parameter ratio, a simple power law can accurately describe the scaling behavior of log accuracy on multiple popular downstream tasks. Our results show that the direct approach extrapolates better than the previously proposed two-stage procedure, which is prone to compounding errors. Furthermore, we introduce functional forms that predict accuracy across token-to-parameter ratios and account for inference compute under repeated sampling. We validate our findings on models with up to 17B parameters trained on up to 350B tokens across two dataset mixtures. To support reproducibility and encourage future research, we release the complete set of pretraining losses and downstream evaluation results.

