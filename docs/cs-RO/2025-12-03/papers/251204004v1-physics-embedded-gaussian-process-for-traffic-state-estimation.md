---
layout: default
title: Physics-Embedded Gaussian Process for Traffic State Estimation
---

# Physics-Embedded Gaussian Process for Traffic State Estimation

**arXiv**: [2512.04004v1](https://arxiv.org/abs/2512.04004) | [PDF](https://arxiv.org/pdf/2512.04004.pdf)

**作者**: Yanlin Chen, Kehua Chen, Yinhai Wang

---

## 💡 一句话要点

**提出物理嵌入高斯过程以解决稀疏观测下的交通状态估计问题**

**关键词**: `交通状态估计` `高斯过程` `物理嵌入学习` `多输出核` `不确定性量化`

## 📋 核心要点

1. 核心问题：低渗透率稀疏观测时，纯数据方法泛化差，物理模型难处理不确定性
2. 方法要点：基于经典交通流模型设计多输出核，通过线性化微分算子嵌入物理结构
3. 实验效果：在HighD、NGSIM数据集上优于非物理基线，PEGP-ARZ在稀疏观测下更可靠

## 📄 摘要（原文）

> Traffic state estimation (TSE) becomes challenging when probe-vehicle penetration is low and observations are spatially sparse. Pure data-driven methods lack physical explanations and have poor generalization when observed data is sparse. In contrast, physical models have difficulty integrating uncertainties and capturing the real complexity of traffic. To bridge this gap, recent studies have explored combining them by embedding physical structure into Gaussian process. These approaches typically introduce the governing equations as soft constraints through pseudo-observations, enabling the integration of model structure within a variational framework. However, these methods rely heavily on penalty tuning and lack principled uncertainty calibration, which makes them sensitive to model mis-specification. In this work, we address these limitations by presenting a novel Physics-Embedded Gaussian Process (PEGP), designed to integrate domain knowledge with data-driven methods in traffic state estimation. Specifically, we design two multi-output kernels informed by classic traffic flow models, constructed via the explicit application of the linearized differential operator. Experiments on HighD, NGSIM show consistent improvements over non-physics baselines. PEGP-ARZ proves more reliable under sparse observation, while PEGP-LWR achieves lower errors with denser observation. Ablation study further reveals that PEGP-ARZ residuals align closely with physics and yield calibrated, interpretable uncertainty, whereas PEGP-LWR residuals are more orthogonal and produce nearly constant variance fields. This PEGP framework combines physical priors, uncertainty quantification, which can provide reliable support for TSE.

