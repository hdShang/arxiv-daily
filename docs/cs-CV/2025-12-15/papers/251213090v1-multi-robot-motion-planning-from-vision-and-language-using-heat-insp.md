---
layout: default
title: Multi-Robot Motion Planning from Vision and Language using Heat-Inspired Diffusion
---

# Multi-Robot Motion Planning from Vision and Language using Heat-Inspired Diffusion

**arXiv**: [2512.13090v1](https://arxiv.org/abs/2512.13090) | [PDF](https://arxiv.org/pdf/2512.13090.pdf)

**作者**: Jebeom Chae, Junwoo Chang, Seungho Yeom, Yujin Kim, Jongeun Choi

---

## 💡 一句话要点

**提出语言条件热启发扩散框架，以解决多机器人视觉语言运动规划中的泛化与计算效率问题。**

**关键词**: `多机器人运动规划` `扩散模型` `语言条件规划` `视觉导航` `碰撞避免` `语义先验`

## 📋 核心要点

1. 核心问题：扩散模型在多机器人语言条件规划中泛化差、计算成本高，缺乏几何可达性推理。
2. 方法要点：集成CLIP语义先验与碰撞避免扩散核，无需显式障碍信息，严格约束语言命令于可达工作空间。
3. 实验或效果：在多样化地图和真实机器人实验中，成功率和规划延迟优于现有扩散规划器。

## 📄 摘要（原文）

> Diffusion models have recently emerged as powerful tools for robot motion planning by capturing the multi-modal distribution of feasible trajectories. However, their extension to multi-robot settings with flexible, language-conditioned task specifications remains limited. Furthermore, current diffusion-based approaches incur high computational cost during inference and struggle with generalization because they require explicit construction of environment representations and lack mechanisms for reasoning about geometric reachability. To address these limitations, we present Language-Conditioned Heat-Inspired Diffusion (LCHD), an end-to-end vision-based framework that generates language-conditioned, collision-free trajectories. LCHD integrates CLIP-based semantic priors with a collision-avoiding diffusion kernel serving as a physical inductive bias that enables the planner to interpret language commands strictly within the reachable workspace. This naturally handles out-of-distribution scenarios -- in terms of reachability -- by guiding robots toward accessible alternatives that match the semantic intent, while eliminating the need for explicit obstacle information at inference time. Extensive evaluations on diverse real-world-inspired maps, along with real-robot experiments, show that LCHD consistently outperforms prior diffusion-based planners in success rate, while reducing planning latency.

