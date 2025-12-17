---
layout: default
title: Never Too Rigid to Reach: Adaptive Virtual Model Control with LLM- and Lyapunov-Based Reinforcement Learning
---

# Never Too Rigid to Reach: Adaptive Virtual Model Control with LLM- and Lyapunov-Based Reinforcement Learning

**arXiv**: [2510.22892v1](https://arxiv.org/abs/2510.22892) | [PDF](https://arxiv.org/pdf/2510.22892.pdf)

**作者**: Jingzehua Xu, Yangyang Li, Yangfei Chen, Guanwen Xie, Shuai Zhang

---

## 💡 一句话要点

**提出自适应虚拟模型控制，结合LLM与Lyapunov强化学习，提升机械臂在不确定环境中的适应性与稳定性。**

**关键词**: `虚拟模型控制` `强化学习` `大语言模型` `Lyapunov稳定性` `机器人控制` `自适应控制`

## 📋 核心要点

1. 核心问题：传统虚拟模型控制参数固定、组件协调不足，在扰动下易失稳且适应性差。
2. 方法要点：LLM提供先验与推理增强协调，Lyapunov强化学习确保理论稳定性约束。
3. 实验或效果：在7自由度Panda臂仿真中，动态任务表现优异，平衡目标并保证安全。

## 📄 摘要（原文）

> Robotic arms are increasingly deployed in uncertain environments, yet
> conventional control pipelines often become rigid and brittle when exposed to
> perturbations or incomplete information. Virtual Model Control (VMC) enables
> compliant behaviors by embedding virtual forces and mapping them into joint
> torques, but its reliance on fixed parameters and limited coordination among
> virtual components constrains adaptability and may undermine stability as task
> objectives evolve. To address these limitations, we propose Adaptive VMC with
> Large Language Model (LLM)- and Lyapunov-Based Reinforcement Learning (RL),
> which preserves the physical interpretability of VMC while supporting
> stability-guaranteed online adaptation. The LLM provides structured priors and
> high-level reasoning that enhance coordination among virtual components,
> improve sample efficiency, and facilitate flexible adjustment to varying task
> requirements. Complementarily, Lyapunov-based RL enforces theoretical stability
> constraints, ensuring safe and reliable adaptation under uncertainty. Extensive
> simulations on a 7-DoF Panda arm demonstrate that our approach effectively
> balances competing objectives in dynamic tasks, achieving superior performance
> while highlighting the synergistic benefits of LLM guidance and
> Lyapunov-constrained adaptation.

