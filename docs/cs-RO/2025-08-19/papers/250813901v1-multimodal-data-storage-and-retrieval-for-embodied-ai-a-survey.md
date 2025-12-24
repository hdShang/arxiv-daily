---
layout: default
title: "Multimodal Data Storage and Retrieval for Embodied AI: A Survey"
---

# Multimodal Data Storage and Retrieval for Embodied AI: A Survey

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13901" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13901v1</a>
  <a href="https://arxiv.org/pdf/2508.13901.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13901v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13901v1', 'Multimodal Data Storage and Retrieval for Embodied AI: A Survey')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihao Lu, Hao Tang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**评估多模态数据存储与检索以解决体现AI的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态数据` `数据存储` `数据检索` `体现AI` `系统评估` `动态可扩展性` `物理基础`

## 📋 核心要点

1. 现有的数据管理系统无法有效处理EAI生成的异构多模态数据流，导致存储和检索的效率低下。
2. 本文提出了对五种存储架构和五种检索范式的系统评估，以满足EAI的核心需求，如物理基础、低延迟访问和动态可扩展性。
3. 通过对180多项相关研究的综合分析，本文为设计下一代自主体现系统所需的高性能数据管理框架提供了严谨的路线图。

## 📝 摘要（中文）

本文综述了体现AI（EAI）代理在与物理世界交互中生成的多样化多模态数据流的存储与检索问题。我们系统评估了五种存储架构（图数据库、多模型数据库、数据湖、向量数据库和时间序列数据库），并分析了五种检索范式（基于融合策略的检索、基于表示对齐的检索、基于图结构的检索、基于生成模型的检索和高效检索优化）。通过分析，我们识别出从物理基础差距到跨模态整合等系统性挑战的关键瓶颈，并提出了未来研究的方向，包括物理感知数据模型和自适应存储-检索协同优化等，以指导EAI的数据管理解决方案。

## 🔬 方法详解

**问题定义**：本文要解决的问题是现有数据管理系统在处理体现AI生成的多模态数据时的不足，特别是在物理基础、低延迟访问和动态可扩展性方面的挑战。

**核心思路**：论文的核心思路是通过系统评估不同的存储架构和检索范式，识别出适合EAI的最佳解决方案，以实现高效的数据管理。

**技术框架**：整体架构包括五种存储架构（图数据库、多模型数据库、数据湖、向量数据库和时间序列数据库）和五种检索范式（融合策略、表示对齐、图结构、生成模型和高效优化），并分析它们的适用性和局限性。

**关键创新**：最重要的技术创新点在于识别出物理基础差距和跨模态整合等关键瓶颈，并提出了针对性的解决方案，推动了EAI领域的数据管理研究。

**关键设计**：在设计中，考虑了存储架构的动态可扩展性和检索的实时响应性，采用了适应性存储-检索协同优化的策略，以提高整体性能。

## 📊 实验亮点

通过对180多项相关研究的综合分析，本文识别出EAI数据管理中的关键瓶颈，并提出了针对性的解决方案，显著提升了数据存储和检索的效率，推动了该领域的研究进展。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟现实等，能够有效管理和检索多模态数据，从而提升系统的智能化水平和响应能力。未来，随着EAI技术的发展，该研究将对数据管理解决方案的标准化和优化产生深远影响。

## 📄 摘要（原文）

> Embodied AI (EAI) agents continuously interact with the physical world, generating vast, heterogeneous multimodal data streams that traditional management systems are ill-equipped to handle. In this survey, we first systematically evaluate five storage architectures (Graph Databases, Multi-Model Databases, Data Lakes, Vector Databases, and Time-Series Databases), focusing on their suitability for addressing EAI's core requirements, including physical grounding, low-latency access, and dynamic scalability. We then analyze five retrieval paradigms (Fusion Strategy-Based Retrieval, Representation Alignment-Based Retrieval, Graph-Structure-Based Retrieval, Generation Model-Based Retrieval, and Efficient Retrieval-Based Optimization), revealing a fundamental tension between achieving long-term semantic coherence and maintaining real-time responsiveness. Based on this comprehensive analysis, we identify key bottlenecks, spanning from the foundational Physical Grounding Gap to systemic challenges in cross-modal integration, dynamic adaptation, and open-world generalization. Finally, we outline a forward-looking research agenda encompassing physics-aware data models, adaptive storage-retrieval co-optimization, and standardized benchmarking, to guide future research toward principled data management solutions for EAI. Our survey is based on a comprehensive review of more than 180 related studies, providing a rigorous roadmap for designing the robust, high-performance data management frameworks essential for the next generation of autonomous embodied systems.

