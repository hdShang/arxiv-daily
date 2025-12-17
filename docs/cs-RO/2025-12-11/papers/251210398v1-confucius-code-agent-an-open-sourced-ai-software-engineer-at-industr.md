---
layout: default
title: Confucius Code Agent: An Open-sourced AI Software Engineer at Industrial Scale
---

# Confucius Code Agent: An Open-sourced AI Software Engineer at Industrial Scale

**arXiv**: [2512.10398v1](https://arxiv.org/abs/2512.10398) | [PDF](https://arxiv.org/pdf/2512.10398.pdf)

**作者**: Zhaodong Wang, Zhenting Qi, Sherman Wong, Nathan Hu, Samuel Lin, Jun Ge, Erwin Gao, Yining Yang, Ben Maurer, Wenlin Chen, David Recordon, Yilun Du, Minlan Yu, Ying Zhang

---

## 💡 一句话要点

**提出Confucius Code Agent开源AI软件工程师，解决工业级代码生成任务中的规模化挑战**

**关键词**: `代码智能体` `工业级软件工程` `长上下文推理` `持续学习` `工具链协调` `开源AI平台`

## 📋 核心要点

1. 现有开源代码智能体在工业级工作负载下表现不足，而专有智能体可扩展性和可控性有限
2. 基于Confucius SDK构建，采用分层工作记忆、持久笔记系统和模块化工具扩展机制
3. 在SWE-Bench-Pro上达到54.3%的Resolve@1性能，显著超越先前代码智能体

## 📄 摘要（原文）

> Real-world AI software engineering demands coding agents that can reason over massive repositories, maintain durable memory across and within long sessions, and robustly coordinate complex toolchains at test time. Existing open-source coding agents provide transparency but frequently fall short when pushed to these industrial-scale workloads, while proprietary coding agents offer strong practical performance but limited extensibility, interpretability, and controllability. We present the Confucius Code Agent (CCA), an open-sourced AI software engineer that can operate at an industrial scale. CCA is built atop the Confucius SDK, an open-sourced agent development platform designed around three complementary perspectives: Agent Experience (AX), User Experience (UX), and Developer Experience (DX). The SDK introduces a unified orchestrator with hierarchical working memory for long-context reasoning, a persistent note-taking system for cross-session continual learning, and a modular extension module for robust tool use. Moreover, a meta-agent automates the synthesis, evaluation, and refinement of agent configurations through a build-test-improve loop, enabling rapid agent development on new tasks, environments, and tool stacks. Instantiated on Confucius SDK with these mechanisms, CCA delivers strong performance on real-world software engineering tasks. On SWE-Bench-Pro, CCA achieves a state-of-the-art Resolve@1 performance of 54.3%, substantially improving over prior coding agents. Together, the Confucius SDK and CCA provide a transparent, extensible, and reproducible foundation for AI agents, bridge gaps between research prototypes and production-grade systems, and support agent development and deployment at industrial scale.

