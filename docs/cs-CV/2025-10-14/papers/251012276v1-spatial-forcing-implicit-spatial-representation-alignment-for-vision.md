---
layout: default
title: Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model
---

# Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model

**arXiv**: [2510.12276v1](https://arxiv.org/abs/2510.12276) | [PDF](https://arxiv.org/pdf/2510.12276.pdf)

**作者**: Fuhao Li, Wenxuan Song, Han Zhao, Jingbo Wang, Pengxiang Ding, Donglin Wang, Long Zeng, Haoang Li

---

## 💡 一句话要点

**提出Spatial Forcing以增强视觉-语言-动作模型在3D空间中的动作精度**

**关键词**: `视觉-语言-动作模型` `空间表示对齐` `3D感知` `机器人控制` `嵌入对齐` `训练加速`

## 📋 核心要点

1. 核心问题：基于2D数据的VLA模型缺乏空间感知，影响3D物理世界操作
2. 方法要点：通过中间层嵌入对齐，强制VLA模型学习隐式空间表示
3. 实验或效果：在仿真和真实环境中实现SOTA，加速训练并提升数据效率

## 📄 摘要（原文）

> Vision-language-action (VLA) models have recently shown strong potential in
> enabling robots to follow language instructions and execute precise actions.
> However, most VLAs are built upon vision-language models pretrained solely on
> 2D data, which lack accurate spatial awareness and hinder their ability to
> operate in the 3D physical world. Existing solutions attempt to incorporate
> explicit 3D sensor inputs such as depth maps or point clouds, but these
> approaches face challenges due to sensor noise, hardware heterogeneity, and
> incomplete depth coverage in existing datasets. Alternative methods that
> estimate 3D cues from 2D images also suffer from the limited performance of
> depth estimators.We propose Spatial Forcing (SF), a simple yet effective
> alignment strategy that implicitly forces VLA models to develop spatial
> comprehension capabilities without relying on explicit 3D inputs or depth
> estimators. SF aligns intermediate visual embeddings of VLAs with geometric
> representations produced by pretrained 3D foundation models. By enforcing
> alignment at intermediate layers, SF guides VLAs to encode richer spatial
> representations that enhance action precision.Extensive experiments in
> simulation and real-world environments demonstrate that SF achieves
> state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further
> accelerates training by up to 3.8x and improves data efficiency across diverse
> robotic tasks. Project page is at https://spatial-forcing.github.io/

