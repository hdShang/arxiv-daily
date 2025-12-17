---
layout: default
title: Functional Mean Flow in Hilbert Space
---

# Functional Mean Flow in Hilbert Space

**arXiv**: [2511.12898v1](https://arxiv.org/abs/2511.12898) | [PDF](https://arxiv.org/pdf/2511.12898.pdf)

**作者**: Zhiqi Li, Yuchen Sun, Greg Turk, Bo Zhu

---

## 💡 一句话要点

**提出Functional Mean Flow，在无限维希尔伯特空间中实现一步生成模型，适用于函数数据生成。**

**关键词**: `函数数据生成` `一步生成模型` `希尔伯特空间` `Flow Matching` `时间序列生成` `图像生成`

## 📋 核心要点

1. 核心问题：将一步生成模型扩展到无限维函数域，处理如时间序列、图像等数据。
2. 方法要点：提供Functional Flow Matching理论框架和实用实现，引入x1预测变体提升稳定性。
3. 实验或效果：框架高效训练和采样，适用于多种函数数据生成任务，如PDE和3D几何。

## 📄 摘要（原文）

> We present Functional Mean Flow (FMF) as a one-step generative model defined in infinite-dimensional Hilbert space. FMF extends the one-step Mean Flow framework to functional domains by providing a theoretical formulation for Functional Flow Matching and a practical implementation for efficient training and sampling. We also introduce an $x_1$-prediction variant that improves stability over the original $u$-prediction form. The resulting framework is a practical one-step Flow Matching method applicable to a wide range of functional data generation tasks such as time series, images, PDEs, and 3D geometry.

