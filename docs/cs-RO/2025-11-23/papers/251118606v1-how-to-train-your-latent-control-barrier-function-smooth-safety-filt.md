---
layout: default
title: "How to Train Your Latent Control Barrier Function: Smooth Safety Filtering Under Hard-to-Model Constraints"
---

# How to Train Your Latent Control Barrier Function: Smooth Safety Filtering Under Hard-to-Model Constraints

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18606" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18606v1</a>
  <a href="https://arxiv.org/pdf/2511.18606.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18606v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18606v1', 'How to Train Your Latent Control Barrier Function: Smooth Safety Filtering Under Hard-to-Model Constraints')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kensuke Nakamura, Arun L. Bishop, Steven Man, Aaron M. Johnson, Zachary Manchester, Andrea Bajcsy

**分类**: cs.RO, cs.LG

**发布日期**: 2025-11-23

**备注**: 3 figures, 10 tables, 22 pages

---

## 💡 一句话要点

**提出LatentCBF，解决难建模约束下的平滑安全滤波问题，提升视觉运动控制任务完成率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `安全滤波` `控制障碍函数` `潜在空间学习` `视觉运动控制` `强化学习`

## 📋 核心要点

1. 现有潜在安全滤波器在标称策略和安全策略间离散切换，影响了视觉运动策略的任务性能。
2. LatentCBF通过梯度惩罚实现平滑裕度函数，并混合标称和安全策略数据进行值训练。
3. 实验表明，LatentCBF实现了平滑安全滤波，任务完成率比现有方法提高了一倍。

## 📝 摘要（中文）

潜在安全滤波器扩展了Hamilton-Jacobi (HJ)可达性，使其能够基于从高维观测中直接学习到的潜在状态表示和动力学进行操作，从而在难以建模的约束下实现安全的视觉运动控制。然而，现有方法采用“最小限制”滤波，在标称策略和安全策略之间离散切换，可能损害现代视觉运动策略的价值。虽然可达性值函数原则上可以调整为控制障碍函数(CBF)以实现基于优化的平滑滤波，但我们从理论和实验上表明，当前的潜在空间学习方法产生根本上不兼容的值函数。我们确定了两种不兼容的来源：首先，在HJ可达性中，故障通过潜在空间中的“裕度函数”编码，其符号指示潜在状态是否在约束集中。然而，将裕度函数表示为分类器会产生饱和的值函数，表现出不连续的跳跃。我们证明了值函数的Lipschitz常数与裕度函数的Lipschitz常数呈线性关系，表明平滑CBF需要平滑裕度。其次，仅在安全策略数据上训练的强化学习(RL)近似会产生对标称策略动作的不准确的值估计，而这正是CBF滤波所需要的。我们提出了LatentCBF，通过梯度惩罚来解决这两个挑战，从而在没有额外标签的情况下产生平滑的裕度函数，以及一种混合来自标称策略和安全策略数据的值训练程序。在模拟基准和带有基于视觉的操作策略的硬件上的实验表明，LatentCBF能够实现平滑的安全滤波，同时使任务完成率比之前的切换方法提高了一倍。

## 🔬 方法详解

**问题定义**：论文旨在解决在难以建模的约束条件下，如何实现视觉运动控制的安全性问题。现有方法，如潜在安全滤波器，虽然能保证安全性，但采用离散切换策略，在标称策略和安全策略之间切换，这会严重影响任务的完成效率和性能，无法充分利用现代视觉运动策略的优势。现有方法学习到的潜在空间表示和值函数与平滑控制障碍函数(CBF)不兼容，导致无法进行平滑的安全滤波。

**核心思路**：论文的核心思路是设计一种新的潜在空间学习方法，使其能够生成与CBF兼容的值函数，从而实现平滑的安全滤波。具体来说，通过引入梯度惩罚来学习平滑的裕度函数，并采用混合数据训练策略来提高值函数的准确性。这样，就可以在保证安全性的同时，尽可能地利用标称策略的优势，提高任务完成率。

