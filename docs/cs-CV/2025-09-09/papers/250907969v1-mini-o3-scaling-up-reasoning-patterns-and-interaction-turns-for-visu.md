---
layout: default
title: "Mini-o3: Scaling Up Reasoning Patterns and Interaction Turns for Visual Search"
---

# Mini-o3: Scaling Up Reasoning Patterns and Interaction Turns for Visual Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07969" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07969v1</a>
  <a href="https://arxiv.org/pdf/2509.07969.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07969v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07969v1', 'Mini-o3: Scaling Up Reasoning Patterns and Interaction Turns for Visual Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Lai, Junyi Li, Wei Li, Tao Liu, Tianjian Li, Hengshuang Zhao

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-09-09

**备注**: Code, datasets, models are available at https://github.com/Mini-o3/Mini-o3. Project Page: https://mini-o3.github.io/

---

## 💡 一句话要点

**Mini-o3：通过扩展推理模式和交互轮数，提升视觉搜索性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉搜索` `多模态模型` `强化学习` `探索式推理` `交互式学习`

## 📋 核心要点

1. 现有开源多模态模型在视觉搜索中推理模式单调，交互轮数有限，难以应对复杂任务。
2. Mini-o3通过构建数据集、迭代数据收集和过度轮次掩蔽策略，扩展推理模式和交互轮数。
3. 实验表明，Mini-o3能生成深度推理路径，显著提升复杂视觉搜索任务的性能。

## 📝 摘要（中文）

大型多模态模型利用基于图像的工具和强化学习来解决视觉问题。然而，现有的开源方法通常表现出单调的推理模式，并且只允许有限的交互轮数，这使得它们不足以应对需要反复试验探索的困难任务。本文通过扩展基于工具的交互来解决这一限制，并引入Mini-o3，该系统执行深度、多轮推理（跨越数十步），并在具有挑战性的视觉搜索任务上实现了最先进的性能。我们的复现OpenAI o3风格行为的方法包括三个关键组成部分。首先，我们构建了Visual Probe Dataset，这是一个包含数千个具有挑战性的视觉搜索问题的集合，专为探索性推理而设计。其次，我们开发了一个迭代数据收集管道，以获得展示多样化推理模式的冷启动轨迹，包括深度优先搜索、反复试验和目标维护。第三，我们提出了一种过度轮次掩蔽策略，以防止在强化学习期间惩罚过度轮次响应（那些达到最大轮数的响应），从而平衡训练时效率与测试时可扩展性。尽管仅使用六个交互轮次的上限进行训练，但我们的模型在推理时生成自然扩展到数十轮的轨迹，并且准确性随着轮数的增加而提高。大量的实验表明，Mini-o3产生丰富的推理模式和深度思考路径，有效地解决了具有挑战性的视觉搜索问题。

## 🔬 方法详解

**问题定义**：现有开源方法在视觉搜索任务中，推理模式单一，交互轮数受限，无法进行有效的探索式推理，导致在复杂视觉搜索任务中表现不佳。痛点在于缺乏足够深度的推理能力和灵活的交互机制。

**核心思路**：Mini-o3的核心思路是通过扩展工具的使用和交互轮数，模拟人类在解决复杂视觉搜索问题时的探索过程。通过构建专门的数据集、迭代数据收集和特殊的训练策略，使模型能够学习到多样化的推理模式，并在推理时能够自适应地进行多轮交互。

**技术框架**：Mini-o3的整体框架包含三个主要部分：Visual Probe Dataset的构建，用于提供具有挑战性的视觉搜索问题；迭代数据收集管道，用于生成包含多样化推理模式的冷启动轨迹；以及基于强化学习的训练过程，其中采用了过度轮次掩蔽策略。模型通过与环境进行多轮交互，逐步缩小搜索范围，最终找到目标。

**关键创新**：Mini-o3的关键创新在于其能够突破交互轮数的限制，在训练时仅使用有限的轮数，但在推理时能够自适应地扩展到数十轮。这得益于过度轮次掩蔽策略，该策略避免了对超过预设轮数的行为进行惩罚，从而鼓励模型探索更长的推理路径。

**关键设计**：Visual Probe Dataset包含数千个具有挑战性的视觉搜索问题，涵盖了各种场景和目标。迭代数据收集管道采用人工标注和模型生成相结合的方式，确保数据的多样性和质量。过度轮次掩蔽策略通过在强化学习的损失函数中对超过最大轮数的行为进行掩蔽，避免了模型过早收敛到短路径，从而鼓励模型探索更长的推理路径。

## 📊 实验亮点

Mini-o3在视觉搜索任务上取得了显著的性能提升。尽管训练时仅使用最多6轮交互，但在推理时能够扩展到数十轮，并且准确率随着轮数的增加而提高。实验结果表明，Mini-o3能够生成丰富的推理模式和深度思考路径，有效解决了具有挑战性的视觉搜索问题。

## 🎯 应用场景

Mini-o3在视觉搜索、机器人导航、智能助手等领域具有广泛的应用前景。它可以用于开发更智能的图像搜索引擎，帮助用户快速找到所需信息。在机器人领域，它可以用于提升机器人的环境感知和自主导航能力。此外，它还可以作为智能助手的核心模块，支持更复杂的视觉任务。

## 📄 摘要（原文）

> Recent advances in large multimodal models have leveraged image-based tools with reinforcement learning to tackle visual problems. However, existing open-source approaches often exhibit monotonous reasoning patterns and allow only a limited number of interaction turns, making them inadequate for difficult tasks that require trial-and-error exploration. In this work, we address this limitation by scaling up tool-based interactions and introduce Mini-o3, a system that executes deep, multi-turn reasoning -- spanning tens of steps -- and achieves state-of-the-art performance on challenging visual search tasks. Our recipe for reproducing OpenAI o3-style behaviors comprises three key components. First, we construct the Visual Probe Dataset, a collection of thousands of challenging visual search problems designed for exploratory reasoning. Second, we develop an iterative data collection pipeline to obtain cold-start trajectories that exhibit diverse reasoning patterns, including depth-first search, trial-and-error, and goal maintenance. Third, we propose an over-turn masking strategy that prevents penalization of over-turn responses (those that hit the maximum number of turns) during reinforcement learning, thereby balancing training-time efficiency with test-time scalability. Despite training with an upper bound of only six interaction turns, our model generates trajectories that naturally scale to tens of turns at inference time, with accuracy improving as the number of turns increases. Extensive experiments demonstrate that Mini-o3 produces rich reasoning patterns and deep thinking paths, effectively solving challenging visual search problems.

