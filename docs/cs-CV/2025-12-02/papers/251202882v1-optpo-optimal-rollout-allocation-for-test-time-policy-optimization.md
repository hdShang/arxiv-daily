---
layout: default
title: OptPO: Optimal Rollout Allocation for Test-time Policy Optimization
---

# OptPO: Optimal Rollout Allocation for Test-time Policy Optimization

**arXiv**: [2512.02882v1](https://arxiv.org/abs/2512.02882) | [PDF](https://arxiv.org/pdf/2512.02882.pdf)

**作者**: Youkang Wang, Jian Wang, Rubing Chen, Tianyi Zeng, Xiao-Yong Wei, Qing Li

---

## 💡 一句话要点

**提出OptPO框架，通过自适应分配推理预算以优化测试时策略学习效率。**

**关键词**: `测试时策略优化` `贝叶斯序贯检验` `自适应推理预算` `大语言模型` `无监督学习`

## 📋 核心要点

1. 核心问题：现有测试时策略优化方法依赖固定预算多数投票，导致计算冗余。
2. 方法要点：将投票过程建模为贝叶斯序贯概率比检验，动态停止采样以提升效率。
3. 实验或效果：在多样推理基准上，显著减少rollout开销，同时保持或提高准确性。

## 📄 摘要（原文）

> Test-time policy optimization enables large language models (LLMs) to adapt to distribution shifts by leveraging feedback from self-generated rollouts. However, existing methods rely on fixed-budget majority voting to estimate rewards, incurring substantial computational redundancy. We propose Optimal Rollout Allocation for Test-time Policy Optimization (OptPO), a principled framework that adaptively allocates inference budgets. By formulating the voting process as a Bayesian sequential probability ratio test, OptPO dynamically halts sampling once the posterior confidence in a consensus answer exceeds a specified threshold. Crucially, it utilizes the retained rollouts for on-policy updates, seamlessly integrating with algorithms like PPO or GRPO without requiring ground-truth labels. Across diverse reasoning benchmarks, OptPO significantly reduces rollout overhead compared to fixed-sample baselines while preserving or improving accuracy. By unifying statistically optimal stopping with test-time learning, OptPO offers a computationally efficient paradigm for test-time adaptation. The source code will be open upon acceptance at https://open-upon-acceptance.

