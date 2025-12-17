---
layout: default
title: Bi-level Meta-Policy Control for Dynamic Uncertainty Calibration in Evidential Deep Learning
---

# Bi-level Meta-Policy Control for Dynamic Uncertainty Calibration in Evidential Deep Learning

**arXiv**: [2510.08938v1](https://arxiv.org/abs/2510.08938) | [PDF](https://arxiv.org/pdf/2510.08938.pdf)

**作者**: Zhen Yang, Yansong Ma, Lei Chen

---

## 💡 一句话要点

**提出元策略控制器以解决动态数据分布下不确定性校准问题**

**关键词**: `元学习` `不确定性校准` `证据深度学习` `双层优化` `Dirichlet先验`

## 📋 核心要点

1. 传统EDL依赖静态超参数，在动态数据分布中校准和泛化能力差
2. 采用双层优化：内层动态配置损失函数，外层策略网络优化KL系数和Dirichlet先验
3. 实验显示显著提升不确定性校准、预测准确性和置信度样本拒绝后性能

## 📄 摘要（原文）

> Traditional Evidence Deep Learning (EDL) methods rely on static
> hyperparameter for uncertainty calibration, limiting their adaptability in
> dynamic data distributions, which results in poor calibration and
> generalization in high-risk decision-making tasks. To address this limitation,
> we propose the Meta-Policy Controller (MPC), a dynamic meta-learning framework
> that adjusts the KL divergence coefficient and Dirichlet prior strengths for
> optimal uncertainty modeling. Specifically, MPC employs a bi-level optimization
> approach: in the inner loop, model parameters are updated through a dynamically
> configured loss function that adapts to the current training state; in the
> outer loop, a policy network optimizes the KL divergence coefficient and
> class-specific Dirichlet prior strengths based on multi-objective rewards
> balancing prediction accuracy and uncertainty quality. Unlike previous methods
> with fixed priors, our learnable Dirichlet prior enables flexible adaptation to
> class distributions and training dynamics. Extensive experimental results show
> that MPC significantly enhances the reliability and calibration of model
> predictions across various tasks, improving uncertainty calibration, prediction
> accuracy, and performance retention after confidence-based sample rejection.

