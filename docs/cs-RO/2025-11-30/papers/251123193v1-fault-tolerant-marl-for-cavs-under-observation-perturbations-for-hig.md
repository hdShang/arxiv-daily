---
layout: default
title: Fault-Tolerant MARL for CAVs under Observation Perturbations for Highway On-Ramp Merging
---

# Fault-Tolerant MARL for CAVs under Observation Perturbations for Highway On-Ramp Merging

**arXiv**: [2511.23193v1](https://arxiv.org/abs/2511.23193) | [PDF](https://arxiv.org/pdf/2511.23193.pdf)

**作者**: Yuchen Shi, Huaxin Pei, Yi Zhang, Danya Yao

---

## 💡 一句话要点

**提出故障容错多智能体强化学习方法，以解决高速公路匝道合流场景中观测扰动问题。**

**关键词**: `多智能体强化学习` `故障容错` `观测扰动` `高速公路合流` `对抗训练` `自诊断`

## 📋 核心要点

1. 核心问题：多智能体强化学习在联网自动驾驶车辆中因观测故障（如数据扰动）导致性能下降，缺乏故障容错能力。
2. 方法要点：引入对抗性故障注入智能体生成扰动以强化训练，并设计具备自诊断能力的故障容错车辆智能体，利用时空相关性检测故障并重构可信观测。
3. 实验或效果：在模拟高速公路合流场景中，该方法显著优于基线方法，在各种观测故障模式下实现接近无故障的安全和效率水平。

## 📄 摘要（原文）

> Multi-Agent Reinforcement Learning (MARL) holds significant promise for enabling cooperative driving among Connected and Automated Vehicles (CAVs). However, its practical application is hindered by a critical limitation, i.e., insufficient fault tolerance against observational faults. Such faults, which appear as perturbations in the vehicles' perceived data, can substantially compromise the performance of MARL-based driving systems. Addressing this problem presents two primary challenges. One is to generate adversarial perturbations that effectively stress the policy during training, and the other is to equip vehicles with the capability to mitigate the impact of corrupted observations. To overcome the challenges, we propose a fault-tolerant MARL method for cooperative on-ramp vehicles incorporating two key agents. First, an adversarial fault injection agent is co-trained to generate perturbations that actively challenge and harden the vehicle policies. Second, we design a novel fault-tolerant vehicle agent equipped with a self-diagnosis capability, which leverages the inherent spatio-temporal correlations in vehicle state sequences to detect faults and reconstruct credible observations, thereby shielding the policy from misleading inputs. Experiments in a simulated highway merging scenario demonstrate that our method significantly outperforms baseline MARL approaches, achieving near-fault-free levels of safety and efficiency under various observation fault patterns.

