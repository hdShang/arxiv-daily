---
layout: default
title: Automated Generation of MDPs Using Logic Programming and LLMs for Robotic Applications
---

# Automated Generation of MDPs Using Logic Programming and LLMs for Robotic Applications

**arXiv**: [2511.23143v1](https://arxiv.org/abs/2511.23143) | [PDF](https://arxiv.org/pdf/2511.23143.pdf)

**作者**: Enrico Saccon, Davide De Martini, Matteo Saveriano, Edoardo Lamon, Luigi Palopoli, Marco Roveri

---

## 💡 一句话要点

**提出集成大语言模型与形式化验证的框架，以自动化生成MDP并合成策略，应用于机器人交互场景。**

**关键词**: `大语言模型` `马尔可夫决策过程` `形式化验证` `机器人规划` `概率规划` `知识提取`

## 📋 核心要点

1. 核心问题：从自然语言描述中自动化创建马尔可夫决策过程（MDP）以支持机器人概率规划，减少手动工作量。
2. 方法要点：利用大语言模型提取Prolog知识库，通过可达性分析自动构建MDP，并使用Storm模型检查器合成最优策略。
3. 实验或效果：在三个人机交互场景中验证框架，生成可执行策略，展示其可访问性和可扩展性。

## 📄 摘要（原文）

> We present a novel framework that integrates Large Language Models (LLMs) with automated planning and formal verification to streamline the creation and use of Markov Decision Processes (MDP). Our system leverages LLMs to extract structured knowledge in the form of a Prolog knowledge base from natural language (NL) descriptions. It then automatically constructs an MDP through reachability analysis, and synthesises optimal policies using the Storm model checker. The resulting policy is exported as a state-action table for execution. We validate the framework in three human-robot interaction scenarios, demonstrating its ability to produce executable policies with minimal manual effort. This work highlights the potential of combining language models with formal methods to enable more accessible and scalable probabilistic planning in robotics.

