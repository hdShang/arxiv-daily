---
layout: default
title: Scalable Formal Verification via Autoencoder Latent Space Abstraction
---

# Scalable Formal Verification via Autoencoder Latent Space Abstraction

**arXiv**: [2512.13593v1](https://arxiv.org/abs/2512.13593) | [PDF](https://arxiv.org/pdf/2512.13593.pdf)

**作者**: Robert Reed, Morteza Lahijanian, Luca Laurenti

---

## 💡 一句话要点

**提出基于凸自编码器潜在空间抽象的可扩展形式验证方法，以解决高维系统验证的扩展性问题。**

**关键词**: `形式验证` `自编码器` `潜在空间抽象` `可扩展性` `高维系统` `核方法`

## 📋 核心要点

1. 核心问题：高维系统形式验证面临状态空间离散化导致的指数级扩展性挑战。
2. 方法要点：使用凸自编码器降维，基于核方法学习潜在空间动态，并构建包含原始系统行为的有限抽象。
3. 实验或效果：在包括26D神经网络控制系统在内的多个系统上验证，显著提升扩展性而不失严谨性。

## 📄 摘要（原文）

> Finite Abstraction methods provide a powerful formal framework for proving that systems satisfy their specifications. However, these techniques face scalability challenges for high-dimensional systems, as they rely on state-space discretization which grows exponentially with dimension. Learning-based approaches to dimensionality reduction, utilizing neural networks and autoencoders, have shown great potential to alleviate this problem. However, ensuring the correctness of the resulting verification results remains an open question. In this work, we provide a formal approach to reduce the dimensionality of systems via convex autoencoders and learn the dynamics in the latent space through a kernel-based method. We then construct a finite abstraction from the learned model in the latent space and guarantee that the abstraction contains the true behaviors of the original system. We show that the verification results in the latent space can be mapped back to the original system. Finally, we demonstrate the effectiveness of our approach on multiple systems, including a 26D system controlled by a neural network, showing significant scalability improvements without loss of rigor.

