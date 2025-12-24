---
layout: default
title: "StateX: Enhancing RNN Recall via Post-training State Expansion"
---

# StateX: Enhancing RNN Recall via Post-training State Expansion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22630" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22630v1</a>
  <a href="https://arxiv.org/pdf/2509.22630.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22630v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22630v1', 'StateX: Enhancing RNN Recall via Post-training State Expansion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingyu Shen, Yingfa Chen, Zhen Leng Thai, Xu Han, Zhiyuan Liu, Maosong Sun

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**StateX：通过后训练状态扩展增强RNN的召回能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `循环神经网络` `RNN` `状态空间模型` `线性注意力` `后训练` `模型扩展` `长文本建模`

## 📋 核心要点

1. Transformer模型处理长文本成本高，而RNN虽然复杂度低，但在长文本信息召回方面存在困难。
2. StateX通过后训练扩展预训练RNN的状态，在不显著增加参数量的前提下，提升模型容量。
3. 实验结果表明，StateX能有效提升RNN的召回能力和上下文学习能力，且后训练成本较低。

## 📝 摘要（中文）

Transformer模型在语言建模方面表现出色，但其高复杂度导致处理长上下文时成本高昂。相比之下，线性注意力和状态空间模型等循环神经网络（RNN）因其恒定的单token复杂度而备受欢迎。然而，这些循环模型在需要准确回忆长上下文信息的任务中表现不佳，因为所有上下文信息都被压缩到固定大小的循环状态中。以往研究表明，召回能力与循环状态大小呈正相关，但直接训练具有较大循环状态的RNN会导致高昂的训练成本。本文提出了StateX，一种通过后训练有效扩展预训练RNN状态的训练流程。针对线性注意力和状态空间模型这两种流行的RNN，我们设计了后训练架构修改，以扩展状态大小，而模型参数几乎没有增加。在高达13亿参数的模型上的实验表明，StateX有效地增强了RNN的召回和上下文学习能力，而不会产生高昂的后训练成本或损害其他能力。

## 🔬 方法详解

**问题定义**：RNN在处理长文本时，需要将所有上下文信息压缩到固定大小的循环状态中，这导致信息损失，尤其是在需要准确回忆长上下文信息的任务中，召回能力不足。直接增大RNN的状态大小可以提升召回能力，但会显著增加训练成本。

**核心思路**：StateX的核心思路是在预训练的RNN基础上，通过后训练的方式扩展其状态大小，从而提升模型的召回能力，同时避免从头训练大状态RNN带来的高昂成本。这种方法旨在利用预训练模型已经学习到的知识，并在此基础上进行高效的状态扩展。

**技术框架**：StateX的整体流程包括以下几个阶段：1) 使用较小的状态大小预训练RNN模型；2) 设计特定的架构修改，以在后训练阶段扩展RNN的状态大小，同时尽可能减少参数量的增加；3) 使用少量数据对扩展后的模型进行后训练，以使其适应更大的状态空间。该框架针对线性注意力和状态空间模型等特定类型的RNN进行了优化。

**关键创新**：StateX的关键创新在于提出了一种高效的后训练状态扩展方法，能够在不显著增加模型参数量的情况下，有效提升RNN的召回能力。与直接训练大状态RNN相比，StateX大大降低了训练成本。此外，StateX还针对不同类型的RNN（如线性注意力和状态空间模型）设计了特定的架构修改方案。

**关键设计**：StateX的关键设计包括：1) 针对线性注意力和状态空间模型，设计了特定的状态扩展架构修改方案，例如，可以通过增加线性注意力头的数量或扩展状态空间模型的维度来实现状态扩展；2) 在后训练阶段，使用少量数据进行微调，以使模型适应更大的状态空间，并保持其原有的性能；3) 在扩展状态时，尽量保持模型参数量的稳定，以避免引入过多的计算负担。

## 📊 实验亮点

StateX在高达13亿参数的模型上进行了实验，结果表明，该方法能够有效提升RNN的召回能力和上下文学习能力，而不会产生高昂的后训练成本或损害其他能力。具体性能提升数据和对比基线信息在原文中未明确给出，属于未知信息。

## 🎯 应用场景

StateX技术可应用于各种需要处理长文本序列的任务，例如长文档摘要、对话系统、代码生成等。通过提升RNN的召回能力，可以提高这些应用在处理长上下文信息时的准确性和效率。该技术还有助于降低长序列建模的计算成本，使得资源受限的设备也能运行复杂的语言模型。

## 📄 摘要（原文）

> While Transformer-based models have demonstrated remarkable language modeling performance, their high complexities result in high costs when processing long contexts. In contrast, recurrent neural networks (RNNs) such as linear attention and state space models have gained popularity due to their constant per-token complexities. However, these recurrent models struggle with tasks that require accurate recall of contextual information from long contexts, because all contextual information is compressed into a constant-size recurrent state. Previous works have shown that recall ability is positively correlated with the recurrent state size, yet directly training RNNs with larger recurrent states results in high training costs. In this paper, we introduce StateX, a training pipeline for efficiently expanding the states of pre-trained RNNs through post-training. For two popular classes of RNNs, linear attention and state space models, we design post-training architectural modifications to scale up the state size with no or negligible increase in model parameters. Experiments on models up to 1.3B parameters demonstrate that StateX efficiently enhances the recall and in-context learning ability of RNNs without incurring high post-training costs or compromising other capabilities.

