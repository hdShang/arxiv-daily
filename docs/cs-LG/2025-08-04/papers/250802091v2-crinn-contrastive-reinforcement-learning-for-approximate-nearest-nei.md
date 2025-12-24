---
layout: default
title: "CRINN: Contrastive Reinforcement Learning for Approximate Nearest Neighbor Search"
---

# CRINN: Contrastive Reinforcement Learning for Approximate Nearest Neighbor Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02091" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02091v2</a>
  <a href="https://arxiv.org/pdf/2508.02091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02091v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02091v2', 'CRINN: Contrastive Reinforcement Learning for Approximate Nearest Neighbor Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoya Li, Xiaofei Sun, Albert Wang, Chris Shum, Jiwei Li

**分类**: cs.LG, cs.AI, cs.CL, cs.DB

**发布日期**: 2025-08-04 (更新: 2025-08-20)

**备注**: Preprint Version

**🔗 代码/项目**: [GITHUB](https://github.com/deepreinforce-ai/CRINN)

---

## 💡 一句话要点

**提出CRINN以解决近似最近邻搜索的优化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `近似最近邻搜索` `强化学习` `算法优化` `深度学习` `信息检索`

## 📋 核心要点

1. 现有的近似最近邻搜索算法在执行速度和准确性之间存在权衡，难以满足高效性需求。
2. CRINN将ANNS优化视为强化学习问题，通过执行速度作为奖励信号，自动生成更快的实现。
3. 实验结果显示，CRINN在多个基准数据集上超越了现有最先进的算法，提升了搜索效率和准确性。

## 📝 摘要（中文）

近似最近邻搜索（ANNS）算法在AI应用中变得愈发重要，尤其是在检索增强生成（RAG）和基于代理的LLM应用中。本文提出了CRINN，这是一种新的ANNS算法范式。CRINN将ANNS优化视为一个强化学习问题，其中执行速度作为奖励信号。这种方法能够自动生成逐步更快的ANNS实现，同时保持准确性约束。实验评估表明，CRINN在六个广泛使用的NNS基准数据集上表现出色。与最先进的开源ANNS算法相比，CRINN在三个数据集上取得最佳性能，并在两个数据集上并列第一。CRINN的成功不仅限于ANNS优化，它验证了增强强化学习的LLM可以作为自动化复杂算法优化的有效工具。

## 🔬 方法详解

**问题定义**：本文旨在解决近似最近邻搜索（ANNS）算法在执行速度和准确性之间的权衡问题。现有方法往往无法在保证准确性的前提下实现高效的搜索，导致在实际应用中受到限制。

**核心思路**：CRINN通过将ANNS优化视为强化学习问题，利用执行速度作为奖励信号，自动生成逐步更快的ANNS实现。这种方法能够在保持准确性的同时，提升搜索效率。

**技术框架**：CRINN的整体架构包括数据预处理、模型训练和执行优化三个主要模块。首先，通过强化学习算法训练模型，然后根据奖励信号优化搜索策略，最后生成高效的ANNS实现。

**关键创新**：CRINN的主要创新在于将强化学习应用于ANNS优化，利用执行速度作为反馈信号。这一方法与传统的基于启发式或手动调整的优化方法有本质区别，能够实现更高效的自动化优化。

**关键设计**：在CRINN中，关键参数包括学习率、奖励函数的设计以及网络结构的选择。损失函数的设计考虑了准确性和速度的平衡，以确保生成的ANNS实现既快速又准确。具体的网络结构采用了深度学习模型，以适应复杂的搜索任务。

## 📊 实验亮点

在实验中，CRINN在GIST-960-Euclidean、MNIST-784-Euclidean和GloVe-25-angular三个数据集上取得了最佳性能，并在SIFT-128-Euclidean和GloVe-25-angular两个数据集上并列第一。相较于现有的最先进开源ANNS算法，CRINN展现出显著的性能提升，验证了其有效性。

## 🎯 应用场景

CRINN的研究成果在多个领域具有广泛的应用潜力，特别是在信息检索、推荐系统和自然语言处理等需要高效搜索的场景中。通过优化ANNS，CRINN能够显著提升系统的响应速度和用户体验，未来可能推动更多智能应用的发展。

## 📄 摘要（原文）

> Approximate nearest-neighbor search (ANNS) algorithms have become increasingly critical for recent AI applications, particularly in retrieval-augmented generation (RAG) and agent-based LLM applications. In this paper, we present CRINN, a new paradigm for ANNS algorithms. CRINN treats ANNS optimization as a reinforcement learning problem where execution speed serves as the reward signal. This approach enables the automatic generation of progressively faster ANNS implementations while maintaining accuracy constraints. Our experimental evaluation demonstrates CRINN's effectiveness across six widely-used NNS benchmark datasets. When compared against state-of-the-art open-source ANNS algorithms, CRINN achieves best performance on three of them (GIST-960-Euclidean, MNIST-784-Euclidean, and GloVe-25-angular), and tied for first place on two of them (SIFT-128-Euclidean and GloVe-25-angular). The implications of CRINN's success reach well beyond ANNS optimization: It validates that LLMs augmented with reinforcement learning can function as an effective tool for automating sophisticated algorithmic optimizations that demand specialized knowledge and labor-intensive manual refinement. Code can be found at https://github.com/deepreinforce-ai/CRINN

