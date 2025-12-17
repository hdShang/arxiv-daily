---
layout: default
title: GUSL-Dehaze: A Green U-Shaped Learning Approach to Image Dehazing
---

# GUSL-Dehaze: A Green U-Shaped Learning Approach to Image Dehazing

**arXiv**: [2510.20266v1](https://arxiv.org/abs/2510.20266) | [PDF](https://arxiv.org/pdf/2510.20266.pdf)

**作者**: Mahtab Movaheddrad, Laurence Palmer, C. -C. Jay Kuo

---

## 💡 一句话要点

**提出GUSL-Dehaze绿色U形学习方法，用于图像去雾以降低计算成本**

**关键词**: `图像去雾` `绿色学习` `U形架构` `特征工程` `轻量模型` `可解释学习`

## 📋 核心要点

1. 图像去雾任务旨在从单张有雾图像恢复清晰图像，传统方法依赖统计先验和物理模型
2. 方法结合物理模型与绿色学习框架，采用U形架构进行无监督特征提取和特征工程
3. 实验显示模型参数显著减少，性能与先进深度学习模型相当，保持数学可解释性

## 📄 摘要（原文）

> Image dehazing is a restoration task that aims to recover a clear image from
> a single hazy input. Traditional approaches rely on statistical priors and the
> physics-based atmospheric scattering model to reconstruct the haze-free image.
> While recent state-of-the-art methods are predominantly based on deep learning
> architectures, these models often involve high computational costs and large
> parameter sizes, making them unsuitable for resource-constrained devices. In
> this work, we propose GUSL-Dehaze, a Green U-Shaped Learning approach to image
> dehazing. Our method integrates a physics-based model with a green learning
> (GL) framework, offering a lightweight, transparent alternative to conventional
> deep learning techniques. Unlike neural network-based solutions, GUSL-Dehaze
> completely avoids deep learning. Instead, we begin with an initial dehazing
> step using a modified Dark Channel Prior (DCP), which is followed by a green
> learning pipeline implemented through a U-shaped architecture. This
> architecture employs unsupervised representation learning for effective feature
> extraction, together with feature-engineering techniques such as the Relevant
> Feature Test (RFT) and the Least-Squares Normal Transform (LNT) to maintain a
> compact model size. Finally, the dehazed image is obtained via a transparent
> supervised learning strategy. GUSL-Dehaze significantly reduces parameter count
> while ensuring mathematical interpretability and achieving performance on par
> with state-of-the-art deep learning models.

