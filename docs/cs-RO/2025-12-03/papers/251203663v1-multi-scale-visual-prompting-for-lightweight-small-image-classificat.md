---
layout: default
title: Multi-Scale Visual Prompting for Lightweight Small-Image Classification
---

# Multi-Scale Visual Prompting for Lightweight Small-Image Classification

**arXiv**: [2512.03663v1](https://arxiv.org/abs/2512.03663) | [PDF](https://arxiv.org/pdf/2512.03663.pdf)

**作者**: Salim Khazem

---

## 💡 一句话要点

**提出多尺度视觉提示方法，以提升轻量级小图像分类性能**

**关键词**: `视觉提示` `小图像分类` `多尺度融合` `轻量级模型` `骨干网络无关`

## 📋 核心要点

1. 针对小图像数据集如MNIST和CIFAR-10，视觉提示方法研究不足的问题
2. 引入多尺度视觉提示模块，通过全局、中尺度和局部提示图融合输入图像
3. 实验显示该方法在多种骨干网络上显著提升性能，参数增加小于0.02%

## 📄 摘要（原文）

> Visual prompting has recently emerged as an efficient strategy to adapt vision models using lightweight, learnable parameters injected into the input space. However, prior work mainly targets large Vision Transformers and high-resolution datasets such as ImageNet. In contrast, small-image benchmarks like MNIST, Fashion-MNIST, and CIFAR-10 remain widely used in education, prototyping, and research, yet have received little attention in the context of prompting. In this paper, we introduce \textbf{Multi-Scale Visual Prompting (MSVP)}, a simple and generic module that learns a set of global, mid-scale, and local prompt maps fused with the input image via a lightweight $1 \times 1$ convolution. MSVP is backbone-agnostic, adds less than $0.02\%$ parameters, and significantly improves performance across CNN and Vision Transformer backbones.
>   We provide a unified benchmark on MNIST, Fashion-MNIST, and CIFAR-10 using a simple CNN, ResNet-18, and a small Vision Transformer. Our method yields consistent improvements with negligible computational overhead. We further include ablations on prompt scales, fusion strategies, and backbone architectures, along with qualitative analyzes using prompt visualizations and Grad-CAM. Our results demonstrate that multi-scale prompting provides an effective inductive bias even on low-resolution images.

