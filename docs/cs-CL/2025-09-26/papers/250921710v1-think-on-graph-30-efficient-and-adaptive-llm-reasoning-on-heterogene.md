---
layout: default
title: "Think-on-Graph 3.0: Efficient and Adaptive LLM Reasoning on Heterogeneous Graphs via Multi-Agent Dual-Evolving Context Retrieval"
---

# Think-on-Graph 3.0: Efficient and Adaptive LLM Reasoning on Heterogeneous Graphs via Multi-Agent Dual-Evolving Context Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21710" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21710v1</a>
  <a href="https://arxiv.org/pdf/2509.21710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21710v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21710v1', 'Think-on-Graph 3.0: Efficient and Adaptive LLM Reasoning on Heterogeneous Graphs via Multi-Agent Dual-Evolving Context Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaojun Wu, Cehao Yang, Xueyuan Lin, Chengjin Xu, Xuhui Jiang, Yuanliang Sun, Hui Xiong, Jia Li, Jian Guo

**分类**: cs.CL

**发布日期**: 2025-09-26

**备注**: 28 pages, 17 figures

---

## 💡 一句话要点

**Think-on-Graph 3.0：通过多智能体双重演化上下文检索，实现异构图上高效自适应的LLM推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `知识图谱` `多智能体系统` `异构图` `LLM推理`

## 📋 核心要点

1. 现有基于图的RAG方法依赖高质量图结构，但手动构建成本高昂，自动提取受限于LLM提取器性能。
2. ToG-3通过多智能体上下文演化和检索(MACER)机制，动态构建和细化异构图索引，实现精确证据检索。
3. 实验表明，ToG-3在深度和广泛的推理基准测试中优于现有方法，验证了MACER框架的有效性。

## 📝 摘要（中文）

检索增强生成(RAG)和基于图的RAG已成为增强大型语言模型(LLM)外部知识的重要范例。然而，现有方法面临着根本性的权衡。虽然基于图的方法本质上依赖于高质量的图结构，但它们面临着重大的实际约束：手动构建知识图谱的扩展成本过高，而从语料库中自动提取的图受到底层LLM提取器性能的限制，尤其是在使用较小的本地部署模型时。本文提出了Think-on-Graph 3.0 (ToG-3)，这是一个新颖的框架，引入了多智能体上下文演化和检索(MACER)机制来克服这些限制。我们的核心创新是动态构建和细化Chunk-Triplets-Community异构图索引，该索引开创性地结合了演化查询和演化子图的双重演化机制，以实现精确的证据检索。这种方法解决了先前基于图的RAG方法的一个关键限制，即它们通常以单次静态方式构建图索引，而不适应实际查询。一个由Constructor、Retriever、Reflector和Responser智能体组成的多智能体系统，协同参与证据检索、答案生成、充分性反思以及至关重要的演化查询和子图的迭代过程。这种双重演化的多智能体系统使ToG-3能够在推理过程中自适应地构建目标图索引，从而减轻了静态、一次性图构建的固有缺陷，并即使使用轻量级LLM也能实现深度、精确的推理。大量的实验表明，ToG-3在深度和广泛的推理基准测试中都优于对比基线，并且消融研究证实了MACER框架组件的有效性。

## 🔬 方法详解

**问题定义**：现有基于图的RAG方法，要么依赖于手动构建的知识图谱，成本高昂难以扩展；要么依赖于自动提取的图，但受限于底层LLM提取器的性能，尤其是在资源受限的环境下，导致推理效果不佳。痛点在于静态图索引无法适应实际查询，导致检索到的信息不够精确。

**核心思路**：ToG-3的核心思路是动态构建和细化图索引，使其能够自适应地响应不同的查询。通过引入多智能体系统，模拟人类思考过程，迭代地进行证据检索、答案生成和反思，并在此过程中不断演化查询和子图，从而构建一个更精确、更相关的图索引。

**技术框架**：ToG-3采用多智能体上下文演化和检索(MACER)框架，包含四个主要智能体：Constructor（负责构建初始图索引）、Retriever（负责从图中检索相关信息）、Reflector（负责评估答案的充分性并指导查询演化）、Responser（负责生成最终答案）。整个流程是一个迭代过程，Retriever根据当前查询从图中检索信息，Responser生成答案，Reflector评估答案的充分性，并根据评估结果指导Constructor演化查询和子图，然后再次进行检索，直到答案足够充分。

**关键创新**：ToG-3最重要的技术创新点在于双重演化机制，即Evolving Query和Evolving Sub-Graph。传统的图RAG方法通常构建一个静态的图索引，然后直接在上面进行检索，而ToG-3则根据实际查询动态地调整查询和子图，从而实现更精确的检索。这种双重演化机制使得ToG-3能够更好地适应不同的查询，并减轻了对初始图质量的依赖。

**关键设计**：ToG-3使用Chunk-Triplets-Community异构图索引，其中Chunk表示文本块，Triplets表示文本块之间的关系三元组，Community表示文本块的社区结构。Constructor智能体负责构建这个图索引，它使用LLM从语料库中提取Chunk和Triplets，并使用社区检测算法识别Community。Reflector智能体使用LLM评估答案的充分性，并生成新的查询或子图演化指令。具体参数设置和损失函数等技术细节在论文中未明确说明，可能使用了标准的LLM训练方法和社区检测算法。

## 📊 实验亮点

实验结果表明，ToG-3在深度和广泛的推理基准测试中均优于现有方法。具体性能数据和提升幅度在摘要中未明确给出，但强调了ToG-3在各种推理任务中的有效性。消融实验也证实了MACER框架中各个组件的有效性。

## 🎯 应用场景

ToG-3可应用于各种需要利用外部知识进行推理的场景，例如问答系统、对话系统、知识库检索等。尤其适用于知识图谱构建成本高昂或质量不佳的领域，例如金融、医疗等。该研究有助于提升LLM在复杂推理任务中的表现，并降低对高质量知识图谱的依赖。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) and Graph-based RAG has become the important paradigm for enhancing Large Language Models (LLMs) with external knowledge. However, existing approaches face a fundamental trade-off. While graph-based methods are inherently dependent on high-quality graph structures, they face significant practical constraints: manually constructed knowledge graphs are prohibitively expensive to scale, while automatically extracted graphs from corpora are limited by the performance of the underlying LLM extractors, especially when using smaller, local-deployed models. This paper presents Think-on-Graph 3.0 (ToG-3), a novel framework that introduces Multi-Agent Context Evolution and Retrieval (MACER) mechanism to overcome these limitations. Our core innovation is the dynamic construction and refinement of a Chunk-Triplets-Community heterogeneous graph index, which pioneeringly incorporates a dual-evolution mechanism of Evolving Query and Evolving Sub-Graph for precise evidence retrieval. This approach addresses a critical limitation of prior Graph-based RAG methods, which typically construct a static graph index in a single pass without adapting to the actual query. A multi-agent system, comprising Constructor, Retriever, Reflector, and Responser agents, collaboratively engages in an iterative process of evidence retrieval, answer generation, sufficiency reflection, and, crucially, evolving query and subgraph. This dual-evolving multi-agent system allows ToG-3 to adaptively build a targeted graph index during reasoning, mitigating the inherent drawbacks of static, one-time graph construction and enabling deep, precise reasoning even with lightweight LLMs. Extensive experiments demonstrate that ToG-3 outperforms compared baselines on both deep and broad reasoning benchmarks, and ablation studies confirm the efficacy of the components of MACER framework.

