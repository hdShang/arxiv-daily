---
layout: default
title: "DiLoCoX: A Low-Communication Large-Scale Training Framework for Decentralized Cluster"
---

# DiLoCoX: A Low-Communication Large-Scale Training Framework for Decentralized Cluster

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21263" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21263v1</a>
  <a href="https://arxiv.org/pdf/2506.21263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21263v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21263v1', 'DiLoCoX: A Low-Communication Large-Scale Training Framework for Decentralized Cluster')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ji Qi, WenPeng Zhu, Li Li, Ming Wu, YingJun Wu, Wu He, Xun Gao, Jason Zeng, Michael Heinrich

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-26

---

## 💡 一句话要点

**提出DiLoCoX以解决大规模分散集群训练中的低通信问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分散训练` `低通信` `大规模模型` `管道并行` `自适应梯度压缩` `深度学习` `机器学习`

## 📋 核心要点

1. 现有的基础模型训练方法在大规模分散集群中面临高通信需求和网络速度限制的挑战。
2. DiLoCoX框架通过结合多种技术，如管道并行和自适应梯度压缩，来降低通信需求并提高训练效率。
3. 实验结果表明，DiLoCoX在1Gbps网络上预训练107B参数模型时，训练速度提升了357倍，且模型收敛性保持良好。

## 📝 摘要（中文）

基础模型，特别是大型语言模型（LLMs）的分布式训练需要高水平的通信，通常依赖于快速可靠的集中式集群。本文提出DiLoCoX，一个低通信的大规模分散集群训练框架，结合了管道并行、双优化器策略、通信与本地训练的一步延迟重叠以及自适应梯度压缩方案。通过理论分析和实证验证，DiLoCoX在1Gbps网络上成功预训练了107B参数的基础模型，相较于传统的AllReduce方法，训练速度提升了357倍，同时模型收敛性几乎没有下降。这是首次成功应用于超过1000亿参数模型的分散训练框架。

## 🔬 方法详解

**问题定义**：本文旨在解决在低速网络环境下进行大规模基础模型训练时的高通信需求问题。现有方法通常依赖于集中式集群，限制了模型规模和训练效率。

**核心思路**：DiLoCoX通过引入管道并行、双优化器策略和自适应梯度压缩等技术，旨在减少通信开销并提高训练速度，从而使得在分散集群中训练超过100亿参数的模型成为可能。

**技术框架**：DiLoCoX的整体架构包括多个模块：首先是管道并行以提高计算效率，其次是双优化器策略以优化训练过程，最后是自适应梯度压缩以减少通信量。

**关键创新**：DiLoCoX的主要创新在于其综合使用了一步延迟重叠的通信与本地训练策略，以及自适应梯度压缩方案，这与传统的AllReduce方法相比，显著降低了通信需求并提升了训练速度。

**关键设计**：在关键设计方面，DiLoCoX采用了特定的参数设置和损失函数，以确保在低通信条件下仍能保持模型的收敛性和训练效果。

## 📊 实验亮点

DiLoCoX在1Gbps网络上成功预训练107B参数的基础模型，相较于传统的AllReduce方法，训练速度提升了357倍，同时模型的收敛性几乎没有下降，展示了其在低通信环境下的优越性能。

## 🎯 应用场景

DiLoCoX框架的潜在应用领域包括大规模语言模型的训练、分散式计算环境下的机器学习任务以及需要高效通信的深度学习应用。其实际价值在于能够在低带宽条件下有效训练超大规模模型，推动人工智能技术的进一步发展。

## 📄 摘要（原文）

> The distributed training of foundation models, particularly large language models (LLMs), demands a high level of communication. Consequently, it is highly dependent on a centralized cluster with fast and reliable interconnects. Can we conduct training on slow networks and thereby unleash the power of decentralized clusters when dealing with models exceeding 100 billion parameters? In this paper, we propose DiLoCoX, a low-communication large-scale decentralized cluster training framework. It combines Pipeline Parallelism with Dual Optimizer Policy, One-Step-Delay Overlap of Communication and Local Training, and an Adaptive Gradient Compression Scheme. This combination significantly improves the scale of parameters and the speed of model pre-training. We justify the benefits of one-step-delay overlap of communication and local training, as well as the adaptive gradient compression scheme, through a theoretical analysis of convergence. Empirically, we demonstrate that DiLoCoX is capable of pre-training a 107B foundation model over a 1Gbps network. Compared to vanilla AllReduce, DiLoCoX can achieve a 357x speedup in distributed training while maintaining negligible degradation in model convergence. To the best of our knowledge, this is the first decentralized training framework successfully applied to models with over 100 billion parameters.

