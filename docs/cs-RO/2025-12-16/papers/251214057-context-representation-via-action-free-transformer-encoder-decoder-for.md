---
layout: default
title: Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning
---

# Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14057" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14057</a>
  <a href="https://arxiv.org/pdf/2512.14057.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14057" onclick="toggleFavorite(this, '2512.14057', 'Context Representation via Action-Free Transformer encoder-decoder for Meta Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amir M. Soufi Enayati, Homayoun Honari, Homayoun Najjaran

**分类**: cs.RO

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出CRAFT：一种基于无动作Transformer的元强化学习上下文表示方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `元强化学习` `上下文表示` `Transformer` `无动作推断` `机器人控制`

## 📋 核心要点

1. 传统元强化学习方法依赖动作信息进行任务推断，导致任务推断与策略优化紧耦合，限制了泛化能力。
2. CRAFT通过仅使用状态和奖励序列进行任务推断，解耦了任务推断与策略优化，支持模块化训练。
3. 实验表明，CRAFT在MetaWorld ML-10基准测试中，相比现有方法，实现了更快的适应、更好的泛化和更有效的探索。

## 📝 摘要（中文）

强化学习(RL)使机器人能够在不确定环境中运行，但标准方法通常难以泛化到未见过的任务。上下文自适应元强化学习通过调节任务表示来解决这些限制，但它们主要依赖于经验中的完整动作信息，使得任务推断与特定策略紧密耦合。本文介绍了一种通过无动作Transformer编码器-解码器(CRAFT)进行上下文表示的方法，这是一种仅从状态和奖励序列推断任务表示的信念模型。通过消除对动作的依赖，CRAFT将任务推断与策略优化解耦，支持模块化训练，并利用摊销变分推断进行可扩展的信念更新。该模型建立在具有旋转位置嵌入的Transformer编码器-解码器之上，可以捕获长程时间依赖性，并稳健地编码参数和非参数任务变化。在MetaWorld ML-10机器人操作基准上的实验表明，与上下文自适应元强化学习基线相比，CRAFT实现了更快的适应、改进的泛化和更有效的探索。这些发现突出了无动作推断作为机器人控制中可扩展RL的基础的潜力。

## 🔬 方法详解

**问题定义**：现有元强化学习方法在进行任务推断时，通常需要依赖完整的动作信息。这种依赖使得任务推断过程与特定的策略紧密耦合，限制了模型在未见过的任务上的泛化能力。此外，这种耦合也使得模型的训练和优化变得复杂，难以进行模块化设计。

**核心思路**：CRAFT的核心思路是通过构建一个信念模型，该模型仅依赖于状态和奖励序列来推断任务表示，从而避免对动作信息的依赖。通过这种方式，CRAFT将任务推断与策略优化解耦，使得模型可以更加灵活地适应不同的任务，并支持模块化的训练和优化。

**技术框架**：CRAFT采用Transformer编码器-解码器架构作为其核心技术框架。该框架包含两个主要模块：编码器和解码器。编码器负责将状态和奖励序列编码成一个上下文向量，该向量代表了对当前任务的信念。解码器则负责根据该上下文向量来预测未来的状态和奖励。此外，CRAFT还采用了摊销变分推断(Amortized Variational Inference)来提高信念更新的可扩展性。

**关键创新**：CRAFT最重要的技术创新点在于其无动作的任务推断方法。与传统的元强化学习方法不同，CRAFT不需要依赖动作信息来进行任务推断，而是仅使用状态和奖励序列。这种无动作的推断方法使得CRAFT可以更加灵活地适应不同的任务，并支持模块化的训练和优化。此外，CRAFT还采用了旋转位置嵌入(Rotary Positional Embeddings)来更好地捕捉长程时间依赖性。

**关键设计**：CRAFT的关键设计包括：1) 使用Transformer编码器-解码器架构来捕捉长程时间依赖性；2) 采用旋转位置嵌入来编码序列信息；3) 使用摊销变分推断来提高信念更新的可扩展性；4) 设计合适的损失函数来训练编码器和解码器，例如，可以使用预测状态和奖励的均方误差作为损失函数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14057/figs/meta_variations.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14057/figs/meta_bamdp.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14057/figs/meta_arch_overview.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CRAFT在MetaWorld ML-10机器人操作基准测试中，相比于上下文自适应元强化学习基线，实现了更快的适应、更好的泛化和更有效的探索。具体来说，CRAFT在多个任务上的性能都优于基线方法，并且在一些困难任务上取得了显著的提升。这些结果表明，CRAFT的无动作任务推断方法是有效的，并且可以作为机器人控制中可扩展RL的基础。

## 🎯 应用场景

CRAFT的潜在应用领域包括机器人控制、自动驾驶、游戏AI等。通过解耦任务推断和策略优化，CRAFT可以帮助机器人在复杂和不确定的环境中更快地适应新任务，提高其泛化能力和鲁棒性。此外，CRAFT的模块化设计也使得其可以更容易地集成到现有的强化学习系统中，从而加速相关领域的研究和应用。

## 📄 摘要（原文）

> Reinforcement learning (RL) enables robots to operate in uncertain environments, but standard approaches often struggle with poor generalization to unseen tasks. Context-adaptive meta reinforcement learning addresses these limitations by conditioning on the task representation, yet they mostly rely on complete action information in the experience making task inference tightly coupled to a specific policy. This paper introduces Context Representation via Action Free Transformer encoder decoder (CRAFT), a belief model that infers task representations solely from sequences of states and rewards. By removing the dependence on actions, CRAFT decouples task inference from policy optimization, supports modular training, and leverages amortized variational inference for scalable belief updates. Built on a transformer encoder decoder with rotary positional embeddings, the model captures long range temporal dependencies and robustly encodes both parametric and non-parametric task variations. Experiments on the MetaWorld ML-10 robotic manipulation benchmark show that CRAFT achieves faster adaptation, improved generalization, and more effective exploration compared to context adaptive meta--RL baselines. These findings highlight the potential of action-free inference as a foundation for scalable RL in robotic control.

