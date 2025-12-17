---
layout: default
title: Rewiring Development in Brain Segmentation: Leveraging Adult Brain Priors for Enhancing Infant MRI Segmentation
---

# Rewiring Development in Brain Segmentation: Leveraging Adult Brain Priors for Enhancing Infant MRI Segmentation

**arXiv**: [2510.09306v1](https://arxiv.org/abs/2510.09306) | [PDF](https://arxiv.org/pdf/2510.09306.pdf)

**作者**: Alemu Sisay Nigru, Michele Svanera, Austin Dibble, Connor Dalby, Mattia Savardi, Sergio Benini

---

## 💡 一句话要点

**提出LODi框架，利用成人脑MRI先验增强婴儿脑MRI分割性能**

**关键词**: `脑MRI分割` `迁移学习` `领域适应` `婴儿神经影像` `弱监督学习`

## 📋 核心要点

1. 婴儿脑MRI分割面临解剖变化、运动伪影和标注数据稀缺等挑战
2. 通过迁移学习和领域适应，将成人模型逐步适配到0-2岁婴儿数据
3. 实验显示方法优于传统监督学习和领域特定模型，提升分割准确性

## 📄 摘要（原文）

> Accurate segmentation of infant brain MRI is critical for studying early
> neurodevelopment and diagnosing neurological disorders. Yet, it remains a
> fundamental challenge due to continuously evolving anatomy of the subjects,
> motion artifacts, and the scarcity of high-quality labeled data. In this work,
> we present LODi, a novel framework that utilizes prior knowledge from an adult
> brain MRI segmentation model to enhance the segmentation performance of infant
> scans. Given the abundance of publicly available adult brain MRI data, we
> pre-train a segmentation model on a large adult dataset as a starting point.
> Through transfer learning and domain adaptation strategies, we progressively
> adapt the model to the 0-2 year-old population, enabling it to account for the
> anatomical and imaging variability typical of infant scans. The adaptation of
> the adult model is carried out using weakly supervised learning on infant brain
> scans, leveraging silver-standard ground truth labels obtained with FreeSurfer.
> By introducing a novel training strategy that integrates hierarchical feature
> refinement and multi-level consistency constraints, our method enables fast,
> accurate, age-adaptive segmentation, while mitigating scanner and site-specific
> biases. Extensive experiments on both internal and external datasets
> demonstrate the superiority of our approach over traditional supervised
> learning and domain-specific models. Our findings highlight the advantage of
> leveraging adult brain priors as a foundation for age-flexible neuroimaging
> analysis, paving the way for more reliable and generalizable brain MRI
> segmentation across the lifespan.

