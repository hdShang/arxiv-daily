---
layout: default
title: OmniIndoor3D: Comprehensive Indoor 3D Reconstruction
---

# OmniIndoor3D: Comprehensive Indoor 3D Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20610" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20610v1</a>
  <a href="https://arxiv.org/pdf/2505.20610.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20610v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20610v1', 'OmniIndoor3D: Comprehensive Indoor 3D Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaobao Wei, Xiaoan Zhang, Hao Wang, Qingpo Wuwu, Ming Lu, Wenzhao Zheng, Shanghang Zhang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-05-27

**🔗 代码/项目**: [PROJECT_PAGE](https://ucwxb.github.io/OmniIndoor3D/)

---

## 💡 一句话要点

**提出OmniIndoor3D以解决室内3D重建精度不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `室内3D重建` `高斯表示` `机器人导航` `全景重建` `多层感知机` `RGB-D图像` `噪声降低`

## 📋 核心要点

1. 现有的3D重建方法在室内场景的几何精度上存在不足，影响了全景重建的质量。
2. OmniIndoor3D通过结合RGB-D图像生成粗略3D重建，并利用轻量级MLP优化几何属性，解决了外观与几何的优化冲突。
3. 在多个数据集上的评估显示，OmniIndoor3D在外观、几何和全景重建方面达到了最先进的结果，填补了室内3D重建中的关键空白。

## 📝 摘要（中文）

我们提出了一种新的框架OmniIndoor3D，用于全面的室内3D重建，利用高斯表示法。该框架能够准确重建由消费级RGB-D相机捕获的多样化室内场景的外观、几何和全景信息。由于现有的3DGS方法主要优化于照片级真实感渲染，缺乏高质量全景重建所需的精确几何，因此OmniIndoor3D首先结合多幅RGB-D图像创建粗略的3D重建，随后用于初始化3D高斯并指导3DGS训练。为了解耦外观与几何之间的优化冲突，我们引入了一种轻量级的多层感知机（MLP），调整3D高斯的几何属性。通过联合优化外观、几何和全景重建，OmniIndoor3D提供了全面的室内场景理解，促进了准确和稳健的机器人导航。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有室内3D重建方法在几何精度和全景重建质量上的不足，尤其是3DGS方法在这些方面的局限性。

**核心思路**：OmniIndoor3D的核心思路是结合多幅RGB-D图像生成粗略的3D重建，并通过轻量级MLP调整3D高斯的几何属性，从而实现外观与几何的解耦优化。

**技术框架**：该框架主要包括三个阶段：首先，利用RGB-D图像生成粗略的3D重建；其次，初始化3D高斯并指导3DGS训练；最后，通过联合优化外观、几何和全景重建，获得全面的室内场景理解。

**关键创新**：论文的关键创新在于引入轻量级MLP作为低通滤波器，显著降低室内场景中的噪声，并通过基于全景先验的稠密化策略改善高斯原语的分布。

**关键设计**：在技术细节上，轻量级MLP的设计使得几何属性的调整更加灵活，损失函数的设置则确保了外观与几何的有效优化，整体架构的模块化设计提升了系统的可扩展性。

## 📊 实验亮点

在多个数据集上的实验结果表明，OmniIndoor3D在外观、几何和全景重建方面均达到了最先进的水平，具体性能提升幅度超过了现有方法，尤其在几何精度上有显著改善，验证了其在室内3D重建中的有效性。

## 🎯 应用场景

OmniIndoor3D在室内环境的3D重建中具有广泛的应用潜力，尤其是在机器人导航、虚拟现实和增强现实等领域。其提供的高质量场景理解能够显著提升机器人在复杂环境中的自主导航能力，并为用户提供更真实的沉浸式体验。未来，该技术可能会推动智能家居、智能建筑等领域的发展。

## 📄 摘要（原文）

> We propose a novel framework for comprehensive indoor 3D reconstruction using Gaussian representations, called OmniIndoor3D. This framework enables accurate appearance, geometry, and panoptic reconstruction of diverse indoor scenes captured by a consumer-level RGB-D camera. Since 3DGS is primarily optimized for photorealistic rendering, it lacks the precise geometry critical for high-quality panoptic reconstruction. Therefore, OmniIndoor3D first combines multiple RGB-D images to create a coarse 3D reconstruction, which is then used to initialize the 3D Gaussians and guide the 3DGS training. To decouple the optimization conflict between appearance and geometry, we introduce a lightweight MLP that adjusts the geometric properties of 3D Gaussians. The introduced lightweight MLP serves as a low-pass filter for geometry reconstruction and significantly reduces noise in indoor scenes. To improve the distribution of Gaussian primitives, we propose a densification strategy guided by panoptic priors to encourage smoothness on planar surfaces. Through the joint optimization of appearance, geometry, and panoptic reconstruction, OmniIndoor3D provides comprehensive 3D indoor scene understanding, which facilitates accurate and robust robotic navigation. We perform thorough evaluations across multiple datasets, and OmniIndoor3D achieves state-of-the-art results in appearance, geometry, and panoptic reconstruction. We believe our work bridges a critical gap in indoor 3D reconstruction. The code will be released at: https://ucwxb.github.io/OmniIndoor3D/

