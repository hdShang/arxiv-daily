---
layout: default
title: ResNet: Enabling Deep Convolutional Neural Networks through Residual Learning
---

# ResNet: Enabling Deep Convolutional Neural Networks through Residual Learning

**arXiv**: [2510.24036v1](https://arxiv.org/abs/2510.24036) | [PDF](https://arxiv.org/pdf/2510.24036.pdf)

**作者**: Xingyu Liu, Kun Ming Goh

---

## 💡 一句话要点

**提出残差网络以解决深度卷积神经网络训练中的梯度消失问题**

**关键词**: `残差网络` `跳跃连接` `梯度消失` `深度卷积神经网络` `CIFAR-10`

## 📋 核心要点

1. 核心问题：深度卷积神经网络训练困难，主要由于梯度消失问题
2. 方法要点：引入跳跃连接，使梯度可直接通过捷径传播
3. 实验或效果：在CIFAR-10数据集上，ResNet-18准确率达89.9%，优于传统深度CNN

## 📄 摘要（原文）

> Convolutional Neural Networks (CNNs) has revolutionized computer vision, but
> training very deep networks has been challenging due to the vanishing gradient
> problem. This paper explores Residual Networks (ResNet), introduced by He et
> al. (2015), which overcomes this limitation by using skip connections. ResNet
> enables the training of networks with hundreds of layers by allowing gradients
> to flow directly through shortcut connections that bypass intermediate layers.
> In our implementation on the CIFAR-10 dataset, ResNet-18 achieves 89.9%
> accuracy compared to 84.1% for a traditional deep CNN of similar depth, while
> also converging faster and training more stably.

