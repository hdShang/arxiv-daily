---
layout: default
title: "BioMol-MQA: A Multi-Modal Question Answering Dataset For LLM Reasoning Over Bio-Molecular Interactions"
---

# BioMol-MQA: A Multi-Modal Question Answering Dataset For LLM Reasoning Over Bio-Molecular Interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05766" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05766v1</a>
  <a href="https://arxiv.org/pdf/2506.05766.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05766v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05766v1', 'BioMol-MQA: A Multi-Modal Question Answering Dataset For LLM Reasoning Over Bio-Molecular Interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saptarshi Sengupta, Shuhua Yang, Paul Kwong Yu, Fali Wang, Suhang Wang

**分类**: cs.CL

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出BioMol-MQA以解决多模态生物分子交互问答问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态问答` `生物分子交互` `知识图谱` `大型语言模型` `检索增强生成`

## 📋 核心要点

1. 现有的RAG方法主要聚焦于单一模态的信息检索，无法有效处理多模态信息，尤其是在医疗领域。
2. 论文提出了BioMol-MQA数据集，结合多模态知识图谱和复杂问题，以测试LLM在多模态信息检索和推理方面的能力。
3. 实验结果显示，现有LLMs在没有背景数据的情况下难以回答问题，强调了强大RAG框架的必要性。

## 📝 摘要（中文）

检索增强生成（RAG）在提升大型语言模型（LLMs）方面展现了强大能力。然而，现有的RAG方法主要集中于单一模态的信息检索，尤其是文本，而在医疗等实际应用中，相关信息往往以多种模态存在，如知识图谱、临床笔记和复杂的分子结构。为了解决这一问题，本文提出了BioMol-MQA，一个关于多药物治疗的新问答数据集，包含多模态知识图谱和设计用于测试LLM能力的挑战性问题。实验表明，现有LLMs在回答这些问题时表现不佳，仅在提供必要背景数据时才能取得较好效果，这表明强大的RAG框架的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RAG方法在多模态信息检索中的不足，尤其是在生物分子交互领域，现有方法无法有效整合多种信息来源。

**核心思路**：提出BioMol-MQA数据集，包含多模态知识图谱和挑战性问题，以促进LLM在多模态信息检索和推理能力的提升。通过结合文本和分子结构信息，增强LLM的回答准确性。

**技术框架**：整体架构包括两个主要部分：一是多模态知识图谱，包含文本和分子结构信息；二是设计用于测试LLM能力的复杂问题。流程包括信息检索、推理和生成回答。

**关键创新**：最重要的创新点在于构建了一个多模态知识图谱，结合了文本和分子结构信息，填补了现有RAG方法在多模态处理上的空白。

**关键设计**：在数据集构建中，采用了多种信息来源，设计了多样化的问题类型，以确保测试的全面性和挑战性。

## 📊 实验亮点

实验结果表明，现有LLMs在回答BioMol-MQA数据集中的问题时表现不佳，尤其是在缺乏背景数据的情况下，准确率显著低于提供背景数据时的表现。这一发现强调了强大RAG框架的必要性，推动了多模态问答系统的发展。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康、药物研发和生物信息学等。通过提升LLM在多模态信息检索和推理方面的能力，可以更好地支持临床决策、药物相互作用分析等实际应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Retrieval augmented generation (RAG) has shown great power in improving Large Language Models (LLMs). However, most existing RAG-based LLMs are dedicated to retrieving single modality information, mainly text; while for many real-world problems, such as healthcare, information relevant to queries can manifest in various modalities such as knowledge graph, text (clinical notes), and complex molecular structure. Thus, being able to retrieve relevant multi-modality domain-specific information, and reason and synthesize diverse knowledge to generate an accurate response is important. To address the gap, we present BioMol-MQA, a new question-answering (QA) dataset on polypharmacy, which is composed of two parts (i) a multimodal knowledge graph (KG) with text and molecular structure for information retrieval; and (ii) challenging questions that designed to test LLM capabilities in retrieving and reasoning over multimodal KG to answer questions. Our benchmarks indicate that existing LLMs struggle to answer these questions and do well only when given the necessary background data, signaling the necessity for strong RAG frameworks.

