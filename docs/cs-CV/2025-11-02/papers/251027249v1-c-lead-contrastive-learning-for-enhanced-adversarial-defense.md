---
layout: default
title: C-LEAD: Contrastive Learning for Enhanced Adversarial Defense
---

# C-LEAD: Contrastive Learning for Enhanced Adversarial Defense

**arXiv**: [2510.27249v1](https://arxiv.org/abs/2510.27249) | [PDF](https://arxiv.org/pdf/2510.27249.pdf)

**作者**: Suklav Ghosh, Sonal Kumar, Arijit Sur

---

## 💡 一句话要点

**提出基于对比学习的对抗防御方法以增强深度神经网络鲁棒性**

**关键词**: `对抗防御` `对比学习` `深度神经网络` `鲁棒性` `图像分类`

## 📋 核心要点

1. 深度神经网络易受对抗攻击影响，导致输入微小扰动时预测错误
2. 利用对比损失函数训练模型，结合干净与对抗扰动图像学习鲁棒表示
3. 实验显示模型对多种对抗扰动鲁棒性显著提升，特征更具信息性和弹性

## 📄 摘要（原文）

> Deep neural networks (DNNs) have achieved remarkable success in computer
> vision tasks such as image classification, segmentation, and object detection.
> However, they are vulnerable to adversarial attacks, which can cause incorrect
> predictions with small perturbations in input images. Addressing this issue is
> crucial for deploying robust deep-learning systems. This paper presents a novel
> approach that utilizes contrastive learning for adversarial defense, a
> previously unexplored area. Our method leverages the contrastive loss function
> to enhance the robustness of classification models by training them with both
> clean and adversarially perturbed images. By optimizing the model's parameters
> alongside the perturbations, our approach enables the network to learn robust
> representations that are less susceptible to adversarial attacks. Experimental
> results show significant improvements in the model's robustness against various
> types of adversarial perturbations. This suggests that contrastive loss helps
> extract more informative and resilient features, contributing to the field of
> adversarial robustness in deep learning.

