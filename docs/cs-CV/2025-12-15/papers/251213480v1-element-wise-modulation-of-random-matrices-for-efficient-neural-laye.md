---
layout: default
title: Element-wise Modulation of Random Matrices for Efficient Neural Layers
---

# Element-wise Modulation of Random Matrices for Efficient Neural Layers

**arXiv**: [2512.13480v1](https://arxiv.org/abs/2512.13480) | [PDF](https://arxiv.org/pdf/2512.13480.pdf)

**作者**: Maksymilian Szorc

---

## 💡 一句话要点

**提出参数化随机投影层以解决全连接层内存与计算开销问题**

**关键词**: `全连接层压缩` `随机投影` `参数化调制` `轻量神经网络` `资源受限部署`

## 📋 核心要点

1. 全连接层因密集参数化导致内存与计算开销大，现有压缩技术常引入复杂权衡或性能下降
2. 使用固定随机矩阵与轻量可学习逐元素参数解耦特征混合与适应，大幅减少可训练参数至线性规模
3. 在多种基准测试中保持可靠精度，为资源受限场景提供稳定高效架构

## 📄 摘要（原文）

> Fully connected layers are a primary source of memory and computational overhead in deep neural networks due to their dense, often redundant parameterization. While various compression techniques exist, they frequently introduce complex engineering trade-offs or degrade model performance. We propose the Parametrized Random Projection (PRP) layer, a novel approach that decouples feature mixing from adaptation by utilizing a fixed random matrix modulated by lightweight, learnable element-wise parameters. This architecture drastically reduces the trainable parameter count to a linear scale while retaining reliable accuracy across various benchmarks. The design serves as a stable, computationally efficient solution for architectural scaling and deployment in resource-limited settings.

