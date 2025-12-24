---
layout: default
title: "VLM-FO1: Bridging the Gap Between High-Level Reasoning and Fine-Grained Perception in VLMs"
---

# VLM-FO1: Bridging the Gap Between High-Level Reasoning and Fine-Grained Perception in VLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25916" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25916v1</a>
  <a href="https://arxiv.org/pdf/2509.25916.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25916v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25916v1', 'VLM-FO1: Bridging the Gap Between High-Level Reasoning and Fine-Grained Perception in VLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peng Liu, Haozhan Shen, Chunxin Fang, Zhicheng Sun, Jiajia Liao, Tiancheng Zhao

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-30

**备注**: 22 pages

---

## 💡 一句话要点

**VLM-FO1：通过特征检索弥合VLM高层推理与细粒度感知之间的差距**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `细粒度感知` `特征检索` `对象定位` `区域理解` `混合编码器` `双阶段训练`

## 📋 核心要点

1. 现有VLM在细粒度感知任务中表现不佳，因为难以生成精确的数值坐标。
2. VLM-FO1将对象感知重构为特征检索任务，避免了直接坐标生成，提升了鲁棒性。
3. VLM-FO1在多个基准测试中达到SOTA，且不影响VLM的通用视觉理解能力。

## 📝 摘要（中文）

视觉-语言模型(VLM)擅长高层场景理解，但在需要精确定位的细粒度感知任务中表现不佳。这种失败源于根本的不匹配，因为生成精确的数值坐标对于以语言为中心的架构来说是一项具有挑战性的任务。本文介绍了一种新颖的框架VLM-FO1，通过将以对象为中心的感知从脆弱的坐标生成问题重新定义为鲁棒的特征检索任务，从而克服了这一限制。我们的方法作为一个即插即用模块运行，可以与任何预训练的VLM集成。它利用混合细粒度区域编码器(HFRE)，具有双视觉编码器，以生成富含语义和空间细节的强大区域tokens。然后，基于token的引用系统使LLM能够无缝地推理和将语言定位在这些特定的视觉区域中。实验表明，VLM-FO1在一系列不同的基准测试中实现了最先进的性能，展示了在对象定位、区域生成理解和视觉区域推理方面的卓越能力。至关重要的是，我们的两阶段训练策略确保了这些感知增益的实现不会损害基础模型的一般视觉理解能力。VLM-FO1为构建具有感知能力的VLM建立了一种有效而灵活的范例，弥合了高层推理和细粒度视觉定位之间的差距。

## 🔬 方法详解

**问题定义**：现有的视觉-语言模型（VLMs）在高层次的场景理解方面表现出色，但在需要精确定位的细粒度感知任务中存在不足。主要痛点在于，语言模型难以直接生成精确的数值坐标，这使得VLM在对象定位、区域理解等任务中面临挑战。

**核心思路**：VLM-FO1的核心思路是将细粒度感知任务从坐标生成问题转化为特征检索问题。不再要求模型直接预测坐标，而是让模型从视觉特征空间中检索与语言描述最相关的区域特征。这种方法更符合语言模型的优势，也更具鲁棒性。

**技术框架**：VLM-FO1是一个即插即用的模块，可以集成到任何预训练的VLM中。其主要组成部分包括：1) 混合细粒度区域编码器（HFRE）：使用双视觉编码器提取区域的语义和空间特征。2) 基于Token的引用系统：允许LLM通过tokens引用特定的视觉区域，从而进行推理和定位。整体流程是，首先HFRE对图像区域进行编码，生成区域tokens；然后，LLM结合语言输入和区域tokens进行推理，完成对象定位、区域理解等任务。

**关键创新**：VLM-FO1最重要的创新点在于将细粒度感知任务重新定义为特征检索问题。这种重构避免了语言模型直接生成坐标的困难，充分利用了语言模型在语义理解和推理方面的优势。此外，HFRE的设计也保证了区域特征包含丰富的语义和空间信息。

**关键设计**：VLM-FO1采用两阶段训练策略。第一阶段，训练HFRE，使其能够生成高质量的区域特征。第二阶段，将HFRE集成到预训练的VLM中，并进行微调，以适应新的特征检索任务。HFRE使用了双视觉编码器，分别提取语义和空间特征，并通过融合机制将两者结合起来。损失函数的设计旨在鼓励模型学习到能够区分不同区域的特征表示。

## 📊 实验亮点

VLM-FO1在多个基准测试中取得了SOTA性能，证明了其有效性。例如，在对象定位任务中，VLM-FO1的精度比现有方法提高了显著的百分比。此外，VLM-FO1的通用视觉理解能力没有受到影响，这表明其具有良好的泛化能力。

## 🎯 应用场景

VLM-FO1具有广泛的应用前景，例如智能客服、自动驾驶、机器人导航、图像编辑等。它可以提升VLM在需要精确定位的任务中的性能，例如目标检测、图像分割、视觉问答等。未来，VLM-FO1可以与其他技术结合，例如3D视觉、知识图谱等，以实现更复杂的应用场景。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) excel at high-level scene understanding but falter on fine-grained perception tasks requiring precise localization. This failure stems from a fundamental mismatch, as generating exact numerical coordinates is a challenging task for language-centric architectures. In this paper, we introduce VLM-FO1, a novel framework that overcomes this limitation by reframing object-centric perception from a brittle coordinate generation problem into a robust feature retrieval task. Our method operates as a plug-and-play module that integrates with any pre-trained VLM. It leverages a Hybrid Fine-grained Region Encoder (HFRE), featuring a dual vision encoder, to generate powerful region tokens rich in both semantic and spatial detail. A token-based referencing system then enables the LLM to seamlessly reason about and ground language in these specific visual regions. Experiments show that VLM-FO1 achieves state-of-the-art performance across a diverse suite of benchmarks, demonstrating exceptional capabilities in object grounding, region generational understanding, and visual region reasoning. Crucially, our two-stage training strategy ensures that these perception gains are achieved without compromising the base model's general visual understanding capabilities. VLM-FO1 establishes an effective and flexible paradigm for building perception-aware VLMs, bridging the gap between high-level reasoning and fine-grained visual grounding.

