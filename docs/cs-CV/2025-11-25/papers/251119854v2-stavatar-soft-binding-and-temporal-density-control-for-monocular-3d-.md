---
layout: default
title: STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction
---

# STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19854" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19854v2</a>
  <a href="https://arxiv.org/pdf/2511.19854.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19854v2" onclick="toggleFavorite(this, '2511.19854v2', 'STAvatar: Soft Binding and Temporal Density Control for Monocular 3D Head Avatars Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiankuo Zhao, Xiangyu Zhu, Zidu Wang, Zhen Lei

**分类**: cs.CV

**发布日期**: 2025-11-25 (更新: 2025-11-27)

**备注**: 17 pages, 14 figures

---

## 💡 一句话要点

**STAvatar：提出软绑定与时序密度控制的单目3D头部Avatar重建方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D头部Avatar重建` `单目视频` `高斯溅射` `软绑定` `时序密度控制`

## 📋 核心要点

1. 现有3D头部Avatar重建方法在处理复杂形变和遮挡区域时存在不足，限制了重建质量和表达能力。
2. STAvatar通过UV自适应软绑定和时序密度控制，增强了对形状、纹理变化以及遮挡区域的适应性。
3. 实验表明，STAvatar在精细细节捕捉和遮挡区域重建方面优于现有方法，实现了最先进的性能。

## 📝 摘要（中文）

本文提出了一种名为STAvatar的方法，用于从单目视频中重建高保真且可动画的3D头部Avatar。现有基于3D高斯溅射的方法通常将高斯绑定到网格三角形，并仅通过线性混合蒙皮来建模形变，导致运动僵硬和表达能力有限。此外，它们缺乏处理频繁遮挡区域（如口腔内部、眼睑）的专门策略。为了解决这些限制，STAvatar包含两个关键组件：（1）UV自适应软绑定框架，利用基于图像和几何先验来学习UV空间中每个高斯特征的偏移量。这种UV表示支持动态重采样，确保与自适应密度控制（ADC）的完全兼容，并增强对形状和纹理变化的适应性。（2）时序ADC策略，首先对结构相似的帧进行聚类，以促进更有针对性地计算密度化标准。它进一步引入了一种新的融合感知误差作为克隆标准，以共同捕获几何和纹理差异，鼓励在需要更精细细节的区域进行密度化。在四个基准数据集上的大量实验表明，STAvatar实现了最先进的重建性能，尤其是在捕获精细细节和重建频繁遮挡区域方面。代码将公开。

## 🔬 方法详解

**问题定义**：现有基于3D高斯溅射的头部Avatar重建方法，主要依赖于将高斯基元绑定到mesh网格上，并使用线性混合蒙皮（Linear Blend Skinning, LBS）来建模形变。这种方法的局限性在于LBS难以捕捉复杂的非刚性形变，例如面部表情中的细微变化。此外，频繁被遮挡的区域（如口腔内部、眼睑等）由于缺乏足够的可见信息，重建效果往往不佳。

**核心思路**：STAvatar的核心思路是通过引入UV自适应软绑定和时序密度控制，来提升模型对复杂形变和遮挡区域的处理能力。UV自适应软绑定允许高斯基元在UV空间中进行动态调整，从而更好地适应形状和纹理的变化。时序密度控制则通过分析视频帧之间的结构相似性，并结合几何和纹理误差，有针对性地在高斯基元稀疏的区域进行密度化，从而提升重建质量。

**技术框架**：STAvatar的整体框架包含以下几个主要阶段：1. **UV自适应软绑定**：利用图像和几何先验，学习每个高斯基元在UV空间中的特征偏移量。2. **动态重采样**：基于UV表示，对高斯基元进行动态重采样，以适应形状和纹理的变化。3. **时序自适应密度控制**：对结构相似的帧进行聚类，并基于融合感知误差，在高斯基元稀疏的区域进行密度化。4. **渲染**：使用优化后的高斯基元进行渲染，生成最终的3D头部Avatar。

**关键创新**：STAvatar的关键创新在于以下两点：1. **UV自适应软绑定**：通过在UV空间中学习高斯基元的特征偏移量，实现了对复杂形变的更精细建模，克服了LBS的局限性。2. **时序自适应密度控制**：通过分析视频帧之间的结构相似性，并结合几何和纹理误差，实现了对高斯基元密度更有效的控制，提升了遮挡区域的重建质量。

**关键设计**：在UV自适应软绑定中，使用了基于图像和几何先验的损失函数来约束UV偏移量的学习。在时序自适应密度控制中，采用了K-means聚类算法对视频帧进行聚类，并使用融合感知误差（包括几何误差和纹理误差）作为克隆标准。此外，还引入了动态重采样策略，以确保高斯基元的密度与形状和纹理的变化相匹配。

## 📊 实验亮点

STAvatar在四个基准数据集上进行了广泛的实验，结果表明其在重建性能上达到了最先进水平。尤其是在捕捉精细细节和重建频繁遮挡区域方面，STAvatar相比现有方法有显著提升。具体的性能数据和对比基线将在论文中详细展示。

## 🎯 应用场景

STAvatar技术可应用于虚拟现实、增强现实、数字人、游戏开发等领域，为用户提供更逼真、更具表现力的3D头部Avatar。该技术能够提升远程会议、虚拟社交、个性化内容创作等应用的用户体验，并为未来的元宇宙应用奠定基础。

## 📄 摘要（原文）

> Reconstructing high-fidelity and animatable 3D head avatars from monocular videos remains a challenging yet essential task. Existing methods based on 3D Gaussian Splatting typically bind Gaussians to mesh triangles and model deformations solely via Linear Blend Skinning, which results in rigid motion and limited expressiveness. Moreover, they lack specialized strategies to handle frequently occluded regions (e.g., mouth interiors, eyelids). To address these limitations, we propose STAvatar, which consists of two key components: (1) a UV-Adaptive Soft Binding framework that leverages both image-based and geometric priors to learn per-Gaussian feature offsets within the UV space. This UV representation supports dynamic resampling, ensuring full compatibility with Adaptive Density Control (ADC) and enhanced adaptability to shape and textural variations. (2) a Temporal ADC strategy, which first clusters structurally similar frames to facilitate more targeted computation of the densification criterion. It further introduces a novel fused perceptual error as clone criterion to jointly capture geometric and textural discrepancies, encouraging densification in regions requiring finer details. Extensive experiments on four benchmark datasets demonstrate that STAvatar achieves state-of-the-art reconstruction performance, especially in capturing fine-grained details and reconstructing frequently occluded regions. The code will be publicly available.

