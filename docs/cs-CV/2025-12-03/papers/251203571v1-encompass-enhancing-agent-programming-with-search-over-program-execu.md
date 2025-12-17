---
layout: default
title: EnCompass: Enhancing Agent Programming with Search Over Program Execution Paths
---

# EnCompass: Enhancing Agent Programming with Search Over Program Execution Paths

**arXiv**: [2512.03571v1](https://arxiv.org/abs/2512.03571) | [PDF](https://arxiv.org/pdf/2512.03571.pdf)

**作者**: Zhening Li, Armando Solar-Lezama, Yisong Yue, Stephan Zheng

---

## 💡 一句话要点

**提出EnCompass框架，通过概率天使非确定性编程模型分离LLM智能体工作流与推理策略。**

**关键词**: `LLM智能体编程` `概率天使非确定性` `推理策略分离` `Python框架` `搜索空间编译` `智能体可靠性`

## 📋 核心要点

1. 核心问题：现有LLM智能体编程常耦合工作流逻辑与推理策略，限制灵活性与实验效率。
2. 方法要点：引入概率天使非确定性编程模型，使用Python装饰器将工作流编译为搜索空间，支持独立调整推理策略。
3. 实验或效果：通过三个案例研究，展示框架能快速提升智能体可靠性，并轻松切换不同推理策略，减少额外编码。

## 📄 摘要（原文）

> We introduce a new approach to agent programming, the development of LLM-based agents. Current approaches to agent programming often entangle two aspects of agent design: the core workflow logic and the inference-time strategy (e.g., tree search). We introduce "probabilistic angelic nondeterminism" ("PAN"), a programming model that disentangles these two concerns, allowing the programmer to describe the agent workflow and independently experiment with different inference-time strategies by simply changing a few inputs. We provide an implementation of PAN in Python as the EnCompass framework, which uses a Python decorator to compile agent workflow programs into a search space. We present three case studies that demonstrate how the framework lets the programmer quickly improve the reliability of an agent and easily switch between different inference-time strategies, all with little additional coding.

