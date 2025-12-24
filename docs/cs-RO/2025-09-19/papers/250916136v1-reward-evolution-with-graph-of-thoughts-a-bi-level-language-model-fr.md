---
layout: default
title: "Reward Evolution with Graph-of-Thoughts: A Bi-Level Language Model Framework for Reinforcement Learning"
---

# Reward Evolution with Graph-of-Thoughts: A Bi-Level Language Model Framework for Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16136" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16136v1</a>
  <a href="https://arxiv.org/pdf/2509.16136.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16136v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16136v1', 'Reward Evolution with Graph-of-Thoughts: A Bi-Level Language Model Framework for Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changwei Yao, Xinzi Liu, Chen Li, Marios Savvides

**分类**: cs.RO

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出RE-GoT框架，利用图推理和视觉反馈实现强化学习中奖励函数的自动进化。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `奖励函数设计` `大型语言模型` `视觉语言模型` `图推理` `自主进化` `机器人操作` `任务分解`

## 📋 核心要点

1. 现有基于LLM的奖励函数设计方法存在幻觉问题，依赖人工反馈，且难以处理复杂多步任务。
2. RE-GoT框架利用图结构分解任务，结合视觉语言模型进行自动评估和迭代优化奖励函数。
3. 实验表明，RE-GoT在RoboGen和ManiSkill2任务上显著优于现有方法，尤其在复杂任务上提升明显。

## 📝 摘要（中文）

设计有效的奖励函数是强化学习（RL）中的一个主要挑战，通常需要大量的人工专业知识和迭代改进。最近的研究利用大型语言模型（LLM）进行自动奖励设计，但这些方法受到幻觉、依赖人工反馈以及处理复杂、多步骤任务的挑战的限制。本文介绍了一种新的双层框架——基于图推理的奖励进化（RE-GoT），该框架通过结构化的基于图的推理增强了LLM，并集成了视觉语言模型（VLM）以进行自动rollout评估。RE-GoT首先将任务分解为文本属性图，从而实现全面的分析和奖励函数生成，然后使用来自VLM的视觉反馈迭代地改进奖励，无需人工干预。在10个RoboGen和4个ManiSkill2任务上的大量实验表明，RE-GoT始终优于现有的基于LLM的基线。在RoboGen上，我们的方法将平均任务成功率提高了32.25%，在复杂的多步骤任务上取得了显著的提升。在ManiSkill2上，RE-GoT在四个不同的操作任务中实现了93.73%的平均成功率，显著超过了先前的基于LLM的方法，甚至超过了专家设计的奖励。我们的结果表明，将LLM和VLM与图推理相结合，为RL中的自主奖励进化提供了一个可扩展且有效的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决强化学习中奖励函数设计难题，现有基于LLM的方法存在幻觉、依赖人工反馈、难以处理复杂任务等痛点，限制了其在实际机器人任务中的应用。

**核心思路**：核心思路是将任务分解为图结构，利用图推理能力增强LLM对任务的理解，并引入VLM进行视觉反馈，实现奖励函数的自动评估和迭代优化，从而避免人工干预和幻觉问题。

**技术框架**：RE-GoT是一个双层框架。第一层，利用LLM将任务分解为文本属性图（Graph-of-Thoughts），每个节点代表任务的一个步骤或状态，边表示步骤之间的关系。第二层，利用VLM对rollout结果进行视觉评估，并根据评估结果迭代优化奖励函数。整个过程无需人工干预。

**关键创新**：关键创新在于结合了图推理和视觉反馈，利用图结构增强LLM的推理能力，使其能够更好地理解复杂任务，并利用VLM的视觉感知能力进行自动评估，从而实现奖励函数的自主进化。与现有方法相比，RE-GoT无需人工反馈，且能更好地处理复杂多步任务。

**关键设计**：RE-GoT使用LLM（例如GPT-4）进行任务分解和奖励函数生成。VLM用于评估rollout结果，并生成反馈信号。奖励函数的优化采用迭代的方式，根据VLM的反馈信号调整奖励函数的参数。具体的参数设置和网络结构细节在论文中进行了详细描述（此处未知具体细节）。

## 📊 实验亮点

RE-GoT在RoboGen任务上平均成功率提升32.25%，尤其在复杂多步任务上提升显著。在ManiSkill2任务上，RE-GoT取得了93.73%的平均成功率，超过了现有基于LLM的方法，甚至超越了专家设计的奖励函数。这些结果表明RE-GoT在自主奖励进化方面具有显著优势。

## 🎯 应用场景

RE-GoT框架具有广泛的应用前景，可应用于机器人操作、自动驾驶、游戏AI等领域。通过自动设计和优化奖励函数，可以降低强化学习的应用门槛，加速智能体的训练过程，并提高智能体的性能。该研究有望推动强化学习在实际场景中的应用。

## 📄 摘要（原文）

> Designing effective reward functions remains a major challenge in reinforcement learning (RL), often requiring considerable human expertise and iterative refinement. Recent advances leverage Large Language Models (LLMs) for automated reward design, but these approaches are limited by hallucinations, reliance on human feedback, and challenges with handling complex, multi-step tasks. In this work, we introduce Reward Evolution with Graph-of-Thoughts (RE-GoT), a novel bi-level framework that enhances LLMs with structured graph-based reasoning and integrates Visual Language Models (VLMs) for automated rollout evaluation. RE-GoT first decomposes tasks into text-attributed graphs, enabling comprehensive analysis and reward function generation, and then iteratively refines rewards using visual feedback from VLMs without human intervention. Extensive experiments on 10 RoboGen and 4 ManiSkill2 tasks demonstrate that RE-GoT consistently outperforms existing LLM-based baselines. On RoboGen, our method improves average task success rates by 32.25%, with notable gains on complex multi-step tasks. On ManiSkill2, RE-GoT achieves an average success rate of 93.73% across four diverse manipulation tasks, significantly surpassing prior LLM-based approaches and even exceeding expert-designed rewards. Our results indicate that combining LLMs and VLMs with graph-of-thoughts reasoning provides a scalable and effective solution for autonomous reward evolution in RL.

