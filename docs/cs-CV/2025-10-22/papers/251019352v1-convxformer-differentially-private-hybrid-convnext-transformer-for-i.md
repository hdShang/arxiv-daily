---
layout: default
title: ConvXformer: Differentially Private Hybrid ConvNeXt-Transformer for Inertial Navigation
---

# ConvXformer: Differentially Private Hybrid ConvNeXt-Transformer for Inertial Navigation

**arXiv**: [2510.19352v1](https://arxiv.org/abs/2510.19352) | [PDF](https://arxiv.org/pdf/2510.19352.pdf)

**作者**: Omer Tariq, Muhammad Bilal, Muneeb Ul Hassan, Dongsoo Han, Jon Crowcroft

---

## 💡 一句话要点

**提出ConvXformer混合架构，结合差分隐私机制，提升GPS缺失环境下的惯性导航精度与隐私保护。**

**关键词**: `惯性导航` `差分隐私` `混合架构` `Transformer` `ConvNeXt` `传感器扰动`

## 📋 核心要点

1. 深度学习惯性导航易泄露敏感数据，现有差分隐私方法因噪声过多损害模型性能。
2. 融合ConvNeXt块与Transformer编码器，采用自适应梯度裁剪和GANI机制保护隐私。
3. 在多个数据集上验证，定位精度提升超40%，并在强磁场环境中展示鲁棒性。

## 📄 摘要（原文）

> Data-driven inertial sequence learning has revolutionized navigation in
> GPS-denied environments, offering superior odometric resolution compared to
> traditional Bayesian methods. However, deep learning-based inertial tracking
> systems remain vulnerable to privacy breaches that can expose sensitive
> training data. \hl{Existing differential privacy solutions often compromise
> model performance by introducing excessive noise, particularly in
> high-frequency inertial measurements.} In this article, we propose ConvXformer,
> a hybrid architecture that fuses ConvNeXt blocks with Transformer encoders in a
> hierarchical structure for robust inertial navigation. We propose an efficient
> differential privacy mechanism incorporating adaptive gradient clipping and
> gradient-aligned noise injection (GANI) to protect sensitive information while
> ensuring model performance. Our framework leverages truncated singular value
> decomposition for gradient processing, enabling precise control over the
> privacy-utility trade-off. Comprehensive performance evaluations on benchmark
> datasets (OxIOD, RIDI, RoNIN) demonstrate that ConvXformer surpasses
> state-of-the-art methods, achieving more than 40% improvement in positioning
> accuracy while ensuring $(\epsilon,\delta)$-differential privacy guarantees. To
> validate real-world performance, we introduce the Mech-IO dataset, collected
> from the mechanical engineering building at KAIST, where intense magnetic
> fields from industrial equipment induce significant sensor perturbations. This
> demonstrated robustness under severe environmental distortions makes our
> framework well-suited for secure and intelligent navigation in cyber-physical
> systems.

