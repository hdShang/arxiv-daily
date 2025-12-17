---
layout: default
title: DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation
---

# DynaRend: Learning 3D Dynamics via Masked Future Rendering for Robotic Manipulation

**arXiv**: [2510.24261v1](https://arxiv.org/abs/2510.24261) | [PDF](https://arxiv.org/pdf/2510.24261.pdf)

**作者**: Jingyi Tian, Le Wang, Sanping Zhou, Sen Wang, Jiayi Li, Gang Hua

---

## 💡 一句话要点

**提出DynaRend框架，通过掩码未来渲染学习3D动态特征以提升机器人操作性能**

**关键词**: `机器人操作` `3D动态学习` `掩码渲染` `表示学习` `体积渲染` `动作价值预测`

## 📋 核心要点

1. 核心问题：机器人操作策略泛化性差，源于真实世界数据稀缺和现有方法难以联合学习几何、语义与动态
2. 方法要点：使用掩码重建和未来预测，通过可微分体积渲染学习3D感知的动态三平面特征
3. 实验或效果：在RLBench和Colosseum基准及真实实验中，显著提高策略成功率、泛化性和实际应用性

## 📄 摘要（原文）

> Learning generalizable robotic manipulation policies remains a key challenge
> due to the scarcity of diverse real-world training data. While recent
> approaches have attempted to mitigate this through self-supervised
> representation learning, most either rely on 2D vision pretraining paradigms
> such as masked image modeling, which primarily focus on static semantics or
> scene geometry, or utilize large-scale video prediction models that emphasize
> 2D dynamics, thus failing to jointly learn the geometry, semantics, and
> dynamics required for effective manipulation. In this paper, we present
> DynaRend, a representation learning framework that learns 3D-aware and
> dynamics-informed triplane features via masked reconstruction and future
> prediction using differentiable volumetric rendering. By pretraining on
> multi-view RGB-D video data, DynaRend jointly captures spatial geometry, future
> dynamics, and task semantics in a unified triplane representation. The learned
> representations can be effectively transferred to downstream robotic
> manipulation tasks via action value map prediction. We evaluate DynaRend on two
> challenging benchmarks, RLBench and Colosseum, as well as in real-world robotic
> experiments, demonstrating substantial improvements in policy success rate,
> generalization to environmental perturbations, and real-world applicability
> across diverse manipulation tasks.

