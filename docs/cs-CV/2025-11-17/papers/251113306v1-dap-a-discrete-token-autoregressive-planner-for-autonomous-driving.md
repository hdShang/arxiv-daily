---
layout: default
title: DAP: A Discrete-token Autoregressive Planner for Autonomous Driving
---

# DAP: A Discrete-token Autoregressive Planner for Autonomous Driving

**arXiv**: [2511.13306v1](https://arxiv.org/abs/2511.13306) | [PDF](https://arxiv.org/pdf/2511.13306.pdf)

**作者**: Bowen Ye, Bin Zhang, Hang Zhao

---

## 💡 一句话要点

**提出DAP离散令牌自回归规划器，联合预测BEV语义与自车轨迹以提升自动驾驶规划。**

**关键词**: `自动驾驶规划` `自回归模型` `BEV语义预测` `强化学习微调` `离散令牌表示`

## 📋 核心要点

1. 核心问题：自动驾驶中数据与模型扩展难以持续提升性能，仅预测自车轨迹监督稀疏且约束弱。
2. 方法要点：采用离散令牌自回归模型，联合预测BEV语义和自车轨迹，强化表示学习与动态条件。
3. 实验或效果：在160M参数下，NAVSIM基准上实现开环SOTA和闭环竞争性结果。

## 📄 摘要（原文）

> Gaining sustainable performance improvement with scaling data and model budget remains a pivotal yet unresolved challenge in autonomous driving. While autoregressive models exhibited promising data-scaling efficiency in planning tasks, predicting ego trajectories alone suffers sparse supervision and weakly constrains how scene evolution should shape ego motion. Therefore, we introduce DAP, a discrete-token autoregressive planner that jointly forecasts BEV semantics and ego trajectories, thereby enforcing comprehensive representation learning and allowing predicted dynamics to directly condition ego motion. In addition, we incorporate a reinforcement-learning-based fine-tuning, which preserves supervised behavior cloning priors while injecting reward-guided improvements. Despite a compact 160M parameter budget, DAP achieves state-of-the-art performance on open-loop metrics and delivers competitive closed-loop results on the NAVSIM benchmark. Overall, the fully discrete-token autoregressive formulation operating on both rasterized BEV and ego actions provides a compact yet scalable planning paradigm for autonomous driving.

