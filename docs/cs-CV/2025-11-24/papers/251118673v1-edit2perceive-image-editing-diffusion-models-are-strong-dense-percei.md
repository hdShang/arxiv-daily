---
layout: default
title: Edit2Perceive: Image Editing Diffusion Models Are Strong Dense Perceivers
---

# Edit2Perceive: Image Editing Diffusion Models Are Strong Dense Perceivers

**arXiv**: [2511.18673v1](https://arxiv.org/abs/2511.18673) | [PDF](https://arxiv.org/pdf/2511.18673.pdf)

**作者**: Yiqing Shi, Yiren Song, Mike Zheng Shou

---

## 💡 一句话要点

**提出Edit2Perceive框架，利用图像编辑扩散模型进行密集感知任务**

**关键词**: `扩散模型` `密集感知` `图像编辑` `几何感知` `一致性损失`

## 📋 核心要点

1. 核心问题：传统密集感知方法依赖文本到图像生成器，缺乏图像一致性。
2. 方法要点：基于FLUX.1 Kontext架构，采用全参数微调和像素空间一致性损失。
3. 实验或效果：在深度、法线和抠图任务中实现SOTA，推理速度提升。

## 📄 摘要（原文）

> Recent advances in diffusion transformers have shown remarkable generalization in visual synthesis, yet most dense perception methods still rely on text-to-image (T2I) generators designed for stochastic generation. We revisit this paradigm and show that image editing diffusion models are inherently image-to-image consistent, providing a more suitable foundation for dense perception task. We introduce Edit2Perceive, a unified diffusion framework that adapts editing models for depth, normal, and matting. Built upon the FLUX.1 Kontext architecture, our approach employs full-parameter fine-tuning and a pixel-space consistency loss to enforce structure-preserving refinement across intermediate denoising states. Moreover, our single-step deterministic inference yields up to faster runtime while training on relatively small datasets. Extensive experiments demonstrate comprehensive state-of-the-art results across all three tasks, revealing the strong potential of editing-oriented diffusion transformers for geometry-aware perception.

