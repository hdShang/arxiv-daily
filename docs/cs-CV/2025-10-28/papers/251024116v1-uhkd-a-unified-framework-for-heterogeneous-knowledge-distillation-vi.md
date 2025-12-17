---
layout: default
title: UHKD: A Unified Framework for Heterogeneous Knowledge Distillation via Frequency-Domain Representations
---

# UHKD: A Unified Framework for Heterogeneous Knowledge Distillation via Frequency-Domain Representations

**arXiv**: [2510.24116v1](https://arxiv.org/abs/2510.24116) | [PDF](https://arxiv.org/pdf/2510.24116.pdf)

**作者**: Fengming Yu, Haiwei Pan, Kejia Zhang, Jian Guan, Haiying Jiang

---

## 💡 一句话要点

**提出UHKD框架，通过频域表示解决异构模型知识蒸馏中的语义差异问题**

**关键词**: `异构知识蒸馏` `频域表示` `特征对齐` `模型压缩` `视觉应用`

## 📋 核心要点

1. 异构模型知识蒸馏中，中间特征语义差异阻碍知识迁移，现有方法多针对同构模型
2. 利用傅里叶变换捕获全局特征，结合特征变换和对齐模块实现跨架构知识传递
3. 在CIFAR-100和ImageNet-1K上实验，准确率提升5.59%和0.83%，优于最新方法

## 📄 摘要（原文）

> Knowledge distillation (KD) is an effective model compression technique that
> transfers knowledge from a high-performance teacher to a lightweight student,
> reducing cost while maintaining accuracy. In visual applications, where
> large-scale image models are widely used, KD enables efficient deployment.
> However, architectural diversity introduces semantic discrepancies that hinder
> the use of intermediate representations. Most existing KD methods are designed
> for homogeneous models and degrade in heterogeneous scenarios, especially when
> intermediate features are involved. Prior studies mainly focus on the logits
> space, making limited use of the semantic information in intermediate layers.
> To address this limitation, Unified Heterogeneous Knowledge Distillation (UHKD)
> is proposed as a framework that leverages intermediate features in the
> frequency domain for cross-architecture transfer. Fourier transform is applied
> to capture global feature information, alleviating representational
> discrepancies between heterogeneous teacher-student pairs. A Feature
> Transformation Module (FTM) produces compact frequency-domain representations
> of teacher features, while a learnable Feature Alignment Module (FAM) projects
> student features and aligns them via multi-level matching. Training is guided
> by a joint objective combining mean squared error on intermediate features with
> Kullback-Leibler divergence on logits. Experiments on CIFAR-100 and ImageNet-1K
> demonstrate gains of 5.59% and 0.83% over the latest method, highlighting UHKD
> as an effective approach for unifying heterogeneous representations and
> enabling efficient utilization of visual knowledge

