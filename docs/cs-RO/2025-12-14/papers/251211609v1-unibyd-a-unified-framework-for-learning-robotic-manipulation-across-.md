---
layout: default
title: UniBYD: A Unified Framework for Learning Robotic Manipulation Across Embodiments Beyond Imitation of Human Demonstrations
---

# UniBYD: A Unified Framework for Learning Robotic Manipulation Across Embodiments Beyond Imitation of Human Demonstrations

**arXiv**: [2512.11609v1](https://arxiv.org/abs/2512.11609) | [PDF](https://arxiv.org/pdf/2512.11609.pdf)

**作者**: Tingyu Yuan, Biaoliang Guan, Wen Ye, Ziyan Tian, Yi Yang, Weijie Zhou, Yan Huang, Peng Wang, Chaoyang Zhao, Jinqiao Wang

---

## 💡 一句话要点

**提出UniBYD统一框架，通过动态强化学习超越人类演示模仿，适应多样机器人手形态。**

**关键词**: `机器人操作学习` `统一形态表示` `动态强化学习` `超越模仿` `多形态基准` `混合马尔可夫引擎`

## 📋 核心要点

1. 核心问题：机器人手与人类手间的形态差异阻碍从人类演示中学习，现有方法局限于模仿，性能受限。
2. 方法要点：引入统一形态表示（UMR）和动态PPO算法，结合混合马尔可夫影子引擎，实现从模仿到探索机器人适应策略的过渡。
3. 实验或效果：在UniManip基准上，成功率比当前最优方法提升67.90%，并计划开源代码和基准。

## 📄 摘要（原文）

> In embodied intelligence, the embodiment gap between robotic and human hands brings significant challenges for learning from human demonstrations. Although some studies have attempted to bridge this gap using reinforcement learning, they remain confined to merely reproducing human manipulation, resulting in limited task performance. In this paper, we propose UniBYD, a unified framework that uses a dynamic reinforcement learning algorithm to discover manipulation policies aligned with the robot's physical characteristics. To enable consistent modeling across diverse robotic hand morphologies, UniBYD incorporates a unified morphological representation (UMR). Building on UMR, we design a dynamic PPO with an annealed reward schedule, enabling reinforcement learning to transition from imitation of human demonstrations to explore policies adapted to diverse robotic morphologies better, thereby going beyond mere imitation of human hands. To address the frequent failures of learning human priors in the early training stage, we design a hybrid Markov-based shadow engine that enables reinforcement learning to imitate human manipulations in a fine-grained manner. To evaluate UniBYD comprehensively, we propose UniManip, the first benchmark encompassing robotic manipulation tasks spanning multiple hand morphologies. Experiments demonstrate a 67.90% improvement in success rate over the current state-of-the-art. Upon acceptance of the paper, we will release our code and benchmark at https://github.com/zhanheng-creator/UniBYD.

