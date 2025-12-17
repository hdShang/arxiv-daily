---
layout: default
title: Content Adaptive based Motion Alignment Framework for Learned Video Compression
---

# Content Adaptive based Motion Alignment Framework for Learned Video Compression

**arXiv**: [2512.12936v1](https://arxiv.org/abs/2512.12936) | [PDF](https://arxiv.org/pdf/2512.12936.pdf)

**作者**: Tiange Zhang, Xiandong Meng, Siwei Ma

---

## 💡 一句话要点

**提出内容自适应运动对齐框架以提升端到端视频压缩性能**

**关键词**: `端到端视频压缩` `运动对齐` `内容自适应` `可变形扭曲` `多参考策略` `免训练模块`

## 📋 核心要点

1. 核心问题：端到端视频压缩框架缺乏内容特定适应，导致压缩性能次优。
2. 方法要点：引入两阶段流引导可变形扭曲机制、多参考质量感知策略和免训练下采样模块。
3. 实验或效果：在标准测试集上，CAMA框架相比基线模型DCVC-TCM节省24.95% BD-rate（PSNR）。

## 📄 摘要（原文）

> Recent advances in end-to-end video compression have shown promising results owing to their unified end-to-end learning optimization. However, such generalized frameworks often lack content-specific adaptation, leading to suboptimal compression performance. To address this, this paper proposes a content adaptive based motion alignment framework that improves performance by adapting encoding strategies to diverse content characteristics. Specifically, we first introduce a two-stage flow-guided deformable warping mechanism that refines motion compensation with coarse-to-fine offset prediction and mask modulation, enabling precise feature alignment. Second, we propose a multi-reference quality aware strategy that adjusts distortion weights based on reference quality, and applies it to hierarchical training to reduce error propagation. Third, we integrate a training-free module that downsamples frames by motion magnitude and resolution to obtain smooth motion estimation. Experimental results on standard test datasets demonstrate that our framework CAMA achieves significant improvements over state-of-the-art Neural Video Compression models, achieving a 24.95% BD-rate (PSNR) savings over our baseline model DCVC-TCM, while also outperforming reproduced DCVC-DC and traditional codec HM-16.25.

