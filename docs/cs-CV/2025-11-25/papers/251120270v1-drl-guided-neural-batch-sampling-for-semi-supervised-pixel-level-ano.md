---
layout: default
title: DRL-Guided Neural Batch Sampling for Semi-Supervised Pixel-Level Anomaly Detection
---

# DRL-Guided Neural Batch Sampling for Semi-Supervised Pixel-Level Anomaly Detection

**arXiv**: [2511.20270v1](https://arxiv.org/abs/2511.20270) | [PDF](https://arxiv.org/pdf/2511.20270.pdf)

**作者**: Amirhossein Khadivi Noghredeh, Abdollah Safari, Fatemeh Ziaeetabar, Firoozeh Haghighi

---

## 💡 一句话要点

**提出基于深度强化学习的神经批采样方法，以解决工业视觉中像素级异常检测问题**

**关键词**: `像素级异常检测` `半监督学习` `深度强化学习` `神经批采样` `工业视觉检查` `自编码器`

## 📋 核心要点

1. 核心问题：工业视觉异常检测中缺陷样本稀缺，现有方法易过拟合且难以检测细微缺陷
2. 方法要点：集成强化学习采样器、自编码器和预测器，通过复合奖励自适应选择信息性图像块
3. 实验效果：在MVTec AD数据集上，F1_max和AUC指标优于现有方法，定位细微异常更准确

## 📄 摘要（原文）

> Anomaly detection in industrial visual inspection is challenging due to the scarcity of defective samples. Most existing methods rely on unsupervised reconstruction using only normal data, often resulting in overfitting and poor detection of subtle defects. We propose a semi-supervised deep reinforcement learning framework that integrates a neural batch sampler, an autoencoder, and a predictor. The RL-based sampler adaptively selects informative patches by balancing exploration and exploitation through a composite reward. The autoencoder generates loss profiles highlighting abnormal regions, while the predictor performs segmentation in the loss-profile space. This interaction enables the system to effectively learn both normal and defective patterns with limited labeled data. Experiments on the MVTec AD dataset demonstrate that our method achieves higher accuracy and better localization of subtle anomalies than recent state-of-the-art approaches while maintaining low complexity, yielding an average improvement of 0.15 in F1_max and 0.06 in AUC, with a maximum gain of 0.37 in F1_max in the best case.

