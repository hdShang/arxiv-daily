---
layout: default
title: "DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion"
---

# DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12095" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12095v1</a>
  <a href="https://arxiv.org/pdf/2506.12095.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12095v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12095v1', 'DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Khang Nguyen, An T. Le, Jan Peters, Minh Nhat Vu

**分类**: cs.RO

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出DoublyAware以解决人形机器人运动中的不确定性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `强化学习` `不确定性建模` `运动控制` `模型预测控制` `样本效率` `动态环境`

## 📋 核心要点

1. 现有方法在高维动作空间中面临环境随机性和不确定性，导致学习效率低下和稳定性差。
2. DoublyAware通过将不确定性分解为规划和策略两部分，结合符合预测和结构化政策回滚来提升学习效果。
3. 在HumanoidBench上测试后，DoublyAware显示出比传统强化学习基线更高的样本效率和更快的收敛速度。

## 📝 摘要（中文）

实现人形机器人运动的稳健学习是基于模型的强化学习中的一项基本挑战，环境中的随机性和不确定性会阻碍有效的探索和学习稳定性。本文提出DoublyAware，这是一个不确定性感知的时间差模型预测控制（TD-MPC）扩展，明确将不确定性分解为规划和策略两部分。DoublyAware通过使用量化校准的风险界限，利用符合预测来处理规划不确定性，同时通过结构化的政策回滚作为信息先验，支持学习阶段。实验结果表明，DoublyAware在HumanoidBench运动套件上表现出更高的样本效率、加快的收敛速度和增强的运动可行性。该研究强调了结构化不确定性建模在基于TD-MPC的人形运动学习中的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决人形机器人运动学习中的环境随机性和不确定性问题，现有方法在高维动作空间中难以有效探索，导致学习效率低下和稳定性不足。

**核心思路**：DoublyAware通过将不确定性分解为规划不确定性和策略不确定性，利用符合预测来过滤候选轨迹，并通过结构化政策回滚提供信息先验，从而提升学习的稳健性和效率。

**技术框架**：DoublyAware的整体架构包括两个主要模块：首先是规划模块，使用符合预测来处理规划不确定性；其次是策略模块，利用Group-Relative Policy Constraint (GRPC)优化器来支持策略学习，确保在潜在动作空间中的适应性信任区域。

**关键创新**：DoublyAware的主要创新在于明确分解不确定性为两部分，并结合符合预测和结构化政策回滚，显著提升了机器人在复杂动态环境中的决策能力。

**关键设计**：在设计中，采用量化校准的风险界限来确保统计一致性，并通过GRPC优化器设置适应性信任区域，以支持高置信度和高奖励行为的优先级。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，DoublyAware在HumanoidBench运动套件上相比于传统强化学习基线，样本效率提高了显著的比例，收敛速度加快，运动可行性增强，验证了结构化不确定性建模的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括人形机器人在复杂环境中的自主导航、运动控制和人机交互等场景。通过提升机器人在动态环境中的决策能力，DoublyAware有望在智能制造、服务机器人和娱乐等多个领域产生实际价值，并推动相关技术的发展。

## 📄 摘要（原文）

> Achieving robust robot learning for humanoid locomotion is a fundamental challenge in model-based reinforcement learning (MBRL), where environmental stochasticity and randomness can hinder efficient exploration and learning stability. The environmental, so-called aleatoric, uncertainty can be amplified in high-dimensional action spaces with complex contact dynamics, and further entangled with epistemic uncertainty in the models during learning phases. In this work, we propose DoublyAware, an uncertainty-aware extension of Temporal Difference Model Predictive Control (TD-MPC) that explicitly decomposes uncertainty into two disjoint interpretable components, i.e., planning and policy uncertainties. To handle the planning uncertainty, DoublyAware employs conformal prediction to filter candidate trajectories using quantile-calibrated risk bounds, ensuring statistical consistency and robustness against stochastic dynamics. Meanwhile, policy rollouts are leveraged as structured informative priors to support the learning phase with Group-Relative Policy Constraint (GRPC) optimizers that impose a group-based adaptive trust-region in the latent action space. This principled combination enables the robot agent to prioritize high-confidence, high-reward behavior while maintaining effective, targeted exploration under uncertainty. Evaluated on the HumanoidBench locomotion suite with the Unitree 26-DoF H1-2 humanoid, DoublyAware demonstrates improved sample efficiency, accelerated convergence, and enhanced motion feasibility compared to RL baselines. Our simulation results emphasize the significance of structured uncertainty modeling for data-efficient and reliable decision-making in TD-MPC-based humanoid locomotion learning.

