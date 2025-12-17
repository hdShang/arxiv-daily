---
layout: default
title: CourtMotion: Learning Event-Driven Motion Representations from Skeletal Data for Basketball
---

# CourtMotion: Learning Event-Driven Motion Representations from Skeletal Data for Basketball

**arXiv**: [2512.01478v1](https://arxiv.org/abs/2512.01478) | [PDF](https://arxiv.org/pdf/2512.01478.pdf)

**作者**: Omer Sela, Michael Chertok, Lior Wolf

---

## 💡 一句话要点

**提出CourtMotion框架，从骨骼数据学习事件驱动运动表示以分析篮球比赛事件**

**关键词**: `骨骼数据建模` `图神经网络` `Transformer` `事件预测` `篮球分析` `时空建模`

## 📋 核心要点

1. 核心问题：传统基于位置的方法无法捕捉身体朝向、防守姿态等关键运动模式，限制篮球事件预测准确性。
2. 方法要点：采用两阶段方法，先通过图神经网络处理骨骼数据，再用Transformer建模球员交互，引入事件投影头连接运动与事件。
3. 实验或效果：在NBA数据上，轨迹预测误差降低35%，并在传球、投篮等下游任务中显著优于现有方法。

## 📄 摘要（原文）

> This paper presents CourtMotion, a spatiotemporal modeling framework for analyzing and predicting game events and plays as they develop in professional basketball. Anticipating basketball events requires understanding both physical motion patterns and their semantic significance in the context of the game. Traditional approaches that use only player positions fail to capture crucial indicators such as body orientation, defensive stance, or shooting preparation motions. Our two-stage approach first processes skeletal tracking data through Graph Neural Networks to capture nuanced motion patterns, then employs a Transformer architecture with specialized attention mechanisms to model player interactions. We introduce event projection heads that explicitly connect player movements to basketball events like passes, shots, and steals, training the model to associate physical motion patterns with their tactical purposes. Experiments on NBA tracking data demonstrate significant improvements over position-only baselines: 35% reduction in trajectory prediction error compared to state-of-the-art position-based models and consistent performance gains across key basketball analytics tasks. The resulting pretrained model serves as a powerful foundation for multiple downstream tasks, with pick detection, shot taker identification, assist prediction, shot location classification, and shot type recognition demonstrating substantial improvements over existing methods.

