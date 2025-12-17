---
layout: default
title: LongComp: Long-Tail Compositional Zero-Shot Generalization for Robust Trajectory Prediction
---

# LongComp: Long-Tail Compositional Zero-Shot Generalization for Robust Trajectory Prediction

**arXiv**: [2511.10411v1](https://arxiv.org/abs/2511.10411) | [PDF](https://arxiv.org/pdf/2511.10411.pdf)

**作者**: Benjamin Stoler, Jonathan Francis, Jean Oh

---

## 💡 一句话要点

**提出长尾组合零样本泛化方法以提升自动驾驶轨迹预测的鲁棒性**

**关键词**: `轨迹预测` `组合零样本学习` `长尾分布` `自动驾驶` `分布外泛化` `模块化网络`

## 📋 核心要点

1. 核心问题：自动驾驶轨迹预测在罕见安全关键场景中依赖真实数据不足，导致分布外泛化能力差。
2. 方法要点：引入安全场景因子化框架和任务模块化门控网络，结合难度预测头优化内部表示。
3. 实验或效果：在闭世界和开世界设置中，分布外性能差距分别从5.0%和14.7%降至2.8%和11.5%。

## 📄 摘要（原文）

> Methods for trajectory prediction in Autonomous Driving must contend with rare, safety-critical scenarios that make reliance on real-world data collection alone infeasible. To assess robustness under such conditions, we propose new long-tail evaluation settings that repartition datasets to create challenging out-of-distribution (OOD) test sets. We first introduce a safety-informed scenario factorization framework, which disentangles scenarios into discrete ego and social contexts. Building on analogies to compositional zero-shot image-labeling in Computer Vision, we then hold out novel context combinations to construct challenging closed-world and open-world settings. This process induces OOD performance gaps in future motion prediction of 5.0% and 14.7% in closed-world and open-world settings, respectively, relative to in-distribution performance for a state-of-the-art baseline. To improve generalization, we extend task-modular gating networks to operate within trajectory prediction models, and develop an auxiliary, difficulty-prediction head to refine internal representations. Our strategies jointly reduce the OOD performance gaps to 2.8% and 11.5% in the two settings, respectively, while still improving in-distribution performance.

