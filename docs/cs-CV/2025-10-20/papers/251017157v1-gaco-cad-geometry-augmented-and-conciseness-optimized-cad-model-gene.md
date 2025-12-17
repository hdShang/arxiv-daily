---
layout: default
title: GACO-CAD: Geometry-Augmented and Conciseness-Optimized CAD Model Generation from Single Image
---

# GACO-CAD: Geometry-Augmented and Conciseness-Optimized CAD Model Generation from Single Image

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17157" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17157v1</a>
  <a href="https://arxiv.org/pdf/2510.17157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17157v1" onclick="toggleFavorite(this, '2510.17157v1', 'GACO-CAD: Geometry-Augmented and Conciseness-Optimized CAD Model Generation from Single Image')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yinghui Wang, Xinyu Zhang, Peng Du

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-20

---

## 💡 一句话要点

**GACO-CAD：通过几何增强与简洁性优化，从单张图像生成CAD模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `CAD模型生成` `单图重建` `多模态大语言模型` `几何先验` `强化学习`

## 📋 核心要点

1. 现有多模态大语言模型在单图生成CAD模型时，由于空间推理能力有限，难以准确推断3D几何。
2. GACO-CAD通过引入几何先验增强和简洁性优化，提升几何精度，并鼓励生成更简洁的建模流程。
3. 实验表明，GACO-CAD在代码有效性、几何精度和建模简洁性方面均优于现有方法，达到SOTA水平。

## 📝 摘要（中文）

本文提出GACO-CAD，一种新颖的两阶段后训练框架，旨在从单张图像生成可编辑的参数化CAD模型，从而降低工业概念设计的门槛。该框架联合优化几何精度和建模过程的简洁性。首先，在监督微调阶段，利用深度图和表面法线图作为密集的几何先验，与RGB图像结合形成多通道输入。这些先验为单视图重建提供互补的空间线索，帮助多模态大语言模型(MLLM)更可靠地从2D观测中恢复3D几何。其次，在强化学习阶段，引入组长度奖励，在保持高几何保真度的同时，鼓励生成更紧凑、更少冗余的参数化建模序列。采用简单的动态加权策略来稳定训练。在DeepCAD和Fusion360数据集上的实验表明，在相同的MLLM骨干网络下，GACO-CAD取得了最先进的性能，在代码有效性、几何精度和建模简洁性方面始终优于现有方法。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像生成精确且简洁的参数化CAD模型的问题。现有的多模态大语言模型在处理这类任务时，由于缺乏足够的3D空间推理能力，生成的CAD模型往往几何精度不高，且建模流程冗余复杂，难以满足工业设计的需求。

**核心思路**：论文的核心思路是通过引入几何先验信息来增强模型的3D空间推理能力，并利用强化学习来优化建模流程的简洁性。具体来说，首先利用深度图和表面法线图作为几何先验，辅助模型理解3D结构；然后，通过强化学习奖励简洁的建模序列，避免冗余操作。

**技术框架**：GACO-CAD是一个两阶段的后训练框架。第一阶段是监督微调（Supervised Fine-tuning），使用多通道输入（RGB图像、深度图、表面法线图）训练MLLM，增强其几何感知能力。第二阶段是强化学习（Reinforcement Learning），通过奖励机制鼓励生成更简洁的CAD建模序列。

**关键创新**：该方法最重要的创新点在于结合了几何先验增强和建模简洁性优化。几何先验增强通过引入深度和法线信息，显著提升了模型对3D几何的理解能力。建模简洁性优化则通过强化学习，有效减少了建模过程中的冗余操作，使得生成的CAD模型更加紧凑高效。

**关键设计**：在监督微调阶段，使用了深度图和表面法线图作为额外的输入通道，与RGB图像一起输入到MLLM中。在强化学习阶段，引入了“组长度奖励”（group length reward），该奖励与几何保真度奖励相结合，共同指导模型的训练。动态加权策略用于平衡几何保真度和建模简洁性之间的关系，稳定训练过程。

## 📊 实验亮点

GACO-CAD在DeepCAD和Fusion360数据集上取得了显著的性能提升，在代码有效性、几何精度和建模简洁性方面均优于现有方法。实验结果表明，该方法能够生成更精确、更简洁的CAD模型，证明了几何先验增强和简洁性优化策略的有效性。具体性能数据未知，但原文强调了“consistently outperforming existing methods”。

## 🎯 应用场景

GACO-CAD技术可应用于工业设计、产品建模、逆向工程等领域。通过单张图像快速生成CAD模型，能够显著降低设计门槛，提高设计效率，加速产品开发周期。该技术还有潜力应用于虚拟现实、增强现实等领域，为用户提供更便捷的3D内容创作工具。

## 📄 摘要（原文）

> Generating editable, parametric CAD models from a single image holds great potential to lower the barriers of industrial concept design. However, current multi-modal large language models (MLLMs) still struggle with accurately inferring 3D geometry from 2D images due to limited spatial reasoning capabilities. We address this limitation by introducing GACO-CAD, a novel two-stage post-training framework. It is designed to achieve a joint objective: simultaneously improving the geometric accuracy of the generated CAD models and encouraging the use of more concise modeling procedures. First, during supervised fine-tuning, we leverage depth and surface normal maps as dense geometric priors, combining them with the RGB image to form a multi-channel input. In the context of single-view reconstruction, these priors provide complementary spatial cues that help the MLLM more reliably recover 3D geometry from 2D observations. Second, during reinforcement learning, we introduce a group length reward that, while preserving high geometric fidelity, promotes the generation of more compact and less redundant parametric modeling sequences. A simple dynamic weighting strategy is adopted to stabilize training. Experiments on the DeepCAD and Fusion360 datasets show that GACO-CAD achieves state-of-the-art performance under the same MLLM backbone, consistently outperforming existing methods in terms of code validity, geometric accuracy, and modeling conciseness.

