---
layout: default
title: Learning to Reconstruct Temperature Field from Sparse Observations with Implicit Physics Priors
---

# Learning to Reconstruct Temperature Field from Sparse Observations with Implicit Physics Priors

**arXiv**: [2512.01196v1](https://arxiv.org/abs/2512.01196) | [PDF](https://arxiv.org/pdf/2512.01196.pdf)

**作者**: Shihang Li, Zhiqiang Gong, Weien Zhou, Yue Gao, Wen Yao

---

## 💡 一句话要点

**提出IPTR框架，利用隐式物理先验从稀疏观测重建温度场，提升泛化能力。**

**关键词**: `温度场重建` `隐式物理先验` `稀疏观测` `双物理嵌入` `泛化能力`

## 📋 核心要点

1. 核心问题：温度场重建面临测量成本高和分布偏移挑战，现有方法未有效利用参考模拟数据。
2. 方法要点：设计双物理嵌入模块，结合参考数据的隐式物理引导和目标观测的空间特征编码。
3. 实验或效果：在单条件、多条件和少样本设置下，IPTR优于现有方法，实现高精度重建和强泛化。

## 📄 摘要（原文）

> Accurate reconstruction of temperature field of heat-source systems (TFR-HSS) is crucial for thermal monitoring and reliability assessment in engineering applications such as electronic devices and aerospace structures. However, the high cost of measurement acquisition and the substantial distributional shifts in temperature field across varying conditions present significant challenges for developing reconstruction models with robust generalization capabilities. Existing DNNs-based methods typically formulate TFR-HSS as a one-to-one regression problem based solely on target sparse measurements, without effectively leveraging reference simulation data that implicitly encode thermal knowledge. To address this limitation, we propose IPTR, an implicit physics-guided temperature field reconstruction framework that introduces sparse monitoring-temperature field pair from reference simulations as priors to enrich physical understanding. To integrate both reference and target information, we design a dual physics embedding module consisting of two complementary branches: an implicit physics-guided branch employing cross-attention to distill latent physics from the reference data, and an auxiliary encoding branch based on Fourier layers to capture the spatial characteristics of the target observation. The fused representation is then decoded to reconstruct the full temperature field. Extensive experiments under single-condition, multi-condition, and few-shot settings demonstrate that IPTR consistently outperforms existing methods, achieving state-of-the-art reconstruction accuracy and strong generalization capability.

