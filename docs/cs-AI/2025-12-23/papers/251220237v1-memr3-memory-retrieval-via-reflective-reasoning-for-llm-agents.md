---
layout: default
title: MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agents
---

# MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20237" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20237v1</a>
  <a href="https://arxiv.org/pdf/2512.20237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20237v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20237v1', 'MemR$^3$: Memory Retrieval via Reflective Reasoning for LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingbo Du, Loka Li, Duzhen Zhang, Le Song

**分类**: cs.AI

**发布日期**: 2025-12-23

**备注**: 16 pages, 6 figures

---

## 💡 一句话要点

**MemR³：通过反思推理实现LLM Agent的记忆检索，提升问答质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `记忆检索` `反思推理` `闭环控制` `证据追踪`

## 📋 核心要点

1. 现有记忆系统侧重压缩存储，缺乏对检索的显式闭环控制，导致LLM Agent在复杂任务中难以有效利用历史经验。
2. MemR³通过引入路由器和全局证据缺口追踪器，实现检索、反思和回答的自主决策，优化证据收集过程，提升答案质量。
3. 实验表明，MemR³在LoCoMo基准测试中超越了现有基线，显著提升了RAG和Zep等检索器的性能，尤其是在问答质量方面。

## 📝 摘要（中文）

本文提出了一种名为MemR³的记忆检索系统，旨在提升大型语言模型（LLM）Agent利用历史经验的能力。与现有主要优化压缩和存储的记忆系统不同，MemR³更侧重于对记忆检索进行显式的闭环控制。该系统包含两个核心机制：1) 一个路由器，用于在检索、反思和回答动作之间进行选择，以优化答案质量；2) 一个全局证据缺口追踪器，用于显式地呈现回答过程并追踪证据收集过程。这种设计通过引入闭环控制机制，实现了自主决策，从而突破了标准的检索-然后-回答的流程。在LoCoMo基准测试上的实验结果表明，MemR³在LLM-as-a-Judge评分上超越了强大的基线，并且在使用GPT-4.1-mini后端时，在RAG（+7.29%）和Zep（+1.94%）等四个类别上改进了现有的检索器，为现有的记忆存储提供了一个即插即用的控制器。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）Agent的记忆系统，虽然能够存储和压缩历史信息，但在检索阶段缺乏有效的控制机制。传统的“检索-然后-回答”流程是单向的，无法根据回答过程中的证据缺口进行动态调整，导致回答质量受限。因此，需要一种能够自主控制检索过程，并根据反馈进行反思和调整的记忆检索系统。

**核心思路**：MemR³的核心思路是将记忆检索过程建模为一个自主决策过程，通过引入闭环控制机制，使Agent能够根据当前的证据状态和回答需求，动态地选择不同的动作（检索、反思、回答）。这种设计允许Agent在检索过程中不断评估证据的充分性，并根据需要进行反思和补充检索，从而提高回答的准确性和完整性。

**技术框架**：MemR³包含两个主要模块：路由器和全局证据缺口追踪器。路由器负责在检索、反思和回答三个动作之间进行选择，其决策基于当前的问题、已检索到的证据以及证据缺口追踪器的反馈。全局证据缺口追踪器负责监控回答过程中的证据收集情况，并识别出缺失或不足的证据，为路由器提供决策依据。整个流程是一个迭代的过程，Agent不断地进行检索、反思和回答，直到证据充分或达到预设的停止条件。

**关键创新**：MemR³最重要的创新在于引入了闭环控制机制，将记忆检索过程从一个单向的流程转变为一个动态的决策过程。通过路由器和全局证据缺口追踪器的协同工作，Agent能够自主地控制检索过程，并根据反馈进行反思和调整。这种设计使得Agent能够更有效地利用历史信息，并生成更准确、更完整的回答。与传统的检索方法相比，MemR³能够更好地适应复杂的问题和动态的环境。

**关键设计**：路由器的设计是MemR³的关键。路由器需要学习在不同的状态下选择合适的动作。这可以通过强化学习或监督学习来实现。全局证据缺口追踪器需要能够准确地识别出缺失或不足的证据。这可以通过分析已检索到的证据和问题之间的语义关系来实现。具体的实现细节，例如路由器的网络结构、证据缺口追踪器的算法等，需要根据具体的应用场景进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20237v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20237v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20237v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在LoCoMo基准测试中，MemR³在使用GPT-4.1-mini后端时，在RAG上取得了+7.29%的提升，在Zep上取得了+1.94%的提升。这些结果表明，MemR³能够有效地提升现有检索器的性能，并显著提高LLM Agent的问答质量。实验结果还表明，MemR³在四个类别上均优于现有检索器，证明了其通用性和有效性。

## 🎯 应用场景

MemR³可应用于各种需要LLM Agent进行复杂推理和决策的场景，例如智能客服、知识问答、任务规划和代码生成等。通过提升Agent对历史信息的利用效率和回答质量，MemR³能够显著提高这些应用的性能和用户体验。未来，MemR³有望成为LLM Agent记忆系统的标准组件，推动Agent技术的发展。

## 📄 摘要（原文）

> Memory systems have been designed to leverage past experiences in Large Language Model (LLM) agents. However, many deployed memory systems primarily optimize compression and storage, with comparatively less emphasis on explicit, closed-loop control of memory retrieval. From this observation, we build memory retrieval as an autonomous, accurate, and compatible agent system, named MemR$^3$, which has two core mechanisms: 1) a router that selects among retrieve, reflect, and answer actions to optimize answer quality; 2) a global evidence-gap tracker that explicitly renders the answering process transparent and tracks the evidence collection process. This design departs from the standard retrieve-then-answer pipeline by introducing a closed-loop control mechanism that enables autonomous decision-making. Empirical results on the LoCoMo benchmark demonstrate that MemR$^3$ surpasses strong baselines on LLM-as-a-Judge score, and particularly, it improves existing retrievers across four categories with an overall improvement on RAG (+7.29%) and Zep (+1.94%) using GPT-4.1-mini backend, offering a plug-and-play controller for existing memory stores.

