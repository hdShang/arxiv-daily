---
layout: default
title: "GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction"
---

# GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02126" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02126v2</a>
  <a href="https://arxiv.org/pdf/2505.02126.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02126v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02126v2', 'GarmentGS: Point-Cloud Guided Gaussian Splatting for High-Fidelity Non-Watertight 3D Garment Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Tang, Shenghao Yang, Hongtao Zhang, Mingbo Zhao

**分类**: cs.CV

**发布日期**: 2025-05-04 (更新: 2025-05-14)

**备注**: Accepted by ICMR 2025

---

## 💡 一句话要点

**提出GarmentGS以解决高保真非密闭3D服装重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D服装重建` `高斯点云` `密集点云` `几何精度` `实时渲染`

## 📋 核心要点

1. 现有的3D服装重建方法通常需要大量的手动操作，效率低下且成本高。
2. GarmentGS方法通过密集点云引导高斯原语的运动和分布，显著提高了重建精度和效率。
3. 实验结果表明，GarmentGS在10分钟内完成点云重建，并实现了实时渲染，质量与传统方法相当。

## 📝 摘要（中文）

传统的3D服装创建需要大量人工操作，导致时间和劳动成本高昂。最近，3D高斯点云技术在3D场景重建和渲染方面取得了突破性进展，吸引了广泛关注，并为3D服装重建开辟了新路径。然而，由于高斯原语的非结构化和不规则特性，重建高保真、非密闭的3D服装仍然具有挑战性。本文提出了GarmentGS，一种密集点云引导的方法，能够以高几何精度重建高保真服装表面，并生成非密闭的单层网格。我们的快速密集点云重建模块可以在10分钟内完成服装点云重建，而传统方法通常需要数小时。此外，我们利用密集点云引导高斯原语的移动、展平和旋转，从而在服装表面实现更好的分布，以获得更优的渲染效果和几何精度。通过数值和视觉比较，我们的方法实现了快速训练和实时渲染，同时保持了竞争力的质量。

## 🔬 方法详解

**问题定义**：本文旨在解决高保真非密闭3D服装重建中的效率和精度问题。现有方法由于高斯原语的非结构化特性，难以实现高质量的重建。

**核心思路**：GarmentGS通过密集点云引导高斯原语的运动、展平和旋转，从而优化其在服装表面上的分布，以提高几何精度和渲染效果。

**技术框架**：该方法包括快速密集点云重建模块和高斯原语引导模块。前者负责在短时间内生成高质量的点云，后者则利用点云信息优化高斯原语的分布。

**关键创新**：GarmentGS的主要创新在于结合密集点云与高斯原语的动态调整，显著提升了重建质量和效率，与传统方法相比，减少了重建时间并提高了几何精度。

**关键设计**：在技术细节上，采用了特定的损失函数来优化高斯原语的分布，并设计了高效的网络结构以支持快速训练和实时渲染。

## 📊 实验亮点

实验结果显示，GarmentGS在10分钟内完成点云重建，相较于传统方法的数小时大幅提升效率。同时，该方法在渲染质量和几何精度上与现有技术保持竞争力，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究在虚拟服装设计、游戏开发和影视特效等领域具有广泛的应用潜力。通过提高3D服装重建的效率和质量，GarmentGS能够为设计师提供更高效的工具，推动相关行业的发展。未来，该技术可能会进一步应用于个性化定制和在线购物体验的提升。

## 📄 摘要（原文）

> Traditional 3D garment creation requires extensive manual operations, resulting in time and labor costs. Recently, 3D Gaussian Splatting has achieved breakthrough progress in 3D scene reconstruction and rendering, attracting widespread attention and opening new pathways for 3D garment reconstruction. However, due to the unstructured and irregular nature of Gaussian primitives, it is difficult to reconstruct high-fidelity, non-watertight 3D garments. In this paper, we present GarmentGS, a dense point cloud-guided method that can reconstruct high-fidelity garment surfaces with high geometric accuracy and generate non-watertight, single-layer meshes. Our method introduces a fast dense point cloud reconstruction module that can complete garment point cloud reconstruction in 10 minutes, compared to traditional methods that require several hours. Furthermore, we use dense point clouds to guide the movement, flattening, and rotation of Gaussian primitives, enabling better distribution on the garment surface to achieve superior rendering effects and geometric accuracy. Through numerical and visual comparisons, our method achieves fast training and real-time rendering while maintaining competitive quality.

