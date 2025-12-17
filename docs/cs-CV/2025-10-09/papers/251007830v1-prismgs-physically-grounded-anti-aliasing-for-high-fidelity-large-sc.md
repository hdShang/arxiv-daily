---
layout: default
title: PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale 3D Gaussian Splatting
---

# PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale 3D Gaussian Splatting

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07830" target="_blank" class="toolbar-btn">arXiv: 2510.07830v1</a>
    <a href="https://arxiv.org/pdf/2510.07830.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07830v1" 
            onclick="toggleFavorite(this, '2510.07830v1', 'PrismGS: Physically-Grounded Anti-Aliasing for High-Fidelity Large-Scale 3D Gaussian Splatting')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Houqiang Zhong, Zhenglong Wu, Sihua Fu, Zihan Zheng, Xin Jin, Xiaoyun Zhang, Li Song, Qiang Hu

**分类**: cs.CV

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**PrismGS：面向大规模高保真3D高斯溅射的物理约束抗锯齿方法**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯溅射` `抗锯齿` `物理约束` `多尺度监督` `正则化` `高分辨率渲染` `城市建模`

## 📋 核心要点

1. 现有3D高斯溅射方法在大型城市环境中渲染时，存在严重的锯齿伪影和优化不稳定性，尤其是在高分辨率下。
2. PrismGS通过引入金字塔多尺度监督和显式大小正则化，从物理约束的角度提升3D高斯的渲染质量。
3. 实验表明，PrismGS在多个数据集上实现了显著的PSNR增益，并在4K渲染下保持了卓越的质量和鲁棒性。

## 📝 摘要（中文）

3D高斯溅射(3DGS)最近实现了紧凑场景中的实时照片级真实感渲染，但扩展到大型城市环境会引入严重的锯齿伪影和优化不稳定，尤其是在高分辨率(例如，4K)渲染下。这些伪影表现为闪烁的纹理和锯齿状边缘，源于高斯基元与城市几何体的多尺度特性之间的不匹配。现有的“分而治之”的流程虽然解决了可扩展性问题，但未能解决这种保真度差距。本文提出了PrismGS，一个物理约束的正则化框架，可以改善3D高斯的内在渲染行为。PrismGS集成了两个协同的正则化器。第一个是金字塔多尺度监督，通过针对预过滤的图像金字塔监督渲染来强制一致性。这迫使模型学习一种固有的抗锯齿表示，该表示在不同的观看尺度上保持一致，直接减轻了闪烁的纹理。第二个是显式的大小正则化，它对3D高斯的尺寸施加了物理约束的下限。这可以防止退化的、与视图相关的基元的形成，从而产生更稳定和更合理的几何表面，并减少锯齿状边缘。我们的方法是即插即用的，并且与现有的流程兼容。在MatrixCity、Mill-19和UrbanScene3D上的大量实验表明，PrismGS实现了最先进的性能，相对于CityGaussian产生了约1.5 dB的显著PSNR增益，同时在苛刻的4K渲染下保持了其卓越的质量和鲁棒性。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模城市环境中3D高斯溅射渲染时出现的锯齿伪影和优化不稳定性问题。现有方法，如“分而治之”策略，虽然提高了可扩展性，但未能有效解决高分辨率渲染下的保真度问题，导致闪烁纹理和锯齿状边缘等视觉瑕疵。

**核心思路**：PrismGS的核心思路是通过物理约束的正则化来改善3D高斯的内在渲染行为。具体来说，它通过多尺度监督来保证不同视角下渲染结果的一致性，并对高斯的大小进行约束，防止生成退化的、与视角相关的基元。这种方法旨在使模型学习到一种固有的抗锯齿表示，从而提高渲染质量和稳定性。

**技术框架**：PrismGS是一个即插即用的框架，可以集成到现有的3D高斯溅射流程中。它主要包含两个模块：金字塔多尺度监督模块和显式大小正则化模块。金字塔多尺度监督模块通过预先过滤的图像金字塔来监督渲染过程，强制模型在不同尺度下保持一致性。显式大小正则化模块对3D高斯的尺寸施加物理约束的下限，防止生成退化的基元。这两个模块协同工作，共同提高渲染质量。

**关键创新**：PrismGS的关键创新在于其物理约束的正则化方法。与现有方法不同，PrismGS不是简单地通过增加高斯基元的数量来提高渲染质量，而是通过约束高斯基元的属性，使其更符合物理规律，从而提高渲染的真实感和稳定性。这种方法可以有效地减少锯齿伪影和优化不稳定性，尤其是在高分辨率渲染下。

**关键设计**：金字塔多尺度监督模块使用预先过滤的图像金字塔作为监督信号，通过计算渲染图像与金字塔图像之间的差异来优化模型。显式大小正则化模块通过对高斯基元的尺寸施加下限约束来实现，该下限可以根据场景的几何特性进行调整。损失函数结合了渲染损失、多尺度监督损失和大小正则化损失，通过调整不同损失的权重来平衡渲染质量和稳定性。

## 📊 实验亮点

实验结果表明，PrismGS在MatrixCity、Mill-19和UrbanScene3D等数据集上取得了显著的性能提升。相对于CityGaussian，PrismGS在PSNR指标上平均提升了约1.5 dB，并且在4K渲染下保持了更高的质量和鲁棒性。这些结果证明了PrismGS在解决大规模城市环境渲染问题上的有效性。

## 🎯 应用场景

PrismGS具有广泛的应用前景，包括城市建模、自动驾驶、虚拟现实和增强现实等领域。它可以用于生成高质量的城市环境渲染，为自动驾驶系统提供更真实的感知数据，并为VR/AR应用提供更沉浸式的体验。此外，PrismGS还可以应用于游戏开发、电影制作等领域，提高视觉效果和渲染效率。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has recently enabled real-time photorealistic rendering in compact scenes, but scaling to large urban environments introduces severe aliasing artifacts and optimization instability, especially under high-resolution (e.g., 4K) rendering. These artifacts, manifesting as flickering textures and jagged edges, arise from the mismatch between Gaussian primitives and the multi-scale nature of urban geometry. While existing ``divide-and-conquer'' pipelines address scalability, they fail to resolve this fidelity gap. In this paper, we propose PrismGS, a physically-grounded regularization framework that improves the intrinsic rendering behavior of 3D Gaussians. PrismGS integrates two synergistic regularizers. The first is pyramidal multi-scale supervision, which enforces consistency by supervising the rendering against a pre-filtered image pyramid. This compels the model to learn an inherently anti-aliased representation that remains coherent across different viewing scales, directly mitigating flickering textures. This is complemented by an explicit size regularization that imposes a physically-grounded lower bound on the dimensions of the 3D Gaussians. This prevents the formation of degenerate, view-dependent primitives, leading to more stable and plausible geometric surfaces and reducing jagged edges. Our method is plug-and-play and compatible with existing pipelines. Extensive experiments on MatrixCity, Mill-19, and UrbanScene3D demonstrate that PrismGS achieves state-of-the-art performance, yielding significant PSNR gains around 1.5 dB against CityGaussian, while maintaining its superior quality and robustness under demanding 4K rendering.

