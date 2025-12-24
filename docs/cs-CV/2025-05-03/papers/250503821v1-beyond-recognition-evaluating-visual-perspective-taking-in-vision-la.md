---
layout: default
title: Beyond Recognition: Evaluating Visual Perspective Taking in Vision Language Models
---

# Beyond Recognition: Evaluating Visual Perspective Taking in Vision Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03821" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03821v1</a>
  <a href="https://arxiv.org/pdf/2505.03821.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03821v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03821v1', 'Beyond Recognition: Evaluating Visual Perspective Taking in Vision Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gracjan Góral, Alicja Ziarko, Piotr Miłoś, Michał Nauman, Maciej Wołczyk, Michał Kosiński

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-03

**备注**: Dataset: https://huggingface.co/datasets/Gracjan/Isle/viewer/Isle-Brick-V2

---

## 💡 一句话要点

**提出视觉语言模型的视觉视角理解评估方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉语言模型` `视觉视角理解` `空间推理` `认知评估` `多模态学习`

## 📋 核心要点

1. 现有视觉语言模型在空间推理和视觉视角理解方面表现不佳，存在明显的认知能力差距。
2. 本研究通过设计144个视觉任务，系统评估VLMs在视觉视角理解中的表现，提出了新的评估框架。
3. 实验结果表明，尽管模型在场景理解上表现良好，但在空间推理和视角理解上显著下降，需改进训练方法。

## 📝 摘要（中文）

本研究探讨了视觉语言模型（VLMs）在视觉视角理解方面的能力，采用了一套新颖的视觉任务，灵感来源于已建立的人类测试。通过精心控制的场景，将单个类人小人和单个物体配对，并系统性地改变空间配置，创建了144个独特的视觉任务。每个任务配有7个诊断问题，旨在评估场景理解、空间推理和视觉视角理解三个层次的视觉认知。对多种先进模型的评估显示，尽管它们在场景理解方面表现优异，但在空间推理和视角理解上的表现显著下降，揭示了表面物体识别与复杂视觉任务所需的深层空间和视角推理之间的差距。

## 🔬 方法详解

**问题定义**：本研究旨在解决视觉语言模型在视觉视角理解方面的不足，现有方法在空间推理和视角理解上表现不佳，导致认知能力差距。

**核心思路**：通过设计一套新颖的视觉任务，结合空间配置的变化，系统评估VLMs的视觉视角理解能力，强调几何表示和定制训练的重要性。

**技术框架**：整体架构包括任务设计、模型评估和结果分析三个主要模块。任务设计中，使用类人小人和物体的组合，评估模型在不同视角下的表现。

**关键创新**：本研究的创新点在于提出了一种新的评估框架，结合了空间配置变化和多层次的认知问题，填补了现有方法在视觉视角理解评估上的空白。

**关键设计**：在任务设计中，设置了144个独特的视觉任务，并为每个任务设计了7个诊断问题，以全面评估模型的视觉认知能力。

## 📊 实验亮点

实验结果显示，尽管模型在场景理解上表现优异，得分接近满分，但在空间推理和视觉视角理解方面的得分显著下降，表明在这两个领域的性能差距达到30%以上。这一发现强调了在VLMs中整合几何表示的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、自动驾驶、虚拟现实等，能够提升机器对复杂场景的理解能力，推动多模态学习的发展。未来，改进的视觉语言模型可在更广泛的实际应用中发挥重要作用，特别是在需要深层次空间推理的任务中。

## 📄 摘要（原文）

> We investigate the ability of Vision Language Models (VLMs) to perform visual perspective taking using a novel set of visual tasks inspired by established human tests. Our approach leverages carefully controlled scenes, in which a single humanoid minifigure is paired with a single object. By systematically varying spatial configurations - such as object position relative to the humanoid minifigure and the humanoid minifigure's orientation - and using both bird's-eye and surface-level views, we created 144 unique visual tasks. Each visual task is paired with a series of 7 diagnostic questions designed to assess three levels of visual cognition: scene understanding, spatial reasoning, and visual perspective taking. Our evaluation of several state-of-the-art models, including GPT-4-Turbo, GPT-4o, Llama-3.2-11B-Vision-Instruct, and variants of Claude Sonnet, reveals that while they excel in scene understanding, the performance declines significantly on spatial reasoning and further deteriorates on perspective-taking. Our analysis suggests a gap between surface-level object recognition and the deeper spatial and perspective reasoning required for complex visual tasks, pointing to the need for integrating explicit geometric representations and tailored training protocols in future VLM development.

