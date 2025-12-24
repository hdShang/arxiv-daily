---
layout: default
title: "Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs"
---

# Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10967" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10967v2</a>
  <a href="https://arxiv.org/pdf/2506.10967.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10967v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10967v2', 'Beyond Attention or Similarity: Maximizing Conditional Diversity for Token Pruning in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qizhe Zhang, Mengzhen Liu, Lichen Li, Ming Lu, Yuan Zhang, Junwen Pan, Qi She, Shanghang Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-12 (更新: 2025-07-01)

**备注**: 22 pages, 5 figures, code: https://github.com/Theia-4869/CDPruner, project page: https://theia-4869.github.io/CDPruner

**🔗 代码/项目**: [GITHUB](https://github.com/Theia-4869/CDPruner)

---

## 💡 一句话要点

**提出CDPruner以解决多模态大语言模型中的视觉token冗余问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉token修剪` `条件多样性` `决定性点过程` `多模态大语言模型` `视觉-语言基准` `高效推理` `模型无关`

## 📋 核心要点

1. 现有的视觉token修剪方法要么依赖于注意力机制，导致冗余token的保留，要么基于相似性，忽视指令相关性，造成性能下降。
2. 本文提出CDPruner，通过最大化条件多样性来优化token修剪，定义了基于指令的条件相似性，并利用DPP重新构建修剪问题。
3. CDPruner在LLaVA模型上实现了95%的FLOPs减少和78%的CUDA延迟降低，同时保持94%的原始准确率，展示了其优越性。

## 📝 摘要（中文）

在多模态大语言模型（MLLMs）中，输入视觉token的长度通常显著大于文本token，导致高推理成本。现有方法通过注意力或相似性进行token修剪，但存在保留冗余token或忽视指令相关性的问题，导致性能不佳。本文提出了一种新颖的视觉token修剪方法CDPruner，旨在最大化保留token的条件多样性。我们定义了基于指令的视觉token条件相似性，并通过决定性点过程（DPP）重新构建token修剪问题，以最大化所选子集的条件多样性。CDPruner无需训练且与模型无关，适用于多种MLLMs。实验结果表明，CDPruner在多个视觉-语言基准上建立了新的最先进水平，能够在高压缩比下保持强性能。

## 🔬 方法详解

**问题定义**：本文解决的是多模态大语言模型中视觉token冗余的问题。现有方法在修剪过程中要么保留了大量重复token，要么忽视了与用户指令的相关性，导致性能不佳。

**核心思路**：CDPruner的核心思路是通过最大化条件多样性来优化token的选择。通过定义视觉token的条件相似性，确保所选token不仅多样化，还能与用户指令紧密相关。

**技术框架**：CDPruner的整体架构包括两个主要模块：首先，计算视觉token的条件相似性；其次，利用决定性点过程（DPP）进行token的选择，以最大化所选子集的条件多样性。

**关键创新**：CDPruner的关键创新在于引入了条件多样性最大化的概念，与现有的注意力和相似性方法本质上不同，能够更有效地选择与指令相关的多样化token。

**关键设计**：在设计中，CDPruner不需要额外的训练过程，且与模型无关，能够方便地应用于不同的MLLMs。具体的参数设置和损失函数设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

CDPruner在LLaVA模型上实现了95%的FLOPs减少和78%的CUDA延迟降低，同时保持94%的原始准确率，展示了其在视觉-语言任务中的显著性能提升，确立了新的最先进水平。

## 🎯 应用场景

该研究的潜在应用领域包括视觉问答、图像描述生成和多模态内容检索等。通过优化视觉token的选择，CDPruner能够显著降低计算成本，同时保持高性能，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> In multimodal large language models (MLLMs), the length of input visual tokens is often significantly greater than that of their textual counterparts, leading to a high inference cost. Many works aim to address this issue by removing redundant visual tokens. However, current approaches either rely on attention-based pruning, which retains numerous duplicate tokens, or use similarity-based pruning, overlooking the instruction relevance, consequently causing suboptimal performance. In this paper, we go beyond attention or similarity by proposing a novel visual token pruning method named CDPruner, which maximizes the conditional diversity of retained tokens. We first define the conditional similarity between visual tokens conditioned on the instruction, and then reformulate the token pruning problem with determinantal point process (DPP) to maximize the conditional diversity of the selected subset. The proposed CDPruner is training-free and model-agnostic, allowing easy application to various MLLMs. Extensive experiments across diverse MLLMs show that CDPruner establishes new state-of-the-art on various vision-language benchmarks. By maximizing conditional diversity through DPP, the selected subset better represents the input images while closely adhering to user instructions, thereby preserving strong performance even with high reduction ratios. When applied to LLaVA, CDPruner reduces FLOPs by 95\% and CUDA latency by 78\%, while maintaining 94\% of the original accuracy. Our code is available at https://github.com/Theia-4869/CDPruner.

