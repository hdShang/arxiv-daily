---
layout: default
title: Accelerating Reinforcement Learning via Error-Related Human Brain Signals
---

# Accelerating Reinforcement Learning via Error-Related Human Brain Signals

**arXiv**: [2511.18878v1](https://arxiv.org/abs/2511.18878) | [PDF](https://arxiv.org/pdf/2511.18878.pdf)

**作者**: Suzie Kim, Hye-Bin Shin, Hyo-Jeong Jang

---

## 💡 一句话要点

**提出基于脑电误差信号的强化学习框架，加速高维机器人操作任务学习**

**关键词**: `强化学习` `脑电信号` `机器人操作` `奖励塑形` `误差相关电位` `人机交互`

## 📋 核心要点

1. 核心问题：高维机器人操作任务中强化学习效率低，脑电反馈应用局限于导航任务
2. 方法要点：解码脑电误差电位，集成到奖励塑形中，并系统评估反馈权重
3. 实验或效果：在7自由度机械臂环境中，神经反馈加速学习，成功率有时超过稀疏奖励基线

## 📄 摘要（原文）

> In this work, we investigate how implicit neural feed back can accelerate reinforcement learning in complex robotic manipulation settings. While prior electroencephalogram (EEG) guided reinforcement learning studies have primarily focused on navigation or low-dimensional locomotion tasks, we aim to understand whether such neural evaluative signals can improve policy learning in high-dimensional manipulation tasks involving obstacles and precise end-effector control. We integrate error related potentials decoded from offline-trained EEG classifiers into reward shaping and systematically evaluate the impact of human-feedback weighting. Experiments on a 7-DoF manipulator in an obstacle-rich reaching environment show that neural feedback accelerates reinforcement learning and, depending on the human-feedback weighting, can yield task success rates that at times exceed those of sparse-reward baselines. Moreover, when applying the best-performing feedback weighting across all sub jects, we observe consistent acceleration of reinforcement learning relative to the sparse-reward setting. Furthermore, leave-one subject-out evaluations confirm that the proposed framework remains robust despite the intrinsic inter-individual variability in EEG decodability. Our findings demonstrate that EEG-based reinforcement learning can scale beyond locomotion tasks and provide a viable pathway for human-aligned manipulation skill acquisition.

