---
layout: default
title: Contextual Dynamic Pricing with Heterogeneous Buyers
---

# Contextual Dynamic Pricing with Heterogeneous Buyers

**arXiv**: [2512.09513v1](https://arxiv.org/abs/2512.09513) | [PDF](https://arxiv.org/pdf/2512.09513.pdf)

**作者**: Thodoris Lykouris, Sloan Nietert, Princewill Okoroafor, Chara Podimata, Julian Zimmert

---

## 💡 一句话要点

**提出基于乐观后验采样的上下文动态定价算法，处理异质买家场景，实现次优后悔界。**

**关键词**: `动态定价` `异质买家` `上下文学习` `后悔界分析` `后验采样`

## 📋 核心要点

1. 研究异质买家下的上下文动态定价问题，买家估值类型来自未知有限分布。
2. 开发乐观后验采样算法，后悔界为Õ(K⋆√dT)，在d和T上紧致。
3. 非上下文场景中提出方差感知缩放算法，优化对K⋆的依赖。

## 📄 摘要（原文）

> We initiate the study of contextual dynamic pricing with a heterogeneous population of buyers, where a seller repeatedly posts prices (over $T$ rounds) that depend on the observable $d$-dimensional context and receives binary purchase feedback. Unlike prior work assuming homogeneous buyer types, in our setting the buyer's valuation type is drawn from an unknown distribution with finite support size $K_{\star}$. We develop a contextual pricing algorithm based on optimistic posterior sampling with regret $\widetilde{O}(K_{\star}\sqrt{dT})$, which we prove to be tight in $d$ and $T$ up to logarithmic terms. Finally, we refine our analysis for the non-contextual pricing case, proposing a variance-aware zooming algorithm that achieves the optimal dependence on $K_{\star}$.

