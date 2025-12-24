---
layout: default
title: "ClusterUCB: Efficient Gradient-Based Data Selection for Targeted Fine-Tuning of LLMs"
---

# ClusterUCB: Efficient Gradient-Based Data Selection for Targeted Fine-Tuning of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10288" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10288v1</a>
  <a href="https://arxiv.org/pdf/2506.10288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10288v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10288v1', 'ClusterUCB: Efficient Gradient-Based Data Selection for Targeted Fine-Tuning of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zige Wang, Qi Zhu, Fei Mi, Minghui Xu, Ruochun Jin, Wenjing Yang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出ClusterUCB以解决大语言模型微调中的数据选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `微调` `数据选择` `聚类` `上置信界` `多臂赌博机` `计算效率`

## 📋 核心要点

1. 现有的基于梯度的数据选择方法在微调大语言模型时计算资源消耗过大，难以实际应用。
2. 本文提出ClusterUCB框架，通过聚类和改进的UCB算法高效选择数据样本，降低计算成本。
3. 实验结果显示，ClusterUCB在多个基准测试中表现出与传统方法相当的效果，同时显著减少了计算消耗。

## 📝 摘要（中文）

在大语言模型的监督微调中，基于梯度的数据影响近似已被用于选择有用的数据样本。然而，微调过程中梯度计算需要消耗过多资源，难以在实际中应用。本文提出了一种高效的基于梯度的数据选择框架ClusterUCB，结合了聚类和改进的上置信界（UCB）算法。我们首先对训练数据池进行聚类，基于相似梯度特征的数据样本具有相似影响的直觉，将跨簇数据选择视为受限计算预算分配问题，并将其视为多臂赌博机问题。通过记录历史数据影响信息，ClusterUCB在迭代采样过程中直接估计每个簇的分布，并采用冷启动策略平衡探索与利用。实验结果表明，ClusterUCB在计算消耗大幅降低的同时，能够实现与原始基于梯度的数据选择方法相当的效果。

## 🔬 方法详解

**问题定义**：本文解决的是在大语言模型微调过程中，如何高效选择有用的数据样本以降低计算资源消耗的问题。现有方法在计算梯度时需要大量资源，导致其在实际应用中的可行性受到限制。

**核心思路**：论文的核心思路是通过聚类将训练数据池中的样本分组，利用相似样本的梯度特征来推测其影响，从而在多臂赌博机框架下进行数据选择，优化计算预算的分配。

**技术框架**：整体架构包括数据聚类、影响估计和数据选择三个主要模块。首先对训练数据进行聚类，然后在每个簇内记录历史影响信息，最后通过改进的UCB算法进行数据选择。

**关键创新**：最重要的创新点在于将数据选择问题转化为多臂赌博机问题，并通过聚类来减少计算复杂度。这一方法与传统的逐样本梯度计算方法本质上不同，显著提高了效率。

**关键设计**：在设计中，采用了冷启动策略以平衡探索与利用，同时在每次迭代中记录历史数据影响信息，以便更准确地估计每个簇的分布。

## 📊 实验亮点

实验结果表明，ClusterUCB在多个基准测试中能够实现与传统基于梯度的数据选择方法相当的性能，同时计算消耗减少了显著的比例，展示了其在高效数据选择方面的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等场景，能够有效提升大语言模型的微调效率，降低计算资源消耗，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Gradient-based data influence approximation has been leveraged to select useful data samples in the supervised fine-tuning of large language models. However, the computation of gradients throughout the fine-tuning process requires too many resources to be feasible in practice. In this paper, we propose an efficient gradient-based data selection framework with clustering and a modified Upper Confidence Bound (UCB) algorithm. Based on the intuition that data samples with similar gradient features will have similar influences, we first perform clustering on the training data pool. Then, we frame the inter-cluster data selection as a constrained computing budget allocation problem and consider it a multi-armed bandit problem. A modified UCB algorithm is leveraged to solve this problem. Specifically, during the iterative sampling process, historical data influence information is recorded to directly estimate the distributions of each cluster, and a cold start is adopted to balance exploration and exploitation. Experimental results on various benchmarks show that our proposed framework, ClusterUCB, can achieve comparable results to the original gradient-based data selection methods while greatly reducing computing consumption.

