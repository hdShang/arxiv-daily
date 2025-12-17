---
layout: default
title: Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning
---

# Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14057" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14057v1</a>
  <a href="https://arxiv.org/pdf/2512.14057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14057v1" onclick="toggleFavorite(this, '2512.14057v1', 'Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amir M. Soufi Enayati, Homayoun Honari, Homayoun Najjaran

**分类**: cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出CRAFT：一种基于无动作Transformer的元强化学习上下文表示方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `元强化学习` `上下文表示` `Transformer` `无动作学习` `机器人控制`

## 📋 核心要点

1. 传统元强化学习方法依赖动作信息进行任务推断，导致任务推断与特定策略绑定，泛化能力受限。
2. CRAFT通过无动作Transformer编码器-解码器，仅从状态和奖励序列推断任务表示，解耦任务推断与策略优化。
3. 实验表明，CRAFT在MetaWorld ML-10上实现了更快的适应、更好的泛化和更有效的探索。

## 📝 摘要（中文）

强化学习(RL)使机器人能够在不确定环境中运行，但标准方法通常难以泛化到未见过的任务。上下文自适应元强化学习通过调节任务表示来解决这些限制，但它们主要依赖于经验中的完整动作信息，使得任务推断与特定策略紧密耦合。本文介绍了一种通过无动作Transformer编码器-解码器(CRAFT)进行上下文表示的方法，这是一种仅从状态和奖励序列推断任务表示的信念模型。通过消除对动作的依赖，CRAFT将任务推断与策略优化解耦，支持模块化训练，并利用摊销变分推断进行可扩展的信念更新。该模型建立在具有旋转位置嵌入的Transformer编码器-解码器之上，捕获长程时间依赖性，并稳健地编码参数和非参数任务变化。在MetaWorld ML-10机器人操作基准上的实验表明，与上下文自适应元强化学习基线相比，CRAFT实现了更快的适应、改进的泛化和更有效的探索。这些发现突出了无动作推断作为机器人控制中可扩展RL的基础的潜力。

## 🔬 方法详解

**问题定义**：现有元强化学习方法在进行任务推断时，通常需要依赖完整的动作信息，这使得任务推断过程与特定的策略紧密耦合。这种耦合限制了模型的泛化能力，尤其是在面对未见过的任务时，模型难以快速适应。此外，依赖动作信息也使得模型难以进行模块化训练，不利于扩展到更复杂的任务。

**核心思路**：CRAFT的核心思路是设计一个无动作的信念模型，该模型仅通过观察状态和奖励序列来推断任务表示。通过消除对动作的依赖，CRAFT将任务推断与策略优化解耦，从而提高了模型的泛化能力和可扩展性。这种解耦也使得模型可以进行模块化训练，例如可以先训练任务推断模型，然后再训练策略优化模型。

**技术框架**：CRAFT的整体框架包括一个Transformer编码器-解码器结构。编码器接收状态和奖励序列作为输入，并将其编码成一个上下文向量，该向量代表了对当前任务的信念。解码器接收该上下文向量，并输出一个任务表示。该任务表示可以被用于指导策略优化。CRAFT使用摊销变分推断来更新信念，从而实现可扩展的信念更新。

**关键创新**：CRAFT最重要的创新点在于其无动作的任务推断方法。与现有方法相比，CRAFT不需要依赖动作信息，从而实现了任务推断与策略优化的解耦。这种解耦提高了模型的泛化能力和可扩展性。此外，CRAFT还使用了Transformer编码器-解码器结构，可以有效地捕获长程时间依赖性。

**关键设计**：CRAFT的关键设计包括：1) 使用旋转位置嵌入的Transformer编码器-解码器，以捕获长程时间依赖性；2) 使用摊销变分推断进行可扩展的信念更新；3) 设计损失函数，以鼓励模型学习到鲁棒的任务表示。具体来说，损失函数包括重构损失和KL散度损失。重构损失用于鼓励模型能够从任务表示中重构出原始的状态和奖励序列，KL散度损失用于约束任务表示的分布。

## 📊 实验亮点

CRAFT在MetaWorld ML-10机器人操作基准测试中表现出色，与上下文自适应元强化学习基线相比，实现了更快的适应速度、更好的泛化能力和更有效的探索。具体性能数据未知，但论文强调了CRAFT在多个指标上均优于现有方法。

## 🎯 应用场景

CRAFT的潜在应用领域包括机器人控制、游戏AI和自动驾驶等。通过学习仅基于状态和奖励的任务表示，CRAFT可以帮助机器人在未知的环境中快速适应和学习新的任务。这对于需要在复杂和动态环境中运行的机器人来说尤其重要。此外，CRAFT的模块化设计也使其易于扩展到更复杂的任务。

## 📄 摘要（原文）

> Reinforcement learning (RL) enables robots to operate in uncertain environments, but standard approaches often struggle with poor generalization to unseen tasks. Context-adaptive meta reinforcement learning addresses these limitations by conditioning on the task representation, yet they mostly rely on complete action information in the experience making task inference tightly coupled to a specific policy. This paper introduces Context Representation via Action Free Transformer encoder decoder (CRAFT), a belief model that infers task representations solely from sequences of states and rewards. By removing the dependence on actions, CRAFT decouples task inference from policy optimization, supports modular training, and leverages amortized variational inference for scalable belief updates. Built on a transformer encoder decoder with rotary positional embeddings, the model captures long range temporal dependencies and robustly encodes both parametric and non-parametric task variations. Experiments on the MetaWorld ML-10 robotic manipulation benchmark show that CRAFT achieves faster adaptation, improved generalization, and more effective exploration compared to context adaptive meta--RL baselines. These findings highlight the potential of action-free inference as a foundation for scalable RL in robotic control.

