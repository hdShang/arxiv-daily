---
layout: default
title: "Joint-GCG: Unified Gradient-Based Poisoning Attacks on Retrieval-Augmented Generation Systems"
---

# Joint-GCG: Unified Gradient-Based Poisoning Attacks on Retrieval-Augmented Generation Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06151" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06151v2</a>
  <a href="https://arxiv.org/pdf/2506.06151.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06151v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06151v2', 'Joint-GCG: Unified Gradient-Based Poisoning Attacks on Retrieval-Augmented Generation Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haowei Wang, Rupeng Zhang, Junjie Wang, Mingyang Li, Yuekai Huang, Dandan Wang, Qing Wang

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-11-12)

**🔗 代码/项目**: [GITHUB](https://github.com/NicerWang/Joint-GCG)

---

## 💡 一句话要点

**提出Joint-GCG以解决RAG系统的毒化攻击问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `毒化攻击` `检索增强生成` `梯度攻击` `模型安全` `自然语言处理`

## 📋 核心要点

1. 现有的毒化攻击方法将检索和生成阶段视为独立，导致攻击效果受限。
2. Joint-GCG通过跨词汇投影、梯度标记对齐和自适应加权融合，统一了检索和生成的攻击策略。
3. 实验结果显示，Joint-GCG在多个模型上攻击成功率显著提高，展现出良好的迁移性。

## 📝 摘要（中文）

检索增强生成（RAG）系统通过从外部语料库检索相关文档来增强大型语言模型（LLM）的能力。然而，这种对外部知识的依赖使得RAG系统易受毒化攻击，攻击者可以通过注入被污染的文档来操控生成的输出。现有的毒化攻击策略通常将检索和生成阶段视为分离的，限制了其有效性。我们提出了Joint-GCG，这是第一个统一检索器和生成器模型的基于梯度的攻击框架，包含三项创新：跨词汇投影、梯度标记对齐和自适应加权融合。评估结果表明，Joint-GCG在多个检索器和生成器上，攻击成功率最高可提高25%，平均提升5%。

## 🔬 方法详解

**问题定义**：本论文旨在解决检索增强生成（RAG）系统在面对毒化攻击时的脆弱性。现有方法通常将检索和生成过程分开，导致攻击效果不佳。

**核心思路**：我们提出Joint-GCG框架，通过统一检索器和生成器的攻击策略，增强毒化攻击的有效性。该设计旨在通过协同优化两个阶段的攻击目标，提升整体攻击成功率。

**技术框架**：Joint-GCG框架包括三个主要模块：跨词汇投影用于对齐嵌入空间，梯度标记对齐用于同步标记级别的梯度信号，自适应加权融合用于动态平衡攻击目标。

**关键创新**：本研究的核心创新在于首次将基于梯度的攻击统一应用于检索和生成阶段，改变了我们对RAG系统脆弱性的理解。与现有方法相比，Joint-GCG在攻击策略上实现了更高的协同效应。

**关键设计**：在设计中，我们采用了特定的损失函数来优化攻击效果，并通过动态调整权重来平衡不同攻击目标的影响。此外，模型结构经过精心设计，以确保在不同环境下的有效性和迁移性。

## 📊 实验亮点

实验结果表明，Joint-GCG在多个检索器和生成器上，攻击成功率最高可提高25%，平均提升5%。此外，生成的毒化样本在未见模型上展现出前所未有的迁移性，显示出该方法的广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、自然语言处理和安全防护等。通过增强对RAG系统的攻击理解，可以为构建更安全的生成模型提供理论基础和实践指导，未来可能影响相关领域的安全策略和模型设计。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) systems enhance Large Language Models (LLMs) by retrieving relevant documents from external corpora before generating responses. This approach significantly expands LLM capabilities by leveraging vast, up-to-date external knowledge. However, this reliance on external knowledge makes RAG systems vulnerable to corpus poisoning attacks that manipulate generated outputs via poisoned document injection. Existing poisoning attack strategies typically treat the retrieval and generation stages as disjointed, limiting their effectiveness. We propose Joint-GCG, the first framework to unify gradient-based attacks across both retriever and generator models through three innovations: (1) Cross-Vocabulary Projection for aligning embedding spaces, (2) Gradient Tokenization Alignment for synchronizing token-level gradient signals, and (3) Adaptive Weighted Fusion for dynamically balancing attacking objectives. Evaluations demonstrate that Joint-GCG achieves at most 25% and an average of 5% higher attack success rate than previous methods across multiple retrievers and generators. While optimized under a white-box assumption, the generated poisons show unprecedented transferability to unseen models. Joint-GCG's innovative unification of gradient-based attacks across retrieval and generation stages fundamentally reshapes our understanding of vulnerabilities within RAG systems. Our code is available at https://github.com/NicerWang/Joint-GCG.

