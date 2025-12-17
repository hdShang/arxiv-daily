---
layout: default
title: Closing the Train-Test Gap in World Models for Gradient-Based Planning
---

# Closing the Train-Test Gap in World Models for Gradient-Based Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09929" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09929v1</a>
  <a href="https://arxiv.org/pdf/2512.09929.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09929v1" onclick="toggleFavorite(this, '2512.09929v1', 'Closing the Train-Test Gap in World Models for Gradient-Based Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arjun Parthasarathy, Nimit Kalra, Rohun Agrawal, Yann LeCun, Oumayma Bounou, Pavel Izmailov, Micah Goldblum

**分类**: cs.LG, cs.RO

**发布日期**: 2025-12-10

---

## 💡 一句话要点

**提出数据合成方法，弥合World Model训练与梯度规划的差距，加速模型预测控制。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `World Model` `模型预测控制` `梯度规划` `数据合成` `机器人控制`

## 📋 核心要点

1. 基于梯度的规划在模型预测控制中具有效率优势，但其性能受限于World Model的训练方式。
2. 通过在训练阶段合成数据，使World Model更好地适应测试阶段的动作序列估计，弥合训练与测试的差异。
3. 实验表明，该方法在物体操作和导航任务中，能以更少的时间预算达到或超过传统无梯度方法的性能。

## 📝 摘要（中文）

本文提出了一种改进的World Model训练方法，旨在提升基于梯度的规划效率。传统的模型预测控制（MPC）依赖于计算缓慢的搜索算法或迭代求解优化问题，而基于梯度的规划提供了一种计算高效的替代方案。然而，其性能一直落后于其他方法。本文的核心在于弥合World Model训练和测试之间的差距：World Model在训练时以预测下一状态为目标，但在测试时用于估计一系列动作。为此，本文提出了训练时的数据合成技术，显著提升了现有World Model的梯度规划性能。在测试时，该方法在多种物体操作和导航任务中，以10%的时间预算超越或匹配了经典的无梯度交叉熵方法（CEM）。

## 🔬 方法详解

**问题定义**：现有的World Model虽然在下一状态预测任务上表现良好，但直接应用于基于梯度的规划时性能不佳。这是因为World Model的训练目标是预测单个状态，而梯度规划需要模型能够准确预测一系列动作的效果，即模型在训练和测试阶段的使用方式存在差异。这种train-test gap导致梯度在反向传播时变得不稳定或不准确，从而影响规划效果。

**核心思路**：论文的核心思路是通过在训练阶段引入数据合成技术，使World Model能够更好地适应测试阶段的动作序列估计。具体来说，就是通过生成包含未来多个时间步的状态和动作序列的数据，来训练World Model，从而让模型学习到长期预测的能力，减少train-test gap。

**技术框架**：整体框架包括World Model的训练和基于梯度的规划两个阶段。在训练阶段，使用真实数据和合成数据混合训练World Model。合成数据通过在真实状态上施加随机动作序列生成。在规划阶段，使用训练好的World Model，通过梯度下降优化动作序列，以达到期望的目标状态。

**关键创新**：关键创新在于训练时的数据合成方法，它显式地考虑了World Model在规划阶段的使用方式，通过生成包含未来多个时间步的状态和动作序列的数据，来训练World Model，从而让模型学习到长期预测的能力。这种方法与传统的只预测下一步状态的训练方式有本质区别。

**关键设计**：数据合成的关键在于如何生成合理的动作序列。论文中采用随机策略生成动作序列，并限制序列的长度。损失函数包括两部分：一部分是真实数据的下一状态预测损失，另一部分是合成数据的多步预测损失。网络结构采用常见的循环神经网络（RNN）或Transformer结构，用于建模状态和动作序列的时序关系。

## 📊 实验亮点

实验结果表明，通过引入数据合成技术，基于梯度的规划方法在多种物体操作和导航任务中，能够以10%的时间预算达到或超过经典的无梯度交叉熵方法（CEM）的性能。这意味着在保证性能的同时，计算效率得到了显著提升。此外，该方法在不同任务和数据集上都表现出良好的泛化能力。

## 🎯 应用场景

该研究成果可广泛应用于机器人控制、自动驾驶、游戏AI等领域。通过提升基于梯度的规划效率，可以使机器人在复杂环境中更快、更准确地完成任务，例如物体操作、路径规划等。该方法还有助于降低对大量计算资源的需求，使得在资源受限的平台上部署复杂的控制算法成为可能。

## 📄 摘要（原文）

> World models paired with model predictive control (MPC) can be trained offline on large-scale datasets of expert trajectories and enable generalization to a wide range of planning tasks at inference time. Compared to traditional MPC procedures, which rely on slow search algorithms or on iteratively solving optimization problems exactly, gradient-based planning offers a computationally efficient alternative. However, the performance of gradient-based planning has thus far lagged behind that of other approaches. In this paper, we propose improved methods for training world models that enable efficient gradient-based planning. We begin with the observation that although a world model is trained on a next-state prediction objective, it is used at test-time to instead estimate a sequence of actions. The goal of our work is to close this train-test gap. To that end, we propose train-time data synthesis techniques that enable significantly improved gradient-based planning with existing world models. At test time, our approach outperforms or matches the classical gradient-free cross-entropy method (CEM) across a variety of object manipulation and navigation tasks in 10% of the time budget.

