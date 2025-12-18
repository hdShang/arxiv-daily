---
layout: default
title: Flow-Opt: Scalable Centralized Multi-Robot Trajectory Optimization with Flow Matching and Differentiable Optimization
---

# Flow-Opt: Scalable Centralized Multi-Robot Trajectory Optimization with Flow Matching and Differentiable Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09204" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09204v1</a>
  <a href="https://arxiv.org/pdf/2510.09204.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09204v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.09204v1', 'Flow-Opt: Scalable Centralized Multi-Robot Trajectory Optimization with Flow Matching and Differentiable Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simon Idoko, Arun Kumar Singh

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-10

---

## 💡 一句话要点

**Flow-Opt：基于流匹配和可微优化的可扩展集中式多机器人轨迹优化**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多机器人轨迹优化` `集中式规划` `流匹配` `扩散模型` `可微优化`

## 📋 核心要点

1. 集中式多机器人轨迹优化计算复杂度高，难以扩展到大规模机器人集群和复杂环境。
2. Flow-Opt通过学习生成模型采样候选轨迹，并使用可微安全滤波器快速满足约束，降低计算成本。
3. 实验表明，Flow-Opt能快速生成大量机器人的平滑轨迹，并支持批量处理，性能优于现有方法。

## 📝 摘要（中文）

本文提出Flow-Opt，一种基于学习的方法，旨在提高集中式多机器人轨迹优化的计算效率。该方法将问题分解为：首先学习一个生成模型来采样不同的候选轨迹，然后使用学习到的安全滤波器(SF)来确保快速的推理时约束满足。我们提出了一个带有扩散Transformer (DiT)的流匹配模型作为生成模型，并用置换不变的机器人位置和地图编码器进行增强。我们为SF开发了一个定制求解器，并配备了一个神经网络来预测上下文相关的初始化。初始化网络以自监督的方式进行训练，利用SF求解器的可微性。我们的方法在以下方面推进了现有技术水平：在杂乱环境中，可以在几十毫秒内生成数十个机器人的轨迹，比现有的集中式优化方法快数倍。此外，与基于扩散模型的竞争基线相比，我们的方法能够更快地生成更平滑的轨迹。其次，我们方法的每个组件都可以进行批处理，从而可以在不到一秒的时间内解决几十个问题实例。最后，我们的方法可以在给定的起点和终点位置之间生成不同的轨迹集，从而捕获不同的避碰行为。

## 🔬 方法详解

**问题定义**：集中式多机器人轨迹优化旨在找到一组无碰撞的、平滑的轨迹，使得多个机器人能够从起始位置到达目标位置。然而，随着机器人数量的增加和环境复杂度的提高，计算复杂度呈指数级增长，现有方法难以扩展到大规模场景。现有方法的痛点在于计算量大，难以满足实时性要求。

**核心思路**：Flow-Opt的核心思路是将轨迹优化问题分解为两个阶段：轨迹生成和安全过滤。首先，使用一个生成模型（基于流匹配的扩散Transformer）生成多个候选轨迹。然后，使用一个学习到的安全滤波器快速评估和修正这些轨迹，以确保满足约束条件（如避免碰撞）。这种分解降低了优化问题的复杂度，提高了计算效率。

**技术框架**：Flow-Opt的整体框架包括以下几个主要模块：1) **轨迹生成器**：基于流匹配的扩散Transformer (DiT)，用于生成候选轨迹。该模型接收机器人位置和地图信息作为输入，并生成满足起点和终点约束的轨迹。2) **安全滤波器 (SF)**：一个定制的求解器，用于评估和修正候选轨迹，确保满足安全约束。3) **初始化网络**：一个神经网络，用于预测SF求解器的上下文相关的初始化，加速求解过程。该网络以自监督的方式进行训练，利用SF求解器的可微性。

**关键创新**：Flow-Opt的关键创新在于将生成模型和可微优化相结合，实现高效的轨迹优化。具体来说，使用流匹配模型生成轨迹，并利用安全滤波器的可微性进行自监督学习，从而加速优化过程。此外，该方法支持批量处理，可以同时解决多个问题实例，进一步提高了计算效率。与现有方法的本质区别在于，Flow-Opt不是直接求解优化问题，而是通过学习来近似最优解，从而降低了计算复杂度。

**关键设计**：1) **流匹配模型**：使用扩散Transformer (DiT)作为生成模型，并用置换不变的机器人位置和地图编码器进行增强，以提高模型的泛化能力。2) **安全滤波器**：开发了一个定制的求解器，并配备了一个神经网络来预测上下文相关的初始化，加速求解过程。3) **自监督学习**：利用安全滤波器的可微性，以自监督的方式训练初始化网络，避免了人工标注数据的需要。4) **损失函数**：使用了流匹配损失函数来训练生成模型，并使用约束违反程度作为安全滤波器的损失函数。

## 📊 实验亮点

Flow-Opt在杂乱环境中，可以在几十毫秒内生成数十个机器人的轨迹，速度比现有的集中式优化方法快数倍。与基于扩散模型的竞争基线相比，Flow-Opt能够更快地生成更平滑的轨迹。此外，Flow-Opt支持批量处理，可以在不到一秒的时间内解决几十个问题实例，这是现有方法无法实现的。

## 🎯 应用场景

Flow-Opt适用于大规模多机器人协同作业的场景，例如仓库自动化、物流配送、农业机器人集群、以及搜索救援等。该方法能够快速生成安全、平滑的轨迹，提高机器人集群的作业效率和安全性。未来，该研究可以扩展到动态环境和更复杂的约束条件，进一步提升多机器人系统的智能化水平。

## 📄 摘要（原文）

> Centralized trajectory optimization in the joint space of multiple robots allows access to a larger feasible space that can result in smoother trajectories, especially while planning in tight spaces. Unfortunately, it is often computationally intractable beyond a very small swarm size. In this paper, we propose Flow-Opt, a learning-based approach towards improving the computational tractability of centralized multi-robot trajectory optimization. Specifically, we reduce the problem to first learning a generative model to sample different candidate trajectories and then using a learned Safety-Filter(SF) to ensure fast inference-time constraint satisfaction. We propose a flow-matching model with a diffusion transformer (DiT) augmented with permutation invariant robot position and map encoders as the generative model. We develop a custom solver for our SF and equip it with a neural network that predicts context-specific initialization. The initialization network is trained in a self-supervised manner, taking advantage of the differentiability of the SF solver. We advance the state-of-the-art in the following respects. First, we show that we can generate trajectories of tens of robots in cluttered environments in a few tens of milliseconds. This is several times faster than existing centralized optimization approaches. Moreover, our approach also generates smoother trajectories orders of magnitude faster than competing baselines based on diffusion models. Second, each component of our approach can be batched, allowing us to solve a few tens of problem instances in a fraction of a second. We believe this is a first such result; no existing approach provides such capabilities. Finally, our approach can generate a diverse set of trajectories between a given set of start and goal locations, which can capture different collision-avoidance behaviors.

