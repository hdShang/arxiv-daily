---
layout: default
title: D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction
---

# D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.25173" target="_blank" class="toolbar-btn">arXiv: 2510.25173v2</a>
    <a href="https://arxiv.org/pdf/2510.25173.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.25173v2" 
            onclick="toggleFavorite(this, '2510.25173v2', 'D$^2$GS: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang

**分类**: cs.CV

**发布日期**: 2025-10-29 (更新: 2025-11-02)

---

## 💡 一句话要点

**提出D$^2$GS以解决无LiDAR城市场景重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市场景重建` `无LiDAR` `高斯喷溅` `深度增强` `自动驾驶` `几何约束` `点云优化`

## 📋 核心要点

1. 现有城市场景重建方法依赖于LiDAR和图像等多模态传感器，获取准确的LiDAR数据面临时空校准和重投影误差等挑战。
2. 本文提出D$^2$GS框架，通过反投影多视角深度预测初始化稠密点云，并利用深度增强器优化高斯几何和深度图。
3. 在Waymo数据集上的实验结果表明，D$^2$GS在几何准确性上超越了现有最先进的方法，展现出优越的性能。

## 📝 摘要（中文）

近年来，高斯喷溅（GS）在自动驾驶城市场景重建中展现出巨大潜力。然而，现有方法通常依赖于多模态传感器输入，如LiDAR和图像。尽管LiDAR点云提供的几何先验可以显著缓解重建中的不适定性，但获取准确的LiDAR数据在实践中仍然具有挑战性。为避免获取准确LiDAR深度的困难，本文提出了D$^2$GS，一个无LiDAR的城市场景重建框架。我们通过反投影多视角度量深度预测初始化稠密点云，并通过渐进修剪策略优化该点云。接着，我们通过深度增强器联合优化高斯几何和预测的稠密度量深度。最后，我们通过约束道路区域内高斯的形状和法线属性来提高地面几何的准确性。大量实验表明，我们的方法在Waymo数据集上始终优于最先进的方法，甚至在与真实LiDAR数据的比较中也表现出更高的几何准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决无LiDAR情况下的城市场景重建问题。现有方法依赖于LiDAR数据，获取这些数据在实践中存在时空校准和重投影误差等困难。

**核心思路**：D$^2$GS框架通过反投影多视角深度预测生成稠密点云，并通过深度增强器优化高斯几何和深度图，从而避免了对LiDAR的依赖。

**技术框架**：该框架主要包括三个阶段：首先，通过反投影生成初始稠密点云；其次，利用渐进修剪策略优化点云的全局一致性；最后，通过深度增强器联合优化高斯几何和深度图。

**关键创新**：最重要的创新在于通过深度增强器引入扩散先验，以增强高斯渲染的深度图，从而提供更强的几何约束。这一方法显著提高了重建的几何准确性。

**关键设计**：在设计中，采用了渐进修剪策略来优化点云，损失函数结合了几何约束和深度增强，网络结构则通过高斯模型与深度增强器的联合优化实现。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在Waymo数据集上的实验结果显示，D$^2$GS在几何重建准确性上超越了最先进的方法，尤其是在与真实LiDAR数据的比较中，表现出更高的几何准确性，提升幅度显著。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、城市规划和虚拟现实等。通过提供高精度的城市场景重建，D$^2$GS能够在无需LiDAR的情况下，支持更广泛的应用场景，降低了对昂贵传感器的依赖，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recently, Gaussian Splatting (GS) has shown great potential for urban scene reconstruction in the field of autonomous driving. However, current urban scene reconstruction methods often depend on multimodal sensors as inputs, \textit{i.e.} LiDAR and images. Though the geometry prior provided by LiDAR point clouds can largely mitigate ill-posedness in reconstruction, acquiring such accurate LiDAR data is still challenging in practice: i) precise spatiotemporal calibration between LiDAR and other sensors is required, as they may not capture data simultaneously; ii) reprojection errors arise from spatial misalignment when LiDAR and cameras are mounted at different locations. To avoid the difficulty of acquiring accurate LiDAR depth, we propose D$^2$GS, a LiDAR-free urban scene reconstruction framework. In this work, we obtain geometry priors that are as effective as LiDAR while being denser and more accurate. $\textbf{First}$, we initialize a dense point cloud by back-projecting multi-view metric depth predictions. This point cloud is then optimized by a Progressive Pruning strategy to improve the global consistency. $\textbf{Second}$, we jointly refine Gaussian geometry and predicted dense metric depth via a Depth Enhancer. Specifically, we leverage diffusion priors from a depth foundation model to enhance the depth maps rendered by Gaussians. In turn, the enhanced depths provide stronger geometric constraints during Gaussian training. $\textbf{Finally}$, we improve the accuracy of ground geometry by constraining the shape and normal attributes of Gaussians within road regions. Extensive experiments on the Waymo dataset demonstrate that our method consistently outperforms state-of-the-art methods, producing more accurate geometry even when compared with those using ground-truth LiDAR data.

