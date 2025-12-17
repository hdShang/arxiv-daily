---
layout: default
title: SPG-CDENet: Spatial Prior-Guided Cross Dual Encoder Network for Multi-Organ Segmentation
---

# SPG-CDENet: Spatial Prior-Guided Cross Dual Encoder Network for Multi-Organ Segmentation

**arXiv**: [2510.26390v1](https://arxiv.org/abs/2510.26390) | [PDF](https://arxiv.org/pdf/2510.26390.pdf)

**作者**: Xizhi Tian, Changjun Zhou, Yulin. Yang

---

## 💡 一句话要点

**提出SPG-CDENet以解决多器官分割中器官大小和形状变化大的问题**

**关键词**: `多器官分割` `空间先验` `交叉双编码器` `对称交叉注意力` `流式解码器` `医学图像分割`

## 📋 核心要点

1. 多器官分割面临器官大小和形状变化大的挑战
2. 采用两阶段范式，包括空间先验网络和交叉双编码器网络
3. 在公共数据集上实验显示性能优于现有方法，模块有效性得到验证

## 📄 摘要（原文）

> Multi-organ segmentation is a critical task in computer-aided diagnosis.
> While recent deep learning methods have achieved remarkable success in image
> segmentation, huge variations in organ size and shape challenge their
> effectiveness in multi-organ segmentation. To address these challenges, we
> propose a Spatial Prior-Guided Cross Dual Encoder Network (SPG-CDENet), a novel
> two-stage segmentation paradigm designed to improve multi-organ segmentation
> accuracy. Our SPG-CDENet consists of two key components: a spatial prior
> network and a cross dual encoder network. The prior network generates coarse
> localization maps that delineate the approximate ROI, serving as spatial
> guidance for the dual encoder network. The cross dual encoder network comprises
> four essential components: a global encoder, a local encoder, a symmetric
> cross-attention module, and a flow-based decoder. The global encoder captures
> global semantic features from the entire image, while the local encoder focuses
> on features from the prior network. To enhance the interaction between the
> global and local encoders, a symmetric cross-attention module is proposed
> across all layers of the encoders to fuse and refine features. Furthermore, the
> flow-based decoder directly propagates high-level semantic features from the
> final encoder layer to all decoder layers, maximizing feature preservation and
> utilization. Extensive qualitative and quantitative experiments on two public
> datasets demonstrate the superior performance of SPG-CDENet compared to
> existing segmentation methods. Furthermore, ablation studies further validate
> the effectiveness of the proposed modules in improving segmentation accuracy.

