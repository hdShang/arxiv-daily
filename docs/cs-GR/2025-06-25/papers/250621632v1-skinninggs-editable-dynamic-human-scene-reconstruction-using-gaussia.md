---
layout: default
title: "SkinningGS: Editable Dynamic Human Scene Reconstruction Using Gaussian Splatting Based on a Skinning Model"
---

# SkinningGS: Editable Dynamic Human Scene Reconstruction Using Gaussian Splatting Based on a Skinning Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21632" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21632v1</a>
  <a href="https://arxiv.org/pdf/2506.21632.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21632v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21632v1', 'SkinningGS: Editable Dynamic Human Scene Reconstruction Using Gaussian Splatting Based on a Skinning Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Da Li, Donggang Jia, Markus Hadwiger, Ivan Viola

**分类**: cs.GR

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出SkinningGS以解决动态人类场景重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `动态场景重建` `人类头像重建` `点云解耦` `卷积神经网络` `实时渲染` `高效算法` `动物场景重建`

## 📋 核心要点

1. 现有方法在动态人类场景重建中面临高复杂度和资源消耗的问题，难以实现实时交互。
2. 本研究通过点云解耦和联合优化，结合卷积神经网络，提出了一种高效的动态人类重建方法。
3. 实验结果表明，SkinningGS在重建指标上超越了HUGS，并实现了超过100 FPS的实时渲染，显著提升了性能。

## 📝 摘要（中文）

重建动态人类场景中的交互式人类头像和背景是一项极具挑战性的任务。本研究采用点云解耦和联合优化策略，实现了背景和人类身体的解耦重建，同时保持人类运动的交互性。我们引入位置纹理来细分Skinned Multi-Person Linear (SMPL)身体模型的表面，并扩展人类点云。为捕捉人类动态和变形的细节，我们结合卷积神经网络结构，根据纹理预测人类身体点云特征。该策略使我们的方法在密集化时无需超参数调优，并有效地用一半的点云表示人类点。我们的方案在重建质量上超越了现有的HUGS，并能泛化到新姿态和视角。此外，该技术在仅使用线性混合蒙皮权重进行人类变换时，实现了超过100 FPS的实时渲染，速度约为HUGS的6倍。该框架还可扩展至动物场景重建。

## 🔬 方法详解

**问题定义**：本论文旨在解决从单目视频中重建动态人类场景的挑战，现有方法在处理复杂动态和实时交互时存在性能瓶颈和资源消耗过高的问题。

**核心思路**：我们提出了一种点云解耦和联合优化的策略，通过引入位置纹理细分SMPL模型表面，来有效捕捉人类动态和变形特征。

**技术框架**：整体架构包括点云解耦模块、纹理细分模块和卷积神经网络模块。首先进行背景和人类身体的解耦重建，然后利用CNN预测人类身体的点云特征，最后实现高效的动态重建。

**关键创新**：本研究的主要创新在于通过位置纹理的引入和CNN的结合，使得重建过程无需超参数调优，同时在点云密度上显著降低，提升了重建质量和效率。

**关键设计**：在网络结构上，我们设计了特定的卷积层来提取纹理特征，并使用线性混合蒙皮权重进行人类变换，确保了高效的实时渲染和较低的GPU资源消耗。

## 📊 实验亮点

实验结果显示，SkinningGS在重建指标上超越了HUGS，且在实时渲染方面达到了超过100 FPS的性能，速度约为HUGS的6倍。这一显著提升展示了该方法在动态人类场景重建中的优越性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发和动画制作等，能够为动态人类场景的实时重建提供高效解决方案。此外，框架的扩展性使其在动物场景重建等其他领域也具备应用价值，推动相关技术的发展。

## 📄 摘要（原文）

> Reconstructing an interactive human avatar and the background from a monocular video of a dynamic human scene is highly challenging. In this work we adopt a strategy of point cloud decoupling and joint optimization to achieve the decoupled reconstruction of backgrounds and human bodies while preserving the interactivity of human motion. We introduce a position texture to subdivide the Skinned Multi-Person Linear (SMPL) body model's surface and grow the human point cloud. To capture fine details of human dynamics and deformations, we incorporate a convolutional neural network structure to predict human body point cloud features based on texture. This strategy makes our approach free of hyperparameter tuning for densification and efficiently represents human points with half the point cloud of HUGS. This approach ensures high-quality human reconstruction and reduces GPU resource consumption during training. As a result, our method surpasses the previous state-of-the-art HUGS in reconstruction metrics while maintaining the ability to generalize to novel poses and views. Furthermore, our technique achieves real-time rendering at over 100 FPS, $\sim$6$\times$ the HUGS speed using only Linear Blend Skinning (LBS) weights for human transformation. Additionally, this work demonstrates that this framework can be extended to animal scene reconstruction when an accurately-posed model of an animal is available.

