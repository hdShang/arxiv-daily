---
layout: default
title: "MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning"
---

# MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16909" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16909v1</a>
  <a href="https://arxiv.org/pdf/2512.16909.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16909v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16909v1', 'MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanchen Ju, Yongyuan Liang, Yen-Jen Wang, Nandiraju Gireesh, Yuanliang Ju, Seungjae Lee, Qiao Gu, Elvis Hsieh, Furong Huang, Koushil Sreenath

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-18

**备注**: 25 pages, 10 figures. Project page:https://hybridrobotics.github.io/MomaGraph/

---

## 💡 一句话要点

**提出MomaGraph，利用视觉-语言模型为具身任务规划构建状态感知的统一场景图。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `场景图` `具身智能` `视觉-语言模型` `任务规划` `强化学习`

## 📋 核心要点

1. 现有场景图方法在处理具身任务时，缺乏对空间-功能关系的统一建模，忽略了对象状态和时间更新，且未充分考虑任务相关信息。
2. MomaGraph通过整合空间-功能关系和部件级交互元素，构建统一的、状态感知的场景图表示，从而更有效地支持具身智能体的任务规划。
3. MomaGraph-R1模型在MomaGraph-Scenes数据集上训练，并在MomaGraph-Bench上评估，实验结果表明其性能优于现有方法，并具有良好的泛化能力。

## 📝 摘要（中文）

本文提出MomaGraph，一种用于具身智能体的统一场景表示，它集成了空间-功能关系和部件级别的交互元素，旨在解决现有场景图表示方法中空间和功能关系分离、场景被视为静态快照以及忽略与当前任务最相关信息的问题。同时，本文贡献了MomaGraph-Scenes，这是首个大规模的、带有丰富标注的、任务驱动的家庭环境场景图数据集，以及MomaGraph-Bench，一个涵盖从高层规划到细粒度场景理解的六种推理能力的系统评估套件。在此基础上，进一步开发了MomaGraph-R1，一个在MomaGraph-Scenes上通过强化学习训练的7B视觉-语言模型。MomaGraph-R1预测面向任务的场景图，并在Graph-then-Plan框架下作为零样本任务规划器。大量实验表明，该模型在开源模型中取得了最先进的结果，在基准测试中达到了71.6%的准确率（比最佳基线高出11.4%），同时推广到公共基准测试并有效地转移到真实机器人实验。

## 🔬 方法详解

**问题定义**：现有方法在移动操作机器人的场景理解中存在局限性，主要体现在：1) 空间关系和功能关系分离；2) 场景被视为静态快照，缺乏对物体状态和时间变化的建模；3) 忽略了与当前任务最相关的信息。这些问题导致机器人难以有效地进行导航和操作。

**核心思路**：MomaGraph的核心思路是构建一个统一的、状态感知的场景图表示，将空间关系、功能关系以及物体状态整合在一起。通过这种方式，机器人可以更好地理解场景，并根据当前任务进行规划。

**技术框架**：MomaGraph的整体框架包含以下几个主要部分：1) MomaGraph-Scenes数据集的构建，用于训练和评估模型；2) MomaGraph-Bench评估套件，用于系统地评估模型的推理能力；3) MomaGraph-R1视觉-语言模型，该模型在MomaGraph-Scenes上进行训练，用于预测任务导向的场景图，并作为零样本任务规划器。

**关键创新**：MomaGraph的关键创新在于：1) 提出了统一的场景图表示，整合了空间-功能关系和物体状态；2) 构建了大规模的、任务驱动的场景图数据集MomaGraph-Scenes；3) 开发了MomaGraph-R1视觉-语言模型，该模型能够预测任务导向的场景图，并作为零样本任务规划器。

**关键设计**：MomaGraph-R1是一个7B的视觉-语言模型，使用强化学习在MomaGraph-Scenes数据集上进行训练。具体的损失函数和网络结构细节在论文中未详细说明，但强调了其在任务导向的场景图预测和零样本任务规划方面的能力。强化学习的使用可能涉及到奖励函数的设计，以鼓励模型生成更符合任务需求的场景图。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16909v1/Figures/Teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16909v1/Figures/Failure.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16909v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

MomaGraph-R1在MomaGraph-Bench基准测试中取得了显著的性能提升，达到了71.6%的准确率，比最佳基线高出11.4%。此外，该模型还展现出良好的泛化能力，能够推广到公共基准测试，并有效地转移到真实机器人实验中。这些结果表明MomaGraph在场景理解和任务规划方面具有强大的潜力。

## 🎯 应用场景

MomaGraph在家庭服务机器人、自动驾驶、虚拟现实等领域具有广泛的应用前景。它可以帮助机器人更好地理解周围环境，从而实现更智能的导航、操作和人机交互。例如，服务机器人可以利用MomaGraph来理解厨房场景，并规划完成诸如“准备早餐”之类的复杂任务。未来，MomaGraph有望成为构建通用人工智能系统的关键组成部分。

## 📄 摘要（原文）

> Mobile manipulators in households must both navigate and manipulate. This requires a compact, semantically rich scene representation that captures where objects are, how they function, and which parts are actionable. Scene graphs are a natural choice, yet prior work often separates spatial and functional relations, treats scenes as static snapshots without object states or temporal updates, and overlooks information most relevant for accomplishing the current task. To address these limitations, we introduce MomaGraph, a unified scene representation for embodied agents that integrates spatial-functional relationships and part-level interactive elements. However, advancing such a representation requires both suitable data and rigorous evaluation, which have been largely missing. We thus contribute MomaGraph-Scenes, the first large-scale dataset of richly annotated, task-driven scene graphs in household environments, along with MomaGraph-Bench, a systematic evaluation suite spanning six reasoning capabilities from high-level planning to fine-grained scene understanding. Built upon this foundation, we further develop MomaGraph-R1, a 7B vision-language model trained with reinforcement learning on MomaGraph-Scenes. MomaGraph-R1 predicts task-oriented scene graphs and serves as a zero-shot task planner under a Graph-then-Plan framework. Extensive experiments demonstrate that our model achieves state-of-the-art results among open-source models, reaching 71.6% accuracy on the benchmark (+11.4% over the best baseline), while generalizing across public benchmarks and transferring effectively to real-robot experiments.

