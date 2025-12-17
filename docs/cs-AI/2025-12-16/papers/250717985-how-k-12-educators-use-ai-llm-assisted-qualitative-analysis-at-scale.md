---
layout: default
title: How K-12 Educators Use AI: LLM-Assisted Qualitative Analysis at Scale
---

# How K-12 Educators Use AI: LLM-Assisted Qualitative Analysis at Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.17985" class="toolbar-btn" target="_blank">📄 arXiv: 2507.17985</a>
  <a href="https://arxiv.org/pdf/2507.17985.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.17985" onclick="toggleFavorite(this, '2507.17985', 'How K-12 Educators Use AI: LLM-Assisted Qualitative Analysis at Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alex Liu, Lief Esbenshade, Shawon Sarkar, Victor Tian, Zachary Zhang, Kevin He, Min Sun

**分类**: cs.HC, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出LLM辅助的K-12教育者AI使用分析方法，用于大规模定性研究。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `教育AI` `定性分析` `K-12教育` `人机交互` `自然语言处理` `教育数据挖掘`

## 📋 核心要点

1. 现有研究缺乏对K-12教育者如何实际使用AI工具的深入理解，以及如何有效分析大规模的教育者-AI交互数据。
2. 论文提出一种LLM辅助的定性分析流程，通过LLM支持主题发现、代码本构建和大规模标注，提升分析效率和可扩展性。
3. 通过分析超过13000个教育者-AI对话，揭示了教育者使用AI进行课程设计、差异化教学等方面的具体模式。

## 📝 摘要（中文）

本研究调查了K-12教育者如何在实际教学场景中使用生成式AI工具，以及大型语言模型(LLM)如何支持对这些交互进行可扩展的定性分析。基于一个开放平台上的超过13000个未经预设的教育者-AI对话，我们考察了教育者使用AI进行课程计划、差异化教学、评估和教学反思的情况。在方法论上，我们介绍了一种可复制的、LLM辅助的定性分析流程，该流程支持归纳式主题发现、代码本开发和大规模标注，同时保持研究人员对概念综合的控制。在经验上，研究结果揭示了教育者在教学推理过程中如何提示、调整和评估AI生成的建议的具体模式。这项工作证明了将LLM支持与定性严谨性相结合，以大规模分析复杂的教育者行为并为AI驱动的教育工具的设计提供信息的可能性。

## 🔬 方法详解

**问题定义**：本研究旨在解决如何大规模分析K-12教育者与AI工具的交互数据，从而深入理解教育者如何利用AI进行教学活动。现有方法难以处理如此大规模的非结构化数据，且缺乏对教育者行为模式的细致分析。

**核心思路**：核心思路是利用LLM强大的自然语言处理能力，辅助研究人员进行定性分析。通过LLM自动提取主题、构建代码本和进行大规模标注，显著降低人工分析的成本和时间，同时保持研究人员对分析过程的控制。

**技术框架**：整体框架包含以下几个主要阶段：1) 数据收集：从开放平台收集教育者与AI的对话数据。2) LLM辅助的主题发现：利用LLM对数据进行初步分析，提取潜在的主题和模式。3) 代码本开发：研究人员基于LLM的分析结果，人工构建代码本。4) LLM辅助的大规模标注：利用LLM根据代码本对数据进行自动标注。5) 结果验证与分析：研究人员对LLM的标注结果进行抽样验证，并进行深入的定性分析。

**关键创新**：关键创新在于将LLM集成到传统的定性研究流程中，实现大规模定性分析。与完全依赖人工分析的方法相比，该方法显著提高了分析效率和可扩展性。与完全依赖LLM自动分析的方法相比，该方法保持了研究人员对分析过程的控制，确保了分析结果的可靠性和有效性。

**关键设计**：论文中没有详细描述具体的参数设置、损失函数或网络结构等技术细节。LLM的选择和prompt的设计是关键，但具体细节未知。代码本的构建和验证过程是保证分析质量的关键环节，具体流程未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.17985/Figure_1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.17985/Figure_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.17985/item.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

研究分析了超过13000个教育者-AI对话，揭示了教育者在课程计划、差异化教学、评估和教学反思等方面使用AI的具体模式。研究结果表明，教育者能够有效地利用AI生成建议，并根据实际情况进行调整和评估。具体的性能数据和提升幅度未知。

## 🎯 应用场景

该研究成果可应用于教育领域，帮助教育工作者更好地理解如何利用AI工具提升教学效果。此外，该方法论可推广到其他领域，例如医疗、金融等，用于分析大规模的文本数据，挖掘潜在的模式和规律，为决策提供支持。未来，可以基于此研究开发AI辅助的教育工具，为教育者提供个性化的教学建议和支持。

## 📄 摘要（原文）

> This study investigates how K-12 educators use generative AI tools in real-world instructional contexts and how large language models (LLMs) can support scalable qualitative analysis of these interactions. Drawing on over 13,000 unscripted educator-AI conversations from an open-access platform, we examine educators' use of AI for lesson planning, differentiation, assessment, and pedagogical reflection. Methodologically, we introduce a replicable, LLM-assisted qualitative analysis pipeline that supports inductive theme discovery, codebook development, and large-scale annotation while preserving researcher control over conceptual synthesis. Empirically, the findings surface concrete patterns in how educators prompt, adapt, and evaluate AI-generated suggestions as part of their instructional reasoning. This work demonstrates the feasibility of combining LLM support with qualitative rigor to analyze complex educator behaviors at scale and inform the design of AI-powered educational tools.

