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

**提出SPARQL-LLM方法，通过轻量级元数据实现实时、低成本的文本到SPARQL查询生成，适用于分布式知识图谱应用。**

🎯 **匹配领域**: **视觉里程计** **强化学习**

**关键词**: `SPARQL查询生成` `自然语言处理` `知识图谱` `联邦查询` `轻量级元数据` `实时系统` `低成本计算` `生物信息学应用`

## 📋 核心要点

1. 现有方法主要关注单一来源的查询准确性，但忽略了联邦查询能力、运行时间和成本，导致难以在生产环境中部署。
2. SPARQL-LLM采用轻量级元数据和专用组件架构，实现与三元存储无关的文本到SPARQL查询生成，提升效率和适应性。
3. 实验显示，F1分数提高24%，支持多语言和复杂联邦查询，运行速度快达36倍，成本低至每问题0.01美元。

## 📝 摘要（中文）

大型语言模型的出现促进了从自然语言生成结构化查询（如SPARQL查询）的新方法。然而，这些新方法大多关注单一来源的响应准确性，而忽略了其他评估标准，如分布式数据存储上的联邦查询能力，以及生成SPARQL查询的运行时间和成本。因此，它们通常不适合生产环境或难以在（可能联邦的）知识图谱上以良好准确性部署。为缓解这些问题，本文扩展了先前工作，描述并系统评估了SPARQL-LLM，这是一种开源且与三元存储无关的方法，由轻量级元数据驱动，从自然语言文本生成SPARQL查询。首先，我们描述了其架构，包括元数据索引、提示构建、查询生成和执行等专用组件。然后，基于一个包含多语言问题的最新挑战，以及来自生物信息学领域三个最流行知识图谱的问题集合进行评估。结果显示，在最新挑战中F1分数显著提高了24%，适应英语和西班牙语等高资源语言，并能形成复杂和联邦的生物信息学查询。此外，SPARQL-LLM比参与挑战的其他系统快达36倍，每个问题成本最高为0.01美元，使其适用于实时、低成本的文本到SPARQL应用。一个部署在真实世界去中心化知识图谱上的此类应用可在https://www.expasy.org/chat找到。

## 🔬 方法详解

**问题定义**：论文旨在解决从自然语言生成SPARQL查询的挑战，现有方法痛点包括过度依赖单一数据源、缺乏联邦查询支持、运行成本高且难以实时部署，限制了在生产环境中的应用。

**核心思路**：通过轻量级元数据驱动，结合大型语言模型，设计一个开源、与三元存储无关的框架，以平衡准确性、效率和成本，实现实时、低成本的查询生成，特别强调对分布式知识图谱的适应性。

**技术框架**：整体架构包括三个主要阶段：元数据索引阶段，用于提取和存储知识图谱的轻量级结构信息；提示构建阶段，基于元数据生成上下文丰富的提示，以指导语言模型；查询生成和执行阶段，利用语言模型生成SPARQL查询并执行验证，确保查询的正确性和可执行性。

**关键创新**：最重要的技术创新是引入轻量级元数据作为中介，减少对原始数据的依赖，从而提升查询生成的速度和成本效益，同时支持联邦查询，与现有方法相比，本质区别在于更注重生产环境中的实用性和可扩展性。

**关键设计**：关键设计包括元数据索引的优化算法，以减少存储和检索开销；提示构建中使用模板化方法，结合多语言支持；查询生成阶段集成错误检测和修正机制；整体框架基于开源工具，参数设置灵活，以适应不同知识图谱和语言模型，具体损失函数和网络结构细节在论文中未明确说明，可能依赖于标准语言模型训练。

## 📊 实验亮点

在最新挑战中，SPARQL-LLM的F1分数比基线方法提高了24%，展示了在多语言（如英语和西班牙语）和复杂联邦查询上的优越性能；运行速度比其他系统快达36倍，每个问题成本最高仅0.01美元，验证了其在实时、低成本应用中的有效性。

## 🎯 应用场景

该研究在生物信息学、语义网和智能问答系统等领域具有广泛应用潜力，能支持实时、低成本的文本到SPARQL查询转换，促进分布式知识图谱的交互式访问，提升数据检索效率，未来可能扩展到更多行业如医疗、金融，推动知识驱动应用的发展。

## 📄 摘要（原文）

> The advent of large language models is contributing to the emergence of novel approaches that promise to better tackle the challenge of generating structured queries, such as SPARQL queries, from natural language. However, these new approaches mostly focus on response accuracy over a single source while ignoring other evaluation criteria, such as federated query capability over distributed data stores, as well as runtime and cost to generate SPARQL queries. Consequently, they are often not production-ready or easy to deploy over (potentially federated) knowledge graphs with good accuracy. To mitigate these issues, in this paper, we extend our previous work and describe and systematically evaluate SPARQL-LLM, an open-source and triplestore-agnostic approach, powered by lightweight metadata, that generates SPARQL queries from natural language text. First, we describe its architecture, which consists of dedicated components for metadata indexing, prompt building, and query generation and execution. Then, we evaluate it based on a state-of-the-art challenge with multilingual questions, and a collection of questions from three of the most prevalent knowledge graphs within the field of bioinformatics. Our results demonstrate a substantial increase of 24% in the F1 Score on the state-of-the-art challenge, adaptability to high-resource languages such as English and Spanish, as well as ability to form complex and federated bioinformatics queries. Furthermore, we show that SPARQL-LLM is up to 36x faster than other systems participating in the challenge, while costing a maximum of $0.01 per question, making it suitable for real-time, low-cost text-to-SPARQL applications. One such application deployed over real-world decentralized knowledge graphs can be found at https://www.expasy.org/chat.

