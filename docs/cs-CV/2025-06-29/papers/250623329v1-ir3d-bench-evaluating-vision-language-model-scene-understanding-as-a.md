---
layout: default
title: "IR3D-Bench: Evaluating Vision-Language Model Scene Understanding as Agentic Inverse Rendering"
---

# IR3D-Bench: Evaluating Vision-Language Model Scene Understanding as Agentic Inverse Rendering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23329" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23329v1</a>
  <a href="https://arxiv.org/pdf/2506.23329.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23329v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23329v1', 'IR3D-Bench: Evaluating Vision-Language Model Scene Understanding as Agentic Inverse Rendering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Parker Liu, Chenxin Li, Zhengxin Li, Yipeng Wu, Wuyang Li, Zhiqin Yang, Zhenyuan Zhang, Yunlong Lin, Sirui Han, Brandon Y. Feng

**分类**: cs.CV

**发布日期**: 2025-06-29

**备注**: Project Page: https://ir3d-bench.github.io/

---

## 💡 一句话要点

**提出IR3D-Bench以解决视觉语言模型场景理解不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `场景理解` `逆渲染` `工具使用` `生成能力` `3D重建` `评估指标`

## 📋 核心要点

1. 现有的视觉语言模型在场景理解方面主要依赖被动识别，缺乏主动创造能力。
2. IR3D-Bench通过要求模型使用工具重建3D结构，推动了“通过创造理解”的新方法。
3. 初步实验表明，尽管工具使用能力良好，但在视觉精度方面仍有待提升。

## 📝 摘要（中文）

视觉语言模型（VLMs）在描述性任务中表现出色，但它们是否真正理解视觉观察中的场景仍然不确定。我们引入了IR3D-Bench，一个基准挑战VLMs通过主动创造而非被动识别来展示理解能力。基于分析-合成范式，IR3D-Bench要求视觉语言代理（VLAs）主动使用编程和渲染工具重建输入图像的3D结构，实现工具使用下的逆渲染。这种“通过创造理解”的方法探讨了VLAs的工具使用生成能力，超越了传统场景理解基准所测量的描述性或对话能力。我们提供了一套全面的指标来评估几何准确性、空间关系、外观属性和整体可信度。初步实验显示，尽管当前的VLMs在工具使用方面表现良好，但在视觉精度上仍存在局限性。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有视觉语言模型在场景理解中的不足，特别是它们在被动识别场景时缺乏主动创造能力的问题。

**核心思路**：论文提出通过IR3D-Bench基准，要求视觉语言代理主动使用编程和渲染工具重建输入图像的3D结构，从而实现工具使用下的逆渲染。这种方法强调“通过创造理解”的理念，旨在提升模型的生成能力。

**技术框架**：IR3D-Bench的整体架构包括数据收集、工具使用、3D重建和评估四个主要模块。模型首先接收输入图像，然后利用编程和渲染工具进行3D结构的重建，最后通过一系列指标进行评估。

**关键创新**：该研究的主要创新在于引入了“理解-创造”这一新范式，突破了传统场景理解的限制，强调了工具使用的生成能力。这与以往仅依赖描述性任务的模型形成鲜明对比。

**关键设计**：在设计上，IR3D-Bench使用了一套全面的评估指标，包括几何准确性、空间关系和外观属性等，以确保对模型生成能力的全面评估。

## 📊 实验亮点

初步实验显示，尽管当前的视觉语言模型在工具使用方面表现良好，但在视觉精度上仍存在显著局限。具体而言，模型在几何准确性和空间关系的重建上未能达到预期效果，提示未来研究需聚焦于提升视觉精度。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和自动化设计等。通过提升视觉语言模型的场景理解能力，可以在这些领域实现更高效的内容生成和交互体验，推动智能代理的发展。

## 📄 摘要（原文）

> Vision-language models (VLMs) excel at descriptive tasks, but whether they truly understand scenes from visual observations remains uncertain. We introduce IR3D-Bench, a benchmark challenging VLMs to demonstrate understanding through active creation rather than passive recognition. Grounded in the analysis-by-synthesis paradigm, IR3D-Bench tasks Vision-Language Agents (VLAs) with actively using programming and rendering tools to recreate the underlying 3D structure of an input image, achieving agentic inverse rendering through tool use. This "understanding-by-creating" approach probes the tool-using generative capacity of VLAs, moving beyond the descriptive or conversational capacity measured by traditional scene understanding benchmarks. We provide a comprehensive suite of metrics to evaluate geometric accuracy, spatial relations, appearance attributes, and overall plausibility. Initial experiments on agentic inverse rendering powered by various state-of-the-art VLMs highlight current limitations, particularly in visual precision rather than basic tool usage. IR3D-Bench, including data and evaluation protocols, is released to facilitate systematic study and development of tool-using VLAs towards genuine scene understanding by creating.

