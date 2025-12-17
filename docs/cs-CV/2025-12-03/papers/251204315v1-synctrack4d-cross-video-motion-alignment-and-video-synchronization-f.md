---
layout: default
title: SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting
---

# SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04315" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04315v1</a>
  <a href="https://arxiv.org/pdf/2512.04315.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04315v1" onclick="toggleFavorite(this, '2512.04315v1', 'SyncTrack4D: Cross-Video Motion Alignment and Video Synchronization for Multi-Video 4D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yonghan Lee, Tsung-Wei Huang, Shiv Gehlot, Jaehoon Choi, Guan-Ming Su, Dinesh Manocha

**分类**: cs.CV

**发布日期**: 2025-12-03

---

## 💡 一句话要点

**SyncTrack4D：面向未同步多视角视频的4D高斯溅射动态场景重建。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `4D高斯溅射` `多视角视频` `视频同步` `动态场景重建` `Gromov-Wasserstein最优传输`

## 📋 核心要点

1. 动态3D场景建模面临高维挑战，需要聚合多视角信息以重建随时间演变的3D几何和运动。
2. SyncTrack4D利用密集4D轨迹表示作为跨视频同步和4DGS重建的关键线索，实现同步和重建的联合优化。
3. 实验表明，该方法在未同步视频上实现了亚帧级的同步精度和高保真度的4D动态场景重建。

## 📝 摘要（中文）

本文提出了一种新颖的多视频4D高斯溅射(4DGS)方法SyncTrack4D，旨在处理真实世界中未同步的视频集。该方法直接利用动态场景部分的密集4D轨迹表示作为线索，用于同步跨视频和4DGS重建。首先，通过融合Gromov-Wasserstein最优传输方法计算密集的每个视频的4D特征轨迹和跨视频轨迹对应关系。接下来，执行全局帧级时间对齐，以最大化匹配的4D轨迹的重叠运动。最后，通过基于运动样条骨架表示的多视频4D高斯溅射实现亚帧同步。最终输出是同步的4DGS表示，具有密集的、显式的3D轨迹和每个视频的时间偏移量。在Panoptic Studio和SyncNeRF Blender数据集上的评估表明，该方法具有亚帧同步精度，平均时间误差低于0.26帧，并在Panoptic Studio数据集上实现了高达26.3 PSNR的高保真4D重建。据我们所知，我们的工作是第一个通用的针对未同步视频集的4D高斯溅射方法，无需假设预定义的场景对象或先验模型。

## 🔬 方法详解

**问题定义**：现有动态3D场景重建方法难以处理未同步的多视角视频，这导致无法准确地对齐不同视角下的运动信息，从而影响重建质量。现有的4D高斯溅射方法通常假设视频是同步的，或者需要预定义的场景对象或先验模型，这限制了它们在真实世界场景中的应用。

**核心思路**：SyncTrack4D的核心思路是利用动态场景中各部分的4D轨迹信息，通过优化跨视频的轨迹对齐来实现视频同步和4D高斯溅射重建的联合优化。通过最大化匹配的4D轨迹的运动重叠，可以有效地估计视频之间的时间偏移量，从而实现亚帧级别的同步。

**技术框架**：SyncTrack4D包含三个主要阶段：1) 密集4D特征轨迹提取和跨视频轨迹对应关系计算：使用融合Gromov-Wasserstein最优传输方法计算每个视频的4D特征轨迹，并建立跨视频的轨迹对应关系。2) 全局帧级时间对齐：通过最大化匹配的4D轨迹的运动重叠，进行全局帧级时间对齐。3) 亚帧同步和多视频4D高斯溅射：基于运动样条骨架表示，实现亚帧同步，并进行多视频4D高斯溅射重建。

**关键创新**：该方法的主要创新在于：1) 提出了一种通用的针对未同步视频集的4D高斯溅射方法，无需假设预定义的场景对象或先验模型。2) 利用密集4D轨迹表示作为跨视频同步和4DGS重建的关键线索，实现了同步和重建的联合优化。3) 采用融合Gromov-Wasserstein最优传输方法计算跨视频轨迹对应关系，提高了轨迹匹配的准确性。

**关键设计**：在轨迹对应关系计算中，使用了融合Gromov-Wasserstein最优传输方法，该方法能够有效地处理不同视角下的轨迹差异。在全局帧级时间对齐中，设计了损失函数来最大化匹配的4D轨迹的运动重叠。在亚帧同步和多视频4D高斯溅射中，使用了运动样条骨架表示，该表示能够有效地捕捉动态场景的运动信息。

## 📊 实验亮点

SyncTrack4D在Panoptic Studio数据集上实现了亚帧同步精度，平均时间误差低于0.26帧，并在该数据集上实现了高达26.3 PSNR的高保真4D重建。这些结果表明，该方法能够有效地处理未同步的多视角视频，并实现高质量的动态3D场景重建。与现有方法相比，SyncTrack4D无需假设预定义的场景对象或先验模型，具有更强的通用性和鲁棒性。

## 🎯 应用场景

该研究成果可应用于各种需要处理未同步多视角视频的场景，例如：动作捕捉、虚拟现实/增强现实、自动驾驶、机器人导航、监控系统等。通过高精度地重建动态3D场景，可以为这些应用提供更准确、更可靠的环境感知和交互能力，具有重要的实际应用价值和广阔的未来发展前景。

## 📄 摘要（原文）

> Modeling dynamic 3D scenes is challenging due to their high-dimensional nature, which requires aggregating information from multiple views to reconstruct time-evolving 3D geometry and motion. We present a novel multi-video 4D Gaussian Splatting (4DGS) approach designed to handle real-world, unsynchronized video sets. Our approach, SyncTrack4D, directly leverages dense 4D track representation of dynamic scene parts as cues for simultaneous cross-video synchronization and 4DGS reconstruction. We first compute dense per-video 4D feature tracks and cross-video track correspondences by Fused Gromov-Wasserstein optimal transport approach. Next, we perform global frame-level temporal alignment to maximize overlapping motion of matched 4D tracks. Finally, we achieve sub-frame synchronization through our multi-video 4D Gaussian splatting built upon a motion-spline scaffold representation. The final output is a synchronized 4DGS representation with dense, explicit 3D trajectories, and temporal offsets for each video. We evaluate our approach on the Panoptic Studio and SyncNeRF Blender, demonstrating sub-frame synchronization accuracy with an average temporal error below 0.26 frames, and high-fidelity 4D reconstruction reaching 26.3 PSNR scores on the Panoptic Studio dataset. To the best of our knowledge, our work is the first general 4D Gaussian Splatting approach for unsynchronized video sets, without assuming the existence of predefined scene objects or prior models.

