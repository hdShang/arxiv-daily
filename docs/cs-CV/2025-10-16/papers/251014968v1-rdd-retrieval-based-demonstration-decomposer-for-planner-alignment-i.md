---
layout: default
title: RDD: Retrieval-Based Demonstration Decomposer for Planner Alignment in Long-Horizon Tasks
---

# RDD: Retrieval-Based Demonstration Decomposer for Planner Alignment in Long-Horizon Tasks

**arXiv**: [2510.14968v1](https://arxiv.org/abs/2510.14968) | [PDF](https://arxiv.org/pdf/2510.14968.pdf)

**作者**: Mingxuan Yan, Yuping Wang, Zechun Liu, Jiachen Li

---

## 💡 一句话要点

**提出基于检索的演示分解器以对齐长视野任务中的规划器**

**关键词**: `长视野任务` `视觉语言动作框架` `演示分解` `视觉特征检索` `规划器对齐` `机器人操作`

## 📋 核心要点

1. 核心问题：VLM规划器微调依赖人工或启发式分解，子任务与低层策略训练数据不匹配，影响性能。
2. 方法要点：RDD通过视觉特征检索自动分解演示，使子任务与低层策略训练数据对齐。
3. 实验或效果：在仿真和真实任务中优于现有分解器，展现跨场景鲁棒性。

## 📄 摘要（原文）

> To tackle long-horizon tasks, recent hierarchical vision-language-action
> (VLAs) frameworks employ vision-language model (VLM)-based planners to
> decompose complex manipulation tasks into simpler sub-tasks that low-level
> visuomotor policies can easily handle. Typically, the VLM planner is finetuned
> to learn to decompose a target task. This finetuning requires target task
> demonstrations segmented into sub-tasks by either human annotation or heuristic
> rules. However, the heuristic subtasks can deviate significantly from the
> training data of the visuomotor policy, which degrades task performance. To
> address these issues, we propose a Retrieval-based Demonstration Decomposer
> (RDD) that automatically decomposes demonstrations into sub-tasks by aligning
> the visual features of the decomposed sub-task intervals with those from the
> training data of the low-level visuomotor policies. Our method outperforms the
> state-of-the-art sub-task decomposer on both simulation and real-world tasks,
> demonstrating robustness across diverse settings. Code and more results are
> available at rdd-neurips.github.io.

