---
layout: default
title: Video Generation Models Are Good Latent Reward Models
---

# Video Generation Models Are Good Latent Reward Models

**arXiv**: [2511.21541v1](https://arxiv.org/abs/2511.21541) | [PDF](https://arxiv.org/pdf/2511.21541.pdf)

**作者**: Xiaoyue Mi, Wenqing Yu, Jiesong Lian, Shibo Jie, Ruizhe Zhong, Zijun Liu, Guozhen Zhang, Zixiang Zhou, Zhiyong Xu, Yuan Zhou, Qinglin Lu, Fan Tang

---

## 💡 一句话要点

**提出PRFL框架以在潜在空间进行视频生成偏好优化，提升效率与对齐性**

**关键词**: `视频生成` `奖励建模` `潜在空间优化` `偏好学习` `效率提升`

## 📋 核心要点

1. 核心问题：视频生成中像素空间奖励模型内存开销大、训练慢，且缺乏早期动态监督
2. 方法要点：利用预训练视频生成模型在噪声潜在空间建模奖励，实现全链梯度反向传播
3. 实验或效果：PRFL显著提升人类偏好对齐，大幅减少内存消耗和训练时间

## 📄 摘要（原文）

> Reward feedback learning (ReFL) has proven effective for aligning image generation with human preferences. However, its extension to video generation faces significant challenges. Existing video reward models rely on vision-language models designed for pixel-space inputs, confining ReFL optimization to near-complete denoising steps after computationally expensive VAE decoding. This pixel-space approach incurs substantial memory overhead and increased training time, and its late-stage optimization lacks early-stage supervision, refining only visual quality rather than fundamental motion dynamics and structural coherence. In this work, we show that pre-trained video generation models are naturally suited for reward modeling in the noisy latent space, as they are explicitly designed to process noisy latent representations at arbitrary timesteps and inherently preserve temporal information through their sequential modeling capabilities. Accordingly, we propose Process Reward Feedback Learning~(PRFL), a framework that conducts preference optimization entirely in latent space, enabling efficient gradient backpropagation throughout the full denoising chain without VAE decoding. Extensive experiments demonstrate that PRFL significantly improves alignment with human preferences, while achieving substantial reductions in memory consumption and training time compared to RGB ReFL.

