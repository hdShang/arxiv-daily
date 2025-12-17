---
layout: default
title: Extreme Model Compression with Structured Sparsity at Low Precision
---

# Extreme Model Compression with Structured Sparsity at Low Precision

**arXiv**: [2511.08360v1](https://arxiv.org/abs/2511.08360) | [PDF](https://arxiv.org/pdf/2511.08360.pdf)

**作者**: Dan Liu, Nikita Dvornik, Xue Liu

---

## 💡 一句话要点

**提出SLOPE框架，结合结构化稀疏与低精度量化以压缩模型**

**关键词**: `模型压缩` `结构化稀疏` `低精度量化` `训练正则化` `角度对齐`

## 📋 核心要点

1. 核心问题：深度神经网络在资源受限设备上部署困难，稀疏与量化结合会严重损害精度
2. 方法要点：通过训练时正则化策略，促进权重角度对齐而非直接匹配
3. 实验或效果：在ResNet-18上实现约20倍模型压缩，保持约99%原始精度

## 📄 摘要（原文）

> Deep neural networks (DNNs) are used in many applications, but their large size and high computational cost make them hard to run on devices with limited resources. Two widely used techniques to address this challenge are weight quantization, which lowers the precision of all weights, and structured sparsity, which removes unimportant weights while retaining the important ones at full precision. Although both are effective individually, they are typically studied in isolation due to their compounded negative impact on model accuracy when combined. In this work, we introduce SLOPE Structured Sparsity at Low Precision), a unified framework, to effectively combine structured sparsity and low-bit quantization in a principled way. We show that naively combining sparsity and quantization severely harms performance due to the compounded impact of both techniques. To address this, we propose a training-time regularization strategy that minimizes the discrepancy between full-precision weights and their sparse, quantized counterparts by promoting angular alignment rather than direct matching. On ResNet-18, SLOPE achieves $\sim20\times$ model size reduction while retaining $\sim$99% of the original accuracy. It consistently outperforms state-of-the-art quantization and structured sparsity methods across classification, detection, and segmentation tasks on models such as ResNet-18, ViT-Small, and Mask R-CNN.

