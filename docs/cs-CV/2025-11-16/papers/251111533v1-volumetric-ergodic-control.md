---
layout: default
title: Volumetric Ergodic Control
---

# Volumetric Ergodic Control

**arXiv**: [2511.11533v1](https://arxiv.org/abs/2511.11533) | [PDF](https://arxiv.org/pdf/2511.11533.pdf)

**作者**: Jueun Kwon, Max M. Sun, Todd Murphey

---

## 💡 一句话要点

**提出体积遍历控制方法，优化机器人空间覆盖效率**

**关键词**: `遍历控制` `体积表示` `机器人覆盖` `实时控制` `空间优化`

## 📋 核心要点

1. 现有遍历控制将机器人建模为无体积点，忽略实际体积交互问题
2. 新方法使用体积状态表示，保持覆盖保证并支持实时控制
3. 实验显示覆盖效率提升超两倍，任务完成率100%，优于标准方法

## 📄 摘要（原文）

> Ergodic control synthesizes optimal coverage behaviors over spatial distributions for nonlinear systems. However, existing formulations model the robot as a non-volumetric point, but in practice a robot interacts with the environment through its body and sensors with physical volume. In this work, we introduce a new ergodic control formulation that optimizes spatial coverage using a volumetric state representation. Our method preserves the asymptotic coverage guarantees of ergodic control, adds minimal computational overhead for real-time control, and supports arbitrary sample-based volumetric models. We evaluate our method across search and manipulation tasks -- with multiple robot dynamics and end-effector geometries or sensor models -- and show that it improves coverage efficiency by more than a factor of two while maintaining a 100% task completion rate across all experiments, outperforming the standard ergodic control method. Finally, we demonstrate the effectiveness of our method on a robot arm performing mechanical erasing tasks.

