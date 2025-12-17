---
layout: default
title: APGNet: Adaptive Prior-Guided for Underwater Camouflaged Object Detection
---

# APGNet: Adaptive Prior-Guided for Underwater Camouflaged Object Detection

**arXiv**: [2510.12056v1](https://arxiv.org/abs/2510.12056) | [PDF](https://arxiv.org/pdf/2510.12056.pdf)

**作者**: Xinxin Huang, Han Sun, Junmin Cai, Ningzhong Liu, Huiyu Zhou

---

## 💡 一句话要点

**提出APGNet自适应先验引导网络以解决水下伪装物体检测问题**

**关键词**: `水下伪装物体检测` `自适应先验引导` `Siamese架构` `多尺度特征提取` `图像增强`

## 📋 核心要点

1. 核心问题：水下图像退化与海洋生物伪装导致检测困难
2. 方法要点：集成Siamese架构与先验引导机制，增强特征鲁棒性
3. 实验或效果：在MAS数据集上优于15种先进方法，验证有效性

## 📄 摘要（原文）

> Detecting camouflaged objects in underwater environments is crucial for
> marine ecological research and resource exploration. However, existing methods
> face two key challenges: underwater image degradation, including low contrast
> and color distortion, and the natural camouflage of marine organisms.
> Traditional image enhancement techniques struggle to restore critical features
> in degraded images, while camouflaged object detection (COD) methods developed
> for terrestrial scenes often fail to adapt to underwater environments due to
> the lack of consideration for underwater optical characteristics.
>   To address these issues, we propose APGNet, an Adaptive Prior-Guided Network,
> which integrates a Siamese architecture with a novel prior-guided mechanism to
> enhance robustness and detection accuracy. First, we employ the Multi-Scale
> Retinex with Color Restoration (MSRCR) algorithm for data augmentation,
> generating illumination-invariant images to mitigate degradation effects.
> Second, we design an Extended Receptive Field (ERF) module combined with a
> Multi-Scale Progressive Decoder (MPD) to capture multi-scale contextual
> information and refine feature representations. Furthermore, we propose an
> adaptive prior-guided mechanism that hierarchically fuses position and boundary
> priors by embedding spatial attention in high-level features for coarse
> localization and using deformable convolution to refine contours in low-level
> features.
>   Extensive experimental results on two public MAS datasets demonstrate that
> our proposed method APGNet outperforms 15 state-of-art methods under widely
> used evaluation metrics.

