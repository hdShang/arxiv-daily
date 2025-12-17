---
layout: default
title: A Fast Heuristic Search Approach for Energy-Optimal Profile Routing for Electric Vehicles
---

# A Fast Heuristic Search Approach for Energy-Optimal Profile Routing for Electric Vehicles

**arXiv**: [2512.01331v1](https://arxiv.org/abs/2512.01331) | [PDF](https://arxiv.org/pdf/2512.01331.pdf)

**作者**: Saman Ahmadi, Mahdi Jalili

---

## 💡 一句话要点

**提出基于多目标A*搜索的标签设置方法，以解决电动汽车在不确定初始能量下的能量最优路径规划问题。**

**关键词**: `电动汽车路径规划` `能量最优搜索` `多目标A*算法` `轮廓支配规则` `标签设置方法` `大规模路网`

## 📋 核心要点

1. 研究电动汽车在大规模路网中的能量最优最短路径问题，考虑下坡段能量回收导致的负能量成本。
2. 提出基于多目标A*搜索的标签设置方法，采用新颖的轮廓支配规则，避免处理复杂轮廓。
3. 在真实路网和能量消耗数据上评估四种方法变体，性能接近已知初始能量水平的能量最优A*搜索。

## 📄 摘要（原文）

> We study the energy-optimal shortest path problem for electric vehicles (EVs) in large-scale road networks, where recuperated energy along downhill segments introduces negative energy costs. While traditional point-to-point pathfinding algorithms for EVs assume a known initial energy level, many real-world scenarios involving uncertainty in available energy require planning optimal paths for all possible initial energy levels, a task known as energy-optimal profile search. Existing solutions typically rely on specialized profile-merging procedures within a label-correcting framework that results in searching over complex profiles. In this paper, we propose a simple yet effective label-setting approach based on multi-objective A* search, which employs a novel profile dominance rule to avoid generating and handling complex profiles. We develop four variants of our method and evaluate them on real-world road networks enriched with realistic energy consumption data. Experimental results demonstrate that our energy profile A* search achieves performance comparable to energy-optimal A* with a known initial energy level.

