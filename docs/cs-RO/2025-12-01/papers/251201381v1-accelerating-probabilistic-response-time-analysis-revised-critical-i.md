---
layout: default
title: Accelerating Probabilistic Response-Time Analysis: Revised Critical Instant and Optimized Convolution
---

# Accelerating Probabilistic Response-Time Analysis: Revised Critical Instant and Optimized Convolution

**arXiv**: [2512.01381v1](https://arxiv.org/abs/2512.01381) | [PDF](https://arxiv.org/pdf/2512.01381.pdf)

**作者**: Hiroto Takahashi, Atsushi Yano, Takuya Azumi

---

## 💡 一句话要点

**提出优化卷积方法以加速概率响应时间分析，提高安全关键实时系统的效率与可靠性**

**关键词**: `概率响应时间分析` `最坏情况截止期限失败概率` `临界时刻` `卷积优化` `安全关键实时系统`

## 📋 核心要点

1. 核心问题：概率设置下传统临界时刻假设可能导致最坏情况截止期限失败概率低估，且高精度估计计算成本高
2. 方法要点：采用修订临界时刻公式，并优化卷积合并顺序以加速计算
3. 实验或效果：实验显示优化聚合卷积比顺序卷积计算时间减少高达一个数量级，同时保持准确安全估计

## 📄 摘要（原文）

> Accurate estimation of the Worst-Case Deadline Failure Probability (WCDFP) has attracted growing attention as a means to provide safety assurances in complex systems such as robotic platforms and autonomous vehicles. WCDFP quantifies the likelihood of deadline misses under the most pessimistic operating conditions, and safe estimation is essential for dependable real-time applications. However, achieving high accuracy in WCDFP estimation often incurs significant computational cost. Recent studies have revealed that the classical assumption of the critical instant, the activation pattern traditionally considered to trigger the worst-case behavior, can lead to underestimation of WCDFP in probabilistic settings. This observation motivates the use of a revised critical instant formulation that more faithfully captures the true worst-case scenario. This paper investigates convolution-based methods for WCDFP estimation under this revised setting and proposes an optimization technique that accelerates convolution by improving the merge order. Extensive experiments with diverse execution-time distributions demonstrate that the proposed optimized Aggregate Convolution reduces computation time by up to an order of magnitude compared to Sequential Convolution, while retaining accurate and safe-sided WCDFP estimates. These results highlight the potential of the approach to provide both efficiency and reliability in probabilistic timing analysis for safety-critical real-time applications.

