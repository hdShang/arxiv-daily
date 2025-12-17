---
layout: default
title: Predictive Safety Shield for Dyna-Q Reinforcement Learning
---

# Predictive Safety Shield for Dyna-Q Reinforcement Learning

**arXiv**: [2511.21531v1](https://arxiv.org/abs/2511.21531) | [PDF](https://arxiv.org/pdf/2511.21531.pdf)

**作者**: Jin Pin, Krasowski Hanna, Vanneaux Elena

---

## 💡 一句话要点

**提出预测性安全护盾以提升离散空间模型强化学习的安全性与性能**

**关键词**: `强化学习安全` `模型预测控制` `离散空间强化学习` `安全护盾` `Q函数更新` `分布偏移鲁棒性`

## 📋 核心要点

1. 核心问题：强化学习在现实任务中难以获得硬安全保证，现有安全护盾忽略不同安全动作的未来性能影响。
2. 方法要点：基于环境模型的安全模拟进行局部Q函数更新，实现预测性安全护盾。
3. 实验或效果：在网格世界环境中，短预测范围即可识别最优路径，且对分布偏移具有鲁棒性。

## 📄 摘要（原文）

> Obtaining safety guarantees for reinforcement learning is a major challenge to achieve applicability for real-world tasks. Safety shields extend standard reinforcement learning and achieve hard safety guarantees. However, existing safety shields commonly use random sampling of safe actions or a fixed fallback controller, therefore disregarding future performance implications of different safe actions. In this work, we propose a predictive safety shield for model-based reinforcement learning agents in discrete space. Our safety shield updates the Q-function locally based on safe predictions, which originate from a safe simulation of the environment model. This shielding approach improves performance while maintaining hard safety guarantees. Our experiments on gridworld environments demonstrate that even short prediction horizons can be sufficient to identify the optimal path. We observe that our approach is robust to distribution shifts, e.g., between simulation and reality, without requiring additional training.

