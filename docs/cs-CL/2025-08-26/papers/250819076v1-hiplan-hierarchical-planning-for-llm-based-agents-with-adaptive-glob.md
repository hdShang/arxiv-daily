---
layout: default
title: "HiPlan: Hierarchical Planning for LLM-Based Agents with Adaptive Global-Local Guidance"
---

# HiPlan: Hierarchical Planning for LLM-Based Agents with Adaptive Global-Local Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19076" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19076v1</a>
  <a href="https://arxiv.org/pdf/2508.19076.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19076v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19076v1', 'HiPlan: Hierarchical Planning for LLM-Based Agents with Adaptive Global-Local Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyue Li, Yuan Chang, Gaihong Yu, Xiaoqiu Le

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出HiPlan以解决LLM代理在复杂规划中的决策问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `层次化规划` `大型语言模型` `决策支持` `动态适应` `智能代理`

## 📋 核心要点

1. 现有的LLM代理在复杂长时间规划任务中缺乏宏观指导，导致决策失误和执行偏差。
2. HiPlan通过层次化规划框架，将复杂任务分解为里程碑和逐步提示，提供全局与局部的自适应指导。
3. 在多个基准测试中，HiPlan的表现显著优于现有强基线，验证了其有效性和创新性。

## 📝 摘要（中文）

基于大型语言模型（LLM）的代理在决策任务中表现出色，但在复杂的长时间规划场景中却面临显著挑战。这主要源于缺乏宏观指导，导致在复杂任务中迷失方向，并且在执行过程中缺乏持续的监督，使其对环境变化反应迟缓且容易偏离。为了解决这些问题，本文提出了HiPlan，一个层次化规划框架，通过自适应的全局-局部指导来提升LLM代理的决策能力。HiPlan将复杂任务分解为里程碑行动指南和逐步提示。在离线阶段，我们从专家演示中构建了里程碑库，实现结构化经验重用。在执行阶段，动态适应过去里程碑的轨迹片段，以生成与当前观察相一致的逐步提示，从而弥补差距并纠正偏差。大量实验表明，HiPlan显著优于强基线，消融研究验证了其层次组件的互补效益。

## 🔬 方法详解

**问题定义**：本文旨在解决LLM代理在复杂长时间规划中的决策问题，现有方法缺乏宏观指导和持续监督，导致执行中的迷失和偏差。

**核心思路**：HiPlan的核心思路是通过层次化规划，将复杂任务分解为里程碑和逐步提示，以提供更清晰的决策路径和实时调整能力。

**技术框架**：HiPlan的整体架构包括离线阶段和执行阶段。在离线阶段，构建里程碑库以实现经验重用；在执行阶段，动态适应过去的轨迹片段生成逐步提示。

**关键创新**：HiPlan的主要创新在于其层次化的规划框架，通过里程碑和逐步提示的结合，显著提升了LLM代理的决策能力，与传统方法相比，提供了更灵活的适应性。

**关键设计**：在设计中，里程碑库的构建依赖于专家演示，动态适应机制确保了生成的提示与当前环境观察相一致，具体参数设置和损失函数的选择未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

在实验中，HiPlan在两个具有挑战性的基准测试上显著超越了多个强基线，具体性能提升幅度未在摘要中提供，但消融研究表明其层次组件的互补效益显著，验证了方法的有效性。

## 🎯 应用场景

HiPlan的研究成果在多个领域具有潜在应用价值，包括智能机器人、自动驾驶、游戏AI等复杂决策系统。通过提升LLM代理的规划能力，能够更好地应对动态环境中的复杂任务，未来可能推动智能代理在实际应用中的广泛使用。

## 📄 摘要（原文）

> Large language model (LLM)-based agents have demonstrated remarkable capabilities in decision-making tasks, but struggle significantly with complex, long-horizon planning scenarios. This arises from their lack of macroscopic guidance, causing disorientation and failures in complex tasks, as well as insufficient continuous oversight during execution, rendering them unresponsive to environmental changes and prone to deviations. To tackle these challenges, we introduce HiPlan, a hierarchical planning framework that provides adaptive global-local guidance to boost LLM-based agents'decision-making. HiPlan decomposes complex tasks into milestone action guides for general direction and step-wise hints for detailed actions. During the offline phase, we construct a milestone library from expert demonstrations, enabling structured experience reuse by retrieving semantically similar tasks and milestones. In the execution phase, trajectory segments from past milestones are dynamically adapted to generate step-wise hints that align current observations with the milestone objectives, bridging gaps and correcting deviations. Extensive experiments across two challenging benchmarks demonstrate that HiPlan substantially outperforms strong baselines, and ablation studies validate the complementary benefits of its hierarchical components.

