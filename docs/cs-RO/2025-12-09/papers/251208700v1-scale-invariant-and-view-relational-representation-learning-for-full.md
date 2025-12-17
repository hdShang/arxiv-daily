---
layout: default
title: Scale-invariant and View-relational Representation Learning for Full Surround Monocular Depth
---

# Scale-invariant and View-relational Representation Learning for Full Surround Monocular Depth

**arXiv**: [2512.08700v1](https://arxiv.org/abs/2512.08700) | [PDF](https://arxiv.org/pdf/2512.08700.pdf)

**作者**: Kyumin Hwang, Wonhyeok Choi, Kiljoon Han, Wonjoon Choi, Minwoo Choi, Yongcheon Na, Minwoo Park, Sunghoon Im

---

## 💡 一句话要点

**提出跨交互与视图关系知识蒸馏策略，以解决全环绕单目深度估计中的计算成本高和尺度估计难问题。**

**关键词**: `全环绕单目深度估计` `知识蒸馏` `尺度不变表示` `视图关系学习` `实时性能优化`

## 📋 核心要点

1. 核心问题：现有基础模型在全环绕单目深度估计中计算成本高且难以预测度量尺度深度。
2. 方法要点：采用混合回归框架，结合知识蒸馏和深度分箱模块，通过跨交互和视图关系蒸馏提升尺度一致性和跨视图深度一致性。
3. 实验或效果：在DDAD和nuScenes数据集上验证有效性，实现性能与效率的平衡，满足实时需求。

## 📄 摘要（原文）

> Recent foundation models demonstrate strong generalization capabilities in monocular depth estimation. However, directly applying these models to Full Surround Monocular Depth Estimation (FSMDE) presents two major challenges: (1) high computational cost, which limits real-time performance, and (2) difficulty in estimating metric-scale depth, as these models are typically trained to predict only relative depth. To address these limitations, we propose a novel knowledge distillation strategy that transfers robust depth knowledge from a foundation model to a lightweight FSMDE network. Our approach leverages a hybrid regression framework combining the knowledge distillation scheme--traditionally used in classification--with a depth binning module to enhance scale consistency. Specifically, we introduce a cross-interaction knowledge distillation scheme that distills the scale-invariant depth bin probabilities of a foundation model into the student network while guiding it to infer metric-scale depth bin centers from ground-truth depth. Furthermore, we propose view-relational knowledge distillation, which encodes structural relationships among adjacent camera views and transfers them to enhance cross-view depth consistency. Experiments on DDAD and nuScenes demonstrate the effectiveness of our method compared to conventional supervised methods and existing knowledge distillation approaches. Moreover, our method achieves a favorable trade-off between performance and efficiency, meeting real-time requirements.

