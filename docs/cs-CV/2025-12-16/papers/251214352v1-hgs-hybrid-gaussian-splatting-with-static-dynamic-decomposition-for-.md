---
layout: default
title: "HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis"
---

# HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14352" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14352v1</a>
  <a href="https://arxiv.org/pdf/2512.14352.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14352v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14352v1', 'HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu

**分类**: cs.CV, cs.CG

**发布日期**: 2025-12-16

**备注**: 11 pages, 9 figures

---

## 💡 一句话要点

**提出混合高斯溅射HGS，通过静态-动态分解实现紧凑的动态视角合成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态新视角合成` `高斯溅射` `静态-动态分解` `径向基函数` `实时渲染`

## 📋 核心要点

1. 现有动态新视角合成方法模型复杂、参数冗余，导致模型大、渲染慢，难以在资源受限设备上实时运行。
2. 提出混合高斯溅射（HGS），通过静态-动态分解策略，对动态区域使用时变RBF，静态区域共享参数，减少冗余。
3. 实验表明，HGS模型尺寸减少高达98%，在RTX 3090上4K分辨率可达125 FPS，并在高频细节和突发场景变化上提升视觉保真度。

## 📝 摘要（中文）

动态新视角合成（NVS）对于创造沉浸式体验至关重要。现有方法通过引入带有隐式变形场或无差别地分配时变参数的3D高斯溅射（3DGS）来推进动态NVS，超越了基于NeRF的方法。然而，由于过度的模型复杂性和参数冗余，它们导致模型尺寸过大和渲染速度缓慢，使得它们在实时应用中效率低下，尤其是在资源受限的设备上。为了获得一个更高效且具有更少冗余参数的模型，本文提出混合高斯溅射（HGS），这是一个紧凑而高效的框架，明确设计用于在统一表示中解耦场景的静态和动态区域。HGS的核心创新在于我们的静态-动态分解（SDD）策略，该策略利用径向基函数（RBF）建模高斯基元。具体来说，对于动态区域，我们采用时间相关的RBF来有效地捕获时间变化并处理突发的场景变化，而对于静态区域，我们通过共享时间不变参数来减少冗余。此外，我们引入了一种为显式模型量身定制的两阶段训练策略，以增强静态-动态边界处的时间一致性。实验结果表明，我们的方法将模型尺寸减少高达98%，并在单个RTX 3090 GPU上以4K分辨率实现高达125 FPS的实时渲染。它还在RTX 3050上以1352 * 1014的分辨率维持160 FPS，并且已集成到VR系统中。此外，HGS在实现与最先进方法相当的渲染质量的同时，为高频细节和突发场景变化提供了显著改进的视觉保真度。

## 🔬 方法详解

**问题定义**：现有动态新视角合成方法，如基于3D高斯溅射（3DGS）的方法，虽然取得了不错的渲染效果，但由于模型复杂度高、参数冗余，导致模型体积大、渲染速度慢，难以满足实时应用的需求，尤其是在移动端或VR/AR等资源受限的设备上。这些方法通常对整个场景采用统一的处理方式，忽略了场景中静态和动态区域的差异，造成了不必要的计算和存储开销。

**核心思路**：HGS的核心思路是将场景分解为静态和动态两部分，并分别采用不同的建模方式。对于动态区域，使用时间相关的径向基函数（RBF）来捕捉时间变化；对于静态区域，则共享时间不变的参数，从而减少冗余。这种静态-动态分解（SDD）策略能够有效地降低模型的复杂度和参数量，提高渲染效率。

**技术框架**：HGS框架主要包含以下几个步骤：1) 使用多视角视频数据作为输入；2) 初始化3D高斯基元；3) 使用SDD策略将高斯基元划分为静态和动态两部分；4) 对动态高斯基元使用时间相关的RBF进行建模，对静态高斯基元共享时间不变参数；5) 使用两阶段训练策略优化模型参数，第一阶段侧重于整体结构，第二阶段侧重于静态-动态边界的平滑过渡；6) 使用优化的高斯基元进行渲染，生成新的视角图像。

**关键创新**：HGS最重要的技术创新点在于其静态-动态分解（SDD）策略。与现有方法对整个场景采用统一建模方式不同，HGS能够根据场景内容自适应地将场景分解为静态和动态区域，并分别采用不同的建模方式。这种分解策略能够有效地减少参数冗余，提高模型的效率。此外，两阶段训练策略也保证了静态和动态区域之间的平滑过渡，避免了伪影的产生。

**关键设计**：HGS的关键设计包括：1) 使用径向基函数（RBF）来建模动态高斯基元的时间变化，RBF的中心点和尺度可以根据时间进行调整，从而捕捉复杂的运动模式；2) 设计了两阶段训练策略，第一阶段使用L1损失和D-SSIM损失来优化整体结构，第二阶段使用额外的正则化项来约束静态-动态边界的平滑性；3) 静态区域的高斯基元共享位置、颜色等参数，只在不透明度上允许微小的变化，从而保证静态区域的稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14352v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14352v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14352v1/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HGS在多个数据集上进行了实验，结果表明，HGS在模型尺寸上相比现有方法减少高达98%，在单个RTX 3090 GPU上以4K分辨率实现高达125 FPS的实时渲染。在RTX 3050上以1352 * 1014的分辨率维持160 FPS。同时，HGS在渲染质量上与现有方法相当，并在高频细节和突发场景变化上提供了显著改进的视觉保真度。

## 🎯 应用场景

HGS在动态新视角合成领域具有广泛的应用前景，例如VR/AR、游戏、电影特效等。它可以用于创建更加逼真和沉浸式的虚拟现实体验，也可以用于生成高质量的动态场景渲染结果。此外，由于HGS具有高效的渲染速度和较小的模型尺寸，它也适用于移动端等资源受限的设备，为移动VR/AR应用提供了可能。未来，HGS可以进一步扩展到更复杂的场景和更具挑战性的动态效果。

## 📄 摘要（原文）

> Dynamic novel view synthesis (NVS) is essential for creating immersive experiences. Existing approaches have advanced dynamic NVS by introducing 3D Gaussian Splatting (3DGS) with implicit deformation fields or indiscriminately assigned time-varying parameters, surpassing NeRF-based methods. However, due to excessive model complexity and parameter redundancy, they incur large model sizes and slow rendering speeds, making them inefficient for real-time applications, particularly on resource-constrained devices. To obtain a more efficient model with fewer redundant parameters, in this paper, we propose Hybrid Gaussian Splatting (HGS), a compact and efficient framework explicitly designed to disentangle static and dynamic regions of a scene within a unified representation. The core innovation of HGS lies in our Static-Dynamic Decomposition (SDD) strategy, which leverages Radial Basis Function (RBF) modeling for Gaussian primitives. Specifically, for dynamic regions, we employ time-dependent RBFs to effectively capture temporal variations and handle abrupt scene changes, while for static regions, we reduce redundancy by sharing temporally invariant parameters. Additionally, we introduce a two-stage training strategy tailored for explicit models to enhance temporal coherence at static-dynamic boundaries. Experimental results demonstrate that our method reduces model size by up to 98% and achieves real-time rendering at up to 125 FPS at 4K resolution on a single RTX 3090 GPU. It further sustains 160 FPS at 1352 * 1014 on an RTX 3050 and has been integrated into the VR system. Moreover, HGS achieves comparable rendering quality to state-of-the-art methods while providing significantly improved visual fidelity for high-frequency details and abrupt scene changes.

