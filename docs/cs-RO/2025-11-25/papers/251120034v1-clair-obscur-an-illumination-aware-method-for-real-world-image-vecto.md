---
layout: default
title: Clair Obscur: an Illumination-Aware Method for Real-World Image Vectorization
---

# Clair Obscur: an Illumination-Aware Method for Real-World Image Vectorization

**arXiv**: [2511.20034v1](https://arxiv.org/abs/2511.20034) | [PDF](https://arxiv.org/pdf/2511.20034.pdf)

**作者**: Xingyue Lin, Shuai Peng, Xiangyu Xie, Jianhua Zhu, Yuxuan Zhou, Liangcai Gao

---

## 💡 一句话要点

**提出COVec框架，通过光照感知向量化解决真实世界图像编辑性问题**

**关键词**: `图像向量化` `内在图像分解` `光照感知` `可编辑向量表示` `真实世界图像`

## 📋 核心要点

1. 现有向量化方法在真实世界图像中产生碎片化形状，牺牲语义简洁性
2. 引入内在图像分解，在向量域分离反照率、阴影和光照层
3. 实验显示COVec在多个数据集上实现更高视觉保真度和可编辑性

## 📄 摘要（原文）

> Image vectorization aims to convert raster images into editable, scalable vector representations while preserving visual fidelity. Existing vectorization methods struggle to represent complex real-world images, often producing fragmented shapes at the cost of semantic conciseness. In this paper, we propose COVec, an illumination-aware vectorization framework inspired by the Clair-Obscur principle of light-shade contrast. COVec is the first to introduce intrinsic image decomposition in the vector domain, separating an image into albedo, shade, and light layers in a unified vector representation. A semantic-guided initialization and two-stage optimization refine these layers with differentiable rendering. Experiments on various datasets demonstrate that COVec achieves higher visual fidelity and significantly improved editability compared to existing methods.

