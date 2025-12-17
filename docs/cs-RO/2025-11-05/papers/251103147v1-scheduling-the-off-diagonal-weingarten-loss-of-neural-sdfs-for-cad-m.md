---
layout: default
title: Scheduling the Off-Diagonal Weingarten Loss of Neural SDFs for CAD Models
---

# Scheduling the Off-Diagonal Weingarten Loss of Neural SDFs for CAD Models

**arXiv**: [2511.03147v1](https://arxiv.org/abs/2511.03147) | [PDF](https://arxiv.org/pdf/2511.03147.pdf)

**作者**: Haotian Yin, Przemyslaw Musialski

---

## 💡 一句话要点

**提出ODW损失调度策略以优化CAD模型的神经SDF重建**

**关键词**: `神经符号距离函数` `CAD模型重建` `曲率正则化` `损失调度` `几何优化`

## 📋 核心要点

1. 神经SDF在CAD重建中需正则化抑制伪影，但固定权重限制细节恢复。
2. 引入时间变化调度策略，初始高权重稳定优化，后衰减以促进精细重构。
3. 实验显示调度策略在ABC数据集上优于固定权重，Chamfer距离提升达35%。

## 📄 摘要（原文）

> Neural signed distance functions (SDFs) have become a powerful representation
> for geometric reconstruction from point clouds, yet they often require both
> gradient- and curvature-based regularization to suppress spurious warp and
> preserve structural fidelity. FlatCAD introduced the Off-Diagonal Weingarten
> (ODW) loss as an efficient second-order prior for CAD surfaces, approximating
> full-Hessian regularization at roughly half the computational cost. However,
> FlatCAD applies a fixed ODW weight throughout training, which is suboptimal:
> strong regularization stabilizes early optimization but suppresses detail
> recovery in later stages. We present scheduling strategies for the ODW loss
> that assign a high initial weight to stabilize optimization and progressively
> decay it to permit fine-scale refinement. We investigate constant, linear,
> quintic, and step interpolation schedules, as well as an increasing warm-up
> variant. Experiments on the ABC CAD dataset demonstrate that time-varying
> schedules consistently outperform fixed weights. Our method achieves up to a
> 35% improvement in Chamfer Distance over the FlatCAD baseline, establishing
> scheduling as a simple yet effective extension of curvature regularization for
> robust CAD reconstruction.

