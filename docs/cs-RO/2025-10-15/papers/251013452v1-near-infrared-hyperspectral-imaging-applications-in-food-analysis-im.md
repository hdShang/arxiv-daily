---
layout: default
title: Near-Infrared Hyperspectral Imaging Applications in Food Analysis -- Improving Algorithms and Methodologies
---

# Near-Infrared Hyperspectral Imaging Applications in Food Analysis -- Improving Algorithms and Methodologies

**arXiv**: [2510.13452v1](https://arxiv.org/abs/2510.13452) | [PDF](https://arxiv.org/pdf/2510.13452.pdf)

**作者**: Ole-Christian Galbo Engstrøm

---

## 💡 一句话要点

**改进近红外高光谱成像算法，提升食品质量分析性能**

**关键词**: `近红外高光谱成像` `卷积神经网络` `偏最小二乘` `食品质量分析` `光谱卷积` `化学图生成`

## 📋 核心要点

1. 核心问题：食品质量分析中化学和物理参数建模的精度与空间分布预测限制
2. 方法要点：结合CNN与PLS，引入光谱卷积层增强2D CNN性能
3. 实验或效果：CNN在联合空间-光谱分析中优于PLS，生成平滑化学图

## 📄 摘要（原文）

> This thesis investigates the application of near-infrared hyperspectral
> imaging (NIR-HSI) for food quality analysis. The investigation is conducted
> through four studies operating with five research hypotheses. For several
> analyses, the studies compare models based on convolutional neural networks
> (CNNs) and partial least squares (PLS). Generally, joint spatio-spectral
> analysis with CNNs outperforms spatial analysis with CNNs and spectral analysis
> with PLS when modeling parameters where chemical and physical visual
> information are relevant. When modeling chemical parameters with a
> 2-dimensional (2D) CNN, augmenting the CNN with an initial layer dedicated to
> performing spectral convolution enhances its predictive performance by learning
> a spectral preprocessing similar to that applied by domain experts. Still,
> PLS-based spectral modeling performs equally well for analysis of the mean
> content of chemical parameters in samples and is the recommended approach.
> Modeling the spatial distribution of chemical parameters with NIR-HSI is
> limited by the ability to obtain spatially resolved reference values.
> Therefore, a study used bulk mean references for chemical map generation of fat
> content in pork bellies. A PLS-based approach gave non-smooth chemical maps and
> pixel-wise predictions outside the range of 0-100\%. Conversely, a 2D CNN
> augmented with a spectral convolution layer mitigated all issues arising with
> PLS. The final study attempted to model barley's germinative capacity by
> analyzing NIR spectra, RGB images, and NIR-HSI images. However, the results
> were inconclusive due to the dataset's low degree of germination. Additionally,
> this thesis has led to the development of two open-sourced Python packages. The
> first facilitates fast PLS-based modeling, while the second facilitates very
> fast cross-validation of PLS and other classical machine learning models with a
> new algorithm.

