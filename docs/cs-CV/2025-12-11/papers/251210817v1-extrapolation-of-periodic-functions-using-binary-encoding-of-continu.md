---
layout: default
title: Extrapolation of Periodic Functions Using Binary Encoding of Continuous Numerical Values
---

# Extrapolation of Periodic Functions Using Binary Encoding of Continuous Numerical Values

**arXiv**: [2512.10817v1](https://arxiv.org/abs/2512.10817) | [PDF](https://arxiv.org/pdf/2512.10817.pdf)

**作者**: Brian P. Powell, Jordan A. Caraballo-Vega, Mark L. Carroll, Thomas Maxwell, Andrew Ptak, Greg Olmschenk, Jorge Martinez-Palomera

---

## 💡 一句话要点

**提出归一化二进制编码使多层感知机无需先验知识即可外推周期性函数。**

**关键词**: `周期性函数外推` `二进制编码` `多层感知机` `归一化编码` `比特相位表示`

## 📋 核心要点

1. 核心问题：神经网络难以外推训练范围外的周期性函数。
2. 方法要点：引入归一化二进制编码将连续数值转换为二进制表示。
3. 实验或效果：多层感知机成功外推多种周期信号，内部激活分析揭示比特相位表示。

## 📄 摘要（原文）

> We report the discovery that binary encoding allows neural networks to extrapolate periodic functions beyond their training bounds. We introduce Normalized Base-2 Encoding (NB2E) as a method for encoding continuous numerical values and demonstrate that, using this input encoding, vanilla multi-layer perceptrons (MLP) successfully extrapolate diverse periodic signals without prior knowledge of their functional form. Internal activation analysis reveals that NB2E induces bit-phase representations, enabling MLPs to learn and extrapolate signal structure independently of position.

