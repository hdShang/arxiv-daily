---
layout: default
title: InstantSfM: Fully Sparse and Parallel Structure-from-Motion
---

# InstantSfM: Fully Sparse and Parallel Structure-from-Motion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13310" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13310v1</a>
  <a href="https://arxiv.org/pdf/2510.13310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13310v1" onclick="toggleFavorite(this, '2510.13310v1', 'InstantSfM: Fully Sparse and Parallel Structure-from-Motion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiankun Zhong, Zitong Zhan, Quankai Gao, Ziyu Chen, Haozhe Lou, Jiageng Mao, Ulrich Neumann, Yue Wang

**分类**: cs.CV

**发布日期**: 2025-10-15

**🔗 代码/项目**: [PROJECT_PAGE](https://cre185.github.io/InstantSfM/)

---

## 💡 一句话要点

**InstantSfM：全稀疏并行Structure-from-Motion，加速大规模场景重建。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `Structure-from-Motion` `三维重建` `GPU加速` `并行计算` `Bundle Adjustment` `Global Positioning` `稀疏优化`

## 📋 核心要点

1. 传统 SfM 方法在大规模场景中计算开销大，精度和速度难以兼顾，且灵活性不足，深度学习方法则受限于GPU内存。
2. 论文提出一种全稀疏并行 SfM 框架 InstantSfM，充分利用 GPU 并行计算加速 BA 和 GP 过程。
3. 实验表明，InstantSfM 在大规模数据集上比 COLMAP 快约 40 倍，并保持或提升了重建精度。

## 📝 摘要（中文）

Structure-from-Motion (SfM) 是一种从无标定图像中恢复相机位姿和场景几何的方法，是机器人重建和模拟的核心组成部分。尽管 COLMAP 及其后续工作 GLOMAP 等传统 SfM 方法具有最先进的性能，但 Bundle Adjustment (BA) 或 Global Positioning (GP) 的 CPU 专用实现方式在处理大规模场景时会引入显著的计算开销，导致 SfM 在精度和速度之间做出权衡。此外，COLMAP 和 GLOMAP 中高效的 C++ 实现也缺乏灵活性，不支持各种外部优化选项。另一方面，像 VGGSfM 和 VGGT 这样基于深度学习的 SfM 流程虽然能够进行前馈 3D 重建，但由于 GPU 内存消耗随着输入视图数量的增长而急剧增加，因此无法扩展到一次处理数千个输入视图。本文充分利用 GPU 并行计算的潜力来加速标准 SfM 流程的每个关键阶段。基于稀疏感知 Bundle Adjustment 优化的最新进展，我们的设计扩展了这些技术，以加速统一全局 SfM 框架内的 BA 和 GP。通过在不同规模的数据集上进行的大量实验（例如，VGGSfM 和 VGGT 内存耗尽的 5000 张图像），我们的方法展示了比 COLMAP 快约 40 倍的速度，同时实现了始终如一的相当甚至更高的重建精度。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模场景下 Structure-from-Motion (SfM) 方法计算效率低下的问题。现有方法，如 COLMAP，在 Bundle Adjustment (BA) 和 Global Positioning (GP) 阶段主要依赖 CPU，导致处理大规模数据集时速度慢。基于深度学习的 SfM 方法虽然可以利用 GPU 加速，但内存消耗随图像数量线性增长，难以扩展到大规模场景。

**核心思路**：论文的核心思路是充分利用 GPU 的并行计算能力，加速 SfM 流程中的关键步骤，特别是 BA 和 GP。通过将稀疏感知优化技术应用于 BA 和 GP，并在统一的全局 SfM 框架内实现，从而在保证重建精度的前提下，显著提高计算速度。

**技术框架**：InstantSfM 沿用了标准 SfM 流程，主要包含特征提取、特征匹配、初始重建、全局 BA 和 GP 等阶段。关键在于对 BA 和 GP 阶段的 GPU 并行加速。整体架构上，论文并没有引入新的模块，而是专注于优化现有模块的计算效率。

**关键创新**：最重要的技术创新点在于将稀疏感知优化技术扩展到 BA 和 GP 阶段，并充分利用 GPU 的并行计算能力。与传统方法相比，InstantSfM 能够更有效地处理大规模稀疏矩阵，从而显著加速 BA 和 GP 的计算过程。

**关键设计**：论文采用了稀疏矩阵表示和并行计算策略，以加速 BA 和 GP 的计算。具体的技术细节包括：(1) 使用高效的稀疏矩阵库来存储和操作相机位姿和三维点之间的关系；(2) 将 BA 和 GP 的计算任务分解为多个小的子任务，并在 GPU 上并行执行；(3) 优化内存访问模式，以减少 GPU 的内存访问延迟。

## 📊 实验亮点

实验结果表明，InstantSfM 在大规模数据集上实现了显著的性能提升。在包含 5000 张图像的数据集上，InstantSfM 的速度比 COLMAP 快约 40 倍，同时保持了相当甚至更高的重建精度。此外，InstantSfM 能够处理 VGGSfM 和 VGGT 因内存限制而无法处理的大规模数据集，证明了其在大规模场景下的优越性。

## 🎯 应用场景

该研究成果可广泛应用于机器人导航、三维地图重建、虚拟现实、增强现实等领域。通过提高 SfM 的计算效率，可以实现更大规模、更高精度的场景重建，为相关应用提供更好的支持。例如，在自动驾驶领域，可以利用 InstantSfM 快速构建高精度的环境地图，从而提高车辆的定位和导航能力。

## 📄 摘要（原文）

> Structure-from-Motion (SfM), a method that recovers camera poses and scene geometry from uncalibrated images, is a central component in robotic reconstruction and simulation. Despite the state-of-the-art performance of traditional SfM methods such as COLMAP and its follow-up work, GLOMAP, naive CPU-specialized implementations of bundle adjustment (BA) or global positioning (GP) introduce significant computational overhead when handling large-scale scenarios, leading to a trade-off between accuracy and speed in SfM. Moreover, the blessing of efficient C++-based implementations in COLMAP and GLOMAP comes with the curse of limited flexibility, as they lack support for various external optimization options. On the other hand, while deep learning based SfM pipelines like VGGSfM and VGGT enable feed-forward 3D reconstruction, they are unable to scale to thousands of input views at once as GPU memory consumption increases sharply as the number of input views grows. In this paper, we unleash the full potential of GPU parallel computation to accelerate each critical stage of the standard SfM pipeline. Building upon recent advances in sparse-aware bundle adjustment optimization, our design extends these techniques to accelerate both BA and GP within a unified global SfM framework. Through extensive experiments on datasets of varying scales (e.g. 5000 images where VGGSfM and VGGT run out of memory), our method demonstrates up to about 40 times speedup over COLMAP while achieving consistently comparable or even improved reconstruction accuracy. Our project page can be found at https://cre185.github.io/InstantSfM/.

