---
layout: default
title: Data Curation Through the Lens of Spectral Dynamics: Static Limits, Dynamic Acceleration, and Practical Oracles
---

# Data Curation Through the Lens of Spectral Dynamics: Static Limits, Dynamic Acceleration, and Practical Oracles

**arXiv**: [2512.02409v1](https://arxiv.org/abs/2512.02409) | [PDF](https://arxiv.org/pdf/2512.02409.pdf)

**作者**: Yizhou Zhang, Lun Du

---

## 💡 一句话要点

**提出基于谱动态的数据筛选理论，分析静态与动态策略对学习加速的影响。**

**关键词**: `数据筛选` `谱动态` `算子理论` `学习加速` `数据剪枝` `合成数据`

## 📋 核心要点

1. 核心问题：数据筛选策略如剪枝和合成数据对模型性能提升效果不一，缺乏理论解释。
2. 方法要点：将数据筛选形式化为采样分布重加权，映射到数据诱导算子的特征结构进行分析。
3. 实验或效果：静态剪枝仅有限改进，动态理想预言机可加速学习，但实际系统只能近似。

## 📄 摘要（原文）

> Large-scale neural models are increasingly trained with data pruning, synthetic data generation, cross-model distillation, reinforcement learning from human feedback (RLHF), and difficulty-based sampling. While several of these data-centric strategies reliably improve training efficiency and downstream performance, others fail to provide meaningful gains -- most notably self-generated synthetic data, which often increases dataset volume without enhancing model capability.
>   We formalize data curation as reweighting the sampling distribution and map its effect onto the eigenstructure of the data-induced operator. Our first main result shows that \textbf{static pruning induces a bounded operator and therefore cannot change the spectral tail exponent}; it provides at most finite-region improvements and cannot alter asymptotic neural scaling. Our second result analyzes \textbf{time-dependent data curation}, showing that an ideal oracle capable of tracking spectral residuals and continuously re-normalizing the tail can provably accelerate learning -- although practical systems can only approximate this behavior.

