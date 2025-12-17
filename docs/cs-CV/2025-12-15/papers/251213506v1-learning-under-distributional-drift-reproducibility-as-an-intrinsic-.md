---
layout: default
title: Learning under Distributional Drift: Reproducibility as an Intrinsic Statistical Resource
---

# Learning under Distributional Drift: Reproducibility as an Intrinsic Statistical Resource

**arXiv**: [2512.13506v1](https://arxiv.org/abs/2512.13506) | [PDF](https://arxiv.org/pdf/2512.13506.pdf)

**作者**: Sofiya Zaichyk

---

## 💡 一句话要点

**提出可重复性预算以量化分布漂移下的统计学习极限**

**关键词**: `分布漂移` `统计可重复性` `Fisher-Rao度量` `泛化界` `极小极大最优` `自适应数据分析`

## 📋 核心要点

1. 核心问题：分布漂移导致经典泛化界失效，需量化系统统计可重复性
2. 方法要点：定义可重复性预算为Fisher-Rao路径长度，推导最优泛化界
3. 实验或效果：证明该界为极小极大最优，建立可重复性速度极限

## 📄 摘要（原文）

> Statistical learning under distributional drift remains insufficiently characterized: when each observation alters the data-generating law, classical generalization bounds can collapse. We introduce a new statistical primitive, the reproducibility budget $C_T$, which quantifies a system's finite capacity for statistical reproducibility - the extent to which its sampling process can remain governed by a consistent underlying distribution in the presence of both exogenous change and endogenous feedback. Formally, $C_T$ is defined as the cumulative Fisher-Rao path length of the coupled learner-environment evolution, measuring the total distributional motion accumulated during learning. From this construct we derive a drift-feedback generalization bound of order $O(T^{-1/2} + C_T/T)$, and we prove a matching minimax lower bound showing that this rate is minimax-optimal. Consequently, the results establish a reproducibility speed limit: no algorithm can achieve smaller worst-case generalization error than that imposed by the average Fisher-Rao drift rate $C_T/T$ of the data-generating process. The framework situates exogenous drift, adaptive data analysis, and performative prediction within a common geometric structure, with $C_T$ emerging as the intrinsic quantity measuring distributional motion across these settings.

