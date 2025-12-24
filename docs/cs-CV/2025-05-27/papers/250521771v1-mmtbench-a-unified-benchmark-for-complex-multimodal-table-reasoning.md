---
layout: default
title: "MMTBENCH: A Unified Benchmark for Complex Multimodal Table Reasoning"
---

# MMTBENCH: A Unified Benchmark for Complex Multimodal Table Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21771" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21771v1</a>
  <a href="https://arxiv.org/pdf/2505.21771.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21771v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21771v1', 'MMTBENCH: A Unified Benchmark for Complex Multimodal Table Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prasham Yatinkumar Titiya, Jainil Trivedi, Chitta Baral, Vivek Gupta

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出MMTBENCH以解决复杂多模态表推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态表推理` `视觉语言模型` `基准测试` `数据分析` `机器学习`

## 📋 核心要点

1. 现有的视觉语言模型在处理复杂的多模态表推理时表现不佳，尤其是在需要视觉推理和多步推理的问题上。
2. 本文提出MMTBENCH基准，包含500个多模态表格及4021个问答对，以评估和推动多模态表推理的研究。
3. 实验结果显示，当前最先进的模型在多模态表推理上存在显著性能差距，特别是在视觉推理和多步推理方面。

## 📝 摘要（中文）

多模态表格结合了半结构化数据与视觉元素，如图表和地图，广泛存在于现实世界中，但对现有的视觉语言模型（VLMs）构成了重大挑战。尽管大型语言模型（LLMs）和VLMs在文本和图像理解方面表现出色，但它们在复杂的现实世界多模态表推理上的表现仍未得到充分探索。为填补这一空白，本文提出了MMTBENCH（多模态表基准），该基准包含500个来自多样化现实世界来源的多模态表格，共有4021个问答对，涵盖四种问题类型和五种推理类型。对现有模型的广泛评估显示，在需要视觉推理和多步推理的问题上存在显著的性能差距，强调了改进架构的迫切需求。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言模型在复杂多模态表推理中的不足，尤其是在视觉推理和多步推理方面的挑战。

**核心思路**：提出MMTBENCH基准，通过提供真实世界的多模态表格和多样化的问答对，来评估和推动多模态表推理的研究，促进模型在此领域的改进。

**技术框架**：MMTBENCH基准包括500个多模态表格，涵盖四种问题类型（显式、隐式、答案提及和基于视觉的问题）和五种推理类型（数学、极值识别、事实验证、基于视觉的推理及其他），为模型评估提供全面的测试场景。

**关键创新**：MMTBENCH的创新在于其综合性和多样性，提供了一个高质量的资源，反映现实世界任务的复杂性，填补了现有基准的空白。

**关键设计**：在设计MMTBENCH时，考虑了多种表格类型（单/多实体、带实体的地图和图表、单/多图表、地图和可视化），确保了基准的全面性和挑战性。每个问题类型和推理类型的设计都旨在考察模型在不同场景下的表现。

## 📊 实验亮点

实验结果显示，当前最先进的模型在MMTBENCH基准上的表现存在显著差距，尤其是在视觉推理和多步推理方面，强调了对新架构的需求。这一发现为未来的研究指明了方向。

## 🎯 应用场景

该研究的潜在应用领域包括数据分析、商业智能、教育和医疗等多个领域，能够帮助用户更好地理解和利用复杂的多模态数据。未来，MMTBENCH有望成为多模态表推理研究的标准基准，推动相关技术的发展。

## 📄 摘要（原文）

> Multimodal tables those that integrate semi structured data with visual elements such as charts and maps are ubiquitous across real world domains, yet they pose a formidable challenge to current vision language models (VLMs). While Large Language models (LLMs) and VLMs have demonstrated strong capabilities in text and image understanding, their performance on complex, real world multimodal table reasoning remains unexplored. To bridge this gap, we introduce MMTBENCH (Multimodal Table Benchmark), a benchmark consisting of 500 real world multimodal tables drawn from diverse real world sources, with a total of 4021 question answer pairs. MMTBENCH questions cover four question types (Explicit, Implicit, Answer Mention, and Visual Based), five reasoning types (Mathematical, Extrema Identification, Fact Verification, Vision Based, and Others), and eight table types (Single/Multiple Entity, Maps and Charts with Entities, Single/Multiple Charts, Maps, and Visualizations). Extensive evaluation of state of the art models on all types reveals substantial performance gaps, particularly on questions requiring visual-based reasoning and multi-step inference. These findings show the urgent need for improved architectures that more tightly integrate vision and language processing. By providing a challenging, high-quality resource that mirrors the complexity of real-world tasks, MMTBENCH underscores its value as a resource for future research on multimodal tables.

