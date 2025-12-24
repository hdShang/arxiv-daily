---
layout: default
title: Hyperbolic Contrastive Learning with Model-augmentation for Knowledge-aware Recommendation
---

# Hyperbolic Contrastive Learning with Model-augmentation for Knowledge-aware Recommendation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08157" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08157v1</a>
  <a href="https://arxiv.org/pdf/2505.08157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08157v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08157v1', 'Hyperbolic Contrastive Learning with Model-augmentation for Knowledge-aware Recommendation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengyin Sun, Chen Ma

**分类**: cs.IR, cs.AI

**发布日期**: 2025-05-13

**备注**: 18 pages

---

## 💡 一句话要点

**提出超曲率对比学习与模型增强以解决知识感知推荐问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `知识感知推荐` `图神经网络` `对比学习` `超曲率学习` `模型增强` `用户偏好` `层次结构` `洛伦兹聚合`

## 📋 核心要点

1. 现有对比学习方法难以有效捕捉用户-物品二分图和知识图的层次结构，导致推荐效果不佳。
2. 本文提出超曲率对比学习与模型增强，设计了洛伦兹知识聚合机制以提升用户和物品的表示能力。
3. 实验结果显示，所提方法在推荐性能上优于现有基线，最大提升达到11.03%。

## 📝 摘要（中文）

基于图神经网络（GNN）和对比学习的知识感知推荐方法已成为主流。然而，现有方法在捕捉用户-物品二分图和知识图中的层次结构方面存在困难。此外，常通过扰动图结构生成正样本，可能导致用户偏好学习的偏移。为了解决这些问题，本文提出了超曲率对比学习与模型增强的方法。首先，设计了一种新颖的洛伦兹知识聚合机制，以更有效地表示用户和物品。然后，提出了三种模型级增强技术，避免了增强正样本对之间的偏好偏移。最后，通过大量实验验证了所提方法相较于现有基线的优越性，最大提升达到11.03%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有知识感知推荐方法在捕捉用户-物品二分图和知识图层次结构方面的不足，尤其是通过扰动图结构生成正样本所导致的用户偏好学习偏移问题。

**核心思路**：提出超曲率对比学习与模型增强，利用洛伦兹知识聚合机制来更有效地表示用户和物品，同时通过模型级增强技术避免增强正样本对之间的偏好偏移。

**技术框架**：整体架构包括三个主要模块：首先是洛伦兹知识聚合机制，用于生成用户和物品的有效表示；其次是三种模型级增强技术，增强对比学习过程；最后是对比学习的损失计算和优化过程。

**关键创新**：最重要的技术创新在于引入了洛伦兹知识聚合机制和模型级增强技术，这与传统的结构级增强方法（如边缘丢弃）本质上不同，能够更好地保持用户偏好。

**关键设计**：在参数设置上，采用了适应性学习率和正则化技术；损失函数设计为对比损失，确保正样本对的相似性；网络结构上，结合了GNN和超曲率空间的特性，以增强表示能力。

## 📊 实验亮点

实验结果表明，所提方法在多个数据集上均优于现有基线，最大提升达到11.03%。这一显著的性能提升验证了超曲率对比学习与模型增强的有效性，展示了其在知识感知推荐中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括个性化推荐系统、社交网络分析和知识图谱构建等。通过提升推荐系统的准确性和用户满意度，能够为商业平台提供更优质的用户体验，未来可能在电商、内容推荐等多个领域产生深远影响。

## 📄 摘要（原文）

> Benefiting from the effectiveness of graph neural networks (GNNs) and contrastive learning, GNN-based contrastive learning has become mainstream for knowledge-aware recommendation. However, most existing contrastive learning-based methods have difficulties in effectively capturing the underlying hierarchical structure within user-item bipartite graphs and knowledge graphs. Moreover, they commonly generate positive samples for contrastive learning by perturbing the graph structure, which may lead to a shift in user preference learning. To overcome these limitations, we propose hyperbolic contrastive learning with model-augmentation for knowledge-aware recommendation. To capture the intrinsic hierarchical graph structures, we first design a novel Lorentzian knowledge aggregation mechanism, which enables more effective representations of users and items. Then, we propose three model-level augmentation techniques to assist Hyperbolic contrastive learning. Different from the classical structure-level augmentation (e.g., edge dropping), the proposed model-augmentations can avoid preference shifts between the augmented positive pair. Finally, we conduct extensive experiments to demonstrate the superiority (maximum improvement of $11.03\%$) of proposed methods over existing baselines.

