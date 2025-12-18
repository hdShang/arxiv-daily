---
layout: default
title: SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions
---

# SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14277" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14277v1</a>
  <a href="https://arxiv.org/pdf/2512.14277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14277v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14277v1', 'SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Panayiotis Smeros, Vincent Emonet, Ruijie Wang, Ana-Claudia Sima, Tarcisio Mendes de Farias

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-12-16

**备注**: 17 pages, 8 figures, 1 table. Under Review

---

## 💡 一句话要点

**SPARQL-LLM：一种基于轻量级元数据的实时自然语言到SPARQL查询生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言处理` `SPARQL查询生成` `知识图谱` `大型语言模型` `元数据索引`

## 📋 核心要点

1. 现有方法在自然语言生成SPARQL查询时，侧重于单数据源的准确性，忽略了联邦查询能力、运行时间和成本等关键因素。
2. SPARQL-LLM利用轻量级元数据，构建了包含元数据索引、提示构建、查询生成和执行的完整架构，实现了高效查询。
3. 实验结果表明，SPARQL-LLM在F1分数上提升了24%，速度提升了36倍，成本极低，适用于实时应用，并支持多种语言和复杂查询。

## 📝 摘要（中文）

大型语言模型的出现正在推动新的方法来更好地解决从自然语言生成结构化查询（如SPARQL查询）的挑战。然而，这些新方法主要关注单个来源的响应准确性，而忽略了其他评估标准，如跨分布式数据存储的联邦查询能力，以及生成SPARQL查询的运行时间和成本。因此，它们通常无法直接用于生产，或者难以在具有良好准确性的（潜在的联邦）知识图谱上部署。为了缓解这些问题，本文扩展了我们之前的工作，描述并系统地评估了SPARQL-LLM，这是一种开源且与三元组存储无关的方法，由轻量级元数据驱动，可以从自然语言文本生成SPARQL查询。首先，我们描述了它的架构，该架构由用于元数据索引、提示构建以及查询生成和执行的专用组件组成。然后，我们基于最先进的挑战（包含多语言问题）以及来自生物信息学领域中最流行的三个知识图谱的问题集合对其进行评估。结果表明，在最先进的挑战中，F1分数显着提高了24％，并且能够适应英语和西班牙语等高资源语言，以及形成复杂和联邦的生物信息学查询。此外，我们表明SPARQL-LLM比参与挑战的其他系统快36倍，每个问题的成本最高为0.01美元，使其适用于实时、低成本的文本到SPARQL应用程序。可以在https://www.expasy.org/chat上找到一个部署在真实世界分散知识图谱上的此类应用程序。

## 🔬 方法详解

**问题定义**：论文旨在解决从自然语言生成SPARQL查询的问题，现有方法的痛点在于无法兼顾准确性、联邦查询能力、运行时间和成本，导致难以在实际生产环境中部署。

**核心思路**：论文的核心思路是利用轻量级元数据来指导大型语言模型生成SPARQL查询。通过对知识图谱的元数据进行索引，可以更有效地构建提示，从而提高查询生成的准确性和效率。

**技术框架**：SPARQL-LLM的整体架构包含以下几个主要模块：1) 元数据索引模块：负责提取和索引知识图谱的元数据，例如类、属性和关系。2) 提示构建模块：根据自然语言问题和索引的元数据，构建用于提示大型语言模型的提示。3) 查询生成模块：使用大型语言模型根据提示生成SPARQL查询。4) 查询执行模块：执行生成的SPARQL查询并返回结果。

**关键创新**：最重要的技术创新点在于利用轻量级元数据来指导大型语言模型生成SPARQL查询。与现有方法相比，SPARQL-LLM不需要对大型语言模型进行微调，而是通过构建更有效的提示来提高查询生成的准确性和效率。此外，SPARQL-LLM的设计使其能够支持联邦查询，即可以跨多个知识图谱执行查询。

**关键设计**：论文中没有详细描述关键的参数设置、损失函数、网络结构等技术细节。元数据索引的具体方法、提示构建的策略以及大型语言模型的选择是影响性能的关键因素，但文中没有给出具体实现细节。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14277v1/figures/system_architecture.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14277v1/figures/system_flow.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14277v1/figures/triple_patterns.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SPARQL-LLM在多语言问题挑战中，F1分数提高了24%。在生物信息学知识图谱查询任务中，SPARQL-LLM比其他系统快36倍，每个问题的成本最高为0.01美元。实验结果表明，该方法在准确性、效率和成本方面都具有显著优势。

## 🎯 应用场景

SPARQL-LLM可应用于各种需要从自然语言查询知识图谱的场景，例如智能问答系统、虚拟助手和生物信息学数据分析。其低成本和实时性使其特别适用于大规模部署和交互式应用。该方法能够有效支持联邦查询，为跨多个数据源的信息集成提供了可能。

## 📄 摘要（原文）

> The advent of large language models is contributing to the emergence of novel approaches that promise to better tackle the challenge of generating structured queries, such as SPARQL queries, from natural language. However, these new approaches mostly focus on response accuracy over a single source while ignoring other evaluation criteria, such as federated query capability over distributed data stores, as well as runtime and cost to generate SPARQL queries. Consequently, they are often not production-ready or easy to deploy over (potentially federated) knowledge graphs with good accuracy. To mitigate these issues, in this paper, we extend our previous work and describe and systematically evaluate SPARQL-LLM, an open-source and triplestore-agnostic approach, powered by lightweight metadata, that generates SPARQL queries from natural language text. First, we describe its architecture, which consists of dedicated components for metadata indexing, prompt building, and query generation and execution. Then, we evaluate it based on a state-of-the-art challenge with multilingual questions, and a collection of questions from three of the most prevalent knowledge graphs within the field of bioinformatics. Our results demonstrate a substantial increase of 24% in the F1 Score on the state-of-the-art challenge, adaptability to high-resource languages such as English and Spanish, as well as ability to form complex and federated bioinformatics queries. Furthermore, we show that SPARQL-LLM is up to 36x faster than other systems participating in the challenge, while costing a maximum of $0.01 per question, making it suitable for real-time, low-cost text-to-SPARQL applications. One such application deployed over real-world decentralized knowledge graphs can be found at https://www.expasy.org/chat.

