---
layout: default
title: Utility Boundary of Dataset Distillation: Scaling and Configuration-Coverage Laws
---

# Utility Boundary of Dataset Distillation: Scaling and Configuration-Coverage Laws

**arXiv**: [2512.05817v1](https://arxiv.org/abs/2512.05817) | [PDF](https://arxiv.org/pdf/2512.05817.pdf)

**作者**: Zhengquan Luo, Zhiqiang Xu

---

## 💡 一句话要点

**提出配置-动态-误差分析框架，揭示数据集蒸馏的缩放与配置覆盖定律。**

**关键词**: `数据集蒸馏` `理论框架` `缩放定律` `配置覆盖` `泛化误差` `样本效率`

## 📋 核心要点

1. 核心问题：数据集蒸馏缺乏统一理论，性能随配置变化不明确。
2. 方法要点：统一分析框架将主流方法重构为泛化误差视角，推导缩放与覆盖定律。
3. 实验或效果：多方法与配置实验验证定律，支持理论驱动的紧凑、鲁棒蒸馏设计。

## 📄 摘要（原文）

> Dataset distillation (DD) aims to construct compact synthetic datasets that allow models to achieve comparable performance to full-data training while substantially reducing storage and computation. Despite rapid empirical progress, its theoretical foundations remain limited: existing methods (gradient, distribution, trajectory matching) are built on heterogeneous surrogate objectives and optimization assumptions, which makes it difficult to analyze their common principles or provide general guarantees. Moreover, it is still unclear under what conditions distilled data can retain the effectiveness of full datasets when the training configuration, such as optimizer, architecture, or augmentation, changes. To answer these questions, we propose a unified theoretical framework, termed configuration--dynamics--error analysis, which reformulates major DD approaches under a common generalization-error perspective and provides two main results: (i) a scaling law that provides a single-configuration upper bound, characterizing how the error decreases as the distilled sample size increases and explaining the commonly observed performance saturation effect; and (ii) a coverage law showing that the required distilled sample size scales linearly with configuration diversity, with provably matching upper and lower bounds. In addition, our unified analysis reveals that various matching methods are interchangeable surrogates, reducing the same generalization error, clarifying why they can all achieve dataset distillation and providing guidance on how surrogate choices affect sample efficiency and robustness. Experiments across diverse methods and configurations empirically confirm the derived laws, advancing a theoretical foundation for DD and enabling theory-driven design of compact, configuration-robust dataset distillation.

