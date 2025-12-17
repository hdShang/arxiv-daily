---
layout: default
title: Process-Centric Analysis of Agentic Software Systems
---

# Process-Centric Analysis of Agentic Software Systems

**arXiv**: [2512.02393v1](https://arxiv.org/abs/2512.02393) | [PDF](https://arxiv.org/pdf/2512.02393.pdf)

**作者**: Shuyang Liu, Yang Chen, Rahul Krishna, Saurabh Sinha, Jatin Ganhotra, Reyhan Jabbarvand

---

## 💡 一句话要点

**提出Graphectory以系统分析智能体软件系统的过程质量，独立于最终成功**

**关键词**: `智能体软件系统` `过程分析` `Graphectory` `大型语言模型` `软件工程代理` `轨迹分析`

## 📋 核心要点

1. 核心问题：现有评估聚焦最终结果，忽视智能体推理、规划和策略变化的详细过程分析。
2. 方法要点：引入Graphectory编码智能体系统的时空和语义关系，支持过程中心度量和分析。
3. 实验或效果：分析4000条轨迹，揭示提示、LLM和问题难度如何影响策略效率和复杂性。

## 📄 摘要（原文）

> Agentic systems are modern software systems: they consist of orchestrated modules, expose interfaces, and are deployed in software pipelines. Unlike conventional programs, their execution (i.e., trajectories) is inherently stochastic and adaptive to the problem they are solving. Evaluation of such systems is often outcome-centric, judging their performance based on success or failure at the final step. This narrow focus overlooks detailed insights about such systems, failing to explain how agents reason, plan, act, or change their strategies over time. Inspired by the structured representation of conventional software systems as graphs, we introduce Graphectory to systematically encode the temporal and semantic relations in such software systems. Graphectory facilitates the design of process-centric metrics and analyses to assess the quality of agentic workflows independent of final success.
>   Using Graphectory, we analyze 4000 trajectories of two dominant agentic programming workflows, namely SWE-agent and OpenHands, with a combination of four backbone Large Language Models (LLMs), attempting to resolve SWE-bench Verified issues. Our fully automated analyses reveal that: (1) agents using richer prompts or stronger LLMs exhibit more complex Graphectory, reflecting deeper exploration, broader context gathering, and more thorough validation before patch submission; (2) agents' problem-solving strategies vary with both problem difficulty and the underlying LLM -- for resolved issues, the strategies often follow coherent localization-patching-validation steps, while unresolved ones exhibit chaotic, repetitive, or backtracking behaviors; (3) even when successful, agentic programming systems often display inefficient processes, leading to unnecessarily prolonged trajectories.

