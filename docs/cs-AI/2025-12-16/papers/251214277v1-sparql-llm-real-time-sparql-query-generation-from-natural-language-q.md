---
layout: default
title: SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions
---

# SPARQL-LLM: Real-Time SPARQL Query Generation from Natural Language Questions

**arXiv**: [2512.14277v1](https://arxiv.org/abs/2512.14277) | [PDF](https://arxiv.org/pdf/2512.14277.pdf)

**作者**: Panayiotis Smeros, Vincent Emonet, Ruijie Wang, Ana-Claudia Sima, Tarcisio Mendes de Farias

**分类**: cs.IR, cs.AI, cs.CL

**发布日期**: 2025-12-16

**备注**: 17 pages, 8 figures, 1 table. Under Review

---

## 💡 一句话要点

**提出SPARQL-LLM方法，通过轻量级元数据实现实时、低成本的自然语言到SPARQL查询生成，适用于分布式知识图谱应用。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `SPARQL查询生成` `自然语言处理` `知识图谱` `联邦查询` `轻量级元数据` `实时系统` `低成本应用` `生物信息学`

## 📋 核心要点

1. 现有方法主要关注单一数据源的准确性，忽视联邦查询能力、运行时间和成本，导致难以在生产环境中部署或适应分布式知识图谱。
2. SPARQL-LLM采用轻量级元数据索引和专用组件架构，实现与三元存储无关的查询生成，提升灵活性和效率。
3. 实验显示F1分数提高24%，支持多语言和复杂联邦查询，运行速度快达36倍，成本低至每问题0.01美元。

## 📝 摘要（中文）

大型语言模型的出现催生了从自然语言生成结构化查询（如SPARQL查询）的新方法。然而，这些方法大多关注单一数据源的响应准确性，而忽略了其他评估标准，如分布式数据存储的联邦查询能力，以及生成SPARQL查询的运行时间和成本。因此，它们通常难以在生产环境中部署，或在（可能联邦的）知识图谱上实现高精度。为缓解这些问题，本文扩展了先前工作，提出并系统评估了SPARQL-LLM——一种开源、与三元存储无关的方法，利用轻量级元数据从自然语言文本生成SPARQL查询。首先，我们描述了其架构，包括元数据索引、提示构建、查询生成和执行等专用组件。然后，基于一个包含多语言问题的最新挑战，以及来自生物信息学领域三个最流行知识图谱的问题集合，对其进行了评估。结果显示，在最新挑战中F1分数显著提高了24%，适应英语和西班牙语等高资源语言，并能形成复杂和联邦的生物信息学查询。此外，SPARQL-LLM比参与挑战的其他系统快达36倍，每个问题成本最高仅0.01美元，使其适用于实时、低成本的文本到SPARQL应用。一个部署在真实世界去中心化知识图谱上的此类应用可在https://www.expasy.org/chat找到。

## 🔬 方法详解

SPARQL-LLM的整体框架包括元数据索引、提示构建、查询生成和执行三个核心组件。关键技术创新在于利用轻量级元数据（而非完整数据）来驱动查询生成，这降低了计算负担并提高了可扩展性。与现有方法的主要区别在于其三元存储无关性，能够处理分布式知识图谱的联邦查询，同时优化了运行时间和成本，使其更适用于实时生产环境。

## 📊 实验亮点

在最新挑战中F1分数提升24%，支持英语和西班牙语多语言查询，能生成复杂联邦查询，运行速度比其他系统快达36倍，每个问题成本最高仅0.01美元。

## 🎯 应用场景

该研究适用于生物信息学、知识图谱查询和智能问答系统等领域，特别是在需要实时、低成本处理自然语言查询的分布式知识图谱应用中，如在线知识服务平台或科研数据检索工具。

## 📄 摘要（原文）

> The advent of large language models is contributing to the emergence of novel approaches that promise to better tackle the challenge of generating structured queries, such as SPARQL queries, from natural language. However, these new approaches mostly focus on response accuracy over a single source while ignoring other evaluation criteria, such as federated query capability over distributed data stores, as well as runtime and cost to generate SPARQL queries. Consequently, they are often not production-ready or easy to deploy over (potentially federated) knowledge graphs with good accuracy. To mitigate these issues, in this paper, we extend our previous work and describe and systematically evaluate SPARQL-LLM, an open-source and triplestore-agnostic approach, powered by lightweight metadata, that generates SPARQL queries from natural language text. First, we describe its architecture, which consists of dedicated components for metadata indexing, prompt building, and query generation and execution. Then, we evaluate it based on a state-of-the-art challenge with multilingual questions, and a collection of questions from three of the most prevalent knowledge graphs within the field of bioinformatics. Our results demonstrate a substantial increase of 24% in the F1 Score on the state-of-the-art challenge, adaptability to high-resource languages such as English and Spanish, as well as ability to form complex and federated bioinformatics queries. Furthermore, we show that SPARQL-LLM is up to 36x faster than other systems participating in the challenge, while costing a maximum of $0.01 per question, making it suitable for real-time, low-cost text-to-SPARQL applications. One such application deployed over real-world decentralized knowledge graphs can be found at https://www.expasy.org/chat.

