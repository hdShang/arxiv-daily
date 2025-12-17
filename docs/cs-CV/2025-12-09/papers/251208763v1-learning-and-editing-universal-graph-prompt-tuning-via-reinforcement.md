---
layout: default
title: Learning and Editing Universal Graph Prompt Tuning via Reinforcement Learning
---

# Learning and Editing Universal Graph Prompt Tuning via Reinforcement Learning

**arXiv**: [2512.08763v1](https://arxiv.org/abs/2512.08763) | [PDF](https://arxiv.org/pdf/2512.08763.pdf)

**作者**: Jinfeng Xu, Zheyu Chen, Shuo Yang, Jinze Li, Hewei Wang, Yijie Li, Edith C. H. Ngai

---

## 💡 一句话要点

**提出LEAP模型以强化通用图提示调优的理论基础并提升性能**

**关键词**: `图神经网络` `提示调优` `强化学习` `通用图提示` `节点选择` `少样本学习`

## 📋 核心要点

1. 早期图提示调优依赖任务特定设计，限制跨预训练策略的适应性
2. LEAP通过全节点提示保持理论基础，并利用强化学习编辑提示
3. 实验表明LEAP在全样本和少样本场景下优于微调和其他提示方法

## 📄 摘要（原文）

> Early graph prompt tuning approaches relied on task-specific designs for Graph Neural Networks (GNNs), limiting their adaptability across diverse pre-training strategies. In contrast, another promising line of research has investigated universal graph prompt tuning, which operates directly in the input graph's feature space and builds a theoretical foundation that universal graph prompt tuning can theoretically achieve an equivalent effect of any prompting function, eliminating dependence on specific pre-training strategies. Recent works propose selective node-based graph prompt tuning to pursue more ideal prompts. However, we argue that selective node-based graph prompt tuning inevitably compromises the theoretical foundation of universal graph prompt tuning. In this paper, we strengthen the theoretical foundation of universal graph prompt tuning by introducing stricter constraints, demonstrating that adding prompts to all nodes is a necessary condition for achieving the universality of graph prompts. To this end, we propose a novel model and paradigm, Learning and Editing Universal GrAph Prompt Tuning (LEAP), which preserves the theoretical foundation of universal graph prompt tuning while pursuing more ideal prompts. Specifically, we first build the basic universal graph prompts to preserve the theoretical foundation and then employ actor-critic reinforcement learning to select nodes and edit prompts. Extensive experiments on graph- and node-level tasks across various pre-training strategies in both full-shot and few-shot scenarios show that LEAP consistently outperforms fine-tuning and other prompt-based approaches.

