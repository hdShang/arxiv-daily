---
layout: default
title: Pruning Overparameterized Multi-Task Networks for Degraded Web Image Restoration
---

# Pruning Overparameterized Multi-Task Networks for Degraded Web Image Restoration

**arXiv**: [2510.14463v1](https://arxiv.org/abs/2510.14463) | [PDF](https://arxiv.org/pdf/2510.14463.pdf)

**作者**: Thomas Katraouras, Dimitrios Rafailidis

---

## 💡 一句话要点

**提出MIR-L模型以压缩多任务图像恢复网络，提升计算效率。**

**关键词**: `图像恢复` `多任务学习` `模型剪枝` `计算效率` `迭代优化`

## 📋 核心要点

1. 多任务图像恢复模型参数过多，导致计算效率低下。
2. 采用迭代剪枝策略，移除低幅值权重并重置剩余权重。
3. 实验显示，保留10%参数仍保持高性能，适用于去雨、去雾和去噪任务。

## 📄 摘要（原文）

> Image quality is a critical factor in delivering visually appealing content
> on web platforms. However, images often suffer from degradation due to lossy
> operations applied by online social networks (OSNs), negatively affecting user
> experience. Image restoration is the process of recovering a clean high-quality
> image from a given degraded input. Recently, multi-task (all-in-one) image
> restoration models have gained significant attention, due to their ability to
> simultaneously handle different types of image degradations. However, these
> models often come with an excessively high number of trainable parameters,
> making them computationally inefficient. In this paper, we propose a strategy
> for compressing multi-task image restoration models. We aim to discover highly
> sparse subnetworks within overparameterized deep models that can match or even
> surpass the performance of their dense counterparts. The proposed model, namely
> MIR-L, utilizes an iterative pruning strategy that removes low-magnitude
> weights across multiple rounds, while resetting the remaining weights to their
> original initialization. This iterative process is important for the multi-task
> image restoration model's optimization, effectively uncovering "winning
> tickets" that maintain or exceed state-of-the-art performance at high sparsity
> levels. Experimental evaluation on benchmark datasets for the deraining,
> dehazing, and denoising tasks shows that MIR-L retains only 10% of the
> trainable parameters while maintaining high image restoration performance. Our
> code, datasets and pre-trained models are made publicly available at
> https://github.com/Thomkat/MIR-L.

