---
layout: default
title: "A Few Words Can Distort Graphs: Knowledge Poisoning Attacks on Graph-based Retrieval-Augmented Generation of Large Language Models"
---

# A Few Words Can Distort Graphs: Knowledge Poisoning Attacks on Graph-based Retrieval-Augmented Generation of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04276" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04276v2</a>
  <a href="https://arxiv.org/pdf/2508.04276.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04276v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04276v2', 'A Few Words Can Distort Graphs: Knowledge Poisoning Attacks on Graph-based Retrieval-Augmented Generation of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayi Wen, Tianxin Chen, Zhirun Zheng, Cheng Huang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-06 (更新: 2025-08-12)

---

## 💡 一句话要点

**提出知识毒化攻击以解决GraphRAG模型的安全隐患问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识毒化` `图基检索` `大型语言模型` `安全性` `图论分析` `问答系统` `自然语言处理`

## 📋 核心要点

1. 现有的GraphRAG方法依赖于LLMs提取知识，存在被恶意操控的风险，可能导致误导性信息的植入。
2. 本文提出两种知识毒化攻击（TKPA和UKPA），通过修改少量文本实现对生成图的控制，影响问答结果。
3. 实验结果显示，TKPA的成功率达到93.1%，而UKPA在修改不到0.05%的文本后，问答准确率从95%降至50%。

## 📝 摘要（中文）

图基检索增强生成（GraphRAG）最近成为提升大型语言模型（LLMs）的有前景的范式，通过将原始文本转换为结构化知识图谱来提高准确性和可解释性。然而，GraphRAG依赖LLMs从原始文本中提取知识，这一过程可能被恶意操控以植入误导性信息。针对这一攻击面，本文提出了两种知识毒化攻击（KPA），并展示了仅修改少量词语即可显著改变构建的图谱，毒化GraphRAG并严重误导下游推理。第一种攻击称为目标KPA（TKPA），通过图论分析定位生成图中的脆弱节点，并使用LLMs重写相应叙述，成功率达到93.1%。第二种攻击称为通用KPA（UKPA），利用语言线索干扰生成图的结构完整性。实验表明，现有的防御方法未能检测到这些攻击，表明保护GraphRAG管道免受知识毒化的研究仍然相对较少。

## 🔬 方法详解

**问题定义**：本文旨在解决GraphRAG模型在知识提取过程中面临的安全隐患，现有方法易受知识毒化攻击，导致生成图谱的可靠性下降。

**核心思路**：提出两种知识毒化攻击（TKPA和UKPA），通过精确控制文本修改，影响下游问答系统的输出结果。TKPA通过图论分析定位脆弱节点，UKPA则利用语言线索干扰图的结构完整性。

**技术框架**：整体流程包括知识图谱的构建、攻击实施和效果评估。首先，利用LLMs生成知识图谱，然后通过TKPA或UKPA进行攻击，最后评估问答系统的准确性变化。

**关键创新**：TKPA和UKPA是针对GraphRAG模型的首个知识毒化攻击方法，能够在保持文本流畅性的同时，精确控制问答结果，且现有防御方法无法有效检测。

**关键设计**：TKPA通过图论分析选择脆弱节点，UKPA则通过修改具有全局影响的词语（如代词和依赖关系）来干扰图结构，确保攻击的隐蔽性和有效性。实验中，修改少于0.05%的文本即可显著降低问答准确率。

## 📊 实验亮点

实验结果显示，TKPA的成功率高达93.1%，而UKPA在修改不到0.05%的文本后，问答准确率从95%骤降至50%。此外，现有的防御方法未能有效检测到这些攻击，突显了GraphRAG模型的安全性问题。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性提升、知识图谱构建的可靠性保障以及信息检索系统的防护。通过理解和防范知识毒化攻击，可以增强AI系统的鲁棒性，确保其在实际应用中的可信度和安全性。

## 📄 摘要（原文）

> Graph-based Retrieval-Augmented Generation (GraphRAG) has recently emerged as a promising paradigm for enhancing large language models (LLMs) by converting raw text into structured knowledge graphs, improving both accuracy and explainability. However, GraphRAG relies on LLMs to extract knowledge from raw text during graph construction, and this process can be maliciously manipulated to implant misleading information. Targeting this attack surface, we propose two knowledge poisoning attacks (KPAs) and demonstrate that modifying only a few words in the source text can significantly change the constructed graph, poison the GraphRAG, and severely mislead downstream reasoning. The first attack, named Targeted KPA (TKPA), utilizes graph-theoretic analysis to locate vulnerable nodes in the generated graphs and rewrites the corresponding narratives with LLMs, achieving precise control over specific question-answering (QA) outcomes with a success rate of 93.1\%, while keeping the poisoned text fluent and natural. The second attack, named Universal KPA (UKPA), exploits linguistic cues such as pronouns and dependency relations to disrupt the structural integrity of the generated graph by altering globally influential words. With fewer than 0.05\% of full text modified, the QA accuracy collapses from 95\% to 50\%. Furthermore, experiments show that state-of-the-art defense methods fail to detect these attacks, highlighting that securing GraphRAG pipelines against knowledge poisoning remains largely unexplored.

