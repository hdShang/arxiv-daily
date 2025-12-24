---
layout: default
title: "Co-Me: Confidence-Guided Token Merging for Visual Geometric Transformers"
---

# Co-Me: Confidence-Guided Token Merging for Visual Geometric Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14751" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14751v1</a>
  <a href="https://arxiv.org/pdf/2511.14751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14751v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14751v1', 'Co-Me: Confidence-Guided Token Merging for Visual Geometric Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yutian Chen, Yuheng Qiu, Ruogu Li, Ali Agha, Shayegan Omidshafiei, Jay Patrikar, Sebastian Scherer

**分类**: cs.CV, cs.RO

**发布日期**: 2025-11-18

---

## 💡 一句话要点

**提出Co-Me，加速视觉几何Transformer，无需重训练即可实现高达11.3倍的加速。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉几何Transformer` `Token合并` `模型加速` `置信度引导` `实时3D感知`

## 📋 核心要点

1. 现有视觉几何Transformer计算成本高昂，限制了其在实时3D感知和重建等领域的应用。
2. Co-Me通过置信度预测器评估token的重要性，合并低置信度token，从而减少计算量并保持空间覆盖率。
3. 实验表明，Co-Me在VGGT和MapAnything上分别实现了高达11.3倍和7.2倍的加速，且无需重训练。

## 📝 摘要（中文）

本文提出了一种名为置信度引导Token合并（Co-Me）的加速机制，用于视觉几何Transformer，无需对基础模型进行重训练或微调。Co-Me提炼出一个轻量级的置信度预测器，通过不确定性对token进行排序，并选择性地合并低置信度的token，从而在保持空间覆盖率的同时有效地减少计算量。与基于相似性的合并或剪枝相比，Co-Me中的置信度信号能够可靠地指示Transformer强调的区域，从而在不降低性能的情况下实现显著的加速。Co-Me可以无缝地应用于各种多视图和流式视觉几何Transformer，实现随序列长度扩展的加速效果。当应用于VGGT和MapAnything时，Co-Me分别实现了高达11.3倍和7.2倍的加速，使视觉几何Transformer能够应用于实时3D感知和重建。

## 🔬 方法详解

**问题定义**：视觉几何Transformer在处理长序列时计算复杂度高，难以满足实时性要求。现有的加速方法，如基于相似性的合并或剪枝，可能导致关键信息的丢失，影响性能。

**核心思路**：Co-Me的核心思想是利用置信度来衡量token的重要性，并优先合并置信度低的token。这样可以在减少计算量的同时，尽可能保留对最终结果影响较大的token，从而在加速的同时保持性能。置信度预测器旨在学习Transformer的注意力机制，预测每个token的重要性。

**技术框架**：Co-Me包含一个轻量级的置信度预测器，该预测器与视觉几何Transformer并行工作。首先，Transformer处理输入序列并生成token。然后，置信度预测器为每个token分配一个置信度分数，表示该token的重要性。接下来，根据置信度分数对token进行排序，并合并置信度最低的token。最后，合并后的token序列被传递到Transformer的后续层进行处理。

**关键创新**：Co-Me的关键创新在于使用置信度作为token合并的指导信号。与基于相似性的合并或剪枝相比，置信度能够更准确地反映token的重要性，从而避免了关键信息的丢失。此外，Co-Me无需对基础模型进行重训练或微调，可以直接应用于现有的视觉几何Transformer。

**关键设计**：置信度预测器可以使用各种轻量级的网络结构实现，例如多层感知机（MLP）。置信度预测器的输入可以是token的特征向量，输出是一个标量值，表示该token的置信度。合并策略可以采用不同的方法，例如，可以设置一个置信度阈值，将低于该阈值的token合并。也可以按照置信度分数从小到大排序，合并一定比例的token。

## 📊 实验亮点

Co-Me在VGGT和MapAnything两个视觉几何Transformer模型上进行了评估，实验结果表明，Co-Me能够显著提高模型的推理速度，同时保持甚至略微提升模型的性能。具体来说，Co-Me在VGGT上实现了高达11.3倍的加速，在MapAnything上实现了高达7.2倍的加速。这些加速效果使得视觉几何Transformer能够应用于实时场景。

## 🎯 应用场景

Co-Me加速后的视觉几何Transformer可应用于实时3D感知和重建，例如机器人导航、自动驾驶、增强现实等领域。通过降低计算成本，Co-Me使得视觉几何Transformer能够在资源受限的设备上运行，从而扩展了其应用范围。未来，Co-Me可以进一步与其他加速技术相结合，以实现更高的性能。

## 📄 摘要（原文）

> We propose Confidence-Guided Token Merging (Co-Me), an acceleration mechanism for visual geometric transformers without retraining or finetuning the base model. Co-Me distilled a light-weight confidence predictor to rank tokens by uncertainty and selectively merge low-confidence ones, effectively reducing computation while maintaining spatial coverage. Compared to similarity-based merging or pruning, the confidence signal in Co-Me reliably indicates regions emphasized by the transformer, enabling substantial acceleration without degrading performance. Co-Me applies seamlessly to various multi-view and streaming visual geometric transformers, achieving speedups that scale with sequence length. When applied to VGGT and MapAnything, Co-Me achieves up to $11.3\times$ and $7.2\times$ speedup, making visual geometric transformers practical for real-time 3D perception and reconstruction.

