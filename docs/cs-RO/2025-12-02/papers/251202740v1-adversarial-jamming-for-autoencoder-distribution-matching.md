---
layout: default
title: Adversarial Jamming for Autoencoder Distribution Matching
---

# Adversarial Jamming for Autoencoder Distribution Matching

**arXiv**: [2512.02740v1](https://arxiv.org/abs/2512.02740) | [PDF](https://arxiv.org/pdf/2512.02740.pdf)

**作者**: Waleed El-Geresy, Deniz Gündüz

---

## 💡 一句话要点

**提出对抗性无线干扰以正则化自编码器潜在空间，匹配对角高斯分布。**

**关键词**: `对抗性干扰` `自编码器` `分布匹配` `潜在空间正则化` `高斯分布` `无线通信`

## 📋 核心要点

1. 核心问题：自编码器潜在空间分布匹配，需正则化以接近对角高斯分布。
2. 方法要点：利用对抗性无线干扰作为辅助目标，通过最小化均方误差失真，鼓励潜在后验匹配对角高斯分布。
3. 实验或效果：实现与标准变分自编码器和Wasserstein自编码器相当的分布匹配性能，并可推广至其他潜在分布。

## 📄 摘要（原文）

> We propose the use of adversarial wireless jamming to regularise the latent space of an autoencoder to match a diagonal Gaussian distribution. We consider the minimisation of a mean squared error distortion, where a jammer attempts to disrupt the recovery of a Gaussian source encoded and transmitted over the adversarial channel. A straightforward consequence of existing theoretical results is the fact that the saddle point of a minimax game - involving such an encoder, its corresponding decoder, and an adversarial jammer - consists of diagonal Gaussian noise output by the jammer. We use this result as inspiration for a novel approach to distribution matching in the latent space, utilising jamming as an auxiliary objective to encourage the aggregated latent posterior to match a diagonal Gaussian distribution. Using this new technique, we achieve distribution matching comparable to standard variational autoencoders and to Wasserstein autoencoders. This approach can also be generalised to other latent distributions.

