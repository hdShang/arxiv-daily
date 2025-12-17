---
layout: default
title: Reverberation: Learning the Latencies Before Forecasting Trajectories
---

# Reverberation: Learning the Latencies Before Forecasting Trajectories

**arXiv**: [2511.11164v1](https://arxiv.org/abs/2511.11164) | [PDF](https://arxiv.org/pdf/2511.11164.pdf)

**作者**: Conghao Wong, Ziqian Zou, Beihao Xia, Xinge You

---

## 💡 一句话要点

**提出Reverberation模型以学习轨迹预测中的延迟动态**

**关键词**: `轨迹预测` `延迟建模` `回响变换` `可解释AI` `多智能体交互`

## 📋 核心要点

1. 核心问题：轨迹预测中代理对事件响应的延迟未被显式学习，影响预测连续性和合理性。
2. 方法要点：引入声学启发的回响变换，使用可学习核模拟代理的延迟偏好和随机性。
3. 实验或效果：多数据集验证，模型在准确性和延迟动态可解释性上表现优异。

## 📄 摘要（原文）

> Bridging the past to the future, connecting agents both spatially and temporally, lies at the core of the trajectory prediction task. Despite great efforts, it remains challenging to explicitly learn and predict latencies, the temporal delays with which agents respond to different trajectory-changing events and adjust their future paths, whether on their own or interactively. Different agents may exhibit distinct latency preferences for noticing, processing, and reacting to any specific trajectory-changing event. The lack of consideration of such latencies may undermine the causal continuity of the forecasting system and also lead to implausible or unintended trajectories. Inspired by the reverberation curves in acoustics, we propose a new reverberation transform and the corresponding Reverberation (short for Rev) trajectory prediction model, which simulates and predicts different latency preferences of each agent as well as their stochasticity by using two explicit and learnable reverberation kernels, allowing for the controllable trajectory prediction based on these forecasted latencies. Experiments on multiple datasets, whether pedestrians or vehicles, demonstrate that Rev achieves competitive accuracy while revealing interpretable latency dynamics across agents and scenarios. Qualitative analyses further verify the properties of the proposed reverberation transform, highlighting its potential as a general latency modeling approach.

