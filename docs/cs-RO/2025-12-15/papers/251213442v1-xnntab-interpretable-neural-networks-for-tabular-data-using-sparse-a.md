---
layout: default
title: XNNTab -- Interpretable Neural Networks for Tabular Data using Sparse Autoencoders
---

# XNNTab -- Interpretable Neural Networks for Tabular Data using Sparse Autoencoders

**arXiv**: [2512.13442v1](https://arxiv.org/abs/2512.13442) | [PDF](https://arxiv.org/pdf/2512.13442.pdf)

**作者**: Khawla Elhadri, Jörg Schlötterer, Christin Seifert

---

## 💡 一句话要点

**提出XNNTab，结合稀疏自编码器实现表格数据神经网络的解释性，以解决黑盒问题。**

**关键词**: `表格数据` `神经网络解释性` `稀疏自编码器` `可解释机器学习` `特征分解`

## 📋 核心要点

1. 核心问题：表格数据应用中，神经网络因黑盒特性难以用于需解释性的场景。
2. 方法要点：使用稀疏自编码器分解非线性特征为单语义特征，并赋予可解释概念。
3. 实验或效果：XNNTab优于可解释模型，性能与非解释性神经网络相当。

## 📄 摘要（原文）

> In data-driven applications relying on tabular data, where interpretability is key, machine learning models such as decision trees and linear regression are applied. Although neural networks can provide higher predictive performance, they are not used because of their blackbox nature. In this work, we present XNNTab, a neural architecture that combines the expressiveness of neural networks and interpretability. XNNTab first learns highly non-linear feature representations, which are decomposed into monosemantic features using a sparse autoencoder (SAE). These features are then assigned human-interpretable concepts, making the overall model prediction intrinsically interpretable. XNNTab outperforms interpretable predictive models, and achieves comparable performance to its non-interpretable counterparts.

