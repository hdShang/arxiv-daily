---
layout: default
title: Multi-source Plume Tracing via Multi-Agent Reinforcement Learning
---

# Multi-source Plume Tracing via Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08825" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08825v1</a>
  <a href="https://arxiv.org/pdf/2505.08825.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08825v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08825v1', 'Multi-source Plume Tracing via Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pedro Antonio Alarcon Granadeno, Theodore Chambers, Jane Cleland-Huang

**分类**: cs.MA, cs.AI

**发布日期**: 2025-05-12

**备注**: 13 pages, 7 figures

---

## 💡 一句话要点

**提出多源蒸汽追踪算法以解决工业污染源定位问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `污染源定位` `高斯蒸汽模型` `部分可观察马尔可夫博弈` `无人机群体` `环境监测` `深度学习`

## 📋 核心要点

1. 现有的蒸汽追踪方法在复杂的湍流环境中表现不佳，难以有效定位多个污染源。
2. 本文提出了一种基于多智能体强化学习的算法，通过建模为部分可观察马尔可夫博弈来解决污染源定位问题。
3. 实验结果显示，该算法仅需探索环境的1.29%即可成功定位污染源，显著优于传统方法。

## 📝 摘要（中文）

工业灾难如1984年的博帕尔灾难和2015年的阿利索峡谷气体泄漏凸显了快速可靠的蒸汽追踪算法的迫切需求。传统方法如基于梯度或生物启发的策略在现实的湍流条件下常常失效。为了解决这些挑战，本文提出了一种多智能体强化学习（MARL）算法，旨在利用小型无人机群体定位多个空气污染源。该方法将问题建模为部分可观察马尔可夫博弈（POMG），采用基于长短期记忆（LSTM）的特定动作双深度递归Q网络（ADDRQN），有效地使用历史动作-观察对序列来近似潜在状态。与以往研究不同，我们使用基于高斯蒸汽模型（GPM）的通用仿真环境，融入了三维环境、传感器噪声、多个交互智能体和多个蒸汽源等现实元素。实验结果表明，该算法显著优于传统方法。

## 🔬 方法详解

**问题定义**：本文旨在解决在复杂湍流环境中定位多个空气污染源的具体问题。现有的传统方法在这种情况下常常无法有效工作，导致定位精度低和响应时间长。

**核心思路**：论文的核心解决思路是采用多智能体强化学习（MARL）算法，将问题建模为部分可观察马尔可夫博弈（POMG），利用小型无人机群体进行污染源的定位。通过使用历史动作-观察对序列，算法能够更好地适应复杂环境。

**技术框架**：整体架构包括多个智能体在三维环境中进行探索和学习，使用基于LSTM的ADDRQN来处理输入的历史数据。主要模块包括环境建模、智能体决策和学习过程。

**关键创新**：最重要的技术创新在于将动作历史作为输入的一部分，这增强了模型在部分可观察环境中的适应性。与现有方法相比，算法在复杂环境中表现出更高的效率和准确性。

**关键设计**：在技术细节上，使用了LSTM网络结构来处理时间序列数据，设计了特定的损失函数以优化智能体的学习过程，并在仿真环境中引入了传感器噪声和多个交互智能体的因素。

## 📊 实验亮点

实验结果表明，提出的算法在环境探索方面表现出色，仅需探索1.29%的环境即可成功定位污染源，显著优于传统的基线方法。这一性能提升展示了多智能体强化学习在复杂环境中的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括环境监测、灾难响应和城市空气质量管理等。通过提高污染源定位的效率和准确性，能够更好地保护公共健康和环境，具有重要的实际价值和社会影响。未来，该技术可扩展至更复杂的环境和更多类型的污染源追踪。

## 📄 摘要（原文）

> Industrial catastrophes like the Bhopal disaster (1984) and the Aliso Canyon gas leak (2015) demonstrate the urgent need for rapid and reliable plume tracing algorithms to protect public health and the environment. Traditional methods, such as gradient-based or biologically inspired approaches, often fail in realistic, turbulent conditions. To address these challenges, we present a Multi-Agent Reinforcement Learning (MARL) algorithm designed for localizing multiple airborne pollution sources using a swarm of small uncrewed aerial systems (sUAS). Our method models the problem as a Partially Observable Markov Game (POMG), employing a Long Short-Term Memory (LSTM)-based Action-specific Double Deep Recurrent Q-Network (ADDRQN) that uses full sequences of historical action-observation pairs, effectively approximating latent states. Unlike prior work, we use a general-purpose simulation environment based on the Gaussian Plume Model (GPM), incorporating realistic elements such as a three-dimensional environment, sensor noise, multiple interacting agents, and multiple plume sources. The incorporation of action histories as part of the inputs further enhances the adaptability of our model in complex, partially observable environments. Extensive simulations show that our algorithm significantly outperforms conventional approaches. Specifically, our model allows agents to explore only 1.29\% of the environment to successfully locate pollution sources.

