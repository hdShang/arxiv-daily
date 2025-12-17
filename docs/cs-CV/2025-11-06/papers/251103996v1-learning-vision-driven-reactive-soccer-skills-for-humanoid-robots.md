---
layout: default
title: Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots
---

# Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots

**arXiv**: [2511.03996v1](https://arxiv.org/abs/2511.03996) | [PDF](https://arxiv.org/pdf/2511.03996.pdf)

**作者**: Yushi Wang, Changsheng Luo, Penghui Chen, Jianran Liu, Weijian Sun, Tong Guo, Kechang Yang, Biao Hu, Yangang Zhang, Mingguo Zhao

---

## 💡 一句话要点

**提出统一强化学习控制器，使人形机器人通过视觉与运动直接集成学习反应式足球技能。**

**关键词**: `人形机器人` `强化学习` `视觉感知` `运动控制` `对抗运动先验` `虚拟感知系统`

## 📋 核心要点

1. 核心问题：现有系统模块解耦导致动态环境中响应延迟和行为不连贯，感知限制加剧问题。
2. 方法要点：扩展对抗运动先验到感知设置，结合编码器-解码器架构和虚拟感知系统。
3. 实验或效果：控制器在真实RoboCup比赛中表现出强反应性，执行连贯且鲁棒的足球行为。

## 📄 摘要（原文）

> Humanoid soccer poses a representative challenge for embodied intelligence,
> requiring robots to operate within a tightly coupled perception-action loop.
> However, existing systems typically rely on decoupled modules, resulting in
> delayed responses and incoherent behaviors in dynamic environments, while
> real-world perceptual limitations further exacerbate these issues. In this
> work, we present a unified reinforcement learning-based controller that enables
> humanoid robots to acquire reactive soccer skills through the direct
> integration of visual perception and motion control. Our approach extends
> Adversarial Motion Priors to perceptual settings in real-world dynamic
> environments, bridging motion imitation and visually grounded dynamic control.
> We introduce an encoder-decoder architecture combined with a virtual perception
> system that models real-world visual characteristics, allowing the policy to
> recover privileged states from imperfect observations and establish active
> coordination between perception and action. The resulting controller
> demonstrates strong reactivity, consistently executing coherent and robust
> soccer behaviors across various scenarios, including real RoboCup matches.

