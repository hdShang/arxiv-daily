---
layout: default
title: FLYINGTRUST: A Benchmark for Quadrotor Navigation Across Scenarios and Vehicles
---

# FLYINGTRUST: A Benchmark for Quadrotor Navigation Across Scenarios and Vehicles

**arXiv**: [2510.26588v1](https://arxiv.org/abs/2510.26588) | [PDF](https://arxiv.org/pdf/2510.26588.pdf)

**作者**: Gang Li, Chunlei Zhai, Teng Wang, Shaun Li, Shangsong Jiang, Xiangwei Zhu

---

## 💡 一句话要点

**提出FLYINGTRUST基准，评估四旋翼导航在不同平台和场景下的鲁棒性。**

**关键词**: `四旋翼导航` `基准测试` `鲁棒性评估` `平台动力学` `场景几何` `视觉导航`

## 📋 核心要点

1. 四旋翼视觉导航算法在跨平台和场景时性能波动大，增加部署成本与风险。
2. 基准使用推力重量比和角加速度指标，结合多样化场景与平台进行标准化评估。
3. 实验揭示导航成功依赖平台能力和场景几何，算法偏好和失败模式各异。

## 📄 摘要（原文）

> Visual navigation algorithms for quadrotors often exhibit a large variation
> in performance when transferred across different vehicle platforms and scene
> geometries, which increases the cost and risk of field deployment. To support
> systematic early-stage evaluation, we introduce FLYINGTRUST, a high-fidelity,
> configurable benchmarking framework that measures how platform kinodynamics and
> scenario structure jointly affect navigation robustness. FLYINGTRUST models
> vehicle capability with two compact, physically interpretable indicators:
> maximum thrust-to-weight ratio and axis-wise maximum angular acceleration. The
> benchmark pairs a diverse scenario library with a heterogeneous set of real and
> virtual platforms and prescribes a standardized evaluation protocol together
> with a composite scoring method that balances scenario importance, platform
> importance and performance stability. We use FLYINGTRUST to compare
> representative optimization-based and learning-based navigation approaches
> under identical conditions, performing repeated trials per platform-scenario
> combination and reporting uncertainty-aware metrics. The results reveal
> systematic patterns: navigation success depends predictably on platform
> capability and scene geometry, and different algorithms exhibit distinct
> preferences and failure modes across the evaluated conditions. These
> observations highlight the practical necessity of incorporating both platform
> capability and scenario structure into algorithm design, evaluation, and
> selection, and they motivate future work on methods that remain robust across
> diverse platforms and scenarios.

