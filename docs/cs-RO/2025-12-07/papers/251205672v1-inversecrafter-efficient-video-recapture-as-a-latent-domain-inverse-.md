---
layout: default
title: InverseCrafter: Efficient Video ReCapture as a Latent Domain Inverse Problem
---

# InverseCrafter: Efficient Video ReCapture as a Latent Domain Inverse Problem

**arXiv**: [2512.05672v1](https://arxiv.org/abs/2512.05672) | [PDF](https://arxiv.org/pdf/2512.05672.pdf)

**作者**: Yeobin Hong, Suhyeon Lee, Hyungjin Chung, Jong Chul Ye

---

## 💡 一句话要点

**提出InverseCrafter，将4D视频生成重构为潜在空间修复问题以提升效率**

**关键词**: `4D视频生成` `潜在空间修复` `视频扩散模型` `计算效率` `视频编辑`

## 📋 核心要点

1. 核心问题：现有可控4D视频生成方法依赖微调视频扩散模型，计算成本高且易遗忘原始生成先验
2. 方法要点：设计机制将像素空间退化算子编码为连续多通道潜在掩码，避免重复VAE操作和反向传播
3. 实验或效果：在相机控制任务中实现可比新视角生成和更优测量一致性，计算开销近零，并擅长通用视频修复编辑

## 📄 摘要（原文）

> Recent approaches to controllable 4D video generation often rely on fine-tuning pre-trained Video Diffusion Models (VDMs). This dominant paradigm is computationally expensive, requiring large-scale datasets and architectural modifications, and frequently suffers from catastrophic forgetting of the model's original generative priors. Here, we propose InverseCrafter, an efficient inpainting inverse solver that reformulates the 4D generation task as an inpainting problem solved in the latent space. The core of our method is a principled mechanism to encode the pixel space degradation operator into a continuous, multi-channel latent mask, thereby bypassing the costly bottleneck of repeated VAE operations and backpropagation. InverseCrafter not only achieves comparable novel view generation and superior measurement consistency in camera control tasks with near-zero computational overhead, but also excels at general-purpose video inpainting with editing. Code is available at https://github.com/yeobinhong/InverseCrafter.

