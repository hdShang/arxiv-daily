---
layout: default
title: GRAN-TED: Generating Robust, Aligned, and Nuanced Text Embedding for Diffusion Models
---

# GRAN-TED: Generating Robust, Aligned, and Nuanced Text Embedding for Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15560" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15560v1</a>
  <a href="https://arxiv.org/pdf/2512.15560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15560v1" onclick="toggleFavorite(this, '2512.15560v1', 'GRAN-TED: Generating Robust, Aligned, and Nuanced Text Embedding for Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bozhou Li, Sihan Yang, Yushuo Guan, Ruichuan An, Xinlong Chen, Yang Shi, Pengfei Wan, Wentao Zhang, Yuanxing zhang

**分类**: cs.CV

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出GRAN-TED框架，用于生成鲁棒、对齐和细致的扩散模型文本嵌入。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本编码器` `扩散模型` `文本到图像` `文本到视频` `多模态学习` `文本嵌入` `评估基准`

## 📋 核心要点

1. 文本到图像/视频生成依赖文本编码器，但缺乏有效评估框架和视觉合成的预训练模型。
2. GRAN-TED通过TED-6K基准评估编码器，并采用两阶段训练提升文本特征的细致性和鲁棒性。
3. 实验表明，GRAN-TED在TED-6K上达到SOTA，并在图像/视频生成任务中显著提升性能。

## 📝 摘要（中文）

本文提出GRAN-TED，一种用于生成扩散模型中鲁棒、对齐和细致文本嵌入的范例。文本编码器是文本到图像和文本到视频扩散模型的关键组成部分，从根本上决定了生成内容的语义保真度。然而，其发展受到两个主要挑战的阻碍：缺乏能够可靠地预测下游生成性能的有效评估框架，以及难以有效地调整预训练语言模型以进行视觉合成。为了解决这些问题，我们提出了TED-6K，这是一个新颖的纯文本基准，无需昂贵的端到端模型训练即可对编码器的表征质量进行高效而稳健的评估。我们证明了TED-6K上的性能（通过轻量级统一适配器标准化）与编码器在下游生成任务中的有效性密切相关。其次，在该验证框架的指导下，我们使用一种新颖的两阶段训练范例开发了一种卓越的文本编码器。此过程包括在多模态大型语言模型上进行初始微调阶段，以获得更好的视觉表示，然后采用分层加权方法来提取更细致和更强大的文本特征。实验表明，由此产生的GRAN-TED编码器不仅在TED-6K上实现了最先进的性能，而且还在文本到图像和文本到视频生成方面带来了明显的性能提升。

## 🔬 方法详解

**问题定义**：文本到图像和文本到视频的扩散模型中，文本编码器是关键组件，决定了生成内容的语义保真度。现有方法缺乏有效的评估框架来可靠地预测下游生成性能，并且难以有效地调整预训练语言模型以进行视觉合成，导致文本编码器的发展受限。

**核心思路**：GRAN-TED的核心思路是首先构建一个高效的文本评估基准TED-6K，用于评估文本编码器的质量，然后基于此基准，通过两阶段训练方法优化文本编码器。这种设计旨在解决现有方法中评估困难和预训练模型适应性差的问题。

**技术框架**：GRAN-TED框架包含两个主要部分：TED-6K文本评估基准和两阶段训练的文本编码器。TED-6K用于评估文本编码器的表征质量。两阶段训练包括：1) 在多模态大型语言模型上进行微调，以提升视觉表示能力；2) 采用分层加权方法，提取更细致和强大的文本特征。

**关键创新**：GRAN-TED的关键创新在于：1) 提出了TED-6K，一个纯文本基准，用于高效评估文本编码器的质量，避免了昂贵的端到端模型训练；2) 提出了两阶段训练方法，首先在多模态LLM上微调，然后进行分层加权，从而提升文本编码器的性能。

**关键设计**：TED-6K包含6000个文本描述，涵盖了广泛的视觉概念。两阶段训练中，第一阶段使用多模态LLM（具体模型未知）进行微调，损失函数未知。第二阶段的分层加权方法，具体权重计算方式未知，但目标是提取更细致和更强大的文本特征。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15560v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15560v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15560v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GRAN-TED在TED-6K基准上取得了state-of-the-art的性能。更重要的是，将GRAN-TED编码器应用于文本到图像和文本到视频的生成任务中，能够显著提升生成质量，具体的性能提升数据未知，但表明了GRAN-TED的有效性。

## 🎯 应用场景

GRAN-TED的研究成果可应用于各种文本到图像和文本到视频的生成任务中，提高生成内容与文本描述的语义一致性和细节丰富度。该方法在创意设计、内容生成、虚拟现实等领域具有潜在的应用价值，并有望推动多模态生成技术的发展。

## 📄 摘要（原文）

> The text encoder is a critical component of text-to-image and text-to-video diffusion models, fundamentally determining the semantic fidelity of the generated content. However, its development has been hindered by two major challenges: the lack of an efficient evaluation framework that reliably predicts downstream generation performance, and the difficulty of effectively adapting pretrained language models for visual synthesis. To address these issues, we introduce GRAN-TED, a paradigm to Generate Robust, Aligned, and Nuanced Text Embeddings for Diffusion models. Our contribution is twofold. First, we propose TED-6K, a novel text-only benchmark that enables efficient and robust assessment of an encoder's representational quality without requiring costly end-to-end model training. We demonstrate that performance on TED-6K, standardized via a lightweight, unified adapter, strongly correlates with an encoder's effectiveness in downstream generation tasks. Second, guided by this validated framework, we develop a superior text encoder using a novel two-stage training paradigm. This process involves an initial fine-tuning stage on a Multimodal Large Language Model for better visual representation, followed by a layer-wise weighting method to extract more nuanced and potent text features. Our experiments show that the resulting GRAN-TED encoder not only achieves state-of-the-art performance on TED-6K but also leads to demonstrable performance gains in text-to-image and text-to-video generation. Our code is available at the following link: https://anonymous.4open.science/r/GRAN-TED-4FCC/.

