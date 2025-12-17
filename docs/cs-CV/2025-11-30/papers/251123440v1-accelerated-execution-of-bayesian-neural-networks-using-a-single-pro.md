---
layout: default
title: Accelerated Execution of Bayesian Neural Networks using a Single Probabilistic Forward Pass and Code Generation
---

# Accelerated Execution of Bayesian Neural Networks using a Single Probabilistic Forward Pass and Code Generation

**arXiv**: [2511.23440v1](https://arxiv.org/abs/2511.23440) | [PDF](https://arxiv.org/pdf/2511.23440.pdf)

**作者**: Bernhard Klein, Falk Selker, Hendrik Borras, Sophie Steger, Franz Pernkopf, Holger Fröning

---

## 💡 一句话要点

**提出基于概率前向传递和代码生成的贝叶斯神经网络加速方法，用于资源受限系统部署。**

**关键词**: `贝叶斯神经网络` `概率前向传递` `不确定性估计` `代码生成` `嵌入式部署` `TVM编译器`

## 📋 核心要点

1. 传统神经网络在安全关键应用中因不确定性处理不足而受限，贝叶斯神经网络计算成本高。
2. 概率前向传递通过高斯分布假设实现单次确定性前向传播，替代采样，提升效率。
3. 结合TVM编译器和优化策略，在嵌入式ARM CPU上实现高效部署，速度提升达4200倍，性能匹配SVI。

## 📄 摘要（原文）

> Machine learning models perform well across domains such as diagnostics, weather forecasting, NLP, and autonomous driving, but their limited uncertainty handling restricts use in safety-critical settings. Traditional neural networks often fail to detect out-of-domain (OOD) data and may output confident yet incorrect predictions. Bayesian neural networks (BNNs) address this by providing probabilistic estimates, but incur high computational cost because predictions require sampling weight distributions and multiple forward passes. The Probabilistic Forward Pass (PFP) offers a highly efficient approximation to Stochastic Variational Inference (SVI) by assuming Gaussian-distributed weights and activations, enabling fully analytic uncertainty propagation and replacing sampling with a single deterministic forward pass. We present an end-to-end pipeline for training, compiling, optimizing, and deploying PFP-based BNNs on embedded ARM CPUs. Using the TVM deep learning compiler, we implement a dedicated library of Gaussian-propagating operators for multilayer perceptrons and convolutional neural networks, combined with manual and automated tuning strategies. Ablation studies show that PFP consistently outperforms SVI in computational efficiency, achieving speedups of up to 4200x for small mini-batches. PFP-BNNs match SVI-BNNs on Dirty-MNIST in accuracy, uncertainty estimation, and OOD detection while greatly reducing compute cost. These results highlight the potential of combining Bayesian approximations with code generation to enable efficient BNN deployment on resource-constrained systems.

