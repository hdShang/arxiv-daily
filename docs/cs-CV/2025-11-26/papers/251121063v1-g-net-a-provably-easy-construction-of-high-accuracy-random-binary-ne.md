---
layout: default
title: G-Net: A Provably Easy Construction of High-Accuracy Random Binary Neural Networks
---

# G-Net: A Provably Easy Construction of High-Accuracy Random Binary Neural Networks

**arXiv**: [2511.21063v1](https://arxiv.org/abs/2511.21063) | [PDF](https://arxiv.org/pdf/2511.21063.pdf)

**作者**: Alireza Aghasi, Nicholas Marshall, Saeid Pourmand, Wyatt Whiting

---

## 💡 一句话要点

**提出G-Net随机算法以构建高精度二进制神经网络，基于超维计算。**

**关键词**: `二进制神经网络` `超维计算` `随机算法` `高精度模型` `理论保证`

## 📋 核心要点

1. 核心问题：传统低精度方法依赖量化，难以保证二进制神经网络的高精度。
2. 方法要点：使用随机二进制嵌入和超维计算，保留浮点网络精度，有理论保证。
3. 实验或效果：在CIFAR-10上准确率比先前HDC模型高近30%，匹配CNN精度。

## 📄 摘要（原文）

> We propose a novel randomized algorithm for constructing binary neural networks with tunable accuracy. This approach is motivated by hyperdimensional computing (HDC), which is a brain-inspired paradigm that leverages high-dimensional vector representations, offering efficient hardware implementation and robustness to model corruptions. Unlike traditional low-precision methods that use quantization, we consider binary embeddings of data as points in the hypercube equipped with the Hamming distance. We propose a novel family of floating-point neural networks, G-Nets, which are general enough to mimic standard network layers. Each floating-point G-Net has a randomized binary embedding, an embedded hyperdimensional (EHD) G-Net, that retains the accuracy of its floating-point counterparts, with theoretical guarantees, due to the concentration of measure. Empirically, our binary models match convolutional neural network accuracies and outperform prior HDC models by large margins, for example, we achieve almost 30\% higher accuracy on CIFAR-10 compared to prior HDC models. G-Nets are a theoretically justified bridge between neural networks and randomized binary neural networks, opening a new direction for constructing robust binary/quantized deep learning models. Our implementation is available at https://github.com/GNet2025/GNet.

