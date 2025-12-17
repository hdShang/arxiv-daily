---
layout: default
title: Do Students Debias Like Teachers? On the Distillability of Bias Mitigation Methods
---

# Do Students Debias Like Teachers? On the Distillability of Bias Mitigation Methods

**arXiv**: [2510.26038v1](https://arxiv.org/abs/2510.26038) | [PDF](https://arxiv.org/pdf/2510.26038.pdf)

**作者**: Jiali Cheng, Chirag Agarwal, Hadi Amiri

---

## 💡 一句话要点

**研究知识蒸馏对去偏能力可蒸馏性的影响并提出改进方法**

**关键词**: `知识蒸馏` `去偏方法` `模型鲁棒性` `自然语言推理` `图像分类` `注意力机制`

## 📋 核心要点

1. 核心问题：知识蒸馏是否影响模型去偏能力在分布外数据上的鲁棒性
2. 方法要点：通过实验分析去偏能力在蒸馏后的变化及内部机制
3. 实验或效果：发现去偏能力受损，提出数据增强等三种改进方案

## 📄 摘要（原文）

> Knowledge distillation (KD) is an effective method for model compression and
> transferring knowledge between models. However, its effect on model's
> robustness against spurious correlations that degrade performance on
> out-of-distribution data remains underexplored. This study investigates the
> effect of knowledge distillation on the transferability of ``debiasing''
> capabilities from teacher models to student models on natural language
> inference (NLI) and image classification tasks. Through extensive experiments,
> we illustrate several key findings: (i) overall the debiasing capability of a
> model is undermined post-KD; (ii) training a debiased model does not benefit
> from injecting teacher knowledge; (iii) although the overall robustness of a
> model may remain stable post-distillation, significant variations can occur
> across different types of biases; and (iv) we pin-point the internal attention
> pattern and circuit that causes the distinct behavior post-KD. Given the above
> findings, we propose three effective solutions to improve the distillability of
> debiasing methods: developing high quality data for augmentation, implementing
> iterative knowledge distillation, and initializing student models with weights
> obtained from teacher models. To the best of our knowledge, this is the first
> study on the effect of KD on debiasing and its interenal mechanism at scale.
> Our findings provide understandings on how KD works and how to design better
> debiasing methods.

