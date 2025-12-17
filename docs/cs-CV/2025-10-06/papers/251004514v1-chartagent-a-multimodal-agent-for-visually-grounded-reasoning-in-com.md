---
layout: default
title: ChartAgent: A Multimodal Agent for Visually Grounded Reasoning in Complex Chart Question Answering
---

# ChartAgent: A Multimodal Agent for Visually Grounded Reasoning in Complex Chart Question Answering

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.04514" target="_blank" class="toolbar-btn">arXiv: 2510.04514v1</a>
    <a href="https://arxiv.org/pdf/2510.04514.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04514v1" 
            onclick="toggleFavorite(this, '2510.04514v1', 'ChartAgent: A Multimodal Agent for Visually Grounded Reasoning in Complex Chart Question Answering')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Rachneet Kaur, Nishan Srishankar, Zhen Zeng, Sumitra Ganesh, Manuela Veloso

**分类**: cs.AI, cs.CE, cs.CL, cs.CV, stat.ME

**发布日期**: 2025-10-06

**备注**: 53 pages, 12 figures, 15 tables

---

## 💡 一句话要点

**提出ChartAgent，通过视觉推理解决复杂图表问答中未标注图表的理解难题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图表问答` `视觉推理` `多模态Agent` `工具增强` `未标注图表`

## 📋 核心要点

1. 现有方法在基于图表的视觉问答中，对未标注图表的精确视觉理解能力不足。
2. ChartAgent通过迭代分解查询为视觉子任务，并使用图表特定工具与图像交互，实现视觉推理。
3. 实验表明，ChartAgent在多个基准测试中显著提升了性能，尤其是在未标注图表上。

## 📝 摘要（中文）

本文提出ChartAgent，一种新颖的agent框架，用于在复杂图表问答中执行视觉推理。与文本思维链推理不同，ChartAgent将查询迭代分解为视觉子任务，并通过专门的动作（如绘制注释、裁剪区域和定位轴）与图表图像进行交互。它利用图表特定的视觉工具库来完成每个子任务，模拟人类的图表理解认知策略。ChartAgent在ChartBench和ChartX基准测试中取得了最先进的准确率，总体上超越了现有方法高达16.07%，在未标注的、数值密集型查询上超越了17.31%。分析表明，ChartAgent在不同的图表类型中有效，在不同的视觉和推理复杂度级别上取得了最高的分数，并且可以作为一个即插即用的框架来提高不同底层LLM的性能。这项工作是首批展示使用工具增强的多模态agent进行图表理解的视觉基础推理的研究之一。

## 🔬 方法详解

**问题定义**：论文旨在解决复杂图表问答中，现有方法在处理未标注图表时性能显著下降的问题。现有方法通常依赖于文本捷径，缺乏直接在图表的空间域中进行视觉推理的能力，导致对数值密集型和需要精细视觉理解的查询表现不佳。

**核心思路**：ChartAgent的核心思路是模仿人类理解图表的认知过程，将复杂的查询分解为一系列可执行的视觉子任务。通过与图表图像进行交互，例如绘制注释、裁剪区域和定位坐标轴，agent能够逐步提取所需的信息，从而完成问答任务。这种基于视觉操作的推理方式避免了对文本信息的过度依赖，提高了对未标注图表的理解能力。

**技术框架**：ChartAgent的整体框架包含以下几个主要模块：1) 查询分解模块：将用户提出的复杂问题分解为一系列更小的、可执行的视觉子任务。2) 工具选择模块：根据当前子任务的需求，从预定义的图表特定视觉工具库中选择合适的工具。3) 视觉操作模块：利用选定的工具对图表图像进行操作，例如绘制注释、裁剪区域、定位坐标轴等。4) 信息提取模块：从操作后的图像中提取相关信息。5) 答案生成模块：根据提取的信息生成最终答案。整个流程是迭代进行的，直到所有子任务都完成，并生成最终答案。

**关键创新**：ChartAgent最重要的技术创新点在于其显式的视觉推理机制。与传统的基于文本的思维链推理不同，ChartAgent直接在图表的空间域中进行操作，通过与图像的交互来提取信息。这种视觉基础的推理方式更符合人类的认知过程，并且能够更好地处理未标注的图表。此外，ChartAgent的工具库包含了多种图表特定的视觉工具，使其能够灵活地应对各种复杂的图表问答任务。

**关键设计**：ChartAgent的关键设计包括：1) 图表特定视觉工具库的设计，包含了各种常用的图表操作，例如绘制注释、裁剪区域、定位坐标轴等。2) 查询分解策略的设计，需要将复杂问题分解为一系列可执行的视觉子任务，并且保证子任务之间的逻辑关系。3) 工具选择策略的设计，需要根据当前子任务的需求，选择合适的工具。4) 奖励函数的设计，用于训练agent学习如何有效地利用工具来完成任务。（具体参数设置、损失函数、网络结构等技术细节在论文中未详细说明，属于未知信息。）

## 📊 实验亮点

ChartAgent在ChartBench和ChartX基准测试中取得了显著的性能提升，总体上超越了现有方法高达16.07%，在未标注的、数值密集型查询上超越了17.31%。实验结果表明，ChartAgent在不同的图表类型和复杂度级别上都表现出色，并且可以作为一个即插即用的框架来提高不同底层LLM的性能。

## 🎯 应用场景

ChartAgent可应用于商业智能、数据分析、教育等领域，帮助用户更好地理解和利用图表数据。例如，在商业智能中，ChartAgent可以自动分析销售数据图表，为决策者提供洞察；在教育领域，它可以帮助学生理解复杂的科学图表。未来，ChartAgent有望成为一种通用的图表理解工具，赋能各行各业。

## 📄 摘要（原文）

> Recent multimodal LLMs have shown promise in chart-based visual question answering, but their performance declines sharply on unannotated charts, those requiring precise visual interpretation rather than relying on textual shortcuts. To address this, we introduce ChartAgent, a novel agentic framework that explicitly performs visual reasoning directly within the chart's spatial domain. Unlike textual chain-of-thought reasoning, ChartAgent iteratively decomposes queries into visual subtasks and actively manipulates and interacts with chart images through specialized actions such as drawing annotations, cropping regions (e.g., segmenting pie slices, isolating bars), and localizing axes, using a library of chart-specific vision tools to fulfill each subtask. This iterative reasoning process closely mirrors human cognitive strategies for chart comprehension. ChartAgent achieves state-of-the-art accuracy on the ChartBench and ChartX benchmarks, surpassing prior methods by up to 16.07% absolute gain overall and 17.31% on unannotated, numerically intensive queries. Furthermore, our analyses show that ChartAgent is (a) effective across diverse chart types, (b) achieve the highest scores across varying visual and reasoning complexity levels, and (c) serves as a plug-and-play framework that boosts performance across diverse underlying LLMs. Our work is among the first to demonstrate visually grounded reasoning for chart understanding using tool-augmented multimodal agents.

