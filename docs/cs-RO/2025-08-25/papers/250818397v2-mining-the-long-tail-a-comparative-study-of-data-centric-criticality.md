---
layout: default
title: "Mining the Long Tail: A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning"
---

# Mining the Long Tail: A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18397" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18397v2</a>
  <a href="https://arxiv.org/pdf/2508.18397.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18397v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18397v2', 'Mining the Long Tail: A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonio Guillen-Perez

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-08-25 (更新: 2025-09-16)

---

## 💡 一句话要点

**提出数据驱动的关键性加权策略以解决离线强化学习中的数据不平衡问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离线强化学习` `自主驾驶` `数据不平衡` `关键性加权` `模型不确定性` `安全性提升` `长尾事件`

## 📋 核心要点

1. 现有的离线强化学习方法在处理真实世界驾驶日志时面临数据不平衡问题，导致学习到的策略不够安全和可靠。
2. 本文提出了六种关键性加权策略，分为启发式、基于不确定性和基于行为三类，以增强学习过程中的信息获取。
3. 实验结果显示，所有提出的方法均显著提升了策略的安全性，特别是基于模型不确定性的加权方法，碰撞率显著降低。

## 📝 摘要（中文）

离线强化学习（RL）为从大规模真实驾驶日志中训练自主车辆（AV）规划策略提供了有前景的范式。然而，这些日志中的极端数据不平衡，导致常见场景远多于稀有的“长尾”事件，使用标准均匀数据采样时会导致脆弱和不安全的策略。本文通过系统的大规模比较研究，提出了六种不同的关键性加权方案，旨在将学习过程集中在信息丰富的样本上。研究结果表明，所有数据策划方法显著优于基线，尤其是基于模型不确定性的策划方法，碰撞率降低近三倍（从16.0%降至5.5%）。

## 🔬 方法详解

**问题定义**：本文旨在解决离线强化学习中因数据不平衡导致的策略脆弱性问题，现有方法在处理稀有事件时效果不佳。

**核心思路**：通过引入六种关键性加权策略，集中学习信息丰富的样本，以提高模型在长尾事件上的表现。

**技术框架**：整体架构包括数据采样、关键性加权、模型训练和评估四个主要模块。采用七个目标条件的保守Q学习（CQL）代理进行训练，并在高保真Waymax模拟器中进行评估。

**关键创新**：提出的数据驱动策划方法利用模型不确定性作为信号，显著提升了策略的安全性，与传统均匀采样方法相比，表现出更好的效果。

**关键设计**：在模型训练中，采用了基于注意力机制的架构，关键性加权策略在时间步和场景层面进行评估，确保在不同时间尺度上优化策略表现。

## 📊 实验亮点

实验结果表明，所有数据策划方法均显著优于基线，尤其是基于模型不确定性的策划方法，碰撞率从16.0%降低至5.5%，实现了近三倍的安全性提升。此外，时间步层面的加权在反应安全性上表现优异，而场景层面的加权则改善了长时间规划能力。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和其他需要高安全性的自主系统。通过优化数据采样和学习策略，可以显著提升自主代理在复杂环境中的决策能力和安全性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Offline Reinforcement Learning (RL) presents a promising paradigm for training autonomous vehicle (AV) planning policies from large-scale, real-world driving logs. However, the extreme data imbalance in these logs, where mundane scenarios vastly outnumber rare "long-tail" events, leads to brittle and unsafe policies when using standard uniform data sampling. In this work, we address this challenge through a systematic, large-scale comparative study of data curation strategies designed to focus the learning process on information-rich samples. We investigate six distinct criticality weighting schemes which are categorized into three families: heuristic-based, uncertainty-based, and behavior-based. These are evaluated at two temporal scales, the individual timestep and the complete scenario. We train seven goal-conditioned Conservative Q-Learning (CQL) agents with a state-of-the-art, attention-based architecture and evaluate them in the high-fidelity Waymax simulator. Our results demonstrate that all data curation methods significantly outperform the baseline. Notably, data-driven curation using model uncertainty as a signal achieves the most significant safety improvements, reducing the collision rate by nearly three-fold (from 16.0% to 5.5%). Furthermore, we identify a clear trade-off where timestep-level weighting excels at reactive safety while scenario-level weighting improves long-horizon planning. Our work provides a comprehensive framework for data curation in Offline RL and underscores that intelligent, non-uniform sampling is a critical component for building safe and reliable autonomous agents.

