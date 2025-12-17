---
layout: default
title: Machine-learning-enabled interpretation of tribological deformation patterns in large-scale MD data
---

# Machine-learning-enabled interpretation of tribological deformation patterns in large-scale MD data

**arXiv**: [2512.05818v1](https://arxiv.org/abs/2512.05818) | [PDF](https://arxiv.org/pdf/2512.05818.pdf)

**作者**: Hendrik J. Ehrich, Marvin C. May, Stefan J. Eder

---

## 💡 一句话要点

**提出基于机器学习的自动化工作流，用于从大规模分子动力学数据中解释摩擦学变形模式。**

**关键词**: `分子动力学模拟` `摩擦学变形模式` `机器学习工作流` `自编码器压缩` `CNN-MLP模型` `变形模式分类`

## 📋 核心要点

1. 核心问题：高维分子动力学数据转化为可解释变形模式图需大量手动处理，资源密集。
2. 方法要点：使用自编码器压缩图像至32维特征向量，结合元数据训练CNN-MLP模型预测变形模式。
3. 实验或效果：模型在验证数据上预测准确率约96%，通过排除特定区域训练评估泛化能力。

## 📄 摘要（原文）

> Molecular dynamics (MD) simulations have become indispensable for exploring tribological deformation patterns at the atomic scale. However, transforming the resulting high-dimensional data into interpretable deformation pattern maps remains a resource-intensive and largely manual process. In this work, we introduce a data-driven workflow that automates this interpretation step using unsupervised and supervised learning. Grain-orientation-colored computational tomograph pictures obtained from CuNi alloy simulations were first compressed through an autoencoder to a 32-dimensional global feature vector. Despite this strong compression, the reconstructed images retained the essential microstructural motifs: grain boundaries, stacking faults, twins, and partial lattice rotations, while omitting only the finest defects. The learned representations were then combined with simulation metadata (composition, load, time, temperature, and spatial position) to train a CNN-MLP model to predict the dominant deformation pattern. The resulting model achieves a prediction accuracy of approximately 96% on validation data. A refined evaluation strategy, in which an entire spatial region containing distinct grains was excluded from training, provides a more robust measure of generalization. The approach demonstrates that essential tribological deformation signatures can be automatically identified and classified from structural images using Machine Learning. This proof of concept constitutes a first step towards fully automated, data-driven construction of tribological mechanism maps and, ultimately, toward predictive modeling frameworks that may reduce the need for large-scale MD simulation campaigns.

