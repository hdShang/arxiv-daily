---
layout: default
title: "RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation"
---

# RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15965" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15965v1</a>
  <a href="https://arxiv.org/pdf/2509.15965.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15965v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15965v1', 'RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chao Yu, Yuanqing Wang, Zhen Guo, Hao Lin, Si Xu, Hongzhi Zang, Quanlu Zhang, Yongji Wu, Chunyang Zhu, Junhao Hu, Zixiao Huang, Mingjie Wei, Yuqing Xie, Ke Yang, Bo Dai, Zhexuan Xu, Xiangyuan Wang, Xu Fu, Zhihao Liu, Kang Chen, Weilin Liu, Gang Liu, Boxun Li, Jianlei Yang, Zhi Yang, Guohao Dai, Yu Wang

**分类**: cs.LG, cs.AI, cs.DC

**发布日期**: 2025-09-19

**备注**: GitHub Repo: https://github.com/RLinf/RLinf

---

## 💡 一句话要点

**RLinf：通过宏微观流转换实现灵活高效的大规模强化学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `大规模训练` `系统优化` `宏微观流转换` `自适应通信`

## 📋 核心要点

1. 现有强化学习系统在处理异构和动态的工作流程时，面临硬件利用率低和训练速度慢的挑战。
2. RLinf提出宏微观流转换（M2Flow）范式，自动分解和重组RL工作流程，优化执行效率。
3. 实验结果表明，RLinf在推理和具身RL任务上均优于现有系统，端到端训练吞吐量提升1.1-2.13倍。

## 📝 摘要（中文）

强化学习（RL）在推动通用人工智能、智能体智能和具身智能方面展现出巨大潜力。然而，RL工作流程固有的异构性和动态性通常导致现有系统上的硬件利用率低和训练速度慢。本文提出了RLinf，一个高性能的RL训练系统，其核心在于系统灵活性。为了最大化灵活性和效率，RLinf基于一种名为宏微观流转换（M2Flow）的新型RL系统设计范式构建，该范式在时间和空间维度上自动分解高级、易于组合的RL工作流程，并将它们重组为优化的执行流。在RLinf工作节点的自适应通信能力的支持下，我们设计了上下文切换和弹性流水线来实现M2Flow转换，并采用剖析引导的调度策略来生成最优执行计划。在推理RL和具身RL任务上的大量评估表明，RLinf始终优于最先进的系统，在端到端训练吞吐量方面实现了1.1倍-2.13倍的加速。

## 🔬 方法详解

**问题定义**：现有强化学习系统在处理大规模、异构和动态的训练任务时，由于缺乏足够的灵活性，导致硬件资源利用率低下，训练效率不高。具体来说，不同的RL算法和任务对计算、通信和存储的需求各不相同，而现有的系统难以根据这些需求进行动态调整和优化。这使得研究人员难以快速迭代和部署新的RL算法。

**核心思路**：RLinf的核心思路是引入宏微观流转换（M2Flow）范式，将高级的、易于组合的RL工作流程分解为更细粒度的任务单元，并在时间和空间维度上进行优化重组。通过这种方式，系统可以根据实际的资源状况和任务需求，动态地调整执行计划，从而提高硬件利用率和训练效率。

**技术框架**：RLinf的整体架构包括以下几个主要模块：1) 工作流程分解器：将高级RL工作流程分解为细粒度的任务单元。2) 任务调度器：根据资源状况和任务依赖关系，生成优化的执行计划。3) 自适应通信模块：支持工作节点之间的灵活通信，实现任务单元的协同执行。4) 弹性流水线：通过上下文切换和流水线技术，提高任务执行的并发度。

**关键创新**：RLinf最重要的技术创新在于宏微观流转换（M2Flow）范式。与传统的静态执行计划相比，M2Flow能够根据实际情况动态地调整任务的执行顺序和资源分配，从而更好地适应RL训练的异构性和动态性。此外，RLinf的自适应通信模块和弹性流水线也为实现高效的M2Flow转换提供了关键支持。

**关键设计**：RLinf的关键设计包括：1) 剖析引导的调度策略：通过对RL工作流程进行剖析，了解各个任务单元的资源需求，从而生成最优的执行计划。2) 上下文切换机制：支持快速切换不同的任务单元，提高资源利用率。3) 弹性流水线：通过将任务分解为多个阶段，并采用流水线技术，提高任务执行的并发度。4) 自适应通信协议：根据任务单元之间的数据依赖关系，选择合适的通信方式，减少通信开销。

## 📊 实验亮点

实验结果表明，RLinf在推理RL和具身RL任务上均优于最先进的系统。具体来说，在端到端训练吞吐量方面，RLinf实现了1.1倍-2.13倍的加速。这些结果表明，RLinf的宏微观流转换范式能够有效地提高RL训练的效率。

## 🎯 应用场景

RLinf具有广泛的应用前景，可用于加速各种强化学习任务的训练，包括机器人控制、游戏AI、自动驾驶、推荐系统等。通过提高训练效率，RLinf可以帮助研究人员更快地探索新的RL算法，并将其应用于更复杂的实际问题中。此外，RLinf还可以降低RL训练的成本，使其更容易被广泛采用。

## 📄 摘要（原文）

> Reinforcement learning (RL) has demonstrated immense potential in advancing artificial general intelligence, agentic intelligence, and embodied intelligence. However, the inherent heterogeneity and dynamicity of RL workflows often lead to low hardware utilization and slow training on existing systems. In this paper, we present RLinf, a high-performance RL training system based on our key observation that the major roadblock to efficient RL training lies in system flexibility. To maximize flexibility and efficiency, RLinf is built atop a novel RL system design paradigm called macro-to-micro flow transformation (M2Flow), which automatically breaks down high-level, easy-to-compose RL workflows at both the temporal and spatial dimensions, and recomposes them into optimized execution flows. Supported by RLinf worker's adaptive communication capability, we devise context switching and elastic pipelining to realize M2Flow transformation, and a profiling-guided scheduling policy to generate optimal execution plans. Extensive evaluations on both reasoning RL and embodied RL tasks demonstrate that RLinf consistently outperforms state-of-the-art systems, achieving 1.1x-2.13x speedup in end-to-end training throughput.

