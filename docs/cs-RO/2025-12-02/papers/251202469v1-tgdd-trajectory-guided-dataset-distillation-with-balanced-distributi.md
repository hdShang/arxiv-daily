---
layout: default
title: TGDD: Trajectory Guided Dataset Distillation with Balanced Distribution
---

# TGDD: Trajectory Guided Dataset Distillation with Balanced Distribution

**arXiv**: [2512.02469v1](https://arxiv.org/abs/2512.02469) | [PDF](https://arxiv.org/pdf/2512.02469.pdf)

**作者**: Fengli Ran, Xiao Pu, Bo Liu, Xiuli Bi, Bin Xiao

---

## 💡 一句话要点

**提出TGDD以动态对齐训练轨迹解决数据集蒸馏中特征演化忽略问题**

**关键词**: `数据集蒸馏` `分布匹配` `训练轨迹` `特征对齐` `合成数据优化`

## 📋 核心要点

1. 核心问题：基于分布匹配的数据集蒸馏方法忽略训练中特征演化，限制合成数据表达力。
2. 方法要点：TGDD将分布匹配重构为沿模型训练轨迹的动态对齐过程，并引入分布约束正则化减少类重叠。
3. 实验或效果：在十个数据集上实现SOTA性能，高分辨率基准上准确率提升5.0%，平衡性能与效率。

## 📄 摘要（原文）

> Dataset distillation compresses large datasets into compact synthetic ones to reduce storage and computational costs. Among various approaches, distribution matching (DM)-based methods have attracted attention for their high efficiency. However, they often overlook the evolution of feature representations during training, which limits the expressiveness of synthetic data and weakens downstream performance. To address this issue, we propose Trajectory Guided Dataset Distillation (TGDD), which reformulates distribution matching as a dynamic alignment process along the model's training trajectory. At each training stage, TGDD captures evolving semantics by aligning the feature distribution between the synthetic and original dataset. Meanwhile, it introduces a distribution constraint regularization to reduce class overlap. This design helps synthetic data preserve both semantic diversity and representativeness, improving performance in downstream tasks. Without additional optimization overhead, TGDD achieves a favorable balance between performance and efficiency. Experiments on ten datasets demonstrate that TGDD achieves state-of-the-art performance, notably a 5.0% accuracy gain on high-resolution benchmarks.

