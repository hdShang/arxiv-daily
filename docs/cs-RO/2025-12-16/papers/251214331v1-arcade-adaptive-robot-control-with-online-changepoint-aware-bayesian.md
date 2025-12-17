---
layout: default
title: ARCADE: Adaptive Robot Control with Online Changepoint-Aware Bayesian Dynamics Learning
---

# ARCADE: Adaptive Robot Control with Online Changepoint-Aware Bayesian Dynamics Learning

**arXiv**: [2512.14331v1](https://arxiv.org/abs/2512.14331) | [PDF](https://arxiv.org/pdf/2512.14331.pdf)

**作者**: Rishabh Dev Yadav, Avirup Das, Hongyu Song, Samuel Kaski, Wei Pan

**分类**: cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出ARCADE框架，通过在线变点感知贝叶斯动力学学习解决机器人动态变化下的自适应控制问题。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `自适应机器人控制` `在线贝叶斯学习` `变点检测` `动力学建模` `非线性系统` `实时适应` `不确定性校准` `机器人鲁棒性`

## 📋 核心要点

1. 核心问题：机器人动态变化（如漂移、波动、突变）要求实时自适应，现有方法难以平衡短期鲁棒性与持久变化响应。
2. 方法要点：解耦表示学习与在线适应，引入变点感知机制，基于贝叶斯更新实现快速重学习。
3. 实验或效果：在仿真和真实实验中，预测准确性、恢复速度和跟踪精度均优于基线，自适应遗憾增长缓慢。

## 📝 摘要（中文）

现实世界中的机器人必须在动态变化的环境中运行，这些变化可能由操作条件改变、外部干扰或未建模效应引起，表现为渐进漂移、瞬态波动或突然转变，需要实时适应能力，既能抵抗短期变化又能响应持久变化。我们提出一个框架，用于建模机器人系统的非线性动力学，能够从流数据中实时更新。该方法将表示学习与在线适应解耦，利用离线学习的潜在表示支持在线闭式贝叶斯更新。为处理演化条件，我们引入一个变点感知机制，通过从数据似然推断的潜在变量指示连续性或转变。当连续性可能时，证据积累以优化预测；当检测到转变时，过去信息被调节以支持快速重新学习。这保持了校准的不确定性，并支持对瞬态、渐进或结构变化的概率推理。我们证明该框架的自适应遗憾仅随时间对数增长，与转变次数线性相关，与已知转变时间的神谕者竞争。我们在倒立摆仿真和真实四旋翼飞行器实验中验证，包括摆动负载和飞行中掉落场景，显示相比相关基线，预测准确性更高、恢复更快、闭环跟踪更准确。

## 🔬 方法详解

ARCADE框架整体采用离线学习潜在表示与在线贝叶斯更新相结合的方式。关键技术创新点包括：1) 表示学习与在线适应解耦，利用离线学习的潜在表示支持在线闭式贝叶斯更新，提高计算效率；2) 变点感知机制，通过推断潜在变量（基于数据似然）动态检测连续性或转变，实现自适应调节；3) 当检测到转变时，调节过去信息以促进快速重新学习，同时保持不确定性校准。与现有方法的主要区别在于其能够实时处理动态变化（包括瞬态、渐进和结构变化），并通过理论证明自适应遗憾增长缓慢（对数时间与线性转变次数），提供更强的鲁棒性和适应性。

## 📊 实验亮点

在倒立摆仿真和真实四旋翼飞行器实验中，ARCADE框架相比基线方法，预测准确性显著提升，恢复速度更快（如在负载掉落场景中），闭环跟踪精度更高。理论分析显示自适应遗憾仅随时间对数增长，与转变次数线性相关，验证了其高效性和鲁棒性。

## 🎯 应用场景

该研究适用于需要实时适应动态变化的机器人系统，如无人机在负载变化或外部干扰下的飞行控制、工业机器人在环境波动中的操作、自动驾驶车辆在路况突变时的导航。潜在价值包括提高机器人在不确定环境中的鲁棒性、安全性和效率，支持更广泛的实际部署。

## 📄 摘要（原文）

> Real-world robots must operate under evolving dynamics caused by changing operating conditions, external disturbances, and unmodeled effects. These may appear as gradual drifts, transient fluctuations, or abrupt shifts, demanding real-time adaptation that is robust to short-term variation yet responsive to lasting change. We propose a framework for modeling the nonlinear dynamics of robotic systems that can be updated in real time from streaming data. The method decouples representation learning from online adaptation, using latent representations learned offline to support online closed-form Bayesian updates. To handle evolving conditions, we introduce a changepoint-aware mechanism with a latent variable inferred from data likelihoods that indicates continuity or shift. When continuity is likely, evidence accumulates to refine predictions; when a shift is detected, past information is tempered to enable rapid re-learning. This maintains calibrated uncertainty and supports probabilistic reasoning about transient, gradual, or structural change. We prove that the adaptive regret of the framework grows only logarithmically in time and linearly with the number of shifts, competitive with an oracle that knows timings of shift. We validate on cartpole simulations and real quadrotor flights with swinging payloads and mid-flight drops, showing improved predictive accuracy, faster recovery, and more accurate closed-loop tracking than relevant baselines.

