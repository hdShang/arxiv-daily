---
layout: default
title: "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search"
---

# ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23519" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23519v1</a>
  <a href="https://arxiv.org/pdf/2509.23519.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23519v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23519v1', 'ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova

**分类**: cs.CR, cs.AI

**发布日期**: 2025-09-27

**备注**: Accepted to NeurIPS 2025

---

## 💡 一句话要点

**提出ReliabilityRAG，利用文档可靠性信息增强RAG在Web搜索中的鲁棒性，防御检索语料库攻击。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `RAG` `对抗鲁棒性` `Web搜索` `最大独立集`

## 📋 核心要点

1. 现有RAG系统易受检索语料库攻击，如提示注入，缺乏有效的防御机制。
2. ReliabilityRAG框架利用文档可靠性信息，通过图论方法识别并过滤恶意文档，增强鲁棒性。
3. 实验表明，ReliabilityRAG在对抗攻击下表现出更强的鲁棒性，同时保持高准确率，尤其擅长长文本生成。

## 📝 摘要（中文）

检索增强生成（RAG）通过将大型语言模型（LLM）的输出建立在外部文档的基础上，来增强其能力。然而，这些系统仍然容易受到检索语料库攻击，例如提示注入。基于RAG的搜索系统（例如，谷歌的搜索AI概览）为研究和防御此类威胁提供了一个有趣的场景，因为防御算法可以受益于内置的可靠性信号（如文档排名），并且由于数十年来为阻止SEO所做的工作，对攻击者来说代表着一个非LLM的挑战。受此场景的启发，但不限于此，本研究引入了ReliabilityRAG，这是一个对抗鲁棒性框架，它显式地利用了检索文档的可靠性信息。我们的第一个贡献采用图论的视角来识别检索文档中的“一致多数”，以过滤掉恶意文档。我们引入了一种基于在文档图上寻找最大独立集（MIS）的新算法，其中边编码矛盾。我们的MIS变体显式地优先考虑更高可靠性的文档，并在自然假设下提供针对有界对抗性破坏的可证明鲁棒性保证。认识到对于大型检索集，精确MIS的计算成本很高，我们的第二个贡献是一个可扩展的加权样本和聚合框架。它显式地利用可靠性信息，在有效处理许多文档的同时，保留了一些鲁棒性保证。我们提出的实验结果表明，与先前的方法相比，ReliabilityRAG提供了优越的对抗攻击鲁棒性，保持了较高的良性准确性，并且在先前以鲁棒性为中心的方法难以处理的长格式生成任务中表现出色。我们的工作是朝着更有效、可证明的鲁棒防御迈出的重要一步，以应对RAG中检索到的语料库损坏。

## 🔬 方法详解

**问题定义**：论文旨在解决RAG系统在Web搜索等场景中，由于检索到的文档被恶意篡改或注入攻击内容，导致LLM生成错误或有害信息的问题。现有方法在防御此类攻击时，要么鲁棒性不足，要么在长文本生成等任务中表现不佳。

**核心思路**：论文的核心思路是利用检索文档的可靠性信息，例如文档的排名、来源的可信度等，来识别并过滤掉恶意文档。通过寻找文档之间的一致性，并优先考虑高可靠性的文档，从而提高RAG系统的鲁棒性。

**技术框架**：ReliabilityRAG框架包含以下主要阶段：1) 文档检索：从外部知识库检索相关文档。2) 文档图构建：构建一个文档图，其中节点代表文档，边表示文档之间的矛盾关系。3) 最大独立集（MIS）查找：在文档图上寻找最大独立集，该独立集代表一组相互一致且可靠的文档。论文提出了一个加权MIS算法，优先选择高可靠性的文档。4) 答案生成：利用选定的可靠文档，通过LLM生成最终答案。

**关键创新**：论文的关键创新在于：1) 提出了一种基于图论的文档一致性分析方法，能够有效地识别和过滤恶意文档。2) 设计了一种加权MIS算法，能够显式地利用文档的可靠性信息，提高鲁棒性。3) 提出了一个可扩展的采样和聚合框架，能够在处理大量文档时保持效率和鲁棒性。

**关键设计**：加权MIS算法的关键设计在于，为每个文档节点赋予一个权重，该权重与其可靠性成正比。在寻找最大独立集时，算法优先选择权重较高的节点。此外，论文还设计了一种基于矛盾关系的边权重计算方法，用于衡量文档之间的不一致程度。采样和聚合框架的关键设计在于，通过随机采样文档子集，并在每个子集上运行MIS算法，然后将结果聚合起来，从而降低计算复杂度。

## 📊 实验亮点

实验结果表明，ReliabilityRAG在对抗攻击下显著优于现有方法，在良性查询下保持高准确率，并在长文本生成任务中表现出色。具体性能数据未知，但论文强调了其在鲁棒性、准确性和长文本生成能力方面的综合优势。

## 🎯 应用场景

ReliabilityRAG可应用于各种基于RAG的Web搜索和问答系统，例如搜索引擎、智能助手和知识图谱。通过提高RAG系统的鲁棒性，可以有效防御恶意攻击，确保用户获取准确、可靠的信息，提升用户体验和安全性。该研究对构建更安全、更可靠的AI系统具有重要意义。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) enhances Large Language Models by grounding their outputs in external documents. These systems, however, remain vulnerable to attacks on the retrieval corpus, such as prompt injection. RAG-based search systems (e.g., Google's Search AI Overview) present an interesting setting for studying and protecting against such threats, as defense algorithms can benefit from built-in reliability signals -- like document ranking -- and represent a non-LLM challenge for the adversary due to decades of work to thwart SEO.
>   Motivated by, but not limited to, this scenario, this work introduces ReliabilityRAG, a framework for adversarial robustness that explicitly leverages reliability information of retrieved documents.
>   Our first contribution adopts a graph-theoretic perspective to identify a "consistent majority" among retrieved documents to filter out malicious ones. We introduce a novel algorithm based on finding a Maximum Independent Set (MIS) on a document graph where edges encode contradiction. Our MIS variant explicitly prioritizes higher-reliability documents and provides provable robustness guarantees against bounded adversarial corruption under natural assumptions. Recognizing the computational cost of exact MIS for large retrieval sets, our second contribution is a scalable weighted sample and aggregate framework. It explicitly utilizes reliability information, preserving some robustness guarantees while efficiently handling many documents.
>   We present empirical results showing ReliabilityRAG provides superior robustness against adversarial attacks compared to prior methods, maintains high benign accuracy, and excels in long-form generation tasks where prior robustness-focused methods struggled. Our work is a significant step towards more effective, provably robust defenses against retrieved corpus corruption in RAG.

