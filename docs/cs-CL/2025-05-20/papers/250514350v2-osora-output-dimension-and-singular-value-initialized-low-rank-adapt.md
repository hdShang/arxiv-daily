---
layout: default
title: "OSoRA: Output-Dimension and Singular-Value Initialized Low-Rank Adaptation"
---

# OSoRA: Output-Dimension and Singular-Value Initialized Low-Rank Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14350" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14350v2</a>
  <a href="https://arxiv.org/pdf/2505.14350.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14350v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14350v2', 'OSoRA: Output-Dimension and Singular-Value Initialized Low-Rank Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jialong Han, Si Zhang, Ke Zhang

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-05-21)

---

## 💡 一句话要点

**提出OSoRA以解决大规模语言模型微调的计算资源挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大规模语言模型` `参数高效微调` `低秩适应` `奇异值分解` `计算资源优化`

## 📋 核心要点

1. 现有的参数高效微调方法在大规模语言模型的微调中面临计算资源需求高的问题，限制了其应用。
2. OSoRA通过结合奇异值分解与可学习的缩放向量，提出了一种新的低秩适应方法，优化了微调过程中的参数数量。
3. 实验结果表明，OSoRA在多个基准测试中表现优异，性能与现有最先进方法相当，且在参数扩展上保持线性增长。

## 📝 摘要（中文）

随着大规模语言模型（LLMs）的发展，微调这些模型变得愈加困难，主要是由于其庞大的规模和相关的计算成本。为此，提出了参数高效微调（PEFT）方法作为计算替代方案，但其实现仍需大量资源。本文提出了OSoRA（输出维度和奇异值初始化的低秩适应），这是一种新颖的PEFT方法。OSoRA通过将奇异值分解（SVD）与可学习的缩放向量结合在一个统一框架中，扩展了低秩适应（LoRA）。该方法首先对预训练权重矩阵进行SVD，然后在训练过程中优化输出维度向量，同时保持相应的奇异向量矩阵不变。OSoRA显著减少了微调过程中的计算资源需求，并在数学推理、常识推理等基准测试中表现出与LoRA和VeRA等最先进方法相当或更优的性能，同时在秩增加到更高维度时保持线性参数扩展。消融研究进一步证实了同时训练奇异值和输出维度向量对实现最佳性能的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模语言模型微调过程中的计算资源需求过高的问题。现有的参数高效微调方法虽然有所改进，但仍需大量计算资源，限制了其实际应用。

**核心思路**：OSoRA的核心思路是通过将奇异值分解（SVD）与可学习的输出维度向量结合，优化微调过程中的可训练参数数量，从而降低计算开销。

**技术框架**：OSoRA的整体架构包括两个主要阶段：首先对预训练权重矩阵进行奇异值分解，得到奇异值和奇异向量；然后在训练过程中优化输出维度向量，同时保持奇异向量矩阵不变。

**关键创新**：OSoRA的主要创新在于将奇异值与输出维度向量的联合训练引入低秩适应框架，这一设计显著提高了微调效率，并与现有方法如LoRA和VeRA形成了本质区别。

**关键设计**：在关键设计上，OSoRA采用了固定的奇异向量矩阵和可学习的输出维度向量，损失函数设计上注重于优化输出维度的同时保持奇异值的稳定性，从而实现了高效的参数利用。

## 📊 实验亮点

OSoRA在数学推理和常识推理等多个基准测试中表现出色，性能与LoRA和VeRA等最先进方法相当或更优。同时，OSoRA在参数扩展上保持线性增长，显著降低了微调所需的可训练参数数量，提升了计算效率。

## 🎯 应用场景

OSoRA的研究成果在多个领域具有潜在应用价值，尤其是在需要大规模语言模型的场景中，如自然语言处理、对话系统和智能问答等。通过降低微调过程中的计算资源需求，OSoRA能够使得更多的研究者和开发者能够在资源有限的情况下使用先进的语言模型，推动相关技术的普及与发展。

## 📄 摘要（原文）

> Fine-tuning Large Language Models (LLMs) has become increasingly challenging due to their massive scale and associated computational costs. Parameter-Efficient Fine-Tuning (PEFT) methodologies have been proposed as computational alternatives; however, their implementations still require significant resources. In this paper, we present OSoRA (Output-Dimension and Singular-Value Initialized Low-Rank Adaptation), a novel PEFT method for LLMs. OSoRA extends Low-Rank Adaptation (LoRA) by integrating Singular Value Decomposition (SVD) with learnable scaling vectors in a unified framework. It first performs an SVD of pre-trained weight matrices, then optimizes an output-dimension vector during training, while keeping the corresponding singular vector matrices frozen. OSoRA substantially reduces computational resource requirements by minimizing the number of trainable parameters during fine-tuning. Comprehensive evaluations across mathematical reasoning, common sense reasoning, and other benchmarks demonstrate that OSoRA achieves comparable or superior performance to state-of-the-art methods like LoRA and VeRA, while maintaining a linear parameter scaling even as the rank increases to higher dimensions. Our ablation studies further confirm that jointly training both the singular values and the output-dimension vector is critical for optimal performance.

