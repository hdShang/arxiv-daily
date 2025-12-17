---
layout: default
title: A-TPT: Angular Diversity Calibration Properties for Test-Time Prompt Tuning of Vision-Language Models
---

# A-TPT: Angular Diversity Calibration Properties for Test-Time Prompt Tuning of Vision-Language Models

**arXiv**: [2510.26441v1](https://arxiv.org/abs/2510.26441) | [PDF](https://arxiv.org/pdf/2510.26441.pdf)

**作者**: Shihab Aaqil Ahamed, Udaya S. K. P. Miriya Thanthrige, Ranga Rodrigo, Muhammad Haris Khan

---

## 💡 一句话要点

**提出A-TPT框架，通过增强角多样性优化视觉语言模型的测试时提示调优校准性能**

**关键词**: `测试时提示调优` `视觉语言模型` `角多样性` `模型校准` `特征分散` `零样本学习`

## 📋 核心要点

1. 核心问题：测试时提示调优中文本特征缺乏分散性，影响模型校准可靠性和安全性
2. 方法要点：引入角多样性，最大化单位超球面上特征间最小成对角距离以实现均匀分布
3. 实验或效果：在多种数据集和骨干网络上，显著降低平均校准误差，保持准确率，泛化至自然分布偏移和医学数据

## 📄 摘要（原文）

> Test-time prompt tuning (TPT) has emerged as a promising technique for
> adapting large vision-language models (VLMs) to unseen tasks without relying on
> labeled data. However, the lack of dispersion between textual features can hurt
> calibration performance, which raises concerns about VLMs' reliability,
> trustworthiness, and safety. Current TPT approaches primarily focus on
> improving prompt calibration by either maximizing average textual feature
> dispersion or enforcing orthogonality constraints to encourage angular
> separation. However, these methods may not always have optimal angular
> separation between class-wise textual features, which implies overlooking the
> critical role of angular diversity. To address this, we propose A-TPT, a novel
> TPT framework that introduces angular diversity to encourage uniformity in the
> distribution of normalized textual features induced by corresponding learnable
> prompts. This uniformity is achieved by maximizing the minimum pairwise angular
> distance between features on the unit hypersphere. We show that our approach
> consistently surpasses state-of-the-art TPT methods in reducing the aggregate
> average calibration error while maintaining comparable accuracy through
> extensive experiments with various backbones on different datasets. Notably,
> our approach exhibits superior zero-shot calibration performance on natural
> distribution shifts and generalizes well to medical datasets. We provide
> extensive analyses, including theoretical aspects, to establish the grounding
> of A-TPT. These results highlight the potency of promoting angular diversity to
> achieve well-dispersed textual features, significantly improving VLM
> calibration during test-time adaptation. Our code will be made publicly
> available.

