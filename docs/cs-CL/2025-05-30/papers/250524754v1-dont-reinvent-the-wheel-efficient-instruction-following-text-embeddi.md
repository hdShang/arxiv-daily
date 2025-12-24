---
layout: default
title: "Don't Reinvent the Wheel: Efficient Instruction-Following Text Embedding based on Guided Space Transformation"
---

# Don't Reinvent the Wheel: Efficient Instruction-Following Text Embedding based on Guided Space Transformation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24754" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24754v1</a>
  <a href="https://arxiv.org/pdf/2505.24754.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24754v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24754v1', 'Don\'t Reinvent the Wheel: Efficient Instruction-Following Text Embedding based on Guided Space Transformation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yingchaojie Feng, Yiqun Sun, Yandong Sun, Minfeng Zhu, Qiang Huang, Anthony K. H. Tung, Wei Chen

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-05-30

**备注**: Accepted to ACL 2025

**🔗 代码/项目**: [GITHUB](https://github.com/YingchaojieFeng/GSTransform)

---

## 💡 一句话要点

**提出GSTransform以解决指令跟随文本嵌入的计算开销问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `指令跟随` `文本嵌入` `引导空间变换` `实时处理` `计算效率` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有方法在处理指令跟随文本嵌入时，需对整个语料库进行重复编码，导致计算开销巨大。
2. GSTransform通过引导空间变换，利用预计算的嵌入实时适应用户指令，避免了重复编码的需求。
3. 实验结果显示，GSTransform在多个下游任务中显著提升了文本嵌入质量，并实现了高达300倍的处理速度提升。

## 📝 摘要（中文）

本研究探讨了一项重要任务，即指令跟随文本嵌入，旨在生成动态文本嵌入以适应用户指令，突出文本的特定属性。尽管已有进展，现有方法仍面临显著的计算开销，因为每次新指令都需重新编码整个语料库。为了解决这一挑战，我们提出了基于引导空间变换的GSTransform框架。我们的关键观察是，指令相关信息本质上已在通用嵌入中编码，但未被充分利用。GSTransform是一种轻量级的变换机制，能够实时调整预计算的嵌入，以与用户指令对齐，且只需少量带有指令聚焦标签注释的文本数据。我们在三个指令感知下游任务和九个真实数据集上进行了广泛实验，结果表明，GSTransform在提高指令跟随文本嵌入质量的同时，实现了6至300倍的实时处理速度提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决指令跟随文本嵌入中的计算开销问题。现有方法需要针对每个新指令重新编码整个文本语料库，导致效率低下和资源浪费。

**核心思路**：论文提出的GSTransform框架通过引导空间变换，利用已有的通用嵌入，实时调整以适应用户指令，从而避免重复编码的过程。该方法通过少量带有指令标签的文本数据进行指导，充分利用了已有嵌入中的指令相关信息。

**技术框架**：GSTransform的整体架构包括预计算的文本嵌入、引导空间变换模块和指令适应模块。首先，预计算的嵌入被存储并在需要时调用；然后，通过引导空间变换模块对这些嵌入进行实时调整，以符合用户的具体指令。

**关键创新**：GSTransform的主要创新在于其轻量级的变换机制，能够在不重新编码整个语料库的情况下，快速适应新的指令。这一方法与现有技术的根本区别在于其高效性和实时性。

**关键设计**：在设计上，GSTransform使用了少量的指令聚焦标签数据来引导变换过程，确保了嵌入的高效适应性。同时，模型的损失函数和网络结构经过精心设计，以优化指令跟随的效果。

## 📊 实验亮点

实验结果表明，GSTransform在三个指令感知下游任务上均优于现有最先进的方法，文本嵌入质量显著提升，同时在大规模数据集上的实时处理速度提升达6至300倍，展现出极高的效率。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化客服和个性化推荐系统等。通过提高文本嵌入的适应性和处理速度，GSTransform能够显著提升用户体验和系统响应效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> In this work, we investigate an important task named instruction-following text embedding, which generates dynamic text embeddings that adapt to user instructions, highlighting specific attributes of text. Despite recent advancements, existing approaches suffer from significant computational overhead, as they require re-encoding the entire corpus for each new instruction. To address this challenge, we propose GSTransform, a novel instruction-following text embedding framework based on Guided Space Transformation. Our key observation is that instruction-relevant information is inherently encoded in generic embeddings but remains underutilized. Instead of repeatedly encoding the corpus for each instruction, GSTransform is a lightweight transformation mechanism that adapts pre-computed embeddings in real time to align with user instructions, guided by a small amount of text data with instruction-focused label annotation. We conduct extensive experiments on three instruction-awareness downstream tasks across nine real-world datasets, demonstrating that GSTransform improves instruction-following text embedding quality over state-of-the-art methods while achieving dramatic speedups of 6~300x in real-time processing on large-scale datasets. The source code is available at https://github.com/YingchaojieFeng/GSTransform.

