---
layout: default
title: HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data
---

# HiMaCon: Discovering Hierarchical Manipulation Concepts from Unlabeled Multi-Modal Data

**arXiv**: [2510.11321v1](https://arxiv.org/abs/2510.11321) | [PDF](https://arxiv.org/pdf/2510.11321.pdf)

**作者**: Ruizhe Liu, Pei Zhou, Qian Luo, Li Sun, Jun Cen, Yibing Song, Yanchao Yang

---

## 💡 一句话要点

**提出自监督框架HiMaCon，从无标签多模态数据学习层次化操作概念以提升机器人泛化能力**

**关键词**: `机器人操作` `自监督学习` `层次化表示` `多模态数据` `时序抽象` `泛化能力`

## 📋 核心要点

1. 核心问题：机器人操作需捕捉跨环境和任务的不变交互模式以实现有效泛化
2. 方法要点：结合跨模态相关网络和多尺度时序预测器，无监督学习层次化操作概念
3. 实验或效果：在仿真和真实部署中，概念增强策略显著提升性能，概念类似人类可解释原语

## 📄 摘要（原文）

> Effective generalization in robotic manipulation requires representations
> that capture invariant patterns of interaction across environments and tasks.
> We present a self-supervised framework for learning hierarchical manipulation
> concepts that encode these invariant patterns through cross-modal sensory
> correlations and multi-level temporal abstractions without requiring human
> annotation. Our approach combines a cross-modal correlation network that
> identifies persistent patterns across sensory modalities with a multi-horizon
> predictor that organizes representations hierarchically across temporal scales.
> Manipulation concepts learned through this dual structure enable policies to
> focus on transferable relational patterns while maintaining awareness of both
> immediate actions and longer-term goals. Empirical evaluation across simulated
> benchmarks and real-world deployments demonstrates significant performance
> improvements with our concept-enhanced policies. Analysis reveals that the
> learned concepts resemble human-interpretable manipulation primitives despite
> receiving no semantic supervision. This work advances both the understanding of
> representation learning for manipulation and provides a practical approach to
> enhancing robotic performance in complex scenarios.

