---
layout: default
title: "HALO: Human Preference Aligned Offline Reward Learning for Robot Navigation"
---

# HALO: Human Preference Aligned Offline Reward Learning for Robot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01539" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01539v1</a>
  <a href="https://arxiv.org/pdf/2508.01539.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01539v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01539v1', 'HALO: Human Preference Aligned Offline Reward Learning for Robot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gershom Seneviratne, Jianyu An, Sahire Ellahy, Kasun Weerakoon, Mohamed Bashir Elnoor, Jonathan Deepak Kannan, Amogha Thalihalla Sunil, Dinesh Manocha

**分类**: cs.RO

**发布日期**: 2025-08-03

---

## 💡 一句话要点

**提出HALO以解决机器人导航中的人类偏好对齐问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `离线奖励学习` `人类偏好对齐` `机器人导航` `专家轨迹` `Boltzmann分布` `Plackett-Luce损失` `智能决策`

## 📋 核心要点

1. 现有的机器人导航方法往往无法有效利用人类的直觉和偏好，导致导航性能不足。
2. HALO通过离线学习人类偏好的奖励模型，将专家轨迹与用户反馈结合，提升导航决策的智能性。
3. 实验结果显示，HALO在成功率上提高了至少33.3%，并在轨迹长度和Frechet距离上均有显著改善。

## 📝 摘要（中文）

本文介绍了一种新颖的离线奖励学习算法HALO，该算法将人类在导航中的直觉量化为基于视觉的奖励函数。HALO从离线数据中学习奖励模型，利用移动机器人收集的专家轨迹。在训练过程中，围绕参考动作均匀采样动作，并使用基于用户反馈的偏好分数对其进行排名。通过Plackett-Luce损失函数训练奖励模型，以与这些排名偏好对齐。实验表明，HALO在多种场景下的实际部署中，训练出的策略在未见环境中有效泛化，并在成功率、轨迹长度和Frechet距离等方面显著优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人导航中如何有效整合人类偏好与直觉的问题。现有方法在利用人类反馈方面存在不足，导致导航效果不佳。

**核心思路**：HALO通过离线数据学习奖励模型，利用专家轨迹和用户反馈来量化人类的导航偏好，从而优化机器人导航策略。

**技术框架**：HALO的整体架构包括数据收集、动作采样、偏好排名和奖励模型训练四个主要模块。首先收集专家轨迹，然后围绕参考动作进行均匀采样，接着根据用户反馈进行偏好排名，最后通过Plackett-Luce损失函数训练奖励模型。

**关键创新**：HALO的主要创新在于将人类偏好与奖励学习结合，通过Boltzmann分布和用户反馈实现了更为精准的导航决策，与传统方法相比具有显著优势。

**关键设计**：在训练过程中，动作的均匀采样和基于用户反馈的偏好评分是关键设计，Plackett-Luce损失函数用于优化奖励模型，使其更好地对齐人类偏好。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

HALO在实际部署中表现出色，相较于现有的视觉导航方法，其成功率提高了至少33.3%，轨迹长度减少了12.9%，Frechet距离降低了26.6%。这些结果表明HALO在多样化场景中的有效性和泛化能力。

## 🎯 应用场景

HALO的研究成果在机器人导航领域具有广泛的应用潜力，能够有效提升机器人在复杂环境中的自主导航能力。其方法不仅适用于移动机器人，还可扩展到其他需要人机交互的智能系统中，未来可能推动智能导航技术的进一步发展。

## 📄 摘要（原文）

> In this paper, we introduce HALO, a novel Offline Reward Learning algorithm that quantifies human intuition in navigation into a vision-based reward function for robot navigation. HALO learns a reward model from offline data, leveraging expert trajectories collected from mobile robots. During training, actions are uniformly sampled around a reference action and ranked using preference scores derived from a Boltzmann distribution centered on the preferred action, and shaped based on binary user feedback to intuitive navigation queries. The reward model is trained via the Plackett-Luce loss to align with these ranked preferences. To demonstrate the effectiveness of HALO, we deploy its reward model in two downstream applications: (i) an offline learned policy trained directly on the HALO-derived rewards, and (ii) a model-predictive-control (MPC) based planner that incorporates the HALO reward as an additional cost term. This showcases the versatility of HALO across both learning-based and classical navigation frameworks. Our real-world deployments on a Clearpath Husky across diverse scenarios demonstrate that policies trained with HALO generalize effectively to unseen environments and hardware setups not present in the training data. HALO outperforms state-of-the-art vision-based navigation methods, achieving at least a 33.3% improvement in success rate, a 12.9% reduction in normalized trajectory length, and a 26.6% reduction in Frechet distance compared to human expert trajectories.

