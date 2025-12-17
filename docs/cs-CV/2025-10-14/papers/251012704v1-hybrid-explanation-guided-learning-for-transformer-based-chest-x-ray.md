---
layout: default
title: Hybrid Explanation-Guided Learning for Transformer-Based Chest X-Ray Diagnosis
---

# Hybrid Explanation-Guided Learning for Transformer-Based Chest X-Ray Diagnosis

**arXiv**: [2510.12704v1](https://arxiv.org/abs/2510.12704) | [PDF](https://arxiv.org/pdf/2510.12704.pdf)

**作者**: Shelley Zixin Shu, Haozhe Luo, Alexander Poellinger, Mauricio Reyes

---

## 💡 一句话要点

**提出混合解释引导学习框架，以提升基于Transformer的胸部X光诊断的泛化能力**

**关键词**: `Transformer模型` `胸部X光诊断` `解释引导学习` `注意力对齐` `自监督学习` `泛化能力`

## 📋 核心要点

1. Transformer模型在医学影像中易学伪相关，导致偏差和泛化受限
2. 结合自监督和人工引导约束，增强注意力对齐，无需高成本监督
3. 在胸部X光分类中优于现有方法，提高准确性和注意力图对齐度

## 📄 摘要（原文）

> Transformer-based deep learning models have demonstrated exceptional
> performance in medical imaging by leveraging attention mechanisms for feature
> representation and interpretability. However, these models are prone to
> learning spurious correlations, leading to biases and limited generalization.
> While human-AI attention alignment can mitigate these issues, it often depends
> on costly manual supervision. In this work, we propose a Hybrid
> Explanation-Guided Learning (H-EGL) framework that combines self-supervised and
> human-guided constraints to enhance attention alignment and improve
> generalization. The self-supervised component of H-EGL leverages
> class-distinctive attention without relying on restrictive priors, promoting
> robustness and flexibility. We validate our approach on chest X-ray
> classification using the Vision Transformer (ViT), where H-EGL outperforms two
> state-of-the-art Explanation-Guided Learning (EGL) methods, demonstrating
> superior classification accuracy and generalization capability. Additionally,
> it produces attention maps that are better aligned with human expertise.

