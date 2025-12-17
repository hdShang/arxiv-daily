---
layout: default
title: Multi-Scale High-Resolution Logarithmic Grapher Module for Efficient Vision GNNs
---

# Multi-Scale High-Resolution Logarithmic Grapher Module for Efficient Vision GNNs

**arXiv**: [2510.13740v1](https://arxiv.org/abs/2510.13740) | [PDF](https://arxiv.org/pdf/2510.13740.pdf)

**作者**: Mustafa Munir, Alex Zhang, Radu Marculescu

---

## 💡 一句话要点

**提出LogViG模型，通过LSGC图构建方法提升视觉图神经网络效率与性能。**

**关键词**: `视觉图神经网络` `图构建方法` `多尺度架构` `高分辨率特征` `图像分类` `语义分割`

## 📋 核心要点

1. 问题：传统图构建方法如KNN在大型图像上计算昂贵，且固定尺度方法易导致过压缩和信息缺失。
2. 方法：引入对数可扩展图构建(LSGC)限制长程连接，并设计多尺度高分辨率分支融合特征。
3. 效果：在ImageNet等任务上，LogViG在准确率、参数和计算量上优于现有ViG、CNN和ViT模型。

## 📄 摘要（原文）

> Vision graph neural networks (ViG) have demonstrated promise in vision tasks
> as a competitive alternative to conventional convolutional neural nets (CNN)
> and transformers (ViTs); however, common graph construction methods, such as
> k-nearest neighbor (KNN), can be expensive on larger images. While methods such
> as Sparse Vision Graph Attention (SVGA) have shown promise, SVGA's fixed step
> scale can lead to over-squashing and missing multiple connections to gain the
> same information that could be gained from a long-range link. Through this
> observation, we propose a new graph construction method, Logarithmic Scalable
> Graph Construction (LSGC) to enhance performance by limiting the number of
> long-range links. To this end, we propose LogViG, a novel hybrid CNN-GNN model
> that utilizes LSGC. Furthermore, inspired by the successes of multi-scale and
> high-resolution architectures, we introduce and apply a high-resolution branch
> and fuse features between our high-resolution and low-resolution branches for a
> multi-scale high-resolution Vision GNN network. Extensive experiments show that
> LogViG beats existing ViG, CNN, and ViT architectures in terms of accuracy,
> GMACs, and parameters on image classification and semantic segmentation tasks.
> Our smallest model, Ti-LogViG, achieves an average top-1 accuracy on
> ImageNet-1K of 79.9% with a standard deviation of 0.2%, 1.7% higher average
> accuracy than Vision GNN with a 24.3% reduction in parameters and 35.3%
> reduction in GMACs. Our work shows that leveraging long-range links in graph
> construction for ViGs through our proposed LSGC can exceed the performance of
> current state-of-the-art ViGs. Code is available at
> https://github.com/mmunir127/LogViG-Official.

