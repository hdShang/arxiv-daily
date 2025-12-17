---
layout: default
title: On Flow Matching KL Divergence
---

# On Flow Matching KL Divergence

**arXiv**: [2511.05480v1](https://arxiv.org/abs/2511.05480) | [PDF](https://arxiv.org/pdf/2511.05480.pdf)

**作者**: Maojiang Su, Jerry Yao-Chieh Hu, Sophia Pi, Han Liu

---

## 💡 一句话要点

**提出流匹配KL散度上界，提升分布估计效率**

**关键词**: `流匹配` `KL散度上界` `分布估计` `统计收敛` `总变差距离` `极小极大效率`

## 📋 核心要点

1. 核心问题：流匹配分布近似的KL散度缺乏确定性上界。
2. 方法要点：基于L2流匹配损失推导KL散度上界，依赖数据与速度场正则性。
3. 实验或效果：数值研究验证理论，流匹配在TV距离下接近极小极大最优效率。

## 📄 摘要（原文）

> We derive a deterministic, non-asymptotic upper bound on the Kullback-Leibler
> (KL) divergence of the flow-matching distribution approximation. In particular,
> if the $L_2$ flow-matching loss is bounded by $\epsilon^2 > 0$, then the KL
> divergence between the true data distribution and the estimated distribution is
> bounded by $A_1 \epsilon + A_2 \epsilon^2$. Here, the constants $A_1$ and $A_2$
> depend only on the regularities of the data and velocity fields. Consequently,
> this bound implies statistical convergence rates of Flow Matching Transformers
> under the Total Variation (TV) distance. We show that, flow matching achieves
> nearly minimax-optimal efficiency in estimating smooth distributions. Our
> results make the statistical efficiency of flow matching comparable to that of
> diffusion models under the TV distance. Numerical studies on synthetic and
> learned velocities corroborate our theory.

