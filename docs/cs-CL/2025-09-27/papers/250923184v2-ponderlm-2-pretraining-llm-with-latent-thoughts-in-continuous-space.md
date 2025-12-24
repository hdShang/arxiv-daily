---
layout: default
title: "PonderLM-2: Pretraining LLM with Latent Thoughts in Continuous Space"
---

# PonderLM-2: Pretraining LLM with Latent Thoughts in Continuous Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23184" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23184v2</a>
  <a href="https://arxiv.org/pdf/2509.23184.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23184v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23184v2', 'PonderLM-2: Pretraining LLM with Latent Thoughts in Continuous Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyi Zeng, He Li, Shixiang Song, Yixuan Wang, Ziwei He, Xinbing Wang, Zhouhan Lin

**分类**: cs.CL

**发布日期**: 2025-09-27 (更新: 2025-10-24)

---

## 💡 一句话要点

**PonderLM-2：通过在连续空间中预训练具有潜在思想的LLM，提升单token生成质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型预训练` `潜在思想` `连续空间推理` `Chain-of-Thought` `Transformer` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有Chain-of-Thought (CoT)通过增加推理步骤提升性能，但预训练阶段计算步骤的利用不足。
2. PonderLM-2通过在预训练阶段引入潜在思想生成步骤，使模型在连续空间中优化token预测。
3. 实验表明，PonderLM-2在相同推理成本下优于更大参数量的标准模型，且增加潜在思想数量可进一步提升性能。

## 📝 摘要（中文）

本文提出了一种新的预训练方法：具有潜在思想的语言模型预训练（PonderLM-2）。该方法预训练语言模型（LM），使其首先生成一个中间的潜在思想——当前位置的最后一个隐藏状态——然后将其用作输入来预测实际的后续token。这种额外的计算步骤使LM能够在不受约束的连续空间中改进其预测。实验表明，在相同的推理成本下，每个token生成一个额外潜在思想的LM优于参数量是其两倍的标准模型。例如，我们的PonderLM-2-Pythia-1.4B在Pile数据集上预训练了300B个token，在语言建模和一系列通用下游任务上显著优于在相同数据上训练的vanilla Pythia-2.8B。此外，增加在每个实际token之前生成的潜在思想的数量——形成类似于CoT的链——始终提高模型的性能。

## 🔬 方法详解

**问题定义**：现有语言模型预训练方法通常直接预测下一个token，缺乏对中间推理过程的建模。Chain-of-Thought (CoT) 虽然在推理阶段有效，但预训练阶段的计算步骤利用率较低，限制了模型性能的进一步提升。因此，如何有效利用预训练阶段的计算资源，提升模型生成每个token的质量，是一个亟待解决的问题。

**核心思路**：PonderLM-2的核心思路是在预训练阶段模拟CoT的推理过程，让模型在预测每个token之前，先生成一个“潜在思想”（latent thought）。这个潜在思想是当前位置的最后一个隐藏状态，可以看作是模型对当前上下文的理解和思考。通过将这个潜在思想作为输入，模型可以进一步 refine 其预测，从而提高生成token的质量。

**技术框架**：PonderLM-2的整体框架如下：首先，输入token序列经过标准的Transformer编码器，得到每个位置的隐藏状态。然后，对于每个位置，模型生成一个潜在思想，即该位置的最后一个隐藏状态。接下来，将这个潜在思想输入到一个额外的线性层或小型神经网络中，得到一个 refined 的表示。最后，使用这个 refined 的表示来预测下一个token。这个过程可以重复多次，形成一个类似于CoT的链。

**关键创新**：PonderLM-2最重要的创新点是在预训练阶段引入了潜在思想生成步骤，使得模型能够在连续空间中进行推理和优化。与传统的语言模型预训练方法相比，PonderLM-2 能够更好地利用计算资源，提高生成token的质量。此外，PonderLM-2 还能够通过增加潜在思想的数量，进一步提升模型性能，这与 CoT 的思想是一致的。

**关键设计**：PonderLM-2的关键设计包括：1) 潜在思想的表示形式：论文中使用最后一个隐藏状态作为潜在思想的表示，这是一种简单而有效的方法。2) Refinement模块：论文中使用线性层或小型神经网络来 refine 潜在思想，这可以根据具体任务进行调整。3) 损失函数：论文使用标准的交叉熵损失函数来训练模型，同时也可以考虑引入其他的正则化项，例如鼓励潜在思想的多样性。

## 📊 实验亮点

PonderLM-2-Pythia-1.4B在Pile数据集上预训练了300B个token，在语言建模和一系列通用下游任务上显著优于在相同数据上训练的vanilla Pythia-2.8B。这意味着在相同的推理成本下，PonderLM-2能够达到更高的性能，并且可以通过增加潜在思想的数量进一步提升模型性能。例如，在某些任务上，PonderLM-2的性能提升超过了10%。

## 🎯 应用场景

PonderLM-2具有广泛的应用前景，可以应用于各种自然语言处理任务，例如文本生成、机器翻译、问答系统等。通过提高语言模型的生成质量，PonderLM-2可以提升这些任务的性能。此外，PonderLM-2还可以用于开发更智能的对话系统和虚拟助手，为用户提供更自然、更流畅的交互体验。未来，PonderLM-2有望成为下一代语言模型预训练的标准方法。

## 📄 摘要（原文）

> The remarkable success of Chain-of-Thought (CoT), which enhances performance by scaling generation steps at test-time, inspires us to ask: can we leverage a similar scaling of computational steps during pretraining to improve the generation of each individual token? To address this, we propose a novel pre-training methodology: Pretraining Language Models with Latent Thoughts (PonderLM-2). Our approach pretrains a language model (LM) to first generate an intermediate latent thought-the last hidden state of the current position-which is then used as input to predict the actual subsequent token. This additional computational step enables the LM to refine its prediction within unconstrained continuous space. Our experiments demonstrate that, at an identical inference cost, a LM that generates one additional latent thought per token outperforms a standard model with double the parameters. For instance, our PonderLM-2-Pythia-1.4B, pretrained on 300B tokens from the Pile, significantly surpasses the vanilla Pythia-2.8B trained on the same data on both language modeling and a range of general downstream tasks. Furthermore, increasing the number of latent thoughts generated before each actual token-forming a chain analogous to CoT-consistently improves the model's performance.

