---
layout: default
title: SteadyDancer: Harmonized and Coherent Human Image Animation with First-Frame Preservation
---

# SteadyDancer: Harmonized and Coherent Human Image Animation with First-Frame Preservation

**arXiv**: [2511.19320v1](https://arxiv.org/abs/2511.19320) | [PDF](https://arxiv.org/pdf/2511.19320.pdf)

**作者**: Jiaming Zhang, Shengming Cao, Rui Li, Xiaotong Zhao, Yutao Cui, Xinglin Hou, Gangshan Wu, Haolan Chen, Yu Xu, Limin Wang, Kai Ma

---

## 💡 一句话要点

**提出SteadyDancer框架以解决人类图像动画中的身份漂移和运动控制问题**

**关键词**: `人类图像动画` `第一帧保留` `条件调和` `姿态调制` `分阶段训练` `时空一致性`

## 📋 核心要点

1. 核心问题：现有方法在图像到视频动画中忽视时空错位，导致身份漂移和视觉伪影
2. 方法要点：引入条件调和机制和协同姿态调制模块，确保第一帧身份保留和运动精确控制
3. 实验或效果：在保真度和运动控制上达到先进水平，且训练资源需求较低

## 📄 摘要（原文）

> Preserving first-frame identity while ensuring precise motion control is a fundamental challenge in human image animation. The Image-to-Motion Binding process of the dominant Reference-to-Video (R2V) paradigm overlooks critical spatio-temporal misalignments common in real-world applications, leading to failures such as identity drift and visual artifacts. We introduce SteadyDancer, an Image-to-Video (I2V) paradigm-based framework that achieves harmonized and coherent animation and is the first to ensure first-frame preservation robustly. Firstly, we propose a Condition-Reconciliation Mechanism to harmonize the two conflicting conditions, enabling precise control without sacrificing fidelity. Secondly, we design Synergistic Pose Modulation Modules to generate an adaptive and coherent pose representation that is highly compatible with the reference image. Finally, we employ a Staged Decoupled-Objective Training Pipeline that hierarchically optimizes the model for motion fidelity, visual quality, and temporal coherence. Experiments demonstrate that SteadyDancer achieves state-of-the-art performance in both appearance fidelity and motion control, while requiring significantly fewer training resources than comparable methods.

