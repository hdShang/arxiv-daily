---
layout: default
title: SynthPix: A lightspeed PIV images generator
---

# SynthPix: A lightspeed PIV images generator

**arXiv**: [2512.09664v1](https://arxiv.org/abs/2512.09664) | [PDF](https://arxiv.org/pdf/2512.09664.pdf)

**作者**: Antonio Terpin, Alan Bonomi, Francesco Banelli, Raffaello D'Andrea

---

## 💡 一句话要点

**提出SynthPix以加速PIV图像生成，支持强化学习训练和实时流体控制开发。**

**关键词**: `粒子图像测速` `合成图像生成` `JAX加速` `强化学习训练` `实时流体控制`

## 📋 核心要点

1. 核心问题：现有PIV图像生成工具性能不足，难以满足数据密集型强化学习训练和实时流体控制迭代需求。
2. 方法要点：基于JAX实现高性能并行合成图像生成器，支持标准配置参数，提升生成吞吐量数个数量级。
3. 实验或效果：未知具体实验细节，但强调在图像对生成每秒的吞吐量上实现显著加速。

## 📄 摘要（原文）

> We describe SynthPix, a synthetic image generator for Particle Image Velocimetry (PIV) with a focus on performance and parallelism on accelerators, implemented in JAX. SynthPix supports the same configuration parameters as existing tools but achieves a throughput several orders of magnitude higher in image-pair generation per second. SynthPix was developed to enable the training of data-hungry reinforcement learning methods for flow estimation and for reducing the iteration times during the development of fast flow estimation methods used in recent active fluids control studies with real-time PIV feedback. We believe SynthPix to be useful for the fluid dynamics community, and in this paper we describe the main ideas behind this software package.

