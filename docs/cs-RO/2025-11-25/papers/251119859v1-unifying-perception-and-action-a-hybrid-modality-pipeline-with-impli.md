---
layout: default
title: Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation
---

# Unifying Perception and Action: A Hybrid-Modality Pipeline with Implicit Visual Chain-of-Thought for Robotic Action Generation

**arXiv**: [2511.19859v1](https://arxiv.org/abs/2511.19859) | [PDF](https://arxiv.org/pdf/2511.19859.pdf)

**作者**: Xiangkai Ma, Lekai Xing, Han Zhang, Wenzhong Li, Sanglu Lu

---

## 💡 一句话要点

**提出VITA框架以解决视觉与动作模态差距及训练不稳定问题**

**关键词**: `视觉语言动作模型` `隐式视觉思维链` `机器人动作生成` `多模态学习` `轨迹对齐`

## 📋 核心要点

1. 核心问题：视觉观察与低级动作间存在模态差距，视觉预测与动作生成目标冲突导致训练不稳定
2. 方法要点：学习共享离散潜空间，通过隐式视觉思维链联合解码未来帧预测和机器人动作
3. 实验或效果：在CALVIN等基准上提升9.6%-14.5%，真实世界任务平均成功率80.5%

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models built upon Chain-of-Thought (CoT) have achieved remarkable success in advancing general-purpose robotic agents, owing to its significant perceptual comprehension. Recently, since text-only CoT struggles to adequately capture scene details in complex spatial environments, a highly promising strategy involves leveraging visual priors to guide robotic action generation. Nevertheless, these strategies face two inherent challenges: (i) a modality gap between visual observations and low-level actions, and (ii) unstable training due to competing objectives between visual prediction and action generation. To address these challenges, we propose a Vision-Integrated Trajectory Alignment (VITA) framework that learns a shared discrete latent space for vision and action, enabling joint modeling of perception and motor control. VITA introduces a implicit visual CoT: autoregressively generated tokens is simultaneously decoded into future frames predictions and robot actions, thereby internalizing visual dynamics as an inductive bias for motion planning. Extensive experiments on simulated and real-world environments demonstrate state-of-the-art performance. VITA improves 14.5\%, 9.6\% and 12.1\% over existing baselines on CALVIN, LIBERO and SimplerEnv. Furthermore, VITA attains an average success rate of 80.5\% across six real-world tasks, demonstrating its potential as a generalist robotic manipulation model.

