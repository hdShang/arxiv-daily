---
layout: default
title: FeatureLens: A Highly Generalizable and Interpretable Framework for Detecting Adversarial Examples Based on Image Features
---

# FeatureLens: A Highly Generalizable and Interpretable Framework for Detecting Adversarial Examples Based on Image Features

**arXiv**: [2512.03625v1](https://arxiv.org/abs/2512.03625) | [PDF](https://arxiv.org/pdf/2512.03625.pdf)

**作者**: Zhigang Yang, Yuan Liu, Jiawei Zhang, Puning Zhang, Xinqiang Ma

---

## 💡 一句话要点

**提出FeatureLens框架，基于图像特征检测对抗样本，实现高泛化性与可解释性。**

**关键词**: `对抗样本检测` `图像特征分析` `轻量级框架` `可解释性` `泛化性能`

## 📋 核心要点

1. 核心问题：深度神经网络易受对抗攻击，现有检测方法复杂且泛化性差。
2. 方法要点：使用轻量级图像特征提取器和浅层分类器，仅需51维特征进行检测。
3. 实验或效果：在多种攻击下，检测准确率高达99.75%，泛化评估达99.6%，参数少至1,000。

## 📄 摘要（原文）

> Although the remarkable performance of deep neural networks (DNNs) in image classification, their vulnerability to adversarial attacks remains a critical challenge. Most existing detection methods rely on complex and poorly interpretable architectures, which compromise interpretability and generalization. To address this, we propose FeatureLens, a lightweight framework that acts as a lens to scrutinize anomalies in image features. Comprising an Image Feature Extractor (IFE) and shallow classifiers (e.g., SVM, MLP, or XGBoost) with model sizes ranging from 1,000 to 30,000 parameters, FeatureLens achieves high detection accuracy ranging from 97.8% to 99.75% in closed-set evaluation and 86.17% to 99.6% in generalization evaluation across FGSM, PGD, CW, and DAmageNet attacks, using only 51 dimensional features. By combining strong detection performance with excellent generalization, interpretability, and computational efficiency, FeatureLens offers a practical pathway toward transparent and effective adversarial defense.

