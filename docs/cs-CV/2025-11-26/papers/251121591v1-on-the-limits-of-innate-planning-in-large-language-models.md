---
layout: default
title: On the Limits of Innate Planning in Large Language Models
---

# On the Limits of Innate Planning in Large Language Models

**arXiv**: [2511.21591v1](https://arxiv.org/abs/2511.21591) | [PDF](https://arxiv.org/pdf/2511.21591.pdf)

**作者**: Charles Schepanowski, Charles Ling

---

## 💡 一句话要点

**评估大语言模型在8-puzzle任务中的内在规划能力，揭示其状态跟踪与启发式规划缺陷**

**关键词**: `大语言模型` `规划能力` `状态跟踪` `8-puzzle任务` `提示策略` `启发式规划`

## 📋 核心要点

1. 核心问题：大语言模型在无外部工具下的规划与状态推理能力存在显著局限
2. 方法要点：使用8-puzzle任务，测试多种提示策略与反馈机制，分析模型行为
3. 实验或效果：反馈提升部分成功率，但模型无法在验证器辅助下解决任何谜题

## 📄 摘要（原文）

> Large language models (LLMs) achieve impressive results on many benchmarks, yet their capacity for planning and stateful reasoning remains unclear. We study these abilities directly, without code execution or other tools, using the 8-puzzle: a classic task that requires state tracking and goal-directed planning while allowing precise, step-by-step evaluation. Four models are tested under common prompting conditions (Zero-Shot, Chain-of-Thought, Algorithm-of-Thought) and with tiered corrective feedback. Feedback improves success rates for some model-prompt combinations, but many successful runs are long, computationally expensive, and indirect. We then examine the models with an external move validator that provides only valid moves. Despite this level of assistance, none of the models solve any puzzles in this setting. Qualitative analysis reveals two dominant deficits across all models: (1) brittle internal state representations, leading to frequent invalid moves, and (2) weak heuristic planning, with models entering loops or selecting actions that do not reduce the distance to the goal state. These findings indicate that, in the absence of external tools such as code interpreters, current LLMs have substantial limitations in planning and that further progress may require mechanisms for maintaining explicit state and performing structured search.

