---
layout: default
title: HTTM: Head-wise Temporal Token Merging for Faster VGGT
---

# HTTM: Head-wise Temporal Token Merging for Faster VGGT

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21317" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21317v1</a>
  <a href="https://arxiv.org/pdf/2511.21317.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21317v1" onclick="toggleFavorite(this, '2511.21317v1', 'HTTM: Head-wise Temporal Token Merging for Faster VGGT')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weitian Wang, Lukas Meiner, Rai Shubham, Cecilia De La Parra, Akash Kumar

**分类**: cs.CV

**发布日期**: 2025-11-26

---

## 💡 一句话要点

**提出头部分时序Token合并(HTTM)加速VGGT，用于快速3D场景重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D场景重建` `Transformer` `模型加速` `Token合并` `多头注意力`

## 📋 核心要点

1. VGGT在3D场景重建中表现出色，但全局注意力机制导致长序列输入时计算量巨大，成为性能瓶颈。
2. HTTM通过在多头注意力机制的头部粒度上进行token合并，保留了特征token的独特性，提升了模型表征能力。
3. 实验表明，HTTM在GPU上实现了高达7倍的加速，同时性能下降可忽略不计，显著提升了VGGT的效率。

## 📝 摘要（中文）

视觉几何基础Transformer (VGGT) 在3D场景重建方面取得了显著进展，它是第一个直接一次性联合推断所有关键3D属性（相机姿态、深度和密集几何）的模型。然而，这种联合推断机制需要全局注意力层，对来自所有视角的token执行全连接注意力计算。对于具有长序列输入的大型场景重建，这会导致显著的延迟瓶颈。本文提出头部分时序合并（HTTM），一种免训练的3D token合并方法，用于加速VGGT。现有的合并技术在不同的注意力头中统一合并token，导致层输出中出现相同的token，这阻碍了模型的表征能力。HTTM通过多头粒度合并token来解决这个问题，从而在头部连接后保持特征token的唯一性。此外，与现有方法相比，这使得HTTM能够利用在头部层面观察到的空间局部性和时间对应性，以更低的合并成本实现更高的合并率。因此，HTTM在基于GPU的推理中实现了高达7倍的加速，而性能下降可忽略不计。

## 🔬 方法详解

**问题定义**：VGGT在3D场景重建中需要对所有视角的token进行全局注意力计算，这在处理长序列输入的大型场景时会产生巨大的计算量，导致推理速度慢，成为性能瓶颈。现有的token合并方法通常在不同注意力头中统一合并token，导致信息冗余，降低了模型的表征能力。

**核心思路**：HTTM的核心思路是在多头注意力机制的头部粒度上进行token合并，而不是像现有方法那样在所有头部统一合并。这样可以保留每个头部学习到的独特特征，避免信息冗余，从而在减少计算量的同时保持模型的表征能力。同时，HTTM利用头部层面的空间局部性和时间对应性，实现更高的合并率和更低的合并成本。

**技术框架**：HTTM主要包含以下步骤：首先，将输入token按照时间顺序分组。然后，对于每个时间步的token，将其输入到多头注意力层。在每个注意力头中，HTTM根据一定的策略（例如，基于相似度或重要性）选择需要保留的token，并合并其余的token。最后，将所有头部的输出连接起来，作为下一层的输入。整个过程无需训练，可以直接应用于预训练的VGGT模型。

**关键创新**：HTTM最重要的创新点在于其头部分时序合并策略。与现有方法在所有头部统一合并token不同，HTTM在每个头部独立地进行token合并，保留了每个头部学习到的独特特征，避免了信息冗余。这种方法能够更有效地减少计算量，同时保持模型的表征能力。

**关键设计**：HTTM的关键设计包括：1) 基于相似度或重要性的token选择策略，用于确定哪些token需要保留，哪些token可以合并；2) 多头粒度的合并操作，确保每个头部的信息能够被充分利用；3) 免训练的设计，使得HTTM可以直接应用于预训练的VGGT模型，无需额外的训练成本。具体的相似度计算方法和重要性评估指标可以根据实际应用场景进行调整。

## 📊 实验亮点

实验结果表明，HTTM在GPU上实现了高达7倍的加速，同时性能下降可忽略不计。这意味着在保持重建质量的前提下，VGGT的推理速度得到了显著提升。此外，HTTM的免训练特性使其能够直接应用于预训练的VGGT模型，无需额外的训练成本，具有很强的实用性。

## 🎯 应用场景

HTTM加速VGGT的方法可广泛应用于需要快速3D场景重建的领域，例如自动驾驶、机器人导航、虚拟现实和增强现实等。通过降低计算成本和延迟，HTTM使得VGGT能够处理更大规模的场景和更长的输入序列，从而提高这些应用的实时性和实用性。未来，该方法还可以扩展到其他基于Transformer的3D视觉任务中。

## 📄 摘要（原文）

> The Visual Geometry Grounded Transformer (VGGT) marks a significant leap forward in 3D scene reconstruction, as it is the first model that directly infers all key 3D attributes (camera poses, depths, and dense geometry) jointly in one pass. However, this joint inference mechanism requires global attention layers that perform all-to-all attention computation on tokens from all views. For reconstruction of large scenes with long-sequence inputs, this causes a significant latency bottleneck. In this paper, we propose head-wise temporal merging (HTTM), a training-free 3D token merging method for accelerating VGGT. Existing merging techniques merge tokens uniformly across different attention heads, resulting in identical tokens in the layers' output, which hinders the model's representational ability. HTTM tackles this problem by merging tokens in multi-head granularity, which preserves the uniqueness of feature tokens after head concatenation. Additionally, this enables HTTM to leverage the spatial locality and temporal correspondence observed at the head level to achieve higher merging ratios with lower merging costs compared to existing methods. Thus, HTTM achieves up to 7x acceleration with negligible performance drops in a GPU-based inference.