**技术框架**：LatentCBF的整体框架包括以下几个主要模块：1) 潜在空间学习模块，用于从高维观测数据中学习低维的潜在状态表示。2) 裕度函数学习模块，用于学习潜在空间中的裕度函数，该函数指示潜在状态是否在安全约束集内。3) 值函数学习模块，用于学习潜在状态的值函数，该函数估计在给定潜在状态下采取某个动作的长期回报。4) CBF滤波模块，利用学习到的裕度函数和值函数，对标称策略的动作进行修正，以保证安全性。

**关键创新**：论文最重要的技术创新点在于提出了两种解决值函数不兼容问题的方法：一是通过梯度惩罚来学习平滑的裕度函数，避免了值函数的不连续跳跃；二是采用混合数据训练策略，利用标称策略和安全策略的数据来训练值函数，提高了值函数对标称策略动作的估计准确性。这两种方法共同保证了学习到的值函数与CBF的兼容性，从而实现了平滑的安全滤波。

**关键设计**：1) 梯度惩罚：在裕度函数学习过程中，引入梯度惩罚项，鼓励裕度函数的梯度尽可能小，从而保证裕度函数的平滑性。2) 混合数据训练：在值函数学习过程中，混合使用来自标称策略和安全策略的数据，以提高值函数对不同动作的估计准确性。具体来说，可以采用重要性采样等方法来平衡两种数据的贡献。3) 网络结构：可以使用深度神经网络来表示潜在空间、裕度函数和值函数。网络结构的选择需要根据具体的任务和数据特点进行调整。

## 📊 实验亮点

实验结果表明，LatentCBF在模拟基准和真实机器人硬件上均取得了显著的性能提升。在视觉操作任务中，LatentCBF的任务完成率比之前的切换方法提高了一倍，同时保证了安全性。这证明了LatentCBF能够有效地解决难建模约束下的安全滤波问题，并为实际应用提供了有力的支持。

## 🎯 应用场景

该研究成果可应用于各种需要安全保障的机器人控制任务中，例如自动驾驶、无人机导航、工业机器人等。特别是在环境复杂、模型难以精确建立的场景下，LatentCBF能够有效地保证机器人的安全性，同时提高任务完成效率。未来，该方法有望推广到更广泛的控制领域，并与其他安全控制技术相结合，构建更加可靠和智能的机器人系统。

## 📄 摘要（原文）

> Latent safety filters extend Hamilton-Jacobi (HJ) reachability to operate on latent state representations and dynamics learned directly from high-dimensional observations, enabling safe visuomotor control under hard-to-model constraints. However, existing methods implement "least-restrictive" filtering that discretely switch between nominal and safety policies, potentially undermining the task performance that makes modern visuomotor policies valuable. While reachability value functions can, in principle, be adapted to be control barrier functions (CBFs) for smooth optimization-based filtering, we theoretically and empirically show that current latent-space learning methods produce fundamentally incompatible value functions. We identify two sources of incompatibility: First, in HJ reachability, failures are encoded via a "margin function" in latent space, whose sign indicates whether or not a latent is in the constraint set. However, representing the margin function as a classifier yields saturated value functions that exhibit discontinuous jumps. We prove that the value function's Lipschitz constant scales linearly with the margin function's Lipschitz constant, revealing that smooth CBFs require smooth margins. Second, reinforcement learning (RL) approximations trained solely on safety policy data yield inaccurate value estimates for nominal policy actions, precisely where CBF filtering needs them. We propose the LatentCBF, which addresses both challenges through gradient penalties that lead to smooth margin functions without additional labeling, and a value-training procedure that mixes data from both nominal and safety policy distributions. Experiments on simulated benchmarks and hardware with a vision-based manipulation policy demonstrate that LatentCBF enables smooth safety filtering while doubling the task-completion rate over prior switching methods.

