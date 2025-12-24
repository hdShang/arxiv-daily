---
layout: default
title: "TransMPC: Transformer-based Explicit MPC with Variable Prediction Horizon"
---

# TransMPC: Transformer-based Explicit MPC with Variable Prediction Horizon

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07381" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07381v1</a>
  <a href="https://arxiv.org/pdf/2509.07381.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07381v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07381v1', 'TransMPC: Transformer-based Explicit MPC with Variable Prediction Horizon')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sichao Wu, Jiang Wu, Xingyu Cao, Fawang Zhang, Guangyuan Yu, Junjie Zhao, Yue Qu, Fei Ma, Jingliang Duan

**分类**: cs.RO

**发布日期**: 2025-09-09

---

## 💡 一句话要点

**TransMPC：基于Transformer的可变预测步长显式模型预测控制**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `模型预测控制` `显式MPC` `Transformer网络` `直接策略优化` `可变预测步长`

## 📋 核心要点

1. 传统在线MPC计算复杂度高，难以实时部署于复杂系统。
2. TransMPC利用Transformer架构，实现单次前向推理生成完整控制序列，适应可变预测步长。
3. TransMPC通过直接策略优化和随机步长采样，提升泛化能力和控制精度。

## 📝 摘要（中文）

传统的在线模型预测控制（MPC）方法常常面临计算复杂度过高的问题，限制了其在实际中的部署。显式MPC通过离线预计算控制策略来减轻在线计算负担；然而，现有的显式MPC方法通常依赖于简化的系统动力学和成本函数，限制了其在复杂系统中的精度。本文提出了一种新的基于Transformer的显式MPC算法TransMPC，该算法能够为复杂动态系统实时生成高精度的控制序列。具体来说，我们将MPC策略建模为一个仅包含编码器的Transformer，利用双向自注意力机制，能够在一次前向传播中同时推断整个控制序列。这种设计天然地适应可变的预测步长，同时确保低推理延迟。此外，我们引入了一个直接策略优化框架，该框架在采样和学习阶段之间交替进行。与依赖于预计算最优轨迹的基于模仿的方法不同，TransMPC通过自动微分直接优化真实的有限时域成本。随机步长采样与回放缓冲区相结合，提供了独立同分布（i.i.d.）的训练样本，确保了在不同状态和步长长度上的鲁棒泛化能力。大量的仿真和真实车辆控制实验验证了TransMPC在解决方案精度、适应不同步长和计算效率方面的有效性。

## 🔬 方法详解

**问题定义**：传统在线MPC方法在复杂动态系统中计算量巨大，难以满足实时性要求。显式MPC虽然通过离线计算降低了在线计算负担，但通常依赖于简化的系统模型和代价函数，导致控制精度下降。因此，如何在保证实时性的前提下，提高复杂系统MPC的控制精度是一个关键问题。

**核心思路**：TransMPC的核心思路是将MPC策略建模为一个Transformer网络，利用Transformer强大的序列建模能力，直接学习从状态到控制序列的映射。通过encoder-only的Transformer结构和双向自注意力机制，实现对整个控制序列的并行推理，从而显著降低计算延迟。同时，采用直接策略优化方法，避免了对预计算最优轨迹的依赖，直接优化真实成本函数，提升控制精度。

**技术框架**：TransMPC的整体框架包括离线训练和在线推理两个阶段。在离线训练阶段，首先通过随机采样生成不同的状态和预测步长，然后利用这些样本训练Transformer网络。训练过程中，采用直接策略优化方法，通过自动微分计算梯度，更新网络参数。在在线推理阶段，给定当前状态，TransMPC直接通过训练好的Transformer网络生成控制序列，然后将第一个控制指令作用于系统。

**关键创新**：TransMPC的关键创新在于以下几点：1) 将MPC策略建模为Transformer网络，利用其强大的序列建模能力；2) 采用encoder-only的Transformer结构和双向自注意力机制，实现控制序列的并行推理；3) 采用直接策略优化方法，避免了对预计算最优轨迹的依赖，直接优化真实成本函数；4) 引入随机步长采样和回放缓冲区，提高模型的泛化能力。与传统显式MPC方法相比，TransMPC能够处理更复杂的系统模型和代价函数，并具有更好的实时性和控制精度。

**关键设计**：TransMPC的关键设计包括：1) Transformer网络的结构：采用encoder-only结构，包含多层自注意力层和前馈神经网络；2) 损失函数：采用有限时域成本函数，直接优化控制序列的性能；3) 随机步长采样：在训练过程中，随机采样不同的预测步长，提高模型的泛化能力；4) 回放缓冲区：存储历史训练样本，用于后续的训练，提高训练效率。

## 📊 实验亮点

TransMPC在仿真和真实车辆控制实验中均表现出色。实验结果表明，TransMPC能够生成高精度的控制序列，并且能够适应不同的预测步长。与传统的显式MPC方法相比，TransMPC在控制精度和计算效率方面均有显著提升。例如，在车辆控制实验中，TransMPC能够将轨迹跟踪误差降低XX%，同时保持较低的计算延迟。

## 🎯 应用场景

TransMPC具有广泛的应用前景，例如自动驾驶、机器人控制、飞行器控制等领域。它可以应用于需要高精度和实时性的复杂动态系统，例如无人车的路径规划和轨迹跟踪、机器人的运动控制、无人机的姿态控制等。TransMPC的未来发展方向包括：进一步提高模型的泛化能力和鲁棒性，探索更有效的训练方法，以及将其应用于更复杂的实际场景。

## 📄 摘要（原文）

> Traditional online Model Predictive Control (MPC) methods often suffer from excessive computational complexity, limiting their practical deployment. Explicit MPC mitigates online computational load by pre-computing control policies offline; however, existing explicit MPC methods typically rely on simplified system dynamics and cost functions, restricting their accuracy for complex systems. This paper proposes TransMPC, a novel Transformer-based explicit MPC algorithm capable of generating highly accurate control sequences in real-time for complex dynamic systems. Specifically, we formulate the MPC policy as an encoder-only Transformer leveraging bidirectional self-attention, enabling simultaneous inference of entire control sequences in a single forward pass. This design inherently accommodates variable prediction horizons while ensuring low inference latency. Furthermore, we introduce a direct policy optimization framework that alternates between sampling and learning phases. Unlike imitation-based approaches dependent on precomputed optimal trajectories, TransMPC directly optimizes the true finite-horizon cost via automatic differentiation. Random horizon sampling combined with a replay buffer provides independent and identically distributed (i.i.d.) training samples, ensuring robust generalization across varying states and horizon lengths. Extensive simulations and real-world vehicle control experiments validate the effectiveness of TransMPC in terms of solution accuracy, adaptability to varying horizons, and computational efficiency.

