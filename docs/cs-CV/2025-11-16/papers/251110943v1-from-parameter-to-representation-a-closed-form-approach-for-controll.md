---
layout: default
title: From Parameter to Representation: A Closed-Form Approach for Controllable Model Merging
---

# From Parameter to Representation: A Closed-Form Approach for Controllable Model Merging

**arXiv**: [2511.10943v1](https://arxiv.org/abs/2511.10943) | [PDF](https://arxiv.org/pdf/2511.10943.pdf)

**作者**: Jialin Wu, Jian Yang, Handing Wang, Jiajun Wen, Zhiyong Yu

---

## 💡 一句话要点

**提出基于表示修正的闭式方法以解决可控模型合并的计算复杂度问题**

**关键词**: `可控模型合并` `表示修正` `闭式解` `多任务学习` `帕累托优化`

## 📋 核心要点

1. 核心问题：模型合并中参数干扰导致多任务性能权衡难以控制，现有方法离线优化复杂度高
2. 方法要点：将表示修正建模为最优线性变换，提供闭式解，实现单步架构无关计算
3. 实验或效果：生成更优帕累托前沿，偏好对齐更精确，计算成本大幅降低

## 📄 摘要（原文）

> Model merging combines expert models for multitask performance but faces challenges from parameter interference. This has sparked recent interest in controllable model merging, giving users the ability to explicitly balance performance trade-offs. Existing approaches employ a compile-then-query paradigm, performing a costly offline multi-objective optimization to enable fast, preference-aware model generation. This offline stage typically involves iterative search or dedicated training, with complexity that grows exponentially with the number of tasks. To overcome these limitations, we shift the perspective from parameter-space optimization to a direct correction of the model's final representation. Our approach models this correction as an optimal linear transformation, yielding a closed-form solution that replaces the entire offline optimization process with a single-step, architecture-agnostic computation. This solution directly incorporates user preferences, allowing a Pareto-optimal model to be generated on-the-fly with complexity that scales linearly with the number of tasks. Experimental results show our method generates a superior Pareto front with more precise preference alignment and drastically reduced computational cost.

