---
layout: default
title: "WorldPrediction: A Benchmark for High-level World Modeling and Long-horizon Procedural Planning"
---

# WorldPrediction: A Benchmark for High-level World Modeling and Long-horizon Procedural Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04363" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04363v1</a>
  <a href="https://arxiv.org/pdf/2506.04363.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04363v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04363v1', 'WorldPrediction: A Benchmark for High-level World Modeling and Long-horizon Procedural Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Delong Chen, Willy Chung, Yejin Bang, Ziwei Ji, Pascale Fung

**分类**: cs.CV

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出WorldPrediction基准以解决高层次世界建模与长远规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界建模` `程序规划` `视频基准` `部分可观察` `半马尔可夫决策过程` `时间抽象` `语义抽象`

## 📋 核心要点

1. 现有AI模型在学习世界模型和进行长远规划方面存在不足，尤其是在多样化环境中的应用效果不佳。
2. 本文提出WorldPrediction基准，强调时间和语义抽象的行动，旨在评估AI模型的世界建模和程序规划能力。
3. 实验结果显示，当前前沿模型在WorldPrediction-WM和WorldPrediction-PP任务上的准确率分别仅为57%和38%，而人类能够完美解决这两个任务。

## 📝 摘要（中文）

人类拥有内在的“世界模型”，使我们能够基于世界状态进行行动规划。AI代理同样需要这样的世界模型以进行有效的行动规划。然而，目前的AI模型，尤其是生成模型，如何学习这些世界模型并在多样化环境中进行程序规划尚不明确。为此，本文提出了WorldPrediction，这是一个基于视频的基准，用于评估不同AI模型的世界建模和程序规划能力。与以往主要关注低层次世界建模和机器人运动规划的基准不同，WorldPrediction首次强调具有时间和语义抽象的行动。该基准通过视觉观察表示状态和行动，并通过提供“行动等价物”来防止模型利用背景场景中的低层次连续性线索。该基准基于部分可观察的半马尔可夫决策过程（semi-MDP）框架，确保评估的可靠性和稳健性。

## 🔬 方法详解

**问题定义**：本文旨在解决AI代理在多样化环境中缺乏有效世界模型和程序规划能力的问题。现有方法主要集中于低层次的世界建模，未能充分考虑高层次的行动抽象。

**核心思路**：WorldPrediction基准通过强调时间和语义抽象的行动，提供了一种新的评估框架，使得AI模型能够在复杂环境中进行有效的行动选择和序列规划。

**技术框架**：该基准的整体架构包括两个主要模块：WorldPrediction-WM（区分适当行动）和WorldPrediction-PP（区分适当的行动序列）。通过视觉观察表示状态和行动，并提供“行动等价物”作为选择候选。

**关键创新**：最重要的创新点在于引入了“行动等价物”，防止模型利用低层次的背景信息进行决策，从而提高了评估的可靠性和有效性。

**关键设计**：在设计中，采用了部分可观察的半马尔可夫决策过程（semi-MDP）框架，确保了评估的稳健性。此外，进行了广泛的人类过滤和验证，以确保基准的有效性。

## 📊 实验亮点

实验结果表明，当前前沿模型在WorldPrediction-WM任务上的准确率仅为57%，在WorldPrediction-PP任务上的准确率为38%。相比之下，人类在这两个任务上均能完美解决，显示出AI模型在高层次世界建模和长远规划方面的显著不足。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟助手等，需要AI代理在复杂环境中进行高效的决策和规划。通过提供一个标准化的评估基准，研究者可以更好地比较和改进不同AI模型的性能，推动相关技术的发展。

## 📄 摘要（原文）

> Humans are known to have an internal "world model" that enables us to carry out action planning based on world states. AI agents need to have such a world model for action planning as well. It is not clear how current AI models, especially generative models, are able to learn such world models and carry out procedural planning in diverse environments. We introduce WorldPrediction, a video-based benchmark for evaluating world modeling and procedural planning capabilities of different AI models. In contrast to prior benchmarks that focus primarily on low-level world modeling and robotic motion planning, WorldPrediction is the first benchmark that emphasizes actions with temporal and semantic abstraction. Given initial and final world states, the task is to distinguish the proper action (WorldPrediction-WM) or the properly ordered sequence of actions (WorldPrediction-PP) from a set of counterfactual distractors. This discriminative task setup enable us to evaluate different types of world models and planners and realize a thorough comparison across different hypothesis. The benchmark represents states and actions using visual observations. In order to prevent models from exploiting low-level continuity cues in background scenes, we provide "action equivalents" - identical actions observed in different contexts - as candidates for selection. This benchmark is grounded in a formal framework of partially observable semi-MDP, ensuring better reliability and robustness of the evaluation. We conduct extensive human filtering and validation on our benchmark and show that current frontier models barely achieve 57% accuracy on WorldPrediction-WM and 38% on WorldPrediction-PP whereas humans are able to solve both tasks perfectly.

