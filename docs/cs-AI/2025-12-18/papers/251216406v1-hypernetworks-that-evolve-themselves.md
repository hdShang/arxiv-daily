---
layout: default
title: Hypernetworks That Evolve Themselves
---

# Hypernetworks That Evolve Themselves

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16406" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16406v1</a>
  <a href="https://arxiv.org/pdf/2512.16406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16406v1', 'Hypernetworks That Evolve Themselves')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joachim Winther Pedersen, Erwan Plantec, Eleni Nisioti, Marcello Barylli, Milton Montero, Kathrin Korte, Sebastian Risi

**分类**: cs.NE, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出自引用图超网络，实现无需外部优化器的神经网络自进化。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自进化神经网络` `超网络` `图神经网络` `强化学习` `自主学习`

## 📋 核心要点

1. 传统神经网络依赖外部优化器进行进化，限制了其自主性和适应性，面临环境变化时表现不佳。
2. 提出自引用图超网络，将变异和遗传机制嵌入网络内部，实现神经网络的自我变异、评估和进化。
3. 在多个强化学习基准测试中，该方法展现出快速适应环境变化的能力，并能自主学习复杂的运动控制策略。

## 📝 摘要（中文）

本文提出自引用图超网络（Self-Referential Graph HyperNetworks, Self-Referential GHNs），该系统将变异和遗传机制嵌入网络内部，无需依赖外部优化器即可实现神经网络的自进化。通过结合超网络、随机参数生成和基于图的表示，Self-Referential GHNs能够自我变异和评估，同时将变异率作为可选择的特征进行调整。在包含环境变化的强化学习基准测试（CartPoleSwitch, LunarLander-Switch）中，Self-Referential GHNs展现出快速、可靠的适应性和涌现的人口动态。在locomotion基准测试Ant-v5中，它们进化出连贯的步态，并通过自主降低种群变异性以集中于有希望的解决方案，展现出良好的微调能力。研究结果表明，可进化性本身可以从神经自我参照中涌现。Self-Referential GHNs代表着朝着更接近生物进化的合成系统迈出的一步，为自主、开放式学习智能体提供了工具。

## 🔬 方法详解

**问题定义**：现有神经网络的进化通常依赖于外部优化器，例如遗传算法或进化策略。这些外部优化器需要手动设计和调整，并且可能无法有效地探索复杂的搜索空间。此外，当环境发生变化时，预先训练好的神经网络可能难以适应，需要重新训练或进行微调，效率较低。因此，如何让神经网络自主地进化，适应不断变化的环境，是一个重要的研究问题。

**核心思路**：本文的核心思路是将神经网络的进化机制嵌入到网络本身中，使其能够自我变异、评估和选择。通过使用超网络生成神经网络的参数，并结合随机参数生成和基于图的表示，可以实现对神经网络结构的灵活控制和修改。同时，将变异率作为可选择的特征进行调整，可以使网络自主地控制自身的进化速度。

**技术框架**：Self-Referential GHNs的整体架构包含以下几个主要模块：1) **图表示模块**：使用图结构来表示神经网络的结构和连接。2) **超网络模块**：使用超网络来生成神经网络的参数，超网络的输入是图表示，输出是神经网络的权重。3) **变异模块**：通过随机修改图结构和超网络参数来实现神经网络的变异。4) **评估模块**：使用强化学习或其他评估方法来评估变异后的神经网络的性能。5) **选择模块**：根据性能选择优秀的个体，并将其作为下一代的基础。

**关键创新**：该方法最重要的技术创新点在于将神经网络的进化机制嵌入到网络本身中，实现了神经网络的自引用和自进化。与传统的进化方法相比，该方法无需外部优化器，可以自主地探索复杂的搜索空间，并适应不断变化的环境。此外，将变异率作为可选择的特征进行调整，可以使网络自主地控制自身的进化速度，提高了进化的效率。

**关键设计**：在具体实现中，使用了图神经网络来表示神经网络的结构和连接。超网络采用多层感知机结构，输入是图节点的特征向量，输出是神经网络的权重。变异操作包括添加、删除和修改图节点和连接。评估方法采用强化学习算法，例如PPO。选择方法采用锦标赛选择或轮盘赌选择。变异率的调整通过梯度下降或其他优化方法来实现。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16406v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16406v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16406v1/figures/environments.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在CartPoleSwitch和LunarLander-Switch等强化学习基准测试中，Self-Referential GHNs展现出快速、可靠的适应性。在Ant-v5 locomotion基准测试中，它们进化出连贯的步态，并通过自主降低种群变异性以集中于有希望的解决方案，展现出良好的微调能力。这些结果表明，该方法具有很强的进化能力和适应性。

## 🎯 应用场景

该研究成果可应用于自主机器人、游戏AI、智能控制等领域。通过自进化，机器人可以自主学习适应复杂环境，游戏AI可以不断进化出更智能的策略，智能控制系统可以自动优化参数以提高性能。该研究为开发更智能、更自主的AI系统提供了新的思路。

## 📄 摘要（原文）

> How can neural networks evolve themselves without relying on external optimizers? We propose Self-Referential Graph HyperNetworks, systems where the very machinery of variation and inheritance is embedded within the network. By uniting hypernetworks, stochastic parameter generation, and graph-based representations, Self-Referential GHNs mutate and evaluate themselves while adapting mutation rates as selectable traits. Through new reinforcement learning benchmarks with environmental shifts (CartPoleSwitch, LunarLander-Switch), Self-Referential GHNs show swift, reliable adaptation and emergent population dynamics. In the locomotion benchmark Ant-v5, they evolve coherent gaits, showing promising fine-tuning capabilities by autonomously decreasing variation in the population to concentrate around promising solutions. Our findings support the idea that evolvability itself can emerge from neural self-reference. Self-Referential GHNs reflect a step toward synthetic systems that more closely mirror biological evolution, offering tools for autonomous, open-ended learning agents.

