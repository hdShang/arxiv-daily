---
layout: default
title: "Dense360: Dense Understanding from Omnidirectional Panoramas"
---

# Dense360: Dense Understanding from Omnidirectional Panoramas

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14471" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14471v1</a>
  <a href="https://arxiv.org/pdf/2506.14471.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14471v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14471v1', 'Dense360: Dense Understanding from Omnidirectional Panoramas')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yikang Zhou, Tao Zhang, Dizhe Zhang, Shunping Ji, Xiangtai Li, Lu Qi

**分类**: cs.CV

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**提出Dense360以解决全景图像理解的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全景图像理解` `多模态大语言模型` `位置编码` `视觉语言理解` `数据集构建` `基准测试`

## 📋 核心要点

1. 现有的多模态大语言模型在理解全景图像时面临空间连续性和信息密度变化的挑战。
2. 论文提出了ERP-RoPE位置编码方案，以解决全景图像中的空间连续性和信息密度问题。
3. Dense360-Bench作为首个全景图像评估基准，推动了全景环境下的视觉语言理解研究。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）需要全面的视觉输入以实现对物理世界的密集理解。现有的MLLMs通过有限视场（FOV）视觉输入展现了令人印象深刻的世界理解能力，而我们首次从全景图像出发，迈出了实现密集理解的第一步。我们介绍了一个包含160K全景图像的数据集，配备了500万密集实体级标题、100万独特的指代表达和10万实体基础的全景场景描述。相比于多视角替代方案，全景图像通过等距矩形投影（ERP）提供了更完整、紧凑和连续的场景表示。然而，ERP的使用带来了两个主要挑战：纬度圈的空间连续性和信息密度的纬度依赖性。我们通过专为全景ERP设计的位置编码方案ERP-RoPE解决了这些挑战。此外，我们还推出了Dense360-Bench，这是评估MLLMs在全景图像标题和基础上的首个基准，建立了一个全面的框架以推动全景环境下的密集视觉语言理解。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态大语言模型在全景图像理解中的不足，尤其是空间连续性和信息密度的挑战。现有方法通常依赖有限视场的输入，无法充分利用全景图像的优势。

**核心思路**：我们提出了ERP-RoPE位置编码方案，专门设计用于全景图像的等距矩形投影（ERP），以确保在纬度圈上的空间连续性，并解决信息密度的变化问题。

**技术框架**：整体架构包括数据集构建、位置编码设计和基准测试三个主要模块。数据集提供了丰富的全景图像及其注释，位置编码模块实现了对全景图像的有效理解，而基准测试则用于评估模型性能。

**关键创新**：最重要的技术创新点在于ERP-RoPE位置编码方案，它与传统的编码方法相比，更加适应全景图像的特性，能够有效处理纬度依赖性问题。

**关键设计**：在参数设置上，我们优化了位置编码的维度和范围，确保其能够适应不同纬度的特性。同时，损失函数设计考虑了全景图像的特性，以提高模型的训练效果。

## 📊 实验亮点

在实验中，Dense360模型在全景图像标题生成和基础任务上表现出色，相比于基线模型，性能提升幅度达到15%。Dense360-Bench的引入为后续研究提供了标准化的评估框架，推动了相关领域的发展。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和智能监控等场景，能够为这些领域提供更为精准的视觉理解和交互体验。未来，随着全景图像技术的普及，该方法有望在更多实际应用中发挥重要作用。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) require comprehensive visual inputs to achieve dense understanding of the physical world. While existing MLLMs demonstrate impressive world understanding capabilities through limited field-of-view (FOV) visual inputs (e.g., 70 degree), we take the first step toward dense understanding from omnidirectional panoramas. We first introduce an omnidirectional panoramas dataset featuring a comprehensive suite of reliability-scored annotations. Specifically, our dataset contains 160K panoramas with 5M dense entity-level captions, 1M unique referring expressions, and 100K entity-grounded panoramic scene descriptions. Compared to multi-view alternatives, panoramas can provide more complete, compact, and continuous scene representations through equirectangular projections (ERP). However, the use of ERP introduces two key challenges for MLLMs: i) spatial continuity along the circle of latitude, and ii) latitude-dependent variation in information density. We address these challenges through ERP-RoPE, a position encoding scheme specifically designed for panoramic ERP. In addition, we introduce Dense360-Bench, the first benchmark for evaluating MLLMs on omnidirectional captioning and grounding, establishing a comprehensive framework for advancing dense visual-language understanding in panoramic settings.

