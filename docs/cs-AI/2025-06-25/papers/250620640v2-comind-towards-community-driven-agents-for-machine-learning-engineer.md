---
layout: default
title: "CoMind: Towards Community-Driven Agents for Machine Learning Engineering"
---

# CoMind: Towards Community-Driven Agents for Machine Learning Engineering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20640" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20640v2</a>
  <a href="https://arxiv.org/pdf/2506.20640.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20640v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20640v2', 'CoMind: Towards Community-Driven Agents for Machine Learning Engineering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sijie Li, Weiwei Sun, Shanda Li, Ameet Talwalkar, Yiming Yang

**分类**: cs.AI, cs.LG

**发布日期**: 2025-06-25 (更新: 2025-11-26)

---

## 💡 一句话要点

**提出CoMind以解决机器学习工程中的知识孤岛问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器学习工程` `多代理系统` `知识共享` `实时评估` `Kaggle竞赛` `集体智慧` `自动化模型开发`

## 📋 核心要点

1. 现有的机器学习工程代理通常在特定问题上孤立工作，缺乏与研究社区的互动，导致知识共享不足。
2. 论文提出了MLE-Live框架，并在此基础上开发了CoMind系统，通过多代理协作整合外部知识，提升解决方案的质量。
3. CoMind在75个Kaggle比赛中实现了36%的奖牌率，并在实时比赛中超越92.6%的人工竞争者，显示出显著的性能提升。

## 📝 摘要（中文）

大型语言模型（LLM）代理在自动化机器学习（ML）工程方面展现出潜力。然而，现有代理通常在特定研究问题上孤立操作，未能与更广泛的研究社区互动。为此，我们引入了MLE-Live，一个旨在评估代理与模拟Kaggle研究社区沟通能力的实时评估框架。在此基础上，我们提出了CoMind，一个多代理系统，旨在主动整合外部知识。CoMind采用迭代并行探索机制，同时开发多个解决方案，以平衡探索广度与实施深度。在我们MLE-Live框架下的75个Kaggle比赛中，CoMind实现了36%的奖牌率，确立了新的技术前沿。值得注意的是，在八个实时进行的比赛中，CoMind的平均表现超过92.6%的人工竞争者，在三个官方排行榜中进入前5%，在一个排行榜中进入前1%。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有机器学习工程代理在特定问题上孤立操作的问题，导致知识共享和协作不足。现有方法未能有效利用研究社区的集体智慧。

**核心思路**：论文提出的CoMind系统通过多代理机制，主动整合外部知识，采用迭代并行探索的方法，旨在同时开发多个解决方案，以提高探索的广度和实施的深度。

**技术框架**：CoMind的整体架构包括多个代理，每个代理负责不同的探索任务。系统通过MLE-Live框架进行实时评估，确保代理能够有效沟通和利用外部知识。

**关键创新**：CoMind的主要创新在于其多代理系统设计和迭代并行探索机制，这与传统的单一代理方法形成鲜明对比，能够更好地利用集体知识。

**关键设计**：在设计中，CoMind采用了动态任务分配策略，确保各代理能够在不同的探索阶段进行有效协作，同时设置了适应性损失函数，以优化每个代理的学习过程。

## 📊 实验亮点

在75个Kaggle比赛中，CoMind实现了36%的奖牌率，创下新纪录。在八个实时比赛中，CoMind的表现超过92.6%的人工竞争者，显示出其在复杂任务中的卓越能力，尤其在三个排行榜中进入前5%，在一个排行榜中进入前1%。

## 🎯 应用场景

该研究的潜在应用领域包括机器学习竞赛、数据科学项目和自动化模型开发等。通过促进代理与研究社区的互动，CoMind能够加速知识共享和创新，提升机器学习工程的整体效率和效果。未来，CoMind可能在更广泛的人工智能应用中发挥重要作用，推动智能系统的协作能力。

## 📄 摘要（原文）

> Large language model (LLM) agents show promise in automating machine learning (ML) engineering. However, existing agents typically operate in isolation on a given research problem, without engaging with the broader research community, where human researchers often gain insights and contribute by sharing knowledge. To bridge this gap, we introduce MLE-Live, a live evaluation framework designed to assess an agent's ability to communicate with and leverage collective knowledge from a simulated Kaggle research community. Building on this framework, we propose CoMind, an multi-agent system designed to actively integrate external knowledge. CoMind employs an iterative parallel exploration mechanism, developing multiple solutions simultaneously to balance exploratory breadth with implementation depth. On 75 past Kaggle competitions within our MLE-Live framework, CoMind achieves a 36% medal rate, establishing a new state of the art. Critically, when deployed in eight live, ongoing competitions, CoMind outperforms 92.6% of human competitors on average, placing in the top 5% on three official leaderboards and the top 1% on one.

