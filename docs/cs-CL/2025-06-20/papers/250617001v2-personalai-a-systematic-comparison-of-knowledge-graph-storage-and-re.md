---
layout: default
title: "PersonalAI: A Systematic Comparison of Knowledge Graph Storage and Retrieval Approaches for Personalized LLM agents"
---

# PersonalAI: A Systematic Comparison of Knowledge Graph Storage and Retrieval Approaches for Personalized LLM agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17001" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17001v2</a>
  <a href="https://arxiv.org/pdf/2506.17001.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17001v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17001v2', 'PersonalAI: A Systematic Comparison of Knowledge Graph Storage and Retrieval Approaches for Personalized LLM agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mikhail Menschikov, Dmitry Evseev, Victoria Dochkina, Ruslan Kostoev, Ilia Perepechkin, Petr Anokhin, Evgeny Burnaev, Nikita Semenov

**分类**: cs.CL, cs.IR

**发布日期**: 2025-06-20 (更新: 2025-08-11)

---

## 💡 一句话要点

**提出基于知识图谱的外部记忆框架以解决个性化LLM代理的存储与检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化语言模型` `知识图谱` `外部记忆` `检索增强生成` `动态语义表示` `时间依赖推理` `自适应AI系统`

## 📋 核心要点

1. 现有的个性化语言模型在处理用户交互历史时缺乏结构化记忆，难以应对复杂的长期交互。
2. 本文提出了一种基于知识图谱的外部记忆框架，能够自动构建和更新，支持多种信息编码格式。
3. 在多个基准测试中，系统表现出不同记忆和检索配置的最佳性能，展示了其在时间依赖和上下文推理中的有效性。

## 📝 摘要（中文）

个性化语言模型通过有效整合用户交互历史仍然是自适应AI系统开发中的核心挑战。尽管结合了检索增强生成（RAG）的大型语言模型（LLMs）在事实准确性上有所改善，但它们通常缺乏结构化记忆，无法在复杂的长期交互中扩展。为此，本文提出了一种灵活的外部记忆框架，基于知识图谱，能够自动构建和更新，支持多种信息编码格式。基于AriGraph架构，本文引入了一种新型混合图设计，支持标准边和两种超边，能够实现丰富的动态语义和时间表示。我们的框架还支持多种检索机制，使其适应不同的数据集和LLM能力。通过在TriviaQA、HotpotQA和DiaASQ三个基准上的评估，展示了不同的记忆和检索配置在任务中的最佳性能。

## 🔬 方法详解

**问题定义**：本文旨在解决个性化语言模型在长期交互中缺乏结构化记忆的问题。现有方法在处理复杂用户交互历史时表现不佳，难以有效存储和检索信息。

**核心思路**：提出了一种灵活的外部记忆框架，基于知识图谱，能够自动构建和更新，支持多种信息编码格式，以增强模型的记忆能力和检索效率。

**技术框架**：整体架构包括知识图谱的构建、信息编码、检索机制等模块。知识图谱通过LLM自动更新，支持节点、三元组、高阶命题和情节痕迹的编码。

**关键创新**：引入了混合图设计，支持标准边和两种超边，能够实现丰富的动态语义和时间表示。这一设计使得模型在处理复杂关系时更具灵活性。

**关键设计**：系统支持多种检索机制，如A*、水圈传播、束搜索等，能够根据不同数据集和LLM能力进行适配。

## 📊 实验亮点

在TriviaQA、HotpotQA和DiaASQ基准测试中，系统表现出不同记忆和检索配置的最佳性能，尤其是在处理时间依赖和上下文推理方面，展示了显著的效果提升，验证了框架的有效性和鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括个性化助手、智能客服和教育技术等。通过有效管理用户交互历史，系统能够提供更为精准和个性化的响应，提升用户体验。未来，该框架有望在更广泛的自适应AI系统中得到应用，推动个性化技术的发展。

## 📄 摘要（原文）

> Personalizing language models by effectively incorporating user interaction history remains a central challenge in the development of adaptive AI systems. While large language models (LLMs) combined with Retrieval-Augmented Generation (RAG) have improved factual accuracy, they often lack structured memory and fail to scale in complex, long-term interactions. To address this, we propose a flexible external memory framework based on knowledge graphs, automatically constructed and updated by the LLM itself, and capable of encoding information in multiple formats-including nodes, triplets, higher-order propositions, and episodic traces. Building upon the AriGraph architecture, we introduce a novel hybrid graph design that supports both standard edges and two types of hyperedges, enabling rich and dynamic semantic and temporal representations. Our framework also supports diverse retrieval mechanisms, including A*, water-circle propagation, beam search, and hybrid methods, making it adaptable to different datasets and LLM capacities. We evaluate our system on three benchmarks-TriviaQA, HotpotQA, and DiaASQ-demonstrating that different memory and retrieval configurations yield optimal performance depending on the task. Additionally, we extend the DiaASQ benchmark with temporal annotations and internally contradictory statements, showing that our system remains robust and effective in managing temporal dependencies and context-aware reasoning.

