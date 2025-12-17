---
layout: default
title: Zero-Shot Instruction Following in RL via Structured LTL Representations
---

# Zero-Shot Instruction Following in RL via Structured LTL Representations

**arXiv**: [2512.02633v1](https://arxiv.org/abs/2512.02633) | [PDF](https://arxiv.org/pdf/2512.02633.pdf)

**作者**: Mattia Giuri, Mathias Jackermeier, Alessandro Abate

---

## 💡 一句话要点

**提出基于图神经网络的布尔公式序列方法，以解决多事件交互下强化学习的零样本指令跟随问题。**

**关键词**: `强化学习` `线性时序逻辑` `图神经网络` `零样本学习` `多任务策略` `结构化表示`

## 📋 核心要点

1. 核心问题：现有方法在多个高维事件同时发生且复杂交互的环境中表现不足。
2. 方法要点：使用布尔公式序列对齐自动机转换，并通过图神经网络编码结构化任务表示。
3. 实验或效果：在复杂棋类环境中验证了方法的优势。

## 📄 摘要（原文）

> Linear temporal logic (LTL) is a compelling framework for specifying complex, structured tasks for reinforcement learning (RL) agents. Recent work has shown that interpreting LTL instructions as finite automata, which can be seen as high-level programs monitoring task progress, enables learning a single generalist policy capable of executing arbitrary instructions at test time. However, existing approaches fall short in environments where multiple high-level events (i.e., atomic propositions) can be true at the same time and potentially interact in complicated ways. In this work, we propose a novel approach to learning a multi-task policy for following arbitrary LTL instructions that addresses this shortcoming. Our method conditions the policy on sequences of simple Boolean formulae, which directly align with transitions in the automaton, and are encoded via a graph neural network (GNN) to yield structured task representations. Experiments in a complex chess-based environment demonstrate the advantages of our approach.

