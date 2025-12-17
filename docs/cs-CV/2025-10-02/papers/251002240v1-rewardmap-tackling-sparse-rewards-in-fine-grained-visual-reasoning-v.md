---
layout: default
title: RewardMap: Tackling Sparse Rewards in Fine-grained Visual Reasoning via Multi-Stage Reinforcement Learning
---

# RewardMap: Tackling Sparse Rewards in Fine-grained Visual Reasoning via Multi-Stage Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02240" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02240v1</a>
  <a href="https://arxiv.org/pdf/2510.02240.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02240v1" onclick="toggleFavorite(this, '2510.02240v1', 'RewardMap: Tackling Sparse Rewards in Fine-grained Visual Reasoning via Multi-Stage Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sicheng Feng, Kaiwen Tuo, Song Wang, Lingdong Kong, Jianke Zhu, Huan Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-02

---

## 💡 一句话要点

**提出RewardMap，通过多阶段强化学习解决细粒度视觉推理中的稀疏奖励问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细粒度视觉推理` `多模态大语言模型` `强化学习` `稀疏奖励` `多阶段学习`

## 📋 核心要点

1. 多模态大语言模型在细粒度视觉推理，尤其是在复杂空间推理任务中，面临稀疏奖励和优化不稳定的挑战。
2. RewardMap通过难度感知奖励设计和多阶段强化学习，从简单感知到复杂推理，有效解决稀疏奖励问题并提升模型性能。
3. 实验表明，RewardMap在多个基准测试中显著提升了模型的视觉理解和推理能力，平均提升3.47%。

## 📝 摘要（中文）

本文针对多模态大语言模型(MLLM)在细粒度视觉推理方面的挑战，特别是ReasonMap提出的在交通地图等结构化和信息丰富的环境中进行空间推理的难题，提出了RewardMap框架。该框架旨在解决标准强化学习在此类任务中面临的稀疏奖励和优化不稳定的问题。首先，构建了ReasonMap-Plus数据集，通过视觉问答(VQA)任务引入密集奖励信号，实现细粒度视觉理解技能的有效冷启动训练。其次，提出了RewardMap，一个多阶段强化学习框架，旨在提高MLLM的视觉理解和推理能力。RewardMap包含难度感知奖励设计，通过细节奖励直接解决稀疏奖励问题，并提供更丰富的监督。此外，还提出了一个多阶段RL方案，从简单的感知任务到复杂的推理任务进行引导训练，提供比传统监督微调(SFT)更有效的冷启动策略。在ReasonMap和ReasonMap-Plus上的实验表明，RewardMap的每个组成部分都有助于性能的持续提升，而它们的组合产生了最佳结果。此外，使用RewardMap训练的模型在涵盖空间推理、细粒度视觉推理以及超出交通地图的通用任务的6个基准测试中，平均提高了3.47%，突出了增强的视觉理解和推理能力。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大语言模型在细粒度视觉推理任务中，由于奖励稀疏导致强化学习训练困难的问题。现有方法，如直接应用强化学习，在复杂任务中难以获得有效的奖励信号，导致模型难以学习。ReasonMap数据集进一步突出了现有模型在空间推理方面的不足。

**核心思路**：论文的核心思路是通过引入密集奖励和多阶段学习策略，克服稀疏奖励带来的挑战。密集奖励通过VQA任务提供更丰富的监督信号，多阶段学习则将复杂的推理任务分解为多个难度递增的阶段，使模型能够逐步学习和提升能力。这样设计能够更有效地引导模型学习，并避免陷入局部最优。

**技术框架**：RewardMap框架包含两个主要组成部分：难度感知奖励设计和多阶段强化学习方案。难度感知奖励设计通过引入细节奖励，为模型提供更细粒度的反馈，从而缓解奖励稀疏的问题。多阶段强化学习方案则将训练过程分解为多个阶段，每个阶段侧重于不同的能力，例如从简单的感知到复杂的推理。整体流程是从ReasonMap-Plus数据集上进行预训练，然后通过多阶段强化学习在ReasonMap数据集上进行微调。

**关键创新**：论文的关键创新在于将难度感知奖励设计和多阶段强化学习方案相结合，以解决细粒度视觉推理中的稀疏奖励问题。与传统的单阶段强化学习方法相比，RewardMap能够更有效地引导模型学习，并取得更好的性能。难度感知奖励设计能够提供更丰富的监督信号，而多阶段强化学习方案则能够使模型逐步学习和提升能力。

**关键设计**：难度感知奖励设计中，细节奖励的权重需要仔细调整，以平衡整体奖励的稀疏性和细节奖励的丰富性。多阶段强化学习方案中，每个阶段的任务难度需要逐步增加，以保证模型能够逐步学习和提升能力。此外，还需要选择合适的强化学习算法，例如PPO或SAC，并调整相应的超参数，以获得最佳的训练效果。

## 📊 实验亮点

RewardMap在ReasonMap和ReasonMap-Plus数据集上取得了显著的性能提升。具体而言，RewardMap的每个组成部分都对性能提升做出了贡献，而它们的组合产生了最佳结果。此外，使用RewardMap训练的模型在涵盖空间推理、细粒度视觉推理以及超出交通地图的通用任务的6个基准测试中，平均提高了3.47%，证明了其增强的视觉理解和推理能力。

## 🎯 应用场景

该研究成果可应用于各种需要细粒度视觉推理的场景，例如智能交通、机器人导航、医学图像分析等。通过提升模型在复杂环境中的推理能力，可以实现更智能、更可靠的自动化系统。例如，在智能交通领域，可以帮助自动驾驶车辆更好地理解交通地图，从而做出更安全的决策。

## 📄 摘要（原文）

> Fine-grained visual reasoning remains a core challenge for multimodal large language models (MLLMs). The recently introduced ReasonMap highlights this gap by showing that even advanced MLLMs struggle with spatial reasoning in structured and information-rich settings such as transit maps, a task of clear practical and scientific importance. However, standard reinforcement learning (RL) on such tasks is impeded by sparse rewards and unstable optimization. To address this, we first construct ReasonMap-Plus, an extended dataset that introduces dense reward signals through Visual Question Answering (VQA) tasks, enabling effective cold-start training of fine-grained visual understanding skills. Next, we propose RewardMap, a multi-stage RL framework designed to improve both visual understanding and reasoning capabilities of MLLMs. RewardMap incorporates two key designs. First, we introduce a difficulty-aware reward design that incorporates detail rewards, directly tackling the sparse rewards while providing richer supervision. Second, we propose a multi-stage RL scheme that bootstraps training from simple perception to complex reasoning tasks, offering a more effective cold-start strategy than conventional Supervised Fine-Tuning (SFT). Experiments on ReasonMap and ReasonMap-Plus demonstrate that each component of RewardMap contributes to consistent performance gains, while their combination yields the best results. Moreover, models trained with RewardMap achieve an average improvement of 3.47% across 6 benchmarks spanning spatial reasoning, fine-grained visual reasoning, and general tasks beyond transit maps, underscoring enhanced visual understanding and reasoning capabilities.

