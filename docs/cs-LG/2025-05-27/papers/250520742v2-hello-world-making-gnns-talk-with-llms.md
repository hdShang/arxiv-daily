---
layout: default
title: "'Hello, World!': Making GNNs Talk with LLMs"
---

# 'Hello, World!': Making GNNs Talk with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20742" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20742v2</a>
  <a href="https://arxiv.org/pdf/2505.20742.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20742v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20742v2', '\'Hello, World!\': Making GNNs Talk with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sunwoo Kim, Soo Yong Lee, Jaemin Yoo, Kijung Shin

**分类**: cs.LG

**发布日期**: 2025-05-27 (更新: 2025-09-15)

**备注**: Published as a conference paper at EMNLP 2025 Findings. Code and datasets are in https://github.com/kswoo97/GLN-Code

---

## 💡 一句话要点

**提出图语言网络以提升图神经网络的可解释性与性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图神经网络` `可解释性` `大型语言模型` `节点分类` `链接预测` `图注意力机制` `残差连接`

## 📋 核心要点

1. 现有的图神经网络由于其高维隐藏表示，导致其内部机制难以理解，成为黑箱。
2. 本文提出的图语言网络（GLN）通过将隐藏表示转化为人类可读文本，提升了可解释性，并结合了多种GNN技术。
3. GLN在节点分类和链接预测任务中展现出强大的零-shot性能，超越了现有的基线方法，显示出显著的提升。

## 📝 摘要（中文）

尽管图神经网络（GNNs）在多种图相关任务中表现出色，但其高维隐藏表示使其成为黑箱。本文提出了图语言网络（GLN），该网络基于大型语言模型（LLMs），其隐藏表示以人类可读文本的形式呈现。通过精心设计的提示，GLN不仅结合了GNN的消息传递模块，还融入了图注意力和初始残差连接等先进技术。GLN的隐藏表示的可理解性使得对节点表示在不同层次和先进GNN技术下的变化进行直观分析成为可能，揭示了GNN的内部工作原理。此外，我们展示了GLN在节点分类和链接预测上的强大零-shot性能，超越了现有基于LLM的基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决图神经网络（GNNs）在高维隐藏表示下的可解释性问题，现有方法往往难以揭示其内部工作机制。

**核心思路**：提出图语言网络（GLN），通过将隐藏表示转化为人类可读文本，结合GNN的消息传递模块及先进技术，提升可解释性和性能。

**技术框架**：GLN的整体架构包括消息传递模块、图注意力机制和初始残差连接，采用精心设计的提示来生成可读文本表示。

**关键创新**：GLN的核心创新在于将GNN的隐藏表示转化为文本形式，使得节点表示的变化更加直观，显著提升了可解释性。

**关键设计**：在设计中，GLN采用了特定的提示策略以优化文本生成，同时结合了图注意力机制和残差连接，确保信息的有效传递与保留。

## 📊 实验亮点

实验结果表明，GLN在节点分类和链接预测任务中实现了强大的零-shot性能，超越了现有基于大型语言模型的基线方法，具体性能提升幅度达到XX%（具体数据待补充）。

## 🎯 应用场景

该研究在图数据分析、社交网络分析、推荐系统等领域具有广泛的应用潜力。通过提升图神经网络的可解释性，GLN能够帮助研究人员和工程师更好地理解和优化图模型，推动相关领域的发展。

## 📄 摘要（原文）

> While graph neural networks (GNNs) have shown remarkable performance across diverse graph-related tasks, their high-dimensional hidden representations render them black boxes. In this work, we propose Graph Lingual Network (GLN), a GNN built on large language models (LLMs), with hidden representations in the form of human-readable text. Through careful prompt design, GLN incorporates not only the message passing module of GNNs but also advanced GNN techniques, including graph attention and initial residual connection. The comprehensibility of GLN's hidden representations enables an intuitive analysis of how node representations change (1) across layers and (2) under advanced GNN techniques, shedding light on the inner workings of GNNs. Furthermore, we demonstrate that GLN achieves strong zero-shot performance on node classification and link prediction, outperforming existing LLM-based baseline methods.

