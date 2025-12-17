---
layout: default
title: Adaptive Tuning of Parameterized Traffic Controllers via Multi-Agent Reinforcement Learning
---

# Adaptive Tuning of Parameterized Traffic Controllers via Multi-Agent Reinforcement Learning

**arXiv**: [2512.07417v1](https://arxiv.org/abs/2512.07417) | [PDF](https://arxiv.org/pdf/2512.07417.pdf)

**作者**: Giray Önür, Azita Dabiri, Bart De Schutter

---

## 💡 一句话要点

**提出多智能体强化学习框架，自适应调整参数化交通控制器以应对动态交通**

**关键词**: `多智能体强化学习` `交通控制` `参数自适应` `状态反馈控制器` `系统韧性`

## 📋 核心要点

1. 核心问题：传统状态反馈控制器缺乏适应性，难以处理复杂时变交通动态。
2. 方法要点：多智能体强化学习框架，低频调整控制器参数，结合反应性与适应性。
3. 实验或效果：在模拟多类交通网络中评估，优于无控制和固定参数控制，对部分故障有强韧性。

## 📄 摘要（原文）

> Effective traffic control is essential for mitigating congestion in transportation networks. Conventional traffic management strategies, including route guidance, ramp metering, and traffic signal control, often rely on state feedback controllers, used for their simplicity and reactivity; however, they lack the adaptability required to cope with complex and time-varying traffic dynamics. This paper proposes a multi-agent reinforcement learning framework in which each agent adaptively tunes the parameters of a state feedback traffic controller, combining the reactivity of state feedback controllers with the adaptability of reinforcement learning. By tuning parameters at a lower frequency rather than directly determining control actions at a high frequency, the reinforcement learning agents achieve improved training efficiency while maintaining adaptability to varying traffic conditions. The multi-agent structure further enhances system robustness, as local controllers can operate independently in the event of partial failures. The proposed framework is evaluated on a simulated multi-class transportation network under varying traffic conditions. Results show that the proposed multi-agent framework outperforms the no control and fixed-parameter state feedback control cases, while performing on par with the single-agent RL-based adaptive state feedback control, with a much better resilience to partial failures.

