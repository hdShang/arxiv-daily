---
layout: default
title: "iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion"
---

# iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14149" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14149v1</a>
  <a href="https://arxiv.org/pdf/2511.14149.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14149v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14149v1', 'iGaussian: Real-Time Camera Pose Estimation via Feed-Forward 3D Gaussian Splatting Inversion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Wang, Linqing Zhao, Xiuwei Xu, Jiwen Lu, Haibin Yan

**分类**: cs.CV

**发布日期**: 2025-11-18

**备注**: IROS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/pythongod-exe/iGaussian)

---

## 💡 一句话要点

**提出iGaussian以解决实时相机位姿估计问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `相机位姿估计` `3D高斯` `实时处理` `深度学习` `视觉导航` `SLAM` `特征匹配`

## 📋 核心要点

1. 现有方法通常依赖于迭代的渲染-比较-优化循环，导致计算开销大，难以实现实时性能。
2. 提出的iGaussian框架通过直接的3D高斯反演实现相机位姿的快速估计，采用了空间均匀采样和引导注意机制。
3. 在多个数据集上的实验结果显示，iGaussian显著降低了旋转误差并提升了跟踪速度，具有良好的实时性能。

## 📝 摘要（中文）

近年来，SLAM和视觉导航领域逐渐采用3D高斯作为场景表示，强调从单幅图像中估计相机位姿的重要性。然而，现有方法通常依赖于迭代的渲染-比较-优化循环，这一过程计算开销大，难以实现实时性能。本文提出了iGaussian，一个两阶段的前馈框架，通过直接的3D高斯反演实现实时相机位姿估计。该方法首先利用基于高斯场景先验的位姿回归网络回归粗略的6DoF位姿，然后通过特征匹配和多模型融合进行精细化。实验结果表明，iGaussian在多个数据集上显著提升了性能，旋转误差中位数降至0.2°，在移动机器人上实现了2.87 FPS的跟踪速度，相较于基于优化的方法提升了10倍。

## 🔬 方法详解

**问题定义**：本文旨在解决从单幅图像中实时估计相机位姿的问题。现有方法依赖于迭代的渲染-比较-优化流程，导致计算效率低下，无法满足实时应用的需求。

**核心思路**：iGaussian框架通过直接的3D高斯反演来实现相机位姿的快速估计，避免了传统方法中的多轮迭代过程，从而提高了计算效率。

**技术框架**：该方法分为两个阶段：第一阶段使用高斯场景先验的位姿回归网络进行粗略位姿回归，第二阶段通过特征匹配和多模型融合进行精细化。主要模块包括空间均匀采样、引导注意机制和交叉相关模块。

**关键创新**：最重要的创新在于交叉相关模块，它能够在没有可微分渲染的情况下对图像嵌入与3D高斯属性进行对齐，同时引入加权多视图预测器，融合来自多个战略采样视点的特征。

**关键设计**：在网络结构上，采用了空间均匀采样和引导注意机制来提高位姿回归的准确性，损失函数设计上则注重于减少旋转误差，确保模型在不同视角下的鲁棒性。

## 📊 实验亮点

实验结果表明，iGaussian在NeRF Synthetic、Mip-NeRF 360和T&T+DB数据集上显著提升了性能，旋转误差中位数降至0.2°，在移动机器人上实现了2.87 FPS的跟踪速度，相较于传统优化方法提升了10倍，展示了其在实时应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、增强现实和无人驾驶等场景。通过实现实时的相机位姿估计，iGaussian能够显著提升这些领域的系统性能和用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Recent trends in SLAM and visual navigation have embraced 3D Gaussians as the preferred scene representation, highlighting the importance of estimating camera poses from a single image using a pre-built Gaussian model. However, existing approaches typically rely on an iterative \textit{render-compare-refine} loop, where candidate views are first rendered using NeRF or Gaussian Splatting, then compared against the target image, and finally, discrepancies are used to update the pose. This multi-round process incurs significant computational overhead, hindering real-time performance in robotics. In this paper, we propose iGaussian, a two-stage feed-forward framework that achieves real-time camera pose estimation through direct 3D Gaussian inversion. Our method first regresses a coarse 6DoF pose using a Gaussian Scene Prior-based Pose Regression Network with spatial uniform sampling and guided attention mechanisms, then refines it through feature matching and multi-model fusion. The key contribution lies in our cross-correlation module that aligns image embeddings with 3D Gaussian attributes without differentiable rendering, coupled with a Weighted Multiview Predictor that fuses features from Multiple strategically sampled viewpoints. Experimental results on the NeRF Synthetic, Mip-NeRF 360, and T\&T+DB datasets demonstrate a significant performance improvement over previous methods, reducing median rotation errors to 0.2° while achieving 2.87 FPS tracking on mobile robots, which is an impressive 10 times speedup compared to optimization-based approaches. Code: https://github.com/pythongod-exe/iGaussian

