---
layout: default
title: "Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights"
---

# Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16406" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16406v1</a>
  <a href="https://arxiv.org/pdf/2506.16406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16406v1', 'Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiyuan Liang, Dongwen Tang, Yuhao Zhou, Xuanlei Zhao, Mingjia Shi, Wangbo Zhao, Zekai Li, Peihao Wang, Konstantin Schürholt, Damian Borth, Michael M. Bronstein, Yang You, Zhangyang Wang, Kai Wang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-19

**备注**: We propose a method that can generate LoRA parameters in seconds

**🔗 代码/项目**: [PROJECT_PAGE](https://jerryliang24.github.io/DnD)

---

## 💡 一句话要点

**提出Drag-and-Drop LLMs以解决大语言模型定制的高成本问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `低秩适应` `提示条件生成` `跨领域泛化` `大语言模型定制`

## 📋 核心要点

1. 现有的参数高效微调方法仍需为每个下游任务进行单独的优化，导致高昂的时间和计算成本。
2. DnD通过提示条件的参数生成，直接将未标记的任务提示映射到LoRA权重更新，消除了每个任务的训练需求。
3. 实验结果显示，DnD在性能上比最强的LoRA训练方法提升了30%，并且在未见数据上具有良好的泛化能力。

## 📝 摘要（中文）

现代参数高效微调（PEFT）方法如低秩适应（LoRA）虽然降低了定制大型语言模型（LLMs）的成本，但仍需针对每个下游数据集进行单独的优化。本文提出了Drag-and-Drop LLMs（DnD），一种基于提示的参数生成器，通过将少量未标记的任务提示直接映射到LoRA权重更新，消除了每个任务的训练需求。DnD在多样化的提示-检查点对上训练后，能够在几秒内生成特定任务的参数，表现出高达12,000倍的低开销和在未见的常识推理、数学、编码及多模态基准上平均提升30%的性能，且在跨领域泛化方面表现稳健。我们的结果表明，基于提示的参数生成是快速专门化LLMs的可行替代方案。

## 🔬 方法详解

**问题定义**：当前的参数高效微调方法如LoRA虽然降低了定制LLMs的成本，但仍需为每个下游任务进行单独的优化，导致时间和计算资源的浪费。

**核心思路**：DnD的核心思想是通过提示条件生成参数，直接将少量未标记的任务提示映射到LoRA权重更新，从而消除每个任务的训练过程。

**技术框架**：DnD的整体架构包括一个轻量级文本编码器和一个级联的超卷积解码器。文本编码器将每个提示批次提炼为条件嵌入，解码器则将这些嵌入转换为完整的LoRA矩阵。

**关键创新**：DnD的主要创新在于其提示条件的参数生成方法，这一方法与传统的基于梯度的适应方法本质上不同，能够快速生成任务特定的参数。

**关键设计**：DnD的设计包括对提示的编码和解码过程，使用了特定的损失函数和网络结构，以确保生成的LoRA矩阵能够有效提升模型在特定任务上的性能。通过在多样化的提示-检查点对上进行训练，DnD能够实现快速的参数生成。

## 📊 实验亮点

DnD在实验中显示出高达12,000倍的低开销，相较于传统的全微调方法，且在未见的常识推理、数学、编码和多模态基准上平均提升了30%的性能。这些结果表明DnD在跨领域泛化能力上也表现出色，尽管从未见过目标数据或标签。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和多模态学习等。DnD的快速参数生成能力使得在不同任务上定制大型语言模型变得更加高效，降低了开发成本，提升了模型的适应性和实用性，未来可能在商业和学术界产生深远影响。

## 📄 摘要（原文）

> Modern Parameter-Efficient Fine-Tuning (PEFT) methods such as low-rank adaptation (LoRA) reduce the cost of customizing large language models (LLMs), yet still require a separate optimization run for every downstream dataset. We introduce \textbf{Drag-and-Drop LLMs (\textit{DnD})}, a prompt-conditioned parameter generator that eliminates per-task training by mapping a handful of unlabeled task prompts directly to LoRA weight updates. A lightweight text encoder distills each prompt batch into condition embeddings, which are then transformed by a cascaded hyper-convolutional decoder into the full set of LoRA matrices. Once trained in a diverse collection of prompt-checkpoint pairs, DnD produces task-specific parameters in seconds, yielding i) up to \textbf{12,000$\times$} lower overhead than full fine-tuning, ii) average gains up to \textbf{30\%} in performance over the strongest training LoRAs on unseen common-sense reasoning, math, coding, and multimodal benchmarks, and iii) robust cross-domain generalization despite never seeing the target data or labels. Our results demonstrate that prompt-conditioned parameter generation is a viable alternative to gradient-based adaptation for rapidly specializing LLMs. Our project is available at \href{https://jerryliang24.github.io/DnD}{https://jerryliang24.github.io/DnD}.

