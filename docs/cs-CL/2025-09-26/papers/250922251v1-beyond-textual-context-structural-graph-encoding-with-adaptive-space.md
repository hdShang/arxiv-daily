---
layout: default
title: "Beyond Textual Context: Structural Graph Encoding with Adaptive Space Alignment to alleviate the hallucination of LLMs"
---

# Beyond Textual Context: Structural Graph Encoding with Adaptive Space Alignment to alleviate the hallucination of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22251" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22251v1</a>
  <a href="https://arxiv.org/pdf/2509.22251.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22251v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22251v1', 'Beyond Textual Context: Structural Graph Encoding with Adaptive Space Alignment to alleviate the hallucination of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifang Zhang, Pengfei Duan, Yiwen Yang, Shengwu Xiong

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

**备注**: 11 pages, 5 figures

**🔗 代码/项目**: [GITHUB](https://github.com/yfangZhang/SSKG-LLM)

---

## 💡 一句话要点

**提出SSKG-LLM，通过结构化图编码和自适应空间对齐缓解LLM幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识图谱` `幻觉问题` `结构化编码` `空间对齐`

## 📋 核心要点

1. 现有LLM解决幻觉问题时，对知识图谱的处理方式过于简单，未能充分利用其结构信息。
2. SSKG-LLM模型通过知识图谱检索、编码和适配模块，将知识图谱的结构和语义信息有效融入LLM推理。
3. 实验结果表明，结合知识图谱结构信息能够显著提升LLM的事实推理能力，有效缓解幻觉问题。

## 📝 摘要（中文）

目前，解决大型语言模型（LLM）幻觉问题的主要方法是融入知识图谱（KG）。然而，LLM通常将KG视为纯文本，仅提取语义信息，限制了KG关键结构化方面的利用。另一个挑战是KG编码器和LLM文本嵌入之间的嵌入空间存在差距，阻碍了结构化知识的有效整合。为了克服这些障碍，我们提出了SSKG-LLM，一种创新的模型架构，旨在有效地将KG的结构和语义信息整合到LLM的推理过程中。SSKG-LLM包含知识图谱检索（KGR）模块和知识图谱编码（KGE）模块，以保留语义并利用结构。然后，加入知识图谱适配（KGA）模块，使LLM能够理解KG嵌入。我们进行了广泛的实验，并提供了详细的分析，以探索结合KG的结构信息如何增强LLM的事实推理能力。我们的代码可在https://github.com/yfangZhang/SSKG-LLM 获取。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在处理知识图谱（KG）时，通常将其视为纯文本，仅关注语义信息，而忽略了KG中蕴含的丰富结构信息。此外，KG编码器和LLM文本嵌入之间的空间差异，使得结构化知识难以有效整合，导致LLM在生成文本时容易出现幻觉问题。

**核心思路**：SSKG-LLM的核心思路是同时利用KG的语义和结构信息，并通过自适应空间对齐，弥合KG嵌入和LLM文本嵌入之间的差距。通过这种方式，模型能够更全面地理解和利用KG中的知识，从而减少幻觉的产生。

**技术框架**：SSKG-LLM包含三个主要模块：知识图谱检索（KGR）模块、知识图谱编码（KGE）模块和知识图谱适配（KGA）模块。首先，KGR模块负责从KG中检索相关知识。然后，KGE模块对检索到的KG进行编码，同时保留语义和结构信息。最后，KGA模块将KG嵌入空间与LLM文本嵌入空间对齐，使LLM能够更好地理解和利用KG知识。

**关键创新**：SSKG-LLM的关键创新在于其能够同时利用KG的结构和语义信息，并采用自适应空间对齐方法。与现有方法相比，SSKG-LLM不仅关注KG的语义信息，还充分利用了其结构信息，从而更全面地理解和利用KG中的知识。此外，自适应空间对齐方法能够有效弥合KG嵌入和LLM文本嵌入之间的差距，使得LLM能够更好地利用KG知识。

**关键设计**：KGR模块的具体实现方式未知，KGE模块可能采用图神经网络等方法对KG进行编码，KGA模块可能采用对抗训练或映射函数等方法进行空间对齐。具体的损失函数和网络结构等技术细节在论文中未详细说明。

## 📊 实验亮点

论文通过实验验证了SSKG-LLM的有效性，表明结合知识图谱结构信息能够显著提升LLM的事实推理能力。具体的性能数据、对比基线和提升幅度在摘要中未提及，需查阅论文全文获取详细信息。

## 🎯 应用场景

该研究成果可应用于问答系统、知识图谱补全、文本生成等领域。通过提升LLM的事实推理能力，可以有效减少生成文本中的错误信息，提高系统的可靠性和准确性。未来，该方法有望在医疗、金融等对信息准确性要求较高的领域发挥重要作用。

## 📄 摘要（原文）

> Currently, the main approach for Large Language Models (LLMs) to tackle the hallucination issue is incorporating Knowledge Graphs(KGs).However, LLMs typically treat KGs as plain text, extracting only semantic information and limiting their use of the crucial structural aspects of KGs. Another challenge is the gap between the embedding spaces of KGs encoders and LLMs text embeddings, which hinders the effective integration of structured knowledge. To overcome these obstacles, we put forward the SSKG-LLM, an innovative model architecture that is designed to efficiently integrate both the Structural and Semantic information of KGs into the reasoning processes of LLMs. SSKG-LLM incorporates the Knowledge Graph Retrieval (KGR) module and the Knowledge Graph Encoding (KGE) module to preserve semantics while utilizing structure. Then, the Knowledge Graph Adaptation (KGA) module is incorporated to enable LLMs to understand KGs embeddings. We conduct extensive experiments and provide a detailed analysis to explore how incorporating the structural information of KGs can enhance the factual reasoning abilities of LLMs. Our code are available at https://github.com/yfangZhang/SSKG-LLM.

