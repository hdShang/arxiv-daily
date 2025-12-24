---
layout: default
title: "Human-in-the-Loop: Quantitative Evaluation of 3D Models Generation by Large Language Models"
---

# Human-in-the-Loop: Quantitative Evaluation of 3D Models Generation by Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07010" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07010v1</a>
  <a href="https://arxiv.org/pdf/2509.07010.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07010v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07010v1', 'Human-in-the-Loop: Quantitative Evaluation of 3D Models Generation by Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmed R. Sadik, Mariusz Bujny

**分类**: cs.CV, cs.AI, cs.ET

**发布日期**: 2025-09-06

---

## 💡 一句话要点

**提出人机闭环框架，量化评估大语言模型生成3D模型质量，加速CAD设计。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D模型生成` `大型语言模型` `人机闭环` `定量评估` `CAD设计`

## 📋 核心要点

1. 现有方法缺乏对LLM生成3D模型的几何和结构保真度的有效评估手段，阻碍了其在CAD领域的应用。
2. 提出人机闭环框架，通过量化指标（体积精度、表面对齐等）对比生成模型与真实CAD模型，实现客观评估。
3. 实验表明，更丰富的语义输入（如代码提示）能显著提升生成模型的保真度，且定量评估加速了模型优化。

## 📝 摘要（中文）

本文提出了一种人机闭环框架，用于定量评估大型语言模型（LLM）生成的3D模型，旨在支持CAD设计的普及化、传统设计的逆向工程和快速原型设计等应用。该框架包含一套全面的相似性和复杂度指标，包括体积精度、表面对齐、尺寸保真度和拓扑复杂性，用于将生成的模型与真实CAD参考模型进行基准测试。以L型支架组件为例，系统地比较了LLM在四种输入模态下的性能：2D正交视图、等距草图、几何结构树和基于代码的校正提示。研究结果表明，随着语义丰富度的增加，生成保真度得到提高，代码级别的提示在所有指标上都实现了完美的重建。这项工作的主要贡献在于证明了所提出的定量评估方法能够显著加快收敛到真实模型的速度，特别是与仅基于视觉检查和人类直觉的传统定性方法相比。这项工作不仅加深了对AI辅助形状合成的理解，而且为验证和改进各种CAD应用的生成模型提供了一种可扩展的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）生成3D模型后，如何对其几何和结构保真度进行有效、定量评估的问题。现有方法主要依赖人工视觉检查，主观性强、效率低，难以支持LLM在CAD设计、逆向工程等领域的应用。因此，需要一种客观、可扩展的评估方法，以促进LLM生成3D模型的优化和应用。

**核心思路**：论文的核心思路是引入“人机闭环”的概念，通过设计一系列量化指标，将LLM生成的3D模型与真实CAD模型进行对比，从而实现对生成模型质量的客观评估。这种方法不仅可以减少主观偏差，还可以为LLM的训练和优化提供有效的反馈信号。

**技术框架**：该框架主要包含以下几个模块：1) LLM生成3D模型：根据不同的输入模态（2D视图、草图、结构树、代码提示）生成3D模型；2) 量化指标计算：计算生成模型与真实CAD模型之间的体积精度、表面对齐、尺寸保真度和拓扑复杂性等指标；3) 人机闭环优化：根据量化指标的结果，对LLM进行调整和优化，提高生成模型的质量。整个流程形成一个闭环，不断迭代优化。

**关键创新**：论文的关键创新在于提出了一个全面的定量评估体系，用于评估LLM生成的3D模型。该体系不仅考虑了几何相似性，还考虑了拓扑复杂性等因素，能够更全面地反映生成模型的质量。此外，论文还证明了定量评估方法能够显著加快模型优化速度，优于传统的定性评估方法。

**关键设计**：论文中，体积精度通过计算生成模型与真实模型之间的体积差异来衡量；表面对齐通过计算两个模型之间的点云距离来衡量；尺寸保真度通过比较关键尺寸参数来衡量；拓扑复杂性则通过分析模型的B-rep结构来衡量。具体参数设置和阈值根据具体应用场景进行调整。

## 📊 实验亮点

实验结果表明，使用代码级别的提示作为输入，LLM在所有评估指标上都实现了完美的3D模型重建。此外，与传统的基于视觉检查的定性评估方法相比，所提出的定量评估方法能够显著加快模型优化速度，实现更快地收敛到真实模型。

## 🎯 应用场景

该研究成果可应用于CAD设计的普及化，降低设计门槛；在逆向工程中，可快速重建现有产品模型；在快速原型设计中，可加速产品迭代过程。通过量化评估，可以更有效地训练和优化LLM，使其生成更高质量的3D模型，从而推动AI在制造业和设计领域的应用。

## 📄 摘要（原文）

> Large Language Models are increasingly capable of interpreting multimodal inputs to generate complex 3D shapes, yet robust methods to evaluate geometric and structural fidelity remain underdeveloped. This paper introduces a human in the loop framework for the quantitative evaluation of LLM generated 3D models, supporting applications such as democratization of CAD design, reverse engineering of legacy designs, and rapid prototyping. We propose a comprehensive suite of similarity and complexity metrics, including volumetric accuracy, surface alignment, dimensional fidelity, and topological intricacy, to benchmark generated models against ground truth CAD references. Using an L bracket component as a case study, we systematically compare LLM performance across four input modalities: 2D orthographic views, isometric sketches, geometric structure trees, and code based correction prompts. Our findings demonstrate improved generation fidelity with increased semantic richness, with code level prompts achieving perfect reconstruction across all metrics. A key contribution of this work is demonstrating that our proposed quantitative evaluation approach enables significantly faster convergence toward the ground truth, especially compared to traditional qualitative methods based solely on visual inspection and human intuition. This work not only advances the understanding of AI assisted shape synthesis but also provides a scalable methodology to validate and refine generative models for diverse CAD applications.

