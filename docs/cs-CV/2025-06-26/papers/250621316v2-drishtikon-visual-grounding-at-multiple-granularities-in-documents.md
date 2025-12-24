---
layout: default
title: "DRISHTIKON: Visual Grounding at Multiple Granularities in Documents"
---

# DRISHTIKON: Visual Grounding at Multiple Granularities in Documents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21316" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21316v2</a>
  <a href="https://arxiv.org/pdf/2506.21316.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21316v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21316v2', 'DRISHTIKON: Visual Grounding at Multiple Granularities in Documents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Badri Vishal Kasuba, Parag Chaudhuri, Ganesh Ramakrishnan

**分类**: cs.CV

**发布日期**: 2025-06-26 (更新: 2025-07-16)

**备注**: Work in Progress

---

## 💡 一句话要点

**提出DRISHTIKON以解决文档图像中的视觉定位问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉定位` `文档智能` `多语言处理` `视觉问答` `区域匹配算法` `多粒度分析` `大型语言模型`

## 📋 核心要点

1. 现有的视觉问答系统在处理复杂的多语言文档时，面临着视觉定位准确性不足的问题。
2. DRISHTIKON框架通过结合多语言OCR和大型语言模型，采用多粒度的区域匹配算法来解决这一问题。
3. 实验表明，DRISHTIKON在定位准确性上达到了最先进水平，尤其在行级粒度上表现最佳。

## 📝 摘要（中文）

视觉定位在文本丰富的文档图像中是一个关键但尚未充分探索的挑战，尤其在文档智能和视觉问答系统中。本文提出了DRISHTIKON，一个多粒度和多块的视觉定位框架，旨在增强复杂多语言文档的可解释性和信任度。该方法结合了多语言OCR、大型语言模型和一种新颖的区域匹配算法，以在块、行、词和点级别定位答案范围。我们引入了多粒度视觉定位基准（MGVG），这是一个经过人工标注的多样化测试集，涵盖来自各个领域的通知。实验结果表明，我们的方法在定位准确性上达到了最先进的水平，行级粒度在精度和召回率之间提供了最佳平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决文本丰富的文档图像中的视觉定位问题，现有方法在多语言和复杂文档的处理上存在准确性不足的痛点。

**核心思路**：DRISHTIKON通过多粒度和多块的视觉定位框架，结合多语言OCR和大型语言模型，设计了一种新颖的区域匹配算法，以提高定位的准确性和可解释性。

**技术框架**：该框架包括多个模块：首先进行多语言OCR处理，然后利用大型语言模型进行语义理解，最后通过区域匹配算法实现多粒度的视觉定位，涵盖块、行、词和点级别。

**关键创新**：最重要的创新点在于引入了多粒度视觉定位基准（MGVG），并通过结构化的对齐方法显著提高了定位的准确性，与现有方法相比，能够更好地处理复杂的文档结构。

**关键设计**：在技术细节上，采用了精细化的人工标注数据集，设计了适应多粒度定位的损失函数，并优化了网络结构以支持多块和多行推理。该设计确保了模型在不同粒度下的有效性和准确性。

## 📊 实验亮点

实验结果显示，DRISHTIKON在视觉定位准确性上达到了最先进的水平，行级粒度的定位精度和召回率之间的平衡最佳。与领先的视觉语言模型相比，DRISHTIKON在精确定位方面表现出明显优势，进一步验证了其结构化对齐方法的有效性。

## 🎯 应用场景

DRISHTIKON的研究成果在文档智能和视觉问答系统中具有广泛的应用潜力，能够提升多语言文档的理解和处理能力。未来，该框架可以应用于法律、医疗和教育等领域，帮助用户更高效地获取和理解信息。

## 📄 摘要（原文）

> Visual grounding in text-rich document images is a critical yet underexplored challenge for Document Intelligence and Visual Question Answering (VQA) systems. We present DRISHTIKON, a multi-granular and multi-block visual grounding framework designed to enhance interpretability and trust in VQA for complex, multilingual documents. Our approach integrates multilingual OCR, large language models, and a novel region matching algorithm to localize answer spans at the block, line, word, and point levels. We introduce the Multi-Granular Visual Grounding (MGVG) benchmark, a curated test set of diverse circular notifications from various sectors, each manually annotated with fine-grained, human-verified labels across multiple granularities. Extensive experiments show that our method achieves state-of-the-art grounding accuracy, with line-level granularity providing the best balance between precision and recall. Ablation studies further highlight the benefits of multi-block and multi-line reasoning. Comparative evaluations reveal that leading vision-language models struggle with precise localization, underscoring the effectiveness of our structured, alignment-based approach. Our findings pave the way for more robust and interpretable document understanding systems in real-world, text-centric scenarios with multi-granular grounding support. Code and dataset are made available for future research.

