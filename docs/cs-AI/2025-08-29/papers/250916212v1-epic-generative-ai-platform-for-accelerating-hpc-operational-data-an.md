---
layout: default
title: "EPIC: Generative AI Platform for Accelerating HPC Operational Data Analytics"
---

# EPIC: Generative AI Platform for Accelerating HPC Operational Data Analytics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16212" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16212v1</a>
  <a href="https://arxiv.org/pdf/2509.16212.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16212v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16212v1', 'EPIC: Generative AI Platform for Accelerating HPC Operational Data Analytics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmad Maroof Karimi, Woong Shin, Jesse Hines, Tirthankar Ghosal, Naw Safrin Sattar, Feiyi Wang

**分类**: cs.DB, cs.AI

**发布日期**: 2025-08-29

---

## 💡 一句话要点

**提出EPIC平台以加速高性能计算操作数据分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `高性能计算` `操作数据分析` `多模态数据` `大型语言模型` `动态分析` `描述性分析` `预测性分析` `节省成本`

## 📋 核心要点

1. 现有高性能计算操作分析方法依赖静态技术，难以适应不断变化的分析任务和需求。
2. EPIC采用分层多代理架构，利用大型语言模型和多个低级代理进行动态数据分析。
3. 实验结果显示，EPIC在复杂查询处理上表现优异，微调模型的准确性提高了26%，并节省了19倍的操作成本。

## 📝 摘要（中文）

我们提出了EPIC，一个旨在增强操作数据分析的AI驱动平台。EPIC采用分层多代理架构，其中顶层的大型语言模型提供查询处理、推理和综合能力。这些能力协调三个专门的低级代理，分别用于信息检索、描述性分析和预测性分析。该架构使EPIC能够动态和迭代地对多模态数据（包括文本、图像和表格格式）进行高性能计算操作分析。EPIC解决了现有高性能计算操作分析方法的局限性，这些方法依赖静态方法，难以适应不断变化的分析任务和利益相关者需求。通过对Frontier HPC系统的广泛评估，我们证明EPIC能够有效处理复杂查询。以描述性分析为用例，经过微调的小型模型在准确性上超过大型前沿模型，提升幅度可达26%。此外，通过结合大型基础模型与微调的本地开放权重模型，我们在LLM操作成本上实现了19倍的节省。

## 🔬 方法详解

**问题定义**：本论文旨在解决高性能计算（HPC）操作数据分析中现有方法的局限性，特别是静态方法无法适应动态变化的分析需求和任务。

**核心思路**：EPIC平台通过分层多代理架构，结合大型语言模型与低级专用代理，提供灵活的查询处理和分析能力，以应对多模态数据的复杂性。

**技术框架**：EPIC的整体架构包括一个顶层的大型语言模型，负责查询处理和推理，底层则由三个专门的代理组成，分别处理信息检索、描述性分析和预测性分析。该架构支持对文本、图像和表格数据的动态分析。

**关键创新**：EPIC的主要创新在于其分层多代理架构，能够动态适应不同的分析任务，与传统静态方法相比，提供了更高的灵活性和准确性。

**关键设计**：在设计中，EPIC结合了大型基础模型与微调的本地开放权重模型，以降低操作成本，并通过精细调整小型模型来提高分析准确性。

## 📊 实验亮点

EPIC在Frontier HPC系统上的实验结果显示，微调的小型模型在描述性分析任务中比大型前沿模型的准确性提高了26%。此外，通过采用混合方法，EPIC在LLM操作成本上实现了19倍的节省，显著降低了资源消耗。

## 🎯 应用场景

EPIC平台在高性能计算领域具有广泛的应用潜力，能够为科研、工程和商业分析等多个领域提供高效的数据分析解决方案。其动态适应能力使其能够满足不断变化的用户需求，提升决策支持的效率和准确性。

## 📄 摘要（原文）

> We present EPIC, an AI-driven platform designed to augment operational data analytics. EPIC employs a hierarchical multi-agent architecture where a top-level large language model provides query processing, reasoning and synthesis capabilities. These capabilities orchestrate three specialized low-level agents for information retrieval, descriptive analytics, and predictive analytics. This architecture enables EPIC to perform HPC operational analytics on multi-modal data, including text, images, and tabular formats, dynamically and iteratively. EPIC addresses the limitations of existing HPC operational analytics approaches, which rely on static methods that struggle to adapt to evolving analytics tasks and stakeholder demands.
>   Through extensive evaluations on the Frontier HPC system, we demonstrate that EPIC effectively handles complex queries. Using descriptive analytics as a use case, fine-tuned smaller models outperform large state-of-the-art foundation models, achieving up to 26% higher accuracy. Additionally, we achieved 19x savings in LLM operational costs compared to proprietary solutions by employing a hybrid approach that combines large foundational models with fine-tuned local open-weight models.

