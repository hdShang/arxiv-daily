---
layout: default
title: FROC: A Unified Framework with Risk-Optimized Control for Machine Unlearning in LLMs
---

# FROC: A Unified Framework with Risk-Optimized Control for Machine Unlearning in LLMs

**arXiv**: [2512.13337v1](https://arxiv.org/abs/2512.13337) | [PDF](https://arxiv.org/pdf/2512.13337.pdf)

**作者**: Si Qi Goh, Yongsen Zheng, Ziyao Liu, Sami Hormi, Kwok-Yan Lam

---

## 💡 一句话要点

**提出FROC框架，通过风险优化控制解决大语言模型机器遗忘中的风险平衡问题。**

**关键词**: `机器遗忘` `大语言模型` `风险控制` `保形风险分析` `超参数优化`

## 📋 核心要点

1. 核心问题：现有机器遗忘技术缺乏有效风险评估与控制机制，难以平衡遗忘充分性与效用保留。
2. 方法要点：基于保形风险分析，引入连续风险模型和保形遗忘风险，以概率约束指导超参数选择。
3. 实验或效果：多方法实验显示FROC能生成稳定风险景观，揭示配置与语义偏移、效用影响的关系。

## 📄 摘要（原文）

> Machine unlearning (MU) seeks to eliminate the influence of specific training examples from deployed models. As large language models (LLMs) become widely used, managing risks arising from insufficient forgetting or utility loss is increasingly crucial. Current MU techniques lack effective mechanisms for evaluating and controlling these risks, hindering the selection of strategies that appropriately balance safety and utility, and raising trust concerns surrounding the "right to be forgotten." To address these issues, we propose FROC, a unified framework with Risk-Optimized Control for machine unlearning in LLMs. FROC is built around a conformal-style risk-control formulation that expresses a user-specified risk budget on unlearning behavior. This probability-based constraint enables FROC to compare MU strategies, identify feasible operating regions, and guide hyperparameter selection according to desired trade-offs between forgetting sufficiency and utility preservation. To operationalize this constraint, FROC introduces a smoothly varying continuous risk model that aggregates forgetting deficiency and utility degradation into a single configuration-level score. Building on conformal risk analysis, FROC computes (1) the Conformal Unlearning Risk (CUR), a data-driven estimated value on the probability that forgotten samples continue to influence model predictions, and (2) risk-controlled configuration sets, which identify unlearning hyperparameters that are valid under the specified risk budget. Experiments across multiple LLM MU methods demonstrate that FROC produces stable, interpretable risk landscapes and reveals consistent relationships between unlearning configurations, semantic shift, and utility impact. FROC reframes MU as a controllable, risk-aware process and offers a practical foundation for managing unlearning behavior in large-scale LLM deployments.

