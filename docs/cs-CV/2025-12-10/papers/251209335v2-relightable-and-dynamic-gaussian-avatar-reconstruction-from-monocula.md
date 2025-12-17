---
layout: default
title: Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video
---

# Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.09335" class="toolbar-btn" target="_blank">📄 arXiv: 2512.09335v2</a>
  <a href="https://arxiv.org/pdf/2512.09335.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.09335v2" onclick="toggleFavorite(this, '2512.09335v2', 'Relightable and Dynamic Gaussian Avatar Reconstruction from Monocular Video')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seonghwa Choi, Moonkyeong Choi, Mingyu Jang, Jaekyung Kim, Jianfei Cai, Wen-Huang Cheng, Sanghoon Lee

**分类**: cs.CV, cs.MM

**发布日期**: 2025-12-10 (更新: 2025-12-11)

**备注**: 8 pages, 9 figures, published in ACM MM 2025

**期刊**: In Proceedings of the 33rd ACM International Conference on Multimedia. 2025. p. 7405-7414

**DOI**: [10.1145/3746027.3754851](https://doi.org/10.1145/3746027.3754851)

---

## 💡 一句话要点

**提出RnD-Avatar，基于3DGS重建可重光照和动态人体Avatar，提升几何细节。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `人体Avatar重建` `3D高斯溅射` `动态蒙皮权重` `可重光照` `神经渲染`

## 📋 核心要点

1. 现有NeRF和3DGS方法在重建人体Avatar时，由于身体运动（如衣物褶皱）相关的几何细节不足，难以产生令人满意的逼真效果。
2. RnD-Avatar通过引入动态蒙皮权重，定义基于姿势的Avatar关节运动，并学习身体运动引起的额外形变，从而实现高保真几何细节的精确姿势变化形变。
3. 论文提出了新的多视角数据集，包含不同的光照条件，用于评估重光照效果。实验表明，该方法在新视角合成、新姿势渲染和重光照方面均达到SOTA。

## 📝 摘要（中文）

本文提出了一种基于3D高斯溅射(3DGS)的人体Avatar建模框架，名为可重光照和动态高斯Avatar (RnD-Avatar)，它能够为高保真几何细节呈现精确的姿势变化形变。为了实现这一目标，我们引入了动态蒙皮权重，该权重定义了基于姿势的人体Avatar的关节运动，同时学习由身体运动引起的额外形变。我们还引入了一种新的正则化方法，以在稀疏视觉线索下捕获精细的几何细节。此外，我们提出了一个新的具有不同光照条件的多视角数据集来评估重光照。我们的框架能够真实地渲染新的姿势和视角，同时支持在任意光照条件下实现照片般逼真的光照效果。我们的方法在新的视角合成、新的姿势渲染和重光照方面实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有基于NeRF和3DGS的人体Avatar重建方法，在处理复杂身体运动（例如衣物褶皱）时，难以捕捉到足够的几何细节，导致渲染效果不够逼真。尤其是在光照变化的情况下，重建质量会进一步下降。因此，需要一种能够更精确地建模人体动态形变和光照效果的方法。

**核心思路**：RnD-Avatar的核心思路是利用3D高斯溅射(3DGS)作为基础表示，并引入动态蒙皮权重来建模人体Avatar的关节运动和形变。通过学习额外的形变场来捕捉身体运动引起的细节变化，并结合新的正则化方法，在稀疏视觉线索下也能重建出精细的几何结构。同时，考虑光照变化，使重建的Avatar具有可重光照的能力。

**技术框架**：RnD-Avatar的整体框架包括以下几个主要模块：1) 3DGS初始化：使用多视角视频数据初始化3D高斯分布。2) 动态蒙皮权重学习：学习动态蒙皮权重，用于定义基于姿势的人体Avatar的关节运动。3) 形变场学习：学习额外的形变场，用于捕捉身体运动引起的细节变化。4) 光照建模：对场景光照进行建模，使Avatar具有可重光照的能力。5) 渲染：使用渲染方程将3D高斯分布投影到2D图像上，并进行优化。

**关键创新**：RnD-Avatar的关键创新点在于：1) 引入了动态蒙皮权重，能够更精确地建模人体Avatar的关节运动和形变。2) 提出了新的正则化方法，能够在稀疏视觉线索下捕获精细的几何细节。3) 构建了一个新的多视角数据集，包含不同的光照条件，用于评估重光照效果。

**关键设计**：在动态蒙皮权重学习中，使用了神经网络来预测每个3D高斯点的蒙皮权重，该网络以姿势参数作为输入。在形变场学习中，使用了另一个神经网络来预测每个3D高斯点的形变向量，该网络以姿势参数和3D坐标作为输入。损失函数包括重建损失、正则化损失和光照一致性损失。重建损失用于保证重建的图像与原始图像一致。正则化损失用于约束形变场的平滑性。光照一致性损失用于保证在不同光照条件下，重建的Avatar的光照效果一致。

## 📊 实验亮点

实验结果表明，RnD-Avatar在新的视角合成、新的姿势渲染和重光照方面均取得了state-of-the-art的性能。与现有方法相比，RnD-Avatar能够重建出更加精细的几何细节，并具有更好的光照效果。在定量评估方面，RnD-Avatar在PSNR、SSIM和LPIPS等指标上均优于其他方法。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、游戏开发、电影制作等领域。例如，可以创建高度逼真的虚拟化身，用于社交互动、远程协作和娱乐。此外，该技术还可以用于服装设计和虚拟试穿，帮助用户更好地了解服装的穿着效果。未来，该技术有望进一步发展，实现更加智能化和个性化的Avatar重建。

## 📄 摘要（原文）

> Modeling relightable and animatable human avatars from monocular video is a long-standing and challenging task. Recently, Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) methods have been employed to reconstruct the avatars. However, they often produce unsatisfactory photo-realistic results because of insufficient geometrical details related to body motion, such as clothing wrinkles. In this paper, we propose a 3DGS-based human avatar modeling framework, termed as Relightable and Dynamic Gaussian Avatar (RnD-Avatar), that presents accurate pose-variant deformation for high-fidelity geometrical details. To achieve this, we introduce dynamic skinning weights that define the human avatar's articulation based on pose while also learning additional deformations induced by body motion. We also introduce a novel regularization to capture fine geometric details under sparse visual cues. Furthermore, we present a new multi-view dataset with varied lighting conditions to evaluate relight. Our framework enables realistic rendering of novel poses and views while supporting photo-realistic lighting effects under arbitrary lighting conditions. Our method achieves state-of-the-art performance in novel view synthesis, novel pose rendering, and relighting.

