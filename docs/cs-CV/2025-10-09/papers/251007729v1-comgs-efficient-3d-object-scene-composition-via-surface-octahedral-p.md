---
layout: default
title: ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes
---

# ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.07729" class="toolbar-btn" target="_blank">📄 arXiv: 2510.07729v1</a>
  <a href="https://arxiv.org/pdf/2510.07729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07729v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.07729v1', 'ComGS: Efficient 3D Object-Scene Composition via Surface Octahedral Probes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Gao, Mengqi Yuan, Yifei Zeng, Chang Zeng, Zhihao Li, Zhenyu Chen, Weichao Qiu, Xiao-Xiao Long, Hao Zhu, Xun Cao, Yao Yao

**分类**: cs.CV

**发布日期**: 2025-10-09

**🔗 代码/项目**: [PROJECT_PAGE](https://nju-3dv.github.io/projects/)

---

## 💡 一句话要点

**ComGS：通过表面八面体探针实现高效的3D物体-场景合成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D物体合成` `场景合成` `Gaussian Splatting` `表面八面体探针` `光照估计`

## 📋 核心要点

1. 现有Gaussian Splatting方法在3D物体-场景合成中，由于烘焙的光照信息导致合成结果不一致，需要可重新光照的物体重建和场景光照估计。
2. ComGS通过引入表面八面体探针(SOPs)存储光照信息，避免昂贵的光线追踪，加速物体重建和阴影计算，并利用扩散模型完成局部光照估计。
3. ComGS实现了高质量的实时渲染（约28 FPS），生成具有生动阴影的和谐结果，编辑时间仅需36秒，显著提升了3D物体-场景合成的效率和质量。

## 📝 摘要（中文）

Gaussian Splatting (GS) 实现了沉浸式渲染，但逼真的3D物体-场景合成仍然具有挑战性。GS辐射场中烘焙的外观和阴影信息在组合物体和场景时会导致不一致。解决这个问题需要可重新光照的物体重建和场景光照估计。针对可重新光照的物体重建，现有的基于Gaussian的逆渲染方法通常依赖于光线追踪，导致效率低下。我们引入了表面八面体探针 (SOPs)，它存储光照和遮挡信息，并通过插值实现高效的3D查询，避免了昂贵的光线追踪。SOPs在重建中至少提供2倍的加速，并支持Gaussian场景中的实时阴影计算。对于光照估计，现有的基于Gaussian的逆渲染方法难以建模复杂的光传输，并且在复杂场景中经常失败，而基于学习的方法从单张图像预测光照，并且对视点敏感。我们观察到3D物体-场景合成主要关注物体的外观和附近的阴影。因此，我们通过关注物体放置位置的环境光照，简化了完整场景光照估计这一具有挑战性的任务。具体来说，我们捕获场景在该位置的360度重建辐射场，并微调扩散模型以完成光照。基于这些进展，我们提出了一种新的3D物体-场景合成框架ComGS。我们的方法实现了高质量、约28 FPS的实时渲染，产生了具有生动阴影的视觉和谐的结果，并且编辑仅需36秒。

## 🔬 方法详解

**问题定义**：现有基于Gaussian Splatting的3D物体-场景合成方法，由于Gaussian Splatting中烘焙了光照信息，直接组合物体和场景会导致光照不一致，阴影不真实。现有的可重新光照物体重建方法依赖于耗时的光线追踪，效率低下；场景光照估计方法难以处理复杂光照环境，或对视点敏感。

**核心思路**：ComGS的核心思路是将复杂的光照估计问题简化为物体放置位置的局部环境光照估计。通过引入表面八面体探针(SOPs)高效地存储和查询光照信息，避免了昂贵的光线追踪。同时，利用扩散模型补全局部环境光照，从而实现逼真的物体-场景合成。

**技术框架**：ComGS框架主要包含两个阶段：1) 可重新光照的物体重建：使用SOPs存储物体表面的光照和遮挡信息，加速物体重建过程。2) 局部环境光照估计：在物体放置位置重建360度辐射场，并使用扩散模型补全光照信息。最后，将重建的物体和场景进行组合，并进行实时渲染。

**关键创新**：ComGS的关键创新在于：1) 引入了表面八面体探针(SOPs)，通过存储光照和遮挡信息，避免了光线追踪，显著提高了物体重建和阴影计算的效率。2) 将全局光照估计简化为局部环境光照估计，降低了光照估计的难度，并利用扩散模型提升了光照估计的质量。

**关键设计**：SOPs的设计：在物体表面采样点处放置八面体探针，每个探针存储多个方向的光照信息和遮挡信息。光照信息通过球谐函数表示。扩散模型的设计：使用预训练的扩散模型，并针对局部环境光照估计任务进行微调。损失函数包括渲染损失和光照一致性损失。

## 📊 实验亮点

ComGS在3D物体-场景合成任务中取得了显著的性能提升。实验结果表明，ComGS在物体重建速度上比现有方法快至少2倍，并且能够以约28 FPS的速度进行实时渲染。合成结果具有逼真的光照和阴影效果，视觉效果和谐。此外，ComGS的编辑时间仅需36秒，大大提高了合成效率。

## 🎯 应用场景

ComGS可应用于虚拟现实、增强现实、游戏开发、电影制作等领域。它能够快速、高效地将3D物体融入到真实或虚拟场景中，并生成逼真的光照和阴影效果，提升用户体验。该技术还可用于产品设计和可视化，帮助设计师更好地展示和评估设计方案。

## 📄 摘要（原文）

> Gaussian Splatting (GS) enables immersive rendering, but realistic 3D object-scene composition remains challenging. Baked appearance and shadow information in GS radiance fields cause inconsistencies when combining objects and scenes. Addressing this requires relightable object reconstruction and scene lighting estimation. For relightable object reconstruction, existing Gaussian-based inverse rendering methods often rely on ray tracing, leading to low efficiency. We introduce Surface Octahedral Probes (SOPs), which store lighting and occlusion information and allow efficient 3D querying via interpolation, avoiding expensive ray tracing. SOPs provide at least a 2x speedup in reconstruction and enable real-time shadow computation in Gaussian scenes. For lighting estimation, existing Gaussian-based inverse rendering methods struggle to model intricate light transport and often fail in complex scenes, while learning-based methods predict lighting from a single image and are viewpoint-sensitive. We observe that 3D object-scene composition primarily concerns the object's appearance and nearby shadows. Thus, we simplify the challenging task of full scene lighting estimation by focusing on the environment lighting at the object's placement. Specifically, we capture a 360 degrees reconstructed radiance field of the scene at the location and fine-tune a diffusion model to complete the lighting. Building on these advances, we propose ComGS, a novel 3D object-scene composition framework. Our method achieves high-quality, real-time rendering at around 28 FPS, produces visually harmonious results with vivid shadows, and requires only 36 seconds for editing. Code and dataset are available at https://nju-3dv.github.io/projects/ComGS/.

