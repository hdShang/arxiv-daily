---
layout: default
title: "ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion"
---

# ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17941" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17941v1</a>
  <a href="https://arxiv.org/pdf/2509.17941.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17941v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.17941v1', 'ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zichao Hu, Chen Tang, Michael J. Munje, Yifeng Zhu, Alex Liu, Shuijing Liu, Garrett Warnell, Peter Stone, Joydeep Biswas

**分类**: cs.RO, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-09-22

**备注**: Conference on Robot Learning (CoRL) 2025 Project site: https://amrl.cs.utexas.edu/ComposableNav/

---

## 💡 一句话要点

**ComposableNav：通过可组合扩散模型实现动态环境中指令跟随导航**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `指令跟随导航` `动态环境` `扩散模型` `运动原语` `强化学习`

## 📋 核心要点

1. 现有方法难以应对指令规范的组合爆炸问题，即指令包含多个规范时，组合数量随技能集指数增长。
2. ComposableNav的核心思想是将指令分解为独立的运动原语，利用扩散模型分别学习，并在部署时并行组合。
3. 实验结果表明，ComposableNav在满足各种未见规范组合的轨迹生成方面，显著优于其他基线方法。

## 📝 摘要（中文）

本文研究了如何使机器人在动态环境中遵循指令进行导航。挑战在于指令规范的组合性质：每条指令可以包含多个规范，并且随着机器人技能集的扩展，可能的规范组合数量呈指数增长。例如，“超车行人，同时保持在道路右侧”包含两个规范：“超车行人”和“在道路右侧行走”。为了应对这一挑战，我们提出了ComposableNav，其基于这样的直觉：遵循指令涉及独立地满足其组成规范，每个规范对应于不同的运动原语。ComposableNav使用扩散模型分别学习每个原语，然后在部署时并行组合它们，以满足训练中未见过的新的规范组合。此外，为了避免对单个运动原语进行繁琐的演示，我们提出了一种两阶段训练程序：（1）监督预训练，用于学习动态导航的基础扩散模型，以及（2）强化学习微调，将基础模型塑造为不同的运动原语。通过仿真和真实世界的实验，我们表明ComposableNav能够通过生成满足各种未见规范组合的轨迹来使机器人遵循指令，显著优于非组合的基于VLM的策略和成本图组合基线。

## 🔬 方法详解

**问题定义**：论文旨在解决动态环境中机器人指令跟随导航的问题，尤其关注指令中包含多个规范时，规范组合数量爆炸带来的挑战。现有方法难以有效处理这些复杂的指令，或者需要大量的演示数据，限制了其泛化能力和实际应用。

**核心思路**：ComposableNav的核心思路是将复杂的指令分解为多个独立的运动原语，每个原语对应一个特定的规范。通过学习这些独立的运动原语，并在部署时将它们组合起来，ComposableNav能够处理训练中未见过的指令组合，从而提高泛化能力。这种组合式的策略能够有效降低学习复杂度和数据需求。

**技术框架**：ComposableNav采用两阶段训练框架。第一阶段是监督预训练，利用已有的动态导航数据训练一个基础扩散模型，使其具备基本的导航能力。第二阶段是强化学习微调，针对不同的运动原语，利用强化学习算法对基础模型进行微调，使其能够执行特定的动作，例如超车、避障、保持在道路右侧等。在部署阶段，ComposableNav根据指令中的规范，并行地组合相应的运动原语，生成最终的导航轨迹。

**关键创新**：ComposableNav的关键创新在于其可组合的扩散模型架构，以及两阶段的训练方法。通过将指令分解为独立的运动原语，ComposableNav能够有效地处理指令规范的组合爆炸问题。两阶段的训练方法则避免了对单个运动原语进行繁琐的演示，降低了数据需求。与现有方法相比，ComposableNav具有更强的泛化能力和更高的效率。

**关键设计**：在扩散模型方面，ComposableNav采用标准的扩散模型架构，并使用高斯噪声进行扩散过程。在强化学习微调方面，ComposableNav使用PPO算法，并设计了相应的奖励函数，以鼓励机器人执行特定的运动原语。具体的参数设置包括扩散模型的步数、噪声水平、PPO算法的学习率等。损失函数包括扩散模型的重构损失和PPO算法的策略损失。

## 📊 实验亮点

ComposableNav在仿真和真实世界的实验中都取得了显著的成果。在仿真环境中，ComposableNav能够成功地执行各种复杂的指令，并且显著优于非组合的基于VLM的策略和成本图组合基线。在真实世界的实验中，ComposableNav也能够成功地导航动态环境，并遵循指令完成任务。实验结果表明，ComposableNav具有很强的泛化能力和鲁棒性。

## 🎯 应用场景

ComposableNav具有广泛的应用前景，例如自动驾驶、服务机器人、物流机器人等。在自动驾驶领域，ComposableNav可以使车辆能够根据复杂的指令进行导航，例如“在保持安全距离的同时超车，并尽快到达目的地”。在服务机器人领域，ComposableNav可以使机器人能够根据用户的指令执行各种任务，例如“将物品送到指定地点，并避开障碍物”。

## 📄 摘要（原文）

> This paper considers the problem of enabling robots to navigate dynamic environments while following instructions. The challenge lies in the combinatorial nature of instruction specifications: each instruction can include multiple specifications, and the number of possible specification combinations grows exponentially as the robot's skill set expands. For example, "overtake the pedestrian while staying on the right side of the road" consists of two specifications: "overtake the pedestrian" and "walk on the right side of the road." To tackle this challenge, we propose ComposableNav, based on the intuition that following an instruction involves independently satisfying its constituent specifications, each corresponding to a distinct motion primitive. Using diffusion models, ComposableNav learns each primitive separately, then composes them in parallel at deployment time to satisfy novel combinations of specifications unseen in training. Additionally, to avoid the onerous need for demonstrations of individual motion primitives, we propose a two-stage training procedure: (1) supervised pre-training to learn a base diffusion model for dynamic navigation, and (2) reinforcement learning fine-tuning that molds the base model into different motion primitives. Through simulation and real-world experiments, we show that ComposableNav enables robots to follow instructions by generating trajectories that satisfy diverse and unseen combinations of specifications, significantly outperforming both non-compositional VLM-based policies and costmap composing baselines. Videos and additional materials can be found on the project page: https://amrl.cs.utexas.edu/ComposableNav/

