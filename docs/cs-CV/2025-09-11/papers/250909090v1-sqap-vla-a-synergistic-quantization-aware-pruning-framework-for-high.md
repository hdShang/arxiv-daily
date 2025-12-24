---
layout: default
title: "SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models"
---

# SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09090" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09090v1</a>
  <a href="https://arxiv.org/pdf/2509.09090.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09090v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09090v1', 'SQAP-VLA: A Synergistic Quantization-Aware Pruning Framework for High-Performance Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengyu Fang, Yijiang Liu, Yuan Du, Li Du, Huanrui Yang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-11

**备注**: 12 pages, 9 figures

---

## 💡 一句话要点

**提出SQAP-VLA框架，协同量化与剪枝加速高性能视觉-语言-动作模型推理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `模型压缩` `量化` `剪枝` `推理加速` `具身智能`

## 📋 核心要点

1. VLA模型计算和内存开销巨大，限制了其在资源受限环境中的部署。
2. SQAP-VLA通过协同设计量化和token剪枝流程，克服了二者不兼容的问题。
3. 实验表明，SQAP-VLA在加速推理的同时，还能提升VLA模型的性能。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型在具身智能方面展现了前所未有的能力。然而，它们巨大的计算和内存成本阻碍了它们的实际部署。现有的VLA压缩和加速方法通常以临时的方式进行量化或token剪枝，但由于观察到的不兼容性，无法同时实现两者以实现整体效率的提升。本文介绍了SQAP-VLA，这是第一个结构化的、免训练的VLA推理加速框架，它同时实现了最先进的量化和token剪枝。我们通过共同设计量化和token剪枝流程来克服这种不兼容性，其中我们提出了新的量化感知token剪枝标准，该标准适用于激进量化的模型，同时改进了量化器的设计以提高剪枝效果。当应用于标准VLA模型时，SQAP-VLA在计算效率和推理速度方面产生了显著的增益，同时成功地保持了核心模型性能，与原始模型相比，实现了1.93倍的加速和高达4.5%的平均成功率提升。

## 🔬 方法详解

**问题定义**：现有VLA模型计算量和内存占用过大，难以部署。现有的量化和token剪枝方法单独使用时效果有限，同时使用时会产生不兼容问题，导致性能下降。因此，需要一种能够同时有效利用量化和剪枝的VLA模型压缩方法。

**核心思路**：SQAP-VLA的核心思路是协同设计量化和token剪枝流程，解决二者之间的不兼容性。通过提出量化感知的token剪枝标准，使得剪枝过程能够适应量化后的模型，同时改进量化器的设计，提升剪枝的有效性。

**技术框架**：SQAP-VLA框架主要包含两个阶段：量化阶段和剪枝阶段。在量化阶段，对模型参数进行量化，降低模型大小和计算复杂度。在剪枝阶段，根据量化感知的token剪枝标准，移除不重要的token，进一步降低计算量。这两个阶段协同工作，共同提升模型的效率。

**关键创新**：SQAP-VLA的关键创新在于提出了量化感知的token剪枝标准。该标准考虑了量化对token重要性的影响，能够更准确地评估token的重要性，从而实现更有效的剪枝。此外，SQAP-VLA还改进了量化器的设计，使其更适合与剪枝结合使用。

**关键设计**：量化感知token剪枝标准的设计是关键。具体来说，该标准可能结合了量化后的参数值、token的激活值以及其他相关信息，以评估token的重要性。量化器的设计可能采用了特定的量化策略，例如训练后量化或量化感知训练，以最小化量化误差。

## 📊 实验亮点

SQAP-VLA在标准VLA模型上实现了显著的性能提升。实验结果表明，与原始模型相比，SQAP-VLA实现了1.93倍的推理速度提升，并且平均成功率提升了高达4.5%。这些结果表明，SQAP-VLA是一种有效的VLA模型压缩和加速方法。

## 🎯 应用场景

SQAP-VLA框架可应用于各种需要高性能和低功耗的具身智能应用场景，例如机器人导航、智能家居、自动驾驶等。通过压缩VLA模型，可以在资源受限的设备上部署复杂的视觉-语言-动作任务，提高系统的响应速度和用户体验。该研究有助于推动具身智能技术在实际场景中的应用。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models exhibit unprecedented capabilities for embodied intelligence. However, their extensive computational and memory costs hinder their practical deployment. Existing VLA compression and acceleration approaches conduct quantization or token pruning in an ad-hoc manner but fail to enable both for a holistic efficiency improvement due to an observed incompatibility. This work introduces SQAP-VLA, the first structured, training-free VLA inference acceleration framework that simultaneously enables state-of-the-art quantization and token pruning. We overcome the incompatibility by co-designing the quantization and token pruning pipeline, where we propose new quantization-aware token pruning criteria that work on an aggressively quantized model while improving the quantizer design to enhance pruning effectiveness. When applied to standard VLA models, SQAP-VLA yields significant gains in computational efficiency and inference speed while successfully preserving core model performance, achieving a $\times$1.93 speedup and up to a 4.5\% average success rate enhancement compared to the original model.

