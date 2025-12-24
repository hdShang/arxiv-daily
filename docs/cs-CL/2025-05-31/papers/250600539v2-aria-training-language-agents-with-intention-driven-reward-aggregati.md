---
layout: default
title: ARIA: Training Language Agents with Intention-Driven Reward Aggregation
---

# ARIA: Training Language Agents with Intention-Driven Reward Aggregation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00539" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00539v2</a>
  <a href="https://arxiv.org/pdf/2506.00539.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00539v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00539v2', 'ARIA: Training Language Agents with Intention-Driven Reward Aggregation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruihan Yang, Yikai Zhang, Aili Chen, Xintao Wang, Siyu Yuan, Jiangjie Chen, Deqing Yang, Yanghua Xiao

**分类**: cs.CL

**发布日期**: 2025-05-31 (更新: 2025-06-04)

---

## 💡 一句话要点

**提出ARIA以解决开放式语言行动环境中的奖励稀疏问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言智能体` `意图空间` `奖励聚合` `强化学习` `自然语言处理`

## 📋 核心要点

1. 现有方法在开放式语言行动环境中面临奖励稀疏性和方差大的挑战，影响强化学习的有效性。
2. ARIA通过将高维联合令牌分布映射到低维意图空间，聚合语义相似动作的奖励，从而提高训练效率。
3. 实验结果显示，ARIA在四个下游任务中平均提升了9.95%的性能，显著降低了策略梯度的方差。

## 📝 摘要（中文）

大型语言模型（LLMs）使得智能体能够通过自由形式的语言交互进行复杂推理和决策。然而，在开放式语言行动环境中，动作空间可以被表述为一个令牌的联合分布，导致动作空间呈指数级增长。采样这样的动作空间可能导致奖励稀疏性极高，从而带来巨大的奖励方差，妨碍有效的强化学习（RL）。为了解决这一问题，本文提出了ARIA，一种通过意图空间聚合奖励的方法，以实现高效的语言智能体训练。ARIA旨在将自然语言动作从高维的联合令牌分布空间投影到低维的意图空间，在该空间中，语义相似的动作被聚类并分配共享奖励。这种意图感知的奖励聚合通过密集化奖励信号来降低奖励方差，促进更好的策略优化。大量实验表明，ARIA不仅显著降低了策略梯度方差，还在四个下游任务中平均提升了9.95%的性能，始终优于离线和在线RL基线。

## 🔬 方法详解

**问题定义**：本文旨在解决开放式语言行动环境中由于动作空间巨大导致的奖励稀疏性和方差问题。现有方法在此类环境中难以有效进行强化学习，导致训练效率低下。

**核心思路**：ARIA的核心思路是通过意图空间聚合奖励，将自然语言动作从高维空间映射到低维意图空间，从而减少奖励方差并提高训练效率。这样的设计使得语义相似的动作能够共享奖励，增强了奖励信号的密集性。

**技术框架**：ARIA的整体架构包括两个主要模块：首先是意图空间的构建模块，通过聚类算法将语义相似的动作聚集在一起；其次是奖励聚合模块，根据聚类结果为每个动作分配共享奖励。整个流程包括数据预处理、意图空间映射和奖励聚合三个阶段。

**关键创新**：ARIA的最大创新在于引入了意图空间的概念，通过聚合语义相似动作的奖励来降低奖励方差，这与传统的逐个动作评估的方式有本质区别。

**关键设计**：在设计上，ARIA采用了特定的聚类算法来构建意图空间，并使用了基于聚类结果的奖励分配机制。此外，损失函数的设计也考虑了奖励的密集性，以促进更好的策略优化。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，ARIA在四个下游任务中平均提升了9.95%的性能，显著降低了策略梯度方差，优于现有的离线和在线强化学习基线。这一成果展示了ARIA在复杂语言环境中的有效性和优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能对话系统、自动问答、在线协商等开放式语言交互场景。通过提高语言智能体的训练效率和决策能力，ARIA能够在实际应用中显著提升用户体验和系统性能，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have enabled agents to perform complex reasoning and decision-making through free-form language interactions. However, in open-ended language action environments (e.g., negotiation or question-asking games), the action space can be formulated as a joint distribution over tokens, resulting in an exponentially large action space. Sampling actions in such a space can lead to extreme reward sparsity, which brings large reward variance, hindering effective reinforcement learning (RL). To address this, we propose ARIA, a method that Aggregates Rewards in Intention space to enable efficient and effective language Agents training. ARIA aims to project natural language actions from the high-dimensional joint token distribution space into a low-dimensional intention space, where semantically similar actions are clustered and assigned shared rewards. This intention-aware reward aggregation reduces reward variance by densifying reward signals, fostering better policy optimization. Extensive experiments demonstrate that ARIA not only significantly reduces policy gradient variance, but also delivers substantial performance gains of an average of 9.95% across four downstream tasks, consistently outperforming offline and online RL baselines.

