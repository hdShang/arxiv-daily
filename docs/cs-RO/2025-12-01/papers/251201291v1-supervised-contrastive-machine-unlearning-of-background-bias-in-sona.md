---
layout: default
title: Supervised Contrastive Machine Unlearning of Background Bias in Sonar Image Classification with Fine-Grained Explainable AI
---

# Supervised Contrastive Machine Unlearning of Background Bias in Sonar Image Classification with Fine-Grained Explainable AI

**arXiv**: [2512.01291v1](https://arxiv.org/abs/2512.01291) | [PDF](https://arxiv.org/pdf/2512.01291.pdf)

**作者**: Kamal Basha S, Athira Nambiar

---

## 💡 一句话要点

**提出结合对比性遗忘与可解释AI的框架，以解决声纳图像分类中海底背景偏差问题。**

**关键词**: `声纳图像分类` `对比性遗忘` `可解释AI` `背景偏差` `模型泛化`

## 📋 核心要点

1. 核心问题：声纳图像分类模型过度依赖海底特征，导致泛化能力差。
2. 方法要点：引入目标对比性遗忘模块减少背景偏差，并开发可解释框架评估遗忘效果。
3. 实验或效果：在真实与合成数据集上验证，显著提升遗忘有效性、鲁棒性和可解释性。

## 📄 摘要（原文）

> Acoustic sonar image analysis plays a critical role in object detection and classification, with applications in both civilian and defense domains. Despite the availability of real and synthetic datasets, existing AI models that achieve high accuracy often over-rely on seafloor features, leading to poor generalization. To mitigate this issue, we propose a novel framework that integrates two key modules: (i) a Targeted Contrastive Unlearning (TCU) module, which extends the traditional triplet loss to reduce seafloor-induced background bias and improve generalization, and (ii) the Unlearn to Explain Sonar Framework (UESF), which provides visual insights into what the model has deliberately forgotten while adapting the LIME explainer to generate more faithful and localized attributions for unlearning evaluation. Extensive experiments across both real and synthetic sonar datasets validate our approach, demonstrating significant improvements in unlearning effectiveness, model robustness, and interpretability.

