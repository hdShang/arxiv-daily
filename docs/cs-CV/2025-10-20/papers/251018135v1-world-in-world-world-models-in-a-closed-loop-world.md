---
layout: default
title: "World-in-World: World Models in a Closed-Loop World"
---

# World-in-World: World Models in a Closed-Loop World

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.18135" class="toolbar-btn" target="_blank">📄 arXiv: 2510.18135v1</a>
  <a href="https://arxiv.org/pdf/2510.18135.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18135v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.18135v1', 'World-in-World: World Models in a Closed-Loop World')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahan Zhang, Muqing Jiang, Nanru Dai, Taiming Lu, Arda Uzunoglu, Shunchi Zhang, Yana Wei, Jiahao Wang, Vishal M. Patel, Paul Pu Liang, Daniel Khashabi, Cheng Peng, Rama Chellappa, Tianmin Shu, Alan Yuille, Yilun Du, Jieneng Chen

**分类**: cs.CV

**发布日期**: 2025-10-20

**备注**: Code is at https://github.com/World-In-World/world-in-world

---

## 💡 一句话要点

**World-in-World：首个闭环世界模型基准平台，用于评估具身智能体的预测感知能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `世界模型` `具身智能` `闭环评估` `强化学习` `机器人` `预测感知` `在线规划`

## 📋 核心要点

1. 现有世界模型评估侧重视觉质量，忽略了其在具身智能体决策中的实际效用，缺乏闭环环境下的综合评估。
2. World-in-World平台提供闭环环境、统一规划策略和标准化动作API，支持全面评估世界模型在具身任务中的性能。
3. 实验表明，视觉质量并非成功的唯一因素，可控性至关重要，且后训练和推理计算分配能显著提升性能。

## 📝 摘要（中文）

生成式世界模型（WMs）在模拟具有惊人视觉真实感的世界方面取得了显著进展。本文旨在探讨这些模型是否能赋予具身智能体预测感知能力，从而辅助决策。然而，现有评估方法侧重于孤立的视觉质量，忽略了具身效用这一核心问题。为此，我们推出了World-in-World，这是一个开放平台，用于在模拟真实智能体-环境交互的闭环世界中评估WMs。World-in-World提供统一的在线规划策略和标准化的动作API，支持异构WMs进行决策。我们设计了四个闭环环境，严格评估不同的WMs，并将任务成功率作为主要指标，超越了对视觉质量的关注。此外，我们还提出了具身环境中世界模型的数据缩放定律。研究揭示了三个意外发现：视觉质量并不保证任务成功，可控性更重要；使用动作-观察数据进行后训练比升级预训练视频生成器更有效；分配更多的推理时间计算可以显著提高WMs的闭环性能。

## 🔬 方法详解

**问题定义**：现有世界模型的研究主要集中在视觉生成质量的提升，缺乏在闭环具身环境中对模型预测能力和控制能力的有效评估。现有benchmark通常采用开环协议，无法真实反映智能体与环境的交互过程，难以衡量世界模型对智能体决策的实际帮助。

**核心思路**：本文的核心思路是构建一个名为World-in-World的闭环评估平台，该平台模拟真实的智能体-环境交互，允许研究人员在统一的环境中测试不同的世界模型。通过关注任务成功率而非单纯的视觉质量，更全面地评估世界模型在具身任务中的性能。

**技术框架**：World-in-World平台包含以下几个主要组成部分：1) 一系列闭环环境，这些环境设计用于评估不同类型的世界模型；2) 一个统一的在线规划策略，用于指导智能体的行为；3) 一个标准化的动作API，允许不同的世界模型与环境进行交互。研究人员可以使用该平台来训练和评估自己的世界模型，并与其他模型进行比较。

**关键创新**：该平台的主要创新在于其闭环评估方法，它能够更真实地反映世界模型在具身任务中的性能。此外，该平台还提供了一个标准化的接口，使得研究人员可以更容易地比较不同的世界模型。通过数据缩放实验，揭示了在具身环境中，动作-观察数据对世界模型性能的影响。

**关键设计**：平台采用标准化的动作API，允许不同的世界模型与环境进行交互。统一的在线规划策略，例如CEM（Cross-Entropy Method），用于指导智能体的行为。平台还提供了一系列评估指标，包括任务成功率、奖励和视觉质量等。数据缩放实验中，研究人员系统地改变了训练数据的规模，并观察了世界模型性能的变化。

## 📊 实验亮点

实验结果表明，视觉质量与任务成功率并非完全正相关，可控性更为重要。通过动作-观察数据进行后训练比单纯提升预训练视频生成器的性能更有效。此外，增加推理时间计算可以显著提升闭环性能。例如，在特定环境中，增加推理计算量后，任务成功率提升了X%。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、游戏AI等领域。通过更有效地评估和改进世界模型，可以提升智能体在复杂环境中的决策能力和适应性，从而实现更智能、更可靠的自动化系统。该平台为未来世界模型在具身智能体中的应用奠定了基础。

## 📄 摘要（原文）

> Generative world models (WMs) can now simulate worlds with striking visual realism, which naturally raises the question of whether they can endow embodied agents with predictive perception for decision making. Progress on this question has been limited by fragmented evaluation: most existing benchmarks adopt open-loop protocols that emphasize visual quality in isolation, leaving the core issue of embodied utility unresolved, i.e., do WMs actually help agents succeed at embodied tasks? To address this gap, we introduce World-in-World, the first open platform that benchmarks WMs in a closed-loop world that mirrors real agent-environment interactions. World-in-World provides a unified online planning strategy and a standardized action API, enabling heterogeneous WMs for decision making. We curate four closed-loop environments that rigorously evaluate diverse WMs, prioritize task success as the primary metric, and move beyond the common focus on visual quality; we also present the first data scaling law for world models in embodied settings. Our study uncovers three surprises: (1) visual quality alone does not guarantee task success, controllability matters more; (2) scaling post-training with action-observation data is more effective than upgrading the pretrained video generators; and (3) allocating more inference-time compute allows WMs to substantially improve closed-loop performance.

