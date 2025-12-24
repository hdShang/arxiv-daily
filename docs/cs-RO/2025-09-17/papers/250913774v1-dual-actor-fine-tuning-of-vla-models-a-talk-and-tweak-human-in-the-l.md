---
layout: default
title: "Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach"
---

# Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.13774" class="toolbar-btn" target="_blank">📄 arXiv: 2509.13774v1</a>
  <a href="https://arxiv.org/pdf/2509.13774.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.13774v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.13774v1', 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Piaopiao Jin, Qi Wang, Guokang Sun, Ziwen Cai, Pinjia He, Yangwei You

**分类**: cs.RO

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出人机协作的双演员微调框架以提升VLA模型的任务表现**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `人机协作` `强化学习` `多任务学习` `机器人训练` `数据生成` `实时反馈`

## 📋 核心要点

1. 现有的VLA模型在复杂的现实任务中表现不佳，尤其是在数据质量受限的情况下，传统的监督微调方法难以满足需求。
2. 本文提出了一种人机协作的双演员微调框架，结合主演员的多任务性能与精细演员的潜在空间适应能力，利用人类反馈生成新的训练数据。
3. 实验结果表明，该方法在三项任务中实现了100%的成功率，并在长时间任务中保持50%的成功率，且在多机器人训练中效率提升显著。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在机器人操作中表现出强大的泛化能力，但在复杂的现实任务中面临挑战。本文提出了一种基于强化学习的人机协作双演员微调框架，集成了一个主演员用于多任务性能的稳健性和一个精细演员用于潜在空间的适应。我们引入了一种轻量级的“谈话与调整”方案，将人类的修正转化为语义化的语言指令，从而生成新的数据集用于策略学习。在实际的多任务实验中，该方法在101分钟的在线微调内实现了三项任务的100%成功率，并在长时间任务中保持了12次连续操作的50%成功率。此外，该框架在多机器人训练中有效扩展，使用双机器人时效率提升可达2倍。

## 🔬 方法详解

**问题定义**：本文旨在解决VLA模型在复杂现实任务中的表现不足，尤其是在数据质量不高的情况下，传统的监督微调方法效果有限。

**核心思路**：提出一种人机协作的双演员微调框架，通过主演员和精细演员的协同工作，利用人类的实时反馈来优化模型性能。

**技术框架**：框架包括两个主要模块：主演员负责执行多任务操作，精细演员则进行潜在空间的调整。此外，框架中引入了“谈话与调整”机制，将人类的修正转化为语言指令。

**关键创新**：最重要的创新在于将人类反馈转化为语义化的语言指令，从而生成新的数据集用于策略学习，这一方法与传统的监督学习显著不同。

**关键设计**：在设计中，采用了轻量级的语言处理模块，并在损失函数中引入了人类反馈的权重，以增强模型对人类指令的适应性。

## 📊 实验亮点

实验结果显示，该方法在三项任务中实现了100%的成功率，且在长时间任务中保持50%的成功率。使用双机器人进行训练时，效率提升可达2倍，展示了该框架在多机器人协作中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化生产线和人机协作系统。通过提升VLA模型在复杂任务中的表现，该框架能够在实际操作中提供更高的灵活性和效率，未来可能推动更多领域的智能化进程。

## 📄 摘要（原文）

> Vision-language-action (VLA) models demonstrate strong generalization in robotic manipulation but face challenges in complex, real-world tasks. While supervised fine-tuning with demonstrations is constrained by data quality, reinforcement learning (RL) offers a promising alternative. We propose a human-in-the-loop dual-actor fine-tuning framework grounded in RL. The framework integrates a primary actor for robust multi-task performance with a refinement actor for latent-space adaptation. Beyond standard physical interventions, we introduce a lightweight talk-and-tweak scheme that converts human corrections into semantically grounded language commands, thereby generating a new dataset for policy learning. In real-world multi-task experiments, our approach achieves 100% success across three tasks within 101 minutes of online fine-tuning. For long-horizon tasks, it sustains a 50% success rate over 12 consecutive operations. Furthermore, the framework scales effectively to multi-robot training, achieving up to a 2 times improvement in efficiency when using dual robots. The experiment videos are available at https://sites.google.com/view/hil-daft/.

