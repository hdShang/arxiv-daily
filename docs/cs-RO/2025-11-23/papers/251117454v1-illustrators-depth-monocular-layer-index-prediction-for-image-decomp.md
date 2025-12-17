---
layout: default
title: Illustrator's Depth: Monocular Layer Index Prediction for Image Decomposition
---

# Illustrator's Depth: Monocular Layer Index Prediction for Image Decomposition

**arXiv**: [2511.17454v1](https://arxiv.org/abs/2511.17454) | [PDF](https://arxiv.org/pdf/2511.17454.pdf)

**作者**: Nissim Maruani, Peiying Zhang, Siddhartha Chaudhuri, Matthew Fisher, Nanxuan Zhao, Vladimir G. Kim, Pierre Alliez, Mathieu Desbrun, Wang Yifan

---

## 💡 一句话要点

**提出Illustrator's Depth以解决图像分解为可编辑有序层的挑战**

**关键词**: `图像分解` `层索引预测` `神经网络训练` `图像矢量化` `深度感知编辑`

## 📋 核心要点

1. 核心问题：如何从平面图像分解出可编辑、有序的图层，以支持数字内容创作。
2. 方法要点：定义Illustrator's Depth，通过神经网络预测像素层索引，实现全局一致的离散排序。
3. 实验或效果：在图像矢量化、文本到矢量图形生成等应用中优于基线，支持深度感知编辑。

## 📄 摘要（原文）

> We introduce Illustrator's Depth, a novel definition of depth that addresses a key challenge in digital content creation: decomposing flat images into editable, ordered layers. Inspired by an artist's compositional process, illustrator's depth infers a layer index to each pixel, forming an interpretable image decomposition through a discrete, globally consistent ordering of elements optimized for editability. We also propose and train a neural network using a curated dataset of layered vector graphics to predict layering directly from raster inputs. Our layer index inference unlocks a range of powerful downstream applications. In particular, it significantly outperforms state-of-the-art baselines for image vectorization while also enabling high-fidelity text-to-vector-graphics generation, automatic 3D relief generation from 2D images, and intuitive depth-aware editing. By reframing depth from a physical quantity to a creative abstraction, illustrator's depth prediction offers a new foundation for editable image decomposition.

