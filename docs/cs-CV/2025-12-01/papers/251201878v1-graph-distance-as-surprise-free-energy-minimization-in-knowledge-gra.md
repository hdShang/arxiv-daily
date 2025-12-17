---
layout: default
title: Graph Distance as Surprise: Free Energy Minimization in Knowledge Graph Reasoning
---

# Graph Distance as Surprise: Free Energy Minimization in Knowledge Graph Reasoning

**arXiv**: [2512.01878v1](https://arxiv.org/abs/2512.01878) | [PDF](https://arxiv.org/pdf/2512.01878.pdf)

**作者**: Gaganpreet Jhajj, Fuhua Lin

---

## 💡 一句话要点

**提出基于图距离的惊奇最小化框架，用于知识图谱推理，连接自由能原理与图神经网络。**

**关键词**: `知识图谱推理` `自由能原理` `图距离` `惊奇最小化` `图神经网络` `强化学习`

## 📋 核心要点

1. 核心问题：知识图谱推理中如何量化惊奇以指导推理过程。
2. 方法要点：使用有向图最短路径距离形式化惊奇，将知识图谱作为生成模型。
3. 实验或效果：未知，本文为进展中研究，探索距离惊奇是否可扩展至语法树结构。

## 📄 摘要（原文）

> In this work, we propose that reasoning in knowledge graph (KG) networks can be guided by surprise minimization. Entities that are close in graph distance will have lower surprise than those farther apart. This connects the Free Energy Principle (FEP) from neuroscience to KG systems, where the KG serves as the agent's generative model. We formalize surprise using the shortest-path distance in directed graphs and provide a framework for KG-based agents. Graph distance appears in graph neural networks as message passing depth and in model-based reinforcement learning as world model trajectories. This work-in-progress study explores whether distance-based surprise can extend recent work showing that syntax minimizes surprise and free energy via tree structures.

