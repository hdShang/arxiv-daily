---
layout: default
title: ARGenSeg: Image Segmentation with Autoregressive Image Generation Model
---

# ARGenSeg: Image Segmentation with Autoregressive Image Generation Model

**arXiv**: [2510.20803v1](https://arxiv.org/abs/2510.20803) | [PDF](https://arxiv.org/pdf/2510.20803.pdf)

**作者**: Xiaolong Wang, Lixiang Ru, Ziyuan Huang, Kaixiang Ji, Dandan Zheng, Jingdong Chen, Jun Zhou

---

## 💡 一句话要点

**提出ARGenSeg，基于自回归图像生成模型实现图像分割，提升细粒度视觉理解与推理速度。**

**关键词**: `图像分割` `自回归生成` `多模态大语言模型` `VQ-VAE` `推理加速` `像素级感知`

## 📋 核心要点

1. 核心问题：现有MLLM分割方法依赖离散表示或专用头，难以捕捉细粒度视觉细节。
2. 方法要点：利用MLLM输出视觉令牌，通过VQ-VAE解码为图像，生成密集掩码。
3. 实验或效果：在多个数据集上超越SOTA，显著提升推理速度，保持强理解能力。

## 📄 摘要（原文）

> We propose a novel AutoRegressive Generation-based paradigm for image
> Segmentation (ARGenSeg), achieving multimodal understanding and pixel-level
> perception within a unified framework. Prior works integrating image
> segmentation into multimodal large language models (MLLMs) typically employ
> either boundary points representation or dedicated segmentation heads. These
> methods rely on discrete representations or semantic prompts fed into
> task-specific decoders, which limits the ability of the MLLM to capture
> fine-grained visual details. To address these challenges, we introduce a
> segmentation framework for MLLM based on image generation, which naturally
> produces dense masks for target objects. We leverage MLLM to output visual
> tokens and detokenize them into images using an universal VQ-VAE, making the
> segmentation fully dependent on the pixel-level understanding of the MLLM. To
> reduce inference latency, we employ a next-scale-prediction strategy to
> generate required visual tokens in parallel. Extensive experiments demonstrate
> that our method surpasses prior state-of-the-art approaches on multiple
> segmentation datasets with a remarkable boost in inference speed, while
> maintaining strong understanding capabilities.

