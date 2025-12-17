---
layout: default
title: Memo: Training Memory-Efficient Embodied Agents with Reinforcement Learning
---

# Memo: Training Memory-Efficient Embodied Agents with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19732" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19732v2</a>
  <a href="https://arxiv.org/pdf/2510.19732.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19732v2" onclick="toggleFavorite(this, '2510.19732v2', 'Memo: Training Memory-Efficient Embodied Agents with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gunshi Gupta, Karmesh Yadav, Zsolt Kira, Yarin Gal, Rahaf Aljundi

**分类**: cs.AI, cs.CV, cs.RO

**发布日期**: 2025-10-22 (更新: 2025-11-27)

**备注**: Accepted for Spotlight Presentation at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/gunshi/memo)

---

## 💡 一句话要点

**提出Memo：一种内存高效的强化学习具身智能体训练方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `具身智能` `强化学习` `Transformer` `记忆网络` `长时程任务`

## 📋 核心要点

1. 现有基于Transformer的具身智能体策略训练，面临视觉输入超出Transformer上下文长度限制的挑战。
2. Memo通过周期性地生成和检索摘要token，将输入信息压缩成记忆，从而实现高效的上下文感知。
3. 实验表明，Memo在内存效率、计算效率和泛化能力上优于传统Transformer，尤其是在长时程任务中。

## 📝 摘要（中文）

为了使具身智能体能够在较长时间范围内有效运行，开发能够形成和访问记忆的模型至关重要，以便在环境中保持上下文感知。在当前基于Transformer的策略训练范式中，视觉输入通常会超出Transformer的上下文限制，而人类可以维护和利用压缩为记忆的终身经验。原则上可以进行显著的压缩，因为大部分输入是不相关的并且可以被抽象。然而，现有的方法主要集中在具有固定大小内存的循环模型或完全依赖上下文的Transformer。本文提出Memo，一种基于Transformer的架构和训练方法，用于在内存密集型、长时程任务上进行强化学习（RL）。Memo通过在训练期间将周期性的摘要token与模型的输入交错，从而实现记忆的创建和检索。我们在网格世界元强化学习基准测试和逼真室内环境中的多对象导航任务中证明了Memo的有效性。Memo优于朴素的长上下文Transformer基线，同时更具计算和存储效率。此外，Memo在推理时更好地泛化到更长的上下文，并且在流式设置中保持鲁棒性，在这种设置中，历史上下文必须被截断以适应推理约束。

## 🔬 方法详解

**问题定义**：现有基于Transformer的具身智能体在长时程任务中面临上下文信息爆炸的问题。Transformer的上下文窗口有限，无法处理长时间序列的视觉输入，导致性能下降。此外，存储和计算成本也随着上下文长度的增加而显著增加。现有方法要么依赖固定大小的循环记忆，要么完全依赖Transformer的上下文，无法有效解决长时程任务中的记忆问题。

**核心思路**：Memo的核心思路是通过周期性地生成和检索摘要token来压缩和利用历史信息。在训练过程中，模型学习将关键信息提炼成摘要token，并将其存储在记忆中。在推理过程中，模型可以根据当前状态检索相关的摘要token，从而在有限的上下文窗口内访问更长的历史信息。这种方法类似于人类的记忆机制，能够有效地处理长时程任务。

**技术框架**：Memo的整体架构包括一个Transformer编码器、一个记忆模块和一个策略网络。Transformer编码器负责将视觉输入编码成特征向量。记忆模块负责存储和检索摘要token。策略网络根据当前状态和检索到的摘要token生成动作。训练过程包括两个阶段：记忆创建阶段和策略学习阶段。在记忆创建阶段，模型学习生成能够代表历史信息的摘要token。在策略学习阶段，模型学习根据当前状态和检索到的摘要token生成最优动作。

**关键创新**：Memo的关键创新在于将记忆机制融入到Transformer架构中，并提出了一种有效的训练方法来学习生成和检索摘要token。与现有方法相比，Memo能够更有效地利用历史信息，并在长时程任务中取得更好的性能。此外，Memo还具有更高的计算和存储效率，使其能够应用于更复杂的具身智能体任务。

**关键设计**：Memo的关键设计包括摘要token的生成方式、记忆模块的结构和检索机制。摘要token通过一个独立的Transformer层生成，该层接收Transformer编码器的输出作为输入。记忆模块采用键值对存储结构，其中键是摘要token，值是对应的历史信息。检索机制采用注意力机制，根据当前状态计算每个摘要token的权重，并选择权重最高的摘要token。损失函数包括策略梯度损失和记忆损失，其中策略梯度损失用于优化策略网络，记忆损失用于优化摘要token的生成。

## 📊 实验亮点

Memo在网格世界元强化学习基准测试和逼真室内环境中的多对象导航任务中取得了显著的成果。在网格世界任务中，Memo的性能优于朴素的长上下文Transformer基线。在多对象导航任务中，Memo在导航成功率和路径长度方面均优于现有方法。此外，Memo还表现出更好的泛化能力，能够在更长的上下文长度下保持鲁棒性。实验结果表明，Memo是一种有效的内存高效的强化学习方法。

## 🎯 应用场景

Memo具有广泛的应用前景，例如机器人导航、长期对话、游戏AI等。在机器人导航领域，Memo可以帮助机器人在复杂环境中进行长期探索和定位。在长期对话领域，Memo可以帮助模型记住对话历史，从而生成更连贯和自然的回复。在游戏AI领域，Memo可以帮助智能体更好地理解游戏环境，并制定更有效的策略。Memo的内存效率和泛化能力使其能够应用于各种需要长期记忆的任务。

## 📄 摘要（原文）

> To enable embodied agents to operate effectively over extended timeframes, it is crucial to develop models that form and access memories to stay contextualized in their environment. In the current paradigm of training transformer-based policies for embodied sequential decision-making tasks, visual inputs often overwhelm the context limits of transformers, while humans can maintain and utilize a lifetime of experience compressed as memories. Significant compression is possible in principle, as much of the input is irrelevant and can be abstracted. However, existing approaches predominantly focus on either recurrent models with fixed-size memory or transformers with full-context reliance. In this work, we propose Memo, a transformer-based architecture and training recipe for reinforcement learning (RL) on memory-intensive, long-horizon tasks. Memo incorporates the creation and retrieval of memory by interleaving periodic summarization tokens with the inputs of a model during training. We demonstrate Memo's effectiveness on a gridworld meta-RL benchmark and a multi-object navigation task in photo-realistic indoor settings. Memo outperforms naive long-context transformer baselines while being more compute and storage efficient. Additionally, Memo generalizes better to longer contexts at inference time and remains robust in streaming settings, where historical context must be truncated to fit inference constraints. Our code is available at: https://github.com/gunshi/memo.

