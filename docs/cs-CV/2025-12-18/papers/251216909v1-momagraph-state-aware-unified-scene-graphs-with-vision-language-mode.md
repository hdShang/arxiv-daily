---
layout: default
title: MomaGraph: State-Aware Unified Scene Graphs with Vision-Language Model for Embodied Task Planning
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

**关键词**: `具身智能` `场景图` `视觉-语言模型` `任务规划` `强化学习`

## 📋 核心要点

1. 现有场景图表示方法在处理具身任务时，缺乏对空间-功能关系的统一建模，且忽略了对象状态和任务相关信息。
2. MomaGraph通过整合空间-功能关系和部件级别的交互元素，构建了状态感知的统一场景图，从而更有效地支持具身智能体的任务规划。
3. MomaGraph-R1模型在MomaGraph-Bench上取得了显著的性能提升，并在真实机器人实验中展现了良好的泛化能力。

## 📝 摘要（中文）

本文提出MomaGraph，一种用于具身智能体的统一场景表示，它集成了空间-功能关系和部件级别的交互元素，旨在解决现有场景图表示方法中空间和功能关系分离、场景静态化以及忽略任务相关信息的问题。同时，本文贡献了MomaGraph-Scenes，一个大规模的、带有丰富标注的、任务驱动的家庭环境场景图数据集，以及MomaGraph-Bench，一个包含从高层规划到细粒度场景理解的六种推理能力的系统评估套件。基于此，本文进一步开发了MomaGraph-R1，一个在MomaGraph-Scenes上通过强化学习训练的7B视觉-语言模型。MomaGraph-R1能够预测面向任务的场景图，并作为Graph-then-Plan框架下的零样本任务规划器。实验结果表明，该模型在开源模型中达到了最先进的水平，在基准测试中达到了71.6%的准确率（比最佳基线高出11.4%），同时能够泛化到公共基准测试，并有效地迁移到真实机器人实验中。

## 🔬 方法详解

**问题定义**：现有场景图方法通常将空间和功能关系分离处理，将场景视为静态快照，忽略了对象的状态变化和与当前任务最相关的信息。这导致具身智能体难以有效地进行任务规划，尤其是在复杂的家庭环境中。

**核心思路**：MomaGraph的核心思路是构建一个统一的、状态感知的场景图表示，它能够同时捕捉对象的位置、功能以及可交互的部件。通过整合空间-功能关系，并利用视觉-语言模型预测场景图，MomaGraph能够为具身智能体提供更全面的场景理解，从而支持更有效的任务规划。

**技术框架**：MomaGraph的整体框架包含数据收集与标注、模型训练和任务规划三个主要阶段。首先，构建MomaGraph-Scenes数据集，其中包含丰富的场景图标注，包括对象、关系和状态信息。然后，利用该数据集训练MomaGraph-R1视觉-语言模型，该模型能够根据视觉输入预测面向任务的场景图。最后，将预测的场景图作为输入，利用Graph-then-Plan框架进行任务规划。

**关键创新**：MomaGraph的关键创新在于其统一的场景图表示，它能够同时捕捉空间-功能关系和对象状态。此外，MomaGraph-R1模型利用视觉-语言模型进行场景图预测，并结合强化学习进行训练，从而提高了模型的性能和泛化能力。与现有方法相比，MomaGraph能够更全面地理解场景，并更好地支持具身智能体的任务规划。

**关键设计**：MomaGraph-R1模型是一个7B参数的视觉-语言模型，它以图像作为输入，输出场景图的表示。模型采用Transformer架构，并使用交叉注意力机制融合视觉和语言信息。在训练过程中，模型使用强化学习进行微调，以优化其在任务规划方面的性能。具体的损失函数包括场景图预测损失和任务规划奖励。

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

MomaGraph-R1在MomaGraph-Bench基准测试中取得了71.6%的准确率，比最佳基线高出11.4%。此外，该模型还能够泛化到公共基准测试，并在真实机器人实验中表现出良好的性能。这些结果表明，MomaGraph是一种有效的场景表示方法，能够显著提高具身智能体的任务规划能力。

## 🎯 应用场景

MomaGraph在家庭服务机器人、自动驾驶、增强现实等领域具有广泛的应用前景。它可以帮助机器人更好地理解周围环境，从而执行更复杂的任务，例如物品整理、清洁和烹饪。此外，MomaGraph还可以用于构建更智能的虚拟助手，为用户提供更个性化的服务。

## 📄 摘要（原文）

> Mobile manipulators in households must both navigate and manipulate. This requires a compact, semantically rich scene representation that captures where objects are, how they function, and which parts are actionable. Scene graphs are a natural choice, yet prior work often separates spatial and functional relations, treats scenes as static snapshots without object states or temporal updates, and overlooks information most relevant for accomplishing the current task. To address these limitations, we introduce MomaGraph, a unified scene representation for embodied agents that integrates spatial-functional relationships and part-level interactive elements. However, advancing such a representation requires both suitable data and rigorous evaluation, which have been largely missing. We thus contribute MomaGraph-Scenes, the first large-scale dataset of richly annotated, task-driven scene graphs in household environments, along with MomaGraph-Bench, a systematic evaluation suite spanning six reasoning capabilities from high-level planning to fine-grained scene understanding. Built upon this foundation, we further develop MomaGraph-R1, a 7B vision-language model trained with reinforcement learning on MomaGraph-Scenes. MomaGraph-R1 predicts task-oriented scene graphs and serves as a zero-shot task planner under a Graph-then-Plan framework. Extensive experiments demonstrate that our model achieves state-of-the-art results among open-source models, reaching 71.6% accuracy on the benchmark (+11.4% over the best baseline), while generalizing across public benchmarks and transferring effectively to real-robot experiments.

