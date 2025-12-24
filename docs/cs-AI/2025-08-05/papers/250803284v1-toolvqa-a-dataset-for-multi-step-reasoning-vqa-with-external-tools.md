---
layout: default
title: "ToolVQA: A Dataset for Multi-step Reasoning VQA with External Tools"
---

# ToolVQA: A Dataset for Multi-step Reasoning VQA with External Tools

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03284" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03284v1</a>
  <a href="https://arxiv.org/pdf/2508.03284.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03284v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03284v1', 'ToolVQA: A Dataset for Multi-step Reasoning VQA with External Tools')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaofeng Yin, Ting Lei, Yang Liu

**分类**: cs.AI

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出ToolVQA以解决多步骤推理VQA中的工具使用能力不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多步骤推理` `视觉问答` `外部工具` `多模态数据集` `深度优先搜索` `人类推理模拟` `智能助手`

## 📋 核心要点

1. 现有的工具增强视觉问答方法在真实世界的多模态场景中表现不佳，特别是在多步骤推理任务上存在显著不足。
2. 本文提出ToolVQA数据集，采用真实视觉上下文和复杂的推理任务，结合ToolEngine生成数据以模拟人类的工具使用推理。
3. 在ToolVQA上微调的7B LFM在测试集上表现优异，超越了大型封闭模型GPT-3.5-turbo，展示了良好的泛化能力。

## 📝 摘要（中文）

将外部工具整合进大型基础模型（LFM）已成为提升其问题解决能力的有效方法。尽管现有研究在工具增强的视觉问答（VQA）中表现良好，但最近的基准测试显示，在需要多步骤推理的多模态场景中，实际工具使用能力存在显著差距。为此，本文提出了ToolVQA，一个包含23K实例的大规模多模态数据集，旨在弥补这一差距。ToolVQA不同于以往依赖于合成场景和简化查询的数据集，采用真实世界的视觉上下文和具有挑战性的隐式多步骤推理任务，更好地与真实用户交互对齐。我们还提出了ToolEngine，一个新颖的数据生成管道，利用深度优先搜索（DFS）和动态上下文示例匹配机制来模拟类人工具使用推理。

## 🔬 方法详解

**问题定义**：本文旨在解决现有工具增强视觉问答（VQA）在真实世界多模态场景中多步骤推理能力不足的问题。现有方法多依赖于合成数据，无法有效应对复杂的实际应用场景。

**核心思路**：提出ToolVQA数据集，包含真实视觉上下文和隐式多步骤推理任务，利用ToolEngine生成数据以模拟人类工具使用的推理过程。通过这种方式，增强了模型在实际应用中的表现。

**技术框架**：ToolVQA的数据生成流程包括数据收集、深度优先搜索（DFS）算法和动态上下文示例匹配机制。ToolEngine作为核心模块，负责生成符合真实场景的多模态数据。

**关键创新**：ToolVQA的主要创新在于其数据生成方法和真实场景的应用，区别于以往依赖合成数据的研究，提供了更具挑战性的推理任务。

**关键设计**：在ToolEngine中，采用DFS算法进行数据生成，并结合动态示例匹配机制，以确保生成的数据能够有效模拟人类的推理过程。

## 📊 实验亮点

在ToolVQA数据集上微调的7B LFM在测试集上表现优异，超越了GPT-3.5-turbo等大型封闭模型，展示了在多个分布外数据集上的强泛化能力，提升幅度显著。

## 🎯 应用场景

ToolVQA的研究成果可广泛应用于智能助手、机器人导航、教育和医疗等领域，提升系统在复杂任务中的决策能力和用户交互体验。未来，随着数据集的不断完善，可能会推动多模态AI系统的进一步发展与应用。

## 📄 摘要（原文）

> Integrating external tools into Large Foundation Models (LFMs) has emerged as a promising approach to enhance their problem-solving capabilities. While existing studies have demonstrated strong performance in tool-augmented Visual Question Answering (VQA), recent benchmarks reveal significant gaps in real-world tool-use proficiency, particularly in functionally diverse multimodal settings requiring multi-step reasoning. In this work, we introduce ToolVQA, a large-scale multimodal dataset comprising 23K instances, designed to bridge this gap. Unlike previous datasets that rely on synthetic scenarios and simplified queries, ToolVQA features real-world visual contexts and challenging implicit multi-step reasoning tasks, better aligning with real user interactions. To construct this dataset, we propose ToolEngine, a novel data generation pipeline that employs Depth-First Search (DFS) with a dynamic in-context example matching mechanism to simulate human-like tool-use reasoning. ToolVQA encompasses 10 multimodal tools across 7 diverse task domains, with an average inference length of 2.78 reasoning steps per instance. The fine-tuned 7B LFMs on ToolVQA not only achieve impressive performance on our test set but also surpass the large close-sourced model GPT-3.5-turbo on various out-of-distribution (OOD) datasets, demonstrating strong generalizability to real-world tool-use scenarios.

