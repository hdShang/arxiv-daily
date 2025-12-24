---
layout: default
title: "WorldWarp: Propagating 3D Geometry with Asynchronous Video Diffusion"
---

# WorldWarp: Propagating 3D Geometry with Asynchronous Video Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19678" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19678v1</a>
  <a href="https://arxiv.org/pdf/2512.19678.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19678v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19678v1', 'WorldWarp: Propagating 3D Geometry with Asynchronous Video Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanyang Kong, Xingyi Yang, Xiaoxu Zheng, Xinchao Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-22

**备注**: Project page: https://hyokong.github.io/worldwarp-page/

**🔗 代码/项目**: [PROJECT_PAGE](https://hyokong.github.io/worldwarp-page/)

---

## 💡 一句话要点

**WorldWarp：利用异步视频扩散传播3D几何信息，生成长时几何一致性视频。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视频生成` `3D几何` `扩散模型` `高斯溅射` `长时视频` `几何一致性` `时空扩散`

## 📋 核心要点

1. 现有视频生成方法难以在长时视频中保持几何一致性，尤其是在遮挡和复杂相机运动下。
2. WorldWarp通过维护一个基于高斯溅射的3D几何缓存，并将历史内容扭曲到新视角，从而实现几何约束。
3. 该方法引入时空扩散模型，通过动态调整噪声调度，实现对扭曲区域的细化和对空白区域的生成，提升视频质量。

## 📝 摘要（中文）

生成长时、几何一致的视频面临一个根本困境：一致性要求严格遵守像素空间中的3D几何结构，而最先进的生成模型在相机条件潜在空间中效果最佳。这种脱节导致现有方法在处理遮挡区域和复杂相机轨迹时遇到困难。为了弥合这一差距，我们提出了WorldWarp，一个将3D结构锚点与2D生成细化器相结合的框架。为了建立几何基础，WorldWarp维护一个通过高斯溅射（3DGS）构建的在线3D几何缓存。通过将历史内容显式地扭曲到新的视角中，该缓存充当结构支架，确保每个新帧都尊重先前的几何结构。然而，由于遮挡，静态扭曲不可避免地会留下孔洞和伪影。我们使用专为“填充和修改”目标设计的时空扩散（ST-Diff）模型来解决这个问题。我们的关键创新是时空变化的噪声调度：空白区域接收完全噪声以触发生成，而扭曲区域接收部分噪声以实现细化。通过在每个步骤动态更新3D缓存，WorldWarp保持视频块之间的一致性。因此，它通过确保3D逻辑指导结构，而扩散逻辑完善纹理，从而实现了最先进的保真度。

## 🔬 方法详解

**问题定义**：现有视频生成方法在生成长时视频时，难以保证几何一致性，尤其是在存在遮挡和复杂相机运动的情况下。这些方法通常在相机条件潜在空间中操作，与像素空间中的3D几何结构脱节，导致生成结果出现不自然的形变和伪影。

**核心思路**：WorldWarp的核心思路是将3D几何信息显式地融入到视频生成过程中。通过维护一个在线更新的3D几何缓存，并利用该缓存将历史内容扭曲到新的视角，从而保证生成的新帧与之前的帧在几何上保持一致。同时，利用时空扩散模型来填充和细化扭曲后的图像，解决遮挡和伪影问题。

**技术框架**：WorldWarp框架主要包含两个核心模块：3D几何缓存和时空扩散模型。3D几何缓存基于高斯溅射（3DGS）构建，用于存储和更新场景的3D几何信息。时空扩散模型（ST-Diff）用于填充和细化扭曲后的图像，生成最终的视频帧。整个流程包括：1）利用3D几何缓存将历史帧扭曲到当前视角；2）使用ST-Diff模型填充和细化扭曲后的图像；3）将生成的新帧更新到3D几何缓存中。

**关键创新**：WorldWarp的关键创新在于将3D几何缓存与时空扩散模型相结合，实现几何约束的视频生成。与现有方法相比，WorldWarp显式地利用3D几何信息，避免了在潜在空间中进行推理时可能出现的几何失真。此外，提出的时空变化的噪声调度策略，能够有效地控制生成和细化的过程，提高生成质量。

**关键设计**：在时空扩散模型中，关键的设计是时空变化的噪声调度。对于扭曲后的区域，施加部分噪声，使其在保留原有结构的基础上进行细化；对于空白区域（例如遮挡区域），施加完全噪声，使其完全由扩散模型生成。这种策略能够有效地平衡几何约束和生成质量。此外，3D几何缓存的更新频率和方式也会影响最终的生成效果，需要在实际应用中进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19678v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19678v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19678v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文提出的WorldWarp框架在长时视频生成任务上取得了显著的成果。通过与现有方法进行对比，WorldWarp在几何一致性和视觉质量方面均有明显提升。实验结果表明，WorldWarp能够生成具有复杂相机运动和遮挡的、几何一致的视频，并且视觉效果更加逼真。

## 🎯 应用场景

WorldWarp在电影制作、游戏开发、虚拟现实等领域具有广泛的应用前景。它可以用于生成具有复杂相机运动和遮挡的长时视频，例如虚拟场景漫游、角色动画等。该技术还可以用于视频修复和增强，例如修复老旧电影或提高视频分辨率。未来，WorldWarp有望成为一种强大的视频生成工具，为各行各业带来创新。

## 📄 摘要（原文）

> Generating long-range, geometrically consistent video presents a fundamental dilemma: while consistency demands strict adherence to 3D geometry in pixel space, state-of-the-art generative models operate most effectively in a camera-conditioned latent space. This disconnect causes current methods to struggle with occluded areas and complex camera trajectories. To bridge this gap, we propose WorldWarp, a framework that couples a 3D structural anchor with a 2D generative refiner. To establish geometric grounding, WorldWarp maintains an online 3D geometric cache built via Gaussian Splatting (3DGS). By explicitly warping historical content into novel views, this cache acts as a structural scaffold, ensuring each new frame respects prior geometry. However, static warping inevitably leaves holes and artifacts due to occlusions. We address this using a Spatio-Temporal Diffusion (ST-Diff) model designed for a "fill-and-revise" objective. Our key innovation is a spatio-temporal varying noise schedule: blank regions receive full noise to trigger generation, while warped regions receive partial noise to enable refinement. By dynamically updating the 3D cache at every step, WorldWarp maintains consistency across video chunks. Consequently, it achieves state-of-the-art fidelity by ensuring that 3D logic guides structure while diffusion logic perfects texture. Project page: \href{https://hyokong.github.io/worldwarp-page/}{https://hyokong.github.io/worldwarp-page/}.

