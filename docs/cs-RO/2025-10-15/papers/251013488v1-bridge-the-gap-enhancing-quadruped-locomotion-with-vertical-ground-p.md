---
layout: default
title: Bridge the Gap: Enhancing Quadruped Locomotion with Vertical Ground Perturbations
---

# Bridge the Gap: Enhancing Quadruped Locomotion with Vertical Ground Perturbations

**arXiv**: [2510.13488v1](https://arxiv.org/abs/2510.13488) | [PDF](https://arxiv.org/pdf/2510.13488.pdf)

**作者**: Maximilian Stasica, Arne Bick, Nico Bohlinger, Omid Mohseni, Max Johannes Alois Fritzsche, Clemens Hübler, Jan Peters, André Seyfarth

---

## 💡 一句话要点

**提出在振荡桥上训练四足机器人以增强垂直地面扰动下的运动鲁棒性**

**关键词**: `四足机器人运动` `强化学习训练` `垂直地面扰动` `零样本迁移` `步态策略`

## 📋 核心要点

1. 核心问题：四足机器人在垂直地面扰动（如振荡表面）下的运动性能未充分探索。
2. 方法要点：使用PPO强化学习在MuJoCo模拟中训练多种步态策略，结合域随机化实现零样本迁移。
3. 实验或效果：振荡桥训练策略在真实世界中表现出更高的稳定性和适应性。

## 📄 摘要（原文）

> Legged robots, particularly quadrupeds, excel at navigating rough terrains,
> yet their performance under vertical ground perturbations, such as those from
> oscillating surfaces, remains underexplored. This study introduces a novel
> approach to enhance quadruped locomotion robustness by training the Unitree Go2
> robot on an oscillating bridge - a 13.24-meter steel-and-concrete structure
> with a 2.0 Hz eigenfrequency designed to perturb locomotion. Using
> Reinforcement Learning (RL) with the Proximal Policy Optimization (PPO)
> algorithm in a MuJoCo simulation, we trained 15 distinct locomotion policies,
> combining five gaits (trot, pace, bound, free, default) with three training
> conditions: rigid bridge and two oscillating bridge setups with differing
> height regulation strategies (relative to bridge surface or ground). Domain
> randomization ensured zero-shot transfer to the real-world bridge. Our results
> demonstrate that policies trained on the oscillating bridge exhibit superior
> stability and adaptability compared to those trained on rigid surfaces. Our
> framework enables robust gait patterns even without prior bridge exposure.
> These findings highlight the potential of simulation-based RL to improve
> quadruped locomotion during dynamic ground perturbations, offering insights for
> designing robots capable of traversing vibrating environments.

