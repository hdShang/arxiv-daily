---
layout: default
title: A Mathematical Theory of Top-$k$ Sparse Attention via Total Variation Distance
---

# A Mathematical Theory of Top-$k$ Sparse Attention via Total Variation Distance

**arXiv**: [2512.07647v1](https://arxiv.org/abs/2512.07647) | [PDF](https://arxiv.org/pdf/2512.07647.pdf)

**作者**: Georgios Tzachristas, Lei Deng, Ioannis Tzachristas, Gong Zhang, Renhai Chen

---

## 💡 一句话要点

**提出基于总变差距离的Top-k稀疏注意力数学理论，量化截断误差并提供确定性边界。**

**关键词**: `注意力机制` `稀疏注意力` `总变差距离` `数学理论` `误差分析` `Top-k截断`

## 📋 核心要点

1. 核心问题：Top-k注意力截断的近似误差缺乏统一数学框架与确定性边界。
2. 方法要点：利用总变差距离量化分布与输出误差，推导非渐近边界及头尾分解公式。
3. 实验或效果：在BERT和合成数据上验证理论，平均减少2-4倍键值计算并满足误差预算。

## 📄 摘要（原文）

> We develop a unified mathematical framework for certified Top-$k$ attention truncation that quantifies approximation error at both the distribution and output levels. For a single attention distribution $P$ and its Top-$k$ truncation $\hat P$, we show that the total-variation distance coincides with the discarded softmax tail mass and satisfies $\mathrm{TV}(P,\hat P)=1-e^{-\mathrm{KL}(\hat P\Vert P)}$, yielding sharp Top-$k$-specific bounds in place of generic inequalities. From this we derive non-asymptotic deterministic bounds -- from a single boundary gap through multi-gap and blockwise variants -- that control $\mathrm{TV}(P,\hat P)$ using only the ordered logits. Using an exact head-tail decomposition, we prove that the output error factorizes as $\\|\mathrm{Attn}(q,K,V)-\mathrm{Attn}_k(q,K,V)\\|_2=τ\\|μ_{\mathrm{tail}}-μ_{\mathrm{head}}\\|_2$ with $τ=\mathrm{TV}(P,\hat P)$, yielding a new head-tail diameter bound $\\|\mathrm{Attn}(q,K,V)-\mathrm{Attn}_k(q,K,V)\\|_2\leτ\,\mathrm{diam}_{H,T}$ and refinements linking the error to $\mathrm{Var}_P(V)$. Under an i.i.d. Gaussian score model $s_i\sim\mathcal N(μ,σ^2)$ we derive closed-form tail masses and an asymptotic rule for the minimal $k_\varepsilon$ ensuring $\mathrm{TV}(P,\hat P)\le\varepsilon$, namely $k_\varepsilon/n\approxΦ_c(σ+Φ^{-1}(\varepsilon))$. Experiments on bert-base-uncased and synthetic logits confirm the predicted scaling of $k_\varepsilon/n$ and show that certified Top-$k$ can reduce scored keys by 2-4$\times$ on average while meeting the prescribed total-variation budget.

