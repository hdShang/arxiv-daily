---
layout: default
title: "REIS: A High-Performance and Energy-Efficient Retrieval System with In-Storage Processing"
---

# REIS: A High-Performance and Energy-Efficient Retrieval System with In-Storage Processing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16444" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16444v2</a>
  <a href="https://arxiv.org/pdf/2506.16444.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16444v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16444v2', 'REIS: A High-Performance and Energy-Efficient Retrieval System with In-Storage Processing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kangqi Chen, Andreas Kosmas Kakolyris, Rakesh Nadig, Manos Frouzakis, Nika Mansouri Ghiasi, Yu Liang, Haiyu Mao, Jisung Park, Mohammad Sadrosadati, Onur Mutlu

**分类**: cs.CL, cs.AR, cs.DB

**发布日期**: 2025-06-19 (更新: 2025-11-11)

**备注**: Extended version of our publication at the 52nd International Symposium on Computer Architecture (ISCA-52), 2025

---

## 💡 一句话要点

**提出REIS以解决检索增强生成中的数据检索瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `存储内处理` `近似最近邻搜索` `数据库优化` `能效提升`

## 📋 核心要点

1. 现有的检索增强生成方法在检索阶段面临显著的数据移动开销，成为推理的瓶颈。
2. REIS通过优化数据库布局、引入ISP定制的数据放置技术和利用存储内计算资源，解决了检索效率低的问题。
3. 实验结果表明，REIS在检索性能上提升了13倍，能效提升了55倍，显著优于传统服务器级系统。

## 📝 摘要（中文）

大型语言模型（LLMs）面临知识局限性的问题，检索增强生成（RAG）通过外部知识库来补充其静态知识。RAG的检索阶段是推理管道中的瓶颈，现有的近似最近邻搜索（ANNS）算法在大数据库中存在显著的数据移动开销。为此，REIS提出了一种专为RAG设计的存储内处理（ISP）系统，通过优化数据库布局、引入ISP定制的数据放置技术以及利用存储系统内的计算资源，显著提高了检索性能和能效。与服务器级系统相比，REIS在检索性能上平均提升了13倍，能效提升了55倍。

## 🔬 方法详解

**问题定义**：本论文旨在解决检索增强生成（RAG）中的检索阶段瓶颈，现有方法在处理大规模数据库时存在显著的数据移动开销，影响了性能和能效。

**核心思路**：REIS的核心思路是通过存储内处理（ISP）技术优化近似最近邻搜索（ANNS），减少数据移动并提高检索效率。设计上，REIS专为RAG系统量身定制，确保高效的数据检索和处理。

**技术框架**：REIS的整体架构包括三个主要模块：数据库布局、ISP定制的数据放置技术和ANNS引擎。数据库布局将嵌入向量与其相关文档链接，便于高效检索；数据放置技术在存储系统的不同平面上分布嵌入；ANNS引擎利用存储系统内的计算资源进行高效检索。

**关键创新**：REIS的主要创新在于其专为ISP设计的数据库布局和数据放置技术，解决了现有方法未能优化数据检索操作的问题，并避免了大规模硬件改动。

**关键设计**：REIS采用轻量级的闪存转换层（Flash Translation Layer），并在数据放置时考虑了存储系统的特性，以实现高效的ANNS操作。

## 📊 实验亮点

REIS在实验中表现出色，与传统服务器级系统相比，检索性能平均提升了13倍，能效提升了55倍。这一显著的性能提升表明REIS在处理大规模数据时的优势，具有重要的实际应用价值。

## 🎯 应用场景

REIS的研究成果在多个领域具有潜在应用价值，特别是在需要快速检索和处理大规模数据的场景，如智能搜索引擎、推荐系统和自然语言处理等。通过提高检索效率和能效，REIS能够为实时数据处理和分析提供支持，推动相关技术的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) face an inherent challenge: their knowledge is confined to the data that they have been trained on. To overcome this issue, Retrieval-Augmented Generation (RAG) complements the static training-derived knowledge of LLMs with an external knowledge repository. RAG consists of three stages: indexing, retrieval, and generation. The retrieval stage of RAG becomes a significant bottleneck in inference pipelines. In this stage, a user query is mapped to an embedding vector and an Approximate Nearest Neighbor Search (ANNS) algorithm searches for similar vectors in the database to identify relevant items. Due to the large database sizes, ANNS incurs significant data movement overheads between the host and the storage system. To alleviate these overheads, prior works propose In-Storage Processing (ISP) techniques that accelerate ANNS by performing computations inside storage. However, existing works that leverage ISP for ANNS (i) employ algorithms that are not tailored to ISP systems, (ii) do not accelerate data retrieval operations for data selected by ANNS, and (iii) introduce significant hardware modifications, limiting performance and hindering their adoption. We propose REIS, the first ISP system tailored for RAG that addresses these limitations with three key mechanisms. First, REIS employs a database layout that links database embedding vectors to their associated documents, enabling efficient retrieval. Second, it enables efficient ANNS by introducing an ISP-tailored data placement technique that distributes embeddings across the planes of the storage system and employs a lightweight Flash Translation Layer. Third, REIS leverages an ANNS engine that uses the existing computational resources inside the storage system. Compared to a server-grade system, REIS improves the performance (energy efficiency) of retrieval by an average of 13x (55x).

