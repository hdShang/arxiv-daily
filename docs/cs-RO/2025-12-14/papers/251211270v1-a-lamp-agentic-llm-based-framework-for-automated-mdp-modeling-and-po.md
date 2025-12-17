---
layout: default
title: A-LAMP: Agentic LLM-Based Framework for Automated MDP Modeling and Policy Generation
---

# A-LAMP: Agentic LLM-Based Framework for Automated MDP Modeling and Policy Generation

**arXiv**: [2512.11270v1](https://arxiv.org/abs/2512.11270) | [PDF](https://arxiv.org/pdf/2512.11270.pdf)

**作者**: Hong Je-Gal, Chan-Bin Yi, Hyun-Suk Lee

---

## 💡 一句话要点

**提出A-LAMP框架，基于智能体化大语言模型自动将自然语言任务描述转化为MDP和训练策略。**

**关键词**: `强化学习自动化` `MDP建模` `智能体化LLM` `策略生成` `语义对齐` `环境生成`

## 📋 核心要点

1. 核心问题：强化学习应用中，从非正式描述到MDP建模、环境实现和策略训练的自动化过程易受建模错误、代码脆弱和目标错位阻碍。
2. 方法要点：采用智能体化LLM框架，将建模、编码和训练分解为可验证阶段，确保语义对齐，自动生成MDP和训练策略。
3. 实验或效果：在经典控制和自定义RL领域，A-LAMP比单一先进LLM模型表现更优，轻量版接近大模型性能，案例研究确认其正确性和可靠性。

## 📄 摘要（原文）

> Applying reinforcement learning (RL) to real-world tasks requires converting informal descriptions into a formal Markov decision process (MDP), implementing an executable environment, and training a policy agent. Automating this process is challenging due to modeling errors, fragile code, and misaligned objectives, which often impede policy training. We introduce an agentic large language model (LLM)-based framework for automated MDP modeling and policy generation (A-LAMP), that automatically translates free-form natural language task descriptions into an MDP formulation and trained policy. The framework decomposes modeling, coding, and training into verifiable stages, ensuring semantic alignment throughout the pipeline. Across both classic control and custom RL domains, A-LAMP consistently achieves higher policy generation capability than a single state-of-the-art LLM model. Notably, even its lightweight variant, which is built on smaller language models, approaches the performance of much larger models. Failure analysis reveals why these improvements occur. In addition, a case study also demonstrates that A-LAMP generates environments and policies that preserve the task's optimality, confirming its correctness and reliability.

