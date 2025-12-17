---
layout: default
title: DiffRegCD: Integrated Registration and Change Detection with Diffusion Features
---

# DiffRegCD: Integrated Registration and Change Detection with Diffusion Features

**arXiv**: [2511.07935v1](https://arxiv.org/abs/2511.07935) | [PDF](https://arxiv.org/pdf/2511.07935.pdf)

**作者**: Seyedehnanita Madani, Rama Chellappa, Vishal M. Patel

---

## 💡 一句话要点

**提出DiffRegCD框架，集成密集配准与变化检测，解决大位移图像变化检测问题。**

**关键词**: `变化检测` `图像配准` `扩散模型` `高斯平滑分类` `遥感图像分析` `集成学习`

## 📋 核心要点

1. 核心问题：真实图像存在视差和视角偏移，导致配准不准，影响变化检测。
2. 方法要点：将配准建模为高斯平滑分类任务，利用预训练扩散模型特征提升鲁棒性。
3. 实验效果：在多个数据集上超越基线，对广泛时空和几何变化保持可靠。

## 📄 摘要（原文）

> Change detection (CD) is fundamental to computer vision and remote sensing, supporting applications in environmental monitoring, disaster response, and urban development. Most CD models assume co-registered inputs, yet real-world imagery often exhibits parallax, viewpoint shifts, and long temporal gaps that cause severe misalignment. Traditional two stage methods that first register and then detect, as well as recent joint frameworks (e.g., BiFA, ChangeRD), still struggle under large displacements, relying on regression only flow, global homographies, or synthetic perturbations. We present DiffRegCD, an integrated framework that unifies dense registration and change detection in a single model. DiffRegCD reformulates correspondence estimation as a Gaussian smoothed classification task, achieving sub-pixel accuracy and stable training. It leverages frozen multi-scale features from a pretrained denoising diffusion model, ensuring robustness to illumination and viewpoint variation. Supervision is provided through controlled affine perturbations applied to standard CD datasets, yielding paired ground truth for both flow and change detection without pseudo labels. Extensive experiments on aerial (LEVIR-CD, DSIFN-CD, WHU-CD, SYSU-CD) and ground level (VL-CMU-CD) datasets show that DiffRegCD consistently surpasses recent baselines and remains reliable under wide temporal and geometric variation, establishing diffusion features and classification based correspondence as a strong foundation for unified change detection.

