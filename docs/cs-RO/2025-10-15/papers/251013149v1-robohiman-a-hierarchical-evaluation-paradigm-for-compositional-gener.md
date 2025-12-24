---
layout: default
title: "RoboHiMan: A Hierarchical Evaluation Paradigm for Compositional Generalization in Long-Horizon Manipulation"
---

# RoboHiMan: A Hierarchical Evaluation Paradigm for Compositional Generalization in Long-Horizon Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13149" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13149v1</a>
  <a href="https://arxiv.org/pdf/2510.13149.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13149v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.13149v1', 'RoboHiMan: A Hierarchical Evaluation Paradigm for Compositional Generalization in Long-Horizon Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yangtao Chen, Zixuan Chen, Nga Teng Chan, Junting Chen, Junhui Yin, Jieqi Shi, Yang Gao, Yong-Lu Li, Jing Huo

**分类**: cs.RO

**发布日期**: 2025-10-15

**备注**: Under review. These first two authors contributed equally to this work

**🔗 代码/项目**: [PROJECT_PAGE](https://chenyt31.github.io/robo-himan.github.io/)

---

## 💡 一句话要点

**提出RoboHiMan，用于评估长时程操作中组合泛化的分层评估范式。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时程操作` `组合泛化` `分层评估` `机器人操作` `基准测试`

## 📋 核心要点

1. 现有端到端模型在长时程操作任务中泛化能力不足，分层方法在复杂扰动下技能组合能力有限。
2. RoboHiMan通过HiMan-Bench基准和三种评估范式，系统性地评估组合泛化、鲁棒性以及规划与执行的相互作用。
3. 实验结果揭示了现有模型在长时程操作任务中的能力差距，为未来模型设计提供了方向。

## 📝 摘要（中文）

本文提出RoboHiMan，一种用于长时程操作中组合泛化的分层评估范式。现有的端到端视觉语言动作模型泛化能力有限，分层方法在复杂扰动下表现不佳，表明技能组合能力不足。现有基准测试主要关注长时程任务完成，缺乏对组合泛化、鲁棒性以及规划与执行之间相互作用的深入研究。RoboHiMan引入HiMan-Bench，一个包含原子和组合任务的基准，支持多层次训练数据集以分析渐进式数据缩放。同时，提出了三种评估范式（vanilla, decoupled, coupled），用于探究技能组合的必要性并揭示分层架构中的瓶颈。实验结果表明，代表性模型和架构存在明显的能力差距，为改进更适合现实世界长时程操作任务的模型指明了方向。

## 🔬 方法详解

**问题定义**：现有长时程操作任务的评估基准主要关注任务完成度，缺乏对组合泛化能力、鲁棒性以及规划与执行之间相互作用的深入评估。现有的端到端模型和分层模型在复杂扰动下表现不佳，难以胜任真实世界的复杂操作任务。

**核心思路**：RoboHiMan的核心思路是提供一个系统性的评估框架，通过精心设计的基准测试和评估范式，深入分析分层模型在长时程操作任务中的组合泛化能力。通过控制任务的复杂度和引入不同的扰动，可以更清晰地揭示模型的瓶颈和不足。

**技术框架**：RoboHiMan包含两个主要组成部分：HiMan-Bench基准测试和三种评估范式。HiMan-Bench包含原子任务和组合任务，涵盖多种扰动类型。三种评估范式分别是：vanilla（端到端评估）、decoupled（分别评估规划和执行模块）、coupled（联合评估规划和执行模块）。通过这三种范式，可以全面评估模型的各个方面。

**关键创新**：RoboHiMan的关键创新在于其系统性的评估方法，它不仅关注任务的完成度，更关注模型的组合泛化能力和鲁棒性。HiMan-Bench的设计考虑了任务的复杂度和扰动的多样性，能够更有效地揭示模型的瓶颈。三种评估范式能够分别评估规划和执行模块，从而更深入地了解模型的行为。

**关键设计**：HiMan-Bench基准测试包含一系列原子任务和组合任务，这些任务涵盖了不同的操作类型和对象。扰动类型包括视觉扰动、物理扰动和时间扰动。多层次训练数据集用于分析渐进式数据缩放对模型性能的影响。三种评估范式通过不同的方式组合规划和执行模块，从而评估模型的不同方面。具体的参数设置、损失函数和网络结构取决于被评估的模型。

## 📊 实验亮点

实验结果表明，现有的代表性模型和架构在RoboHiMan基准测试中存在明显的能力差距，尤其是在组合泛化和鲁棒性方面。例如，端到端模型在复杂任务中表现不佳，分层模型在面对扰动时容易失效。这些结果为未来模型的设计提供了重要的参考依据。

## 🎯 应用场景

RoboHiMan的研究成果可应用于机器人操作、自动化生产线、智能家居等领域。通过提升机器人的组合泛化能力和鲁棒性，可以使其更好地适应复杂多变的环境，完成更复杂的任务。该研究有助于推动机器人技术在实际场景中的应用。

## 📄 摘要（原文）

> Enabling robots to flexibly schedule and compose learned skills for novel long-horizon manipulation under diverse perturbations remains a core challenge. Early explorations with end-to-end VLA models show limited success, as these models struggle to generalize beyond the training distribution. Hierarchical approaches, where high-level planners generate subgoals for low-level policies, bring certain improvements but still suffer under complex perturbations, revealing limited capability in skill composition. However, existing benchmarks primarily emphasize task completion in long-horizon settings, offering little insight into compositional generalization, robustness, and the interplay between planning and execution. To systematically investigate these gaps, we propose RoboHiMan, a hierarchical evaluation paradigm for compositional generalization in long-horizon manipulation. RoboHiMan introduces HiMan-Bench, a benchmark of atomic and compositional tasks under diverse perturbations, supported by a multi-level training dataset for analyzing progressive data scaling, and proposes three evaluation paradigms (vanilla, decoupled, coupled) that probe the necessity of skill composition and reveal bottlenecks in hierarchical architectures. Experiments highlight clear capability gaps across representative models and architectures, pointing to directions for advancing models better suited to real-world long-horizon manipulation tasks. Videos and open-source code can be found on our project website: https://chenyt31.github.io/robo-himan.github.io/.

