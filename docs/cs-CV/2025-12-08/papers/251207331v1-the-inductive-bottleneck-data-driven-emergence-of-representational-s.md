---
layout: default
title: The Inductive Bottleneck: Data-Driven Emergence of Representational Sparsity in Vision Transformers
---

# The Inductive Bottleneck: Data-Driven Emergence of Representational Sparsity in Vision Transformers

**arXiv**: [2512.07331v1](https://arxiv.org/abs/2512.07331) | [PDF](https://arxiv.org/pdf/2512.07331.pdf)

**作者**: Kanishk Awadhiya

---

## 💡 一句话要点

**揭示视觉Transformer中数据驱动的表示稀疏性，即归纳瓶颈与任务语义抽象相关**

**关键词**: `视觉Transformer` `表示稀疏性` `归纳瓶颈` `有效编码维度` `数据驱动适应` `语义抽象`

## 📋 核心要点

1. 核心问题：视觉Transformer缺乏卷积网络的层次归纳偏置，但常自发形成U形熵分布，中间层压缩信息
2. 方法要点：通过分析DINO训练ViT的层间有效编码维度，探究数据集组成复杂度对表示稀疏性的影响
3. 实验或效果：发现纹理丰富数据集保持高秩表示，而对象中心数据集驱动网络在中间层抑制高频信息，学习语义特征隔离

## 📄 摘要（原文）

> Vision Transformers (ViTs) lack the hierarchical inductive biases inherent to Convolutional Neural Networks (CNNs), theoretically allowing them to maintain high-dimensional representations throughout all layers. However, recent observations suggest ViTs often spontaneously manifest a "U-shaped" entropy profile-compressing information in middle layers before expanding it for the final classification. In this work, we demonstrate that this "Inductive Bottleneck" is not an architectural artifact, but a data-dependent adaptation. By analyzing the layer-wise Effective Encoding Dimension (EED) of DINO-trained ViTs across datasets of varying compositional complexity (UC Merced, Tiny ImageNet, and CIFAR-100), we show that the depth of the bottleneck correlates strongly with the semantic abstraction required by the task. We find that while texture-heavy datasets preserve high-rank representations throughout, object-centric datasets drive the network to dampen high-frequency information in middle layers, effectively "learning" a bottleneck to isolate semantic features.

