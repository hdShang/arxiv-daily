---
layout: default
title: "Drive As You Like: Strategy-Level Motion Planning Based on A Multi-Head Diffusion Model"
---

# Drive As You Like: Strategy-Level Motion Planning Based on A Multi-Head Diffusion Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16947" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16947v1</a>
  <a href="https://arxiv.org/pdf/2508.16947.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16947v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16947v1', 'Drive As You Like: Strategy-Level Motion Planning Based on A Multi-Head Diffusion Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Ding, Xuewen Luo, Hwa Hui Tew, Ruturaj Reddy, Xikun Wang, Junn Yong Loo

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-23

**备注**: Has been submitted to AAAI 2026

---

## 💡 一句话要点

**提出基于多头扩散模型的策略级运动规划以解决自主驾驶灵活性不足问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主驾驶` `运动规划` `扩散模型` `多头结构` `策略优化` `动态环境` `人类偏好`

## 📋 核心要点

1. 现有的自主驾驶运动规划方法在经过训练后策略固定，导致驾驶行为缺乏灵活性，无法适应动态环境和人类偏好。
2. 本文提出了一种基于扩散模型的多头轨迹规划器，通过共享权重和群体相对策略优化，实现多样化的驾驶策略。
3. 实验结果显示，所提规划器在nuPlan val14基准上表现出色，生成的轨迹具有明显多样性，满足多模态驾驶需求。

## 📝 摘要（中文）

近年来，自主驾驶的运动规划取得了显著进展，能够生成高质量的轨迹。然而，现有的规划器在经过监督训练后通常会固定其策略，导致驾驶行为一致但缺乏灵活性，无法有效反映人类偏好或适应动态指令驱动的需求。本文提出了一种基于扩散模型的多头轨迹规划器（M-diffusion planner）。在早期训练阶段，所有输出头共享权重以学习生成高质量轨迹。利用扩散模型的概率特性，我们应用了群体相对策略优化（GRPO）来微调预训练模型，以实现多样化的策略特定行为。在推理阶段，我们结合大型语言模型（LLM）来指导策略选择，实现动态的、指令感知的规划，而无需切换模型。闭环仿真表明，我们的后训练规划器在保持强大规划能力的同时，在nuPlan val14基准上达到了最先进的性能。开放式结果进一步表明，生成的轨迹展现出明显的多样性，有效满足多模态驾驶行为需求。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自主驾驶运动规划方法在训练后策略固定的问题，导致驾驶行为缺乏灵活性和适应性，无法满足动态环境下的需求。

**核心思路**：提出了一种基于扩散模型的多头轨迹规划器（M-diffusion planner），在训练初期通过共享权重生成高质量轨迹，随后利用群体相对策略优化（GRPO）微调模型以实现多样化的策略行为。

**技术框架**：整体架构包括两个主要阶段：第一阶段为共享权重的训练阶段，所有输出头共同学习生成轨迹；第二阶段为微调阶段，应用GRPO进行策略特定的优化。推理时结合大型语言模型（LLM）进行策略选择。

**关键创新**：最重要的创新在于将扩散模型与多头结构结合，利用其概率特性实现灵活的策略生成，与现有方法相比，能够更好地适应动态指令和人类偏好。

**关键设计**：在模型设计中，采用了共享权重的多头结构，损失函数设计为支持多样化轨迹生成，网络结构上结合了扩散模型的特性，以增强生成轨迹的质量和多样性。

## 📊 实验亮点

实验结果表明，所提M-diffusion planner在nuPlan val14基准上达到了最先进的性能，生成的轨迹在多样性上显著优于现有方法，能够有效满足多模态驾驶行为需求，展示出强大的规划能力。

## 🎯 应用场景

该研究的潜在应用领域包括自主驾驶、智能交通系统和机器人导航等。通过实现灵活的运动规划，该方法能够提升自主驾驶系统在复杂环境中的适应能力，满足多样化的驾驶需求，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in motion planning for autonomous driving have led to models capable of generating high-quality trajectories. However, most existing planners tend to fix their policy after supervised training, leading to consistent but rigid driving behaviors. This limits their ability to reflect human preferences or adapt to dynamic, instruction-driven demands. In this work, we propose a diffusion-based multi-head trajectory planner(M-diffusion planner). During the early training stage, all output heads share weights to learn to generate high-quality trajectories. Leveraging the probabilistic nature of diffusion models, we then apply Group Relative Policy Optimization (GRPO) to fine-tune the pre-trained model for diverse policy-specific behaviors. At inference time, we incorporate a large language model (LLM) to guide strategy selection, enabling dynamic, instruction-aware planning without switching models. Closed-loop simulation demonstrates that our post-trained planner retains strong planning capability while achieving state-of-the-art (SOTA) performance on the nuPlan val14 benchmark. Open-loop results further show that the generated trajectories exhibit clear diversity, effectively satisfying multi-modal driving behavior requirements. The code and related experiments will be released upon acceptance of the paper.

