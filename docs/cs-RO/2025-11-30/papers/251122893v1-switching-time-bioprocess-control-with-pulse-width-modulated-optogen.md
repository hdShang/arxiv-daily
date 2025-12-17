---
layout: default
title: Switching-time bioprocess control with pulse-width-modulated optogenetics
---

# Switching-time bioprocess control with pulse-width-modulated optogenetics

**arXiv**: [2511.22893v1](https://arxiv.org/abs/2511.22893) | [PDF](https://arxiv.org/pdf/2511.22893.pdf)

**作者**: Sebastián Espinel-Ríos

---

## 💡 一句话要点

**提出基于强化学习的占空比参数化方法，以解决脉冲宽度调制光遗传学中的切换时间最优控制问题。**

**关键词**: `光遗传学` `脉冲宽度调制` `切换时间控制` `强化学习` `占空比参数化` `生物过程控制`

## 📋 核心要点

1. 核心问题：光强度驱动控制在高剂量响应关系下难以精细调节基因表达，导致可调性受限。
2. 方法要点：采用脉冲宽度调制平滑平均响应，并通过占空比连续变量参数化控制动作，避免混合整数规划的计算复杂性。
3. 实验或效果：未知。

## 📄 摘要（原文）

> Biotechnology can benefit from dynamic control to improve production efficiency. In this context, optogenetics enables modulation of gene expression using light as an external input, allowing fine-tuning of protein levels to unlock dynamic metabolic control and regulation of cell growth. Optogenetic systems can be actuated by light intensity. However, relying solely on intensity-driven control (i.e., signal amplitude) may fail to properly tune optogenetic bioprocesses when the dose-response relationship (i.e., light intensity versus gene-expression strength) is steep. In these cases, tunability is effectively constrained to either fully active or fully repressed gene expression, with little intermediate regulation. Pulse-width modulation, a concept widely used in electronics, can alleviate this issue by alternating between fully ON and OFF light intensity within forcing periods, thereby smoothing the average response and enhancing process controllability. Naturally, optimizing pulse-width-modulated optogenetics entails a switching-time optimal control problem with a binary input over many forcing periods. While this can be formulated as a mixed-integer program on a refined time grid, the number of decision variables can grow rapidly with increasing time-grid resolution and number of forcing periods, compromising tractability. Here, we propose an alternative solution based on reinforcement learning. We parametrize control actions via the duty cycle, a continuous variable that encodes the ON-to-OFF switching time within each forcing period, thereby respecting the intrinsic binary nature of the light intensity.

