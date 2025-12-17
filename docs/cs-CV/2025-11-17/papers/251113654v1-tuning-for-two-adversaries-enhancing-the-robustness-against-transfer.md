---
layout: default
title: Tuning for Two Adversaries: Enhancing the Robustness Against Transfer and Query-Based Attacks using Hyperparameter Tuning
---

# Tuning for Two Adversaries: Enhancing the Robustness Against Transfer and Query-Based Attacks using Hyperparameter Tuning

**arXiv**: [2511.13654v1](https://arxiv.org/abs/2511.13654) | [PDF](https://arxiv.org/pdf/2511.13654.pdf)

**作者**: Pascal Zimmer, Ghassan Karame

---

## 💡 一句话要点

**通过超参数调优增强对抗转移和查询攻击的鲁棒性**

**关键词**: `超参数调优` `对抗鲁棒性` `转移攻击` `查询攻击` `分布式训练` `学习率优化`

## 📋 核心要点

1. 核心问题：优化超参数如何影响对抗转移和查询攻击的鲁棒性。
2. 方法要点：分析学习率等超参数，理论实验结合，覆盖多种训练设置。
3. 实验效果：学习率降低提升转移攻击鲁棒性64%，增加提升查询攻击鲁棒性28%。

## 📄 摘要（原文）

> In this paper, we present the first detailed analysis of how optimization hyperparameters -- such as learning rate, weight decay, momentum, and batch size -- influence robustness against both transfer-based and query-based attacks. Supported by theory and experiments, our study spans a variety of practical deployment settings, including centralized training, ensemble learning, and distributed training. We uncover a striking dichotomy: for transfer-based attacks, decreasing the learning rate significantly enhances robustness by up to $64\%$. In contrast, for query-based attacks, increasing the learning rate consistently leads to improved robustness by up to $28\%$ across various settings and data distributions. Leveraging these findings, we explore -- for the first time -- the optimization hyperparameter design space to jointly enhance robustness against both transfer-based and query-based attacks. Our results reveal that distributed models benefit the most from hyperparameter tuning, achieving a remarkable tradeoff by simultaneously mitigating both attack types more effectively than other training setups.

