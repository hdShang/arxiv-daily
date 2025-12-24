---
layout: default
title: "Latent Activation Editing: Inference-Time Refinement of Learned Policies for Safer Multirobot Navigation"
---

# Latent Activation Editing: Inference-Time Refinement of Learned Policies for Safer Multirobot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20623" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20623v1</a>
  <a href="https://arxiv.org/pdf/2509.20623.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20623v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20623v1', 'Latent Activation Editing: Inference-Time Refinement of Learned Policies for Safer Multirobot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Satyajeet Das, Darren Chiu, Zhehui Huang, Lars Lindemann, Gaurav S. Sukhatme

**分类**: cs.RO

**发布日期**: 2025-09-24

---

## 💡 一句话要点

**提出Latent Activation Editing，用于多机器人导航中强化学习策略的推理时安全优化。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `多机器人导航` `安全控制` `激活编辑` `推理时优化`

## 📋 核心要点

1. 强化学习在多无人机协同导航等复杂领域取得了显著进展，但训练好的策略在复杂环境中仍易发生碰撞。
2. 受大型语言模型激活引导和计算机视觉潜在编辑的启发，提出LAE框架，在推理时优化策略，无需修改模型权重。
3. 实验表明，LAE能显著减少碰撞次数，提高无碰撞轨迹比例，同时保持任务完成度，且适用于资源受限硬件。

## 📝 摘要（中文）

本文提出了一种推理时潜在激活编辑（LAE）框架，用于优化预训练策略的行为，无需修改其权重或架构，从而提高多无人机导航的安全性。该框架包含两个阶段：(i) 在线分类器监测中间激活，以检测与不良行为相关的状态；(ii) 激活编辑模块选择性地修改标记的激活，以将策略转移到更安全的区域。通过训练潜在碰撞世界模型来预测未来的碰撞前激活，从而促使更早和更谨慎的避障反应，以此来增强策略对风险的内部感知。大量的仿真和真实世界的Crazyflie实验表明，LAE在显著减少碰撞（与未编辑的基线相比，累积碰撞减少近90%）并大幅增加无碰撞轨迹的比例的同时，保持了任务完成度。LAE是一种轻量级范例，适用于资源受限的硬件，可用于已部署机器人策略的后部署优化。

## 🔬 方法详解

**问题定义**：多机器人导航中，即使经过良好训练的强化学习策略，在复杂环境中仍然存在碰撞风险。重新训练或微调策略以解决这些偶发但关键的安全问题，成本高昂，并且可能降低先前学习到的技能。因此，需要在不修改模型参数的情况下，提高现有策略的安全性。

**核心思路**：通过在推理时修改策略的中间激活值，引导策略朝着更安全的方向发展。核心思想是放大策略对风险的内部感知，使其能够更早、更谨慎地做出避障反应。具体来说，通过训练一个潜在碰撞世界模型，预测未来的碰撞前激活，从而实现对风险的感知增强。

**技术框架**：LAE框架包含两个主要阶段：(1) **在线分类器**：该模块监测策略的中间激活，判断当前状态是否与不良行为（如即将发生碰撞）相关联。可以使用任何合适的分类器，例如神经网络或支持向量机。(2) **激活编辑模块**：如果在线分类器检测到潜在的危险状态，该模块会选择性地修改相应的激活值。修改的目标是引导策略采取更安全的行动。

**关键创新**：LAE的关键创新在于其推理时激活编辑的能力，它允许在不修改模型权重的情况下，对已部署的强化学习策略进行微调和优化。这与传统的重新训练或微调方法不同，后者需要大量的计算资源和时间，并且可能导致策略性能的退化。LAE提供了一种轻量级、高效的策略优化方法。

**关键设计**：关键设计包括：(1) **潜在碰撞世界模型**：该模型用于预测未来的碰撞前激活，从而提供风险感知信号。模型的训练数据来自历史碰撞轨迹。(2) **激活编辑策略**：选择哪些激活进行修改，以及如何修改这些激活，是影响LAE性能的关键因素。论文中采用了一种基于梯度的激活编辑方法，根据潜在碰撞世界模型的梯度信息，调整激活值，以降低碰撞风险。(3) **在线分类器阈值**：需要仔细调整在线分类器的阈值，以平衡误报和漏报的风险。过高的阈值可能导致漏报，无法及时进行激活编辑；过低的阈值可能导致误报，不必要地修改激活值，影响策略的正常行为。

## 📊 实验亮点

实验结果表明，LAE能够显著减少多无人机导航中的碰撞次数。在仿真环境中，与未编辑的基线相比，LAE使累积碰撞次数减少了近90%。在真实世界的Crazyflie实验中，LAE也表现出显著的碰撞减少效果，同时保持了较高的任务完成率。这些结果验证了LAE在提高强化学习策略安全性方面的有效性。

## 🎯 应用场景

LAE可应用于各种机器人导航场景，特别是那些安全至关重要的场景，如无人机配送、自动驾驶和工业机器人。它还可用于其他强化学习应用，例如游戏和金融交易，以提高策略的鲁棒性和安全性。该方法尤其适用于资源受限的嵌入式系统，为已部署的机器人策略提供了一种轻量级的优化方案。

## 📄 摘要（原文）

> Reinforcement learning has enabled significant progress in complex domains such as coordinating and navigating multiple quadrotors. However, even well-trained policies remain vulnerable to collisions in obstacle-rich environments. Addressing these infrequent but critical safety failures through retraining or fine-tuning is costly and risks degrading previously learned skills. Inspired by activation steering in large language models and latent editing in computer vision, we introduce a framework for inference-time Latent Activation Editing (LAE) that refines the behavior of pre-trained policies without modifying their weights or architecture. The framework operates in two stages: (i) an online classifier monitors intermediate activations to detect states associated with undesired behaviors, and (ii) an activation editing module that selectively modifies flagged activations to shift the policy towards safer regimes. In this work, we focus on improving safety in multi-quadrotor navigation. We hypothesize that amplifying a policy's internal perception of risk can induce safer behaviors. We instantiate this idea through a latent collision world model trained to predict future pre-collision activations, thereby prompting earlier and more cautious avoidance responses. Extensive simulations and real-world Crazyflie experiments demonstrate that LAE achieves statistically significant reduction in collisions (nearly 90% fewer cumulative collisions compared to the unedited baseline) and substantially increases the fraction of collision-free trajectories, while preserving task completion. More broadly, our results establish LAE as a lightweight paradigm, feasible on resource-constrained hardware, for post-deployment refinement of learned robot policies.

