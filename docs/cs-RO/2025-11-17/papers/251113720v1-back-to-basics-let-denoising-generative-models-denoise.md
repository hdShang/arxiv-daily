---
layout: default
title: Back to Basics: Let Denoising Generative Models Denoise
---

# Back to Basics: Let Denoising Generative Models Denoise

**arXiv**: [2511.13720v1](https://arxiv.org/abs/2511.13720) | [PDF](https://arxiv.org/pdf/2511.13720.pdf)

**作者**: Tianhong Li, Kaiming He

---

## 💡 一句话要点

**提出JiT方法，通过直接预测干净图像解决扩散模型在高维空间失效问题**

**关键词**: `扩散模型` `流形假设` `Transformer生成` `图像去噪` `高维数据生成`

## 📋 核心要点

1. 核心问题：扩散模型预测噪声而非干净图像，违背流形假设，导致高维生成失败
2. 方法要点：使用大块Transformer直接预测干净数据，无需分词器、预训练或额外损失
3. 实验或效果：在ImageNet 256和512分辨率上，JiT取得竞争性结果，验证有效性

## 📄 摘要（原文）

> Today's denoising diffusion models do not "denoise" in the classical sense, i.e., they do not directly predict clean images. Rather, the neural networks predict noise or a noised quantity. In this paper, we suggest that predicting clean data and predicting noised quantities are fundamentally different. According to the manifold assumption, natural data should lie on a low-dimensional manifold, whereas noised quantities do not. With this assumption, we advocate for models that directly predict clean data, which allows apparently under-capacity networks to operate effectively in very high-dimensional spaces. We show that simple, large-patch Transformers on pixels can be strong generative models: using no tokenizer, no pre-training, and no extra loss. Our approach is conceptually nothing more than "$\textbf{Just image Transformers}$", or $\textbf{JiT}$, as we call it. We report competitive results using JiT with large patch sizes of 16 and 32 on ImageNet at resolutions of 256 and 512, where predicting high-dimensional noised quantities can fail catastrophically. With our networks mapping back to the basics of the manifold, our research goes back to basics and pursues a self-contained paradigm for Transformer-based diffusion on raw natural data.

