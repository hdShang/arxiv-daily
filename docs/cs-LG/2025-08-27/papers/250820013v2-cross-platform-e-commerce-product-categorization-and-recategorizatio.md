---
layout: default
title: "Cross-Platform E-Commerce Product Categorization and Recategorization: A Multimodal Hierarchical Classification Approach"
---

# Cross-Platform E-Commerce Product Categorization and Recategorization: A Multimodal Hierarchical Classification Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20013" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20013v2</a>
  <a href="https://arxiv.org/pdf/2508.20013.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20013v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20013v2', 'Cross-Platform E-Commerce Product Categorization and Recategorization: A Multimodal Hierarchical Classification Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lotte Gross, Rebecca Walter, Nicole Zoppi, Adrien Justus, Alessandro Gambetti, Qiwei Han, Maximilian Kaiser

**分类**: cs.LG, cs.AI, cs.IR

**发布日期**: 2025-08-27 (更新: 2025-11-09)

**备注**: Accetped at IEEE BigData 2025, 10 pages, 5 figures, 3 tables

---

## 💡 一句话要点

**提出多模态层次分类框架以解决电商产品分类问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电商产品分类` `多模态融合` `层次分类` `动态掩码` `自监督学习` `聚类分析` `视觉特征提取` `文本特征提取`

## 📋 核心要点

1. 现有电商产品分类方法面临平台异构性和分类法结构性局限性的问题，导致分类效果不理想。
2. 本研究提出了一种多模态层次分类框架，结合文本、视觉和联合特征，采用动态掩码和多种融合策略以提高分类一致性。
3. 实验结果显示，使用CLIP嵌入的晚期融合策略实现了98.59%的层次F1值，且自监督的重新分类管道有效发现了新类别。

## 📝 摘要（中文）

本研究针对电商产品分类中的平台异构性和现有分类法的结构性局限性，开发并部署了一种多模态层次分类框架。利用来自40个国际时尚电商平台的271,700个产品数据集，整合文本特征（RoBERTa）、视觉特征（ViT）和联合视觉-语言表示（CLIP）。我们探讨了包括早期、晚期和基于注意力的融合策略，并通过动态掩码增强层次结构以确保分类一致性。结果表明，通过MLP基础的晚期融合策略组合的CLIP嵌入实现了最高的层次F1值（98.59%），超越了单模态基线。为了解决浅层或不一致的类别，我们进一步引入了自监督的“产品重新分类”管道，发现了新的细粒度类别，聚类纯度超过86%。

## 🔬 方法详解

**问题定义**：本研究旨在解决电商产品分类中的平台异构性和现有分类法的结构性局限性。现有方法往往无法有效处理不同平台间的产品特征差异，导致分类效果不佳。

**核心思路**：论文提出了一种多模态层次分类框架，通过整合文本、视觉和联合特征，利用动态掩码和多种融合策略来提高分类的一致性和准确性。这样的设计旨在充分利用不同模态的信息，增强分类模型的表现。

**技术框架**：整体架构包括三个主要模块：文本特征提取（使用RoBERTa）、视觉特征提取（使用ViT）和联合视觉-语言表示（使用CLIP）。在层次结构中，采用动态掩码技术以确保分类的一致性，并通过不同的融合策略（早期、晚期和注意力融合）进行特征整合。

**关键创新**：最重要的技术创新点在于引入了动态掩码和多模态融合策略，尤其是MLP基础的晚期融合方法，显著提升了分类的准确性和一致性。这与传统的单模态方法形成了鲜明对比。

**关键设计**：在参数设置上，采用了适应性学习率和多层感知机（MLP）结构进行晚期融合。损失函数设计上，结合了分类损失和聚类损失，以优化模型的分类效果和聚类性能。

## 📊 实验亮点

实验结果显示，使用CLIP嵌入的MLP基础晚期融合策略达到了98.59%的层次F1值，显著优于单模态基线。同时，自监督的产品重新分类管道成功发现了新的细粒度类别，聚类纯度超过86%。

## 🎯 应用场景

该研究的多模态层次分类框架可广泛应用于电商平台的产品分类和重新分类，帮助商家更准确地组织和展示产品，提高用户体验。此外，该框架的工业可扩展性使其适用于其他领域，如在线零售和市场分析，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This study addresses critical industrial challenges in e-commerce product categorization, namely platform heterogeneity and the structural limitations of existing taxonomies, by developing and deploying a multimodal hierarchical classification framework. Using a dataset of 271,700 products from 40 international fashion e-commerce platforms, we integrate textual features (RoBERTa), visual features (ViT), and joint vision-language representations (CLIP). We investigate fusion strategies, including early, late, and attention-based fusion within a hierarchical architecture enhanced by dynamic masking to ensure taxonomic consistency. Results show that CLIP embeddings combined via an MLP-based late-fusion strategy achieve the highest hierarchical F1 (98.59%), outperforming unimodal baselines. To address shallow or inconsistent categories, we further introduce a self-supervised "product recategorization" pipeline using SimCLR, UMAP, and cascade clustering, which discovered new, fine-grained categories (for example, subtypes of "Shoes") with cluster purities above 86%. Cross-platform experiments reveal a deployment-relevant trade-off: complex late-fusion methods maximize accuracy with diverse training data, while simpler early-fusion methods generalize more effectively to unseen platforms. Finally, we demonstrate the framework's industrial scalability through deployment in EURWEB's commercial transaction intelligence platform via a two-stage inference pipeline, combining a lightweight RoBERTa stage with a GPU-accelerated multimodal stage to balance cost and accuracy.

