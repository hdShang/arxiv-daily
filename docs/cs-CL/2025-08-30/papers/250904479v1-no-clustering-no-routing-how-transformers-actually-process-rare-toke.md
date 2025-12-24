---
layout: default
title: "No Clustering, No Routing: How Transformers Actually Process Rare Tokens"
---

# No Clustering, No Routing: How Transformers Actually Process Rare Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04479" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04479v1</a>
  <a href="https://arxiv.org/pdf/2509.04479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04479v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04479v1', 'No Clustering, No Routing: How Transformers Actually Process Rare Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jing Liu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-30

---

## 💡 一句话要点

**揭示Transformer如何处理稀有词汇以提升预测能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀有词汇处理` `Transformer` `神经元影响分析` `注意力机制` `大型语言模型`

## 📋 核心要点

1. 核心问题：现有大型语言模型在稀有词汇预测方面表现不佳，专门化机制尚不清晰。
2. 方法要点：通过神经元影响分析和消融实验，探讨稀有词汇处理的神经元组织与注意力机制。
3. 实验或效果：发现稀有词汇处理需要额外的神经元，并且这些神经元是空间分布的，未形成模块化结构。

## 📝 摘要（中文）

大型语言模型在稀有词汇预测方面面临挑战，但其专门化机制尚不明确。先前研究发现稀有词汇的“平台”神经元具有独特的三阶段影响模式，但其功能组织尚不清楚。本文通过神经元影响分析、基于图的聚类和注意力头消融研究了GPT-2 XL和Pythia模型。研究结果表明，稀有词汇处理需要额外的“平台”神经元，形成双重计算机制；这些神经元是空间分布的，而非模块化聚类；注意力机制没有优先路由到专家神经元。这些结果表明，稀有词汇的专门化是通过分布式、训练驱动的差异化实现的，而非架构模块化，保持了上下文敏感的灵活性，同时实现了自适应能力分配。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在稀有词汇预测中的不足，尤其是稀有词汇的专门化机制尚不明确，导致模型性能受限。

**核心思路**：通过分析神经元的影响力和注意力机制，探讨稀有词汇处理所需的额外神经元及其组织形式，提出稀有词汇处理的双重计算机制。

**技术框架**：研究采用神经元影响分析、图形聚类和注意力头消融实验，重点分析GPT-2 XL和Pythia模型的神经元分布和功能。

**关键创新**：提出稀有词汇处理需要额外的“平台”神经元，形成双重计算机制，且这些神经元是空间分布的，而非传统的模块化聚类。

**关键设计**：在实验中，使用了不同的神经元影响力分析方法，设计了消融实验以验证注意力机制的路由特性，确保了结果的可靠性和有效性。

## 📊 实验亮点

实验结果显示，稀有词汇处理需要额外的“平台”神经元，且这些神经元在空间上分布而非聚集，注意力机制未对专家神经元进行优先路由。这一发现为理解语言模型的内部机制提供了新的证据。

## 🎯 应用场景

该研究为大型语言模型在稀有词汇处理中的应用提供了新的视角，可能对自然语言处理、机器翻译和对话系统等领域产生深远影响。通过理解稀有词汇的处理机制，可以进一步优化模型设计，提高其在复杂语言任务中的表现。

## 📄 摘要（原文）

> Large language models struggle with rare token prediction, yet the mechanisms driving their specialization remain unclear. Prior work identified specialized ``plateau'' neurons for rare tokens following distinctive three-regime influence patterns \cite{liu2025emergent}, but their functional organization is unknown. We investigate this through neuron influence analyses, graph-based clustering, and attention head ablations in GPT-2 XL and Pythia models. Our findings show that: (1) rare token processing requires additional plateau neurons beyond the power-law regime sufficient for common tokens, forming dual computational regimes; (2) plateau neurons are spatially distributed rather than forming modular clusters; and (3) attention mechanisms exhibit no preferential routing to specialists. These results demonstrate that rare token specialization arises through distributed, training-driven differentiation rather than architectural modularity, preserving context-sensitive flexibility while achieving adaptive capacity allocation.

