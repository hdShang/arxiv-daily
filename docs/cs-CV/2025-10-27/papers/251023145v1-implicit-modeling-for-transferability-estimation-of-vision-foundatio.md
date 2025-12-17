---
layout: default
title: Implicit Modeling for Transferability Estimation of Vision Foundation Models
---

# Implicit Modeling for Transferability Estimation of Vision Foundation Models

**arXiv**: [2510.23145v1](https://arxiv.org/abs/2510.23145) | [PDF](https://arxiv.org/pdf/2510.23145.pdf)

**作者**: Yaoyan Zheng, Huiqun Wang, Nan Zhou, Di Huang

---

## 💡 一句话要点

**提出隐式建模框架以提升视觉基础模型迁移性估计的泛化能力**

**关键词**: `迁移性估计` `隐式建模` `变分近似` `视觉基础模型` `下游任务`

## 📋 核心要点

1. 现有方法难以准确评估新兴预训练模型的迁移性
2. 引入隐式建模和分治变分近似策略高效近似嵌入空间演化
3. 实验表明在稳定性和效率上优于现有方法

## 📄 摘要（原文）

> Transferability estimation identifies the best pre-trained models for
> downstream tasks without incurring the high computational cost of full
> fine-tuning. This capability facilitates deployment and advances the
> pre-training and fine-tuning paradigm. However, existing methods often struggle
> to accurately assess transferability for emerging pre-trained models with
> diverse architectures, training strategies, and task alignments. In this work,
> we propose Implicit Transferability Modeling (ITM), a novel framework that
> implicitly models each model's intrinsic transferability, coupled with a
> Divide-and-Conquer Variational Approximation (DVA) strategy to efficiently
> approximate embedding space evolution. This design enables generalization
> across a broader range of models and downstream tasks. Extensive experiments on
> a comprehensive benchmark--spanning extensive training regimes and a wider
> variety of model types--demonstrate that ITM consistently outperforms existing
> methods in terms of stability, effectiveness, and efficiency.

