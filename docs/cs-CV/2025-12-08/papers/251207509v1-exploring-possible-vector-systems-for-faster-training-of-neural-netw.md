---
layout: default
title: Exploring possible vector systems for faster training of neural networks with preconfigured latent spaces
---

# Exploring possible vector systems for faster training of neural networks with preconfigured latent spaces

**arXiv**: [2512.07509v1](https://arxiv.org/abs/2512.07509) | [PDF](https://arxiv.org/pdf/2512.07509.pdf)

**作者**: Nikita Gabdullin

---

## 💡 一句话要点

**探索预定义向量系统以加速具有预配置潜在空间的神经网络训练**

**关键词**: `潜在空间配置` `向量系统` `神经网络训练加速` `超多类别分类` `嵌入优化` `收敛加速`

## 📋 核心要点

1. 研究预定义向量系统（如An根系向量）用于配置潜在空间结构，以优化神经网络嵌入分布。
2. 利用向量系统训练分类器网络无需分类层，适用于超多类别数据集，加速ImageNet-1K和50k-600k类别训练。
3. 实验表明最小化潜在空间维度可加速收敛，并可能减少嵌入存储的向量数据库大小。

## 📄 摘要（原文）

> The overall neural network (NN) performance is closely related to the properties of its embedding distribution in latent space (LS). It has recently been shown that predefined vector systems, specifically An root system vectors, can be used as targets for latent space configurations (LSC) to ensure the desired LS structure. One of the main LSC advantage is the possibility of training classifier NNs without classification layers, which facilitates training NNs on datasets with extremely large numbers of classes. This paper provides a more general overview of possible vector systems for NN training along with their properties and methods for vector system construction. These systems are used to configure LS of encoders and visual transformers to significantly speed up ImageNet-1K and 50k-600k classes LSC training. It is also shown that using the minimum number of LS dimensions for a specific number of classes results in faster convergence. The latter has potential advantages for reducing the size of vector databases used to store NN embeddings.

