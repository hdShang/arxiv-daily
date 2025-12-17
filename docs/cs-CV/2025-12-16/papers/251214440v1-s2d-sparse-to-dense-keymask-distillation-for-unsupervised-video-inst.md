---
layout: default
title: S2D: Sparse-To-Dense Keymask Distillation for Unsupervised Video Instance Segmentation
---

# S2D: Sparse-To-Dense Keymask Distillation for Unsupervised Video Instance Segmentation

**arXiv**: [2512.14440v1](https://arxiv.org/abs/2512.14440) | [PDF](https://arxiv.org/pdf/2512.14440.pdf)

**作者**: Leon Sick, Lukas Hoyer, Dominik Engel, Pedro Hermosilla, Timo Ropinski

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project Page with Code/Models/Demo: https://leonsick.github.io/s2d/

---

## 💡 一句话要点

**提出稀疏到稠密关键掩码蒸馏方法，以解决无监督视频实例分割中合成数据运动建模不准确的问题。**

**关键词**: `无监督学习` `视频实例分割` `稀疏到稠密蒸馏` `时间一致性` `深度运动先验` `关键掩码筛选` `隐式掩码传播` `真实视频数据`

## 📋 核心要点

1. 核心问题：现有方法依赖合成视频数据，无法准确建模真实视频中的复杂运动，如透视变化和部分运动。
2. 方法要点：利用深度运动先验识别高质量关键掩码，通过稀疏到稠密蒸馏和时间丢弃损失训练模型实现隐式传播。
3. 实验或效果：在多个基准测试中超越当前最先进方法，显著提升无监督视频实例分割性能。

## 📝 摘要（中文）

近年来，无监督视频实例分割的最先进方法严重依赖于从以对象为中心的图像数据集（如ImageNet）生成的合成视频数据。然而，通过人工移动和缩放图像实例掩码来合成视频，无法准确建模视频中的真实运动，例如透视变化、单个或多个实例的部分运动或相机运动。为解决这一问题，我们提出了一种仅使用真实视频数据训练的无监督视频实例分割模型。我们从单个视频帧上的无监督实例分割掩码开始。但这些单帧分割存在时间噪声，且质量在视频中变化。因此，我们通过利用深度运动先验识别视频中的高质量关键掩码来建立时间一致性。稀疏关键掩码伪标注随后用于训练一个用于隐式掩码传播的分割模型，为此我们提出了一种稀疏到稠密蒸馏方法，辅以时间丢弃损失。在最终模型上对生成的稠密标签集进行训练后，我们的方法在各种基准测试中超越了当前最先进水平。

## 🔬 方法详解

整体框架基于真实视频数据，从单帧无监督分割掩码出发，通过深度运动先验筛选高质量关键掩码建立时间一致性。关键技术创新点包括稀疏到稠密蒸馏方法，将稀疏关键掩码作为伪标注训练分割模型进行隐式掩码传播，并引入时间丢弃损失以优化训练过程。与现有方法的主要区别在于完全避免合成数据，直接利用真实视频中的运动信息，从而更准确地建模动态场景。

## 📊 实验亮点

在多个无监督视频实例分割基准测试中，该方法显著超越现有最先进模型，证明了仅使用真实视频数据训练的有效性，并展示了在复杂运动场景下的优越性能。

## 🎯 应用场景

该研究可应用于视频监控、自动驾驶、机器人视觉和视频编辑等领域，通过无监督方式实现视频中实例的精确分割和跟踪，降低对标注数据的依赖，提升实际场景中的鲁棒性和效率。

## 📄 摘要（原文）

> In recent years, the state-of-the-art in unsupervised video instance segmentation has heavily relied on synthetic video data, generated from object-centric image datasets such as ImageNet. However, video synthesis by artificially shifting and scaling image instance masks fails to accurately model realistic motion in videos, such as perspective changes, movement by parts of one or multiple instances, or camera motion. To tackle this issue, we propose an unsupervised video instance segmentation model trained exclusively on real video data. We start from unsupervised instance segmentation masks on individual video frames. However, these single-frame segmentations exhibit temporal noise and their quality varies through the video. Therefore, we establish temporal coherence by identifying high-quality keymasks in the video by leveraging deep motion priors. The sparse keymask pseudo-annotations are then used to train a segmentation model for implicit mask propagation, for which we propose a Sparse-To-Dense Distillation approach aided by a Temporal DropLoss. After training the final model on the resulting dense labelset, our approach outperforms the current state-of-the-art across various benchmarks.

