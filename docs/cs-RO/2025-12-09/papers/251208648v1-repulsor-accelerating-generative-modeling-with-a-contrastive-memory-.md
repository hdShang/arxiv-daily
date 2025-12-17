---
layout: default
title: Repulsor: Accelerating Generative Modeling with a Contrastive Memory Bank
---

# Repulsor: Accelerating Generative Modeling with a Contrastive Memory Bank

**arXiv**: [2512.08648v1](https://arxiv.org/abs/2512.08648) | [PDF](https://arxiv.org/pdf/2512.08648.pdf)

**作者**: Shaofeng Zhang, Xuanqi Chen, Ning Liao, Haoxiang Zhao, Xiaoxing Wang, Haoru Tan, Sitong Wu, Xiaosong Jia, Qi Fan, Junchi Yan

---

## 💡 一句话要点

**提出Repulsor框架，通过对比记忆库加速生成模型训练，无需外部编码器。**

**关键词**: `生成模型` `对比学习` `记忆库机制` `训练加速` `图像合成`

## 📋 核心要点

1. 核心问题：去噪生成模型训练成本高，依赖外部编码器引入开销和领域偏移。
2. 方法要点：集成动态更新的记忆库机制，解耦负样本数与批次大小，使用低维投影头减少开销。
3. 实验或效果：在ImageNet-256上，400k步内达到FID 2.40，收敛更快，推理无额外成本。

## 📄 摘要（原文）

> The dominance of denoising generative models (e.g., diffusion, flow-matching) in visual synthesis is tempered by their substantial training costs and inefficiencies in representation learning. While injecting discriminative representations via auxiliary alignment has proven effective, this approach still faces key limitations: the reliance on external, pre-trained encoders introduces overhead and domain shift. A dispersed-based strategy that encourages strong separation among in-batch latent representations alleviates this specific dependency. To assess the effect of the number of negative samples in generative modeling, we propose {\mname}, a plug-and-play training framework that requires no external encoders. Our method integrates a memory bank mechanism that maintains a large, dynamically updated queue of negative samples across training iterations. This decouples the number of negatives from the mini-batch size, providing abundant and high-quality negatives for a contrastive objective without a multiplicative increase in computational cost. A low-dimensional projection head is used to further minimize memory and bandwidth overhead. {\mname} offers three principal advantages: (1) it is self-contained, eliminating dependency on pretrained vision foundation models and their associated forward-pass overhead; (2) it introduces no additional parameters or computational cost during inference; and (3) it enables substantially faster convergence, achieving superior generative quality more efficiently. On ImageNet-256, {\mname} achieves a state-of-the-art FID of \textbf{2.40} within 400k steps, significantly outperforming comparable methods.

