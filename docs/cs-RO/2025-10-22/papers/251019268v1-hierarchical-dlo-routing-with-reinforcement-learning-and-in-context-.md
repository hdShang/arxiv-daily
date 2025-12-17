---
layout: default
title: Hierarchical DLO Routing with Reinforcement Learning and In-Context Vision-language Models
---

# Hierarchical DLO Routing with Reinforcement Learning and In-Context Vision-language Models

**arXiv**: [2510.19268v1](https://arxiv.org/abs/2510.19268) | [PDF](https://arxiv.org/pdf/2510.19268.pdf)

**作者**: Mingen Li, Houjian Yu, Yixuan Huang, Youngjin Hong, Changhyun Choi

---

## 💡 一句话要点

**提出分层框架结合强化学习和视觉语言模型，以解决可变形线性物体的长时程路由任务。**

**关键词**: `可变形线性物体路由` `分层框架` `强化学习` `视觉语言模型` `长时程规划` `失败恢复机制`

## 📋 核心要点

1. 核心问题：可变形线性物体在工业装配中需长时程规划和可靠技能执行，适应非线性动态。
2. 方法要点：利用视觉语言模型进行上下文推理生成计划，强化学习训练低层技能执行。
3. 实验或效果：在长时程路由场景中成功率92.5%，优于基线方法近50%。

## 📄 摘要（原文）

> Long-horizon routing tasks of deformable linear objects (DLOs), such as
> cables and ropes, are common in industrial assembly lines and everyday life.
> These tasks are particularly challenging because they require robots to
> manipulate DLO with long-horizon planning and reliable skill execution.
> Successfully completing such tasks demands adapting to their nonlinear
> dynamics, decomposing abstract routing goals, and generating multi-step plans
> composed of multiple skills, all of which require accurate high-level reasoning
> during execution. In this paper, we propose a fully autonomous hierarchical
> framework for solving challenging DLO routing tasks. Given an implicit or
> explicit routing goal expressed in language, our framework leverages
> vision-language models~(VLMs) for in-context high-level reasoning to synthesize
> feasible plans, which are then executed by low-level skills trained via
> reinforcement learning. To improve robustness in long horizons, we further
> introduce a failure recovery mechanism that reorients the DLO into
> insertion-feasible states. Our approach generalizes to diverse scenes involving
> object attributes, spatial descriptions, as well as implicit language commands.
> It outperforms the next best baseline method by nearly 50% and achieves an
> overall success rate of 92.5% across long-horizon routing scenarios.

