---
layout: default
title: RAR: Setting Knowledge Tripwires for Retrieval Augmented Rejection
---

# RAR: Setting Knowledge Tripwires for Retrieval Augmented Rejection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13581" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13581v1</a>
  <a href="https://arxiv.org/pdf/2505.13581.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13581v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13581v1', 'RAR: Setting Knowledge Tripwires for Retrieval Augmented Rejection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tommaso Mario Buonocore, Enea Parimbelli

**分类**: cs.IR, cs.CL, cs.CR

**发布日期**: 2025-05-19

**备注**: 7 pages, 4 figures, 2 tables

---

## 💡 一句话要点

**提出RAR方法以解决大语言模型内容审核问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内容审核` `大语言模型` `检索增强生成` `动态拒绝` `安全威胁`

## 📋 核心要点

1. 现有的大语言模型在内容审核方面面临灵活性不足和响应速度慢的问题，难以应对快速变化的安全威胁。
2. RAR方法通过利用检索增强生成架构，动态拒绝不安全的用户查询，避免了模型的重新训练，提高了系统的灵活性。
3. 初步实验结果显示，RAR在性能上与现有的嵌入式审核方法相当，同时在实时定制能力上具有显著优势。

## 📝 摘要（中文）

大语言模型（LLMs）的内容审核仍然是一个重大挑战，需要灵活且适应性强的解决方案，以快速应对新兴威胁。本文介绍了一种新颖的方法——检索增强拒绝（RAR），该方法利用检索增强生成（RAG）架构，动态拒绝不安全的用户查询，而无需对模型进行重新训练。通过将恶意文档战略性地插入并标记到向量数据库中，系统能够在检索到这些文档时识别并拒绝有害请求。初步结果表明，RAR在性能上与Claude 3.5 Sonnet等LLMs中的嵌入式审核相当，同时提供了更优的灵活性和实时定制能力，这是及时应对关键漏洞的基本特征。该方法对现有RAG系统没有架构上的改变，仅需添加特别制作的文档和基于检索结果的简单拒绝机制。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在内容审核中灵活性不足和响应速度慢的问题。现有方法通常需要对模型进行重新训练，无法快速适应新兴的安全威胁。

**核心思路**：RAR方法的核心思路是利用检索增强生成架构，通过动态拒绝不安全的用户查询，避免了模型的重新训练。通过将恶意文档插入向量数据库，系统能够在检索时识别并拒绝这些有害请求。

**技术框架**：RAR的整体架构包括一个检索模块和一个拒绝机制。检索模块负责从向量数据库中检索相关文档，而拒绝机制则根据检索结果决定是否拒绝用户的查询。

**关键创新**：RAR的主要创新在于其无需对现有RAG系统进行架构上的改变，仅需添加特别制作的文档和简单的拒绝机制。这种设计使得系统能够灵活应对新出现的威胁。

**关键设计**：在关键设计方面，RAR方法通过插入恶意文档并标记其特征，利用检索结果进行判断，确保系统能够实时拒绝不安全的请求。

## 📊 实验亮点

实验结果表明，RAR方法在性能上与Claude 3.5 Sonnet等嵌入式审核方法相当，同时在灵活性和实时定制能力上具有显著提升。这种方法能够快速适应新兴威胁，确保内容审核的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体平台、在线内容审核系统和任何需要实时内容监控的环境。RAR方法的灵活性和实时定制能力使其在应对不断变化的安全威胁时具有重要价值，未来可能会在更广泛的内容生成和审核场景中得到应用。

## 📄 摘要（原文）

> Content moderation for large language models (LLMs) remains a significant challenge, requiring flexible and adaptable solutions that can quickly respond to emerging threats. This paper introduces Retrieval Augmented Rejection (RAR), a novel approach that leverages a retrieval-augmented generation (RAG) architecture to dynamically reject unsafe user queries without model retraining. By strategically inserting and marking malicious documents into the vector database, the system can identify and reject harmful requests when these documents are retrieved. Our preliminary results show that RAR achieves comparable performance to embedded moderation in LLMs like Claude 3.5 Sonnet, while offering superior flexibility and real-time customization capabilities, a fundamental feature to timely address critical vulnerabilities. This approach introduces no architectural changes to existing RAG systems, requiring only the addition of specially crafted documents and a simple rejection mechanism based on retrieval results.

