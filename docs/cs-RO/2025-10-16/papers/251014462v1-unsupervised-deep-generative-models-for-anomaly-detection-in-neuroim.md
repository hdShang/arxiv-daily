---
layout: default
title: Unsupervised Deep Generative Models for Anomaly Detection in Neuroimaging: A Systematic Scoping Review
---

# Unsupervised Deep Generative Models for Anomaly Detection in Neuroimaging: A Systematic Scoping Review

**arXiv**: [2510.14462v1](https://arxiv.org/abs/2510.14462) | [PDF](https://arxiv.org/pdf/2510.14462.pdf)

**作者**: Youwan Mahé, Elise Bannier, Stéphanie Leplaideur, Elisa Fromont, Francesca Galassi

---

## 💡 一句话要点

**综述无监督深度生成模型在神经影像异常检测中的应用与进展**

**关键词**: `无监督学习` `深度生成模型` `神经影像异常检测` `伪健康重建` `脑部MRI` `综述研究`

## 📋 核心要点

1. 核心问题：监督方法依赖大量标注数据，难以处理罕见或异质性疾病。
2. 方法要点：使用健康数据训练生成模型，检测异常作为与规范结构的偏差。
3. 实验或效果：模型在大型局灶性病变中表现良好，并生成可解释的伪健康重建。

## 📄 摘要（原文）

> Unsupervised deep generative models are emerging as a promising alternative
> to supervised methods for detecting and segmenting anomalies in brain imaging.
> Unlike fully supervised approaches, which require large voxel-level annotated
> datasets and are limited to well-characterised pathologies, these models can be
> trained exclusively on healthy data and identify anomalies as deviations from
> learned normative brain structures. This PRISMA-guided scoping review
> synthesises recent work on unsupervised deep generative models for anomaly
> detection in neuroimaging, including autoencoders, variational autoencoders,
> generative adversarial networks, and denoising diffusion models. A total of 49
> studies published between 2018 - 2025 were identified, covering applications to
> brain MRI and, less frequently, CT across diverse pathologies such as tumours,
> stroke, multiple sclerosis, and small vessel disease. Reported performance
> metrics are compared alongside architectural design choices. Across the
> included studies, generative models achieved encouraging performance for large
> focal lesions and demonstrated progress in addressing more subtle
> abnormalities. A key strength of generative models is their ability to produce
> interpretable pseudo-healthy (also referred to as counterfactual)
> reconstructions, which is particularly valuable when annotated data are scarce,
> as in rare or heterogeneous diseases. Looking ahead, these models offer a
> compelling direction for anomaly detection, enabling semi-supervised learning,
> supporting the discovery of novel imaging biomarkers, and facilitating within-
> and cross-disease deviation mapping in unified end-to-end frameworks. To
> realise clinical impact, future work should prioritise anatomy-aware modelling,
> development of foundation models, task-appropriate evaluation metrics, and
> rigorous clinical validation.

