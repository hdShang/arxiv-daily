---
layout: default
title: "MaRGen: Multi-Agent LLM Approach for Self-Directed Market Research and Analysis"
---

# MaRGen: Multi-Agent LLM Approach for Self-Directed Market Research and Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01370" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01370v1</a>
  <a href="https://arxiv.org/pdf/2508.01370.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01370v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01370v1', 'MaRGen: Multi-Agent LLM Approach for Self-Directed Market Research and Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Roman Koshkin, Pengyu Dai, Nozomi Fujikawa, Masahito Togami, Marco Visentini-Scarzanella

**分类**: cs.CL, cs.IR

**发布日期**: 2025-08-02

---

## 💡 一句话要点

**提出MaRGen框架以实现自动化市场研究与分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `市场研究` `自动化分析` `大型语言模型` `多代理系统` `报告生成`

## 📋 核心要点

1. 现有市场研究方法往往依赖人工分析，效率低且成本高，难以满足快速变化的市场需求。
2. 论文提出了一种多代理协作的框架，通过大型语言模型实现市场研究的自动化，提升分析效率和报告质量。
3. 实验结果显示，该框架能够在7分钟内生成高质量的市场报告，成本仅为1美元，显著提高了报告生成的速度和经济性。

## 📝 摘要（中文）

我们提出了一种自主框架，利用大型语言模型（LLMs）自动化端到端的商业分析和市场报告生成。该系统核心采用了专门的代理——研究员、审阅者、撰写者和检索者，协同分析数据并生成全面报告。这些代理通过上下文学习，从亚马逊真实专业顾问的演示材料中学习，以复制专业分析方法。该框架执行多步骤过程：查询数据库、分析数据、生成洞察、创建可视化和撰写市场报告。我们还引入了一种基于LLM的评估系统，用于评估报告质量，显示与专家人类评估的一致性。基于这些评估，我们实施了迭代改进机制，通过自动化审阅周期优化报告质量。实验结果表明，报告质量可以通过自动化审阅周期和顾问的非结构化知识得到提升。我们的框架能够在约7分钟内生成详细的6页报告，成本约为1美元。

## 🔬 方法详解

**问题定义**：本论文旨在解决传统市场研究方法效率低下和成本高昂的问题。现有方法依赖人工分析，难以快速响应市场变化。

**核心思路**：论文提出的解决方案是构建一个多代理协作的框架，利用大型语言模型自动化市场分析和报告生成，模拟专业顾问的分析流程。

**技术框架**：该框架包括四个主要模块：研究员负责数据查询，审阅者进行质量评估，撰写者生成报告，检索者提供信息支持。整个流程涵盖数据查询、分析、洞察生成、可视化和报告撰写。

**关键创新**：最重要的技术创新在于引入了基于LLM的评估系统，能够自动评估报告质量并与人类专家评估保持一致，此外，迭代改进机制通过自动化审阅周期进一步优化报告质量。

**关键设计**：在设计中，采用了上下文学习的方法，使代理能够从真实的专业材料中学习，此外，评估系统的参数设置和损失函数设计也经过精心调整，以确保评估的准确性和有效性。

## 📊 实验亮点

实验结果表明，MaRGen框架能够在7分钟内生成6页详细市场报告，成本约为1美元。通过自动化审阅周期和顾问的非结构化知识，报告质量显著提升，展示了该框架在市场研究中的有效性和经济性。

## 🎯 应用场景

该研究的潜在应用领域包括市场研究、商业分析和咨询服务等。通过自动化生成市场报告，企业可以快速获得市场洞察，降低分析成本，从而在竞争中获得优势。未来，该框架有望扩展到其他领域，如金融分析和产品开发等，推动更广泛的自动化应用。

## 📄 摘要（原文）

> We present an autonomous framework that leverages Large Language Models (LLMs) to automate end-to-end business analysis and market report generation. At its core, the system employs specialized agents - Researcher, Reviewer, Writer, and Retriever - that collaborate to analyze data and produce comprehensive reports. These agents learn from real professional consultants' presentation materials at Amazon through in-context learning to replicate professional analytical methodologies. The framework executes a multi-step process: querying databases, analyzing data, generating insights, creating visualizations, and composing market reports. We also introduce a novel LLM-based evaluation system for assessing report quality, which shows alignment with expert human evaluations. Building on these evaluations, we implement an iterative improvement mechanism that optimizes report quality through automated review cycles. Experimental results show that report quality can be improved by both automated review cycles and consultants' unstructured knowledge. In experimental validation, our framework generates detailed 6-page reports in 7 minutes at a cost of approximately \$1. Our work could be an important step to automatically create affordable market insights.

