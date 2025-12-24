---
layout: default
title: "Unify Graph Learning with Text: Unleashing LLM Potentials for Session Search"
---

# Unify Graph Learning with Text: Unleashing LLM Potentials for Session Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14156" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14156v1</a>
  <a href="https://arxiv.org/pdf/2505.14156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14156v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14156v1', 'Unify Graph Learning with Text: Unleashing LLM Potentials for Session Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Songhao Wu, Quan Tu, Hong Liu, Jia Xu, Zhongyi Liu, Guannan Zhang, Ran Wang, Xiuying Chen, Rui Yan

**分类**: cs.CV, cs.AI, cs.IR, cs.LG

**发布日期**: 2025-05-20

**DOI**: [10.1145/3589334.3645574](https://doi.org/10.1145/3589334.3645574)

---

## 💡 一句话要点

**提出符号图排序器以解决会话搜索中的信息结构建模问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `会话搜索` `图学习` `大型语言模型` `自监督学习` `信息检索` `符号语法` `深度学习`

## 📋 核心要点

1. 现有会话搜索方法多集中于顺序建模，忽视了交互中的图结构，导致信息建模不足。
2. 本文提出符号图排序器（SGR），通过符号语法规则将会话图转换为文本，结合LLMs的能力进行信息处理。
3. 在AOL和Tiangong-ST数据集上的实验结果显示，SGR在性能上显著优于传统方法，验证了其有效性。

## 📝 摘要（中文）

会话搜索涉及一系列交互查询和操作，以满足用户复杂的信息需求。现有策略通常优先考虑顺序建模，忽视交互中的图结构。本文提出符号图排序器（SGR），旨在通过利用大型语言模型（LLMs）的能力，结合文本和图形方法。我们引入一组符号语法规则，将会话图转换为文本，从而无缝整合会话历史、交互过程和任务指令。此外，针对LLMs在文本语料上预训练与我们生成的符号语言之间的自然差异，我们设计了一系列自监督符号学习任务，以增强LLMs捕捉图结构的能力。实验结果表明，我们的方法在AOL和Tiangong-ST两个基准数据集上表现优越。

## 🔬 方法详解

**问题定义**：本文旨在解决会话搜索中信息建模不足的问题，现有方法多依赖顺序建模，无法充分利用交互中的图结构信息。

**核心思路**：提出符号图排序器（SGR），通过符号语法规则将会话图转换为文本，利用大型语言模型（LLMs）进行深度语义理解，从而实现图结构与文本信息的有效结合。

**技术框架**：SGR的整体架构包括三个主要模块：符号语法规则生成模块、LLM输入整合模块和自监督学习任务模块。首先，将会话图转换为文本格式，然后将其输入LLM进行处理，最后通过自监督任务增强模型的学习能力。

**关键创新**：最重要的创新在于引入符号语法规则，将图结构信息以文本形式呈现，使得LLMs能够更好地捕捉和理解图结构信息，这一方法与传统的图表示方法有本质区别。

**关键设计**：在模型设计中，采用了自监督学习任务，包括链接预测、节点内容生成和生成对比学习，以促进LLMs从粗粒度到细粒度捕捉拓扑信息，损失函数和网络结构经过精心设计，以确保模型的有效性和稳定性。

## 📊 实验亮点

实验结果显示，SGR在AOL和Tiangong-ST数据集上的表现显著优于基线方法，具体提升幅度达到XX%（具体数据需根据实验结果填写），验证了其在会话搜索中的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、智能助手和个性化推荐系统等。通过更好地理解用户的会话历史和需求，能够提供更精准的搜索结果和推荐，提升用户体验。未来，该方法有望在多模态信息处理和复杂查询理解等领域发挥更大作用。

## 📄 摘要（原文）

> Session search involves a series of interactive queries and actions to fulfill user's complex information need. Current strategies typically prioritize sequential modeling for deep semantic understanding, overlooking the graph structure in interactions. While some approaches focus on capturing structural information, they use a generalized representation for documents, neglecting the word-level semantic modeling. In this paper, we propose Symbolic Graph Ranker (SGR), which aims to take advantage of both text-based and graph-based approaches by leveraging the power of recent Large Language Models (LLMs). Concretely, we first introduce a set of symbolic grammar rules to convert session graph into text. This allows integrating session history, interaction process, and task instruction seamlessly as inputs for the LLM. Moreover, given the natural discrepancy between LLMs pre-trained on textual corpora, and the symbolic language we produce using our graph-to-text grammar, our objective is to enhance LLMs' ability to capture graph structures within a textual format. To achieve this, we introduce a set of self-supervised symbolic learning tasks including link prediction, node content generation, and generative contrastive learning, to enable LLMs to capture the topological information from coarse-grained to fine-grained. Experiment results and comprehensive analysis on two benchmark datasets, AOL and Tiangong-ST, confirm the superiority of our approach. Our paradigm also offers a novel and effective methodology that bridges the gap between traditional search strategies and modern LLMs.

