---
layout: default
title: One-shot Humanoid Whole-body Motion Learning
---

# One-shot Humanoid Whole-body Motion Learning

**arXiv**: [2510.25241v1](https://arxiv.org/abs/2510.25241) | [PDF](https://arxiv.org/pdf/2510.25241.pdf)

**作者**: Hao Huang, Geeta Chandra Raju Bethala, Shuaihang Yuan, Congcong Wen, Anthony Tzes, Yi Fang

---

## 💡 一句话要点

**提出单样本人形机器人全身运动学习方法，利用行走运动生成新动作**

**关键词**: `人形机器人运动` `单样本学习` `最优传输` `姿态插值` `强化学习` `运动重定向`

## 📋 核心要点

1. 核心问题：传统方法需多样本训练，数据收集成本高且耗时
2. 方法要点：使用保序最优传输计算距离，插值生成中间姿态，优化后训练策略
3. 实验效果：在CMU MoCap数据集上优于基线，性能指标提升

## 📄 摘要（原文）

> Whole-body humanoid motion represents a cornerstone challenge in robotics,
> integrating balance, coordination, and adaptability to enable human-like
> behaviors. However, existing methods typically require multiple training
> samples per motion category, rendering the collection of high-quality human
> motion datasets both labor-intensive and costly. To address this, we propose a
> novel approach that trains effective humanoid motion policies using only a
> single non-walking target motion sample alongside readily available walking
> motions. The core idea lies in leveraging order-preserving optimal transport to
> compute distances between walking and non-walking sequences, followed by
> interpolation along geodesics to generate new intermediate pose skeletons,
> which are then optimized for collision-free configurations and retargeted to
> the humanoid before integration into a simulated environment for policy
> training via reinforcement learning. Experimental evaluations on the CMU MoCap
> dataset demonstrate that our method consistently outperforms baselines,
> achieving superior performance across metrics. Code will be released upon
> acceptance.

