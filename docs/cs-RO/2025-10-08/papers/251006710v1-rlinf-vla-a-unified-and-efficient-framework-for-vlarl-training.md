---
layout: default
title: RLinf-VLA: A Unified and Efficient Framework for VLA+RL Training
---

# RLinf-VLA: A Unified and Efficient Framework for VLA+RL Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.06710" class="toolbar-btn" target="_blank">📄 arXiv: 2510.06710v1</a>
  <a href="https://arxiv.org/pdf/2510.06710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.06710v1" onclick="toggleFavorite(this, '2510.06710v1', 'RLinf-VLA: A Unified and Efficient Framework for VLA+RL Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongzhi Zang, Mingjie Wei, Si Xu, Yongji Wu, Zhen Guo, Yuanqing Wang, Hao Lin, Liangzhi Shi, Yuqing Xie, Zhexuan Xu, Zhihao Liu, Kang Chen, Wenhao Tang, Quanlu Zhang, Weinan Zhang, Chao Yu, Yu Wang

**分类**: cs.RO

**发布日期**: 2025-10-08

**备注**: This is the technical report of the RLinf Team, focusing on the algorithm side. For the system-level design, please refer to arXiv:2509.15965. The open-sourced code link: https://github.com/RLinf/RLinf

---

## 💡 一句话要点

