---
layout: default
title: LightsOut: Diffusion-based Outpainting for Enhanced Lens Flare Removal
---

# LightsOut: Diffusion-based Outpainting for Enhanced Lens Flare Removal

**arXiv**: [2510.15868v1](https://arxiv.org/abs/2510.15868) | [PDF](https://arxiv.org/pdf/2510.15868.pdf)

**作者**: Shr-Ruei Tsai, Wei-Cheng Chang, Jie-Ying Lee, Chih-Hai Su, Yu-Lun Liu

---

## 💡 一句话要点

**提出LightsOut扩散外绘框架以增强镜头光晕移除性能**

**关键词**: `镜头光晕移除` `扩散模型` `图像外绘` `LoRA微调` `预处理增强`

## 📋 核心要点

1. 核心问题：离帧光源不完整或缺失导致单图像光晕移除方法性能下降
2. 方法要点：利用多任务回归模块和LoRA微调扩散模型实现物理一致外绘
3. 实验或效果：无需额外训练即可提升现有方法性能，作为通用预处理方案

## 📄 摘要（原文）

> Lens flare significantly degrades image quality, impacting critical computer
> vision tasks like object detection and autonomous driving. Recent Single Image
> Flare Removal (SIFR) methods perform poorly when off-frame light sources are
> incomplete or absent. We propose LightsOut, a diffusion-based outpainting
> framework tailored to enhance SIFR by reconstructing off-frame light sources.
> Our method leverages a multitask regression module and LoRA fine-tuned
> diffusion model to ensure realistic and physically consistent outpainting
> results. Comprehensive experiments demonstrate LightsOut consistently boosts
> the performance of existing SIFR methods across challenging scenarios without
> additional retraining, serving as a universally applicable plug-and-play
> preprocessing solution. Project page: https://ray-1026.github.io/lightsout/

