---
layout: default
title: Branching Strategies Based on Subgraph GNNs: A Study on Theoretical Promise versus Practical Reality
---

# Branching Strategies Based on Subgraph GNNs: A Study on Theoretical Promise versus Practical Reality

**arXiv**: [2512.09355v1](https://arxiv.org/abs/2512.09355) | [PDF](https://arxiv.org/pdf/2512.09355.pdf)

**作者**: Junru Zhou, Yicheng Wang, Pan Li

---

## 💡 一句话要点

**研究子图GNN在MILP分支选择中的理论优势与实践局限**

**关键词**: `图神经网络` `混合整数线性规划` `分支策略` `表达能力` `计算效率` `子图GNN`

## 📋 核心要点

1. 核心问题：标准MPNN表达能力不足，高阶GNN计算成本高，需平衡表达力与效率。
2. 方法要点：证明节点锚定子图GNN（低于3-WL表达能力）足以近似强分支分数。
3. 实验或效果：实证显示子图GNN因O(n)复杂度导致内存瓶颈和求解时间慢于MPNN和启发式方法。

## 📄 摘要（原文）

> Graph Neural Networks (GNNs) have emerged as a promising approach for ``learning to branch'' in Mixed-Integer Linear Programming (MILP). While standard Message-Passing GNNs (MPNNs) are efficient, they theoretically lack the expressive power to fully represent MILP structures. Conversely, higher-order GNNs (like 2-FGNNs) are expressive but computationally prohibitive. In this work, we investigate Subgraph GNNs as a theoretical middle ground. Crucially, while previous work [Chen et al., 2025] demonstrated that GNNs with 3-WL expressive power can approximate Strong Branching, we prove a sharper result: node-anchored Subgraph GNNs whose expressive power is strictly lower than 3-WL [Zhang et al., 2023] are sufficient to approximate Strong Branching scores. However, our extensive empirical evaluation on four benchmark datasets reveals a stark contrast between theory and practice. While node-anchored Subgraph GNNs theoretically offer superior branching decisions, their $O(n)$ complexity overhead results in significant memory bottlenecks and slower solving times than MPNNs and heuristics. Our results indicate that for MILP branching, the computational cost of expressive GNNs currently outweighs their gains in decision quality, suggesting that future research must focus on efficiency-preserving expressivity.

