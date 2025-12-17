---
layout: default
title: PerspAct: Enhancing LLM Situated Collaboration Skills through Perspective Taking and Active Vision
---

# PerspAct: Enhancing LLM Situated Collaboration Skills through Perspective Taking and Active Vision

**arXiv**: [2511.08098v1](https://arxiv.org/abs/2511.08098) | [PDF](https://arxiv.org/pdf/2511.08098.pdf)

**作者**: Sabrina Patania, Luca Annese, Anita Pellegrini, Silvia Serino, Anna Lambiase, Luca Pallonetto, Silvia Rossi, Simone Colombani, Tom Foulsham, Azzurra Ruggeri, Dimitri Ognibene

---

## 💡 一句话要点

**提出PerspAct方法，通过视角采择和主动视觉增强LLM在协作系统中的能力**

**关键词**: `视角采择` `主动视觉` `多智能体系统` `ReAct框架` `LLM协作`

## 📋 核心要点

1. 核心问题：LLM在多智能体交互中缺乏视角采择能力，导致推理主观视角困难
2. 方法要点：扩展ReAct框架，引入主动视觉探索和多样化视角提示策略
3. 实验或效果：在七种复杂场景中，显著提升模型解释准确性和协作有效性

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) and multimodal foundation models have significantly broadened their application in robotics and collaborative systems. However, effective multi-agent interaction necessitates robust perspective-taking capabilities, enabling models to interpret both physical and epistemic viewpoints. Current training paradigms often neglect these interactive contexts, resulting in challenges when models must reason about the subjectivity of individual perspectives or navigate environments with multiple observers. This study evaluates whether explicitly incorporating diverse points of view using the ReAct framework, an approach that integrates reasoning and acting, can enhance an LLM's ability to understand and ground the demands of other agents. We extend the classic Director task by introducing active visual exploration across a suite of seven scenarios of increasing perspective-taking complexity. These scenarios are designed to challenge the agent's capacity to resolve referential ambiguity based on visual access and interaction, under varying state representations and prompting strategies, including ReAct-style reasoning. Our results demonstrate that explicit perspective cues, combined with active exploration strategies, significantly improve the model's interpretative accuracy and collaborative effectiveness. These findings highlight the potential of integrating active perception with perspective-taking mechanisms in advancing LLMs' application in robotics and multi-agent systems, setting a foundation for future research into adaptive and context-aware AI systems.

