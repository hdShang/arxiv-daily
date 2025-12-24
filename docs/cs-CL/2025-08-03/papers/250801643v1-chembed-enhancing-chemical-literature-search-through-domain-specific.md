---
layout: default
title: "ChEmbed: Enhancing Chemical Literature Search Through Domain-Specific Text Embeddings"
---

# ChEmbed: Enhancing Chemical Literature Search Through Domain-Specific Text Embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01643" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01643v1</a>
  <a href="https://arxiv.org/pdf/2508.01643.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01643v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01643v1', 'ChEmbed: Enhancing Chemical Literature Search Through Domain-Specific Text Embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Shiraee Kasmaee, Mohammad Khodadad, Mehdi Astaraki, Mohammad Arshi Saloot, Nicholas Sherck, Hamidreza Mahyar, Soheila Samiee

**分类**: cs.IR, cs.CL

**发布日期**: 2025-08-03

---

## 💡 一句话要点

**提出ChEmbed以解决化学文献检索中的嵌入表示不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `化学文献检索` `文本嵌入` `领域适应` `大型语言模型` `信息检索`

## 📋 核心要点

1. 现有的通用文本嵌入模型在处理复杂化学术语时表现不佳，导致化学文献检索的准确性和相关性不足。
2. ChEmbed通过在特定的化学文本数据集上微调，生成了针对化学文献检索的领域适应嵌入模型，显著提升了检索效果。
3. 在ChemRxiv检索基准测试中，ChEmbed的nDCG@10从0.82提升至0.91，显示出其在文献检索中的优越性能。

## 📝 摘要（中文）

化学领域的检索增强生成（RAG）系统在文献检索中依赖于准确相关的化学文献检索。然而，通用文本嵌入模型常常无法充分表示复杂的化学术语，导致检索质量不佳。为此，本文提出ChEmbed，一种针对化学文献检索的领域适应文本嵌入模型，经过在PubChem、Semantic Scholar和ChemRxiv数据集上微调。我们利用大型语言模型合成生成查询，创建了约170万对高质量的查询-段落对，并通过增加900个化学专用标记来增强分词器，显著减少化学实体的碎片化。ChEmbed保持8192个标记的上下文长度，能够高效检索较长段落。经过评估，ChEmbed在ChemRxiv检索基准上超越了最先进的通用嵌入模型，将nDCG@10从0.82提升至0.91，展示了其在化学文献检索中的实用性和有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决通用文本嵌入模型在化学文献检索中无法有效表示复杂化学术语的问题，导致检索质量不理想。

**核心思路**：提出ChEmbed模型，通过在化学特定文本上进行微调，生成更适合化学文献检索的嵌入表示，以提高检索的准确性和相关性。

**技术框架**：整体架构包括数据准备、模型训练和评估三个主要阶段。数据准备阶段利用大型语言模型合成查询，生成高质量的查询-段落对；模型训练阶段在特定数据集上微调嵌入模型；评估阶段使用ChemRxiv检索基准进行性能测试。

**关键创新**：ChEmbed的主要创新在于其领域适应性，特别是通过增加化学专用标记和保持较长的上下文长度（8192个标记），显著减少了化学实体的碎片化，提升了检索效果。

**关键设计**：在模型设计中，增加了900个化学专用标记，优化了分词器的使用，并采用了适合化学文献的损失函数和网络结构，以确保模型的高效性和准确性。

## 📊 实验亮点

ChEmbed在ChemRxiv检索基准测试中表现优异，nDCG@10从0.82提升至0.91，提升幅度达到9个百分点，超越了现有的最先进通用嵌入模型，展现了其在化学文献检索中的显著优势。

## 🎯 应用场景

ChEmbed模型在化学文献检索中具有广泛的应用潜力，能够帮助研究人员更高效地获取相关文献，提高研究效率。未来，该模型的设计理念和技术框架也可扩展到其他专业领域的文献检索中，推动相关领域的研究进展。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems in chemistry heavily depend on accurate and relevant retrieval of chemical literature. However, general-purpose text embedding models frequently fail to adequately represent complex chemical terminologies, resulting in suboptimal retrieval quality. Specialized embedding models tailored to chemical literature retrieval have not yet been developed, leaving a substantial performance gap. To address this challenge, we introduce ChEmbed, a domain-adapted family of text embedding models fine-tuned on a dataset comprising chemistry-specific text from the PubChem, Semantic Scholar, and ChemRxiv corpora. To create effective training data, we employ large language models to synthetically generate queries, resulting in approximately 1.7 million high-quality query-passage pairs. Additionally, we augment the tokenizer by adding 900 chemically specialized tokens to previously unused slots, which significantly reduces the fragmentation of chemical entities, such as IUPAC names. ChEmbed also maintains a 8192-token context length, enabling the efficient retrieval of longer passages compared to many other open-source embedding models, which typically have a context length of 512 or 2048 tokens. Evaluated on our newly introduced ChemRxiv Retrieval benchmark, ChEmbed outperforms state-of-the-art general embedding models, raising nDCG@10 from 0.82 to 0.91 (+9 pp). ChEmbed represents a practical, lightweight, and reproducible embedding solution that effectively improves retrieval for chemical literature search.

