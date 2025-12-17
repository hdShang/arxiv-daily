---
layout: default
title: Vision to Geometry: 3D Spatial Memory for Sequential Embodied MLLM Reasoning and Exploration
---

# Vision to Geometry: 3D Spatial Memory for Sequential Embodied MLLM Reasoning and Exploration

**arXiv**: [2512.02458v1](https://arxiv.org/abs/2512.02458) | [PDF](https://arxiv.org/pdf/2512.02458.pdf)

**作者**: Zhongyi Cai, Yi Du, Chen Wang, Yu Kong

---

## 💡 一句话要点

**提出3DSPMR方法，利用3D空间记忆增强MLLM在顺序具身任务中的推理与探索能力。**

**关键词**: `顺序具身任务` `3D空间记忆` `多模态大语言模型` `具身问答` `具身多模态导航` `几何信息集成`

## 📋 核心要点

1. 研究顺序具身任务中空间知识复用的核心挑战，如搜索不存在物体导致子任务不可行。
2. 提出3DSPMR方法，整合关系、视觉和几何线索构建3D空间记忆以增强MLLM。
3. 在SEER-Bench基准上验证，3DSPMR在顺序EQA和EMN任务中性能显著提升。

## 📄 摘要（原文）

> Existing research on indoor embodied tasks typically requires agents to actively explore unknown environments and reason about the scene to achieve a specific goal. However, when deployed in real life, agents often face sequential tasks, where each new sub-task follows the completion of the previous one, and certain sub-tasks may be infeasible, such as searching for a non-existent object. Compared with the single-task setting, the core challenge lies in reusing spatial knowledge accumulated from previous explorations to support subsequent reasoning and exploration. In this work, we investigate this underexplored yet practically significant embodied AI challenge. To evaluate this challenge, we introduce SEER-Bench, a new Sequential Embodied Exploration and Reasoning Benchmark encompassing encompassing two classic embodied tasks: Embodied Question Answering (EQA) and Embodied Multi-modal Navigation (EMN). Building on SEER-Bench, we propose 3DSPMR, a 3D SPatial Memory Reasoning approach that exploits relational, visual, and geometric cues from explored regions to augment Multi-Modal Large Language Models (MLLMs) for reasoning and exploration in sequential embodied tasks. To the best of our knowledge, this is the first work to explicitly incorporate geometric information into MLLM-based spatial understanding and reasoning. Extensive experiments verify that 3DSPMR achieves substantial performance gains on both sequential EQA and EMN tasks.

