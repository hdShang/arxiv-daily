---
layout: default
title: High-Performance Dual-Arm Task and Motion Planning for Tabletop Rearrangement
---

# High-Performance Dual-Arm Task and Motion Planning for Tabletop Rearrangement

**arXiv**: [2512.08206v1](https://arxiv.org/abs/2512.08206) | [PDF](https://arxiv.org/pdf/2512.08206.pdf)

**作者**: Duo Zhang, Junshan Huang, Jingjin Yu

---

## 💡 一句话要点

**提出SDAR框架以解决双臂协同桌面重排任务中的强纠缠对象规划问题**

**关键词**: `任务与运动规划` `双臂机器人` `桌面重排` `同步规划` `GPU加速运动规划`

## 📋 核心要点

1. 核心问题：双臂机器人在桌面重排中处理起始与目标配置强纠缠对象的任务与运动规划挑战
2. 方法要点：SDAR结合依赖驱动任务规划与同步双臂运动规划，通过分解全局依赖图优化任务计划
3. 实验或效果：在复杂非单调长视距任务中实现100%成功率，解决方案质量远超先前最优方法

## 📄 摘要（原文）

> We propose Synchronous Dual-Arm Rearrange- ment Planner (SDAR), a task and motion planning (TAMP) framework for tabletop rearrangement, where two robot arms equipped with 2-finger grippers must work together in close proximity to rearrange objects whose start and goal config- urations are strongly entangled. To tackle such challenges, SDAR tightly knit together its dependency-driven task planner (SDAR-T) and synchronous dual-arm motion planner (SDAR- M), to intelligently sift through a large number of possible task and motion plans. Specifically, SDAR-T applies a simple yet effective strategy to decompose the global object dependency graph induced by the rearrangement task, to produce more optimal dual-arm task plans than solutions derived from optimal task plans for a single arm. Leveraging state-of-the-art GPU SIMD-based motion planning tools, SDAR-M employs a layered motion planning strategy to sift through many task plans for the best synchronous dual-arm motion plan while ensuring high levels of success rate. Comprehensive evaluation demonstrates that SDAR delivers a 100% success rate in solving complex, non-monotone, long-horizon tabletop rearrangement tasks with solution quality far exceeding the previous state- of-the-art. Experiments on two UR-5e arms further confirm SDAR directly and reliably transfers to robot hardware.

