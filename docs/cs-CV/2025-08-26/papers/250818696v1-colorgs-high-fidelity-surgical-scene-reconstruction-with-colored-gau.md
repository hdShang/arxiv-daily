---
layout: default
title: "ColorGS: High-fidelity Surgical Scene Reconstruction with Colored Gaussian Splatting"
---

# ColorGS: High-fidelity Surgical Scene Reconstruction with Colored Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18696" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18696v1</a>
  <a href="https://arxiv.org/pdf/2508.18696.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18696v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18696v1', 'ColorGS: High-fidelity Surgical Scene Reconstruction with Colored Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qun Ji, Peng Li, Mingqiang Wei

**分类**: cs.CV

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出ColorGS以解决内窥镜视频中组织重建的色彩与变形建模问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `内窥镜视频` `可变形组织` `高保真重建` `增强变形模型` `动态锚点` `色彩编码` `实时渲染` `手术导航`

## 📋 核心要点

1. 现有方法在重建可变形组织时难以捕捉细微的色彩变化和全局变形，导致重建效果不理想。
2. ColorGS框架通过Colored Gaussian Primitives和增强变形模型，提升了色彩表达能力和变形建模的精确性。
3. 在DaVinci机器人手术视频和多个基准数据集上，ColorGS实现了39.85的PSNR和97.25%的SSIM，显著优于现有方法。

## 📝 摘要（中文）

高保真重建可变形组织的内窥镜视频仍然面临挑战，现有方法在捕捉细微色彩变化和建模全局变形方面存在局限。为此，本文提出ColorGS框架，结合空间自适应色彩编码和增强变形建模。通过引入动态锚点和可学习色彩参数的Colored Gaussian Primitives，显著提高了复杂光照和组织相似性下的色彩表现力。同时，设计了增强变形模型(EDM)，结合时间感知的高斯基函数与可学习的时间独立变形，精确捕捉局部组织变形和手术交互引起的全局运动一致性。实验表明，ColorGS在DaVinci机器人手术视频和基准数据集上表现优异，PSNR达到39.85，比之前的3DGS方法提高1.5，SSIM为97.25%，同时保持实时渲染效率。

## 🔬 方法详解

**问题定义**：本文旨在解决内窥镜视频中可变形组织的高保真重建问题。现有方法在捕捉细微色彩变化和全局变形建模方面存在不足，导致重建效果不佳。

**核心思路**：ColorGS框架通过引入动态锚点和可学习色彩参数的Colored Gaussian Primitives，适应性地编码空间变化的纹理，从而提升色彩表现力。同时，采用增强变形模型(EDM)来精确捕捉组织的局部变形和全局运动一致性。

**技术框架**：ColorGS的整体架构包括两个主要模块：Colored Gaussian Primitives和增强变形模型。前者负责色彩编码，后者则处理变形建模。整个流程通过动态学习和时间感知的高斯基函数实现。

**关键创新**：ColorGS的核心创新在于Colored Gaussian Primitives的设计，允许动态调整色彩参数以适应复杂的光照和组织特性。这一方法与传统的固定色彩分配方式有本质区别，显著提升了重建的色彩准确性。

**关键设计**：在技术细节上，ColorGS使用了可学习的时间独立变形参数，并结合时间感知的高斯基函数，以实现对组织变形的精确建模。损失函数的设计也经过优化，以确保在训练过程中能够有效捕捉到细微的色彩变化和全局一致性。

## 📊 实验亮点

ColorGS在实验中表现出色，PSNR达到39.85，比之前的3DGS方法提高1.5，SSIM达到97.25%。这些结果表明，ColorGS在高保真重建和实时渲染效率方面均优于现有技术，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在手术导航和增强现实/虚拟现实(AR/VR)领域。通过提供高保真的手术场景重建，ColorGS能够为外科医生提供更准确的视觉信息，提升手术安全性和效率。此外，该技术也可扩展到其他医疗影像处理和分析任务中，推动相关领域的发展。

## 📄 摘要（原文）

> High-fidelity reconstruction of deformable tissues from endoscopic videos remains challenging due to the limitations of existing methods in capturing subtle color variations and modeling global deformations. While 3D Gaussian Splatting (3DGS) enables efficient dynamic reconstruction, its fixed per-Gaussian color assignment struggles with intricate textures, and linear deformation modeling fails to model consistent global deformation. To address these issues, we propose ColorGS, a novel framework that integrates spatially adaptive color encoding and enhanced deformation modeling for surgical scene reconstruction. First, we introduce Colored Gaussian Primitives, which employ dynamic anchors with learnable color parameters to adaptively encode spatially varying textures, significantly improving color expressiveness under complex lighting and tissue similarity. Second, we design an Enhanced Deformation Model (EDM) that combines time-aware Gaussian basis functions with learnable time-independent deformations, enabling precise capture of both localized tissue deformations and global motion consistency caused by surgical interactions. Extensive experiments on DaVinci robotic surgery videos and benchmark datasets (EndoNeRF, StereoMIS) demonstrate that ColorGS achieves state-of-the-art performance, attaining a PSNR of 39.85 (1.5 higher than prior 3DGS-based methods) and superior SSIM (97.25\%) while maintaining real-time rendering efficiency. Our work advances surgical scene reconstruction by balancing high fidelity with computational practicality, critical for intraoperative guidance and AR/VR applications.

