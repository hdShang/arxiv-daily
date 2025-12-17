---
layout: default
title: Agility Meets Stability: Versatile Humanoid Control with Heterogeneous Data
---

# Agility Meets Stability: Versatile Humanoid Control with Heterogeneous Data

**arXiv**: [2511.17373v1](https://arxiv.org/abs/2511.17373) | [PDF](https://arxiv.org/pdf/2511.17373.pdf)

**作者**: Yixuan Pan, Ruoyi Qiao, Li Chen, Kashyap Chitta, Liang Pan, Haoguang Mai, Qingwen Bu, Hao Zhao, Cunyuan Zheng, Ping Luo, Hongyang Li

---

## 💡 一句话要点

**提出AMS框架以统一人形机器人的动态运动跟踪与极端平衡控制**

**关键词**: `人形机器人控制` `异构数据学习` `混合奖励设计` `自适应训练策略` `动态运动跟踪` `平衡维护`

## 📋 核心要点

1. 核心问题：现有方法在敏捷性与稳定性间难以兼顾，导致控制器功能单一。
2. 方法要点：利用异构数据源和混合奖励方案，结合自适应学习策略训练单一策略。
3. 实验或效果：在仿真和真实机器人上验证，能执行舞蹈、奔跑及零样本平衡动作。

## 📄 摘要（原文）

> Humanoid robots are envisioned to perform a wide range of tasks in human-centered environments, requiring controllers that combine agility with robust balance. Recent advances in locomotion and whole-body tracking have enabled impressive progress in either agile dynamic skills or stability-critical behaviors, but existing methods remain specialized, focusing on one capability while compromising the other. In this work, we introduce AMS (Agility Meets Stability), the first framework that unifies both dynamic motion tracking and extreme balance maintenance in a single policy. Our key insight is to leverage heterogeneous data sources: human motion capture datasets that provide rich, agile behaviors, and physically constrained synthetic balance motions that capture stability configurations. To reconcile the divergent optimization goals of agility and stability, we design a hybrid reward scheme that applies general tracking objectives across all data while injecting balance-specific priors only into synthetic motions. Further, an adaptive learning strategy with performance-driven sampling and motion-specific reward shaping enables efficient training across diverse motion distributions. We validate AMS extensively in simulation and on a real Unitree G1 humanoid. Experiments demonstrate that a single policy can execute agile skills such as dancing and running, while also performing zero-shot extreme balance motions like Ip Man's Squat, highlighting AMS as a versatile control paradigm for future humanoid applications.

