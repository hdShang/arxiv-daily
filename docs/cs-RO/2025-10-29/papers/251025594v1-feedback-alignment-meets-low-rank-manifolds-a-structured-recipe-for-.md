---
layout: default
title: Feedback Alignment Meets Low-Rank Manifolds: A Structured Recipe for Local Learning
---

# Feedback Alignment Meets Low-Rank Manifolds: A Structured Recipe for Local Learning

**arXiv**: [2510.25594v1](https://arxiv.org/abs/2510.25594) | [PDF](https://arxiv.org/pdf/2510.25594.pdf)

**作者**: Arani Roy, Marco P. Apolinario, Shristi Das Biswas, Kaushik Roy

---

## 💡 一句话要点

**提出基于SVD低秩流形的结构化局部学习框架，以解决直接反馈对齐的可扩展性问题。**

**关键词**: `局部学习` `低秩流形` `直接反馈对齐` `奇异值分解` `结构化训练` `神经网络优化`

## 📋 核心要点

1. 核心问题：直接反馈对齐在深层网络中因非结构化反馈和可扩展性差而受限。
2. 方法要点：在SVD分解权重上应用复合损失，构建结构化反馈矩阵实现局部更新。
3. 实验或效果：在CIFAR和ImageNet上达到与反向传播相当的精度，减少可训练参数。

## 📄 摘要（原文）

> Training deep neural networks (DNNs) with backpropagation (BP) achieves
> state-of-the-art accuracy but requires global error propagation and full
> parameterization, leading to substantial memory and computational overhead.
> Direct Feedback Alignment (DFA) enables local, parallelizable updates with
> lower memory requirements but is limited by unstructured feedback and poor
> scalability in deeper architectures, specially convolutional neural networks.
> To address these limitations, we propose a structured local learning framework
> that operates directly on low-rank manifolds defined by the Singular Value
> Decomposition (SVD) of weight matrices. Each layer is trained in its decomposed
> form, with updates applied to the SVD components using a composite loss that
> integrates cross-entropy, subspace alignment, and orthogonality regularization.
> Feedback matrices are constructed to match the SVD structure, ensuring
> consistent alignment between forward and feedback pathways. Our method reduces
> the number of trainable parameters relative to the original DFA model, without
> relying on pruning or post hoc compression. Experiments on CIFAR-10, CIFAR-100,
> and ImageNet show that our method achieves accuracy comparable to that of BP.
> Ablation studies confirm the importance of each loss term in the low-rank
> setting. These results establish local learning on low-rank manifolds as a
> principled and scalable alternative to full-rank gradient-based training.

