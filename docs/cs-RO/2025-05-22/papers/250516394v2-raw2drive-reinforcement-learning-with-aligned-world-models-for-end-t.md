---
layout: default
title: Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2)
---

# Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16394" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16394v2</a>
  <a href="https://arxiv.org/pdf/2505.16394.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16394v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.16394v2', 'Raw2Drive: Reinforcement Learning with Aligned World Models for End-to-End Autonomous Driving (in CARLA v2)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenjie Yang, Xiaosong Jia, Qifeng Li, Xue Yang, Maoqing Yao, Junchi Yan

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-05-22 (更新: 2025-10-25)

**备注**: Accepted by NeurIPS 2025

---

## 💡 一句话要点

**提出Raw2Drive以解决端到端自动驾驶中的训练困难问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `端到端自动驾驶` `模型驱动强化学习` `世界模型` `CARLA` `智能交通` `机器人导航`

## 📋 核心要点

1. 现有的模仿学习方法在端到端自动驾驶中面临训练困难和性能限制，强化学习的应用尚未成熟。
2. Raw2Drive通过设计双流模型，结合特权世界模型和原始传感器世界模型，解决了训练中的信息不一致问题。
3. 该方法在CARLA平台上实现了最先进的性能，成为唯一基于强化学习的端到端方法，显著提升了自动驾驶的效果。

## 📝 摘要（中文）

强化学习（RL）可以缓解模仿学习（IL）中固有的因果混淆和分布转移。然而，将RL应用于端到端自动驾驶（E2E-AD）仍然是一个开放问题，主要由于其训练难度，而IL在学术界和工业界仍是主流范式。本文提出了一种双流模型的强化学习方法Raw2Drive，通过设计特定的世界模型和引导机制，结合原始传感器数据和特权信息，有效提升了训练效果。Raw2Drive在CARLA Leaderboard 2.0和Bench2Drive上取得了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决端到端自动驾驶中强化学习应用的训练困难，现有模仿学习方法在因果推理和分布转移方面存在不足。

**核心思路**：Raw2Drive采用双流模型，首先训练一个基于特权信息的世界模型，然后通过引导机制训练原始传感器世界模型，以确保两者之间的一致性。

**技术框架**：整体架构包括两个主要模块：特权世界模型和原始传感器世界模型。特权模型用于初步规划，而原始模型则在训练过程中结合特权模型的知识进行策略优化。

**关键创新**：Raw2Drive的创新在于引入了引导机制，确保原始传感器模型与特权模型在训练过程中的一致性，这一设计显著提升了训练效率和效果。

**关键设计**：在模型设计中，采用了特定的损失函数以平衡两个模型的训练，同时在网络结构上确保了信息的有效传递和利用。

## 📊 实验亮点

在CARLA Leaderboard 2.0和Bench2Drive上，Raw2Drive实现了最先进的性能，相较于传统模仿学习方法，性能提升显著，展示了强化学习在自动驾驶领域的巨大潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车、智能交通系统和机器人导航等。通过提升端到端自动驾驶的训练效率和性能，Raw2Drive有望推动自动驾驶技术的商业化和普及，提升交通安全和效率。

## 📄 摘要（原文）

> Reinforcement Learning (RL) can mitigate the causal confusion and distribution shift inherent to imitation learning (IL). However, applying RL to end-to-end autonomous driving (E2E-AD) remains an open problem for its training difficulty, and IL is still the mainstream paradigm in both academia and industry. Recently Model-based Reinforcement Learning (MBRL) have demonstrated promising results in neural planning; however, these methods typically require privileged information as input rather than raw sensor data. We fill this gap by designing Raw2Drive, a dual-stream MBRL approach. Initially, we efficiently train an auxiliary privileged world model paired with a neural planner that uses privileged information as input. Subsequently, we introduce a raw sensor world model trained via our proposed Guidance Mechanism, which ensures consistency between the raw sensor world model and the privileged world model during rollouts. Finally, the raw sensor world model combines the prior knowledge embedded in the heads of the privileged world model to effectively guide the training of the raw sensor policy. Raw2Drive is so far the only RL based end-to-end method on CARLA Leaderboard 2.0, and Bench2Drive and it achieves state-of-the-art performance.

