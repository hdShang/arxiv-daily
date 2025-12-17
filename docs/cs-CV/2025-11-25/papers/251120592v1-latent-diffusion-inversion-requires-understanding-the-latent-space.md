---
layout: default
title: Latent Diffusion Inversion Requires Understanding the Latent Space
---

# Latent Diffusion Inversion Requires Understanding the Latent Space

**arXiv**: [2511.20592v1](https://arxiv.org/abs/2511.20592) | [PDF](https://arxiv.org/pdf/2511.20592.pdf)

**作者**: Mingxing Rao, Bowen Qu, Daniel Moyer

---

## 💡 一句话要点

**提出基于潜在维度排序的方法以改进潜在扩散模型的成员推理攻击性能**

**关键词**: `潜在扩散模型` `模型反转` `成员推理攻击` `潜在空间分析` `解码器回拉度量`

## 📋 核心要点

1. 核心问题：潜在扩散模型在潜在空间中存在非均匀记忆化，影响模型反转攻击效果
2. 方法要点：通过解码器回拉度量排序潜在维度，识别高记忆化维度
3. 实验或效果：在多个数据集上，移除低记忆化维度显著提升AUROC和TPR@1%FPR

## 📄 摘要（原文）

> The recovery of training data from generative models (``model inversion'') has been extensively studied for diffusion models in the data domain. The encoder/decoder pair and corresponding latent codes have largely been ignored by inversion techniques applied to latent space generative models, e.g., Latent Diffusion models (LDMs). In this work we describe two key findings: (1) The diffusion model exhibits non-uniform memorization across latent codes, tending to overfit samples located in high-distortion regions of the decoder pullback metric. (2) Even within a single latent code, different dimensions contribute unequally to memorization. We introduce a principled method to rank latent dimensions by their per-dimensional contribution to the decoder pullback metric, identifying those most responsible for memorization. Empirically, removing less-memorizing dimensions when computing attack statistics for score-based membership inference attacker significantly improves performance, with average AUROC gains of 2.7\% and substantial increases in TPR@1\%FPR (6.42\%) across diverse datasets including CIFAR-10, CelebA, ImageNet-1K, Pokémon, MS-COCO, and Flickr. This indicates stronger confidence in identifying members under extremely low false-positive tolerance. Our results highlight the overlooked influence of the auto-encoder geometry on LDM memorization and provide a new perspective for analyzing privacy risks in diffusion-based generative models.

