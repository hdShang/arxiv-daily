---
layout: default
title: Attention Via Convolutional Nearest Neighbors
---

# Attention Via Convolutional Nearest Neighbors

**arXiv**: [2511.14137v1](https://arxiv.org/abs/2511.14137) | [PDF](https://arxiv.org/pdf/2511.14137.pdf)

**作者**: Mingi Kang, Jeová Farias Sales Rocha Neto

---

## 💡 一句话要点

**提出卷积最近邻框架以统一卷积与注意力，提升图像分类性能**

**关键词**: `卷积神经网络` `自注意力机制` `k近邻聚合` `图像分类` `架构统一` `正则化效果`

## 📋 核心要点

1. 核心问题：卷积与自注意力被视为不同架构，缺乏统一理论框架
2. 方法要点：基于k近邻聚合，卷积选空间邻近，注意力选特征相似
3. 实验效果：在CIFAR数据集上，混合架构和ViT变体均优于标准方法

## 📄 摘要（原文）

> The shift from Convolutional Neural Networks to Transformers has reshaped computer vision, yet these two architectural families are typically viewed as fundamentally distinct. We argue that convolution and self-attention, despite their apparent differences, can be unified within a single k-nearest neighbor aggregation framework. The critical insight is that both operations are special cases of neighbor selection and aggregation; convolution selects neighbors by spatial proximity, while attention selects by feature similarity, revealing they exist on a continuous spectrum. We introduce Convolutional Nearest Neighbors (ConvNN), a unified framework that formalizes this connection. Crucially, ConvNN serves as a drop-in replacement for convolutional and attention layers, enabling systematic exploration of the intermediate spectrum between these two extremes. We validate the framework's coherence on CIFAR-10 and CIFAR-100 classification tasks across two complementary architectures: (1) Hybrid branching in VGG improves accuracy on both CIFAR datasets by combining spatial-proximity and feature-similarity selection; and (2) ConvNN in ViT outperforms standard attention and other attention variants on both datasets. Extensive ablations on $k$ values and architectural variants reveal that interpolating along this spectrum provides regularization benefits by balancing local and global receptive fields. Our work provides a unifying framework that dissolves the apparent distinction between convolution and attention, with implications for designing more principled and interpretable vision architectures.

