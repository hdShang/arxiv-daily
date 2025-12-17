---
layout: default
title: Digital Twin-based Control Co-Design of Full Vehicle Active Suspensions via Deep Reinforcement Learning
---

# Digital Twin-based Control Co-Design of Full Vehicle Active Suspensions via Deep Reinforcement Learning

**arXiv**: [2512.03891v1](https://arxiv.org/abs/2512.03891) | [PDF](https://arxiv.org/pdf/2512.03891.pdf)

**作者**: Ying-Kuan Tsai, Yi-Ping Chen, Vispi Karkaria, Wei Chen

---

## 💡 一句话要点

**提出基于数字孪生和深度强化学习的整车主动悬架控制协同设计框架，以优化动态工况下的性能。**

**关键词**: `数字孪生` `深度强化学习` `控制协同设计` `主动悬架系统` `不确定性建模` `个性化优化`

## 📋 核心要点

1. 核心问题：主动悬架系统在不确定动态工况下性能受限，硬件与控制策略难以自适应。
2. 方法要点：集成自动微分于深度强化学习，联合优化物理组件与控制策略，并引入分位数学习处理数据不确定性。
3. 实验或效果：在温和与激进驾驶设置下，优化系统轨迹更平滑，控制努力分别减少约43%和52%，保持舒适与稳定。

## 📄 摘要（原文）

> Active suspension systems are critical for enhancing vehicle comfort, safety, and stability, yet their performance is often limited by fixed hardware designs and control strategies that cannot adapt to uncertain and dynamic operating conditions. Recent advances in digital twins (DTs) and deep reinforcement learning (DRL) offer new opportunities for real-time, data-driven optimization across a vehicle's lifecycle. However, integrating these technologies into a unified framework remains an open challenge. This work presents a DT-based control co-design (CCD) framework for full-vehicle active suspensions using multi-generation design concepts. By integrating automatic differentiation into DRL, we jointly optimize physical suspension components and control policies under varying driver behaviors and environmental uncertainties. DRL also addresses the challenge of partial observability, where only limited states can be sensed and fed back to the controller, by learning optimal control actions directly from available sensor information. The framework incorporates model updating with quantile learning to capture data uncertainty, enabling real-time decision-making and adaptive learning from digital-physical interactions. The approach demonstrates personalized optimization of suspension systems under two distinct driving settings (mild and aggressive). Results show that the optimized systems achieve smoother trajectories and reduce control efforts by approximately 43% and 52% for mild and aggressive, respectively, while maintaining ride comfort and stability. Contributions include: developing a DT-enabled CCD framework integrating DRL and uncertainty-aware model updating for full-vehicle active suspensions, introducing a multi-generation design strategy for self-improving systems, and demonstrating personalized optimization of active suspension systems for distinct driver types.

