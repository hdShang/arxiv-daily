---
layout: default
title: Intrinsic-Motivation Multi-Robot Social Formation Navigation with Coordinated Exploration
---

# Intrinsic-Motivation Multi-Robot Social Formation Navigation with Coordinated Exploration

**arXiv**: [2512.13293v1](https://arxiv.org/abs/2512.13293) | [PDF](https://arxiv.org/pdf/2512.13293.pdf)

**作者**: Hao Fua, Wei Liu, Shuai Zhoua

---

## 💡 一句话要点

**提出基于内在动机协调探索的多机器人强化学习算法以解决社交编队导航中的探索效率问题**

**关键词**: `多机器人强化学习` `社交编队导航` `内在动机探索` `协调探索` `集中训练分散执行`

## 📋 核心要点

1. 核心问题：多机器人社交编队导航中，行人行为不可预测且不合作，导致协调探索效率低下
2. 方法要点：引入内在奖励机制缓解策略保守性，采用双采样模式和两时间尺度更新规则优化策略与奖励表示
3. 实验或效果：在社交编队导航基准测试中，算法在关键指标上优于现有先进方法

## 📄 摘要（原文）

> This paper investigates the application of reinforcement learning (RL) to multi-robot social formation navigation, a critical capability for enabling seamless human-robot coexistence. While RL offers a promising paradigm, the inherent unpredictability and often uncooperative dynamics of pedestrian behavior pose substantial challenges, particularly concerning the efficiency of coordinated exploration among robots. To address this, we propose a novel coordinated-exploration multi-robot RL algorithm introducing an intrinsic motivation exploration. Its core component is a self-learning intrinsic reward mechanism designed to collectively alleviate policy conservatism. Moreover, this algorithm incorporates a dual-sampling mode within the centralized training and decentralized execution framework to enhance the representation of both the navigation policy and the intrinsic reward, leveraging a two-time-scale update rule to decouple parameter updates. Empirical results on social formation navigation benchmarks demonstrate the proposed algorithm's superior performance over existing state-of-the-art methods across crucial metrics. Our code and video demos are available at: https://github.com/czxhunzi/CEMRRL.

