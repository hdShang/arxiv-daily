---
layout: default
title: Factuality Matters: When Image Generation and Editing Meet Structured Visuals
---

# Factuality Matters: When Image Generation and Editing Meet Structured Visuals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.05091" class="toolbar-btn" target="_blank">📄 arXiv: 2510.05091v1</a>
  <a href="https://arxiv.org/pdf/2510.05091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05091v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.05091v1', 'Factuality Matters: When Image Generation and Editing Meet Structured Visuals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Zhuo, Songhao Han, Yuandong Pu, Boxiang Qiu, Sayak Paul, Yue Liao, Yihao Liu, Jie Shao, Xi Chen, Si Liu, Hongsheng Li

**分类**: cs.CV

**发布日期**: 2025-10-06

**备注**: Project page: https://structvisuals.github.io

---

## 💡 一句话要点

**针对结构化视觉生成与编辑的事实性问题，提出StructBench基准和多模态融合模型。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `结构化视觉` `图像生成` `图像编辑` `多模态融合` `事实性` `知识推理`

## 📋 核心要点

1. 现有视觉生成模型难以处理结构化视觉内容，缺乏对组合规划、文本渲染和多模态推理能力。
2. 提出一种统一模型，集成VLM和FLUX.1 Kontext，通过三阶段训练课程增强特征对齐、知识注入和推理能力。
3. 构建StructBench基准和StructScore指标，实验表明该模型在结构化视觉编辑任务上表现出色，推理时推理带来持续提升。

## 📝 摘要（中文）

现代视觉生成模型在创建美观的自然图像方面表现出色，但在生成或编辑结构化视觉内容（如图表、示意图和数学图形）时面临挑战，这些内容需要组合规划、文本渲染和多模态推理以保证事实准确性。为了解决这个问题，我们对该领域进行了首次全面、系统的研究，包括数据构建、模型训练和评估基准。首先，我们构建了一个包含130万高质量结构化图像对的大规模数据集，这些图像对来自可执行的绘图程序，并使用思维链推理注释进行了增强。在此基础上，我们训练了一个统一的模型，该模型通过轻量级连接器将VLM与FLUX.1 Kontext集成，以增强多模态理解。一个三阶段的训练课程实现了渐进式特征对齐、知识注入和推理增强生成，并在推理时通过外部推理器进一步提升。最后，我们引入了StructBench，这是一个用于生成和编辑的新基准，包含超过1700个具有挑战性的实例，以及一个配套的评估指标StructScore，它采用多轮问答协议来评估细粒度的事实准确性。对15个模型的评估表明，即使是领先的闭源系统也远未达到令人满意的水平。我们的模型获得了强大的编辑性能，并且推理时推理在各种架构中都产生了持续的收益。通过发布数据集、模型和基准，我们旨在推进结构化视觉的统一多模态基础。

## 🔬 方法详解

**问题定义**：现有视觉生成模型在处理结构化视觉内容时，难以保证生成或编辑结果的事实准确性。这些结构化视觉内容，例如图表、示意图和数学图形，需要模型具备组合规划、文本渲染和多模态推理能力。现有方法通常无法很好地处理这些需求，导致生成结果在语义上不准确或与原始意图不符。

**核心思路**：论文的核心思路是构建一个统一的多模态模型，该模型能够理解结构化视觉内容的内在结构和语义信息，并利用外部推理器来增强生成和编辑过程中的事实准确性。通过将视觉语言模型（VLM）与FLUX.1 Kontext集成，并采用三阶段训练课程，模型能够逐步学习特征对齐、知识注入和推理增强生成。

**技术框架**：整体框架包含数据构建、模型训练和评估基准三个主要部分。数据构建阶段创建了一个包含130万高质量结构化图像对的大规模数据集，并使用思维链推理注释进行增强。模型训练阶段采用三阶段训练课程，包括特征对齐、知识注入和推理增强生成。评估基准阶段引入了StructBench和StructScore，用于评估模型在生成和编辑任务中的事实准确性。

**关键创新**：论文的关键创新在于以下几个方面：1) 首次全面、系统地研究了结构化视觉生成与编辑的事实性问题；2) 构建了一个大规模、高质量的结构化图像数据集，并提供了思维链推理注释；3) 提出了一个统一的多模态模型，该模型能够有效地处理结构化视觉内容；4) 引入了StructBench和StructScore，为结构化视觉生成与编辑提供了一个新的评估基准。

**关键设计**：模型采用轻量级连接器将VLM与FLUX.1 Kontext集成，以增强多模态理解。三阶段训练课程包括：1) 特征对齐，通过对比学习将视觉和文本特征对齐；2) 知识注入，利用预训练的知识图谱增强模型对结构化视觉内容的理解；3) 推理增强生成，利用外部推理器来验证生成结果的事实准确性。推理时，使用外部推理器对生成结果进行验证和修正。

## 📊 实验亮点

论文提出的模型在StructBench基准上取得了显著的性能提升，尤其是在结构化视觉编辑任务上表现出色。实验结果表明，即使是领先的闭源系统也远未达到令人满意的水平，而该模型通过推理时推理获得了持续的收益。StructScore评估指标能够有效地评估模型生成结果的事实准确性。

## 🎯 应用场景

该研究成果可应用于自动化图表生成、科学文献编辑、教育资源创建等领域。例如，可以根据用户输入的文本描述自动生成相应的图表，或者对已有的科学论文中的图表进行编辑和修改，提高其准确性和可读性。未来，该技术有望在人机交互、智能设计等领域发挥重要作用。

## 📄 摘要（原文）

> While modern visual generation models excel at creating aesthetically pleasing natural images, they struggle with producing or editing structured visuals like charts, diagrams, and mathematical figures, which demand composition planning, text rendering, and multimodal reasoning for factual fidelity. To address this, we present the first comprehensive, systematic investigation of this domain, encompassing data construction, model training, and an evaluation benchmark. First, we construct a large-scale dataset of 1.3 million high-quality structured image pairs derived from executable drawing programs and augmented with chain-of-thought reasoning annotations. Building on it, we train a unified model that integrates a VLM with FLUX.1 Kontext via a lightweight connector for enhanced multimodal understanding. A three-stage training curriculum enables progressive feature alignment, knowledge infusion, and reasoning-augmented generation, further boosted by an external reasoner at inference time. Finally, we introduce StructBench, a novel benchmark for generation and editing with over 1,700 challenging instances, and an accompanying evaluation metric, StructScore, which employs a multi-round Q\&A protocol to assess fine-grained factual accuracy. Evaluations of 15 models reveal that even leading closed-source systems remain far from satisfactory. Our model attains strong editing performance, and inference-time reasoning yields consistent gains across diverse architectures. By releasing the dataset, model, and benchmark, we aim to advance unified multimodal foundations for structured visuals.

