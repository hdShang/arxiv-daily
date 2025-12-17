---
layout: default
title: On the Convergence of Density-Based Predictive Control for Multi-Agent Non-Uniform Area Coverage
---

# On the Convergence of Density-Based Predictive Control for Multi-Agent Non-Uniform Area Coverage

**arXiv**: [2512.02367v1](https://arxiv.org/abs/2512.02367) | [PDF](https://arxiv.org/pdf/2512.02367.pdf)

**作者**: Sungjun Seo, Kooktae Lee

---

## 💡 一句话要点

**提出密度预测控制以解决多智能体非均匀区域覆盖问题**

**关键词**: `多智能体控制` `非均匀区域覆盖` `最优传输理论` `密度预测控制` `Wasserstein距离` `收敛分析`

## 📋 核心要点

1. 核心问题：传统均匀覆盖无法适应大规模场景中区域优先级变化，如搜救或环境监测。
2. 方法要点：基于最优传输理论，利用参考分布分配智能体覆盖努力，在高优先级区域投入更多时间。
3. 实验或效果：通过一阶动力学和线性化四旋翼模型仿真，轨迹紧密匹配非均匀参考分布，优于现有方法。

## 📄 摘要（原文）

> This paper presents Density-based Predictive Control (DPC), a novel multi-agent control strategy for efficient non-uniform area coverage, grounded in optimal transport theory. In large-scale scenarios such as search and rescue or environmental monitoring, traditional uniform coverage fails to account for varying regional priorities. DPC leverages a pre-constructed reference distribution to allocate agents' coverage efforts, spending more time in high-priority or densely sampled regions. We analyze convergence conditions using the Wasserstein distance, derive an analytic optimal control law for unconstrained cases, and propose a numerical method for constrained scenarios. Simulations on first-order dynamics and linearized quadrotor models demonstrate that DPC achieves trajectories closely matching the non-uniform reference distribution, outperforming existing coverage methods.

