---
layout: default
title: "RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models"
---

# RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02062" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02062v1</a>
  <a href="https://arxiv.org/pdf/2508.02062.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02062v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02062v1', 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaustubh Sridhar, Souradeep Dutta, Dinesh Jayaraman, Insup Lee

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-04

**备注**: Conference on Robot Learning 2025 (CoRL 2025), 17 pages

---

## 💡 一句话要点

**提出RICL以解决VLA模型缺乏上下文适应性的问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `上下文学习` `机器人操作` `多任务学习` `模型微调`

## 📋 核心要点

1. 现有的VLA模型在新任务和新环境中的表现虽好，但缺乏用户友好的适应性提升方法。
2. 本文提出RICL，通过少量演示数据后期注入上下文适应性，允许模型在不更新参数的情况下执行新任务。
3. 实验表明，RICL在多种操作任务中仅需20个演示便能显著提升性能，且在参数更新时效果更佳。

## 📝 摘要（中文）

多任务的“视觉-语言-动作”（VLA）模型在机器人领域展现出良好的通用性，但用户需要简单的方法来提升其性能。尽管语言和视觉模型具备上下文学习（ICL）的能力，但经过模仿学习预训练的VLA模型并不具备这种能力。本文提出了一种后期注入上下文适应性的技术RICL，允许用户通过少量（10-20个）演示来教授新任务。经过RICL处理后，模型能够利用这些演示中的相关部分进行任务执行，显著提升性能。我们在$π_{0}$-FAST VLA上应用RICL，展示了在多种新操作任务中仅需20个演示便可实现显著的性能提升，并且在可能的参数更新情况下，RICL微调进一步提高了性能。我们还发布了RICL-$π_{0}$-FAST的代码和模型权重，以便首次实现简单的上下文学习接口。

## 🔬 方法详解

**问题定义**：本文旨在解决经过模仿学习预训练的VLA模型缺乏上下文学习能力的问题。现有方法无法有效利用用户提供的少量演示来适应新任务。

**核心思路**：RICL通过后期微调和少量演示数据，注入上下文适应性，使得VLA模型能够在不进行参数更新的情况下，利用演示中的信息来执行新任务。

**技术框架**：RICL的整体架构包括数据收集、模型微调和任务执行三个主要阶段。用户提供演示数据后，模型通过特定的微调过程来增强其上下文学习能力。

**关键创新**：RICL的主要创新在于其后期注入上下文适应性的能力，允许模型在不改变参数的情况下，灵活适应新任务。这与传统的需要大量参数调整的方法形成鲜明对比。

**关键设计**：在RICL中，关键的参数设置包括演示数据的数量（10-20个），以及微调过程中使用的损失函数和优化策略。模型结构保持不变，重点在于如何有效利用现有的演示数据。

## 📊 实验亮点

实验结果显示，RICL在多种新操作任务中，仅需20个演示便能实现显著的性能提升，具体表现为在任务执行中的成功率和效率均有大幅提高。此外，当允许对目标任务演示进行参数更新时，RICL微调进一步增强了模型的表现，展现出其强大的适应能力。

## 🎯 应用场景

RICL技术具有广泛的应用潜力，尤其在机器人操作、智能家居和人机交互等领域。通过简化用户与模型之间的交互，用户可以更轻松地教授新任务，从而提升机器人在复杂环境中的适应能力和灵活性。未来，RICL可能会推动更智能的机器人系统的开发，使其能够更好地服务于人类需求。

## 📄 摘要（原文）

> Multi-task ``vision-language-action'' (VLA) models have recently demonstrated increasing promise as generalist foundation models for robotics, achieving non-trivial performance out of the box on new tasks in new environments. However, for such models to be truly useful, an end user must have easy means to teach them to improve. For language and vision models, the emergent ability to perform in-context learning (ICL) has proven to be a versatile and highly useful interface to easily teach new tasks with no parameter finetuning. Unfortunately, VLAs pre-trained with imitation learning objectives do not naturally acquire ICL abilities. In this paper, we demonstrate that, with the right finetuning recipe and a small robot demonstration dataset, it is possible to inject in-context adaptability post hoc into such a VLA. After retraining for in-context learning (RICL), our system permits an end user to provide a small number (10-20) of demonstrations for a new task. RICL then fetches the most relevant portions of those demonstrations into the VLA context to exploit ICL, performing the new task and boosting task performance. We apply RICL to inject ICL into the $π_{0}$-FAST VLA, and show that it permits large in-context improvements for a variety of new manipulation tasks with only 20 demonstrations per task, without any parameter updates. When parameter updates on the target task demonstrations is possible, RICL finetuning further boosts performance. We release code and model weights for RICL-$π_{0}$-FAST alongside the paper to enable, for the first time, a simple in-context learning interface for new manipulation tasks. Website: https://ricl-vla.github.io.

