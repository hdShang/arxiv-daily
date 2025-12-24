---
layout: default
title: "All for One: LLMs Solve Mental Math at the Last Token With Information Transferred From Other Tokens"
---

# All for One: LLMs Solve Mental Math at the Last Token With Information Transferred From Other Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09650" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09650v1</a>
  <a href="https://arxiv.org/pdf/2509.09650.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09650v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09650v1', 'All for One: LLMs Solve Mental Math at the Last Token With Information Transferred From Other Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siddarth Mamidanna, Daking Rai, Ziyu Yao, Yilun Zhou

**分类**: cs.CL

**发布日期**: 2025-09-11

**备注**: EMNLP 2025 Main Conference

---

## 💡 一句话要点

**提出All-for-One子图，使LLM仅用末尾token计算解决心算问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `心算任务` `信息传递` `计算路径` `模型可解释性`

## 📋 核心要点

1. 大型语言模型在计算任务中表现出色，但其内部计算机制尚不明确，需要深入研究。
2. 论文提出All-for-One (AF1)子图，通过CAMA和ABP技术，限制计算发生在最后一个token，简化计算过程。
3. 实验表明AF1子图对于心算任务的高性能至关重要，且具有跨模型和输入风格的泛化能力。

## 📝 摘要（中文）

大型语言模型(LLM)在众多计算任务中表现出卓越的能力，但其内部运作机制仍不清楚。理论上，因果自注意力机制和多层感知机层的结合使得每个token都能访问并计算基于所有先前token的信息。实际上，这种操作在多大程度上存在？在本文中，针对心算任务（即通过下一个token预测直接进行数学计算，而无需显式推理），我们分三个步骤研究这个问题：抑制初始层中特定于输入的token计算，限制接下来几层中跨token位置的信息传递路径，并强制所有计算在剩余层中的最后一个token处发生。通过两种提出的技术，上下文感知平均消融(CAMA)和基于注意力的窥视(ABP)，我们识别出一个All-for-One子图(AF1)，该子图在各种心算任务上具有很高的准确性，其中有意义的计算发生在非常晚的层（就层深度而言），并且仅发生在最后一个token处，该token接收来自特定中间层中其他token的信息。在各种模型和算术表达式上的实验表明，该子图对于高模型性能是充分且必要的，可以在不同的模型之间转移，并且适用于各种输入样式。对不同CAMA和ABP替代方案的消融实验揭示了它们相对于其他方法的独特优势，这些优势可能具有独立的意义。

## 🔬 方法详解

**问题定义**：论文旨在探究大型语言模型在执行心算任务时，信息如何在不同token之间传递和计算。现有方法通常将LLM视为黑盒，缺乏对内部计算过程的细粒度理解，难以解释其能力来源。论文希望通过实验手段揭示LLM在心算任务中的关键计算路径和信息传递模式。

**核心思路**：论文的核心思路是通过逐步限制LLM的计算能力，最终将所有计算集中在最后一个token上。通过这种方式，可以识别出对于心算任务至关重要的信息传递路径和计算模块，从而揭示LLM解决心算问题的关键机制。这种方法类似于“剥洋葱”，逐步去除不必要的计算，最终留下核心的计算路径。

**技术框架**：论文的技术框架主要包括三个阶段：1) 抑制初始层中特定于输入的token计算；2) 限制中间层中跨token位置的信息传递路径；3) 强制所有计算在剩余层中的最后一个token处发生。为了实现这些目标，论文提出了两种关键技术：Context-Aware Mean Ablation (CAMA) 和 Attention-Based Peeking (ABP)。CAMA用于抑制不必要的token计算，ABP用于控制信息在不同token之间的传递。

**关键创新**：论文的关键创新在于提出了All-for-One (AF1)子图的概念，并证明了该子图对于心算任务的高性能至关重要。AF1子图表明，LLM在解决心算问题时，并非所有token都参与计算，而是将大部分计算集中在最后一个token上，并通过特定的信息传递路径将其他token的信息传递给最后一个token。这种计算模式与传统的分布式计算模式不同，揭示了LLM在特定任务中的高效计算策略。

**关键设计**：CAMA通过计算每个token在不同上下文中的平均激活值，并将其作为消融的基准，从而实现对不必要token计算的抑制。ABP通过修改注意力机制，允许最后一个token“窥视”其他token的信息，但限制其他token之间的信息传递。这些技术细节的设计旨在精确控制LLM的计算过程，从而识别出AF1子图。

## 📊 实验亮点

实验结果表明，All-for-One (AF1)子图对于心算任务的高性能是充分且必要的。在各种模型和算术表达式上的实验表明，AF1子图可以在不同的模型之间转移，并且适用于各种输入样式。消融实验表明，CAMA和ABP技术相对于其他方法具有独特的优势，能够更有效地识别关键计算路径。

## 🎯 应用场景

该研究成果可应用于提升LLM的计算效率和可解释性。通过理解LLM在特定任务中的关键计算路径，可以设计更高效的模型结构和训练方法。此外，该研究也有助于开发更可靠的LLM，避免模型过度依赖某些token或计算路径，从而提高模型的鲁棒性和泛化能力。该研究对于开发轻量级、高效的LLM具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs) demonstrate proficiency across numerous computational tasks, yet their inner workings remain unclear. In theory, the combination of causal self-attention and multilayer perceptron layers allows every token to access and compute information based on all preceding tokens. In practice, to what extent are such operations present? In this paper, on mental math tasks (i.e., direct math calculation via next-token prediction without explicit reasoning), we investigate this question in three steps: inhibiting input-specific token computations in the initial layers, restricting the routes of information transfer across token positions in the next few layers, and forcing all computation to happen at the last token in the remaining layers. With two proposed techniques, Context-Aware Mean Ablation (CAMA) and Attention-Based Peeking (ABP), we identify an All-for-One subgraph (AF1) with high accuracy on a wide variety of mental math tasks, where meaningful computation occurs very late (in terms of layer depth) and only at the last token, which receives information of other tokens in few specific middle layers. Experiments on a variety of models and arithmetic expressions show that this subgraph is sufficient and necessary for high model performance, transfers across different models, and works on a variety of input styles. Ablations on different CAMA and ABP alternatives reveal their unique advantages over other methods, which may be of independent interest.

