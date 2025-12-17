---
layout: default
title: FutrTrack: A Camera-LiDAR Fusion Transformer for 3D Multiple Object Tracking
---

# FutrTrack: A Camera-LiDAR Fusion Transformer for 3D Multiple Object Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.19981" class="toolbar-btn" target="_blank">📄 arXiv: 2510.19981</a>
  <a href="https://arxiv.org/pdf/2510.19981.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19981" onclick="toggleFavorite(this, '2510.19981', 'FutrTrack: A Camera-LiDAR Fusion Transformer for 3D Multiple Object Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Martha Teiko Teye, Ori Maoz, Matthias Rottmann

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**FutrTrack：一种用于3D多目标跟踪的相机-激光雷达融合Transformer**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D多目标跟踪` `多模态融合` `Transformer` `相机-激光雷达融合` `目标跟踪`

## 📋 核心要点

1. 现有3D多目标跟踪方法在遮挡和视点变化下鲁棒性不足，且对多模态信息的有效融合仍具挑战。
2. FutrTrack利用Transformer架构，通过多模态融合特征和时间平滑，提升跟踪的准确性和鲁棒性。
3. 实验表明，FutrTrack在nuScenes和KITTI数据集上表现出色，尤其在减少身份切换方面有显著提升。

## 📝 摘要（中文）

我们提出了FutrTrack，一个模块化的相机-激光雷达多目标跟踪框架，它建立在现有的3D检测器之上，引入了一个基于Transformer的平滑器和一个融合驱动的跟踪器。受到基于查询的跟踪框架的启发，FutrTrack采用了一种多模态两阶段Transformer细化和跟踪流程。我们的融合跟踪器集成了来自多个相机和激光雷达的边界框与多模态鸟瞰图（BEV）融合特征，而无需显式的运动模型。该跟踪器在帧之间分配和传播身份，利用几何和语义线索来实现遮挡和视点变化下的鲁棒重识别。在跟踪之前，我们使用移动窗口上的时间平滑器来细化边界框序列，以细化轨迹，减少抖动并提高空间一致性。在nuScenes和KITTI上的评估表明，与之前的单传感器方法相比，基于查询的Transformer跟踪方法从多模态传感器特征中获益匪浅。在nuScenes测试集上，FutrTrack的aMOTA为74.7，在3D MOT基准测试中表现出色，在保持竞争力的同时减少了身份切换。我们的方法提供了一个高效的框架，用于改进基于Transformer的跟踪器，即使在数据有限且没有预训练的情况下，也能与其他基于神经网络的方法竞争。

## 🔬 方法详解

**问题定义**：论文旨在解决3D多目标跟踪（MOT）问题，特别是在复杂场景下，由于遮挡、视点变化以及传感器噪声等因素，导致跟踪性能下降的问题。现有方法通常依赖于显式的运动模型，对运动状态假设较强，且难以有效融合来自不同模态（相机和激光雷达）的信息。

**核心思路**：FutrTrack的核心思路是利用Transformer架构强大的特征提取和关联能力，通过多模态融合和时间平滑来提升跟踪的准确性和鲁棒性。该方法避免了对运动模型的显式依赖，而是通过学习数据中的潜在关联来实现跟踪。

**技术框架**：FutrTrack包含三个主要模块：3D目标检测器（使用现有方法）、基于Transformer的时间平滑器和融合驱动的跟踪器。首先，使用3D检测器提取每一帧的物体边界框。然后，时间平滑器利用Transformer对一段时间内的边界框序列进行优化，减少抖动并提高空间一致性。最后，融合驱动的跟踪器将相机和激光雷达的多模态BEV特征与边界框信息融合，利用Transformer进行目标关联和身份传播。

**关键创新**：FutrTrack的关键创新在于其融合驱动的跟踪器，它能够有效地融合来自多个相机和激光雷达的多模态BEV特征，而无需显式的运动模型。此外，使用Transformer进行时间平滑也提高了轨迹的质量。

**关键设计**：时间平滑器使用Transformer编码器-解码器结构，将一段时间内的边界框序列作为输入，输出优化后的边界框序列。融合驱动的跟踪器使用Transformer进行目标关联，损失函数包括分类损失和回归损失，用于优化目标关联和边界框预测。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.19981/images/page1img.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.19981/images/overall_fig1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2510.19981/images/vis_futrtrack3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

FutrTrack在nuScenes测试集上取得了74.7的aMOTA，显著优于之前的单传感器方法。与现有技术相比，FutrTrack在保持竞争力的同时，显著减少了身份切换的次数，表明其在复杂场景下的跟踪鲁棒性更强。实验结果验证了多模态融合和Transformer架构在3D多目标跟踪中的有效性。

## 🎯 应用场景

FutrTrack在自动驾驶、机器人导航、智能交通等领域具有广泛的应用前景。它可以用于提高车辆和机器人在复杂环境下的感知能力，实现更安全、更可靠的自主导航和决策。该研究对于提升多传感器融合和目标跟踪技术水平具有重要意义。

## 📄 摘要（原文）

> We propose FutrTrack, a modular camera-LiDAR multi-object tracking framework that builds on existing 3D detectors by introducing a transformer-based smoother and a fusion-driven tracker. Inspired by query-based tracking frameworks, FutrTrack employs a multimodal two-stage transformer refinement and tracking pipeline. Our fusion tracker integrates bounding boxes with multimodal bird's-eye-view (BEV) fusion features from multiple cameras and LiDAR without the need for an explicit motion model. The tracker assigns and propagates identities across frames, leveraging both geometric and semantic cues for robust re-identification under occlusion and viewpoint changes. Prior to tracking, we refine sequences of bounding boxes with a temporal smoother over a moving window to refine trajectories, reduce jitter, and improve spatial consistency. Evaluated on nuScenes and KITTI, FutrTrack demonstrates that query-based transformer tracking methods benefit significantly from multimodal sensor features compared with previous single-sensor approaches. With an aMOTA of 74.7 on the nuScenes test set, FutrTrack achieves strong performance on 3D MOT benchmarks, reducing identity switches while maintaining competitive accuracy. Our approach provides an efficient framework for improving transformer-based trackers to compete with other neural-network-based methods even with limited data and without pretraining.

