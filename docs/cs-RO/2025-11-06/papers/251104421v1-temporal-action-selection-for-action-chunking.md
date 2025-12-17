---
layout: default
title: Temporal Action Selection for Action Chunking
---

# Temporal Action Selection for Action Chunking

**arXiv**: [2511.04421v1](https://arxiv.org/abs/2511.04421) | [PDF](https://arxiv.org/pdf/2511.04421.pdf)

**作者**: Yueyang Weng, Xiaopeng Zhang, Yongjin Mu, Yingcong Zhu, Yanjie Li, Qi Liu

---

## 💡 一句话要点

**提出Temporal Action Selector以解决动作分块中的反应性不足问题**

**关键词**: `动作分块` `学习演示` `反应性优化` `决策一致性` `运动连贯性` `残差强化学习`

## 📋 核心要点

1. 动作分块减少决策频率，导致对噪声和动态环境反应性下降
2. TAS缓存多步预测动作块，通过轻量选择器动态选择最优动作
3. 实验显示TAS显著提升成功率，并增强残差强化学习训练效率

## 📄 摘要（原文）

> Action chunking is a widely adopted approach in Learning from Demonstration
> (LfD). By modeling multi-step action chunks rather than single-step actions,
> action chunking significantly enhances modeling capabilities for human expert
> policies. However, the reduced decision frequency restricts the utilization of
> recent observations, degrading reactivity - particularly evident in the
> inadequate adaptation to sensor noise and dynamic environmental changes.
> Existing efforts to address this issue have primarily resorted to trading off
> reactivity against decision consistency, without achieving both. To address
> this limitation, we propose a novel algorithm, Temporal Action Selector (TAS),
> which caches predicted action chunks from multiple timesteps and dynamically
> selects the optimal action through a lightweight selector network. TAS achieves
> balanced optimization across three critical dimensions: reactivity, decision
> consistency, and motion coherence. Experiments across multiple tasks with
> diverse base policies show that TAS significantly improves success rates -
> yielding an absolute gain of up to 73.3%. Furthermore, integrating TAS as a
> base policy with residual reinforcement learning (RL) substantially enhances
> training efficiency and elevates the performance plateau. Experiments in both
> simulation and physical robots confirm the method's efficacy.

