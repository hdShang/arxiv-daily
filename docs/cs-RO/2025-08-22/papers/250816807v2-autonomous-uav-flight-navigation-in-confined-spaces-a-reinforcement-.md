---
layout: default
title: "Autonomous UAV Flight Navigation in Confined Spaces: A Reinforcement Learning Approach"
---

# Autonomous UAV Flight Navigation in Confined Spaces: A Reinforcement Learning Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16807" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16807v2</a>
  <a href="https://arxiv.org/pdf/2508.16807.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16807v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16807v2', 'Autonomous UAV Flight Navigation in Confined Spaces: A Reinforcement Learning Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marco S. Tayar, Lucas K. de Oliveira, Felipe Andrade G. Tommaselli, Juliano D. Negri, Thiago H. Segreto, Ricardo V. Godoy, Marcelo Becker

**分类**: cs.RO, cs.AI, cs.LG, eess.SY

**发布日期**: 2025-08-22 (更新: 2025-10-11)

**期刊**: 2025 Latin American Robotics Symposium (LARS)

**DOI**: [10.1109/LARS69345.2025.11273007](https://doi.org/10.1109/LARS69345.2025.11273007)

---

## 💡 一句话要点

**提出基于强化学习的无人机自主飞行导航方法以解决狭小空间中的碰撞问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无人机导航` `深度强化学习` `近端策略优化` `软演员评论家` `安全关键任务` `碰撞避免` `工业检查` `程序化环境`

## 📋 核心要点

1. 现有的无人机导航方法在狭小空间中面临碰撞风险，缺乏有效的解决方案。
2. 论文提出通过比较PPO和SAC两种强化学习算法，探索在高精度导航任务中的表现差异。
3. 实验结果显示，PPO能够稳定学习到完整的无碰撞策略，而SAC则未能成功完成任务。

## 📝 摘要（中文）

本研究针对无人机在狭小工业基础设施（如通风管道）中的自主检查任务，提出了一种基于深度强化学习的导航策略。研究比较了两种强化学习算法：近端策略优化（PPO）和软演员评论家（SAC），并探讨了它们在高精度飞行中的表现。结果表明，PPO能够稳定学习到无碰撞的导航策略，而SAC则未能找到完整解决方案，最终收敛到次优策略。这一研究表明，在安全关键的导航任务中，稳定收敛的策略比样本效率更为重要。

## 🔬 方法详解

**问题定义**：本论文旨在解决无人机在狭小空间中自主飞行导航时的碰撞问题。现有方法在高风险环境中往往无法保证稳定性和安全性，导致导航失败。

**核心思路**：论文通过比较两种强化学习算法（PPO和SAC），探讨在高精度和安全关键的导航任务中，哪种算法能够更有效地学习到无碰撞的导航策略。选择PPO作为对比的原因在于其在训练稳定性方面的优势。

**技术框架**：研究使用高保真模拟器生成程序化的通风管道环境，PPO和SAC算法分别在此环境中进行训练。整体流程包括环境建模、算法训练、策略评估等阶段。

**关键创新**：本研究的主要创新在于系统性地比较了PPO和SAC在特定任务中的表现，强调了在安全关键任务中，稳定收敛的重要性。与以往研究不同，本研究提供了明确的实证数据支持这一观点。

**关键设计**：在算法设计中，PPO采用了特定的超参数设置以确保训练的稳定性，而SAC则侧重于样本效率。损失函数的设计也有所不同，PPO使用了剪切损失函数以防止策略更新过大。

## 📊 实验亮点

实验结果显示，PPO算法在整个训练过程中成功学习到稳定的无碰撞策略，能够完成整个课程，而SAC算法则未能找到完整解决方案，仅在初始阶段表现良好，最终收敛到次优策略。这表明PPO在高精度导航任务中的优势，尤其是在安全关键的应用场景中。

## 🎯 应用场景

该研究的成果可广泛应用于工业领域的无人机自主检查，尤其是在狭小和复杂环境中，如通风管道、仓库和其他工业设施。通过提高无人机的导航精度和安全性，能够有效降低人工检查的风险和成本，提升工作效率。未来，该技术还可能扩展到其他领域，如灾后救援和环境监测等。

## 📄 摘要（原文）

> Autonomous UAV inspection of confined industrial infrastructure, such as ventilation ducts, demands robust navigation policies where collisions are unacceptable. While Deep Reinforcement Learning (DRL) offers a powerful paradigm for developing such policies, it presents a critical trade-off between on-policy and off-policy algorithms. Off-policy methods promise high sample efficiency, a vital trait for minimizing costly and unsafe real-world fine-tuning. In contrast, on-policy methods often exhibit greater training stability, which is essential for reliable convergence in hazard-dense environments. This paper directly investigates this trade-off by comparing a leading on-policy algorithm, Proximal Policy Optimization (PPO), against an off-policy counterpart, Soft Actor-Critic (SAC), for precision flight in procedurally generated ducts within a high-fidelity simulator. Our results show that PPO consistently learned a stable, collision-free policy that completed the entire course. In contrast, SAC failed to find a complete solution, converging to a suboptimal policy that navigated only the initial segments before failure. This work provides evidence that for high-precision, safety-critical navigation tasks, the reliable convergence of a well-established on-policy method can be more decisive than the nominal sample efficiency of an off-policy algorithm.

