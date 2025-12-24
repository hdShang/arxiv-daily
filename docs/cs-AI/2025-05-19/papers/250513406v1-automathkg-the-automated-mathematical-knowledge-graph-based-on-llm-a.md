---
layout: default
title: AutoMathKG: The automated mathematical knowledge graph based on LLM and vector database
---

# AutoMathKG: The automated mathematical knowledge graph based on LLM and vector database

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13406" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13406v1</a>
  <a href="https://arxiv.org/pdf/2505.13406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13406v1', 'AutoMathKG: The automated mathematical knowledge graph based on LLM and vector database')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rong Bian, Yu Geng, Zijian Yang, Bing Cheng

**分类**: cs.AI

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出AutoMathKG以解决数学知识图谱构建的自动化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学知识图谱` `自动化构建` `大语言模型` `向量数据库` `知识补全` `知识融合` `数学推理` `数据增强`

## 📋 核心要点

1. 现有数学知识图谱构建方法受限于语料库的完整性，无法实现全面自动化整合多样知识来源。
2. AutoMathKG通过将数学视为有向图，利用大语言模型和向量数据库实现知识的自动更新与补全。
3. 实验结果显示，AutoMathKG在可达性查询和数学推理能力上优于五个基线模型，具有广泛的适用性。

## 📝 摘要（中文）

数学知识图谱（KG）以结构化方式呈现数学领域的知识。构建数学KG的过程既重要又具有挑战性，现有方法存在两个主要局限：一是受限于语料库的完整性，常常丢弃或手动补充不完整的知识；二是通常未能完全自动化整合多样的知识来源。本文提出了AutoMathKG，一个高质量、覆盖广泛且多维的数学KG，能够实现自动更新。AutoMathKG将数学视为一个由定义、定理和问题实体组成的广泛有向图，利用大语言模型（LLMs）通过上下文学习增强实体和关系，并构建了MathVD向量数据库以搜索相似实体。为实现自动更新，提出了知识补全和知识融合机制，实验结果表明AutoMathKG在多个方面表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数学知识图谱构建过程中存在的知识不完整和整合效率低下的问题。现有方法往往依赖于手动补充，无法实现全面自动化。

**核心思路**：AutoMathKG通过将数学知识视为一个有向图，利用大语言模型进行数据增强，并结合向量数据库实现知识的自动更新与补全，从而提高知识图谱的质量和覆盖面。

**技术框架**：AutoMathKG的整体架构包括知识图谱的构建、知识补全机制和知识融合机制。知识图谱由定义、定理和问题实体构成，MathVD向量数据库用于相似实体的检索。

**关键创新**：最重要的创新点在于结合了大语言模型与向量数据库，实现了数学知识的自动更新与补全，显著提升了知识图谱的构建效率和质量。

**关键设计**：在设计中，采用了SBERT进行嵌入策略，构建MathVD向量数据库；同时，开发了Math LLM与AutoMathKG交互，实现缺失证明或解的自动提供。

## 📊 实验亮点

实验结果表明，AutoMathKG在MathVD的可达性查询上优于五个基线模型，且在数学推理能力方面表现出色，展示了其强大的应用潜力和实际价值。

## 🎯 应用场景

AutoMathKG的潜在应用领域包括教育、科研和智能问答系统等。其自动化构建和更新的能力将极大提升数学知识的获取和利用效率，推动数学教育和研究的智能化发展。

## 📄 摘要（原文）

> A mathematical knowledge graph (KG) presents knowledge within the field of mathematics in a structured manner. Constructing a math KG using natural language is an essential but challenging task. There are two major limitations of existing works: first, they are constrained by corpus completeness, often discarding or manually supplementing incomplete knowledge; second, they typically fail to fully automate the integration of diverse knowledge sources. This paper proposes AutoMathKG, a high-quality, wide-coverage, and multi-dimensional math KG capable of automatic updates. AutoMathKG regards mathematics as a vast directed graph composed of Definition, Theorem, and Problem entities, with their reference relationships as edges. It integrates knowledge from ProofWiki, textbooks, arXiv papers, and TheoremQA, enhancing entities and relationships with large language models (LLMs) via in-context learning for data augmentation. To search for similar entities, MathVD, a vector database, is built through two designed embedding strategies using SBERT. To automatically update, two mechanisms are proposed. For knowledge completion mechanism, Math LLM is developed to interact with AutoMathKG, providing missing proofs or solutions. For knowledge fusion mechanism, MathVD is used to retrieve similar entities, and LLM is used to determine whether to merge with a candidate or add as a new entity. A wide range of experiments demonstrate the advanced performance and broad applicability of the AutoMathKG system, including superior reachability query results in MathVD compared to five baselines and robust mathematical reasoning capability in Math LLM.

