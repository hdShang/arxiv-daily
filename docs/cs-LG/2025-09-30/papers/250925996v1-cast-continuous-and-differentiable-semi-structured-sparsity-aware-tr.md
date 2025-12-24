---
layout: default
title: "CAST: Continuous and Differentiable Semi-Structured Sparsity-Aware Training for Large Language Models"
---

# CAST: Continuous and Differentiable Semi-Structured Sparsity-Aware Training for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25996" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25996v1</a>
  <a href="https://arxiv.org/pdf/2509.25996.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25996v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25996v1', 'CAST: Continuous and Differentiable Semi-Structured Sparsity-Aware Training for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiyu Huang, Yuezhou Hu, Jun Zhu, Jianfei Chen

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-30

**备注**: Submitted to IEEE TPAMI

---

## 💡 一句话要点

**提出CAST框架，实现大语言模型半结构化稀疏训练，提升推理效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `稀疏训练` `半结构化稀疏` `知识蒸馏` `模型压缩`

## 📋 核心要点

1. 现有稀疏训练方法通常分离稀疏模式和权重的优化，导致训练效率低下，难以充分挖掘稀疏潜力。
2. CAST框架通过AdamS优化器、权重缩放和知识蒸馏，实现了稀疏模式和权重的连续联合优化，提升训练效率。
3. 实验表明，CAST在多个模型上显著提升困惑度和零样本准确率，尤其在LLaMA2-7B上表现出色，仅用少量资源即可接近密集模型性能。

## 📝 摘要（中文）

本文提出了一种名为连续自适应稀疏训练器（CAST）的框架，用于大语言模型（LLMs）的完全连续且可微的半结构化（或“N:M”）稀疏训练。与以往分别优化稀疏模式和权重的方法不同，CAST实现了训练期间的无缝联合优化，同时逐步将模型转换为所需的稀疏格式。CAST引入了三个关键组件：AdamS（一种稀疏感知优化器，利用自适应L1衰减来促进所有参数的均匀稀疏化）、权重缩放（旨在减轻衰减引起的幅度减小，同时保留所需的稀疏模式）和知识蒸馏（利用密集模型作为自教师来提高训练效率）。在125M到13B参数的多个模型系列中，我们在2:4稀疏模式下评估了CAST。结果表明，与之前的最先进方法相比，在困惑度和零样本准确率方面都有显著提高，且仅需极少的训练资源。值得注意的是，在LLaMA2-7B上，我们的2:4稀疏模型仅使用原始预训练tokens的2%，就实现了可忽略不计的0.09的困惑度增加和0.36%的零样本准确率提升。此外，我们建立了一个准确而稳健的经验缩放定律，以预测给定足够训练资源的稀疏模型性能。最后，我们通过在量化和微调场景下评估我们的稀疏模型，证明了它们的实际适用性。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型稀疏训练中，稀疏模式和权重分离优化导致的训练效率低下的问题。现有方法通常需要交替进行稀疏模式选择和权重更新，无法实现端到端的优化，限制了稀疏模型的性能。

**核心思路**：论文的核心思路是设计一个完全连续且可微的稀疏训练框架，允许稀疏模式和权重在训练过程中进行联合优化。通过引入自适应L1衰减、权重缩放和知识蒸馏等技术，实现模型向目标稀疏格式的平滑过渡，并保持模型的性能。

**技术框架**：CAST框架包含三个主要模块：1) AdamS优化器：使用自适应L1衰减来促进参数的均匀稀疏化。2) 权重缩放：补偿L1衰减导致的权重幅度减小，保持稀疏模式的稳定性。3) 知识蒸馏：利用密集模型作为教师模型，指导稀疏模型的训练，提高训练效率和模型性能。整个训练过程是端到端的，稀疏模式和权重同步更新。

**关键创新**：CAST的关键创新在于实现了稀疏模式和权重的连续联合优化。与以往方法相比，CAST无需交替进行稀疏模式选择和权重更新，而是通过可微的方式，在训练过程中逐步调整稀疏模式，从而更有效地利用稀疏性。此外，AdamS优化器和权重缩放模块的设计，保证了稀疏训练的稳定性和有效性。

**关键设计**：AdamS优化器采用自适应L1衰减，对不同参数应用不同的衰减率，以实现更均匀的稀疏化。权重缩放模块通过对权重进行缩放，补偿L1衰减导致的幅度减小，保持稀疏模式的稳定性。知识蒸馏采用密集模型作为教师模型，使用KL散度等损失函数，指导稀疏模型的训练。具体的L1衰减系数、缩放因子等超参数需要根据具体模型和数据集进行调整。

## 📊 实验亮点

实验结果表明，CAST框架在多个模型（125M到13B参数）上实现了显著的性能提升。例如，在LLaMA2-7B模型上，使用2:4稀疏模式，仅使用2%的原始预训练tokens，就实现了与密集模型几乎相同的困惑度（0.09的增加）和更高的零样本准确率（0.36%的提升）。这表明CAST框架能够有效地训练高性能的稀疏模型，并显著降低训练成本。

## 🎯 应用场景

CAST框架可应用于各种大语言模型的稀疏化，降低模型推理的计算和存储成本，使其更容易部署在资源受限的设备上，例如移动设备和边缘服务器。该技术还有助于加速模型的微调和推理，提高用户体验，并推动大语言模型在更多实际场景中的应用。

## 📄 摘要（原文）

> Sparsity-aware training is an effective approach for transforming large language models (LLMs) into hardware-friendly sparse patterns, thereby reducing latency and memory consumption during inference. In this paper, we propose Continuous Adaptive Sparse Trainer (CAST), a fully continuous and differentiable sparsity-aware training framework for semi-structured (or "N:M") sparse models. Unlike previous approaches that optimize sparsity patterns and weights separately, CAST enables seamless joint optimization during training, while progressively transforming the model into the desired sparsity format. Specifically, CAST introduces three key components: 1) AdamS, a sparsity-aware optimizer that leverages adaptive L1 decay to promote uniform sparsification across all parameters; 2) Weight Scaling, a module designed to mitigate the magnitude reduction caused by decay while preserving desired sparsity patterns; 3) Knowledge Distillation, which employs the dense model as a self-teacher to enhance training efficiency. We evaluate CAST under 2:4 sparsity patterns across multiple model families, ranging from 125M to 13B parameters. Our results demonstrate significant improvements over previous state-of-the-art methods in both perplexity and zero-shot accuracy with minimal training resources. Notably, on LLaMA2-7B, our 2:4 sparse model achieves a negligible perplexity increase of 0.09 and a 0.36% gain in zero-shot accuracy compared to the dense model using only 2% of the original pretraining tokens. Additionally, we establish an accurate and robust empirical scaling law to predict sparse model performance given adequate training resources. Finally, we demonstrate the practical applicability of our sparse models by evaluating them under quantization and fine-tuning scenarios.

