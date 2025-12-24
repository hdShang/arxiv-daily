---
layout: default
title: "DenseLoRA: Dense Low-Rank Adaptation of Large Language Models"
---

# DenseLoRA: Dense Low-Rank Adaptation of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23808" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23808v1</a>
  <a href="https://arxiv.org/pdf/2505.23808.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23808v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23808v1', 'DenseLoRA: Dense Low-Rank Adaptation of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lin Mu, Xiaoyu Wang, Li Ni, Yang Li, Zhize Wu, Peiquan Jin, Yiwen Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27

**🔗 代码/项目**: [GITHUB](https://github.com/mulin-ahu/DenseLoRA)

---

## 💡 一句话要点

**提出DenseLoRA以提高大语言模型的参数效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低秩适应` `大语言模型` `参数效率` `模型微调` `自然语言处理` `深度学习`

## 📋 核心要点

1. 现有的低秩适应方法存在冗余权重，导致参数利用效率低下，影响模型性能。
2. DenseLoRA通过引入单个编码器-解码器来精炼和压缩隐藏表示，使用密集低秩矩阵替代冗余的低秩矩阵。
3. 在LLaMA3-8B基准上，DenseLoRA实现了83.8%的准确率，且可训练参数仅为0.01%，显著优于LoRA的80.8%准确率和0.70%参数。

## 📝 摘要（中文）

低秩适应（LoRA）被开发为一种高效的适应大型语言模型（LLMs）的方法，通过微调两个低秩矩阵来减少可训练参数的数量。然而，先前研究表明，这些矩阵中的许多权重是冗余的，导致参数利用效率低下。为了解决这一限制，我们提出了Dense Low-Rank Adaptation（DenseLoRA），这是一种新颖的方法，能够在提高参数效率的同时，超越LoRA的性能。DenseLoRA基于表示微调的概念，结合单个编码器-解码器在应用适应之前，精炼和压缩所有适应层的隐藏表示。与LoRA依赖于两个冗余低秩矩阵不同，DenseLoRA通过一个密集低秩矩阵来适应LLMs，从而提高了参数利用率和适应效率。我们在多个基准上评估DenseLoRA，结果显示其在仅使用0.01%的可训练参数时达到了83.8%的准确率，而LoRA在0.70%的可训练参数下仅达到了80.8%的准确率。此外，我们进行了广泛的实验，以系统评估DenseLoRA各组件对整体模型性能的影响。代码可在https://github.com/mulin-ahu/DenseLoRA获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有低秩适应方法中冗余权重导致的参数利用效率低下问题。传统的LoRA方法依赖于两个低秩矩阵，造成了不必要的冗余。

**核心思路**：DenseLoRA的核心思想是通过引入单个编码器-解码器来精炼和压缩隐藏表示，使用一个密集低秩矩阵进行适应，从而提高参数利用率和适应效率。

**技术框架**：DenseLoRA的整体架构包括一个编码器-解码器模块，该模块在适应层之前处理隐藏表示，随后通过密集低秩矩阵进行适应。主要模块包括表示精炼、压缩和适应过程。

**关键创新**：DenseLoRA的主要创新在于使用单个密集低秩矩阵替代冗余的两个低秩矩阵，显著提高了参数的利用效率和模型的适应性能。

**关键设计**：在DenseLoRA中，关键的参数设置和网络结构设计包括编码器-解码器的层数、低秩矩阵的维度选择以及损失函数的优化策略，这些设计共同促进了模型性能的提升。

## 📊 实验亮点

DenseLoRA在LLaMA3-8B基准上实现了83.8%的准确率，仅使用0.01%的可训练参数，相较于LoRA的80.8%准确率和0.70%参数，提升显著。这表明DenseLoRA在参数效率和模型性能方面具有明显优势。

## 🎯 应用场景

DenseLoRA的研究成果在自然语言处理、对话系统和文本生成等领域具有广泛的应用潜力。通过提高大语言模型的参数效率，该方法能够在资源受限的环境中实现更高效的模型训练和推理，推动智能应用的发展。

## 📄 摘要（原文）

> Low-rank adaptation (LoRA) has been developed as an efficient approach for adapting large language models (LLMs) by fine-tuning two low-rank matrices, thereby reducing the number of trainable parameters. However, prior research indicates that many of the weights in these matrices are redundant, leading to inefficiencies in parameter utilization. To address this limitation, we introduce Dense Low-Rank Adaptation (DenseLoRA), a novel approach that enhances parameter efficiency while achieving superior performance compared to LoRA. DenseLoRA builds upon the concept of representation fine-tuning, incorporating a single Encoder-Decoder to refine and compress hidden representations across all adaptation layers before applying adaptation. Instead of relying on two redundant low-rank matrices as in LoRA, DenseLoRA adapts LLMs through a dense low-rank matrix, improving parameter utilization and adaptation efficiency. We evaluate DenseLoRA on various benchmarks, showing that it achieves 83.8% accuracy with only 0.01% of trainable parameters, compared to LoRA's 80.8% accuracy with 0.70% of trainable parameters on LLaMA3-8B. Additionally, we conduct extensive experiments to systematically assess the impact of DenseLoRA's components on overall model performance. Code is available at https://github.com/mulin-ahu/DenseLoRA.

