---
layout: default
title: PointCNN++: Performant Convolution on Native Points
---

# PointCNN++: Performant Convolution on Native Points

**arXiv**: [2511.23227v1](https://arxiv.org/abs/2511.23227) | [PDF](https://arxiv.org/pdf/2511.23227.pdf)

**作者**: Lihan Li, Haofeng Zhong, Rui Bu, Mingchao Sun, Wenzheng Chen, Baoquan Chen, Yangyan Li

---

## 💡 一句话要点

**提出PointCNN++以解决点云卷积中几何精度与计算性能的权衡问题**

**关键词**: `点云卷积` `几何精度` `计算性能` `GPU优化` `点云配准` `稀疏卷积`

## 📋 核心要点

1. 现有方法在点云卷积中存在几何精度与性能的权衡：点方法精度高但性能低，体素方法性能高但精度低
2. PointCNN++将稀疏卷积从体素推广到点，设计基于原始点坐标的点中心卷积和高效GPU内核
3. 实验显示PointCNN++比点方法内存少一个数量级、速度快数倍，并显著提升点云配准精度

## 📄 摘要（原文）

> Existing convolutional learning methods for 3D point cloud data are divided into two paradigms: point-based methods that preserve geometric precision but often face performance challenges, and voxel-based methods that achieve high efficiency through quantization at the cost of geometric fidelity. This loss of precision is a critical bottleneck for tasks such as point cloud registration. We propose PointCNN++, a novel architectural design that fundamentally mitigates this precision-performance trade-off. It \textbf{generalizes sparse convolution from voxels to points}, treating voxel-based convolution as a specialized, degraded case of our more general point-based convolution. First, we introduce a point-centric convolution where the receptive field is centered on the original, high-precision point coordinates. Second, to make this high-fidelity operation performant, we design a computational strategy that operates \textbf{natively} on points. We formulate the convolution on native points as a Matrix-Vector Multiplication and Reduction (MVMR) problem, for which we develop a dedicated, highly-optimized GPU kernel. Experiments demonstrate that PointCNN++ \textbf{uses an order of magnitude less memory and is several times faster} than representative point-based methods. Furthermore, when used as a simple replacement for the voxel-based backbones it generalizes, it \textbf{significantly improves point cloud registration accuracies while proving both more memory-efficient and faster}. PointCNN++ shows that preserving geometric detail and achieving high performance are not mutually exclusive, paving the way for a new class of 3D learning with high fidelity and efficiency. Our code will be open sourced.

