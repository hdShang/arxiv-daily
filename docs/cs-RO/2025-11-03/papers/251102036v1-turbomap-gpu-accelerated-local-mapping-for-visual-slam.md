---
layout: default
title: TurboMap: GPU-Accelerated Local Mapping for Visual SLAM
---

# TurboMap: GPU-Accelerated Local Mapping for Visual SLAM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02036" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02036v1</a>
  <a href="https://arxiv.org/pdf/2511.02036.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02036v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.02036v1', 'TurboMap: GPU-Accelerated Local Mapping for Visual SLAM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Parsa Hosseininejad, Kimia Khabiri, Shishir Gopinath, Soudabeh Mohammadhashemi, Karthik Dantu, Steven Y. Ko

**分类**: cs.RO

**发布日期**: 2025-11-03

**备注**: Submitted to ICRA 2026

---

## 💡 一句话要点

**TurboMap：面向视觉SLAM的GPU加速局部地图构建模块**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉SLAM` `局部地图构建` `GPU加速` `CUDA` `Bundle Adjustment`

## 📋 核心要点

1. 视觉SLAM局部地图构建计算量大，是系统性能瓶颈，现有方法难以兼顾精度与效率。
2. TurboMap通过GPU加速地图点三角化与融合，CPU优化关键帧剔除，以及GPU加速的BA求解器，提升效率。
3. 实验表明，TurboMap在EuRoC和TUM-VI数据集上实现了显著加速，同时保持了ORB-SLAM3的精度。

## 📝 摘要（中文）

本文提出了TurboMap，一个为视觉SLAM系统设计的GPU加速和CPU优化的局部地图构建模块。我们识别了视觉SLAM局部地图构建过程中的关键性能瓶颈，并通过有针对性的GPU和CPU优化来解决这些问题。具体来说，我们将地图点的三角化和融合卸载到GPU上，加速CPU上的冗余关键帧剔除，并集成了一个GPU加速的求解器来加速局部Bundle Adjustment。我们的实现基于ORB-SLAM3，并利用CUDA进行GPU编程。实验结果表明，在桌面和嵌入式平台上，TurboMap在EuRoC数据集上实现了平均1.3倍的局部地图构建模块加速，在TUM-VI数据集上实现了1.6倍的加速，同时保持了原始系统的精度。

## 🔬 方法详解

**问题定义**：视觉SLAM中的局部地图构建模块是计算密集型任务，尤其是在高精度和大规模场景下。现有的方法通常在CPU上执行，效率较低，难以满足实时性需求。此外，关键帧的冗余剔除和Bundle Adjustment的求解也是耗时操作，限制了SLAM系统的整体性能。

**核心思路**：TurboMap的核心思路是将局部地图构建中的计算密集型任务卸载到GPU上进行并行处理，充分利用GPU的计算能力。同时，对CPU上的任务进行优化，减少不必要的计算，从而提高整体效率。通过CPU和GPU的协同工作，实现局部地图构建的加速。

**技术框架**：TurboMap构建于ORB-SLAM3之上，主要包含以下几个模块：1) GPU加速的地图点三角化和融合模块，负责从多个关键帧中恢复地图点，并将新的地图点融合到现有地图中；2) CPU优化的关键帧剔除模块，负责剔除冗余的关键帧，减少后续Bundle Adjustment的计算量；3) GPU加速的局部Bundle Adjustment模块，负责优化局部地图和相机位姿。

**关键创新**：TurboMap的关键创新在于将地图点三角化和融合、局部Bundle Adjustment等计算密集型任务卸载到GPU上，并针对CPU上的关键帧剔除进行优化。这种CPU和GPU协同工作的策略，充分利用了两种硬件的优势，实现了局部地图构建的加速。与现有方法相比，TurboMap能够在保持精度的前提下，显著提高局部地图构建的效率。

**关键设计**：TurboMap使用CUDA进行GPU编程，充分利用GPU的并行计算能力。在地图点三角化和融合模块中，采用了高效的并行算法，加速了地图点的恢复和融合过程。在关键帧剔除模块中，采用了基于共视关系的剔除策略，减少了冗余关键帧的数量。在局部Bundle Adjustment模块中，采用了GPU加速的求解器，加速了优化过程。具体参数设置和损失函数与ORB-SLAM3保持一致。

## 📊 实验亮点

TurboMap在EuRoC数据集上实现了平均1.3倍的局部地图构建模块加速，在TUM-VI数据集上实现了1.6倍的加速。这些加速是在桌面和嵌入式平台上实现的，表明TurboMap具有良好的可移植性和适应性。更重要的是，TurboMap在加速的同时，保持了ORB-SLAM3的精度，证明了其有效性。

## 🎯 应用场景

TurboMap可应用于需要实时性和高精度的视觉SLAM应用中，例如增强现实、机器人导航、无人机自主飞行、自动驾驶等。通过加速局部地图构建，TurboMap可以提高SLAM系统的整体性能，使其能够处理更大规模的场景和更复杂的环境。此外，TurboMap还可以在嵌入式平台上运行，使其能够应用于资源受限的移动设备和机器人。

## 📄 摘要（原文）

> This paper presents TurboMap, a GPU-accelerated and CPU-optimized local mapping module for visual SLAM systems. We identify key performance bottlenecks in the local mapping process for visual SLAM and address them through targeted GPU and CPU optimizations. Specifically, we offload map point triangulation and fusion to the GPU, accelerate redundant keyframe culling on the CPU, and integrate a GPU-accelerated solver to speed up local bundle adjustment. Our implementation is built on top of ORB-SLAM3 and leverages CUDA for GPU programming. The experimental results show that TurboMap achieves an average speedup of 1.3x in the EuRoC dataset and 1.6x in the TUM-VI dataset in the local mapping module, on both desktop and embedded platforms, while maintaining the accuracy of the original system.

