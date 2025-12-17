---
layout: default
title: HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis
---

# HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14352" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14352</a>
  <a href="https://arxiv.org/pdf/2512.14352.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14352" onclick="toggleFavorite(this, '2512.14352', 'HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu

**分类**: cs.CV, cs.CG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出HGS混合高斯溅射方法，通过静态-动态分解实现紧凑的动态视角合成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态新视角合成` `高斯溅射` `静态-动态分解` `径向基函数` `实时渲染`

## 📋 核心要点

1. 现有动态新视角合成方法模型复杂、参数冗余，导致模型体积大、渲染速度慢，难以在资源受限设备上实时运行。
2. HGS通过静态-动态分解策略，利用径向基函数建模高斯基元，对动态区域使用时变RBF，静态区域共享时不变参数，减少冗余。
3. 实验表明，HGS模型大小减少高达98%，在RTX 3090上实现4K分辨率125 FPS实时渲染，并在高频细节和突发场景变化上提升视觉保真度。

## 📝 摘要（中文）

动态新视角合成（NVS）对于创造沉浸式体验至关重要。现有方法通过引入带有隐式变形场的3D高斯溅射（3DGS）或不加区分地分配时变参数来推进动态NVS，超越了基于NeRF的方法。然而，由于过度的模型复杂性和参数冗余，它们导致模型体积庞大和渲染速度缓慢，使得它们在实时应用中效率低下，尤其是在资源受限的设备上。为了获得一个更高效且冗余参数更少的模型，本文提出混合高斯溅射（HGS），这是一个紧凑而高效的框架，专门设计用于在统一表示中解耦场景的静态和动态区域。HGS的核心创新在于我们的静态-动态分解（SDD）策略，该策略利用径向基函数（RBF）建模高斯基元。具体来说，对于动态区域，我们采用时间相关的RBF来有效地捕获时间变化并处理突发的场景变化，而对于静态区域，我们通过共享时间不变参数来减少冗余。此外，我们引入了一种为显式模型量身定制的两阶段训练策略，以增强静态-动态边界处的时间一致性。实验结果表明，我们的方法将模型大小减少了高达98%，并在单个RTX 3090 GPU上实现了高达125 FPS的4K分辨率实时渲染。它还在RTX 3050上保持了160 FPS（1352 * 1014），并且已集成到VR系统中。此外，HGS在实现与最先进方法相当的渲染质量的同时，为高频细节和突发场景变化提供了显着改进的视觉保真度。

## 🔬 方法详解

**问题定义**：现有动态新视角合成方法，如基于3D高斯溅射（3DGS）的方法，虽然取得了不错的渲染效果，但由于模型复杂度和参数冗余，导致模型体积过大，渲染速度慢，难以满足实时应用的需求，尤其是在移动端或VR等资源受限的设备上。这些方法没有充分利用场景中静态和动态区域的差异，对所有区域都采用复杂的时变参数建模，造成了不必要的计算负担。

**核心思路**：HGS的核心思路是将场景分解为静态和动态两个部分，并分别采用不同的建模方式。对于动态区域，使用时变的径向基函数（RBF）来捕捉时间变化；对于静态区域，则共享时间不变的参数，从而减少冗余参数，降低模型复杂度。通过这种静态-动态分解（SDD）策略，HGS能够在保证渲染质量的同时，显著减小模型体积，提高渲染速度。

**技术框架**：HGS的整体框架包含以下几个主要步骤：1) 使用多视角视频数据作为输入；2) 初始化3D高斯基元；3) 使用静态-动态分解（SDD）策略，将高斯基元分为静态和动态两部分；4) 对动态区域的高斯基元使用时变RBF建模，对静态区域的高斯基元共享时间不变参数；5) 使用两阶段训练策略优化模型参数，增强静态-动态边界处的时间一致性；6) 使用优化的模型进行新视角的渲染。

**关键创新**：HGS最重要的技术创新点在于其静态-动态分解（SDD）策略。与现有方法不同，HGS不是对整个场景都采用统一的时变参数建模，而是根据场景的静态和动态特性，分别采用不同的建模方式。这种分解策略能够有效地减少参数冗余，降低模型复杂度，从而提高渲染效率。此外，使用RBF对高斯基元进行建模也是一个创新点，RBF能够灵活地捕捉动态区域的时间变化。

**关键设计**：HGS的关键设计包括：1) 静态-动态分解的判断标准，需要设计合理的指标来区分静态和动态区域；2) RBF函数的选择和参数设置，需要根据具体的场景和数据进行调整；3) 两阶段训练策略的设计，需要平衡渲染质量和时间一致性；4) 损失函数的设计，需要考虑渲染质量、时间一致性和模型复杂度等因素。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14352/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14352/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14352/x5.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HGS在多个数据集上进行了实验，结果表明，HGS可以将模型大小减少高达98%，并在单个RTX 3090 GPU上实现4K分辨率下125 FPS的实时渲染。在RTX 3050上，HGS也能达到160 FPS（1352 * 1014）。同时，HGS在渲染质量上与最先进的方法相当，并且在高频细节和突发场景变化上具有更好的视觉保真度。

## 🎯 应用场景

HGS在动态新视角合成领域具有广泛的应用前景，例如VR/AR、游戏、电影特效、机器人导航等。它可以用于创建更加逼真和沉浸式的虚拟现实体验，也可以用于生成高质量的动态场景渲染图像。此外，由于其模型体积小、渲染速度快的特点，HGS特别适合在移动端或嵌入式设备上部署，从而实现实时的动态新视角合成。

## 📄 摘要（原文）

> Dynamic novel view synthesis (NVS) is essential for creating immersive experiences. Existing approaches have advanced dynamic NVS by introducing 3D Gaussian Splatting (3DGS) with implicit deformation fields or indiscriminately assigned time-varying parameters, surpassing NeRF-based methods. However, due to excessive model complexity and parameter redundancy, they incur large model sizes and slow rendering speeds, making them inefficient for real-time applications, particularly on resource-constrained devices. To obtain a more efficient model with fewer redundant parameters, in this paper, we propose Hybrid Gaussian Splatting (HGS), a compact and efficient framework explicitly designed to disentangle static and dynamic regions of a scene within a unified representation. The core innovation of HGS lies in our Static-Dynamic Decomposition (SDD) strategy, which leverages Radial Basis Function (RBF) modeling for Gaussian primitives. Specifically, for dynamic regions, we employ time-dependent RBFs to effectively capture temporal variations and handle abrupt scene changes, while for static regions, we reduce redundancy by sharing temporally invariant parameters. Additionally, we introduce a two-stage training strategy tailored for explicit models to enhance temporal coherence at static-dynamic boundaries. Experimental results demonstrate that our method reduces model size by up to 98% and achieves real-time rendering at up to 125 FPS at 4K resolution on a single RTX 3090 GPU. It further sustains 160 FPS at 1352 * 1014 on an RTX 3050 and has been integrated into the VR system. Moreover, HGS achieves comparable rendering quality to state-of-the-art methods while providing significantly improved visual fidelity for high-frequency details and abrupt scene changes.

