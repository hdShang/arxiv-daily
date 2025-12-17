---
layout: default
title: CLEAR: Causal Learning Framework For Robust Histopathology Tumor Detection Under Out-Of-Distribution Shifts
---

# CLEAR: Causal Learning Framework For Robust Histopathology Tumor Detection Under Out-Of-Distribution Shifts

**arXiv**: [2510.14273v1](https://arxiv.org/abs/2510.14273) | [PDF](https://arxiv.org/pdf/2510.14273.pdf)

**作者**: Kieu-Anh Truong Thi, Huy-Hieu Pham, Duc-Trong Le

---

## 💡 一句话要点

**提出因果学习框架CLEAR以解决组织病理学肿瘤检测中的域偏移问题**

**关键词**: `组织病理学图像分析` `因果推断` `域偏移` `肿瘤检测` `前门原理` `深度学习`

## 📋 核心要点

1. 核心问题：组织病理学图像因采集过程或数据源差异导致域偏移，影响深度学习模型泛化能力
2. 方法要点：基于因果推断，利用前门原理设计转换策略，结合语义特征和中介变量减少混杂因素影响
3. 实验或效果：在CAMELYON17和私有数据集上验证，域外性能提升达7%，优于现有基线方法

## 📄 摘要（原文）

> Domain shift in histopathology, often caused by differences in acquisition
> processes or data sources, poses a major challenge to the generalization
> ability of deep learning models. Existing methods primarily rely on modeling
> statistical correlations by aligning feature distributions or introducing
> statistical variation, yet they often overlook causal relationships. In this
> work, we propose a novel causal-inference-based framework that leverages
> semantic features while mitigating the impact of confounders. Our method
> implements the front-door principle by designing transformation strategies that
> explicitly incorporate mediators and observed tissue slides. We validate our
> method on the CAMELYON17 dataset and a private histopathology dataset,
> demonstrating consistent performance gains across unseen domains. As a result,
> our approach achieved up to a 7% improvement in both the CAMELYON17 dataset and
> the private histopathology dataset, outperforming existing baselines. These
> results highlight the potential of causal inference as a powerful tool for
> addressing domain shift in histopathology image analysis.

