---
layout: default
title: Dynamic Learning Rate Scheduling based on Loss Changes Leads to Faster Convergence
---

# Dynamic Learning Rate Scheduling based on Loss Changes Leads to Faster Convergence

**arXiv**: [2512.14527v1](https://arxiv.org/abs/2512.14527) | [PDF](https://arxiv.org/pdf/2512.14527.pdf)

**作者**: Shreyas Subramanian, Bala Krishnamoorthy, Pranav Murthy

**分类**: cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于损失变化的动态学习率调度器GreedyLR，以加速模型训练收敛**

**关键词**: `动态学习率调度` `训练优化` `收敛加速` `自适应调整` `损失变化` `大规模模型训练` `理论分析` `鲁棒性验证`

## 📋 核心要点

1. 现有方法多依赖固定模式调度器（如余弦衰减），缺乏对训练动态的自适应调整，可能导致收敛速度慢或性能不佳。
2. 提出GreedyLR调度器，核心思想是根据损失变化动态调整学习率，通过理论推导确定最优缩放因子以加速收敛。
3. 在NLP、CV和LLM任务上实验显示，GreedyLR在准确率、速度和收敛性上优于现有调度器，参数规模达70亿。

## 📝 摘要（中文）

尽管训练优化器取得了显著进展，但大多数研究工作仍使用余弦或指数衰减等常见调度器。本文研究了GreedyLR，这是一种新颖的调度器，能够根据当前损失在训练过程中自适应调整学习率。为了验证所提出调度器的有效性，我们在多个NLP、CV和LLM任务上进行了实验，参数规模高达70亿，包括微调和预训练实验。结果表明，我们的方法在准确性、速度和收敛性方面优于几种最先进的调度器。我们还提供了GreedyLR算法的理论分析，包括收敛性证明和最大化收敛速率的最优缩放因子F的推导，并通过实验展示了算法对现实噪声环境的鲁棒性。我们的调度器易于实现、计算高效，可被视为训练的良好默认调度器。

## 🔬 方法详解

GreedyLR是一种动态学习率调度器，整体框架基于训练过程中的损失变化来调整学习率。关键技术创新点在于自适应机制：算法实时监控损失值，根据损失的变化幅度计算学习率调整因子，通过理论分析推导出最优缩放因子F以最大化收敛速率。与现有方法的主要区别在于，它不依赖预定义的时间表（如余弦衰减），而是根据训练动态进行实时调整，从而更灵活地适应不同任务和模型，提高了对噪声环境的鲁棒性。

## 📊 实验亮点

实验在多个NLP、CV和LLM任务上进行，参数规模高达70亿，结果显示GreedyLR在准确率、训练速度和收敛性方面均优于现有最先进调度器，同时算法对噪声环境表现出良好鲁棒性。

## 🎯 应用场景

该研究可广泛应用于自然语言处理、计算机视觉和大语言模型的训练场景，包括微调和预训练任务。其实际价值在于提供了一种高效、自适应的学习率调度方法，能加速模型收敛、提升训练效率，适用于大规模参数模型（如70亿参数）的训练优化。

## 📄 摘要（原文）

> Despite significant advances in optimizers for training, most research works use common scheduler choices like Cosine or exponential decay. In this paper, we study \emph{GreedyLR}, a novel scheduler that adaptively adjusts the learning rate during training based on the current loss. To validate the effectiveness of our proposed scheduler, we conduct experiments on several NLP, CV, and LLM tasks with up to $7B$ parameters, including both fine-tuning and pre-training experiments. The results show that our approach outperforms several state-of-the-art schedulers in terms of accuracy, speed, and convergence. We also provide a theoretical analysis of the GreedyLR algorithm, including a proof of convergence and derivation of the optimal scaling factor $F$ that maximizes the convergence rate, along with experiments to show robustness of the algorithm to realistic noisy landscapes. Our scheduler is easy to implement, computationally efficient, and could be considered a good default scheduler for training.

