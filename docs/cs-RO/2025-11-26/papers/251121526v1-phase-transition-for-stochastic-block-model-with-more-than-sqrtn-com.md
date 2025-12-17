---
layout: default
title: Phase Transition for Stochastic Block Model with more than $\sqrt{n}$ Communities (II)
---

# Phase Transition for Stochastic Block Model with more than $\sqrt{n}$ Communities (II)

**arXiv**: [2511.21526v1](https://arxiv.org/abs/2511.21526) | [PDF](https://arxiv.org/pdf/2511.21526.pdf)

**作者**: Alexandra Carpentier, Christophe Giraud, Nicolas Verzelen

---

## 💡 一句话要点

**提出基于 motif 计数的方法，在 SBM 多社区场景中实现社区恢复**

**关键词**: `随机块模型` `社区检测` `计算复杂性` `motif 计数` `多项式时间算法`

## 📋 核心要点

1. 研究 SBM 中社区数 K≥√n 时的计算障碍与恢复条件
2. 构建特定结构 motif 并证明其计数可实现社区恢复
3. 在适度稀疏设置中验证方法有效性，优于谱方法

## 📄 摘要（原文）

> A fundamental theoretical question in network analysis is to determine under which conditions community recovery is possible in polynomial time in the Stochastic Block Model (SBM). When the number $K$ of communities remains smaller than $\sqrt{n}$ --where $n$ denotes the number of nodes--, non-trivial community recovery is possible in polynomial time above, and only above, the Kesten--Stigum (KS) threshold, originally postulated using arguments from statistical physics.
>   When $K \geq \sqrt{n}$, Chin, Mossel, Sohn, and Wein recently proved that, in the \emph{sparse regime}, community recovery in polynomial time is achievable below the KS threshold by counting non-backtracking paths. This finding led them to postulate a new threshold for the many-communities regime $K \geq \sqrt{n}$. Subsequently, Carpentier, Giraud, and Verzelen established the failure of low-degree polynomials below this new threshold across all density regimes, and demonstrated successful recovery above the threshold in certain moderately sparse settings. While these results provide strong evidence that, in the many community setting, the computational barrier lies at the threshold proposed in~Chin et al., the question of achieving recovery above this threshold still remains open in most density regimes.
>   The present work is a follow-up to~Carpentier et al., in which we prove Conjecture~1.4 stated therein by: \\ 1- Constructing a family of motifs satisfying specific structural properties; and\\ 2- Proving that community recovery is possible above the proposed threshold by counting such motifs.\\ Our results complete the picture of the computational barrier for community recovery in the SBM with $K \geq \sqrt{n}$ communities. They also indicate that, in moderately sparse regimes, the optimal algorithms appear to be fundamentally different from spectral methods.

