---
layout: default
title: "TrimTokenator: Towards Adaptive Visual Token Pruning for Large Multimodal Models"
---

# TrimTokenator: Towards Adaptive Visual Token Pruning for Large Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00320" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00320v2</a>
  <a href="https://arxiv.org/pdf/2509.00320.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00320v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00320v2', 'TrimTokenator: Towards Adaptive Visual Token Pruning for Large Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Zhang, Mengsi Lyu, Chenrui He, Yulong Ao, Yonghua Lin

**分类**: cs.CV

**发布日期**: 2025-08-30 (更新: 2025-10-02)

**备注**: 15 pages

---

## 💡 一句话要点

**提出视觉令牌修剪策略以提升多模态模型的推理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `视觉令牌修剪` `互信息` `推理效率` `计算机视觉` `自然语言处理` `信息多样性`

## 📋 核心要点

1. 现有的多模态模型在推理过程中面临计算和内存成本显著增加的问题，尤其是令牌数量的增加导致冗余。
2. 本文提出了一种针对视觉令牌的修剪策略，旨在通过保持跨模态对齐和信息多样性来优化模型性能。
3. 实验结果显示，该方法在LLaVA-1.5-7B和LLaVA-NEXT-7B模型上实现了88.9%的令牌减少和56.7%的推理速度提升。

## 📝 摘要（中文）

大型多模态模型（LMMs）在各种任务中取得了显著成功。这些模型通常将视觉输入编码为密集的令牌序列，并与文本令牌连接后共同处理。然而，令牌数量的增加显著提高了推理过程中的计算和内存成本。令牌修剪作为一种有前景的方法，能够有效解决这一问题。现有的修剪方法往往依赖于昂贵的校准或次优的重要性度量，导致保留的令牌冗余。本文分析了视觉和文本令牌之间的冗余差异，提出仅对视觉令牌进行修剪的策略，确保跨模态对齐和模态内部信息多样性。我们引入了一种基于互信息的修剪策略，去除与文本令牌语义不对齐的视觉令牌，从而有效保持视觉和文本模态之间的对齐。实验结果表明，该方法在保持强大性能的同时，令牌减少了88.9%，推理速度提升了56.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型多模态模型在推理过程中由于令牌数量增加而导致的计算和内存成本高的问题。现有的令牌修剪方法往往依赖于昂贵的校准或不够有效的重要性度量，导致保留的令牌冗余，影响模型性能。

**核心思路**：论文的核心思路是仅对视觉令牌进行修剪，分析视觉和文本令牌之间的冗余差异，确保跨模态对齐和模态内部信息的多样性。通过引入基于互信息的修剪策略，去除与文本令牌语义不对齐的视觉令牌，从而优化模型的表示能力。

**技术框架**：整体架构包括两个主要模块：首先是互信息计算模块，用于评估视觉令牌与文本令牌的对齐程度；其次是冗余令牌修剪模块，通过最大化嵌入空间中的期望成对距离来进一步优化保留的视觉令牌。

**关键创新**：最重要的技术创新在于提出了一种新的视觉令牌修剪策略，强调了跨模态对齐的重要性，并通过互信息度量来优化视觉令牌的选择。这一方法与现有依赖于单一重要性度量的修剪方法本质上不同。

**关键设计**：在关键设计方面，论文采用了贪心算法来高效解决最大化期望成对距离的问题。此外，损失函数的设计确保了保留的视觉令牌在语义上与文本令牌保持一致，增强了模型的整体表现。

## 📊 实验亮点

实验结果表明，TrimTokenator方法在LLaVA-1.5-7B和LLaVA-NEXT-7B模型上实现了88.9%的令牌减少，同时推理速度提升了56.7%。这一显著提升展示了该方法在优化多模态模型性能方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理以及多模态学习等。通过优化多模态模型的推理效率，能够在实时应用中提升用户体验，降低计算资源消耗，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Multimodal Models (LMMs) have achieved significant success across various tasks. These models usually encode visual inputs into dense token sequences, which are then concatenated with textual tokens and jointly processed by a language model. However, the increased token count substantially raises computational and memory costs during inference. Token pruning has emerged as a promising approach to address this issue. Existing token pruning methods often rely on costly calibration or suboptimal importance metrics, leading to redundant retained tokens. In this paper, we analyze the redundancy differences between visual and textual tokens and propose pruning exclusively on visual tokens. Based on this, we propose a visual token pruning strategy that explicitly preserves both cross-modal alignment and intra-modal informational diversity. We introduce a mutual information-based token pruning strategy that removes visual tokens semantically misaligned with textual tokens, effectively preserving the alignment between the visual and textual modalities. To further improve the representational quality of the retained tokens, we additionally prune redundant visual tokens by maximizing the expected pairwise distances in the embedding space, which is solved efficiently with a greedy algorithm. Extensive experiments demonstrate that our method maintains strong performance while reducing tokens by 88.9% on models such as LLaVA-1.5-7B and LLaVA-NEXT-7B, resulting in a 56.7% improvement in inference speed.

