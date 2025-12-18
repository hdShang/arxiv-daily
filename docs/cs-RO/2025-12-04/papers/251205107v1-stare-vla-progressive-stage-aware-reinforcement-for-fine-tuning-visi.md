---
layout: default
title: STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models
---

# STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05107" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05107v1</a>
  <a href="https://arxiv.org/pdf/2512.05107.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05107v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.05107v1', 'STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Feng Xu, Guangyao Zhai, Xin Kong, Tingzhong Fu, Daniel F. N. Gordon, Xueli An, Benjamin Busam

**分类**: cs.RO

**发布日期**: 2025-12-04

---

## 💡 一句话要点

**提出STARE-VLA，通过阶段感知强化学习微调视觉-语言-动作模型，提升机器人操作性能。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉-语言-动作模型` `强化学习` `机器人操作` `阶段感知` `长时程任务`

## 📋 核心要点

1. 现有VLA模型在长时程任务中面临信用分配粗糙和训练不稳定的问题。
2. STARE-VLA将动作轨迹分解为语义阶段，提供阶段对齐的强化信号，实现阶段感知优化。
3. 在SimplerEnv和ManiSkill3上，STARE-VLA显著提升了任务成功率，达到SOTA水平。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型受益于大型语言模型和基于强化学习的微调，在机器人操作领域取得了显著进展。现有方法通常将长时程动作视为语言序列，并应用轨迹级优化方法，如轨迹偏好优化(TPO)或近端策略优化(PPO)，导致粗糙的信用分配和不稳定的训练。与语言不同，动作轨迹通过因果链连接的不同阶段，具有不同的学习难度。因此，我们提出了阶段感知强化(STARE)模块，将长时程动作轨迹分解为语义上有意义的阶段，并提供密集、可解释且阶段对齐的强化信号。通过将STARE集成到TPO和PPO中，我们分别得到了用于离线阶段偏好的STA-TPO和用于在线阶段内交互的STA-PPO。此外，基于监督微调作为初始化，我们提出了模仿->偏好->交互(IPI)的串行微调流程，以提高VLA模型中的动作准确性。在SimplerEnv和ManiSkill3上的实验表明，该方法取得了显著的提升，在SimplerEnv和ManiSkill3任务上分别达到了98.0%和96.4%的最先进成功率。

## 🔬 方法详解

**问题定义**：现有VLA模型在处理长时程机器人操作任务时，通常将动作序列视为统一的整体进行优化，忽略了动作序列中不同阶段的语义差异和学习难度。这种处理方式导致信用分配不准确，难以有效学习各个阶段的关键动作，最终影响整体任务的成功率。现有方法如TPO和PPO虽然在一定程度上可以优化轨迹，但无法针对性地优化不同阶段的动作。

**核心思路**：论文的核心思路是将长时程动作轨迹分解为多个语义上有意义的阶段，并为每个阶段提供独立的强化信号。通过这种阶段感知的强化学习，模型可以更准确地学习每个阶段的关键动作，从而提高整体任务的成功率。这种分解和强化方式借鉴了人类解决复杂任务的习惯，即将大任务分解为小任务，逐步完成。

**技术框架**：STARE-VLA的整体框架包含以下几个主要部分：1) 监督微调(SFT)初始化模型参数；2) 阶段感知强化(STARE)模块，用于将动作轨迹分解为阶段并生成阶段对齐的强化信号；3) 轨迹偏好优化(TPO)或近端策略优化(PPO)，用于优化策略；4) 模仿->偏好->交互(IPI)的串行微调流程，进一步提升模型性能。具体来说，STARE模块会根据预定义的阶段划分规则或学习到的阶段划分策略，将长时程动作轨迹分割成多个阶段，并为每个阶段设计相应的奖励函数，从而引导模型学习每个阶段的关键动作。

**关键创新**：STARE-VLA最重要的创新点在于提出了阶段感知的强化学习方法。与传统的轨迹级优化方法不同，STARE-VLA能够针对性地优化动作序列中的不同阶段，从而更有效地学习长时程任务。此外，IPI串行微调流程也进一步提升了模型的性能，通过模仿学习初始化模型，然后通过偏好学习和交互学习逐步优化模型。

**关键设计**：STARE模块的关键设计包括：1) 阶段划分规则，可以是预定义的或学习到的；2) 阶段奖励函数，用于引导模型学习每个阶段的关键动作；3) IPI串行微调流程，包括模仿学习、偏好学习和交互学习三个阶段。具体的奖励函数设计需要根据具体的任务进行调整，例如，可以根据动作的完成程度、与目标的距离等因素来设计奖励函数。此外，IPI流程中，模仿学习使用专家数据进行初始化，偏好学习使用人工标注的偏好数据进行优化，交互学习则通过与环境的交互进行进一步的优化。

## 📊 实验亮点

STARE-VLA在SimplerEnv和ManiSkill3两个机器人操作基准测试中取得了显著的性能提升。在SimplerEnv上，STARE-VLA达到了98.0%的成功率，超过了现有方法的最佳结果。在ManiSkill3上，STARE-VLA达到了96.4%的成功率，同样取得了SOTA水平。这些实验结果表明，STARE-VLA能够有效地提高VLA模型在长时程机器人操作任务中的性能。

## 🎯 应用场景

STARE-VLA在机器人操作领域具有广泛的应用前景，例如，可以应用于家庭服务机器人、工业机器人、医疗机器人等。该方法可以帮助机器人更好地完成复杂的长时程任务，例如，组装家具、烹饪食物、清洁房间等。此外，该方法还可以应用于虚拟环境中的智能体控制，例如，游戏AI、自动驾驶等。

## 📄 摘要（原文）

> Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

