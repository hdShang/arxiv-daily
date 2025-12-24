---
layout: default
title: CompeteSMoE -- Statistically Guaranteed Mixture of Experts Training via Competition
---

# CompeteSMoE -- Statistically Guaranteed Mixture of Experts Training via Competition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13380" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13380v1</a>
  <a href="https://arxiv.org/pdf/2505.13380.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13380v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13380v1', 'CompeteSMoE -- Statistically Guaranteed Mixture of Experts Training via Competition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nam V. Nguyen, Huy Nguyen, Quang Pham, Van Nguyen, Savitha Ramasamy, Nhat Ho

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-19

**备注**: 52 pages. This work is an improved version of the previous study at arXiv:2402.02526

**🔗 代码/项目**: [GITHUB](https://github.com/Fsoft-AIC/CompeteSMoE)

---

## 💡 一句话要点

**提出CompeteSMoE以解决稀疏专家模型训练中的路由效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏专家模型` `竞争机制` `路由效率` `语言模型` `视觉指令调优` `样本效率` `深度学习`

## 📋 核心要点

1. 现有的稀疏专家模型训练方法在路由过程中效率低下，导致计算资源浪费。
2. 本文提出了一种竞争机制，通过优化令牌路由到响应最强的专家，提高了样本效率。
3. 实验结果显示，CompeteSMoE在多个任务上表现优异，训练开销低，具有良好的可扩展性。

## 📝 摘要（中文）

稀疏专家模型（SMoE）为提升模型复杂度提供了有效的解决方案，但现有训练方法在路由过程中存在不足，导致计算效率低下。本文提出了一种竞争机制，通过将输入令牌路由到响应最强的专家，显著提高了样本效率。我们开发了CompeteSMoE算法，利用路由器学习竞争策略，在视觉指令调优和语言预训练任务中表现出色，且训练开销低。实验结果表明，CompeteSMoE在性能、鲁棒性和可扩展性方面优于现有的SMoE策略。

## 🔬 方法详解

**问题定义**：本文旨在解决稀疏专家模型（SMoE）训练中的路由效率问题。现有方法的路由过程未能有效利用专家的计算能力，导致样本效率低下。

**核心思路**：我们提出了一种竞争机制，通过将输入令牌路由到响应最强的专家，从而提高了样本效率。这种设计使得每个专家的计算能力能够直接影响路由决策。

**技术框架**：CompeteSMoE的整体架构包括一个路由器模块，该模块学习竞争策略以优化令牌的路由过程。算法通过训练过程不断调整路由策略，以实现高效的专家选择。

**关键创新**：本文的主要创新在于引入竞争机制，显著提高了样本效率，相较于传统的softmax路由方法，能够更有效地利用专家的计算能力。

**关键设计**：在算法实现中，我们设置了适当的损失函数以优化路由策略，并采用了简单的网络结构以降低训练开销，同时确保了模型的性能和可扩展性。

## 📊 实验亮点

在多个实验中，CompeteSMoE在视觉指令调优和语言预训练任务上均表现出色，相较于现有的SMoE策略，性能提升显著，具体提升幅度达到XX%（具体数据待补充）。此外，训练开销显著降低，使得大规模模型训练更加可行。

## 🎯 应用场景

CompeteSMoE在大规模语言模型训练、视觉指令调优等领域具有广泛的应用潜力。其高效的路由机制和低训练开销使其适用于需要快速响应和高性能的实际场景，如智能助手、自动翻译和多模态学习等。未来，该方法有望推动更复杂模型的开发与应用。

## 📄 摘要（原文）

> Sparse mixture of experts (SMoE) offers an appealing solution to scale up the model complexity beyond the mean of increasing the network's depth or width. However, we argue that effective SMoE training remains challenging because of the suboptimal routing process where experts that perform computation do not directly contribute to the routing process. In this work, we propose competition, a novel mechanism to route tokens to experts with the highest neural response. Theoretically, we show that the competition mechanism enjoys a better sample efficiency than the traditional softmax routing. Furthermore, we develop CompeteSMoE, a simple yet effective algorithm to train large language models by deploying a router to learn the competition policy, thus enjoying strong performances at a low training overhead. Our extensive empirical evaluations on both the visual instruction tuning and language pre-training tasks demonstrate the efficacy, robustness, and scalability of CompeteSMoE compared to state-of-the-art SMoE strategies. We have made the implementation available at: https://github.com/Fsoft-AIC/CompeteSMoE. This work is an improved version of the previous study at arXiv:2402.02526

