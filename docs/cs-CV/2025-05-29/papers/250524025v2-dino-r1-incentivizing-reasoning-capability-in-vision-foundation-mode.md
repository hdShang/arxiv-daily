---
layout: default
title: "DINO-R1: Incentivizing Reasoning Capability in Vision Foundation Models"
---

# DINO-R1: Incentivizing Reasoning Capability in Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24025" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24025v2</a>
  <a href="https://arxiv.org/pdf/2505.24025.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24025v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24025v2', 'DINO-R1: Incentivizing Reasoning Capability in Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenbin Pan, Wenbin He, Zhengzhong Tu, Liu Ren

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-29 (更新: 2025-08-01)

---

## 💡 一句话要点

**提出DINO-R1以增强视觉基础模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉推理` `强化学习` `查询优化` `模型训练` `多模态学习`

## 📋 核心要点

1. 现有的视觉基础模型在推理能力方面的探索相对较少，缺乏有效的训练策略来提升其视觉上下文推理能力。
2. DINO-R1通过引入GRQO策略，利用强化学习激励视觉模型的推理能力，并结合KL正则化来稳定训练过程。
3. 在多个数据集上的实验结果显示，DINO-R1在开放词汇和闭集视觉提示场景中均显著优于传统的监督微调方法。

## 📝 摘要（中文）

近年来，大型语言模型的推理能力引起了广泛关注，但视觉基础模型在这方面的探索仍然不足。本文提出DINO-R1，首次通过强化学习激励视觉上下文推理能力。DINO-R1引入了一种新颖的强化训练策略——Group Relative Query Optimization (GRQO)，该策略基于组归一化的对齐质量计算查询级奖励。此外，论文还应用KL正则化以稳定目标分布，减少训练不稳定性。通过Grounding-DINO，训练了一系列DINO-R1模型，实验结果表明其在COCO、LVIS和ODinW数据集上显著优于监督微调基线，展现了在开放词汇和闭集视觉提示场景中的强泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉基础模型在推理能力上的不足，现有方法未能有效激励模型进行视觉上下文推理，导致其在复杂任务中的表现不佳。

**核心思路**：DINO-R1通过引入GRQO策略，利用强化学习框架来激励模型的推理能力，设计了基于查询的奖励机制，以提升模型在视觉任务中的表现。

**技术框架**：DINO-R1的整体架构包括视觉提示编码器和视觉引导的查询选择机制，采用强化学习策略进行训练，结合KL正则化以增强训练稳定性。

**关键创新**：DINO-R1的主要创新在于GRQO策略的提出，它通过计算组归一化的对齐质量来生成查询级奖励，这是与现有方法的本质区别。

**关键设计**：在模型训练中，采用KL正则化来稳定目标分布，设计了特定的损失函数以减少过拟合和分布漂移，同时确保查询之间的密集和表达性监督。

## 📊 实验亮点

在COCO、LVIS和ODinW数据集上的实验结果显示，DINO-R1在开放词汇和闭集视觉提示场景中均显著优于传统的监督微调基线，具体提升幅度达到XX%，展现了强大的泛化能力和应用潜力。

## 🎯 应用场景

DINO-R1的研究成果具有广泛的应用潜力，尤其是在需要视觉推理的任务中，如图像理解、自动驾驶、智能监控等领域。通过提升视觉模型的推理能力，能够更好地支持复杂的决策过程，推动相关技术的发展和应用。未来，该方法可能会影响更多视觉任务的研究方向，促进多模态学习的进步。

## 📄 摘要（原文）

> The recent explosive interest in the reasoning capabilities of large language models, such as DeepSeek-R1, has demonstrated remarkable success through reinforcement learning-based fine-tuning frameworks, exemplified by methods like Group Relative Policy Optimization (GRPO). However, such reasoning abilities remain underexplored and notably absent in vision foundation models, including representation models like the DINO series. In this work, we propose \textbf{DINO-R1}, the first such attempt to incentivize visual in-context reasoning capabilities of vision foundation models using reinforcement learning. Specifically, DINO-R1 introduces \textbf{Group Relative Query Optimization (GRQO)}, a novel reinforcement-style training strategy explicitly designed for query-based representation models, which computes query-level rewards based on group-normalized alignment quality. We also apply KL-regularization to stabilize the objectness distribution to reduce the training instability. This joint optimization enables dense and expressive supervision across queries while mitigating overfitting and distributional drift. Building upon Grounding-DINO, we train a series of DINO-R1 family models that integrate a visual prompt encoder and a visual-guided query selection mechanism. Extensive experiments on COCO, LVIS, and ODinW demonstrate that DINO-R1 significantly outperforms supervised fine-tuning baselines, achieving strong generalization in both open-vocabulary and closed-set visual prompting scenarios.

