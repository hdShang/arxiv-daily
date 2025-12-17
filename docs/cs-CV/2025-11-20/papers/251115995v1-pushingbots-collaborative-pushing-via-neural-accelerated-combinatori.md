---
layout: default
title: PushingBots: Collaborative Pushing via Neural Accelerated Combinatorial Hybrid Optimization
---

# PushingBots: Collaborative Pushing via Neural Accelerated Combinatorial Hybrid Optimization

**arXiv**: [2511.15995v1](https://arxiv.org/abs/2511.15995) | [PDF](https://arxiv.org/pdf/2511.15995.pdf)

**作者**: Zili Tang, Ying Zhang, Meng Guo

---

## 💡 一句话要点

**提出基于组合混合优化的协作推动方法，解决多机器人推动任意物体问题**

**关键词**: `多机器人协作` `非抓取操作` `组合优化` `混合控制` `扩散加速器`

## 📋 核心要点

1. 核心问题：多机器人在复杂环境中协作推动任意形状物体，处理任务协调和接触模式切换
2. 方法要点：组合优化任务分配，关键帧引导混合搜索，扩散加速器提升规划效率
3. 实验或效果：仿真和硬件验证效率，适用于异构机器人和6D推动

## 📄 摘要（原文）

> Many robots are not equipped with a manipulator and many objects are not suitable for prehensile manipulation (such as large boxes and cylinders). In these cases, pushing is a simple yet effective non-prehensile skill for robots to interact with and further change the environment. Existing work often assumes a set of predefined pushing modes and fixed-shape objects. This work tackles the general problem of controlling a robotic fleet to push collaboratively numerous arbitrary objects to respective destinations, within complex environments of cluttered and movable obstacles. It incorporates several characteristic challenges for multi-robot systems such as online task coordination under large uncertainties of cost and duration, and for contact-rich tasks such as hybrid switching among different contact modes, and under-actuation due to constrained contact forces. The proposed method is based on combinatorial hybrid optimization over dynamic task assignments and hybrid execution via sequences of pushing modes and associated forces. It consists of three main components: (I) the decomposition, ordering and rolling assignment of pushing subtasks to robot subgroups; (II) the keyframe guided hybrid search to optimize the sequence of parameterized pushing modes for each subtask; (III) the hybrid control to execute these modes and transit among them. Last but not least, a diffusion-based accelerator is adopted to predict the keyframes and pushing modes that should be prioritized during hybrid search; and further improve planning efficiency. The framework is complete under mild assumptions. Its efficiency and effectiveness under different numbers of robots and general-shaped objects are validated extensively in simulations and hardware experiments, as well as generalizations to heterogeneous robots, planar assembly and 6D pushing.

