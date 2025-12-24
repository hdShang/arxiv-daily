---
layout: default
title: "D-AR: Diffusion via Autoregressive Models"
---

# D-AR: Diffusion via Autoregressive Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23660" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23660v1</a>
  <a href="https://arxiv.org/pdf/2505.23660.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23660v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23660v1', 'D-AR: Diffusion via Autoregressive Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziteng Gao, Mike Zheng Shou

**分类**: cs.CV

**发布日期**: 2025-05-29

**备注**: Technical report

**🔗 代码/项目**: [GITHUB](https://github.com/showlab/D-AR)

---

## 💡 一句话要点

**提出D-AR以重构图像扩散过程为自回归模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像生成` `自回归模型` `扩散过程` `离散标记` `视觉合成` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有的图像生成方法在扩散过程的建模上存在复杂性和效率低下的问题。
2. 论文提出通过自回归模型将图像扩散过程简化为标准的下一个标记预测，设计了适合的分词器。
3. 在ImageNet基准测试中，D-AR方法达到了2.09的FID，相较于传统方法有显著提升。

## 📝 摘要（中文）

本文提出了一种新的范式——通过自回归模型进行扩散（D-AR），将图像扩散过程重新构建为标准的下一个标记预测的自回归程序。我们设计了一种分词器，将图像转换为离散标记序列，不同位置的标记可以解码为像素空间中的不同扩散去噪步骤。得益于扩散特性，这些标记自然遵循粗到细的顺序，适合自回归建模。我们在标准的ImageNet基准上，使用775M的Llama骨干网络和256个离散标记，达到了2.09的FID。希望我们的工作能激发未来在视觉合成统一自回归架构方面的研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有图像生成方法在扩散过程中的复杂性和效率问题，传统方法往往需要复杂的设计和训练策略。

**核心思路**：D-AR通过将图像扩散过程转化为自回归模型的下一个标记预测，简化了生成流程，利用分词器将图像转化为离散标记序列。

**技术框架**：整体架构包括分词器、标记序列生成和解码模块。分词器将图像转换为离散标记，随后通过自回归模型生成标记，最后将生成的标记解码为扩散去噪步骤。

**关键创新**：最重要的创新在于将图像扩散过程与自回归建模相结合，利用扩散特性使得标记生成遵循粗到细的顺序，直接反映扩散过程。

**关键设计**：在参数设置上，使用775M的Llama骨干网络和256个离散标记，保持了训练和推理策略的标准化，确保了生成过程的高效性和一致性。

## 📊 实验亮点

在标准ImageNet基准测试中，D-AR方法达到了2.09的FID，相较于传统方法有显著提升，展示了其在图像生成任务中的有效性和潜力。该方法的设计使得生成过程更加高效且一致，支持零-shot布局控制合成。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、视频合成和计算机视觉中的各种任务。通过简化扩散过程，D-AR可以提高生成模型的效率和效果，具有广泛的实际价值。未来，随着大语言模型的进一步发展，D-AR可能会在视觉合成领域产生更深远的影响。

## 📄 摘要（原文）

> This paper presents Diffusion via Autoregressive models (D-AR), a new paradigm recasting the image diffusion process as a vanilla autoregressive procedure in the standard next-token-prediction fashion. We start by designing the tokenizer that converts images into sequences of discrete tokens, where tokens in different positions can be decoded into different diffusion denoising steps in the pixel space. Thanks to the diffusion properties, these tokens naturally follow a coarse-to-fine order, which directly lends itself to autoregressive modeling. Therefore, we apply standard next-token prediction on these tokens, without modifying any underlying designs (either causal masks or training/inference strategies), and such sequential autoregressive token generation directly mirrors the diffusion procedure in image space. That is, once the autoregressive model generates an increment of tokens, we can directly decode these tokens into the corresponding diffusion denoising step in the streaming manner. Our pipeline naturally reveals several intriguing properties, for example, it supports consistent previews when generating only a subset of tokens and enables zero-shot layout-controlled synthesis. On the standard ImageNet benchmark, our method achieves 2.09 FID using a 775M Llama backbone with 256 discrete tokens. We hope our work can inspire future research on unified autoregressive architectures of visual synthesis, especially with large language models. Code and models will be available at https://github.com/showlab/D-AR

