---
layout: default
title: Policy Contrastive Decoding for Robotic Foundation Models
---

# Policy Contrastive Decoding for Robotic Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13255" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13255v4</a>
  <a href="https://arxiv.org/pdf/2505.13255.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13255v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13255v4', 'Policy Contrastive Decoding for Robotic Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shihan Wu, Xu Luo, Ji Zhang, Junlin Xie, Jingkuan Song, Heng Tao Shen, Lianli Gao

**分类**: cs.RO

**发布日期**: 2025-05-19 (更新: 2025-10-18)

**🔗 代码/项目**: [PROJECT_PAGE](https://Koorye.github.io/proj/)

---

## 💡 一句话要点

**提出政策对比解码以解决机器人政策泛化能力不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人政策` `对比学习` `视觉线索` `泛化能力` `无训练方法` `政策改进` `开源实验`

## 📋 核心要点

1. 现有机器人政策容易学习到虚假关联，导致其在真实环境中的泛化能力不足。
2. 提出的政策对比解码（PCD）方法通过对比不同视觉输入的动作概率分布，引导政策关注重要的视觉线索。
3. 实验结果显示，PCD在仿真和现实环境中均显著提升了机器人政策的性能，尤其在现实环境中提升幅度达到108%。

## 📝 摘要（中文）

机器人基础模型或通用机器人政策具有极大的潜力，可以实现灵活、通用和灵巧的机器人系统。然而，实证实验表明，现有机器人政策容易从预训练轨迹中学习到虚假关联，影响其在训练数据之外的泛化能力。为此，本文提出了一种新颖的政策对比解码（PCD）方法，通过对比来自原始和对象遮蔽视觉输入的动作概率分布，引导机器人政策关注与对象相关的视觉线索。作为一种无训练的方法，PCD可以作为插件用于改进不同类型的机器人政策，而无需微调或访问模型权重。我们在三种开源机器人政策上进行了广泛实验，结果证明了PCD的灵活性和有效性，例如在仿真环境中提升了最先进政策$π_0$的性能8.9%，在现实环境中提升了108%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有机器人政策在泛化能力方面的不足，尤其是它们容易从预训练轨迹中学习到虚假关联，影响在新环境中的表现。

**核心思路**：提出的政策对比解码（PCD）方法通过对比原始视觉输入和对象遮蔽视觉输入的动作概率分布，引导机器人政策关注与任务相关的视觉信息，从而提高其泛化能力。

**技术框架**：PCD的整体架构包括数据预处理、动作概率分布计算和对比损失计算三个主要模块。首先，对输入视觉数据进行处理，生成原始和遮蔽的视觉输入；然后，计算对应的动作概率分布；最后，通过对比这两种分布来优化政策。

**关键创新**：PCD的主要创新在于其无训练特性，能够作为插件改进现有机器人政策，而无需对模型进行微调或访问权重。这一设计使得PCD具有广泛的适用性。

**关键设计**：在实现过程中，PCD使用了特定的对比损失函数来衡量原始和遮蔽输入之间的差异，确保机器人政策能够有效聚焦于与对象相关的视觉线索。

## 📊 实验亮点

实验结果显示，PCD在仿真环境中提升了最先进政策$π_0$的性能8.9%，而在现实环境中则实现了高达108%的提升。这表明PCD在不同环境下的灵活性和有效性，具有显著的实用价值。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、工业自动化和智能家居等场景。通过提高机器人政策的泛化能力，PCD能够使机器人在复杂和动态环境中更灵活地执行任务，提升其实际应用价值和用户体验。未来，随着技术的进一步发展，PCD可能会在更多领域中得到应用，推动机器人技术的进步。

## 📄 摘要（原文）

> Robotic foundation models, or generalist robot policies, hold immense potential to enable flexible, general-purpose and dexterous robotic systems. Despite their advancements, our empirical experiments reveal that existing robot policies are prone to learning spurious correlations from pre-training trajectories, adversely affecting their generalization capabilities beyond the training data. To tackle this, we propose a novel Policy Contrastive Decoding (PCD) approach, which redirects the robot policy's focus toward object-relevant visual clues by contrasting action probability distributions derived from original and object-masked visual inputs. As a training-free method, our PCD can be used as a plugin to improve different types of robot policies without needing to finetune or access model weights. We conduct extensive experiments on top of three open-source robot policies, including the autoregressive policy OpenVLA and the diffusion-based policies Octo and $π_0$. The obtained results in both simulation and real-world environments prove PCD's flexibility and effectiveness, e.g., PCD enhances the state-of-the-art policy $π_0$ by 8.9% in the simulation environment and by 108% in the real-world environment. Code and demos are publicly available at: https://Koorye.github.io/proj/PCD.