**RLinf-VLA：用于VLA+RL训练的统一高效框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言动作模型` `强化学习` `具身智能` `机器人控制` `统一框架` `高效训练` `资源分配`

## 📋 核心要点

1. 现有VLA模型主要依赖监督微调，泛化能力受限，强化学习虽有潜力，但缺乏统一的训练平台。
2. RLinf-VLA框架通过灵活的资源分配和混合流水线，高效集成渲染、训练和推理，加速VLA模型的RL训练。
3. 实验表明，RLinf-VLA在多个模拟器和任务中表现出色，并在真实机器人上展现出比SFT更强的泛化能力。

## 📝 摘要（中文）

视觉语言基础模型（VLA）的最新进展显著提升了多模态理解、推理和生成能力，激发了人们对通过视觉-语言-动作（VLA）模型将这些能力扩展到具身环境的兴趣。然而，大多数VLA模型仍然采用监督微调（SFT）进行训练，由于误差累积，SFT在分布偏移下难以泛化。强化学习（RL）通过直接优化交互中的任务性能提供了一种有希望的替代方案，但现有的尝试仍然是分散的，并且缺乏一个统一的平台，以便在模型架构和算法设计之间进行公平和系统的比较。为了解决这一差距，我们推出了RLinf-VLA，这是一个用于VLA模型可扩展RL训练的统一高效框架。该系统采用高度灵活的资源分配设计，解决了在RL+VLA训练中集成渲染、训练和推理的挑战。特别是，对于GPU并行模拟器，RLinf-VLA实现了一种新颖的混合细粒度流水线分配模式，实现了1.61x-1.88x的训练加速。通过统一的接口，RLinf-VLA无缝支持各种VLA架构（例如，OpenVLA、OpenVLA-OFT）、多种RL算法（例如，PPO、GRPO）和各种模拟器（例如，ManiSkill、LIBERO）。在模拟中，统一模型在130个LIBERO任务中实现了98.11%的成功率，在25个ManiSkill任务中实现了97.66%的成功率。除了经验性能之外，我们的研究还提炼了一套将RL应用于VLA训练的最佳实践，并阐明了这种集成中出现的新模式。此外，我们还在真实的Franka机器人上进行了初步部署，其中RL训练的策略比SFT训练的策略表现出更强的泛化能力。我们设想RLinf-VLA将成为加速和标准化具身智能研究的基础。

## 🔬 方法详解

**问题定义**：现有视觉-语言-动作（VLA）模型主要通过监督微调（SFT）训练，这种方法在面对环境变化时泛化能力较弱，容易出现误差累积。强化学习（RL）虽然可以通过与环境交互直接优化任务性能，但缺乏一个统一的平台来支持不同VLA架构和RL算法的公平比较和系统研究。

**核心思路**：RLinf-VLA的核心思路是构建一个统一且高效的框架，用于VLA模型的强化学习训练。该框架通过灵活的资源分配和优化的流水线设计，解决了在RL+VLA训练中集成渲染、训练和推理的挑战，从而加速训练过程并支持多种VLA架构和RL算法。

**技术框架**：RLinf-VLA框架包含以下主要模块：1) 资源分配模块：负责根据任务需求和硬件资源，灵活地分配计算资源给渲染、训练和推理等不同阶段。2) 混合细粒度流水线：针对GPU并行模拟器，实现了一种新的流水线模式，以提高训练效率。3) 统一接口：提供统一的接口，支持各种VLA架构（如OpenVLA、OpenVLA-OFT）、RL算法（如PPO、GRPO）和模拟器（如ManiSkill、LIBERO）。

**关键创新**：RLinf-VLA的关键创新在于其统一的框架设计和高效的资源分配策略。它通过统一的接口支持多种VLA架构、RL算法和模拟器，降低了研究人员的开发成本。此外，混合细粒度流水线能够充分利用GPU资源，显著加速训练过程。

**关键设计**：RLinf-VLA的关键设计包括：1) 混合细粒度流水线：针对GPU并行模拟器，将每个GPU的任务进一步细分，实现更高效的资源利用。2) 统一接口：通过统一的接口，简化了不同VLA架构、RL算法和模拟器的集成过程。3) 灵活的资源分配策略：根据任务需求和硬件资源，动态调整渲染、训练和推理等阶段的资源分配。

## 📊 实验亮点

RLinf-VLA框架在模拟环境中取得了显著的性能提升。在130个LIBERO任务中，统一模型实现了98.11%的成功率，在25个ManiSkill任务中实现了97.66%的成功率。此外，在真实Franka机器人上的初步部署表明，RL训练的策略比SFT训练的策略表现出更强的泛化能力，训练速度提升1.61x-1.88x。

## 🎯 应用场景

RLinf-VLA框架可广泛应用于机器人控制、自动驾驶、游戏AI等领域。它能够帮助研究人员更高效地训练具有更强泛化能力的VLA模型，从而实现更智能、更自主的机器人和智能体。该框架的统一性和高效性将加速具身智能领域的研究进展。

## 📄 摘要（原文）

> Recent progress in vision and language foundation models has significantly advanced multimodal understanding, reasoning, and generation, inspiring a surge of interest in extending such capabilities to embodied settings through vision-language-action (VLA) models. Yet, most VLA models are still trained with supervised fine-tuning (SFT), which struggles to generalize under distribution shifts due to error accumulation. Reinforcement learning (RL) offers a promising alternative by directly optimizing task performance through interaction, but existing attempts remain fragmented and lack a unified platform for fair and systematic comparison across model architectures and algorithmic designs. To address this gap, we introduce RLinf-VLA, a unified and efficient framework for scalable RL training of VLA models. The system adopts a highly flexible resource allocation design that addresses the challenge of integrating rendering, training, and inference in RL+VLA training. In particular, for GPU-parallelized simulators, RLinf-VLA implements a novel hybrid fine-grained pipeline allocation mode, achieving a 1.61x-1.88x speedup in training. Through a unified interface, RLinf-VLA seamlessly supports diverse VLA architectures (e.g., OpenVLA, OpenVLA-OFT), multiple RL algorithms (e.g., PPO, GRPO), and various simulators (e.g., ManiSkill, LIBERO). In simulation, a unified model achieves 98.11\% across 130 LIBERO tasks and 97.66\% across 25 ManiSkill tasks. Beyond empirical performance, our study distills a set of best practices for applying RL to VLA training and sheds light on emerging patterns in this integration. Furthermore, we present preliminary deployment on a real-world Franka robot, where RL-trained policies exhibit stronger generalization than those trained with SFT. We envision RLinf-VLA as a foundation to accelerate and standardize research on embodied intelligence.

