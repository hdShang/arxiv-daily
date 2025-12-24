---
layout: default
title: "GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned Residuals"
---

# GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned Residuals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02141" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02141v1</a>
  <a href="https://arxiv.org/pdf/2509.02141.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02141v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02141v1', 'GRMM: Real-Time High-Fidelity Gaussian Morphable Head Model with Learned Residuals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohit Mendiratta, Mayur Deshmukh, Kartik Teotia, Vladislav Golyanik, Adam Kortylewski, Christian Theobalt

**分类**: cs.GR, cs.CV

**发布日期**: 2025-09-02

**备注**: Project page: https://mohitm1994.github.io/GRMM/

---

## 💡 一句话要点

**GRMM：基于可学习残差的实时高保真高斯可变形头部模型**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D可变形模型` `高斯溅射` `人脸重建` `表情迁移` `实时渲染` `残差学习` `计算机视觉`

## 📋 核心要点

1. 传统基于PCA的3DMM在分辨率、细节和照片真实感方面存在局限性，神经体渲染方法虽然提升了真实感，但速度慢，难以交互。
2. GRMM通过学习残差来增强基础3DMM，从而捕捉高频细节，实现身份和表情的解耦控制，并保持实时渲染性能。
3. GRMM在单目3D人脸重建、新视角合成和表情迁移等任务上，超越了现有技术，实现了更高的保真度和表情准确性。

## 📝 摘要（中文）

本文提出了一种名为GRMM的完整头部高斯3D可变形模型，它通过残差几何和外观分量来增强基础3DMM，这些附加的改进可以恢复高频细节，如皱纹、精细的皮肤纹理和发际线变化。GRMM通过低维、可解释的参数（例如，身份形状、面部表情）提供解耦控制，同时独立地对残差进行建模，以捕捉超出基础模型能力的特定于主体和表情的细节。粗解码器产生顶点级网格变形，精细解码器表示每个高斯的表观，轻量级CNN细化光栅化图像以增强真实感，同时保持75 FPS的实时渲染。为了学习一致的、高保真的残差，我们提出了EXPRESS-50，这是第一个包含50个身份的60个对齐表情的数据集，从而能够在基于高斯的3DMM中实现身份和表情的鲁棒解耦。在单目3D人脸重建、新视角合成和表情迁移方面，GRMM在保真度和表情准确性方面超越了最先进的方法，同时提供交互式实时性能。

## 🔬 方法详解

**问题定义**：现有基于网格的3DMM在捕捉高频细节（如皱纹、皮肤纹理和发际线）方面存在局限性，而神经体渲染方法虽然可以提升真实感，但计算成本高，难以实现实时交互。因此，需要一种既能保持实时渲染性能，又能捕捉高保真细节的头部模型。

**核心思路**：GRMM的核心思路是利用高斯溅射（Gaussian Splatting）的快速渲染能力，并结合传统的3DMM，通过学习残差来弥补3DMM在高频细节上的不足。这种方法既能利用3DMM的参数化控制能力，又能通过残差学习来提升模型的真实感。

**技术框架**：GRMM的整体框架包括以下几个主要模块：1) 基于3DMM的粗糙形状和表情解码器，用于生成初始的头部网格；2) 残差几何解码器，用于在顶点级别上对网格进行变形，以捕捉更精细的几何细节；3) 残差外观解码器，用于调整每个高斯的颜色和不透明度，以捕捉更真实的皮肤纹理；4) 轻量级CNN，用于对光栅化图像进行后处理，进一步提升图像质量。

**关键创新**：GRMM的关键创新在于引入了可学习的残差分量，用于增强基础3DMM。与传统的3DMM相比，GRMM能够捕捉到更多的高频细节，从而实现更高的真实感。此外，GRMM还提出了EXPRESS-50数据集，用于训练具有更好解耦性的高斯3DMM。

**关键设计**：GRMM的关键设计包括：1) 使用高斯溅射作为渲染引擎，以实现实时渲染；2) 设计了残差几何和外观解码器，用于学习高频细节；3) 使用轻量级CNN进行图像后处理，以进一步提升图像质量；4) 提出了EXPRESS-50数据集，包含50个身份的60个对齐表情，用于训练具有更好解耦性的高斯3DMM。损失函数包括重建损失、正则化损失等，用于约束模型的学习。

## 📊 实验亮点

GRMM在多个任务上取得了显著的性能提升。在单目3D人脸重建任务中，GRMM在保真度和表情准确性方面均优于现有方法。在新视角合成和表情迁移任务中，GRMM也表现出更高的真实感和更强的控制能力。此外，GRMM还实现了75 FPS的实时渲染性能，使其能够应用于交互式应用。

## 🎯 应用场景

GRMM具有广泛的应用前景，包括虚拟现实/增强现实（VR/AR）、游戏、动画制作、虚拟化身、视频会议等。它可以用于创建更逼真、更具表现力的虚拟角色，提升用户在虚拟环境中的沉浸感。此外，GRMM还可以用于人脸重建、表情迁移等任务，为相关领域的研究提供新的思路。

## 📄 摘要（原文）

> 3D Morphable Models (3DMMs) enable controllable facial geometry and expression editing for reconstruction, animation, and AR/VR, but traditional PCA-based mesh models are limited in resolution, detail, and photorealism. Neural volumetric methods improve realism but remain too slow for interactive use. Recent Gaussian Splatting (3DGS) based facial models achieve fast, high-quality rendering but still depend solely on a mesh-based 3DMM prior for expression control, limiting their ability to capture fine-grained geometry, expressions, and full-head coverage. We introduce GRMM, the first full-head Gaussian 3D morphable model that augments a base 3DMM with residual geometry and appearance components, additive refinements that recover high-frequency details such as wrinkles, fine skin texture, and hairline variations. GRMM provides disentangled control through low-dimensional, interpretable parameters (e.g., identity shape, facial expressions) while separately modelling residuals that capture subject- and expression-specific detail beyond the base model's capacity. Coarse decoders produce vertex-level mesh deformations, fine decoders represent per-Gaussian appearance, and a lightweight CNN refines rasterised images for enhanced realism, all while maintaining 75 FPS real-time rendering. To learn consistent, high-fidelity residuals, we present EXPRESS-50, the first dataset with 60 aligned expressions across 50 identities, enabling robust disentanglement of identity and expression in Gaussian-based 3DMMs. Across monocular 3D face reconstruction, novel-view synthesis, and expression transfer, GRMM surpasses state-of-the-art methods in fidelity and expression accuracy while delivering interactive real-time performance.

