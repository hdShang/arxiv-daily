---
layout: default
title: Learned-Rule-Augmented Large Language Model Evaluators
---

# Learned-Rule-Augmented Large Language Model Evaluators

**arXiv**: [2512.01958v1](https://arxiv.org/abs/2512.01958) | [PDF](https://arxiv.org/pdf/2512.01958.pdf)

**作者**: Jie Meng, Jin Mao

---

## 💡 一句话要点

**提出规则增强评估范式，通过规则蒸馏与策略应用提升大语言模型作为通用评估器的泛化能力。**

**关键词**: `大语言模型评估` `规则蒸馏` `蒙特卡洛树搜索` `链式规则` `强化学习` `通用评估器`

## 📋 核心要点

1. 核心问题：现有大语言模型评估器依赖人工设计原则，泛化受限且与数据和模型理解不匹配。
2. 方法要点：采用蒙特卡洛树搜索自动从数据中蒸馏评分规则，并设计链式规则和强化学习策略以增强模型应用规则的能力。
3. 实验或效果：在多样化任务上验证了方法的有效性和泛化性，适用于广泛评估场景。

## 📄 摘要（原文）

> Large language models (LLMs) are predominantly used as evaluators for natural language generation (NLG) tasks, but their application to broader evaluation scenarios remains limited. In this work, we explore the potential of LLMs as general evaluators across diverse tasks. Although LLM-based evaluators have made progress in different areas, existing methods struggle to generalize due to their reliance on costly, human-designed evaluation principles, which are often misaligned with both annotated data and LLMs' understanding.To address these challenges, we propose a rule-augmented evaluation paradigm. First, we introduce a rule distillation method that automatically extracts scoring rules from data using an LLM-assisted Monte Carlo Tree Search (MCTS), alleviating scalability issues and improving alignment with data. Second, to enable LLMs to effectively apply the learned rules, we propose two strategies: (1) Chain-of-Rule (CoR), which guides LLM to follow distilled rules, and (2) training a rule-augmented LLM evaluator (RuAE) via reinforcement learning, further bridging the gap between rules and LLMs' reasoning. Extensive experiments on diverse tasks demonstrate the effectiveness and generalizability of our approach across various evaluation scenarios.

