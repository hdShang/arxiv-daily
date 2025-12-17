---
layout: default
title: Intelligent Communication Mixture-of-Experts Boosted-Medical Image Segmentation Foundation Model
---

# Intelligent Communication Mixture-of-Experts Boosted-Medical Image Segmentation Foundation Model

**arXiv**: [2510.17684v1](https://arxiv.org/abs/2510.17684) | [PDF](https://arxiv.org/pdf/2510.17684.pdf)

**作者**: Xinwei Zhang, Hu Chen, Zhe Yuan, Sukun Tian, Peng Feng

---

## 💡 一句话要点

**提出IC-MoE模型以增强医学图像分割基础模型的高层特征表示和预训练权重完整性**

**关键词**: `医学图像分割` `混合专家模型` `对比学习` `自适应微调` `高层特征表示`

## 📋 核心要点

1. 现有方法高层特征表示不足且微调破坏预训练权重结构完整性
2. 构建多专家模块并采用像素概率自适应投票策略进行专家选择与融合
3. 在三个公共数据集上实验显示IC-MoE优于其他SOTA模型，验证其泛化能力

## 📄 摘要（原文）

> Foundation models for medical image segmentation have achieved remarkable
> performance. Adaptive fine-tuning of natural image segmentation foundation
> models is crucial for medical image segmentation tasks. However, some
> limitations exist in existing fine-tuning methods: 1) insufficient
> representation of high-level features and 2) the fine-tuning process disrupts
> the structural integrity of pretrained weights. Inspired by these critical
> problems, we propose an intelligent communication mixture-of-experts
> boosted-medical image segmentation foundation model, named IC-MoE, with twofold
> ideas: 1) We construct basic experts, semantic experts, and adaptive experts.
> Moreover, we implement a pixel probability adaptive voting strategy, which
> enables expert selection and fusion through label consistency and load
> balancing. This approach preliminarily enhances the representation capability
> of high-level features while preserving the structural integrity of pretrained
> weights. 2) We propose a semantic-guided contrastive learning method to address
> the issue of weak supervision in contrastive learning. This method further
> enhances the representation capability of high-level features while preserving
> the structural integrity of pretrained weights. Extensive experiments across
> three public medical image segmentation datasets demonstrate that the IC-MoE
> outperforms other SOTA models. Consequently, the proposed IC-MoE effectively
> supplements foundational medical image segmentation models with high-level
> features and pretrained structural integrity. We also validate the superior
> generalizability of the IC-MoE across diverse medical image segmentation
> scenarios.

