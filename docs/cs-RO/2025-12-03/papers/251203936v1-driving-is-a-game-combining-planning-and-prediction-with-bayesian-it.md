---
layout: default
title: Driving is a Game: Combining Planning and Prediction with Bayesian Iterative Best Response
---

# Driving is a Game: Combining Planning and Prediction with Bayesian Iterative Best Response

**arXiv**: [2512.03936v1](https://arxiv.org/abs/2512.03936) | [PDF](https://arxiv.org/pdf/2512.03936.pdf)

**作者**: Aron Distelzweig, Yiwei Wang, Faris Janjoš, Marcel Hallgarten, Mihai Dobre, Alexander Langmann, Joschka Boedecker, Johannes Betz

---

## 💡 一句话要点

**提出BIBeR框架，结合贝叶斯置信估计与迭代最优响应，以解决密集城市交通中的交互式规划问题。**

**关键词**: `自动驾驶规划` `博弈论规划` `运动预测` `交互感知` `贝叶斯置信估计` `迭代最优响应`

## 📋 核心要点

1. 核心问题：现有自动驾驶规划在密集交通中难以预测和影响其他智能体，导致交互能力不足。
2. 方法要点：集成先进预测器于迭代最优响应循环，通过双向适应近似纳什均衡，并量化预测可靠性以调整更新强度。
3. 实验或效果：在交互式换道场景中优于现有规划器11%，并在标准基准测试中表现更佳。

## 📄 摘要（原文）

> Autonomous driving planning systems perform nearly perfectly in routine scenarios using lightweight, rule-based methods but still struggle in dense urban traffic, where lane changes and merges require anticipating and influencing other agents. Modern motion predictors offer highly accurate forecasts, yet their integration into planning is mostly rudimental: discarding unsafe plans. Similarly, end-to-end models offer a one-way integration that avoids the challenges of joint prediction and planning modeling under uncertainty. In contrast, game-theoretic formulations offer a principled alternative but have seen limited adoption in autonomous driving. We present Bayesian Iterative Best Response (BIBeR), a framework that unifies motion prediction and game-theoretic planning into a single interaction-aware process. BIBeR is the first to integrate a state-of-the-art predictor into an Iterative Best Response (IBR) loop, repeatedly refining the strategies of the ego vehicle and surrounding agents. This repeated best-response process approximates a Nash equilibrium, enabling bidirectional adaptation where the ego both reacts to and shapes the behavior of others. In addition, our proposed Bayesian confidence estimation quantifies prediction reliability and modulates update strength, more conservative under low confidence and more decisive under high confidence. BIBeR is compatible with modern predictors and planners, combining the transparency of structured planning with the flexibility of learned models. Experiments show that BIBeR achieves an 11% improvement over state-of-the-art planners on highly interactive interPlan lane-change scenarios, while also outperforming existing approaches on standard nuPlan benchmarks.

