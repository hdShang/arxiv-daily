---
layout: default
title: "TReB: A Comprehensive Benchmark for Evaluating Table Reasoning Capabilities of Large Language Models"
---

# TReB: A Comprehensive Benchmark for Evaluating Table Reasoning Capabilities of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18421" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18421v2</a>
  <a href="https://arxiv.org/pdf/2506.18421.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18421v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18421v2', 'TReB: A Comprehensive Benchmark for Evaluating Table Reasoning Capabilities of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ce Li, Xiaofan Liu, Zhiyan Song, Ce Chi, Chen Zhao, Jingjing Yang, Zhendong Wang, Kexin Yang, Boshen Shi, Xing Wang, Chao Deng, Junlan Feng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-23 (更新: 2025-07-14)

**备注**: Benmark report v1.1

---

## 💡 一句话要点

**提出TReB基准以评估大型语言模型的表格推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格推理` `大型语言模型` `评估基准` `数据集构建` `推理能力`

## 📋 核心要点

1. 现有方法在评估大型语言模型的表格推理能力时缺乏有效的基准，导致性能反映不全面。
2. 论文提出了TReB基准，涵盖26个子任务，旨在全面评估表格的浅层和深层推理能力。
3. 实验结果显示，现有LLMs在复杂表格任务上仍有显著提升空间，验证了TReB的有效性。

## 📝 摘要（中文）

在商业和工业中，大量数据以表格、数据库和数据仓库的形式存储。由于表格结构数据的隐含语义、内在复杂性和结构化特性，推理面临重大挑战。现有缺乏有效的评估基准来公平反映大型语言模型（LLMs）在广泛表格推理能力上的表现。本文提出了一个全面的表格推理基准TReB，涵盖26个子任务，测量浅层和深层表格理解能力。通过迭代数据处理程序构建高质量数据集，并创建评估框架以稳健测量表格推理能力，验证了20多种最先进LLMs的有效性。实验结果表明，现有LLMs在处理复杂的实际表格任务时仍有显著提升空间。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在表格推理能力评估中的不足，现有方法无法全面反映模型在复杂表格任务上的表现。

**核心思路**：提出TReB基准，通过构建高质量数据集和评估框架，全面测量模型的表格理解和推理能力，设计了三种推理模式以适应不同的推理需求。

**技术框架**：整体架构包括数据集构建、评估框架设计和模型评估三个主要模块。数据集通过迭代处理生成，评估框架则采用TCoT、PoT和ICoT三种推理模式进行能力测量。

**关键创新**：TReB基准的创新在于其全面性和多样性，涵盖了多种表格推理任务，能够有效评估模型在实际应用中的表现，与现有方法相比，提供了更为细致的评估标准。

**关键设计**：在数据集构建中，采用了迭代数据处理程序，确保数据质量；评估框架中，设计了多种推理模式，能够适应不同的推理场景，增强了评估的灵活性和准确性。

## 📊 实验亮点

实验结果表明，使用TReB基准评估的20多种最先进的LLMs在复杂表格任务上仍有显著提升空间，验证了该基准的有效性和必要性。具体性能数据和对比基线将在公开数据集中提供，进一步促进研究的透明性和可重复性。

## 🎯 应用场景

该研究的潜在应用领域包括商业智能、数据分析和自动化决策等。通过提供一个全面的评估基准，TReB能够帮助研究人员和开发者更好地理解和提升大型语言模型在表格数据处理中的能力，推动相关技术的进步和应用。

## 📄 摘要（原文）

> The majority of data in businesses and industries is stored in tables, databases, and data warehouses. Reasoning with table-structured data poses significant challenges for large language models (LLMs) due to its hidden semantics, inherent complexity, and structured nature. One of these challenges is lacking an effective evaluation benchmark fairly reflecting the performances of LLMs on broad table reasoning abilities. In this paper, we fill in this gap, presenting a comprehensive table reasoning evolution benchmark, TReB, which measures both shallow table understanding abilities and deep table reasoning abilities, a total of 26 sub-tasks. We construct a high quality dataset through an iterative data processing procedure. We create an evaluation framework to robustly measure table reasoning capabilities with three distinct inference modes, TCoT, PoT and ICoT. Further, we benchmark over 20 state-of-the-art LLMs using this frame work and prove its effectiveness. Experimental results reveal that existing LLMs still have significant room for improvement in addressing the complex and real world Table related tasks. Both the dataset and evaluation framework are publicly available, with the dataset hosted on huggingface.co/datasets/JT-LM/JIUTIAN-TReB and the framework on github.com/JT-LM/jiutian-treb.

