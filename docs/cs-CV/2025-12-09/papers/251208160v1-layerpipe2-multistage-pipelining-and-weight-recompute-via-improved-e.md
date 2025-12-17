---
layout: default
title: LayerPipe2: Multistage Pipelining and Weight Recompute via Improved Exponential Moving Average for Training Neural Networks
---

# LayerPipe2: Multistage Pipelining and Weight Recompute via Improved Exponential Moving Average for Training Neural Networks

**arXiv**: [2512.08160v1](https://arxiv.org/abs/2512.08160) | [PDF](https://arxiv.org/pdf/2512.08160.pdf)

**作者**: Nanda K. Unnikrishnan, Keshab K. Parhi

---

## 💡 一句话要点

**提出LayerPipe2框架，通过延迟梯度分析和权重重构实现可扩展的神经网络流水线训练**

**关键词**: `神经网络训练` `流水线并行` `梯度延迟` `权重重构` `内存优化` `可扩展性`

## 📋 核心要点

1. 核心问题：流水线训练中梯度延迟的量化与历史权重存储瓶颈
2. 方法要点：基于网络结构推导延迟需求，开发流水线感知移动平均重构权重
3. 实验或效果：降低内存成本，保持精度，支持可控计算通信权衡

## 📄 摘要（原文）

> In our prior work, LayerPipe, we had introduced an approach to accelerate training of convolutional, fully connected, and spiking neural networks by overlapping forward and backward computation. However, despite empirical success, a principled understanding of how much gradient delay needs to be introduced at each layer to achieve desired level of pipelining was not addressed. This paper, LayerPipe2, fills that gap by formally deriving LayerPipe using variable delayed gradient adaptation and retiming. We identify where delays may be legally inserted and show that the required amount of delay follows directly from the network structure where inner layers require fewer delays and outer layers require longer delays. When pipelining is applied at every layer, the amount of delay depends only on the number of remaining downstream stages. When layers are pipelined in groups, all layers in the group share the same assignment of delays. These insights not only explain previously observed scheduling patterns but also expose an often overlooked challenge that pipelining implicitly requires storage of historical weights. We overcome this storage bottleneck by developing a pipeline--aware moving average that reconstructs the required past states rather than storing them explicitly. This reduces memory cost without sacrificing the accuracy guarantees that makes pipelined learning viable. The result is a principled framework that illustrates how to construct LayerPipe architectures, predicts their delay requirements, and mitigates their storage burden, thereby enabling scalable pipelined training with controlled communication computation tradeoffs.

