---
layout: default
title: A Theoretical Framework for Discovering Groups and Unitary Representations via Tensor Factorization
---

# A Theoretical Framework for Discovering Groups and Unitary Representations via Tensor Factorization

**arXiv**: [2511.23152v1](https://arxiv.org/abs/2511.23152) | [PDF](https://arxiv.org/pdf/2511.23152.pdf)

**作者**: Dongsung Huh, Halyun Jeong

---

## 💡 一句话要点

**提出超立方体模型，通过张量分解发现群结构及其酉表示。**

**关键词**: `张量分解` `群发现` `酉表示` `超立方体模型` `共线流形`

## 📋 核心要点

1. 核心问题：如何从数据中自动发现群结构和其酉表示。
2. 方法要点：分解目标函数为尺度调节项和方向对齐项，隔离共线流形。
3. 实验或效果：证明共线流形仅允许群同位素解，并在共线性主导下实现全局最小。

## 📄 摘要（原文）

> We analyze the HyperCube model, an \textit{operator-valued} tensor factorization architecture that discovers group structures and their unitary representations. We provide a rigorous theoretical explanation for this inductive bias by decomposing its objective into a term regulating factor scales ($\mathcal{B}$) and a term enforcing directional alignment ($\mathcal{R} \geq 0$). This decomposition isolates the \textit{collinear manifold} ($\mathcal{R}=0$), to which numerical optimization consistently converges for group isotopes. We prove that this manifold admits feasible solutions exclusively for group isotopes, and that within it, $\mathcal{B}$ exerts a variational pressure toward unitarity. To bridge the gap to the global landscape, we formulate a \textit{Collinearity Dominance Conjecture}, supported by empirical observations. Conditional on this dominance, we prove two key results: (1) the global minimum is achieved by the unitary regular representation for groups, and (2) non-group operations incur a strictly higher objective value, formally quantifying the model's inductive bias toward the associative structure of groups (up to isotopy).

