---
layout: default
title: Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models
---

# Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14008" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14008</a>
  <a href="https://arxiv.org/pdf/2512.14008.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14008" onclick="toggleFavorite(this, '2512.14008', 'Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shufan Li, Jiuxiang Gu, Kangning Liu, Zhe Lin, Zijun Wei, Aditya Grover, Jason Kuen

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Sparse-LaViDa：通过稀疏化采样加速多模态离散扩散语言模型**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态扩散模型` `稀疏采样` `模型加速` `图像生成` `图像编辑`

## 📋 核心要点

1. MDM推理速度受限于重复处理冗余的masked tokens。
2. Sparse-LaViDa动态截断不必要的tokens，并用register tokens保持质量。
3. 特殊attention mask保证训练与推理一致性，加速效果显著。

## 📝 摘要（中文）

本文提出了一种名为Sparse-LaViDa的新建模框架，旨在加速Masked Discrete Diffusion Models (MDMs)的推理过程。MDMs在图像理解、生成和编辑等多种多模态任务中表现出色，但由于需要在每个采样步骤中重复处理冗余的masked tokens，导致推理速度较慢。Sparse-LaViDa通过在每个推理步骤中动态截断不必要的masked tokens来解决这个问题。为了保持生成质量，引入了专门的register tokens，作为被截断tokens的紧凑表示。此外，为了确保训练和推理之间的一致性，设计了一种专门的attention mask，在训练期间忠实地匹配截断的采样过程。基于最先进的统一MDM LaViDa-O，Sparse-LaViDa在文本到图像生成、图像编辑和数学推理等多种任务中实现了高达2倍的加速，同时保持了生成质量。

## 🔬 方法详解

**问题定义**：现有的Masked Discrete Diffusion Models (MDMs)虽然在多模态任务中表现出色，但其推理速度较慢。主要原因是需要在每个采样步骤中重复处理大量的masked tokens，这些tokens中有很多是冗余的，不包含有效信息，导致计算资源的浪费。因此，如何减少冗余计算，加速MDM的推理过程是一个重要的研究问题。

**核心思路**：Sparse-LaViDa的核心思路是在推理过程中动态地截断那些不必要的masked tokens，从而减少计算量，加速推理过程。为了弥补截断tokens带来的信息损失，引入了register tokens作为被截断tokens的紧凑表示，以保持生成质量。通过这种稀疏化的采样方式，可以在保证生成质量的前提下，显著提高推理速度。

**技术框架**：Sparse-LaViDa建立在LaViDa-O模型之上，整体框架仍然是扩散模型的迭代采样过程。主要包含以下几个关键模块：1) Token截断模块：根据某种策略（例如，基于attention score）动态地选择并截断一部分masked tokens。2) Register Token模块：为每个被截断的token集合生成一个register token，用于保留被截断token的信息。3) Attention Mask模块：设计一种特殊的attention mask，在训练过程中模拟推理时的截断过程，保证训练和推理的一致性。

**关键创新**：Sparse-LaViDa的关键创新在于动态稀疏化采样和register token的设计。与传统的MDM方法不同，Sparse-LaViDa不是在每个采样步骤中处理所有的masked tokens，而是只处理一部分重要的tokens，从而减少了计算量。Register token的设计保证了在截断tokens的同时，尽可能地保留了被截断tokens的信息，避免了生成质量的下降。

**关键设计**：关于token截断模块，一种可能的实现方式是基于attention score进行选择。例如，可以计算每个masked token与其他token之间的平均attention score，然后选择attention score较低的tokens进行截断。Register token可以通过一个小型神经网络来生成，其输入是被截断的tokens的表示，输出是register token的表示。Attention mask的设计需要保证在训练过程中，模型只能看到未被截断的tokens和register tokens，从而模拟推理时的截断过程。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14008/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14008/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14008/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Sparse-LaViDa在多种任务上实现了显著的加速效果。在文本到图像生成、图像编辑和数学推理等任务中，Sparse-LaViDa相比于LaViDa-O实现了高达2倍的加速，同时保持了生成质量。这表明Sparse-LaViDa是一种有效的加速MDM推理的方法，具有很强的实用价值。

## 🎯 应用场景

Sparse-LaViDa具有广泛的应用前景，包括但不限于：文本到图像生成、图像编辑、视频生成、3D内容生成、数学推理等。通过加速多模态内容的生成和编辑过程，可以提高生产效率，降低计算成本，并为创意设计提供更多可能性。该研究还有助于推动人工智能在各个领域的应用，例如教育、娱乐、医疗等。

## 📄 摘要（原文）

> Masked Discrete Diffusion Models (MDMs) have achieved strong performance across a wide range of multimodal tasks, including image understanding, generation, and editing. However, their inference speed remains suboptimal due to the need to repeatedly process redundant masked tokens at every sampling step. In this work, we propose Sparse-LaViDa, a novel modeling framework that dynamically truncates unnecessary masked tokens at each inference step to accelerate MDM sampling. To preserve generation quality, we introduce specialized register tokens that serve as compact representations for the truncated tokens. Furthermore, to ensure consistency between training and inference, we design a specialized attention mask that faithfully matches the truncated sampling procedure during training. Built upon the state-of-the-art unified MDM LaViDa-O, Sparse-LaViDa achieves up to a 2x speedup across diverse tasks including text-to-image generation, image editing, and mathematical reasoning, while maintaining generation quality.

