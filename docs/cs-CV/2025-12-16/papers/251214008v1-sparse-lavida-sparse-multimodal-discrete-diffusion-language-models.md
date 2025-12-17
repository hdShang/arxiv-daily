---
layout: default
title: Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models
---

# Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14008" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14008v1</a>
  <a href="https://arxiv.org/pdf/2512.14008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14008v1" onclick="toggleFavorite(this, '2512.14008v1', 'Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shufan Li, Jiuxiang Gu, Kangning Liu, Zhe Lin, Zijun Wei, Aditya Grover, Jason Kuen

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 18 pages (12 pages for the main paper and 6 pages for the appendix), 9 figures

---

## 💡 一句话要点

**Sparse-LaViDa：通过稀疏化采样加速多模态离散扩散语言模型推理。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态扩散模型` `稀疏采样` `模型加速` `图像生成` `图像编辑`

## 📋 核心要点

1. MDM推理速度受限于重复处理冗余masked tokens，效率有待提升。
2. Sparse-LaViDa动态截断不必要的masked tokens，并用register tokens保持生成质量。
3. 通过专门设计的attention mask，Sparse-LaViDa保证训练与推理过程的一致性。

## 📝 摘要（中文）

本文提出了一种名为Sparse-LaViDa的新建模框架，旨在加速Masked Discrete Diffusion Models (MDMs)的推理过程。MDMs在图像理解、生成和编辑等多种多模态任务中表现出色，但由于需要在每个采样步骤中重复处理冗余的masked tokens，其推理速度仍有优化空间。Sparse-LaViDa通过在每个推理步骤中动态截断不必要的masked tokens来加速MDM采样。为了保持生成质量，引入了专门的register tokens，作为被截断tokens的紧凑表示。此外，为了确保训练和推理之间的一致性，设计了一种专门的attention mask，在训练期间忠实地匹配截断的采样过程。基于最先进的统一MDM LaViDa-O，Sparse-LaViDa在文本到图像生成、图像编辑和数学推理等多种任务中实现了高达2倍的加速，同时保持了生成质量。

## 🔬 方法详解

**问题定义**：Masked Discrete Diffusion Models (MDMs) 在多模态任务中表现出色，但推理速度较慢，主要原因是需要在每个采样步骤中重复处理大量的masked tokens。这些masked tokens在早期阶段可能对最终结果贡献不大，但仍然需要消耗计算资源。因此，如何减少冗余计算，加速MDM的推理过程是一个关键问题。

**核心思路**：Sparse-LaViDa的核心思路是在推理过程中动态地截断那些对生成结果影响较小的masked tokens，从而减少计算量。为了弥补截断tokens带来的信息损失，引入了register tokens作为被截断tokens的紧凑表示。这些register tokens能够保留被截断tokens的关键信息，从而保证生成质量。

**技术框架**：Sparse-LaViDa建立在现有的MDM框架LaViDa-O之上。其主要流程如下：1) 在每个采样步骤中，模型首先评估每个masked token的重要性。2) 根据重要性评估结果，截断一部分不重要的masked tokens。3) 使用register tokens来表示被截断的tokens。4) 使用修改后的attention机制，将register tokens的信息融入到剩余的tokens中。5) 重复以上步骤，直到生成最终结果。

**关键创新**：Sparse-LaViDa的关键创新在于动态截断机制和register tokens的使用。动态截断机制能够有效地减少计算量，而register tokens能够保证生成质量。此外，为了保证训练和推理的一致性，论文还设计了一种专门的attention mask，在训练期间模拟截断过程。

**关键设计**：论文中register tokens的设计是一个关键细节。register tokens需要能够有效地表示被截断tokens的信息，同时不能引入过多的计算负担。论文中可能采用了某种pooling或者attention机制来生成register tokens。此外，attention mask的设计也至关重要，它需要保证模型在训练期间能够学习到如何处理被截断的tokens。

## 📊 实验亮点

Sparse-LaViDa在多种任务上实现了显著的加速效果，同时保持了生成质量。例如，在文本到图像生成任务中，Sparse-LaViDa实现了高达2倍的加速。实验结果表明，Sparse-LaViDa能够有效地减少冗余计算，提高MDM的推理效率，而不会显著降低生成质量。

## 🎯 应用场景

Sparse-LaViDa具有广泛的应用前景，包括文本到图像生成、图像编辑、视频生成、机器人控制等。通过加速MDM的推理过程，Sparse-LaViDa可以降低计算成本，提高用户体验，并促进多模态人工智能技术的发展。该方法在资源受限的设备上部署大型多模态模型具有重要意义。

## 📄 摘要（原文）

> Masked Discrete Diffusion Models (MDMs) have achieved strong performance across a wide range of multimodal tasks, including image understanding, generation, and editing. However, their inference speed remains suboptimal due to the need to repeatedly process redundant masked tokens at every sampling step. In this work, we propose Sparse-LaViDa, a novel modeling framework that dynamically truncates unnecessary masked tokens at each inference step to accelerate MDM sampling. To preserve generation quality, we introduce specialized register tokens that serve as compact representations for the truncated tokens. Furthermore, to ensure consistency between training and inference, we design a specialized attention mask that faithfully matches the truncated sampling procedure during training. Built upon the state-of-the-art unified MDM LaViDa-O, Sparse-LaViDa achieves up to a 2x speedup across diverse tasks including text-to-image generation, image editing, and mathematical reasoning, while maintaining generation quality.

