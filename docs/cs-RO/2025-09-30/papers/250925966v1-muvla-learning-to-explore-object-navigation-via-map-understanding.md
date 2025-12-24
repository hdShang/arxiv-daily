---
layout: default
title: "MUVLA: Learning to Explore Object Navigation via Map Understanding"
---

# MUVLA: Learning to Explore Object Navigation via Map Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25966" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25966v1</a>
  <a href="https://arxiv.org/pdf/2509.25966.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25966v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25966v1', 'MUVLA: Learning to Explore Object Navigation via Map Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peilong Han, Fan Jia, Min Zhang, Yutao Qiu, Hongyao Tang, Yan Zheng, Tiancai Wang, Jianye Hao

**分类**: cs.RO

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**MUVLA：通过地图理解学习物体导航，提升探索能力**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `物体导航` `语义地图` `视觉语言动作模型` `强化学习` `模仿学习`

## 📋 核心要点

1. 现有物体导航方法难以有效利用历史信息，导致探索效率低下。
2. MUVLA通过语义地图抽象统一历史信息，并结合视觉、语言和动作信息进行建模。
3. MUVLA在HM3D和Gibson数据集上表现出良好的泛化能力，并能从低质量轨迹中学习。

## 📝 摘要（中文）

本文提出了MUVLA，一个专为物体导航设计的地图理解视觉-语言-动作模型。它利用语义地图抽象来统一和结构化历史信息，以紧凑且一致的形式编码空间上下文。MUVLA将当前和历史观测以及语义地图作为输入，并根据目标物体的描述预测动作序列。此外，它通过基于密集短程进展信号的奖励引导回报建模来放大监督，使模型能够发展对奖励最大化的动作值的详细理解。MUVLA采用三阶段训练流程：学习地图级空间理解、模仿混合质量演示的行为以及奖励放大。这种策略使MUVLA能够将不同的演示统一为鲁棒的空间表示，并生成更合理的探索策略。在HM3D和Gibson基准上的实验表明，MUVLA实现了良好的泛化，即使从低质量或部分成功的轨迹中也能学习到有效的探索行为。

## 🔬 方法详解

**问题定义**：物体导航任务旨在让智能体在未知环境中找到指定的目标物体。现有方法通常难以有效地整合历史观测信息，导致探索过程效率低下，容易陷入局部最优。此外，如何从不同质量的演示数据中学习也是一个挑战。

**核心思路**：MUVLA的核心思路是利用语义地图抽象来统一和结构化历史信息，从而使智能体能够更好地理解环境的空间结构。通过将视觉、语言和动作信息与语义地图相结合，MUVLA能够预测更合理的导航策略。此外，通过奖励引导的回报建模，MUVLA能够从低质量的演示数据中学习，并提升探索能力。

**技术框架**：MUVLA的整体框架包含三个主要阶段：1) 地图级空间理解学习：利用历史观测构建语义地图，并学习地图的空间表示。2) 行为模仿学习：利用混合质量的演示数据，模仿人类的导航行为。3) 奖励放大：通过奖励引导的回报建模，提升智能体的探索能力。MUVLA模型以当前和历史观测以及语义地图作为输入，输出动作序列。

**关键创新**：MUVLA的关键创新在于：1) 利用语义地图抽象来统一和结构化历史信息，从而更好地理解环境的空间结构。2) 采用奖励引导的回报建模，从低质量的演示数据中学习，并提升探索能力。3) 三阶段训练流程，逐步提升模型的性能。与现有方法相比，MUVLA能够更有效地利用历史信息，并从不同质量的演示数据中学习。

**关键设计**：MUVLA使用Transformer网络来编码视觉、语言和动作信息。语义地图采用栅格地图表示，每个栅格包含语义信息。奖励引导的回报建模使用Q-learning算法，通过密集短程进展信号来计算奖励。损失函数包括模仿学习损失和Q-learning损失。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

MUVLA在HM3D和Gibson基准测试中取得了显著的性能提升。实验结果表明，MUVLA能够从低质量或部分成功的轨迹中学习到有效的探索行为，并且具有良好的泛化能力。相较于现有方法，MUVLA在导航成功率和路径长度方面均有明显改善。

## 🎯 应用场景

MUVLA技术可应用于家庭服务机器人、仓储物流机器人、自动驾驶等领域。通过提升机器人在复杂环境中的导航能力，可以实现更高效、更智能的自动化服务，例如家庭清洁、物品搬运、自动驾驶导航等，具有广阔的应用前景和实际价值。

## 📄 摘要（原文）

> In this paper, we present MUVLA, a Map Understanding Vision-Language-Action model tailored for object navigation. It leverages semantic map abstractions to unify and structure historical information, encoding spatial context in a compact and consistent form. MUVLA takes the current and history observations, as well as the semantic map, as inputs and predicts the action sequence based on the description of goal object. Furthermore, it amplifies supervision through reward-guided return modeling based on dense short-horizon progress signals, enabling the model to develop a detailed understanding of action value for reward maximization. MUVLA employs a three-stage training pipeline: learning map-level spatial understanding, imitating behaviors from mixed-quality demonstrations, and reward amplification. This strategy allows MUVLA to unify diverse demonstrations into a robust spatial representation and generate more rational exploration strategies. Experiments on HM3D and Gibson benchmarks demonstrate that MUVLA achieves great generalization and learns effective exploration behaviors even from low-quality or partially successful trajectories.

