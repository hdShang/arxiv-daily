---
layout: default
title: A segment anchoring-based balancing algorithm for agricultural multi-robot task allocation with energy constraints
---

# A segment anchoring-based balancing algorithm for agricultural multi-robot task allocation with energy constraints

**arXiv**: [2511.17076v1](https://arxiv.org/abs/2511.17076) | [PDF](https://arxiv.org/pdf/2511.17076.pdf)

**作者**: Peng Chen, Jing Liang, Kang-Jia Qiao, Hui Song, Tian-lei Ma, Kun-Jie Yu, Cai-Tong Yue, Ponnuthurai Nagaratnam Suganthan, Witold Pedryc

---

## 💡 一句话要点

**提出分段锚定平衡算法以解决农业多机器人能量约束任务分配问题**

**关键词**: `多机器人系统` `任务分配` `能量约束` `优化算法` `智能农业` `调度问题`

## 📋 核心要点

1. 核心问题：能量约束下多机器人任务分配中，充电导致负载重置和调度中断。
2. 方法要点：结合顺序锚定和比例分割机制，重构路径并优化完工时间。
3. 实验或效果：在真实案例和基准测试中，优于6种先进算法收敛性和多样性。

## 📄 摘要（原文）

> Multi-robot systems have emerged as a key technology for addressing the efficiency and cost challenges in labor-intensive industries. In the representative scenario of smart farming, planning efficient harvesting schedules for a fleet of electric robots presents a highly challenging frontier problem. The complexity arises not only from the need to find Pareto-optimal solutions for the conflicting objectives of makespan and transportation cost, but also from the necessity to simultaneously manage payload constraints and finite battery capacity. When robot loads are dynamically updated during planned multi-trip operations, a mandatory recharge triggered by energy constraints introduces an unscheduled load reset. This interaction creates a complex cascading effect that disrupts the entire schedule and renders traditional optimization methods ineffective. To address this challenge, this paper proposes the segment anchoring-based balancing algorithm (SABA). The core of SABA lies in the organic combination of two synergistic mechanisms: the sequential anchoring and balancing mechanism, which leverages charging decisions as `anchors' to systematically reconstruct disrupted routes, while the proportional splitting-based rebalancing mechanism is responsible for the fine-grained balancing and tuning of the final solutions' makespans. Extensive comparative experiments, conducted on a real-world case study and a suite of benchmark instances, demonstrate that SABA comprehensively outperforms 6 state-of-the-art algorithms in terms of both solution convergence and diversity. This research provides a novel theoretical perspective and an effective solution for the multi-robot task allocation problem under energy constraints.

