---
layout: default
title: Rank, Chunk and Expand: Lineage-Oriented Reasoning for Taxonomy Expansion
---

# Rank, Chunk and Expand: Lineage-Oriented Reasoning for Taxonomy Expansion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13282" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13282v4</a>
  <a href="https://arxiv.org/pdf/2505.13282.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13282v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13282v4', 'Rank, Chunk and Expand: Lineage-Oriented Reasoning for Taxonomy Expansion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sahil Mishra, Kumar Arjun, Tanmoy Chakraborty

**分类**: cs.CL

**发布日期**: 2025-05-19 (更新: 2025-05-31)

**备注**: Accepted in the Findings of ACL 2025

---

## 💡 一句话要点

**提出LORex框架以解决税onomies扩展中的噪声与上下文限制问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `税onomies扩展` `知识图谱` `推荐系统` `生成推理` `判别模型` `上下文优化` `噪声过滤` `层次推理`

## 📋 核心要点

1. 现有方法在税onomies扩展中面临判别模型的表示能力和泛化能力不足，以及生成方法处理噪声和上下文限制的问题。
2. 本文提出LORex框架，通过将候选术语分批处理，结合判别排名和生成推理，有效过滤噪声并优化选择过程。
3. 实验结果显示，LORex在准确率上提高了12%，在Wu & Palmer相似度上提高了5%，超越了现有最先进的方法。

## 📝 摘要（中文）

税onomies作为层次化知识图谱在推荐系统和网络应用中至关重要。随着数据的增长，扩展税onomies变得尤为重要。然而，现有方法面临关键挑战：判别模型在表示能力和泛化方面存在局限，而生成方法要么一次性处理所有候选项，导致噪声和上下文限制，要么通过选择噪声候选项而丢弃相关实体。为此，本文提出了LORex（Lineage-Oriented Reasoning for Taxonomy Expansion），一个结合判别排名和生成推理的高效税onomies扩展框架。LORex通过将候选术语分批排名和分块，过滤噪声并通过推理候选项的层次结构迭代精炼选择，从而确保上下文效率。实验结果表明，LORex在四个基准和十二个基线上的准确率提高了12%，Wu & Palmer相似度提高了5%。

## 🔬 方法详解

**问题定义**：本文旨在解决税onomies扩展中的噪声干扰和上下文限制问题。现有的判别模型和生成方法在处理候选项时存在显著不足，导致扩展效果不佳。

**核心思路**：LORex框架的核心思想是将候选术语进行排名和分块处理，通过推理候选项的层次结构来过滤噪声，从而提高上下文效率和扩展质量。

**技术框架**：LORex的整体架构包括两个主要模块：判别排名模块和生成推理模块。首先，候选术语被分为多个批次进行处理，接着通过判别模型进行排名，最后利用生成推理对每个批次进行上下文优化。

**关键创新**：LORex的主要创新在于其将判别和生成方法结合，采用分块处理策略，有效减少了噪声干扰，并通过层次推理提升了选择的准确性。这与传统方法的单一处理方式有本质区别。

**关键设计**：在设计上，LORex使用了特定的损失函数来优化排名效果，并在网络结构中引入了层次推理机制，以确保候选项的上下文相关性和准确性。

## 📊 实验亮点

LORex在四个基准测试和十二个基线方法上的实验结果显示，其准确率提高了12%，Wu & Palmer相似度提升了5%。这些结果表明，LORex在处理税onomies扩展任务时显著优于现有最先进的方法，展示了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括推荐系统、知识图谱构建和信息检索等。通过提高税onomies的扩展效率，LORex能够帮助企业和研究机构更好地管理和利用大规模数据，提升用户体验和决策支持。未来，该框架可能在多领域的知识管理和智能应用中发挥重要作用。

## 📄 摘要（原文）

> Taxonomies are hierarchical knowledge graphs crucial for recommendation systems, and web applications. As data grows, expanding taxonomies is essential, but existing methods face key challenges: (1) discriminative models struggle with representation limits and generalization, while (2) generative methods either process all candidates at once, introducing noise and exceeding context limits, or discard relevant entities by selecting noisy candidates. We propose LORex (Lineage-Oriented Reasoning for Taxonomy Expansion), a plug-and-play framework that combines discriminative ranking and generative reasoning for efficient taxonomy expansion. Unlike prior methods, LORex ranks and chunks candidate terms into batches, filtering noise and iteratively refining selections by reasoning candidates' hierarchy to ensure contextual efficiency. Extensive experiments across four benchmarks and twelve baselines show that LORex improves accuracy by 12% and Wu & Palmer similarity by 5% over state-of-the-art methods.

