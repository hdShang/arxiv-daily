---
layout: default
title: Conformal Bandits: Bringing statistical validity and reward efficiency to the small-gap regime
---

# Conformal Bandits: Bringing statistical validity and reward efficiency to the small-gap regime

**arXiv**: [2512.09850v1](https://arxiv.org/abs/2512.09850) | [PDF](https://arxiv.org/pdf/2512.09850.pdf)

**作者**: Simone Cuonzo, Nina Deliu

---

## 💡 一句话要点

**提出Conformal Bandits框架，将共形预测融入赌博机问题，以在小差距场景中实现统计有效性和奖励效率。**

**关键词**: `共形预测` `赌博机问题` `小差距场景` `统计保证` `投资组合分配` `隐马尔可夫模型`

## 📋 核心要点

1. 传统赌博机策略如Thompson Sampling和UCB依赖分布假设或渐近保证，忽视统计性质，在小差距场景中表现不佳。
2. 通过共形预测，将决策策略的遗憾最小化潜力与有限时间预测覆盖的统计保证相结合。
3. 模拟研究和投资组合分配应用显示，在小差距场景中提升遗憾效率和覆盖保证，结合隐马尔可夫模型增强探索-利用权衡。

## 📄 摘要（原文）

> We introduce Conformal Bandits, a novel framework integrating Conformal Prediction (CP) into bandit problems, a classic paradigm for sequential decision-making under uncertainty. Traditional regret-minimisation bandit strategies like Thompson Sampling and Upper Confidence Bound (UCB) typically rely on distributional assumptions or asymptotic guarantees; further, they remain largely focused on regret, neglecting their statistical properties. We address this gap. Through the adoption of CP, we bridge the regret-minimising potential of a decision-making bandit policy with statistical guarantees in the form of finite-time prediction coverage.
>   We demonstrate the potential of it Conformal Bandits through simulation studies and an application to portfolio allocation, a typical small-gap regime, where differences in arm rewards are far too small for classical policies to achieve optimal regret bounds in finite sample. Motivated by this, we showcase our framework's practical advantage in terms of regret in small-gap settings, as well as its added value in achieving nominal coverage guarantees where classical UCB policies fail. Focusing on our application of interest, we further illustrate how integrating hidden Markov models to capture the regime-switching behaviour of financial markets, enhances the exploration-exploitation trade-off, and translates into higher risk-adjusted regret efficiency returns, while preserving coverage guarantees.

