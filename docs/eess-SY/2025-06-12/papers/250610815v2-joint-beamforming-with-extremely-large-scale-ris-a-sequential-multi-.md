---
layout: default
title: "Joint Beamforming with Extremely Large Scale RIS: A Sequential Multi-Agent A2C Approach"
---

# Joint Beamforming with Extremely Large Scale RIS: A Sequential Multi-Agent A2C Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10815" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10815v2</a>
  <a href="https://arxiv.org/pdf/2506.10815.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10815v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10815v2', 'Joint Beamforming with Extremely Large Scale RIS: A Sequential Multi-Agent A2C Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhi Chai, Jiajie Xu, Justin P Coon, Mohamed-Slim Alouini

**分类**: eess.SY

**发布日期**: 2025-06-12 (更新: 2025-06-13)

**备注**: There are some flaws that need to be figured out

---

## 💡 一句话要点

**提出深度强化学习算法解决极大规模RIS的联合波束形成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `可重构智能表面` `波束形成` `多用户MIMO` `信道状态信息` `计算复杂度` `系统优化`

## 📋 核心要点

1. 在极大规模的RIS场景中，联合优化基站预编码和RIS相位面临计算复杂度高和性能不佳的挑战。
2. 本文提出顺序多智能体A2C算法，通过深度强化学习有效解决RIS相位和基站预编码的联合优化问题。
3. 实验结果显示，所提算法在总光谱效率上优于零强迫波束形成器，并且计算复杂度更低，表现出良好的鲁棒性。

## 📝 摘要（中文）

在RIS辅助的多用户多输入多输出（MU-MIMO）场景中，同时优化基站（BS）预编码矩阵和可重构智能表面（RIS）相位是一项具有挑战性的任务。本文提出了一种名为顺序多智能体优势演员-评论员（A2C）的深度强化学习算法来解决这一问题。研究考虑了RIS的离散相位、不完美的信道状态信息（CSI）以及用户间的信道相关性。通过对比零强迫（ZF）波束形成器，分析了所提算法的计算复杂度，并发现其计算复杂度低于基准，同时性能更优。仿真结果表明，该算法对中等信道估计误差具有鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决在极大规模可重构智能表面（RIS）下，基站（BS）预编码矩阵与RIS相位的联合优化问题。现有方法在处理复杂信道状态信息和用户间信道相关性时，计算复杂度较高且性能受限。

**核心思路**：论文提出的顺序多智能体A2C算法利用深度强化学习框架，通过多智能体协作来优化RIS相位和BS预编码，从而降低计算复杂度并提升系统性能。

**技术框架**：该算法包括多个智能体，每个智能体负责优化一个用户的RIS相位。通过与环境交互，智能体学习最优策略，最终实现全局优化。算法流程包括状态表示、动作选择、奖励计算和策略更新等主要模块。

**关键创新**：最重要的创新在于将深度强化学习应用于极大规模RIS的联合优化，尤其是在考虑不完美CSI和用户间信道相关性方面，与传统方法相比，显著提升了系统的适应性和性能。

**关键设计**：算法中采用了适应性损失函数，以平衡不同用户的需求，网络结构设计为多层深度神经网络，以增强学习能力。参数设置方面，采用了经验回放和目标网络技术，以提高训练的稳定性和效率。

## 📊 实验亮点

实验结果表明，所提A2C算法在总光谱效率上优于零强迫波束形成器，且计算复杂度降低。具体而言，所提算法在中等信道估计误差下仍能保持良好的性能，显示出其在实际应用中的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括5G及未来的6G通信系统，尤其是在高密度用户环境下的无线网络优化。通过有效的波束形成和信道优化，能够显著提升网络的传输效率和用户体验，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> It is a challenging problem to jointly optimize the base station (BS) precoding matrix and the reconfigurable intelligent surface (RIS) phases simultaneously in a RIS-assisted multiple-user multiple-input-multiple-output (MU-MIMO) scenario when the size of the RIS becomes extremely large. In this paper, we propose a deep reinforcement learning algorithm called sequential multi-agent advantage actor-critic (A2C) to solve this problem. In addition, the discrete phase of RISs, imperfect channel state information (CSI), and channel correlations between users are taken into consideration. The computational complexity is also analyzed, and the performance of the proposed algorithm is compared with the zero-forcing (ZF) beamformer in terms of the sum spectral efficiency (SE). It is noted that the computational complexity of the proposed algorithm is lower than the benchmark, while the performance is better than the benchmark. Throughout simulations, it is also found that the proposed algorithm is robust to medium channel estimation error.

