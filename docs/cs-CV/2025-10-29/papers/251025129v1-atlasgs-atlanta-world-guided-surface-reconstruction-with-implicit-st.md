---
layout: default
title: AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians
---

# AtlasGS: Atlanta-world Guided Surface Reconstruction with Implicit Structured Gaussians

**arXiv**: [2510.25129v1](https://arxiv.org/abs/2510.25129) | [PDF](https://arxiv.org/pdf/2510.25129.pdf)

**作者**: Xiyu Zhang, Chong Bao, Yipeng Chen, Hongjia Zhai, Yitong Dong, Hujun Bao, Zhaopeng Cui, Guofeng Zhang

---

## 💡 一句话要点

**提出Atlanta-world引导的隐式结构化高斯泼溅，实现平滑室内和城市场景重建**

**关键词**: `三维重建` `高斯泼溅` `Atlanta-world模型` `隐式表面表示` `室内场景` `城市场景`

## 📋 核心要点

1. 现有几何先验缺乏全局一致性，高斯泼溅和隐式SDF存在不连续或效率低问题
2. 结合Atlanta-world模型和隐式结构化高斯表示，确保低纹理区域准确重建
3. 实验显示在室内和城市场景中优于现有方法，重建质量高且效率佳

## 📄 摘要（原文）

> 3D reconstruction of indoor and urban environments is a prominent research
> topic with various downstream applications. However, existing geometric priors
> for addressing low-texture regions in indoor and urban settings often lack
> global consistency. Moreover, Gaussian Splatting and implicit SDF fields often
> suffer from discontinuities or exhibit computational inefficiencies, resulting
> in a loss of detail. To address these issues, we propose an Atlanta-world
> guided implicit-structured Gaussian Splatting that achieves smooth indoor and
> urban scene reconstruction while preserving high-frequency details and
> rendering efficiency. By leveraging the Atlanta-world model, we ensure the
> accurate surface reconstruction for low-texture regions, while the proposed
> novel implicit-structured GS representations provide smoothness without
> sacrificing efficiency and high-frequency details. Specifically, we propose a
> semantic GS representation to predict the probability of all semantic regions
> and deploy a structure plane regularization with learnable plane indicators for
> global accurate surface reconstruction. Extensive experiments demonstrate that
> our method outperforms state-of-the-art approaches in both indoor and urban
> scenes, delivering superior surface reconstruction quality.

