---
layout: default
title: CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking
---

# CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15580" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15580v3</a>
  <a href="https://arxiv.org/pdf/2511.15580.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15580v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.15580v3', 'CompTrack: Information Bottleneck-Guided Low-Rank Dynamic Token Compression for Point Cloud Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sifan Zhou, Yichao Cao, Jiahao Nie, Yuqian Fu, Ziyu Zhao, Xiaobo Lu, Shuo Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-19 (更新: 2025-11-22)

**备注**: Accepted by AAAI 2026 (Oral)

---

## 💡 一句话要点

**CompTrack：信息瓶颈引导的低秩动态Token压缩，用于点云单目标跟踪。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `点云跟踪` `单目标跟踪` `信息瓶颈` `动态Token压缩` `低秩近似` `LiDAR` `自动驾驶`

## 📋 核心要点

1. 现有3D单目标跟踪器受限于点云的稀疏性，面临背景噪声的空间冗余和前景信息内部的信息冗余的双重挑战。
2. CompTrack通过空间前景预测器（SFP）消除背景噪声，并利用信息瓶颈引导的动态Token压缩（IB-DTC）模块压缩前景信息，实现高效跟踪。
3. 实验结果表明，CompTrack在KITTI、nuScenes和Waymo数据集上实现了领先的跟踪性能，并在RTX 3090 GPU上达到90 FPS的实时速度。

## 📝 摘要（中文）

本文提出CompTrack，一个新颖的端到端框架，旨在系统性地消除LiDAR点云中的冗余信息，从而提升3D单目标跟踪（SOT）的性能。针对点云固有的稀疏性带来的双重冗余问题：背景噪声造成的空间冗余和前景信息内部的信息冗余，CompTrack首先引入空间前景预测器（SFP）模块，基于信息熵过滤掉不相关的背景噪声，解决空间冗余问题。然后，利用信息瓶颈引导的动态Token压缩（IB-DTC）模块，消除前景内部的信息冗余。该模块基于低秩近似的理论基础，利用在线SVD分析自适应地将冗余前景压缩成紧凑且信息量大的代理Token集合。在KITTI、nuScenes和Waymo数据集上的大量实验表明，CompTrack实现了顶级的跟踪性能和卓越的效率，在单个RTX 3090 GPU上以90 FPS的实时速度运行。

## 🔬 方法详解

**问题定义**：现有的3D单目标跟踪方法在处理LiDAR点云时，由于点云的稀疏性，存在两个主要的痛点：一是背景噪声带来的空间冗余，降低了跟踪的准确性；二是前景信息内部存在信息冗余，限制了跟踪的效率。因此，如何在保证跟踪精度的前提下，有效地消除点云中的冗余信息，是本文要解决的关键问题。

**核心思路**：CompTrack的核心思路是通过两个阶段的冗余消除来提升跟踪性能和效率。首先，利用空间前景预测器（SFP）过滤掉不相关的背景噪声，减少空间冗余。然后，利用信息瓶颈引导的动态Token压缩（IB-DTC）模块，将前景信息压缩成更紧凑、信息量更大的表示，从而减少信息冗余。这种两阶段的冗余消除策略旨在保留关键信息的同时，降低计算复杂度。

**技术框架**：CompTrack的整体框架包含两个主要模块：空间前景预测器（SFP）和信息瓶颈引导的动态Token压缩（IB-DTC）。SFP模块首先对输入点云进行处理，预测前景区域，并过滤掉背景噪声。然后，IB-DTC模块对SFP输出的前景点云进行进一步压缩，提取关键的代理Token。最后，利用这些代理Token进行目标跟踪。整个过程是端到端可训练的。

**关键创新**：CompTrack的关键创新在于信息瓶颈引导的动态Token压缩（IB-DTC）模块。该模块利用信息瓶颈原理，通过在线SVD分析自适应地压缩前景信息，提取最具代表性的Token。与传统的静态Token选择方法不同，IB-DTC能够根据输入点云的动态变化，自适应地调整Token的数量和位置，从而更好地保留目标的关键信息。此外，将低秩近似理论引入点云跟踪任务，为解决信息冗余问题提供了新的思路。

**关键设计**：SFP模块的设计基于信息熵，用于评估每个点的显著性，从而区分前景和背景。IB-DTC模块的关键在于在线SVD分析，用于计算点云特征的奇异值和奇异向量，从而确定最具代表性的Token。损失函数的设计需要平衡跟踪精度和压缩效率，例如，可以采用跟踪损失和信息瓶颈损失的加权和。具体的网络结构细节（如卷积层数、通道数等）需要根据具体数据集进行调整。

## 📊 实验亮点

CompTrack在KITTI、nuScenes和Waymo数据集上取得了显著的性能提升。例如，在KITTI数据集上，CompTrack的跟踪精度超过了现有最佳方法，并且在单个RTX 3090 GPU上实现了90 FPS的实时速度。这表明CompTrack在保证跟踪精度的同时，显著提高了跟踪效率，使其更适用于实际应用场景。

## 🎯 应用场景

CompTrack在自动驾驶、机器人导航、智能监控等领域具有广泛的应用前景。通过提高3D目标跟踪的效率和准确性，可以提升自动驾驶系统的感知能力，增强机器人在复杂环境中的导航能力，并改善智能监控系统的目标检测和跟踪性能。该研究的成果有助于推动这些领域的发展，并为未来的研究提供新的思路。

## 📄 摘要（原文）

> 3D single object tracking (SOT) in LiDAR point clouds is a critical task in computer vision and autonomous driving. Despite great success having been achieved, the inherent sparsity of point clouds introduces a dual-redundancy challenge that limits existing trackers: (1) vast spatial redundancy from background noise impairs accuracy, and (2) informational redundancy within the foreground hinders efficiency. To tackle these issues, we propose CompTrack, a novel end-to-end framework that systematically eliminates both forms of redundancy in point clouds. First, CompTrack incorporates a Spatial Foreground Predictor (SFP) module to filter out irrelevant background noise based on information entropy, addressing spatial redundancy. Subsequently, its core is an Information Bottleneck-guided Dynamic Token Compression (IB-DTC) module that eliminates the informational redundancy within the foreground. Theoretically grounded in low-rank approximation, this module leverages an online SVD analysis to adaptively compress the redundant foreground into a compact and highly informative set of proxy tokens. Extensive experiments on KITTI, nuScenes and Waymo datasets demonstrate that CompTrack achieves top-performing tracking performance with superior efficiency, running at a real-time 90 FPS on a single RTX 3090 GPU.

