---
layout: default
title: "Share Your Attention: Transformer Weight Sharing via Matrix-based Dictionary Learning"
---

# Share Your Attention: Transformer Weight Sharing via Matrix-based Dictionary Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04581" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04581v1</a>
  <a href="https://arxiv.org/pdf/2508.04581.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04581v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04581v1', 'Share Your Attention: Transformer Weight Sharing via Matrix-based Dictionary Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Magauiya Zhussip, Dmitriy Shopkhoev, Ammar Ali, Stamatios Lefkimmiatis

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出MASA框架以解决变换器层间冗余问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `变换器压缩` `权重共享` `字典学习` `大型语言模型` `视觉变换器` `参数效率` `深度学习`

## 📋 核心要点

1. 现有的压缩技术主要集中在变换器内部块的优化，未能有效利用层间的冗余性。
2. 本文提出的MASA框架通过结构化权重共享，减少了变换器层之间的参数冗余，提升了模型效率。
3. 实验结果显示，MASA在多个参数规模下的性能优于传统的低秩基线和分组查询注意力方法，且参数减少达66.7%。

## 📝 摘要（中文）

大型语言模型（LLMs）在人工智能应用中取得了革命性进展，但其高计算和内存需求限制了其广泛部署。现有的压缩技术主要集中在内部块优化上，而变换器的重复层结构暗示了显著的层间冗余。本文提出了一种基于矩阵字典学习的结构化权重共享框架MASA，通过将注意力投影矩阵分解为共享字典原子，减少了66.7%的参数，同时保持了性能。MASA作为一种即插即用的替代方案，能够与标准优化器一起训练，并将每层的权重表示为共享矩阵原子的线性组合。实验表明，MASA在多个参数规模下的基准准确性和困惑度优于其他方法，且在视觉变换器中同样表现出色。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中变换器层间的冗余问题，现有方法未能充分利用层间的相似性，导致参数使用效率低下。

**核心思路**：MASA框架通过将注意力投影矩阵分解为共享的字典原子，允许不同层共享相同的参数，从而减少冗余并提高效率。

**技术框架**：MASA的整体架构包括三个主要模块：1) 字典学习模块，用于生成共享的矩阵原子；2) 权重表示模块，将每层的权重表示为共享原子的线性组合；3) 训练模块，使用标准优化器进行训练。

**关键创新**：MASA的主要创新在于其结构化权重共享机制，允许跨层共享参数，而无需复杂的蒸馏或架构变更，这与现有方法形成鲜明对比。

**关键设计**：在设计上，MASA采用了标准的损失函数和优化策略，字典的大小和共享表示的有效性经过消融实验验证，确保了模型的鲁棒性和性能。

## 📊 实验亮点

实验结果显示，MASA在100M到700M参数规模的模型中，基准准确性和困惑度均优于分组查询注意力（GQA）和低秩基线，且在参数预算相当的情况下，参数减少达66.7%。在视觉变换器中，MASA同样实现了与传统方法相当的性能，展现了其广泛的适用性。

## 🎯 应用场景

MASA框架具有广泛的应用潜力，特别是在需要高效参数使用的大型语言模型和视觉变换器中。其结构化权重共享策略可以显著降低模型的计算和内存需求，使得在资源受限的环境中部署大型模型成为可能。此外，MASA还可以应用于预训练模型的参数压缩，进一步提升其实际价值。

## 📄 摘要（原文）

> Large language models (LLMs) have revolutionized AI applications, yet their high computational and memory demands hinder their widespread deployment. Existing compression techniques focus on intra-block optimizations (e.g. low-rank approximation, attention head pruning), while the repetitive layered structure of transformers implies significant inter-block redundancy - a dimension largely unexplored beyond key-value (KV) caching. Inspired by dictionary learning in CNNs, we propose a framework for structured weight sharing across transformer layers. Our approach decomposes attention projection matrices into shared dictionary atoms, reducing the attention module's parameters by 66.7% while achieving on-par performance. Unlike complex methods requiring distillation or architectural changes, MASA (Matrix Atom Sharing in Attention) operates as a drop-in replacement - trained with standard optimizers - and represents each layer's weights as linear combinations of shared matrix atoms. Experiments across scales (100M-700M parameters) show that MASA achieves better benchmark accuracy and perplexity than grouped-query attention (GQA), low-rank baselines and recently proposed Repeat-all-over/Sequential sharing at comparable parameter budgets. Ablation studies confirm robustness to the dictionary size and the efficacy of shared representations in capturing cross-layer statistical regularities. Extending to Vision Transformers (ViT), MASA matches performance metrics on image classification and detection tasks with 66.7% fewer attention parameters. By combining dictionary learning strategies with transformer efficiency, MASA offers a scalable blueprint for parameter-efficient models without sacrificing performance. Finally, we investigate the possibility of employing MASA on pretrained LLMs to reduce their number of parameters without experiencing any significant drop in their performance.

