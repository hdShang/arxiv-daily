---
layout: default
title: SIT-Graph: State Integrated Tool Graph for Multi-Turn Agents
---

# SIT-Graph: State Integrated Tool Graph for Multi-Turn Agents

**arXiv**: [2512.07287v1](https://arxiv.org/abs/2512.07287) | [PDF](https://arxiv.org/pdf/2512.07287.pdf)

**作者**: Sijia Li, Yuchen Huang, Zifan Liu, Zijian Li, Jingjing fu, Lei Song, Jiang Bian, Jun Zhang, Rui Wang

---

## 💡 一句话要点

**提出状态集成工具图以增强多轮工具使用，通过利用部分重叠经验平衡情景回忆与程序执行。**

**关键词**: `多轮工具使用` `状态集成工具图` `经验复用` `情景记忆` `程序记忆` `工具依赖`

## 📋 核心要点

1. 核心问题：多轮工具使用中意图渐进澄清和环境动态变化，现有方法难以适应状态和信息演化。
2. 方法要点：构建工具图并增强边上的紧凑状态摘要，实现基于情景回忆和工具依赖的决策平衡。
3. 实验或效果：在多个状态多轮工具使用基准上优于强基线，提升工具选择和经验迁移效果。

## 📄 摘要（原文）

> Despite impressive advances in agent systems, multi-turn tool-use scenarios remain challenging. It is mainly because intent is clarified progressively and the environment evolves with each tool call. While reusing past experience is natural, current LLM agents either treat entire trajectories or pre-defined subtasks as indivisible units, or solely exploit tool-to-tool dependencies, hindering adaptation as states and information evolve across turns. In this paper, we propose a State Integrated Tool Graph (SIT-Graph), which enhances multi-turn tool use by exploiting partially overlapping experience. Inspired by human decision-making that integrates episodic and procedural memory, SIT-Graph captures both compact state representations (episodic-like fragments) and tool-to-tool dependencies (procedural-like routines) from historical trajectories. Specifically, we first build a tool graph from accumulated tool-use sequences, and then augment each edge with a compact state summary of the dialog and tool history that may shape the next action. At inference time, SIT-Graph enables a human-like balance between episodic recall and procedural execution: when the next decision requires recalling prior context, the agent retrieves the state summaries stored on relevant edges and uses them to guide its next action; when the step is routine, it follows high-confidence tool dependencies without explicit recall. Experiments across multiple stateful multi-turn tool-use benchmarks show that SIT-Graph consistently outperforms strong memory- and graph-based baselines, delivering more robust tool selection and more effective experience transfer.

