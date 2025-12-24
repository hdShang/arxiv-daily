---
layout: default
title: Efficient Information Updates in Compute-First Networking via Reinforcement Learning with Joint AoI and VoI
---

# Efficient Information Updates in Compute-First Networking via Reinforcement Learning with Joint AoI and VoI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06025" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06025v1</a>
  <a href="https://arxiv.org/pdf/2505.06025.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06025v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06025v1', 'Efficient Information Updates in Compute-First Networking via Reinforcement Learning with Joint AoI and VoI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianpeng Qi, Chao Liu, Chengxiang Xu, Rui Wang, Junyu Dong, Yanwei Yu

**分类**: cs.NI, cs.DC, eess.SY

**发布日期**: 2025-05-09

**备注**: 11pages, 40 figures

---

## 💡 一句话要点

**提出AVA指标以优化计算优先网络中的信息更新**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `计算优先网络` `强化学习` `信息更新` `年龄与价值感知` `服务信息传播`

## 📋 核心要点

1. 现有方法在动态用户请求和有限计算资源的情况下，难以高效传播服务信息，导致信息更新频率过高。
2. 论文提出了一种年龄与价值感知（AVA）指标，结合强化学习策略，优化服务信息的选择性更新。
3. 实验结果显示，采用AVA的更新策略在更新频率上平均减少超过90%，且不影响任务执行的准确性。

## 📝 摘要（中文）

在计算优先网络系统中，及时和高效的信息传播至关重要，尤其是在用户请求动态到达且计算资源受限的情况下。本文考虑了单源单目的系统，引入了年龄与价值感知（AVA）指标，联合捕捉服务信息的时效性和任务相关性。与传统的基于新鲜度的指标不同，AVA明确考虑了服务器端服务能力的变化和接入点（AP）的转发决策，从而实现更具上下文感知的更新评估。基于AVA，本文提出了一种基于强化学习的更新策略，旨在选择性地传输服务信息更新，以最大化任务成功率并最小化不必要的通信。大量模拟实验表明，与基线相比，AVA在更新频率上平均减少超过90%，在某些配置下甚至达到98%的减少，同时不影响任务执行的准确性和决策质量。

## 🔬 方法详解

**问题定义**：本文解决的是在计算优先网络中，如何高效传播服务信息的问题。现有方法往往忽视了信息的时效性和任务相关性，导致频繁的更新和不必要的通信开销。

**核心思路**：论文提出了年龄与价值感知（AVA）指标，旨在同时考虑信息的时效性和任务的相关性。通过强化学习，学习如何选择性地更新信息，以提高任务成功率并减少通信负担。

**技术框架**：整体架构包括信息更新的评估模块、强化学习策略模块和决策执行模块。首先，利用AVA指标评估信息的价值，然后通过强化学习算法决定是否更新信息，最后执行更新决策。

**关键创新**：最重要的创新在于引入AVA指标，该指标结合了信息的时效性和任务相关性，显著提升了信息更新的上下文感知能力，与传统方法相比，能够更有效地减少不必要的更新。

**关键设计**：在设计中，采用了特定的损失函数来平衡任务成功率和更新频率，同时强化学习模型的参数设置经过多次实验优化，以确保在不同用户请求模式下的鲁棒性。

## 📊 实验亮点

实验结果表明，采用AVA指标的更新策略在更新频率上平均减少超过90%，在某些配置下甚至达到98%的减少。这一显著提升在不影响任务执行准确性和决策质量的前提下，实现了更高效的信息传播。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、物联网设备管理和实时数据服务等。在这些场景中，及时更新信息能够显著提升系统的响应速度和效率，未来可能推动更智能的网络架构和服务优化。

## 📄 摘要（原文）

> Timely and efficient dissemination of service information is critical in compute-first networking systems, where user requests arrive dynamically and computing resources are constrained. In such systems, the access point (AP) plays a key role in forwarding user requests to a server based on its latest received service information. This paper considers a single-source, single-destination system and introduces an Age-and-Value-Aware (AVA) metric that jointly captures both the timeliness and the task relevance of service information. Unlike traditional freshness-based metrics, AVA explicitly incorporates variations in server-side service capacity and AP forwarding decisions, allowing more context-aware update evaluation. Building upon AVA, we propose a reinforcement learning-based update policy that learns to selectively transmit service information updates to the AP. It aims to maximize overall task success while minimizing unnecessary communications. Extensive simulations under diverse user request patterns and varying service capacities demonstrate that AVA reduces the update frequency by over 90% on average compared to baselines, with reductions reaching 98% in certain configurations. Crucially, this reduction is achieved without compromising the accuracy of task execution or the quality of decision making.

