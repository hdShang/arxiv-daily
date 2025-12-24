---
layout: default
title: "PosterO: Structuring Layout Trees to Enable Language Models in Generalized Content-Aware Layout Generation"
---

# PosterO: Structuring Layout Trees to Enable Language Models in Generalized Content-Aware Layout Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07843" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07843v2</a>
  <a href="https://arxiv.org/pdf/2505.07843.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07843v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07843v2', 'PosterO: Structuring Layout Trees to Enable Language Models in Generalized Content-Aware Layout Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: HsiaoYuan Hsu, Yuxin Peng

**分类**: cs.GR, cs.LG

**发布日期**: 2025-05-06 (更新: 2025-05-27)

**备注**: Accepted to CVPR 2025. Minor editing issue fixed. Code and dataset are available at https://thekinsley.github.io/PosterO/

---

## 💡 一句话要点

**提出PosterO以解决海报设计中的布局生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `海报设计` `内容感知` `布局生成` `大型语言模型` `多样性` `SVG结构` `设计意图`

## 📋 核心要点

1. 现有方法在布局生成中主要集中于图像增强，忽视了布局多样性，难以处理形状变化和设计意图多样化的问题。
2. 本文提出PosterO，通过将布局结构化为树形结构，利用大型语言模型进行上下文学习，从而生成多用途海报。
3. 实验结果显示，PosterO在多个基准测试中达到了新的最先进性能，生成的布局在视觉上也更具吸引力。

## 📝 摘要（中文）

在海报设计中，内容感知的布局生成对于自动排列视觉文本元素至关重要。现有方法主要集中于图像中心的增强，忽视了布局的多样性，无法应对形状变化元素或多样化设计意图。为此，本文提出了一种布局中心的方法PosterO，利用大型语言模型（LLMs）隐含的布局知识，创建多用途海报。具体而言，PosterO通过通用形状、设计意图向量化和层次节点表示，将数据集中的布局结构化为SVG语言的树形结构。在推理过程中，利用LLMs进行上下文学习，预测新的布局树。实验结果表明，PosterO在多个基准测试中实现了新的最先进性能，并生成了视觉上吸引人的布局。为进一步探索PosterO在广义设置下的能力，本文构建了PStylish7数据集，提供了多用途海报和各种形状元素的挑战性测试。

## 🔬 方法详解

**问题定义**：本文旨在解决海报设计中内容感知布局生成的挑战，现有方法因过于依赖图像增强而无法应对布局多样性和形状变化元素的问题。

**核心思路**：提出PosterO，通过将布局知识结构化为树形结构，并利用大型语言模型进行上下文学习，以生成符合多样化设计意图的海报布局。

**技术框架**：整体架构包括三个主要模块：布局结构化模块（将布局转化为SVG树形结构）、LLM推理模块（进行上下文学习和布局预测）、以及海报生成模块（将生成的布局实现为实际海报设计）。

**关键创新**：最重要的创新在于利用大型语言模型的上下文学习能力，结合设计意图向量化和层次节点表示，显著提升了布局生成的灵活性和多样性。

**关键设计**：在技术细节上，采用了SVG格式进行布局表示，设计意图通过向量化进行编码，LLM的选择和训练策略也经过精心设计，以确保生成的布局符合预期的设计意图。

## 📊 实验亮点

实验结果表明，PosterO在多个基准测试中实现了新的最先进性能，相较于现有方法，布局生成的视觉吸引力显著提升，具体性能数据尚未公开。该方法在处理多样化设计意图和形状变化元素方面表现出色，展示了其在实际应用中的潜力。

## 🎯 应用场景

PosterO的研究成果在广告、市场营销、社交媒体内容创作等领域具有广泛的应用潜力。通过自动化生成符合特定设计意图的海报布局，可以大幅提升设计效率，降低人力成本。此外，该方法的灵活性使其能够适应不同的设计需求，推动个性化内容创作的发展。

## 📄 摘要（原文）

> In poster design, content-aware layout generation is crucial for automatically arranging visual-textual elements on the given image. With limited training data, existing work focused on image-centric enhancement. However, this neglects the diversity of layouts and fails to cope with shape-variant elements or diverse design intents in generalized settings. To this end, we proposed a layout-centric approach that leverages layout knowledge implicit in large language models (LLMs) to create posters for omnifarious purposes, hence the name PosterO. Specifically, it structures layouts from datasets as trees in SVG language by universal shape, design intent vectorization, and hierarchical node representation. Then, it applies LLMs during inference to predict new layout trees by in-context learning with intent-aligned example selection. After layout trees are generated, we can seamlessly realize them into poster designs by editing the chat with LLMs. Extensive experimental results have demonstrated that PosterO can generate visually appealing layouts for given images, achieving new state-of-the-art performance across various benchmarks. To further explore PosterO's abilities under the generalized settings, we built PStylish7, the first dataset with multi-purpose posters and various-shaped elements, further offering a challenging test for advanced research.

