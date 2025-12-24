---
layout: default
title: "R-Zero: Self-Evolving Reasoning LLM from Zero Data"
---

# R-Zero: Self-Evolving Reasoning LLM from Zero Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.05004" class="toolbar-btn" target="_blank">📄 arXiv: 2508.05004v2</a>
  <a href="https://arxiv.org/pdf/2508.05004.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.05004v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.05004v2', 'R-Zero: Self-Evolving Reasoning LLM from Zero Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengsong Huang, Wenhao Yu, Xiaoyang Wang, Hongming Zhang, Zongxia Li, Ruosen Li, Jiaxin Huang, Haitao Mi, Dong Yu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-07 (更新: 2025-08-27)

---

## 💡 一句话要点

**提出R-Zero以解决自我进化推理模型的数据依赖问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我进化` `大型语言模型` `无监督学习` `推理能力` `数据生成` `挑战者模型` `解决者模型` `人工智能`

## 📋 核心要点

1. 现有方法在训练自我进化模型时依赖大量人工标注数据，限制了AI系统的进步。
2. R-Zero通过自主生成训练数据，利用挑战者和解决者模型的互动，实现自我进化的推理能力提升。
3. 实验证明，R-Zero在多个基准测试中显著提高了推理能力，尤其是在数学和通用领域推理上。

## 📝 摘要（中文）

自我进化的大型语言模型（LLMs）通过自主生成、优化和学习自身经验，提供了一条可扩展的通往超智能的路径。然而，现有训练方法仍然严重依赖大量人工策划的任务和标签，这成为推动AI系统超越人类智能能力的根本瓶颈。为了解决这一限制，本文提出了R-Zero，一个完全自主的框架，从零开始生成训练数据。R-Zero从单一基础LLM出发，初始化两个独立模型，分别为挑战者和解决者。这些模型通过交互独立优化并共同进化：挑战者因提出接近解决者能力边缘的任务而获得奖励，而解决者因解决挑战者提出的日益困难的任务而获得奖励。这一过程生成了一个有针对性的、自我提升的课程，无需任何预先存在的任务和标签。实验证明，R-Zero显著提升了不同基础LLM的推理能力，例如在数学推理基准上提升了Qwen3-4B-Base +6.49，在通用领域推理基准上提升了+7.54。

## 🔬 方法详解

**问题定义**：本文旨在解决自我进化大型语言模型在训练过程中对人工标注数据的依赖问题。现有方法通常通过微调或强化学习来训练模型，导致了效率低下和能力瓶颈。

**核心思路**：R-Zero的核心思路是通过自主生成训练数据，消除对人工任务和标签的依赖。通过设置挑战者和解决者两个模型，形成一种自我进化的学习机制。

**技术框架**：R-Zero的整体架构包括两个主要模块：挑战者模型和解决者模型。挑战者负责提出任务，而解决者则尝试解决这些任务。两者通过奖励机制进行互动和优化。

**关键创新**：R-Zero的最大创新在于其完全自主的数据生成能力，通过模型间的互动实现了无监督的自我提升。这与传统依赖人工标注的训练方法本质上不同。

**关键设计**：在模型设计上，挑战者和解决者的奖励机制至关重要，挑战者提出的任务需接近解决者的能力边缘，确保任务的适应性和挑战性。

## 📊 实验亮点

实验结果显示，R-Zero在数学推理基准上提升了Qwen3-4B-Base模型的性能6.49分，在通用领域推理基准上提升了7.54分。这些结果表明R-Zero在推理能力上的显著提升，超越了传统训练方法的效果。

## 🎯 应用场景

R-Zero的研究成果在多个领域具有潜在应用价值，包括教育、游戏设计和自动化推理系统等。通过自主生成任务和学习，R-Zero能够在没有人工干预的情况下不断提升自身能力，推动智能系统的进步。

## 📄 摘要（原文）

> Self-evolving Large Language Models (LLMs) offer a scalable path toward super-intelligence by autonomously generating, refining, and learning from their own experiences. However, existing methods for training such models still rely heavily on vast human-curated tasks and labels, typically via fine-tuning or reinforcement learning, which poses a fundamental bottleneck to advancing AI systems toward capabilities beyond human intelligence. To overcome this limitation, we introduce R-Zero, a fully autonomous framework that generates its own training data from scratch. Starting from a single base LLM, R-Zero initializes two independent models with distinct roles, a Challenger and a Solver. These models are optimized separately and co-evolve through interaction: the Challenger is rewarded for proposing tasks near the edge of the Solver capability, and the Solver is rewarded for solving increasingly challenging tasks posed by the Challenger. This process yields a targeted, self-improving curriculum without any pre-existing tasks and labels. Empirically, R-Zero substantially improves reasoning capability across different backbone LLMs, e.g., boosting the Qwen3-4B-Base by +6.49 on math-reasoning benchmarks and +7.54 on general-domain reasoning benchmarks.

