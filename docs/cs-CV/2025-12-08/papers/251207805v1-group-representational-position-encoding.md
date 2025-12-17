---
layout: default
title: Group Representational Position Encoding
---

# Group Representational Position Encoding

**arXiv**: [2512.07805v1](https://arxiv.org/abs/2512.07805) | [PDF](https://arxiv.org/pdf/2512.07805.pdf)

**作者**: Yifan Zhang, Zixiang Chen, Yifeng Liu, Zhen Qin, Huizhuo Yuan, Kangping Xu, Yang Yuan, Quanquan Gu, Andrew Chi-Chih Yao

---

## 💡 一句话要点

**提出GRAPE统一框架，基于群作用统一位置编码，涵盖RoPE和ALiBi等机制。**

**关键词**: `位置编码` `群作用` `长上下文模型` `相对位置编码` `统一框架`

## 📋 核心要点

1. 核心问题：统一位置编码机制，解决长上下文模型中的位置几何设计问题。
2. 方法要点：基于群作用，包括乘法旋转和加法对数偏置，支持相对、组合和规范保持映射。
3. 实验或效果：GRAPE扩展了RoPE和ALiBi，提供原则性设计空间，具体效果未知。

## 📄 摘要（原文）

> We present GRAPE (Group RepresentAtional Position Encoding), a unified framework for positional encoding based on group actions. GRAPE brings together two families of mechanisms: (i) multiplicative rotations (Multiplicative GRAPE) in $\mathrm{SO}(d)$ and (ii) additive logit biases (Additive GRAPE) arising from unipotent actions in the general linear group $\mathrm{GL}$. In Multiplicative GRAPE, a position $n \in \mathbb{Z}$ (or $t \in \mathbb{R}$) acts as $\mathbf{G}(n)=\exp(n\,ω\,\mathbf{L})$ with a rank-2 skew generator $\mathbf{L} \in \mathbb{R}^{d \times d}$, yielding a relative, compositional, norm-preserving map with a closed-form matrix exponential. RoPE is recovered exactly when the $d/2$ planes are the canonical coordinate pairs with log-uniform spectrum. Learned commuting subspaces and compact non-commuting mixtures strictly extend this geometry to capture cross-subspace feature coupling at $O(d)$ and $O(r d)$ cost per head, respectively. In Additive GRAPE, additive logits arise as rank-1 (or low-rank) unipotent actions, recovering ALiBi and the Forgetting Transformer (FoX) as exact special cases while preserving an exact relative law and streaming cacheability. Altogether, GRAPE supplies a principled design space for positional geometry in long-context models, subsuming RoPE and ALiBi as special cases. Project Page: https://github.com/model-architectures/GRAPE.

