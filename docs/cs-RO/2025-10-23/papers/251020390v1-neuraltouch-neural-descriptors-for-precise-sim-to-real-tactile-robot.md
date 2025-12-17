---
layout: default
title: NeuralTouch: Neural Descriptors for Precise Sim-to-Real Tactile Robot Control
---

# NeuralTouch: Neural Descriptors for Precise Sim-to-Real Tactile Robot Control

**arXiv**: [2510.20390v1](https://arxiv.org/abs/2510.20390) | [PDF](https://arxiv.org/pdf/2510.20390.pdf)

**作者**: Yijiong Lin, Bowen Deng, Chenghua Lu, Max Yang, Efi Psomopoulou, Nathan F. Lepora

---

## 💡 一句话要点

**提出NeuralTouch框架，集成视觉与触觉感知以提升机器人抓取精度**

**关键词**: `机器人抓取` `多模态感知` `强化学习` `触觉反馈` `零样本转移`

## 📋 核心要点

1. 核心问题：视觉方法NDF因校准误差和点云不完整导致抓取姿态不准确
2. 方法要点：结合NDF和触觉反馈，通过强化学习策略优化抓取过程
3. 实验或效果：在模拟和真实任务中实现零样本转移，显著提高准确性和鲁棒性

## 📄 摘要（原文）

> Grasping accuracy is a critical prerequisite for precise object manipulation,
> often requiring careful alignment between the robot hand and object. Neural
> Descriptor Fields (NDF) offer a promising vision-based method to generate
> grasping poses that generalize across object categories. However, NDF alone can
> produce inaccurate poses due to imperfect camera calibration, incomplete point
> clouds, and object variability. Meanwhile, tactile sensing enables more precise
> contact, but existing approaches typically learn policies limited to simple,
> predefined contact geometries. In this work, we introduce NeuralTouch, a
> multimodal framework that integrates NDF and tactile sensing to enable
> accurate, generalizable grasping through gentle physical interaction. Our
> approach leverages NDF to implicitly represent the target contact geometry,
> from which a deep reinforcement learning (RL) policy is trained to refine the
> grasp using tactile feedback. This policy is conditioned on the neural
> descriptors and does not require explicit specification of contact types. We
> validate NeuralTouch through ablation studies in simulation and zero-shot
> transfer to real-world manipulation tasks--such as peg-out-in-hole and bottle
> lid opening--without additional fine-tuning. Results show that NeuralTouch
> significantly improves grasping accuracy and robustness over baseline methods,
> offering a general framework for precise, contact-rich robotic manipulation.

