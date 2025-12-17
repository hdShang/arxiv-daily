---
layout: default
title: History-Augmented Contrastive Meta-Learning for Unsupervised Blind Super-Resolution of Planetary Remote Sensing Images
---

# History-Augmented Contrastive Meta-Learning for Unsupervised Blind Super-Resolution of Planetary Remote Sensing Images

**arXiv**: [2511.20045v1](https://arxiv.org/abs/2511.20045) | [PDF](https://arxiv.org/pdf/2511.20045.pdf)

**作者**: Huijia Zhao, Jie Lu, Yunqing Jiang, Xiao-Ping Lu, Kaichang Di

---

## 💡 一句话要点

**提出历史增强对比元学习框架，用于行星遥感图像的无监督盲超分辨率**

**关键词**: `盲超分辨率` `对比学习` `元学习` `行星遥感` `无监督学习` `图像退化`

## 📋 核心要点

1. 行星遥感图像受未知退化影响，缺乏真实图像，限制监督盲超分辨率性能。
2. 方法包括对比核采样和历史增强对比学习，避免高斯偏差并优化收敛。
3. 实验在Ceres-50数据集上验证，与先进无监督方法相比性能竞争。

## 📄 摘要（原文）

> Planetary remote sensing images are affected by diverse and unknown degradations caused by imaging environments and hardware constraints. These factors limit image quality and hinder supervised blind super-resolution due to the lack of ground-truth images. This work presents History-Augmented Contrastive Blind Super-Resolution (HACBSR), an unsupervised framework for blind super-resolution that operates without ground-truth images and external kernel priors. HACBSR comprises two components: (1) a contrastive kernel sampling mechanism with kernel similarity control to mitigate distribution bias from Gaussian sampling, and (2) a history-augmented contrastive learning that uses historical models to generate negative samples to enable less greedy optimization and to induce strong convexity without ground-truth. A convergence analysis of the history-augmented contrastive learning is given in the Appendix. To support evaluation in planetary applications, we introduce Ceres-50, a dataset with diverse geological features simulated degradation patterns. Experiments show that HACBSR achieves competitive performance compared with state-of-the-art unsupervised methods across multiple upscaling factors. The code is available at https://github.com/2333repeat/HACBSR, and the dataset is available at https://github.com/2333repeat/Ceres-50.

