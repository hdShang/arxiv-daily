---
layout: default
title: Fast SceneScript: Accurate and Efficient Structured Language Model via Multi-Token Prediction
---

# Fast SceneScript: Accurate and Efficient Structured Language Model via Multi-Token Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05597" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05597v1</a>
  <a href="https://arxiv.org/pdf/2512.05597.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05597v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.05597v1', 'Fast SceneScript: Accurate and Efficient Structured Language Model via Multi-Token Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruihong Yin, Xuepeng Shi, Oleksandr Bailo, Marco Manfredi, Theo Gevers

**分类**: cs.CV

**发布日期**: 2025-12-05

**备注**: 10 pages, 8 figures

---

## 💡 一句话要点

**Fast SceneScript：通过多Token预测实现高效精确的结构化语言模型，用于3D场景布局估计。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `3D场景布局估计` `结构化语言模型` `多Token预测` `自推测解码` `置信度引导解码`

## 📋 核心要点

1. 基于语言模型的通用感知方法在3D场景布局估计等任务中表现出色，但自回归Token预测速度慢。
2. Fast SceneScript通过多Token预测（MTP）减少自回归迭代，并采用置信度引导解码（CGD）过滤不可靠Token。
3. 实验表明，Fast SceneScript在保证精度的前提下，显著提升了推理速度，且参数增加较少。

## 📝 摘要（中文）

本文提出了一种名为Fast SceneScript的新型结构化语言模型，用于准确高效的3D场景布局估计。该方法采用多Token预测（MTP）来减少自回归迭代次数，从而显著加速推理过程。为了解决MTP带来的Token预测可靠性问题，本文将自推测解码（SSD）适配于结构化语言模型，并引入了置信度引导解码（CGD），该方法使用改进的评分机制来评估Token的可靠性。此外，本文还设计了一种参数高效的机制，以减少MTP带来的参数开销。在ASE和Structured3D基准测试上的大量实验表明，Fast SceneScript在不牺牲准确性的前提下，每个解码器推理步骤可以生成多达9个Token，同时仅增加约7.5%的额外参数。

## 🔬 方法详解

**问题定义**：现有基于语言模型的3D场景布局估计方法依赖于自回归的next-token预测，这种方式需要多次迭代，导致推理速度较慢。如何加速3D场景布局估计，同时保证精度，是本文要解决的核心问题。现有方法的痛点在于推理效率低，难以满足实时性要求。

**核心思路**：本文的核心思路是采用多Token预测（MTP）来减少自回归迭代的次数，从而加速推理过程。为了解决MTP可能带来的预测精度下降问题，引入自推测解码（SSD）和置信度引导解码（CGD）来过滤不可靠的Token，保证生成结果的准确性。

**技术框架**：Fast SceneScript的整体框架包括一个编码器-解码器结构，其中编码器负责提取场景特征，解码器负责生成结构化的场景描述。解码器采用多Token预测机制，一次性预测多个Token。为了提高预测的可靠性，引入了自推测解码（SSD）和置信度引导解码（CGD）。此外，还设计了一个参数高效的机制来减少MTP带来的参数开销。

**关键创新**：本文的关键创新在于将多Token预测（MTP）引入到结构化语言模型中，并结合自推测解码（SSD）和置信度引导解码（CGD）来提高预测的可靠性。与传统的自回归方法相比，MTP可以显著减少迭代次数，从而加速推理过程。同时，CGD能够有效过滤不可靠的Token，保证生成结果的准确性。

**关键设计**：置信度引导解码（CGD）的关键在于设计了一个改进的评分机制，用于评估Token的可靠性。该评分机制综合考虑了Token的预测概率、上下文信息等因素，从而更准确地判断Token是否可靠。此外，参数高效机制通过参数共享等方式，减少了MTP带来的参数开销，使得模型更加轻量化。

## 📊 实验亮点

实验结果表明，Fast SceneScript在ASE和Structured3D基准测试上取得了显著的性能提升。在不牺牲准确性的前提下，每个解码器推理步骤可以生成多达9个Token，同时仅增加约7.5%的额外参数。与现有方法相比，推理速度得到了显著提升，同时保持了较高的精度。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实、增强现实等领域。通过快速准确地估计3D场景布局，可以帮助机器人更好地理解周围环境，从而实现更智能的交互和导航。在虚拟现实和增强现实中，可以用于快速生成逼真的3D场景，提升用户体验。

## 📄 摘要（原文）

> Recent perception-generalist approaches based on language models have achieved state-of-the-art results across diverse tasks, including 3D scene layout estimation, via unified architecture and interface. However, these approaches rely on autoregressive next-token prediction, which is inherently slow. In this work, we introduce Fast SceneScript, a novel structured language model for accurate and efficient 3D scene layout estimation. Our method employs multi-token prediction (MTP) to reduce the number of autoregressive iterations and significantly accelerate inference. While MTP improves speed, unreliable token predictions can significantly reduce accuracy. To filter out unreliable tokens, we adapt self-speculative decoding (SSD) for structured language models and introduce confidence-guided decoding (CGD) with an improved scoring mechanism for token reliability. Furthermore, we design a parameter-efficient mechanism that reduces the parameter overhead of MTP. Extensive experiments on the ASE and Structured3D benchmarks demonstrate that Fast SceneScript can generate up to 9 tokens per decoder inference step without compromising accuracy, while adding only $\sim7.5\%$ additional parameters.

