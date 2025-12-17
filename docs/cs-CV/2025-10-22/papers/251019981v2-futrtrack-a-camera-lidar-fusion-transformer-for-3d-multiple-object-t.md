---
layout: default
title: FutrTrack: A Camera-LiDAR Fusion Transformer for 3D Multiple Object Tracking
---

# FutrTrack: A Camera-LiDAR Fusion Transformer for 3D Multiple Object Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19981" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19981v2</a>
  <a href="https://arxiv.org/pdf/2510.19981.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19981v2" onclick="toggleFavorite(this, '2510.19981v2', 'FutrTrack: A Camera-LiDAR Fusion Transformer for 3D Multiple Object Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Martha Teiko Teye, Ori Maoz, Matthias Rottmann

**分类**: cs.CV

**发布日期**: 2025-10-22 (更新: 2025-12-15)

**备注**: Accepted to VISAPP 2026

---

## 💡 一句话要点

**FutrTrack：一种用于3D多目标跟踪的相机-激光雷达融合Transformer**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多目标跟踪` `3D目标检测` `Transformer` `多模态融合` `相机-激光雷达融合` `自动驾驶` `鸟瞰图`

## 📋 核心要点

1. 现有3D多目标跟踪方法在遮挡和视角变化下鲁棒性不足，且对多模态信息的有效融合仍具挑战。
2. FutrTrack利用Transformer架构，通过多模态融合和时间平滑，提升跟踪的准确性和鲁棒性，无需显式运动模型。
3. 在nuScenes和KITTI数据集上，FutrTrack表现出强大的性能，尤其是在减少身份切换方面有显著提升。

## 📝 摘要（中文）

我们提出了FutrTrack，一个模块化的相机-激光雷达多目标跟踪框架，它建立在现有的3D检测器之上，引入了一个基于Transformer的平滑器和一个融合驱动的跟踪器。受到基于查询的跟踪框架的启发，FutrTrack采用了一种多模态两阶段Transformer细化和跟踪流程。我们的融合跟踪器集成了边界框以及来自多个相机和激光雷达的多模态鸟瞰图（BEV）融合特征，而无需显式的运动模型。该跟踪器跨帧分配和传播身份，利用几何和语义线索来实现遮挡和视角变化下的鲁棒重识别。在跟踪之前，我们使用移动窗口上的时间平滑器来细化边界框序列，以优化轨迹，减少抖动并提高空间一致性。在nuScenes和KITTI上的评估表明，与之前的单传感器方法相比，基于查询的Transformer跟踪方法可以从多模态传感器特征中获益匪浅。FutrTrack在nuScenes测试集上实现了74.7的aMOTA，在3D MOT基准测试中表现出色，在保持竞争力的同时减少了身份切换。我们的方法提供了一个高效的框架，用于改进基于Transformer的跟踪器，即使在数据有限且没有预训练的情况下也能与其他基于神经网络的方法竞争。

## 🔬 方法详解

**问题定义**：论文旨在解决3D多目标跟踪（MOT）问题，尤其是在复杂场景下，如遮挡、视角变化等因素导致的跟踪性能下降。现有方法通常依赖于单一传感器信息或显式的运动模型，难以充分利用多模态数据，并且在身份保持方面存在挑战。

**核心思路**：FutrTrack的核心思路是利用Transformer架构，结合相机和激光雷达的多模态信息，进行融合驱动的跟踪。通过基于查询的跟踪方式，将目标检测结果作为查询，利用Transformer的注意力机制，在多模态特征空间中进行关联和跟踪。同时，引入时间平滑模块，优化轨迹，减少抖动。

**技术框架**：FutrTrack包含三个主要模块：3D目标检测器（backbone，可替换），基于Transformer的平滑器，以及融合驱动的跟踪器。首先，使用3D目标检测器提取每一帧的边界框。然后，时间平滑器对边界框序列进行优化，减少噪声。最后，融合跟踪器将边界框与多模态BEV融合特征结合，利用Transformer进行目标关联和身份传播。

**关键创新**：该论文的关键创新在于提出了一个多模态融合的Transformer跟踪框架，无需显式的运动模型，即可实现鲁棒的3D MOT。通过两阶段Transformer细化和跟踪流程，有效利用了相机和激光雷达的信息，提升了跟踪的准确性和鲁棒性。

**关键设计**：FutrTrack的关键设计包括：1) 多模态BEV融合特征的提取，用于提供丰富的上下文信息；2) 基于Transformer的跟踪器，利用注意力机制进行目标关联；3) 时间平滑模块，优化轨迹，减少抖动；4) 两阶段Transformer结构，分别进行细化和跟踪。

## 📊 实验亮点

FutrTrack在nuScenes测试集上实现了74.7的aMOTA，显著优于之前的单传感器方法。实验结果表明，多模态融合能够显著提升基于Transformer的跟踪器的性能。此外，FutrTrack在减少身份切换方面表现出色，表明其在复杂场景下具有更强的鲁棒性。

## 🎯 应用场景

FutrTrack可应用于自动驾驶、机器人导航、智能监控等领域。通过融合相机和激光雷达等多模态信息，能够提升复杂环境下目标跟踪的准确性和鲁棒性，为安全可靠的智能系统提供关键技术支撑，并有望在智慧交通、安防等领域发挥重要作用。

## 📄 摘要（原文）

> We propose FutrTrack, a modular camera-LiDAR multi-object tracking framework that builds on existing 3D detectors by introducing a transformer-based smoother and a fusion-driven tracker. Inspired by query-based tracking frameworks, FutrTrack employs a multimodal two-stage transformer refinement and tracking pipeline. Our fusion tracker integrates bounding boxes with multimodal bird's-eye-view (BEV) fusion features from multiple cameras and LiDAR without the need for an explicit motion model. The tracker assigns and propagates identities across frames, leveraging both geometric and semantic cues for robust re-identification under occlusion and viewpoint changes. Prior to tracking, we refine sequences of bounding boxes with a temporal smoother over a moving window to refine trajectories, reduce jitter, and improve spatial consistency. Evaluated on nuScenes and KITTI, FutrTrack demonstrates that query-based transformer tracking methods benefit significantly from multimodal sensor features compared with previous single-sensor approaches. With an aMOTA of 74.7 on the nuScenes test set, FutrTrack achieves strong performance on 3D MOT benchmarks, reducing identity switches while maintaining competitive accuracy. Our approach provides an efficient framework for improving transformer-based trackers to compete with other neural-network-based methods even with limited data and without pretraining.

