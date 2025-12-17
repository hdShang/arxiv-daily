---
layout: default
title: AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning
---

# AutoTool: Dynamic Tool Selection and Integration for Agentic Reasoning

**arXiv**: [2512.13278v1](https://arxiv.org/abs/2512.13278) | [PDF](https://arxiv.org/pdf/2512.13278.pdf)

**作者**: Jiaru Zou, Ling Yang, Yunzhe Qi, Sirui Chen, Mengting Ai, Ke Shen, Jingrui He, Mengdi Wang

---

## 💡 一句话要点

**提出AutoTool框架，使LLM代理在推理轨迹中动态选择工具以增强适应性。**

**关键词**: `动态工具选择` `代理推理` `强化学习` `多任务基准` `工具集成` `泛化能力`

## 📋 核心要点

1. 现有方法假设固定工具集，限制LLM代理对新工具集的适应性。
2. AutoTool通过双阶段优化管道实现动态工具选择，包括轨迹稳定和KL正则化排名。
3. 在多个基准测试中，AutoTool以较少参数实现性能提升，并展示对未见工具的泛化能力。

## 📄 摘要（原文）

> Agentic reinforcement learning has advanced large language models (LLMs) to reason through long chain-of-thought trajectories while interleaving external tool use. Existing approaches assume a fixed inventory of tools, limiting LLM agents' adaptability to new or evolving toolsets. We present AutoTool, a framework that equips LLM agents with dynamic tool-selection capabilities throughout their reasoning trajectories. We first construct a 200k dataset with explicit tool-selection rationales across 1,000+ tools and 100+ tasks spanning mathematics, science, code generation, and multimodal reasoning. Building on this data foundation, AutoTool employs a dual-phase optimization pipeline: (i) supervised and RL-based trajectory stabilization for coherent reasoning, and (ii) KL-regularized Plackett-Luce ranking to refine consistent multi-step tool selection. Across ten diverse benchmarks, we train two base models, Qwen3-8B and Qwen2.5-VL-7B, with AutoTool. With fewer parameters, AutoTool consistently outperforms advanced LLM agents and tool-integration methods, yielding average gains of 6.4% in math & science reasoning, 4.5% in search-based QA, 7.7% in code generation, and 6.9% in multimodal understanding. In addition, AutoTool exhibits stronger generalization by dynamically leveraging unseen tools from evolving toolsets during inference.

