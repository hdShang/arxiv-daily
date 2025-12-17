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

**提出ARCADE框架，通过在线变化点感知贝叶斯动力学学习，解决机器人系统在动态变化环境中的实时自适应控制问题。**

**关键词**: `机器人自适应控制` `在线贝叶斯学习` `变化点检测` `非线性动力学建模` `实时流数据更新` `概率推理` `闭环跟踪` `无人机应用`

## 📋 核心要点

1. 核心问题：现有方法难以实时适应机器人动力学中的渐进漂移、瞬时波动或突然转变，导致预测不准确和跟踪性能下降。
2. 方法要点：提出ARCADE框架，结合离线表示学习和在线贝叶斯更新，通过变化点感知机制动态调整信息积累，实现快速自适应。
3. 实验或效果：在模拟和真实机器人实验中，ARCADE显著提升预测准确性、加速恢复时间，并改善闭环跟踪性能，优于基线方法。

## 📝 摘要（中文）

现实世界中的机器人必须在动态变化的环境中运行，这些变化可能由操作条件改变、外部干扰或未建模效应引起，表现为渐进漂移、瞬时波动或突然转变，需要实时适应机制，既能抵抗短期变化，又能响应持久变化。本文提出一个框架，用于建模机器人系统的非线性动力学，可从流数据中实时更新。该方法将表示学习与在线适应解耦，利用离线学习的潜在表示支持在线闭式贝叶斯更新。为处理演化条件，引入变化点感知机制，通过从数据似然推断的潜在变量指示连续性或转变。当连续性可能时，证据累积以优化预测；当检测到转变时，过去信息被调节以支持快速重新学习。这保持了校准的不确定性，并支持对瞬时、渐进或结构变化的概率推理。我们证明该框架的自适应遗憾仅随时间对数增长，并与转变次数线性相关，与知道转变时间的神谕方法竞争。在倒立摆模拟和真实四旋翼飞行器实验中验证，包括摆动负载和飞行中掉落场景，相比相关基线，展示了改进的预测准确性、更快恢复和更准确的闭环跟踪。

## 🔬 方法详解

ARCADE框架整体上采用两阶段方法：离线阶段学习非线性动力学的潜在表示，在线阶段基于流数据进行闭式贝叶斯更新。关键技术创新点包括变化点感知机制，通过推断潜在变量来检测动力学连续性或转变，从而动态调节过去信息的权重。与现有方法的主要区别在于解耦表示学习与在线适应，支持实时更新和概率推理，同时理论证明自适应遗憾增长缓慢，增强鲁棒性和效率。

## 📊 实验亮点

在倒立摆模拟和真实四旋翼飞行器实验中，ARCADE相比基线方法，预测准确性提高，恢复时间缩短，闭环跟踪误差降低，特别是在摆动负载和飞行中掉落场景中表现突出，验证了其高效自适应能力。

## 🎯 应用场景

该研究适用于需要实时自适应控制的机器人系统，如无人机在负载变化或干扰下的飞行、工业机器人在动态环境中的操作，以及自主车辆在不确定条件下的导航，提升系统在复杂环境中的鲁棒性和性能。

## 📄 摘要（原文）

> Real-world robots must operate under evolving dynamics caused by changing operating conditions, external disturbances, and unmodeled effects. These may appear as gradual drifts, transient fluctuations, or abrupt shifts, demanding real-time adaptation that is robust to short-term variation yet responsive to lasting change. We propose a framework for modeling the nonlinear dynamics of robotic systems that can be updated in real time from streaming data. The method decouples representation learning from online adaptation, using latent representations learned offline to support online closed-form Bayesian updates. To handle evolving conditions, we introduce a changepoint-aware mechanism with a latent variable inferred from data likelihoods that indicates continuity or shift. When continuity is likely, evidence accumulates to refine predictions; when a shift is detected, past information is tempered to enable rapid re-learning. This maintains calibrated uncertainty and supports probabilistic reasoning about transient, gradual, or structural change. We prove that the adaptive regret of the framework grows only logarithmically in time and linearly with the number of shifts, competitive with an oracle that knows timings of shift. We validate on cartpole simulations and real quadrotor flights with swinging payloads and mid-flight drops, showing improved predictive accuracy, faster recovery, and more accurate closed-loop tracking than relevant baselines.

