---
layout: default
title: "CoDiEmb: A Collaborative yet Distinct Framework for Unified Representation Learning in Information Retrieval and Semantic Textual Similarity"
---

# CoDiEmb: A Collaborative yet Distinct Framework for Unified Representation Learning in Information Retrieval and Semantic Textual Similarity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11442" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11442v2</a>
  <a href="https://arxiv.org/pdf/2508.11442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11442v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11442v2', 'CoDiEmb: A Collaborative yet Distinct Framework for Unified Representation Learning in Information Retrieval and Semantic Textual Similarity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bowen Zhang, Zixin Song, Chunquan Chen, Qian-Wen Zhang, Di Yin, Xing Sun

**分类**: cs.CL

**发布日期**: 2025-08-15 (更新: 2025-09-29)

---

## 💡 一句话要点

**提出CoDiEmb以解决信息检索与语义文本相似性联合学习中的负迁移问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `信息检索` `语义文本相似性` `联合学习` `文本嵌入` `负迁移` `深度学习`

## 📋 核心要点

1. 现有方法在信息检索与语义文本相似性联合训练中存在负迁移问题，导致性能折衷。
2. CoDiEmb框架通过解耦任务特定信号，采用动态采样和任务专用目标实现有效联合优化。
3. 在15个标准基准上进行的实验验证了CoDiEmb的有效性，显著提升了嵌入空间的几何特性。

## 📝 摘要（中文）

在表示学习中，学习能够在多种下游任务中表现优异的统一文本嵌入是一个核心目标，但负迁移仍然是一个持续的障碍。特别是在信息检索（IR）和语义文本相似性（STS）这两项基本但本质上不同的任务中，联合训练单一编码器通常会导致性能的显著折衷。为了解决这一冲突，本文提出了CoDiEmb框架，通过系统性地解耦任务特定的学习信号，整合了三项关键创新以实现有效的联合优化。实验结果表明，该框架不仅减轻了跨任务的折衷，还显著改善了嵌入空间的几何特性。

## 🔬 方法详解

**问题定义**：本文旨在解决信息检索（IR）和语义文本相似性（STS）任务联合训练中的负迁移问题。现有方法在这两项任务上往往表现不佳，导致性能折衷。

**核心思路**：CoDiEmb框架通过系统性地解耦任务特定的学习信号，采用动态采样和任务专用目标，旨在有效地联合优化这两项任务。

**技术框架**：CoDiEmb整体架构包括三个主要模块：任务专用目标与动态采样器、基于偏差的模型融合策略，以及高效的单阶段训练管道。

**关键创新**：该框架的创新点在于采用任务专用目标和动态采样，防止梯度干扰；通过分析参数偏差实现细粒度的模型融合；以及设计简单且稳定收敛的单阶段训练流程。

**关键设计**：在损失函数方面，IR任务使用多正样本和难负样本的对比损失，STS任务则采用顺序感知目标；模型融合策略通过计算每个参数的偏差来确定合并权重。

## 📊 实验亮点

在15个标准基准上的实验结果显示，CoDiEmb框架显著改善了信息检索和语义文本相似性任务的性能，相较于基线方法，嵌入空间的几何特性得到了显著提升，具体性能提升幅度未知。

## 🎯 应用场景

CoDiEmb框架在信息检索和语义文本相似性等自然语言处理任务中具有广泛的应用潜力。其有效的联合学习方法能够提高文本嵌入的质量，进而提升搜索引擎、推荐系统和对话系统等应用的性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Learning unified text embeddings that excel across diverse downstream tasks is a central goal in representation learning, yet negative transfer remains a persistent obstacle. This challenge is particularly pronounced when jointly training a single encoder for Information Retrieval (IR) and Semantic Textual Similarity (STS), two essential but fundamentally disparate tasks for which naive co-training typically yields steep performance trade-offs. We argue that resolving this conflict requires systematically decoupling task-specific learning signals throughout the training pipeline. To this end, we introduce CoDiEmb, a unified framework that reconciles the divergent requirements of IR and STS in a collaborative yet distinct manner. CoDiEmb integrates three key innovations for effective joint optimization: (1) Task-specialized objectives paired with a dynamic sampler that forms single-task batches and balances per-task updates, thereby preventing gradient interference. For IR, we employ a contrastive loss with multiple positives and hard negatives, augmented by cross-device sampling. For STS, we adopt order-aware objectives that directly optimize correlation and ranking consistency. (2) A delta-guided model fusion strategy that computes fine-grained merging weights for checkpoints by analyzing each parameter's deviation from its pre-trained initialization, proving more effective than traditional Model Soups. (3) An efficient, single-stage training pipeline that is simple to implement and converges stably. Extensive experiments on 15 standard IR and STS benchmarks across three base encoders validate CoDiEmb. Our results and analysis demonstrate that the framework not only mitigates cross-task trade-offs but also measurably improves the geometric properties of the embedding space.

