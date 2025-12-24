---
layout: default
title: "RLP: Reinforcement as a Pretraining Objective"
---

# RLP: Reinforcement as a Pretraining Objective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01265" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01265v1</a>
  <a href="https://arxiv.org/pdf/2510.01265.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01265v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01265v1', 'RLP: Reinforcement as a Pretraining Objective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Hatamizadeh, Syeda Nahida Akter, Shrimai Prabhumoye, Jan Kautz, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Yejin Choi

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-09-26

**备注**: RLP introduces a new paradigm for RL-based Pretraining

---

## 💡 一句话要点

**提出RLP：一种将强化学习作为预训练目标的方法，提升模型推理能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `预训练` `思维链` `信息增益` `推理能力`

## 📋 核心要点

1. 现有大型语言模型训练主要依赖于基于大量数据的下一个token预测，缺乏探索性学习。
2. RLP将强化学习融入预训练阶段，鼓励模型通过思维链探索，并根据信息增益给予奖励。
3. 实验表明，RLP在多个数学和科学推理基准测试中显著提升了模型性能，且具有良好的可扩展性。

## 📝 摘要（中文）

大型推理模型的训练范式通常始于在海量数据上使用下一个token预测损失进行预训练。强化学习虽然在扩展推理能力方面很强大，但通常只作为后训练的最后阶段引入，并且先于监督微调。本文提出了RLP，一种信息驱动的强化预训练目标，将强化学习的核心精神——探索——带到预训练的最后阶段。核心思想是将思维链视为一种探索性行为，其奖励基于其为预测未来token提供的信息增益来计算。这种训练目标本质上鼓励模型在预测接下来会发生什么之前进行独立思考，从而在预训练的早期阶段培养独立的思考行为。更具体地说，奖励信号衡量的是在同时以上下文和一个采样的推理链为条件时，下一个token的对数似然的增加，与仅以上下文为条件相比。这种方法产生了一种无需验证器的密集奖励信号，从而可以在预训练期间对整个文档流进行有效训练。具体来说，RLP将推理的强化学习重新定义为普通文本上的预训练目标，弥合了下一个token预测和有用的思维链推理的出现之间的差距。在Qwen3-1.7B-Base上使用RLP进行预训练，使八个基准数学和科学套件的总体平均水平提高了19%。通过相同的后训练，收益会累积，在诸如AIME25和MMLU-Pro等推理繁重的任务上获得了最大的改进。将RLP应用于混合Nemotron-Nano-12B-v2将总体平均水平从42.81%提高到61.32%，并将科学推理的平均水平提高了23%，证明了跨架构和模型大小的可扩展性。

## 🔬 方法详解

**问题定义**：现有大型语言模型的训练范式主要依赖于下一个token预测，这种方法虽然有效，但缺乏对模型推理过程的显式引导，导致模型在复杂推理任务中表现不佳。现有方法通常在预训练后才引入强化学习，但此时模型已经形成了固定的模式，难以进行根本性的改变。

**核心思路**：RLP的核心思路是将强化学习融入到预训练阶段，通过奖励模型进行探索性推理。具体来说，RLP将思维链（Chain-of-Thought, CoT）视为一种探索性行为，并根据该思维链对预测未来token的信息增益来计算奖励。这种方法鼓励模型在预测下一个token之前进行独立思考，从而在预训练的早期阶段培养独立的推理能力。

**技术框架**：RLP的整体框架是在标准的语言模型预训练流程中引入一个强化学习的奖励机制。模型首先根据上下文生成一个思维链，然后根据上下文和思维链预测下一个token。奖励信号衡量的是在同时以上下文和一个采样的推理链为条件时，下一个token的对数似然的增加，与仅以上下文为条件相比。这个奖励信号被用来更新模型的参数，鼓励模型生成更有助于预测未来token的思维链。

**关键创新**：RLP最重要的创新在于将强化学习作为预训练目标，而不是仅仅作为后训练的手段。这种方法使得模型能够在预训练阶段就学习到如何进行有效的推理，从而提高了模型在复杂推理任务中的表现。此外，RLP使用信息增益作为奖励信号，避免了对验证器的依赖，使得训练更加高效。

**关键设计**：RLP的关键设计包括：1) 将思维链视为探索性行为；2) 使用信息增益作为奖励信号，具体来说，奖励函数计算的是在给定上下文和思维链的情况下，下一个token的对数似然与仅给定上下文的情况下，下一个token的对数似然之间的差异；3) 将RLP应用于标准的语言模型预训练流程中，无需对模型架构进行修改。

## 📊 实验亮点

RLP在Qwen3-1.7B-Base上进行预训练，在八个基准数学和科学套件的总体平均水平提高了19%。在Nemotron-Nano-12B-v2上，RLP将总体平均水平从42.81%提高到61.32%，并将科学推理的平均水平提高了23%。这些结果表明，RLP可以显著提升模型的推理能力，并且具有良好的可扩展性。

## 🎯 应用场景

RLP具有广泛的应用前景，可以应用于各种需要复杂推理能力的场景，例如数学问题求解、科学推理、代码生成等。通过将强化学习融入预训练阶段，RLP可以显著提升模型在这些任务中的表现，从而提高人工智能系统的智能化水平。未来，RLP还可以与其他技术相结合，例如知识图谱、符号推理等，进一步提升模型的推理能力。

## 📄 摘要（原文）

> The dominant paradigm for training large reasoning models starts with pre-training using next-token prediction loss on vast amounts of data. Reinforcement learning, while powerful in scaling reasoning, is introduced only as the very last phase of post-training, preceded by supervised fine-tuning. While dominant, is this an optimal way of training? In this paper, we present RLP, an information-driven reinforcement pretraining objective, that brings the core spirit of reinforcement learning -- exploration -- to the last phase of pretraining. The key idea is to treat chain-of-thought as an exploratory action, with rewards computed based on the information gain it provides for predicting future tokens. This training objective essentially encourages the model to think for itself before predicting what comes next, thus teaching an independent thinking behavior earlier in the pretraining. More concretely, the reward signal measures the increase in log-likelihood of the next token when conditioning on both context and a sampled reasoning chain, compared to conditioning on context alone. This approach yields a verifier-free dense reward signal, allowing for efficient training for the full document stream during pretraining. Specifically, RLP reframes reinforcement learning for reasoning as a pretraining objective on ordinary text, bridging the gap between next-token prediction and the emergence of useful chain-of-thought reasoning. Pretraining with RLP on Qwen3-1.7B-Base lifts the overall average across an eight-benchmark math-and-science suite by 19%. With identical post-training, the gains compound, with the largest improvements on reasoning-heavy tasks such as AIME25 and MMLU-Pro. Applying RLP to the hybrid Nemotron-Nano-12B-v2 increases the overall average from 42.81% to 61.32% and raises the average on scientific reasoning by 23%, demonstrating scalability across architectures and model sizes.

