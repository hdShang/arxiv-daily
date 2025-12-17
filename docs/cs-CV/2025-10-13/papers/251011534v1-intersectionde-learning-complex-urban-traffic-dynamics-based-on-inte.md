---
layout: default
title: IntersectioNDE: Learning Complex Urban Traffic Dynamics based on Interaction Decoupling Strategy
---

# IntersectioNDE: Learning Complex Urban Traffic Dynamics based on Interaction Decoupling Strategy

**arXiv**: [2510.11534v1](https://arxiv.org/abs/2510.11534) | [PDF](https://arxiv.org/pdf/2510.11534.pdf)

**作者**: Enli Lin, Ziyuan Yang, Qiujing Lu, Jianming Hu, Shuo Feng

---

## 💡 一句话要点

**提出IntersectioNDE模拟器，基于交互解耦策略学习复杂城市交叉口交通动态**

**关键词**: `交通模拟` `交互解耦` `城市交叉口` `多智能体交互` `数据驱动模拟` `Transformer网络`

## 📋 核心要点

1. 核心问题：现有模拟器难以建模密集异构交互和高维联合分布，导致模式崩溃和长期不稳定
2. 方法要点：引入交互解耦策略，从代理子集学习组合动态，集成场景感知Transformer网络
3. 实验或效果：在CiCross数据集上验证，模拟保真度、稳定性和复杂动态复现能力优于基线

## 📄 摘要（原文）

> Realistic traffic simulation is critical for ensuring the safety and
> reliability of autonomous vehicles (AVs), especially in complex and diverse
> urban traffic environments. However, existing data-driven simulators face two
> key challenges: a limited focus on modeling dense, heterogeneous interactions
> at urban intersections - which are prevalent, crucial, and practically
> significant in countries like China, featuring diverse agents including
> motorized vehicles (MVs), non-motorized vehicles (NMVs), and pedestrians - and
> the inherent difficulty in robustly learning high-dimensional joint
> distributions for such high-density scenes, often leading to mode collapse and
> long-term simulation instability. We introduce City Crossings Dataset
> (CiCross), a large-scale dataset collected from a real-world urban
> intersection, uniquely capturing dense, heterogeneous multi-agent interactions,
> particularly with a substantial proportion of MVs, NMVs and pedestrians. Based
> on this dataset, we propose IntersectioNDE (Intersection Naturalistic Driving
> Environment), a data-driven simulator tailored for complex urban intersection
> scenarios. Its core component is the Interaction Decoupling Strategy (IDS), a
> training paradigm that learns compositional dynamics from agent subsets,
> enabling the marginal-to-joint simulation. Integrated into a scene-aware
> Transformer network with specialized training techniques, IDS significantly
> enhances simulation robustness and long-term stability for modeling
> heterogeneous interactions. Experiments on CiCross show that IntersectioNDE
> outperforms baseline methods in simulation fidelity, stability, and its ability
> to replicate complex, distribution-level urban traffic dynamics.

