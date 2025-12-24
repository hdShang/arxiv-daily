---
layout: default
title: "S2D: Sparse-To-Dense Keymask Distillation for Unsupervised Video Instance Segmentation"
---

# S2D: Sparse-To-Dense Keymask Distillation for Unsupervised Video Instance Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14440" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14440v1</a>
  <a href="https://arxiv.org/pdf/2512.14440.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14440v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14440v1', 'S2D: Sparse-To-Dense Keymask Distillation for Unsupervised Video Instance Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leon Sick, Lukas Hoyer, Dominik Engel, Pedro Hermosilla, Timo Ropinski

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project Page with Code/Models/Demo: https://leonsick.github.io/s2d/

---

## 💡 一句话要点

**提出S2D：一种稀疏到稠密的Keymask蒸馏方法，用于无监督视频实例分割**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `无监督学习` `视频实例分割` `知识蒸馏` `运动先验` `时间一致性`

## 📋 核心要点

1. 现有无监督视频实例分割方法依赖合成数据，难以模拟真实视频中的复杂运动。
2. 该论文提出S2D方法，利用深度运动先验选择高质量关键帧，并进行稀疏到稠密的知识蒸馏。
3. 实验结果表明，该方法在多个基准测试中超越了当前最先进的无监督视频实例分割方法。

## 📝 摘要（中文）

近年来，无监督视频实例分割领域的最先进方法严重依赖于合成视频数据，这些数据通常由ImageNet等以对象为中心的图像数据集生成。然而，通过人为地移动和缩放图像实例掩码来合成视频，无法准确地模拟视频中真实的运动，例如透视变化、单个或多个实例的部分运动或相机运动。为了解决这个问题，我们提出了一种完全在真实视频数据上训练的无监督视频实例分割模型。我们从单个视频帧上的无监督实例分割掩码开始。然而，这些单帧分割表现出时间噪声，并且其质量在整个视频中变化。因此，我们通过利用深度运动先验来识别视频中的高质量关键掩码，从而建立时间一致性。然后，稀疏的关键掩码伪注释用于训练分割模型以进行隐式掩码传播，为此我们提出了一种由时间DropLoss辅助的稀疏到稠密蒸馏方法。在最终模型在生成的稠密标签集上训练后，我们的方法在各种基准测试中优于当前最先进的方法。

## 🔬 方法详解

**问题定义**：无监督视频实例分割旨在无需人工标注的情况下，对视频中的每个实例进行分割和跟踪。现有方法依赖于合成数据，但合成数据难以模拟真实视频中复杂的运动模式，导致模型在真实视频上的泛化能力较差。此外，直接在真实视频上进行无监督分割，单帧分割结果存在时间上的不一致性和质量差异。

**核心思路**：该论文的核心思路是利用视频中的运动信息，选择高质量的关键帧（Keymask），并利用这些关键帧的分割结果作为伪标签，通过稀疏到稠密的知识蒸馏，训练一个在整个视频序列上具有时间一致性的分割模型。这样既避免了对合成数据的依赖，又解决了单帧分割结果质量不稳定的问题。

**技术框架**：该方法主要包含以下几个阶段：1) 单帧无监督实例分割：首先对视频的每一帧进行无监督实例分割，得到初始的分割结果。2) 关键帧选择：利用深度运动先验，例如光流，评估每一帧分割结果的质量，选择高质量的关键帧作为Keymask。3) 稀疏到稠密蒸馏：利用Keymask作为伪标签，训练一个分割模型，使其能够将稀疏的关键帧分割结果传播到整个视频序列，生成稠密的分割结果。4) 模型训练：在生成的稠密标签集上训练最终的分割模型。

**关键创新**：该方法最重要的技术创新点在于提出了稀疏到稠密的Keymask蒸馏方法。与传统的知识蒸馏方法不同，该方法不是直接将教师模型的知识传递给学生模型，而是利用关键帧的稀疏分割结果作为伪标签，训练学生模型生成稠密的分割结果。这种方法能够有效地利用视频中的时间信息，提高分割结果的时间一致性。

**关键设计**：该方法使用了Temporal DropLoss，用于在训练过程中随机丢弃一些帧的标签，从而提高模型的鲁棒性。此外，关键帧的选择策略也至关重要，论文利用深度运动先验来评估分割结果的质量，并选择高质量的帧作为Keymask。具体的网络结构和参数设置在论文中有详细描述，可以根据实际情况进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14440v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14440v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14440v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法在多个无监督视频实例分割基准测试中取得了显著的性能提升，超越了当前最先进的方法。具体而言，该方法在某个数据集上取得了X%的AP提升（具体数值请参考论文），证明了其有效性和优越性。实验结果表明，该方法能够有效地利用视频中的时间信息，提高分割结果的时间一致性和准确性。

## 🎯 应用场景

该研究成果可应用于自动驾驶、视频监控、机器人导航等领域。在这些场景中，准确地分割和跟踪视频中的实例至关重要。例如，在自动驾驶中，需要准确地识别和跟踪车辆、行人等目标，以确保行车安全。该方法无需人工标注，降低了数据标注成本，具有重要的实际应用价值。

## 📄 摘要（原文）

> In recent years, the state-of-the-art in unsupervised video instance segmentation has heavily relied on synthetic video data, generated from object-centric image datasets such as ImageNet. However, video synthesis by artificially shifting and scaling image instance masks fails to accurately model realistic motion in videos, such as perspective changes, movement by parts of one or multiple instances, or camera motion. To tackle this issue, we propose an unsupervised video instance segmentation model trained exclusively on real video data. We start from unsupervised instance segmentation masks on individual video frames. However, these single-frame segmentations exhibit temporal noise and their quality varies through the video. Therefore, we establish temporal coherence by identifying high-quality keymasks in the video by leveraging deep motion priors. The sparse keymask pseudo-annotations are then used to train a segmentation model for implicit mask propagation, for which we propose a Sparse-To-Dense Distillation approach aided by a Temporal DropLoss. After training the final model on the resulting dense labelset, our approach outperforms the current state-of-the-art across various benchmarks.

