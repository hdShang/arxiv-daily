---
layout: default
title: "GS4: Generalizable Sparse Splatting Semantic SLAM"
---

# GS4: Generalizable Sparse Splatting Semantic SLAM

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06517" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06517v3</a>
  <a href="https://arxiv.org/pdf/2506.06517.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06517v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06517v3', 'GS4: Generalizable Sparse Splatting Semantic SLAM')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingqi Jiang, Chanho Kim, Chen Ziwen, Li Fuxin

**分类**: cs.CV

**发布日期**: 2025-06-06 (更新: 2025-12-03)

**备注**: 15 pages, 6 figures

---

## 💡 一句话要点

**提出GS4以解决传统SLAM在语义映射中的不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语义SLAM` `高斯点云` `3D映射` `深度学习` `机器人导航` `增强现实` `自动驾驶`

## 📋 核心要点

1. 现有SLAM方法在生成高质量语义地图时面临速度慢和高斯点使用过多的问题。
2. GS4通过前馈网络增量构建3D高斯点，结合颜色和语义预测，显著提高了效率。
3. 在ScanNet和ScanNet++基准测试中，GS4展现出最先进的语义SLAM性能，并在NYUv2和TUM RGB-D数据集上实现零样本迁移的强泛化能力。

## 📝 摘要（中文）

传统的SLAM算法在相机跟踪方面表现优异，但通常生成的不完整且低分辨率的地图与语义预测的集成度较低。近期的研究将高斯点云（Gaussian Splatting, GS）集成到SLAM中，以实现密集且逼真的3D映射。然而，现有的基于GS的SLAM方法需要逐场景优化，速度慢且消耗过多高斯点。本文提出GS4，这是第一个可泛化的基于GS的语义SLAM系统。与之前的方法相比，GS4运行速度快10倍，使用的高斯点少10倍，并在颜色、深度、语义映射和相机跟踪方面实现了最先进的性能。GS4从RGB-D视频流中增量构建和更新一组3D高斯点，采用前馈网络进行处理。

## 🔬 方法详解

**问题定义**：本文旨在解决传统SLAM在语义映射中生成低分辨率和不完整地图的问题，现有方法需要逐场景优化，导致速度慢且高斯点消耗过多。

**核心思路**：GS4通过前馈网络从RGB-D视频流中增量构建3D高斯点，结合颜色和语义信息，避免了冗余并提高了处理速度。

**技术框架**：GS4的整体架构包括高斯预测模型和高斯精炼网络。高斯预测模型从输入帧中估计稀疏的高斯参数，而高斯精炼网络则合并新高斯点与现有集合。

**关键创新**：GS4是首个可泛化的基于GS的语义SLAM系统，运行速度快10倍，使用的高斯点少10倍，显著提升了跟踪精度和语义映射质量。

**关键设计**：在高斯预测模型中，采用了统一的骨干网络来处理颜色和语义预测；高斯精炼网络通过避免冗余来优化高斯点的使用；在显著姿态变化时，仅进行1-5次联合高斯-姿态优化以减少漂移和提高跟踪精度。

## 📊 实验亮点

在真实世界的ScanNet和ScanNet++基准测试中，GS4展现出最先进的语义SLAM性能，运行速度提升10倍，使用的高斯点减少10倍。此外，GS4在NYUv2和TUM RGB-D数据集上实现了零样本迁移，显示出强大的泛化能力。

## 🎯 应用场景

GS4的研究成果在机器人导航、增强现实和自动驾驶等领域具有广泛的应用潜力。通过提供高质量的语义地图，GS4能够支持更智能的环境理解和决策制定，推动相关技术的发展与应用。未来，GS4可能在实时场景重建和人机交互等方面发挥重要作用。

## 📄 摘要（原文）

> Traditional SLAM algorithms excel at camera tracking, but typically produce incomplete and low-resolution maps that are not tightly integrated with semantics prediction. Recent work integrates Gaussian Splatting (GS) into SLAM to enable dense, photorealistic 3D mapping, yet existing GS-based SLAM methods require per-scene optimization that is slow and consumes an excessive number of Gaussians. We present GS4, the first generalizable GS-based semantic SLAM system. Compared with prior approaches, GS4 runs 10x faster, uses 10x fewer Gaussians, and achieves state-of-the-art performance across color, depth, semantic mapping and camera tracking. From an RGB-D video stream, GS4 incrementally builds and updates a set of 3D Gaussians using a feed-forward network. First, the Gaussian Prediction Model estimates a sparse set of Gaussian parameters from input frame, which integrates both color and semantic prediction with the same backbone. Then, the Gaussian Refinement Network merges new Gaussians with the existing set while avoiding redundancy. Finally, when significant pose changes are detected, we perform only 1-5 iterations of joint Gaussian-pose optimization to correct drift, remove floaters, and further improve tracking accuracy. Experiments on the real-world ScanNet and ScanNet++ benchmarks demonstrate state-of-the-art semantic SLAM performance, with strong generalization capability shown through zero-shot transfer to the NYUv2 and TUM RGB-D datasets.

