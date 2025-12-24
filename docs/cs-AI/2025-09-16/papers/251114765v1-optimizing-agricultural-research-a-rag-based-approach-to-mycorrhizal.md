---
layout: default
title: "Optimizing Agricultural Research: A RAG-Based Approach to Mycorrhizal Fungi Information"
---

# Optimizing Agricultural Research: A RAG-Based Approach to Mycorrhizal Fungi Information

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14765" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14765v1</a>
  <a href="https://arxiv.org/pdf/2511.14765.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14765v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14765v1', 'Optimizing Agricultural Research: A RAG-Based Approach to Mycorrhizal Fungi Information')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Usman Altam, Md Imtiaz Habib, Tuan Hoang

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-09-16

**备注**: 10 pages, 4 figures, 1 table

---

## 💡 一句话要点

**提出基于RAG的农业研究系统，提升菌根真菌信息检索与利用效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `菌根真菌` `农业研究` `知识发现` `向量数据库`

## 📋 核心要点

1. 传统大型语言模型受限于静态训练数据，无法有效处理特定领域的动态知识，尤其是在农业研究中。
2. 该论文提出基于RAG的系统，通过语义检索和结构化数据提取，动态整合农学和生物技术知识，增强响应的准确性和可靠性。
3. 实验结果表明，该系统能够有效检索和综合AMF与作物系统相互作用的信息，加速农业生态创新。

## 📝 摘要（中文）

本文提出了一种基于检索增强生成（RAG）的系统，用于优化农业研究，特别是丛枝菌根真菌（AMF）相关信息的利用。与受限于静态训练语料库的传统大型语言模型（LLM）不同，该系统动态整合领域特定的外部知识源，克服了时间和学科的限制。该系统采用双层策略：(i) 使用向量嵌入对农学和生物技术语料库中的领域特定内容进行语义检索和增强；(ii) 结构化数据提取，捕获预定义的实验元数据，如接种方法、孢子密度、土壤参数和产量结果。这种混合方法确保生成的响应不仅在语义上对齐，而且得到结构化实验证据的支持。嵌入存储在高性能向量数据库中，支持从不断发展的文献库中进行近实时检索。实证评估表明，该系统能够检索和综合关于AMF与作物系统（如番茄）相互作用的高度相关信息。该框架突出了人工智能驱动的知识发现加速农业生态创新和增强可持续农业系统决策的潜力。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在处理农业领域，特别是菌根真菌（AMF）相关信息时，由于其训练数据的局限性，无法提供及时、准确和全面的信息。研究人员需要花费大量时间从海量文献中检索和整合相关知识，效率低下。因此，如何高效地从不断增长的农业文献中提取和利用AMF相关信息是一个亟待解决的问题。

**核心思路**：该论文的核心思路是利用检索增强生成（RAG）框架，将外部知识库与LLM相结合，从而克服LLM的知识局限性。通过动态检索与AMF相关的农学和生物技术文献，并将其融入到LLM的生成过程中，可以显著提高生成信息的准确性和相关性。此外，通过结构化数据提取，可以捕获实验元数据，为生成的响应提供实验证据支持。

**技术框架**：该RAG系统的整体架构包含两个主要阶段：(1) 语义检索与增强：利用向量嵌入技术，将农学和生物技术语料库中的文献转换为向量表示，并存储在高性能向量数据库中。当用户提出问题时，系统首先将问题转换为向量表示，然后在向量数据库中检索与问题最相关的文献片段。这些检索到的文献片段被用作LLM的上下文信息，以增强LLM的生成能力。(2) 结构化数据提取：系统设计了专门的数据提取模块，用于从文献中提取预定义的实验元数据，如接种方法、孢子密度、土壤参数和产量结果。这些结构化数据被用于验证和补充LLM生成的响应。

**关键创新**：该论文的关键创新在于将RAG框架应用于农业研究领域，并结合了语义检索和结构化数据提取两种方法。这种混合方法不仅提高了信息检索的效率，还确保了生成信息的准确性和可靠性。此外，该系统利用高性能向量数据库存储和检索文献向量，支持从不断增长的文献库中进行近实时检索。

**关键设计**：该系统的关键设计包括：(1) 使用预训练的语言模型（例如，BERT或RoBERTa）生成文献和问题的向量表示；(2) 设计高效的向量数据库索引和检索算法，以支持大规模文献的快速检索；(3) 开发专门的数据提取规则和模型，用于从文献中提取实验元数据；(4) 设计合适的提示工程（Prompt Engineering）策略，引导LLM生成准确和相关的响应。

## 📊 实验亮点

实验结果表明，该系统能够有效地检索和综合关于AMF与作物系统（如番茄）相互作用的高度相关信息。通过与传统的信息检索方法相比，该系统能够提供更准确、更全面的信息，并能够生成包含实验证据支持的响应。具体性能数据未知，但论文强调了该系统在检索相关性和信息综合方面的优势。

## 🎯 应用场景

该研究成果可应用于精准农业、农业知识问答系统、农业决策支持系统等领域。农民和农业研究人员可以通过该系统快速获取关于特定作物和菌根真菌相互作用的知识，从而优化种植方案、提高作物产量和改善土壤健康。该系统还有助于加速农业生态创新，促进可持续农业发展。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) represents a transformative approach within natural language processing (NLP), combining neural information retrieval with generative language modeling to enhance both contextual accuracy and factual reliability of responses. Unlike conventional Large Language Models (LLMs), which are constrained by static training corpora, RAG-powered systems dynamically integrate domain-specific external knowledge sources, thereby overcoming temporal and disciplinary limitations. In this study, we present the design and evaluation of a RAG-enabled system tailored for Mycophyto, with a focus on advancing agricultural applications related to arbuscular mycorrhizal fungi (AMF). These fungi play a critical role in sustainable agriculture by enhancing nutrient acquisition, improving plant resilience under abiotic and biotic stresses, and contributing to soil health. Our system operationalizes a dual-layered strategy: (i) semantic retrieval and augmentation of domain-specific content from agronomy and biotechnology corpora using vector embeddings, and (ii) structured data extraction to capture predefined experimental metadata such as inoculation methods, spore densities, soil parameters, and yield outcomes. This hybrid approach ensures that generated responses are not only semantically aligned but also supported by structured experimental evidence. To support scalability, embeddings are stored in a high-performance vector database, allowing near real-time retrieval from an evolving literature base. Empirical evaluation demonstrates that the proposed pipeline retrieves and synthesizes highly relevant information regarding AMF interactions with crop systems, such as tomato (Solanum lycopersicum). The framework underscores the potential of AI-driven knowledge discovery to accelerate agroecological innovation and enhance decision-making in sustainable farming systems.

