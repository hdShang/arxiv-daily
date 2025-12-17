---
layout: default
title: Breaking Determinism: Stochastic Modeling for Reliable Off-Policy Evaluation in Ad Auctions
---

# Breaking Determinism: Stochastic Modeling for Reliable Off-Policy Evaluation in Ad Auctions

**arXiv**: [2512.03354v1](https://arxiv.org/abs/2512.03354) | [PDF](https://arxiv.org/pdf/2512.03354.pdf)

**作者**: Hongseon Yeom, Jaeyoul Shin, Soojin Min, Jeongmin Yoon, Seunghak Yu, Dongyeop Kang

---

## 💡 一句话要点

**提出基于出价景观模型的随机建模框架，以解决确定性广告拍卖中离策略评估的挑战。**

**关键词**: `广告拍卖` `离策略评估` `确定性环境` `倾向得分` `反事实评估` `出价景观模型`

## 📋 核心要点

1. 核心问题：确定性广告拍卖中胜者通吃导致非胜出广告曝光概率为零，标准离策略评估方法不适用。
2. 方法要点：利用出价景观模型近似倾向得分，支持使用自归一化逆倾向评分等稳定估计器进行反事实评估。
3. 实验或效果：在AuctionNet模拟基准和工业平台A/B测试中验证，点击率预测的平均方向准确率达92%，显著优于基线。

## 📄 摘要（原文）

> Online A/B testing, the gold standard for evaluating new advertising policies, consumes substantial engineering resources and risks significant revenue loss from deploying underperforming variations. This motivates the use of Off-Policy Evaluation (OPE) for rapid, offline assessment. However, applying OPE to ad auctions is fundamentally more challenging than in domains like recommender systems, where stochastic policies are common. In online ad auctions, it is common for the highest-bidding ad to win the impression, resulting in a deterministic, winner-takes-all setting. This results in zero probability of exposure for non-winning ads, rendering standard OPE estimators inapplicable. We introduce the first principled framework for OPE in deterministic auctions by repurposing the bid landscape model to approximate the propensity score. This model allows us to derive robust approximate propensity scores, enabling the use of stable estimators like Self-Normalized Inverse Propensity Scoring (SNIPS) for counterfactual evaluation. We validate our approach on the AuctionNet simulation benchmark and against 2-weeks online A/B test from a large-scale industrial platform. Our method shows remarkable alignment with online results, achieving a 92\% Mean Directional Accuracy (MDA) in CTR prediction, significantly outperforming the parametric baseline. MDA is the most critical metric for guiding deployment decisions, as it reflects the ability to correctly predict whether a new model will improve or harm performance. This work contributes the first practical and validated framework for reliable OPE in deterministic auction environments, offering an efficient alternative to costly and risky online experiments.

