---
layout: default
title: Spiking Patches: Asynchronous, Sparse, and Efficient Tokens for Event Cameras
---

# Spiking Patches: Asynchronous, Sparse, and Efficient Tokens for Event Cameras

**arXiv**: [2510.26614v1](https://arxiv.org/abs/2510.26614) | [PDF](https://arxiv.org/pdf/2510.26614.pdf)

**作者**: Christoffer Koo Øhrstrøm, Ronja Güldenring, Lazaros Nalpantidis

---

## 💡 一句话要点

**提出Spiking Patches令牌化方法，以保持事件相机异步稀疏特性并提升效率。**

**关键词**: `事件相机` `令牌化` `异步处理` `稀疏表示` `高效推理` `计算机视觉`

## 📋 核心要点

1. 事件相机输出异步稀疏事件流，现有帧或体素表示牺牲这些特性。
2. Spiking Patches令牌化方法生成异步稀疏令牌，保留事件相机独特属性。
3. 实验显示，在姿态识别和物体检测中，速度提升达10.4倍，精度相当或更高。

## 📄 摘要（原文）

> We propose tokenization of events and present a tokenizer, Spiking Patches,
> specifically designed for event cameras. Given a stream of asynchronous and
> spatially sparse events, our goal is to discover an event representation that
> preserves these properties. Prior works have represented events as frames or as
> voxels. However, while these representations yield high accuracy, both frames
> and voxels are synchronous and decrease the spatial sparsity. Spiking Patches
> gives the means to preserve the unique properties of event cameras and we show
> in our experiments that this comes without sacrificing accuracy. We evaluate
> our tokenizer using a GNN, PCN, and a Transformer on gesture recognition and
> object detection. Tokens from Spiking Patches yield inference times that are up
> to 3.4x faster than voxel-based tokens and up to 10.4x faster than frames. We
> achieve this while matching their accuracy and even surpassing in some cases
> with absolute improvements up to 3.8 for gesture recognition and up to 1.4 for
> object detection. Thus, tokenization constitutes a novel direction in
> event-based vision and marks a step towards methods that preserve the
> properties of event cameras.

