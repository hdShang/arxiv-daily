---
layout: default
title: Symmetry-Aware Steering of Equivariant Diffusion Policies: Benefits and Limits
---

# Symmetry-Aware Steering of Equivariant Diffusion Policies: Benefits and Limits

**arXiv**: [2512.11345v1](https://arxiv.org/abs/2512.11345) | [PDF](https://arxiv.org/pdf/2512.11345.pdf)

**作者**: Minwoo Park, Junwoo Chang, Jongeun Choi, Roberto Horowitz

---

## 💡 一句话要点

**提出对称感知引导框架以提升等变扩散策略的强化学习效率与稳定性**

**关键词**: `等变扩散策略` `对称感知引导` `强化学习` `样本效率` `几何对称性` `策略改进`

## 📋 核心要点

1. 核心问题：标准强化学习引导等变扩散策略时忽略对称性，导致样本效率低且不稳定
2. 方法要点：理论证明等变扩散过程的等变性，构建群不变潜在噪声MDP，提出对称感知引导框架
3. 实验或效果：在对称性程度不同的任务中验证，对称感知引导显著提升样本效率、防止价值发散、改善策略

## 📄 摘要（原文）

> Equivariant diffusion policies (EDPs) combine the generative expressivity of diffusion models with the strong generalization and sample efficiency afforded by geometric symmetries. While steering these policies with reinforcement learning (RL) offers a promising mechanism for fine-tuning beyond demonstration data, directly applying standard (non-equivariant) RL can be sample-inefficient and unstable, as it ignores the symmetries that EDPs are designed to exploit. In this paper, we theoretically establish that the diffusion process of an EDP is equivariant, which in turn induces a group-invariant latent-noise MDP that is well-suited for equivariant diffusion steering. Building on this theory, we introduce a principled symmetry-aware steering framework and compare standard, equivariant, and approximately equivariant RL strategies through comprehensive experiments across tasks with varying degrees of symmetry. While we identify the practical boundaries of strict equivariance under symmetry breaking, we show that exploiting symmetry during the steering process yields substantial benefits-enhancing sample efficiency, preventing value divergence, and achieving strong policy improvements even when EDPs are trained from extremely limited demonstrations.

