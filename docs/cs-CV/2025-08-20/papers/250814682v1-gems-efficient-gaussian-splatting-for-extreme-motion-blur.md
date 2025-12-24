---
layout: default
title: "GeMS: Efficient Gaussian Splatting for Extreme Motion Blur"
---

# GeMS: Efficient Gaussian Splatting for Extreme Motion Blur

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14682" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14682v1</a>
  <a href="https://arxiv.org/pdf/2508.14682.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14682v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14682v1', 'GeMS: Efficient Gaussian Splatting for Extreme Motion Blur')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gopi Raju Matta, Trisha Reddypalli, Vemunuri Divya Madhuri, Kaushik Mitra

**分类**: cs.CV

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出GeMS框架以解决极端运动模糊问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `运动模糊` `3D重建` `高斯点云` `深度学习` `计算机视觉` `去模糊` `结构从运动` `事件驱动`

## 📋 核心要点

1. 现有去模糊方法通常依赖于清晰图像进行相机姿态估计，无法处理极端运动模糊。
2. GeMS框架直接从模糊图像重建场景，集成了深度学习运动结构估计和稳健的初始化方法。
3. GeMS和GeMS-E在合成和真实数据集上表现出色，达到了当前最先进的性能水平。

## 📝 摘要（中文）

我们提出了GeMS，一个用于3D高斯点云重建的框架，旨在处理严重运动模糊的图像。现有的去模糊方法通常假设可以获取清晰图像用于相机姿态估计和点云生成，这在极端模糊情况下并不现实。GeMS通过直接从模糊图像重建场景，集成了基于深度学习的运动结构估计、稳健的场景初始化和相机轨迹与高斯参数的联合优化。为进一步提高重建质量，GeMS-E引入了事件驱动的双重积分去模糊步骤，显著改善了姿态估计和点云生成。GeMS和GeMS-E在合成和真实数据集上均达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本论文旨在解决从严重运动模糊图像中重建3D场景的问题。现有方法如ExBluRF和Deblur-GS通常依赖于清晰图像进行相机姿态估计和点云生成，这在极端模糊情况下是不切实际的。

**核心思路**：GeMS框架通过直接从模糊图像重建场景，避免了对清晰图像的依赖。其核心思想是利用深度学习技术和概率分布来处理模糊图像中的信息，从而实现稳健的重建。

**技术框架**：GeMS的整体架构包括三个主要模块：VGGSfM用于从模糊输入中估计姿态和生成点云；3DGS-MCMC用于稳健的场景初始化；以及相机轨迹与高斯参数的联合优化。GeMS-E进一步集成了事件驱动的去模糊步骤，以提高重建质量。

**关键创新**：GeMS是首个直接从严重模糊输入中处理极端运动模糊的3D高斯点云重建框架。其创新之处在于通过概率分布处理高斯样本，消除了传统方法中的启发式密集化和修剪步骤。

**关键设计**：在技术细节上，GeMS采用了深度学习模型进行运动结构估计，结合了事件驱动的双重积分去模糊方法，以提高图像清晰度和重建精度。

## 📊 实验亮点

在实验中，GeMS和GeMS-E在合成和真实数据集上均表现出色，达到了当前最先进的性能水平。具体而言，GeMS在处理极端模糊图像时，相较于基线方法提升了重建精度，展示了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、机器人导航和增强现实等。GeMS框架能够在极端运动模糊条件下实现高质量的3D重建，具有重要的实际价值，能够提升相关领域的技术水平和应用效果。

## 📄 摘要（原文）

> We introduce GeMS, a framework for 3D Gaussian Splatting (3DGS) designed to handle severely motion-blurred images. State-of-the-art deblurring methods for extreme blur, such as ExBluRF, as well as Gaussian Splatting-based approaches like Deblur-GS, typically assume access to sharp images for camera pose estimation and point cloud generation, an unrealistic assumption. Methods relying on COLMAP initialization, such as BAD-Gaussians, also fail due to unreliable feature correspondences under severe blur. To address these challenges, we propose GeMS, a 3DGS framework that reconstructs scenes directly from extremely blurred images. GeMS integrates: (1) VGGSfM, a deep learning-based Structure-from-Motion pipeline that estimates poses and generates point clouds directly from blurred inputs; (2) 3DGS-MCMC, which enables robust scene initialization by treating Gaussians as samples from a probability distribution, eliminating heuristic densification and pruning; and (3) joint optimization of camera trajectories and Gaussian parameters for stable reconstruction. While this pipeline produces strong results, inaccuracies may remain when all inputs are severely blurred. To mitigate this, we propose GeMS-E, which integrates a progressive refinement step using events: (4) Event-based Double Integral (EDI) deblurring restores sharper images that are then fed into GeMS, improving pose estimation, point cloud generation, and overall reconstruction. Both GeMS and GeMS-E achieve state-of-the-art performance on synthetic and real-world datasets. To our knowledge, this is the first framework to address extreme motion blur within 3DGS directly from severely blurred inputs.

