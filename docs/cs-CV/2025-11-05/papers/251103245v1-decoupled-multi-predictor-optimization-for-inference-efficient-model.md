---
layout: default
title: Decoupled Multi-Predictor Optimization for Inference-Efficient Model Tuning
---

# Decoupled Multi-Predictor Optimization for Inference-Efficient Model Tuning

**arXiv**: [2511.03245v1](https://arxiv.org/abs/2511.03245) | [PDF](https://arxiv.org/pdf/2511.03245.pdf)

**作者**: Liwei Luo, Shuaitengyuan Li, Dongwei Ren, Qilong Wang, Pengfei Zhu, Qinghua Hu

---

## 💡 一句话要点

**提出解耦多预测器优化方法以提升预训练模型调优的推理效率**

**关键词**: `模型调优` `推理效率` `早期退出` `多预测器` `解耦优化` `特征表示`

## 📋 核心要点

1. 核心问题：早期阶段如何同时提供低层基础特征给深层阶段和高层判别特征给早期预测器
2. 方法要点：引入轻量旁路模块和高阶统计预测器，并采用解耦优化分配两阶段损失权重
3. 实验效果：在多种数据集和预训练骨干上，DMPO在降低计算成本时明显优于对比方法

## 📄 摘要（原文）

> Recently, remarkable progress has been made in large-scale pre-trained model
> tuning, and inference efficiency is becoming more crucial for practical
> deployment. Early exiting in conjunction with multi-stage predictors, when
> cooperated with a parameter-efficient fine-tuning strategy, offers a
> straightforward way to achieve an inference-efficient model. However, a key
> challenge remains unresolved: How can early stages provide low-level
> fundamental features to deep stages while simultaneously supplying high-level
> discriminative features to early-stage predictors? To address this problem, we
> propose a Decoupled Multi-Predictor Optimization (DMPO) method to effectively
> decouple the low-level representative ability and high-level discriminative
> ability in early stages. First, in terms of architecture, we introduce a
> lightweight bypass module into multi-stage predictors for functional
> decomposition of shallow features from early stages, while a high-order
> statistics-based predictor is developed for early stages to effectively enhance
> their discriminative ability. To reasonably train our multi-predictor
> architecture, a decoupled optimization is proposed to allocate two-phase loss
> weights for multi-stage predictors during model tuning, where the initial
> training phase enables the model to prioritize the acquisition of
> discriminative ability of deep stages via emphasizing representative ability of
> early stages, and the latter training phase drives discriminative ability
> towards earlier stages as much as possible. As such, our DMPO can effectively
> decouple representative and discriminative abilities in early stages in terms
> of architecture design and model optimization. Experiments across various
> datasets and pre-trained backbones demonstrate that DMPO clearly outperforms
> its counterparts when reducing computational cost.

