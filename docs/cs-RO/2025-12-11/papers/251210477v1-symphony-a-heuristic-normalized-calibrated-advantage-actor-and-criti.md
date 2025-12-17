---
layout: default
title: Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots
---

# Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots

**arXiv**: [2512.10477v1](https://arxiv.org/abs/2512.10477) | [PDF](https://arxiv.org/pdf/2512.10477.pdf)

**作者**: Timur Ishuov, Michele Folgheraiter, Madi Nurmanov, Goncalo Gordo, Richárd Farkas, József Dombi

---

## 💡 一句话要点

**提出Symphony算法，通过归一化校准优势与确定性策略，实现人形机器人安全高效训练。**

**关键词**: `人形机器人控制` `强化学习算法` `样本效率优化` `动作安全性` `确定性策略梯度` `经验回放缓冲`

## 📋 核心要点

1. 核心问题：机器人从零训练需高样本效率与安全性，避免机械损伤。
2. 方法要点：结合Swaddling正则化限制动作强度，使用Fading Replay Buffer优化样本采样。
3. 实验或效果：相比随机算法，减少噪声并提升动作安全性，实现单次更新Actor与Critic。

## 📄 摘要（原文）

> In our work we not explicitly hint that it is a misconception to think that humans learn fast. Learning process takes time. Babies start learning to move in the restricted liquid area called placenta. Children often are limited by underdeveloped body. Even adults are not allowed to participate in complex competitions right away. However, with robots, when learning from scratch, we often don't have the privilege of waiting for dozen millions of steps. "Swaddling" regularization is responsible for restraining an agent in rapid but unstable development penalizing action strength in a specific way not affecting actions directly. The Symphony, Transitional-policy Deterministic Actor and Critic algorithm, is a concise combination of different ideas for possibility of training humanoid robots from scratch with Sample Efficiency, Sample Proximity and Safety of Actions in mind. It is no secret that continuous increase in Gaussian noise without appropriate smoothing is harmful for motors and gearboxes. Compared to Stochastic algorithms, we set a limited parametric noise and promote a reduced strength of actions, safely increasing entropy, since the actions are kind of immersed in weaker noise. When actions require more extreme values, actions rise above the weak noise. Training becomes empirically much safer for both the environment around and the robot's mechanisms. We use Fading Replay Buffer: using a fixed formula containing the hyperbolic tangent, we adjust the batch sampling probability: the memory contains a recent memory and a long-term memory trail. Fading Replay Buffer allows us to use Temporal Advantage when we improve the current Critic Network prediction compared to the exponential moving average. Temporal Advantage allows us to update Actor and Critic in one pass, as well as combine Actor and Critic in one Object and implement their Losses in one line.

