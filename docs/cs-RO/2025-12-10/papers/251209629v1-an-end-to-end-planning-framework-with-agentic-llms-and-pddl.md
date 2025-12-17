---
layout: default
title: An End-to-end Planning Framework with Agentic LLMs and PDDL
---

# An End-to-end Planning Framework with Agentic LLMs and PDDL

**arXiv**: [2512.09629v1](https://arxiv.org/abs/2512.09629) | [PDF](https://arxiv.org/pdf/2512.09629.pdf)

**作者**: Emanuele La Malfa, Ping Zhu, Samuele Marro, Sara Bernardini, Michael Wooldridge

---

## 💡 一句话要点

**提出基于大语言模型与PDDL的端到端规划框架，以自动化处理自然语言规范并生成可执行计划。**

**关键词**: `端到端规划` `大语言模型` `PDDL` `自然语言处理` `自动化验证` `规划引擎集成`

## 📋 核心要点

1. 核心问题：自然语言规范存在模糊性和矛盾，传统规划需人工干预，大语言模型在复杂规划任务中表现不佳。
2. 方法要点：使用编排器和代理模块迭代精炼PDDL模型，集成外部规划引擎，无需人工干预。
3. 实验或效果：在Google NaturalPlan、PlanBench等基准测试中验证灵活性，支持多种PDDL引擎如Fast Downward。

## 📄 摘要（原文）

> We present an end-to-end framework for planning supported by verifiers. An orchestrator receives a human specification written in natural language and converts it into a PDDL (Planning Domain Definition Language) model, where the domain and problem are iteratively refined by sub-modules (agents) to address common planning requirements, such as time constraints and optimality, as well as ambiguities and contradictions that may exist in the human specification. The validated domain and problem are then passed to an external planning engine to generate a plan. The orchestrator and agents are powered by Large Language Models (LLMs) and require no human intervention at any stage of the process. Finally, a module translates the final plan back into natural language to improve human readability while maintaining the correctness of each step. We demonstrate the flexibility and effectiveness of our framework across various domains and tasks, including the Google NaturalPlan benchmark and PlanBench, as well as planning problems like Blocksworld and the Tower of Hanoi (where LLMs are known to struggle even with small instances). Our framework can be integrated with any PDDL planning engine and validator (such as Fast Downward, LPG, POPF, VAL, and uVAL, which we have tested) and represents a significant step toward end-to-end planning aided by LLMs.

