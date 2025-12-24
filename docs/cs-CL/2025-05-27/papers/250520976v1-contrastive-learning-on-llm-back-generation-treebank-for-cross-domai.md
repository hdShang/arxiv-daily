---
layout: default
title: Contrastive Learning on LLM Back Generation Treebank for Cross-domain Constituency Parsing
---

# Contrastive Learning on LLM Back Generation Treebank for Cross-domain Constituency Parsing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20976" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20976v1</a>
  <a href="https://arxiv.org/pdf/2505.20976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20976v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20976v1', 'Contrastive Learning on LLM Back Generation Treebank for Cross-domain Constituency Parsing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peiming Guo, Meishan Zhang, Jianling Li, Min Zhang, Yue Zhang

**分类**: cs.CL

**发布日期**: 2025-05-27

**备注**: Accepted by ACL 2025 main conference

---

## 💡 一句话要点

**提出LLM反向生成方法以解决跨领域句法分析问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨领域句法分析` `大型语言模型` `自动树库生成` `对比学习` `自然语言处理` `句法树` `机器学习`

## 📋 核心要点

1. 跨领域句法分析面临的主要挑战是缺乏足够的多领域句法树库，现有方法在此方面的表现不佳。
2. 本文提出的LLM反向生成方法通过填充缺失单词生成跨领域句法树库，结合对比学习预训练策略提升分析效果。
3. 实验结果显示，所提方法在五个目标领域上实现了最先进的性能，相较于多种基线有显著提升。

## 📝 摘要（中文）

跨领域句法分析在计算语言学中仍然是一个未解决的挑战，因为可用的多领域句法树库有限。本文研究了通过大型语言模型（LLMs）进行自动树库生成。由于LLMs在句法分析中的表现较差，我们提出了一种新颖的树库生成方法——LLM反向生成，该方法类似于句法分析的逆过程。LLM反向生成以仅包含领域关键词叶节点的不完整跨领域句法树为输入，填充缺失的单词以生成跨领域句法树库。此外，我们还引入了一种基于跨度的对比学习预训练策略，以充分利用LLM反向生成树库进行跨领域句法分析。实验结果表明，与各种基线相比，我们的方法在五个目标领域的平均结果上达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决跨领域句法分析中由于缺乏足够的多领域句法树库而导致的性能不足问题。现有方法在处理不同领域的句法结构时表现不佳，限制了其应用范围。

**核心思路**：论文提出的LLM反向生成方法通过将不完整的跨领域句法树作为输入，填充缺失的单词，从而生成完整的句法树库。这种方法模拟了句法分析的逆过程，旨在提高LLMs在句法分析中的表现。

**技术框架**：整体架构包括两个主要模块：首先是LLM反向生成模块，该模块接收不完整的句法树并生成完整的树库；其次是对比学习预训练模块，通过对比学习策略进一步优化模型在句法分析任务中的表现。

**关键创新**：最重要的技术创新在于提出了LLM反向生成方法，这一方法通过逆向填充的方式生成句法树库，与传统的句法分析方法有本质区别，能够有效提升跨领域分析的准确性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化生成的句法树的质量，并通过对比学习策略增强模型对不同领域句法结构的适应能力。

## 📊 实验亮点

实验结果表明，所提出的LLM反向生成方法结合对比学习预训练，在五个目标领域上实现了最先进的性能，平均提升幅度超过了现有多种基线，显示出显著的效果改进。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的句法分析、机器翻译和信息提取等。通过提升跨领域句法分析的准确性，能够为多领域的语言理解和生成任务提供更强的支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Cross-domain constituency parsing is still an unsolved challenge in computational linguistics since the available multi-domain constituency treebank is limited. We investigate automatic treebank generation by large language models (LLMs) in this paper. The performance of LLMs on constituency parsing is poor, therefore we propose a novel treebank generation method, LLM back generation, which is similar to the reverse process of constituency parsing. LLM back generation takes the incomplete cross-domain constituency tree with only domain keyword leaf nodes as input and fills the missing words to generate the cross-domain constituency treebank. Besides, we also introduce a span-level contrastive learning pre-training strategy to make full use of the LLM back generation treebank for cross-domain constituency parsing. We verify the effectiveness of our LLM back generation treebank coupled with contrastive learning pre-training on five target domains of MCTB. Experimental results show that our approach achieves state-of-the-art performance on average results compared with various baselines.

