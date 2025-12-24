---
layout: default
title: Complex System Diagnostics Using a Knowledge Graph-Informed and Large Language Model-Enhanced Framework
---

# Complex System Diagnostics Using a Knowledge Graph-Informed and Large Language Model-Enhanced Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21291" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21291v1</a>
  <a href="https://arxiv.org/pdf/2505.21291.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21291v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21291v1', 'Complex System Diagnostics Using a Knowledge Graph-Informed and Large Language Model-Enhanced Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saman Marandi, Yu-Shu Hu, Mohammad Modarres

**分类**: cs.AI

**发布日期**: 2025-05-27

**备注**: 22 Pages, 11 Figures

**DOI**: [10.3390/app15179428](https://doi.org/10.3390/app15179428)

---

## 💡 一句话要点

**提出知识图谱与大语言模型结合的诊断框架以解决复杂系统诊断问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `大语言模型` `系统诊断` `动态主逻辑` `故障推理` `交互式诊断` `自动化构建`

## 📋 核心要点

1. 现有的诊断建模方法在面对复杂系统时表现不佳，导致功能建模成为更优选择。
2. 论文提出的框架结合知识图谱和大语言模型，自动化构建逻辑并支持交互式诊断。
3. 案例研究显示该框架在关键元素上达到了90%以上的准确率，证明了其有效性。

## 📝 摘要（中文）

本文提出了一种新颖的诊断框架，结合知识图谱（KGs）和大语言模型（LLMs），以支持核电厂等高可靠性系统的诊断。传统的诊断建模在系统复杂性增加时面临挑战，而功能建模则成为更具吸引力的方法。该框架基于动态主逻辑（DML）模型的功能建模原则，包含两个协调的LLM组件，分别用于自动构建DML逻辑和交互式诊断。生成的逻辑被编码为结构化的KG，称为KG-DML，支持分层故障推理。用户通过自然语言查询与LLM代理进行交互，代理选择适当的工具进行结构化推理。案例研究表明，该框架在关键元素上超过90%的准确率，支持其在安全关键诊断中的应用。

## 🔬 方法详解

**问题定义**：本文旨在解决复杂系统（如核电厂）中的诊断问题，现有方法在系统复杂性增加时难以有效建模，导致诊断精度不足。

**核心思路**：提出的框架基于动态主逻辑（DML）模型，通过结合知识图谱和大语言模型，自动化构建逻辑并实现交互式诊断，以提高诊断的准确性和深度。

**技术框架**：整体架构包括两个主要模块：一个是基于LLM的工作流，用于从系统文档自动构建DML逻辑；另一个是LLM代理，负责处理用户的自然语言查询并进行结构化推理。生成的DML逻辑被编码为KG-DML，支持分层故障推理。

**关键创新**：最重要的创新在于将知识图谱与大语言模型相结合，LLM代理能够区分诊断和解释任务，选择合适的工具进行结构化推理，而不是将KG内容嵌入每个提示中。

**关键设计**：在设计中，LLM代理通过选择外部工具进行KG推理，针对诊断任务执行特定操作；而对于一般查询，采用图基检索增强生成（Graph-RAG）方法，检索相关KG片段并嵌入提示中以生成自然语言解释。

## 📊 实验亮点

在对辅助给水系统的案例研究中，该框架在关键元素上达到了超过90%的准确率，且在工具和论证提取方面表现一致，证明了其在安全关键诊断中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括核电厂、航空航天、医疗设备等高可靠性系统的故障诊断与维护。通过提高诊断的准确性和效率，该框架能够显著提升系统的安全性和可靠性，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> In this paper, we present a novel diagnostic framework that integrates Knowledge Graphs (KGs) and Large Language Models (LLMs) to support system diagnostics in high-reliability systems such as nuclear power plants. Traditional diagnostic modeling struggles when systems become too complex, making functional modeling a more attractive approach. Our approach introduces a diagnostic framework grounded in the functional modeling principles of the Dynamic Master Logic (DML) model. It incorporates two coordinated LLM components, including an LLM-based workflow for automated construction of DML logic from system documentation and an LLM agent that facilitates interactive diagnostics. The generated logic is encoded into a structured KG, referred to as KG-DML, which supports hierarchical fault reasoning. Expert knowledge or operational data can also be incorporated to refine the model's precision and diagnostic depth. In the interaction phase, users submit natural language queries, which are interpreted by the LLM agent. The agent selects appropriate tools for structured reasoning, including upward and downward propagation across the KG-DML. Rather than embedding KG content into every prompt, the LLM agent distinguishes between diagnostic and interpretive tasks. For diagnostics, the agent selects and executes external tools that perform structured KG reasoning. For general queries, a Graph-based Retrieval-Augmented Generation (Graph-RAG) approach is used, retrieving relevant KG segments and embedding them into the prompt to generate natural explanations. A case study on an auxiliary feedwater system demonstrated the framework's effectiveness, with over 90% accuracy in key elements and consistent tool and argument extraction, supporting its use in safety-critical diagnostics.

