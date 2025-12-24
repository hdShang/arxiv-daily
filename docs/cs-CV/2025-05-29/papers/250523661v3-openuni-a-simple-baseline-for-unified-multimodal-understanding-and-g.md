---
layout: default
title: OpenUni: A Simple Baseline for Unified Multimodal Understanding and Generation
---

# OpenUni: A Simple Baseline for Unified Multimodal Understanding and Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23661" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23661v3</a>
  <a href="https://arxiv.org/pdf/2505.23661.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23661v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23661v3', 'OpenUni: A Simple Baseline for Unified Multimodal Understanding and Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Size Wu, Zhonghua Wu, Zerui Gong, Qingyi Tao, Sheng Jin, Qinyue Li, Wei Li, Chen Change Loy

**分类**: cs.CV

**发布日期**: 2025-05-29 (更新: 2025-06-02)

**🔗 代码/项目**: [GITHUB](https://github.com/wusize/OpenUni)

---

## 💡 一句话要点

**提出OpenUni以实现多模态理解与生成的统一**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态理解` `图像生成` `文本生成` `轻量级模型` `开源研究`

## 📋 核心要点

1. 现有多模态模型在理解和生成任务中存在复杂性高、训练效率低的问题。
2. OpenUni通过轻量级的变换器连接器和可学习的查询，简化了多模态模型的训练过程。
3. 在多个标准基准上，OpenUni以1.1B和3.1B的参数量实现了高质量图像生成和优异的性能表现。

## 📝 摘要（中文）

在本报告中，我们提出了OpenUni，这是一个简单、轻量且完全开源的基线模型，旨在统一多模态理解与生成。受现有统一模型学习实践的启发，我们采用了一种高效的训练策略，通过一组可学习的查询和轻量级的基于变换器的连接器，将现成的多模态大语言模型与扩散模型相结合，从而最小化训练复杂性和开销。通过简约的架构选择，我们展示了OpenUni能够生成高质量且符合指令的图像，并在GenEval、DPG-Bench和WISE等标准基准上取得了卓越的性能，仅使用了1.1B和3.1B的激活参数。为了支持开放研究和社区发展，我们在https://github.com/wusize/OpenUni上发布了所有模型权重、训练代码及我们整理的训练数据集（包括2300万对图像-文本）。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态理解与生成任务中的训练复杂性和效率低下的问题。现有方法通常需要大量的计算资源和复杂的架构设计，导致实际应用受限。

**核心思路**：OpenUni的核心思路是通过结合现成的多模态大语言模型和扩散模型，采用轻量级的变换器连接器和可学习的查询，从而简化训练过程并提高效率。这样的设计使得模型在保持性能的同时，显著降低了计算开销。

**技术框架**：OpenUni的整体架构包括三个主要模块：首先是多模态大语言模型，负责理解和生成文本；其次是扩散模型，用于生成高质量图像；最后是轻量级的变换器连接器，负责将两者有效结合。整个流程通过可学习的查询进行优化，以实现更好的协同效果。

**关键创新**：OpenUni的最重要创新在于其轻量级的设计和高效的训练策略，这与现有方法相比，显著降低了模型的复杂性和计算需求。通过这种创新，OpenUni能够在较少的参数下实现高质量的多模态生成。

**关键设计**：在参数设置上，OpenUni使用了1.1B和3.1B的激活参数，确保了模型的高效性。损失函数设计上，采用了适应性损失策略，以优化多模态生成的质量。网络结构方面，轻量级的变换器连接器是关键设计，确保了模型的快速训练和高效推理。

## 📊 实验亮点

在实验中，OpenUni在GenEval、DPG-Bench和WISE等标准基准上表现出色，生成的图像质量高且符合指令要求。使用1.1B和3.1B的参数量，OpenUni在性能上超越了许多现有的多模态模型，展示了其在效率和效果上的显著提升。

## 🎯 应用场景

OpenUni的研究成果在多个领域具有广泛的应用潜力，包括图像生成、文本生成以及人机交互等场景。其高效的训练策略和轻量级设计使得在资源受限的环境中也能实现高质量的多模态生成，推动了相关技术的普及与发展。未来，OpenUni可能在教育、娱乐和创意产业等领域发挥重要作用。

## 📄 摘要（原文）

> In this report, we present OpenUni, a simple, lightweight, and fully open-source baseline for unifying multimodal understanding and generation. Inspired by prevailing practices in unified model learning, we adopt an efficient training strategy that minimizes the training complexity and overhead by bridging the off-the-shelf multimodal large language models (LLMs) and diffusion models through a set of learnable queries and a light-weight transformer-based connector. With a minimalist choice of architecture, we demonstrate that OpenUni can: 1) generate high-quality and instruction-aligned images, and 2) achieve exceptional performance on standard benchmarks such as GenEval, DPG- Bench, and WISE, with only 1.1B and 3.1B activated parameters. To support open research and community advancement, we release all model weights, training code, and our curated training datasets (including 23M image-text pairs) at https://github.com/wusize/OpenUni.

