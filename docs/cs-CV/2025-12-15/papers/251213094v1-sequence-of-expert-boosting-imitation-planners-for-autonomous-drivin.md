---
layout: default
title: Sequence of Expert: Boosting Imitation Planners for Autonomous Driving through Temporal Alternation
---

# Sequence of Expert: Boosting Imitation Planners for Autonomous Driving through Temporal Alternation

**arXiv**: [2512.13094v1](https://arxiv.org/abs/2512.13094) | [PDF](https://arxiv.org/pdf/2512.13094.pdf)

**作者**: Xiang Li, Gang Liu, Weitao Zhou, Hongyi Zhu, Zhong Cao

---

## 💡 一句话要点

**提出Sequence of Experts方法，通过时序交替策略提升自动驾驶模仿规划器的闭环性能。**

**关键词**: `自动驾驶` `模仿学习` `时序交替` `闭环规划` `鲁棒性增强` `nuPlan基准`

## 📋 核心要点

1. 核心问题：模仿学习在自动驾驶中因误差累积导致闭环性能下降，现有方法多关注单时间点状态级鲁棒性。
2. 方法要点：引入Sequence of Experts，一种时序交替策略，无需增加模型规模或数据需求，利用时间尺度增强鲁棒性。
3. 实验或效果：在nuPlan基准测试中，SoE方法显著提升所有评估模型性能，达到未知水平。

## 📄 摘要（原文）

> Imitation learning (IL) has emerged as a central paradigm in autonomous driving. While IL excels in matching expert behavior in open-loop settings by minimizing per-step prediction errors, its performance degrades unexpectedly in closed-loop due to the gradual accumulation of small, often imperceptible errors over time.Over successive planning cycles, these errors compound, potentially resulting in severe failures.Current research efforts predominantly rely on increasingly sophisticated network architectures or high-fidelity training datasets to enhance the robustness of IL planners against error accumulation, focusing on the state-level robustness at a single time point. However, autonomous driving is inherently a continuous-time process, and leveraging the temporal scale to enhance robustness may provide a new perspective for addressing this issue.To this end, we propose a method termed Sequence of Experts (SoE), a temporal alternation policy that enhances closed-loop performance without increasing model size or data requirements. Our experiments on large-scale autonomous driving benchmarks nuPlan demonstrate that SoE method consistently and significantly improves the performance of all the evaluated models, and achieves state-of-the-art performance.This module may provide a key and widely applicable support for improving the training efficiency of autonomous driving models.

