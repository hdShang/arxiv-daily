---
layout: default
title: SUM-AgriVLN: Spatial Understanding Memory for Agricultural Vision-and-Language Navigation
---

# SUM-AgriVLN: Spatial Understanding Memory for Agricultural Vision-and-Language Navigation

**arXiv**: [2510.14357v1](https://arxiv.org/abs/2510.14357) | [PDF](https://arxiv.org/pdf/2510.14357.pdf)

**作者**: Xiaobei Zhao, Xingqi Lyu, Xiang Li

---

## 💡 一句话要点

**提出空间理解记忆方法以提升农业视觉语言导航性能**

**关键词**: `农业机器人` `视觉语言导航` `空间记忆` `3D重建` `A2A基准`

## 📋 核心要点

1. 核心问题：农业导航中重复指令被独立处理，缺乏空间上下文利用。
2. 方法要点：通过3D重建和表示构建空间记忆模块，增强导航理解。
3. 实验效果：在A2A基准上，成功率从0.47提升至0.54，导航误差略增。

## 📄 摘要（原文）

> Agricultural robots are emerging as powerful assistants across a wide range
> of agricultural tasks, nevertheless, still heavily rely on manual operation or
> fixed rail systems for movement. The AgriVLN method and the A2A benchmark
> pioneeringly extend Vision-and-Language Navigation (VLN) to the agricultural
> domain, enabling robots to navigate to the target positions following the
> natural language instructions. In practical agricultural scenarios, navigation
> instructions often repeatedly occur, yet AgriVLN treat each instruction as an
> independent episode, overlooking the potential of past experiences to provide
> spatial context for subsequent ones. To bridge this gap, we propose the method
> of Spatial Understanding Memory for Agricultural Vision-and-Language Navigation
> (SUM-AgriVLN), in which the SUM module employs spatial understanding and save
> spatial memory through 3D reconstruction and representation. When evaluated on
> the A2A benchmark, our SUM-AgriVLN effectively improves Success Rate from 0.47
> to 0.54 with slight sacrifice on Navigation Error from 2.91m to 2.93m,
> demonstrating the state-of-the-art performance in the agricultural domain.
> Code: https://github.com/AlexTraveling/SUM-AgriVLN.

