---
layout: default
title: MPCFormer: A physics-informed data-driven approach for explainable socially-aware autonomous driving
---

# MPCFormer: A physics-informed data-driven approach for explainable socially-aware autonomous driving

**arXiv**: [2512.03795v1](https://arxiv.org/abs/2512.03795) | [PDF](https://arxiv.org/pdf/2512.03795.pdf)

**作者**: Jia Hu, Zhexi Lian, Xuerun Yan, Ruiang Bi, Dou Shen, Yu Ruan, Haoran Wang

---

## 💡 一句话要点

**提出MPCFormer以解决自动驾驶在动态交互场景中缺乏社会交互理解的问题**

**关键词**: `自动驾驶` `社会交互建模` `Transformer` `模型预测控制` `轨迹预测` `可解释性`

## 📋 核心要点

1. 核心问题：自动驾驶在动态交通中难以模拟人类行为，源于对社会交互机制理解不足
2. 方法要点：结合物理先验与数据驱动，通过Transformer学习多车社会交互动力学，并集成MPC框架提升安全性和可解释性
3. 实验或效果：在NGSIM数据集上轨迹预测误差最低（ADE 0.86米），闭环实验中规划成功率94.67%，碰撞率降至0.5%

## 📄 摘要（原文）

> Autonomous Driving (AD) vehicles still struggle to exhibit human-like behavior in highly dynamic and interactive traffic scenarios. The key challenge lies in AD's limited ability to interact with surrounding vehicles, largely due to a lack of understanding the underlying mechanisms of social interaction. To address this issue, we introduce MPCFormer, an explainable socially-aware autonomous driving approach with physics-informed and data-driven coupled social interaction dynamics. In this model, the dynamics are formulated into a discrete space-state representation, which embeds physics priors to enhance modeling explainability. The dynamics coefficients are learned from naturalistic driving data via a Transformer-based encoder-decoder architecture. To the best of our knowledge, MPCFormer is the first approach to explicitly model the dynamics of multi-vehicle social interactions. The learned social interaction dynamics enable the planner to generate manifold, human-like behaviors when interacting with surrounding traffic. By leveraging the MPC framework, the approach mitigates the potential safety risks typically associated with purely learning-based methods. Open-looped evaluation on NGSIM dataset demonstrates that MPCFormer achieves superior social interaction awareness, yielding the lowest trajectory prediction errors compared with other state-of-the-art approach. The prediction achieves an ADE as low as 0.86 m over a long prediction horizon of 5 seconds. Close-looped experiments in highly intense interaction scenarios, where consecutive lane changes are required to exit an off-ramp, further validate the effectiveness of MPCFormer. Results show that MPCFormer achieves the highest planning success rate of 94.67%, improves driving efficiency by 15.75%, and reduces the collision rate from 21.25% to 0.5%, outperforming a frontier Reinforcement Learning (RL) based planner.

