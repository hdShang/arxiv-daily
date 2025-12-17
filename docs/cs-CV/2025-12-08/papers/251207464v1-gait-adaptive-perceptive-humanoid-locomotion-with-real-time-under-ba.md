---
layout: default
title: Gait-Adaptive Perceptive Humanoid Locomotion with Real-Time Under-Base Terrain Reconstruction
---

# Gait-Adaptive Perceptive Humanoid Locomotion with Real-Time Under-Base Terrain Reconstruction

**arXiv**: [2512.07464v1](https://arxiv.org/abs/2512.07464) | [PDF](https://arxiv.org/pdf/2512.07464.pdf)

**作者**: Haolin Song, Hongbo Zhu, Tao Yu, Yan Liu, Mingqi Yuan, Wengang Zhou, Hua Chen, Houqiang Li

---

## 💡 一句话要点

**提出感知性人形机器人步态自适应框架，以解决复杂地形下可靠行走的挑战。**

**关键词**: `人形机器人行走` `地形感知` `强化学习控制` `实时重建` `步态自适应` `全身控制`

## 📋 核心要点

1. 核心问题：人形机器人在复杂地形（如长楼梯）行走时，感知有限、步态时序不适应易导致失衡。
2. 方法要点：集成深度相机实时重建地形高度图，通过统一强化学习策略联合调节步态时序和全身姿态。
3. 实验或效果：在31自由度人形机器人上验证，实现楼梯上下行和跨越46厘米间隙的稳健行走。

## 📄 摘要（原文）

> For full-size humanoid robots, even with recent advances in reinforcement learning-based control, achieving reliable locomotion on complex terrains, such as long staircases, remains challenging. In such settings, limited perception, ambiguous terrain cues, and insufficient adaptation of gait timing can cause even a single misplaced or mistimed step to result in rapid loss of balance. We introduce a perceptive locomotion framework that merges terrain sensing, gait regulation, and whole-body control into a single reinforcement learning policy. A downward-facing depth camera mounted under the base observes the support region around the feet, and a compact U-Net reconstructs a dense egocentric height map from each frame in real time, operating at the same frequency as the control loop. The perceptual height map, together with proprioceptive observations, is processed by a unified policy that produces joint commands and a global stepping-phase signal, allowing gait timing and whole-body posture to be adapted jointly to the commanded motion and local terrain geometry. We further adopt a single-stage successive teacher-student training scheme for efficient policy learning and knowledge transfer. Experiments conducted on a 31-DoF, 1.65 m humanoid robot demonstrate robust locomotion in both simulation and real-world settings, including forward and backward stair ascent and descent, as well as crossing a 46 cm gap. Project Page:https://ga-phl.github.io/

