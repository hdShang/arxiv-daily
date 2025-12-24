---
layout: default
title: "Question-Driven Analysis and Synthesis: Building Interpretable Thematic Trees with LLMs for Text Clustering and Controllable Generation"
---

# Question-Driven Analysis and Synthesis: Building Interpretable Thematic Trees with LLMs for Text Clustering and Controllable Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22211" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22211v2</a>
  <a href="https://arxiv.org/pdf/2509.22211.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22211v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22211v2', 'Question-Driven Analysis and Synthesis: Building Interpretable Thematic Trees with LLMs for Text Clustering and Controllable Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tiago Fernandes Tavares

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出递归主题划分（RTP），利用LLM构建可解释主题树，实现文本聚类和可控生成。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本聚类` `主题模型` `大型语言模型` `可解释性` `自然语言生成` `知识驱动` `递归划分`

## 📋 核心要点

1. 传统主题模型在数据稀缺场景下表现不佳，且生成的关键词列表缺乏语义连贯性，难以解释。
2. RTP利用LLM构建二叉树，每个节点是一个自然语言问题，通过问答驱动的方式进行数据分割，形成可解释的层级结构。
3. 实验证明RTP比传统方法更具可解释性，且生成的聚类结果在下游分类任务中表现出强大的特征表达能力。

## 📝 摘要（中文）

本文提出了一种名为递归主题划分（RTP）的新框架，旨在解决文本语料库的无监督分析难题，尤其是在数据稀缺领域中传统主题模型表现不佳的问题。RTP利用大型语言模型（LLM）交互式地构建二叉树，树中的每个节点都是一个自然语言问题，用于语义分割数据，从而形成完全可解释的分类体系，其中每个集群的逻辑都是显式的。实验表明，RTP的问答驱动层次结构比BERTopic等基线模型的关键词主题更具可解释性。此外，通过证明这些集群可以作为下游分类任务中的强大特征（尤其是在数据的基础主题与任务标签相关时），验证了这些集群的量化效用。RTP引入了一种新的数据探索范例，将重点从统计模式发现转移到知识驱动的主题分析。此外，RTP树中的主题路径可以作为生成模型的结构化、可控提示，将分析框架转变为强大的合成工具，从而能够一致地模仿源语料库中发现的特定特征。

## 🔬 方法详解

**问题定义**：论文旨在解决文本语料库无监督分析中，传统主题模型在数据稀缺场景下表现不佳，且输出的关键词列表缺乏语义连贯性，难以解释的问题。现有方法依赖统计模式发现，缺乏知识驱动的主题分析。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）的语义理解和生成能力，通过递归地提出自然语言问题来划分文本数据，构建一个可解释的二叉树结构。每个节点的问题明确地定义了其子树包含的主题，从而实现了知识驱动的主题分析。

**技术框架**：RTP框架主要包含以下步骤：1) 选择一个根节点，包含整个数据集。2) 使用LLM生成一个自然语言问题，该问题能够将数据集划分为两个语义上不同的子集。3) 根据问题答案将数据划分到左右子节点。4) 对每个子节点递归地执行步骤2和3，直到满足停止条件（例如，节点包含的数据量小于阈值）。最终形成一棵二叉树，每个节点都对应一个自然语言问题和一组文本数据。

**关键创新**：RTP最重要的创新点在于其问答驱动的层次结构构建方式。与传统的基于统计模式发现的主题模型不同，RTP利用LLM的语义理解能力，通过自然语言问题来明确地定义每个集群的主题，从而显著提高了模型的可解释性。此外，RTP还能够将主题路径作为生成模型的结构化提示，实现可控的文本生成。

**关键设计**：RTP的关键设计包括：1) LLM的选择：论文使用了具有强大语义理解和生成能力的LLM。2) 问题生成策略：论文设计了特定的提示工程（prompt engineering）方法，引导LLM生成能够有效划分数据的自然语言问题。3) 停止条件：论文设置了节点包含数据量的阈值作为停止条件，防止树的过度生长。4) 数据划分策略：根据LLM对问题的回答，将文本数据划分到相应的子节点。

## 📊 实验亮点

实验结果表明，RTP生成的问答驱动层次结构比BERTopic等基线模型更具可解释性。此外，RTP生成的聚类结果在下游分类任务中表现出强大的特征表达能力，尤其是在数据的基础主题与任务标签相关时，性能提升显著。RTP还展示了其作为可控文本生成工具的潜力。

## 🎯 应用场景

RTP可应用于各种文本数据分析场景，例如社交媒体舆情分析、客户反馈分析、科学文献分类等。其可解释性强的特点使其在需要人工干预和理解的领域具有重要价值。此外，RTP还可作为可控文本生成的基础，用于生成具有特定主题和风格的文本内容，例如新闻报道、产品描述等。

## 📄 摘要（原文）

> Unsupervised analysis of text corpora is challenging, especially in data-scarce domains where traditional topic models struggle. While these models offer a solution, they typically describe clusters with lists of keywords that require significant manual effort to interpret and often lack semantic coherence. To address this critical interpretability gap, we introduce Recursive Thematic Partitioning (RTP), a novel framework that leverages Large Language Models (LLMs) to interactively build a binary tree. Each node in the tree is a natural language question that semantically partitions the data, resulting in a fully interpretable taxonomy where the logic of each cluster is explicit. Our experiments demonstrate that RTP's question-driven hierarchy is more interpretable than the keyword-based topics from a strong baseline like BERTopic. Furthermore, we establish the quantitative utility of these clusters by showing they serve as powerful features in downstream classification tasks, particularly when the data's underlying themes correlate with the task labels. RTP introduces a new paradigm for data exploration, shifting the focus from statistical pattern discovery to knowledge-driven thematic analysis. Furthermore, we demonstrate that the thematic paths from the RTP tree can serve as structured, controllable prompts for generative models. This transforms our analytical framework into a powerful tool for synthesis, enabling the consistent imitation of specific characteristics discovered in the source corpus.

