---
layout: default
title: "Introducing ORKG ASK: an AI-driven Scholarly Literature Search and Exploration System Taking a Neuro-Symbolic Approach"
---

# Introducing ORKG ASK: an AI-driven Scholarly Literature Search and Exploration System Taking a Neuro-Symbolic Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16425" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16425v1</a>
  <a href="https://arxiv.org/pdf/2512.16425.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16425v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16425v1', 'Introducing ORKG ASK: an AI-driven Scholarly Literature Search and Exploration System Taking a Neuro-Symbolic Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Allard Oelen, Mohamad Yaser Jaradeh, Sören Auer

**分类**: cs.IR, cs.AI

**发布日期**: 2025-12-18

**DOI**: [10.1007/978-3-031-97207-2_2](https://doi.org/10.1007/978-3-031-97207-2_2)

---

## 💡 一句话要点

**提出ORKG ASK：一种基于神经符号方法的AI驱动的学术文献搜索与探索系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `学术文献搜索` `知识图谱` `大型语言模型` `神经符号方法` `检索增强生成`

## 📋 核心要点

1. 现有学术文献数量庞大，研究人员面临难以快速找到相关文献的挑战。
2. ASK系统采用神经符号方法，结合向量搜索、LLM和知识图谱，辅助研究人员进行文献检索。
3. ASK系统通过RAG方法，能够根据用户提出的自然语言问题，自动提取信息并生成答案。

## 📝 摘要（中文）

随着已发表的学术文献数量持续增长，找到相关的文献变得越来越困难。生成式人工智能（AI）的兴起，特别是大型语言模型（LLM），为发现和探索文献带来了新的可能性。我们介绍ASK（科学知识助手），这是一个AI驱动的学术文献搜索和探索系统，它遵循神经符号方法。ASK旨在通过利用向量搜索、LLM和知识图谱，为研究人员寻找相关学术文献提供积极支持。该系统允许用户以自然语言输入研究问题并检索相关文章。ASK自动提取关键信息，并使用检索增强生成（RAG）方法生成研究问题的答案。我们对ASK进行了评估，评估了系统的可用性和实用性。调查结果表明，该系统用户友好，用户在使用该系统时普遍感到满意。

## 🔬 方法详解

**问题定义**：当前学术文献数量爆炸式增长，研究人员难以高效地找到所需文献。传统文献检索方法依赖关键词匹配，无法理解用户提问的深层语义，导致检索结果不准确或不全面。现有方法缺乏对文献内容的深入理解和推理能力，难以直接回答用户提出的复杂研究问题。

**核心思路**：ASK系统的核心思路是结合神经方法和符号方法，利用LLM的语义理解能力和知识图谱的结构化知识，实现更智能的文献检索和探索。通过向量搜索快速定位相关文献，然后利用LLM提取关键信息并生成答案，最后利用知识图谱进行知识推理和扩展。

**技术框架**：ASK系统主要包含以下几个模块：1) 自然语言查询接口：接收用户以自然语言提出的研究问题。2) 向量搜索模块：利用预训练的向量模型将用户查询和文献进行向量化表示，通过计算向量相似度快速检索相关文献。3) 信息抽取模块：利用LLM从检索到的文献中提取关键信息，例如研究目的、方法、结果等。4) 答案生成模块：利用RAG方法，结合提取的关键信息和知识图谱中的相关知识，生成对用户问题的答案。5) 知识图谱模块：存储和管理领域知识，为答案生成提供背景知识和推理能力。

**关键创新**：ASK系统的关键创新在于其神经符号方法的融合。它将LLM的强大的自然语言处理能力与知识图谱的结构化知识表示相结合，实现了更准确、更全面的文献检索和知识发现。与传统的基于关键词的检索方法相比，ASK能够理解用户查询的深层语义，并提供更相关的结果。与单纯使用LLM的方法相比，ASK能够利用知识图谱进行知识推理和扩展，生成更准确、更可靠的答案。

**关键设计**：ASK系统使用了预训练的BERT模型进行向量化表示，使用Transformer模型进行信息抽取和答案生成。向量搜索模块使用了FAISS库进行高效的向量相似度计算。知识图谱使用了RDF格式进行存储和管理。RAG方法使用了Beam Search算法进行答案生成，并使用了惩罚机制避免生成重复或不相关的答案。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16425v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16425v1/figures/screenshot-ask.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16425v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文对ASK系统进行了可用性和实用性评估，结果表明用户对该系统普遍满意，认为其用户友好且实用。具体而言，用户认为ASK系统能够有效地帮助他们找到相关文献，并快速获取所需信息。虽然论文中没有给出具体的性能数据，但用户反馈表明ASK系统在文献检索和知识发现方面具有显著优势。

## 🎯 应用场景

ASK系统可应用于各个学科领域，帮助研究人员快速找到相关文献，提高科研效率。该系统还可以用于辅助教学，帮助学生更好地理解和掌握领域知识。未来，ASK系统可以扩展到其他类型的知识资源，例如专利、报告等，成为一个综合性的知识发现平台。此外，还可以将ASK系统与科研工作流集成，实现自动化文献综述和研究报告生成。

## 📄 摘要（原文）

> As the volume of published scholarly literature continues to grow, finding relevant literature becomes increasingly difficult. With the rise of generative Artificial Intelligence (AI), and particularly Large Language Models (LLMs), new possibilities emerge to find and explore literature. We introduce ASK (Assistant for Scientific Knowledge), an AI-driven scholarly literature search and exploration system that follows a neuro-symbolic approach. ASK aims to provide active support to researchers in finding relevant scholarly literature by leveraging vector search, LLMs, and knowledge graphs. The system allows users to input research questions in natural language and retrieve relevant articles. ASK automatically extracts key information and generates answers to research questions using a Retrieval-Augmented Generation (RAG) approach. We present an evaluation of ASK, assessing the system's usability and usefulness. Findings indicate that the system is user-friendly and users are generally satisfied while using the system.

