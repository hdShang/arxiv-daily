---
layout: default
title: SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions
---

# SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14277" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14277v1</a>
  <a href="https://arxiv.org/pdf/2512.14277.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14277v1" onclick="toggleFavorite(this, '2512.14277v1', 'SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Panayiotis Smeros, Vincent Emonet, Ruijie Wang, Ana-Claudia Sima, Tarcisio Mendes de Farias

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-12-16

**备注**: 17 pages, 8 figures, 1 table. Under Review

---

## 💡 一句话要点

**SPARQL-LLM：轻量级元数据驱动的实时自然语言到SPARQL查询生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自然语言处理` `SPARQL查询生成` `知识图谱` `大型语言模型` `元数据驱动`

## 📋 核心要点

1. 现有方法在自然语言生成SPARQL查询时，侧重于单数据源准确性，忽略了联邦查询能力、运行时间和成本，难以实际部署。
2. SPARQL-LLM利用轻量级元数据，构建三元组存储无关的查询生成流程，包含元数据索引、提示构建和查询生成执行等模块。
3. 实验表明，SPARQL-LLM在多语言数据集上F1提升24%，速度提升36倍，成本极低，适用于实时低成本应用。

## 📝 摘要（中文）

大型语言模型的出现促进了从自然语言生成结构化查询（如SPARQL查询）的新方法。然而，这些方法主要关注单个数据源的响应准确性，忽略了其他评估标准，如跨分布式数据存储的联邦查询能力，以及生成SPARQL查询的运行时间和成本。因此，它们通常不具备生产就绪性，或者难以在具有良好准确性的（潜在的联邦）知识图谱上部署。为了解决这些问题，本文扩展了我们之前的工作，描述并系统地评估了SPARQL-LLM，这是一种开源且与三元组存储无关的方法，由轻量级元数据驱动，可以从自然语言文本生成SPARQL查询。首先，我们描述了它的架构，该架构由用于元数据索引、提示构建和查询生成与执行的专用组件组成。然后，我们基于最先进的挑战（包含多语言问题）以及来自生物信息学领域中最流行的三个知识图谱的问题集合对其进行评估。结果表明，在最先进的挑战中，F1分数大幅提高了24%，对英语和西班牙语等高资源语言的适应性良好，并且能够形成复杂且联邦的生物信息学查询。此外，我们表明SPARQL-LLM比参与挑战的其他系统快36倍，每个问题的成本最高为0.01美元，使其适用于实时、低成本的文本到SPARQL应用程序。可以在https://www.expasy.org/chat上找到一个部署在真实世界分散知识图谱上的此类应用程序。

## 🔬 方法详解

**问题定义**：论文旨在解决从自然语言生成SPARQL查询的问题，现有方法主要关注单数据源的准确性，忽略了联邦查询能力、运行时间和成本，导致难以在实际生产环境中部署，尤其是在大规模、分布式的知识图谱上。

**核心思路**：论文的核心思路是利用轻量级的元数据来指导大型语言模型生成SPARQL查询。通过对知识图谱的元数据进行索引，可以帮助语言模型更好地理解知识图谱的结构和语义，从而生成更准确、更有效的查询。这种方法降低了对大型语言模型参数规模的依赖，从而降低了成本和延迟。

**技术框架**：SPARQL-LLM的整体架构包含三个主要模块：元数据索引模块、提示构建模块和查询生成与执行模块。首先，元数据索引模块负责从知识图谱中提取和索引元数据，例如实体、关系和属性的名称和描述。然后，提示构建模块利用索引的元数据和自然语言问题，构建一个包含上下文信息的提示，输入到大型语言模型中。最后，查询生成与执行模块负责从大型语言模型的输出中提取SPARQL查询，并在知识图谱上执行该查询。

**关键创新**：SPARQL-LLM的关键创新在于使用轻量级元数据来指导大型语言模型生成SPARQL查询。与直接使用大型语言模型生成查询的方法相比，SPARQL-LLM可以显著提高查询的准确性和效率，并降低成本。此外，SPARQL-LLM的设计是三元组存储无关的，可以应用于各种不同的知识图谱。

**关键设计**：论文中没有详细描述具体的参数设置、损失函数或网络结构等技术细节。但是，元数据索引模块的设计是至关重要的，需要选择合适的元数据类型和索引方法，以确保能够有效地提取和利用知识图谱的信息。提示构建模块的设计也需要仔细考虑，需要选择合适的提示模板和上下文信息，以确保大型语言模型能够生成准确的查询。

## 📊 实验亮点

实验结果表明，SPARQL-LLM在多语言数据集上的F1分数比现有方法提高了24%，并且速度提高了36倍，每个问题的成本最高为0.01美元。这些结果表明，SPARQL-LLM是一种高效、准确且经济的自然语言到SPARQL查询生成方法。

## 🎯 应用场景

SPARQL-LLM可应用于各种需要从自然语言查询知识图谱的场景，例如智能问答系统、语义搜索、数据集成和生物信息学研究。其低成本和实时性使其特别适用于大规模、分布式的知识图谱应用，例如药物发现、疾病诊断和个性化医疗。

## 📄 摘要（原文）

> The advent of large language models is contributing to the emergence of novel approaches that promise to better tackle the challenge of generating structured queries, such as SPARQL queries, from natural language. However, these new approaches mostly focus on response accuracy over a single source while ignoring other evaluation criteria, such as federated query capability over distributed data stores, as well as runtime and cost to generate SPARQL queries. Consequently, they are often not production-ready or easy to deploy over (potentially federated) knowledge graphs with good accuracy. To mitigate these issues, in this paper, we extend our previous work and describe and systematically evaluate SPARQL-LLM, an open-source and triplestore-agnostic approach, powered by lightweight metadata, that generates SPARQL queries from natural language text. First, we describe its architecture, which consists of dedicated components for metadata indexing, prompt building, and query generation and execution. Then, we evaluate it based on a state-of-the-art challenge with multilingual questions, and a collection of questions from three of the most prevalent knowledge graphs within the field of bioinformatics. Our results demonstrate a substantial increase of 24% in the F1 Score on the state-of-the-art challenge, adaptability to high-resource languages such as English and Spanish, as well as ability to form complex and federated bioinformatics queries. Furthermore, we show that SPARQL-LLM is up to 36x faster than other systems participating in the challenge, while costing a maximum of $0.01 per question, making it suitable for real-time, low-cost text-to-SPARQL applications. One such application deployed over real-world decentralized knowledge graphs can be found at https://www.expasy.org/chat.

