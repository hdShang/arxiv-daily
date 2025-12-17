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

**提出S2D稀疏到稠密关键掩码蒸馏方法，利用真实视频数据解决无监督视频实例分割中的运动建模不足问题。**

🎯 **匹配领域**: **动作生成**

**关键词**: `无监督视频实例分割` `稀疏到稠密蒸馏` `深度运动先验` `关键掩码识别` `时间一致性` `真实视频数据` `隐式掩码传播` `时间DropLoss`

## 📋 核心要点

1. 现有方法依赖合成视频数据，无法准确建模真实运动如视角变化和部分运动，导致分割质量受限。
2. 提出S2D方法，利用深度运动先验识别高质量关键掩码，并通过稀疏到稠密蒸馏训练模型实现隐式掩码传播。
3. 在多个基准测试中，该方法超越了当前最先进水平，显著提升了无监督视频实例分割的性能。

## 📝 摘要（中文）

近年来，无监督视频实例分割的最先进方法严重依赖从ImageNet等以对象为中心的图像数据集生成的合成视频数据。然而，通过人工平移和缩放图像实例掩码来合成视频的方法无法准确建模视频中的真实运动，例如视角变化、单个或多个实例的部分运动或相机运动。为解决这一问题，我们提出了一种仅使用真实视频数据训练的无监督视频实例分割模型。我们从单个视频帧上的无监督实例分割掩码开始。然而，这些单帧分割存在时间噪声，且其质量在整个视频中变化。因此，我们通过利用深度运动先验识别视频中的高质量关键掩码来建立时间一致性。稀疏的关键掩码伪标注随后用于训练一个用于隐式掩码传播的分割模型，为此我们提出了一种由时间DropLoss辅助的稀疏到稠密蒸馏方法。在最终模型上对生成的稠密标签集进行训练后，我们的方法在各种基准测试中超越了当前的最先进水平。

## 🔬 方法详解

论文提出S2D框架，整体基于真实视频数据训练无监督视频实例分割模型。首先从单帧无监督分割掩码出发，利用深度运动先验识别高质量关键掩码以建立时间一致性。关键技术创新包括稀疏到稠密蒸馏方法，将稀疏关键掩码伪标注用于训练分割模型进行隐式掩码传播，并引入时间DropLoss辅助训练。与现有方法的主要区别在于完全依赖真实视频数据而非合成数据，通过运动先验和蒸馏策略有效处理时间噪声和掩码质量变化，避免了合成数据中运动建模不准确的问题。

## 📊 实验亮点

在多个基准测试中，S2D方法显著超越了当前最先进的无监督视频实例分割模型，证明了仅使用真实视频数据训练的有效性，并通过稀疏到稠密蒸馏和时间DropLoss提升了分割性能。

## 🎯 应用场景

该研究可应用于视频监控、自动驾驶、机器人视觉和视频编辑等领域，通过无监督学习实现高质量的视频实例分割，减少对标注数据的依赖，提升在真实世界视频中的分割准确性和鲁棒性。

## 📄 摘要（原文）

> In recent years, the state-of-the-art in unsupervised video instance segmentation has heavily relied on synthetic video data, generated from object-centric image datasets such as ImageNet. However, video synthesis by artificially shifting and scaling image instance masks fails to accurately model realistic motion in videos, such as perspective changes, movement by parts of one or multiple instances, or camera motion. To tackle this issue, we propose an unsupervised video instance segmentation model trained exclusively on real video data. We start from unsupervised instance segmentation masks on individual video frames. However, these single-frame segmentations exhibit temporal noise and their quality varies through the video. Therefore, we establish temporal coherence by identifying high-quality keymasks in the video by leveraging deep motion priors. The sparse keymask pseudo-annotations are then used to train a segmentation model for implicit mask propagation, for which we propose a Sparse-To-Dense Distillation approach aided by a Temporal DropLoss. After training the final model on the resulting dense labelset, our approach outperforms the current state-of-the-art across various benchmarks.

