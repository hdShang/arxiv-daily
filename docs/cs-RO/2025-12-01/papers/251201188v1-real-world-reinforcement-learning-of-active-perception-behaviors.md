---
layout: default
title: Real-World Reinforcement Learning of Active Perception Behaviors
---

# Real-World Reinforcement Learning of Active Perception Behaviors

**arXiv**: [2512.01188v1](https://arxiv.org/abs/2512.01188) | [PDF](https://arxiv.org/pdf/2512.01188.pdf)

**作者**: Edward S. Hu, Jie Wang, Xingfang Yuan, Fiona Luo, Muyao Li, Gaspard Lambrechts, Oleh Rybkin, Dinesh Jayaraman

---

## 💡 一句话要点

**提出AAWR方法以在部分可观测环境中高效训练机器人主动感知行为**

**关键词**: `主动感知` `部分可观测性` `强化学习` `机器人操作` `特权学习` `策略优化`

## 📋 核心要点

1. 核心问题：机器人部分可观测下标准学习技术难以生成主动感知行为
2. 方法要点：利用特权传感器训练价值函数，结合演示和粗初始化快速优化策略
3. 实验或效果：在8个任务上优于现有方法，能处理严重部分可观测性

## 📄 摘要（原文）

> A robot's instantaneous sensory observations do not always reveal task-relevant state information. Under such partial observability, optimal behavior typically involves explicitly acting to gain the missing information. Today's standard robot learning techniques struggle to produce such active perception behaviors. We propose a simple real-world robot learning recipe to efficiently train active perception policies. Our approach, asymmetric advantage weighted regression (AAWR), exploits access to "privileged" extra sensors at training time. The privileged sensors enable training high-quality privileged value functions that aid in estimating the advantage of the target policy. Bootstrapping from a small number of potentially suboptimal demonstrations and an easy-to-obtain coarse policy initialization, AAWR quickly acquires active perception behaviors and boosts task performance. In evaluations on 8 manipulation tasks on 3 robots spanning varying degrees of partial observability, AAWR synthesizes reliable active perception behaviors that outperform all prior approaches. When initialized with a "generalist" robot policy that struggles with active perception tasks, AAWR efficiently generates information-gathering behaviors that allow it to operate under severe partial observability for manipulation tasks. Website: https://penn-pal-lab.github.io/aawr/

