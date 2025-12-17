---
layout: default
title: APULSE: A Scalable Hybrid Algorithm for the RCSPP on Large-Scale Dense Graphs
---

# APULSE: A Scalable Hybrid Algorithm for the RCSPP on Large-Scale Dense Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18236" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18236v2</a>
  <a href="https://arxiv.org/pdf/2511.18236.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18236v2" onclick="toggleFavorite(this, '2511.18236v2', 'APULSE: A Scalable Hybrid Algorithm for the RCSPP on Large-Scale Dense Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nuno Soares, António Grilo

**分类**: cs.RO, eess.SY

**发布日期**: 2025-11-23 (更新: 2025-11-30)

**备注**: This version corrects keywords and reference [9]. 9 pages

---

## 💡 一句话要点

**APULSE：一种可扩展的混合算法，用于求解大规模稠密图上的资源约束最短路径问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `资源约束最短路径问题` `RCSPP` `A*搜索` `Pulse剪枝` `时间分桶` `无人地面车辆` `UGV规划`

## 📋 核心要点

1. 现有RCSPP求解器在处理大规模稠密图时面临可扩展性瓶颈，限制了其在实际场景中的应用。
2. APULSE算法结合A*搜索、Pulse剪枝和时间分桶策略，旨在高效求解大规模RCSPP。
3. 实验表明，APULSE在UGV规划场景中，相较于现有算法，在速度和鲁棒性上均有显著提升。

## 📝 摘要（中文）

资源约束最短路径问题（RCSPP）是一个基本的NP-hard优化难题，在网络路由和自主导航等领域有着广泛的应用。该问题旨在找到一条在满足次要资源预算约束下，主要成本最小化的路径。虽然已经存在各种RCSPP求解器，但当应用于复杂、真实场景中常见的大规模稠密图时，它们通常面临严重的可扩展性限制，使其在时间紧迫的规划中不切实际。无人地面车辆（UGV）的任务规划等领域尤其面临这一挑战，需要在大规模地形图上求解。本文提出了一种混合标签设置算法APULSE，旨在有效地解决此类具有挑战性的图上的RCSPP。APULSE集成了由A*启发式引导的最佳优先搜索、积极的Pulse式剪枝机制以及用于有效状态空间缩减的时间分桶策略。计算研究使用大规模UGV规划场景，将APULSE与最先进的算法进行基准测试。结果表明，APULSE始终能找到接近最优的解决方案，同时速度和鲁棒性提高了几个数量级，尤其是在竞争方法失败的大型问题实例上。这种卓越的可扩展性使APULSE成为复杂、大规模环境中RCSPP的有效解决方案，从而实现交互式决策支持和动态重规划等功能。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模稠密图上的资源约束最短路径问题（RCSPP）。现有方法在处理此类图时，由于状态空间爆炸，计算复杂度高，难以在实际应用中满足时间要求。特别是在无人地面车辆（UGV）的任务规划等需要实时或近实时响应的场景中，现有算法难以胜任。

**核心思路**：APULSE算法的核心思路是通过结合A*搜索的启发式引导、Pulse剪枝的积极状态空间缩减以及时间分桶策略的有效状态管理，来提高RCSPP求解的效率和可扩展性。A*搜索利用启发式信息引导搜索方向，减少搜索空间；Pulse剪枝通过识别和消除非有希望的路径，进一步缩减状态空间；时间分桶策略则将状态按照时间进行分组，从而更有效地管理和比较状态。

**技术框架**：APULSE算法的整体框架可以概括为以下几个步骤：1. 初始化：构建图数据结构，初始化A*搜索的启发式函数，设置时间分桶参数。2. 搜索：使用A*算法进行最佳优先搜索，每次扩展具有最小f值的节点。3. 剪枝：在搜索过程中，应用Pulse剪枝策略，消除被支配的路径。4. 时间分桶：使用时间分桶策略管理状态，减少状态比较的次数。5. 终止：当找到满足资源约束的最短路径或搜索空间耗尽时，算法终止。

**关键创新**：APULSE算法的关键创新在于其混合策略。它并非简单地将几种技术叠加，而是巧妙地将A*搜索、Pulse剪枝和时间分桶策略融合在一起，使其相互协同，共同提高算法的性能。与传统的RCSPP求解器相比，APULSE在状态空间缩减方面更加积极，能够更有效地处理大规模稠密图。

**关键设计**：A*启发式函数的设计至关重要，需要选择一个既能准确估计剩余成本，又能快速计算的函数。Pulse剪枝策略的有效性取决于支配关系的定义，需要根据具体问题进行调整。时间分桶的大小需要仔细选择，过小会导致状态比较次数增加，过大会降低剪枝的效果。具体参数设置未知，需要根据实际问题进行调整。

## 📊 实验亮点

实验结果表明，APULSE算法在无人地面车辆（UGV）规划场景中，相较于现有算法，在速度和鲁棒性上均有显著提升。APULSE能够始终找到接近最优的解决方案，同时速度提高了几个数量级，尤其是在竞争方法失败的大型问题实例上。具体性能数据未知，但结果表明APULSE具有卓越的可扩展性。

## 🎯 应用场景

APULSE算法在资源约束最短路径问题（RCSPP）领域具有广泛的应用前景，尤其适用于需要处理大规模稠密图的场景，如无人地面车辆（UGV）的任务规划、网络路由优化、交通流量控制、物流配送等。该算法能够实现交互式决策支持和动态重规划，提高系统的效率和鲁棒性，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> The resource-constrained shortest path problem (RCSPP) is a fundamental NP-hard optimization challenge with broad applications, from network routing to autonomous navigation. This problem involves finding a path that minimizes a primary cost subject to a budget on a secondary resource. While various RCSPP solvers exist, they often face critical scalability limitations when applied to the large, dense graphs characteristic of complex, real-world scenarios, making them impractical for time-critical planning. This challenge is particularly acute in domains like mission planning for unmanned ground vehicles (UGVs), which demand solutions on large-scale terrain graphs. This paper introduces APULSE, a hybrid label-setting algorithm designed to efficiently solve the RCSPP on such challenging graphs. APULSE integrates a best-first search guided by an A* heuristic with aggressive, Pulse-style pruning mechanisms and a time-bucketing strategy for effective state-space reduction. A computational study, using a large-scale UGV planning scenario, benchmarks APULSE against state-of-the-art algorithms. The results demonstrate that APULSE consistently finds near-optimal solutions while being orders of magnitude faster and more robust, particularly on large problem instances where competing methods fail. This superior scalability establishes APULSE as an effective solution for RCSPP in complex, large-scale environments, enabling capabilities such as interactive decision support and dynamic replanning.

