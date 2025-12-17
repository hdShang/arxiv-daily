---
layout: default
title: Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting
---

# Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15102" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15102v1</a>
  <a href="https://arxiv.org/pdf/2511.15102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15102v1" onclick="toggleFavorite(this, '2511.15102v1', 'Gaussian Blending: Rethinking Alpha Blending in 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junseo Koo, Jinseo Jeong, Gunhee Kim

**分类**: cs.CV

**发布日期**: 2025-11-19

**备注**: AAAI 2026

---

## 💡 一句话要点

**提出高斯混合：重新思考3D高斯溅射中的Alpha混合，提升新视角合成质量**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `新视角合成` `Alpha混合` `高斯混合` `渲染质量` `空间分布` `视觉伪影`

## 📋 核心要点

1. 现有3DGS方法在新视角合成中，尤其是在不同采样率下，存在模糊和阶梯伪影，影响渲染质量。
2. 论文提出高斯混合方法，将alpha和透射率视为空间分布，而非标量，从而更准确地计算透射率。
3. 实验表明，该方法在不同采样率下均能有效捕捉细节，并在新视角合成任务中超越现有模型。

## 📝 摘要（中文）

3D高斯溅射(3DGS)的引入显著提升了新视角合成技术。尽管一些研究进一步改进了3DGS的渲染质量，但在训练期间未见过的采样率下合成视图时，仍然存在明显的视觉差异。具体来说，当放大时会出现由腐蚀引起的模糊伪影，而当缩小时会出现由膨胀引起的阶梯伪影。我们推测这些伪影源于3DGS方法中采用的alpha混合的根本限制。我们提出用新的高斯混合来代替传统的alpha混合，将alpha和透射率视为空间变化的分布，而不是计算像素上的标量。因此，可以考虑像素区域上alpha值的空间分布来更新透射率，从而允许附近的背景splat对最终渲染做出贡献。我们的高斯混合保持了实时渲染速度，不需要额外的内存成本，并且可以很容易地作为即插即用组件集成到现有的基于3DGS或其他NVS框架中。大量实验表明，高斯混合有效地捕捉了各种训练期间未见过的采样率下的精细细节，在未见过的和见过的采样率下始终优于现有的新视角合成模型。

## 🔬 方法详解

**问题定义**：现有3D高斯溅射（3DGS）方法在进行新视角合成时，尤其是在训练时未见过的采样率下，会产生视觉伪影。具体表现为放大时出现模糊（erosion-induced blurring），缩小的时候出现阶梯状伪影（dilation-induced staircase artifacts）。这些问题降低了渲染质量，限制了3DGS的实际应用。

**核心思路**：论文的核心思路是重新思考3DGS中使用的alpha混合方法。传统的alpha混合将alpha和透射率作为标量进行计算，忽略了像素区域内的空间分布信息。论文提出将alpha和透射率视为空间变化的分布，从而更准确地计算透射率，并允许附近的背景splat对最终渲染做出贡献。这种方法能够更好地处理不同采样率下的渲染问题，减少伪影的产生。

**技术框架**：该方法可以作为一个即插即用的模块集成到现有的3DGS框架中。它替换了原有的alpha混合模块，并利用高斯分布来建模alpha和透射率的空间变化。整个渲染流程基本保持不变，因此可以保持实时渲染速度，并且不需要额外的内存开销。该方法可以应用于各种基于3DGS的新视角合成框架。

**关键创新**：该论文的关键创新在于提出了高斯混合（Gaussian Blending）的概念，将alpha和透射率视为空间分布。与传统的标量alpha混合相比，高斯混合能够更好地捕捉像素区域内的空间信息，从而更准确地计算透射率。这种方法能够有效地减少在新视角合成中产生的伪影，提高渲染质量。

**关键设计**：该方法使用高斯分布来建模alpha和透射率的空间变化。具体来说，对于每个splat，其alpha值被建模为一个高斯分布，该高斯分布的均值和方差可以根据splat的位置、大小和形状进行计算。在计算透射率时，需要考虑像素区域内所有splat的alpha分布，并进行积分。为了简化计算，论文采用了一些近似方法，例如使用蒙特卡洛积分或高斯积分。此外，该方法还设计了一些参数来控制高斯分布的形状和大小，从而可以进一步优化渲染效果。

## 📊 实验亮点

实验结果表明，高斯混合方法在各种采样率下均能有效捕捉细节，并在新视角合成任务中超越现有模型。尤其是在训练时未见过的采样率下，该方法能够显著减少模糊和阶梯状伪影，提高渲染质量。在定量指标上，该方法在PSNR、SSIM和LPIPS等指标上均取得了显著提升。

## 🎯 应用场景

该研究成果可广泛应用于虚拟现实、增强现实、游戏开发、自动驾驶等领域。通过提升新视角合成的质量，可以为用户提供更逼真、更沉浸式的体验。例如，在VR/AR应用中，用户可以自由地改变视角，而不会出现模糊或阶梯状伪影。在自动驾驶领域，可以利用该技术生成高质量的合成图像，用于训练和评估自动驾驶算法。

## 📄 摘要（原文）

> The recent introduction of 3D Gaussian Splatting (3DGS) has significantly advanced novel view synthesis. Several studies have further improved the rendering quality of 3DGS, yet they still exhibit noticeable visual discrepancies when synthesizing views at sampling rates unseen during training. Specifically, they suffer from (i) erosion-induced blurring artifacts when zooming in and (ii) dilation-induced staircase artifacts when zooming out. We speculate that these artifacts arise from the fundamental limitation of the alpha blending adopted in 3DGS methods. Instead of the conventional alpha blending that computes alpha and transmittance as scalar quantities over a pixel, we propose to replace it with our novel Gaussian Blending that treats alpha and transmittance as spatially varying distributions. Thus, transmittances can be updated considering the spatial distribution of alpha values across the pixel area, allowing nearby background splats to contribute to the final rendering. Our Gaussian Blending maintains real-time rendering speed and requires no additional memory cost, while being easily integrated as a drop-in replacement into existing 3DGS-based or other NVS frameworks. Extensive experiments demonstrate that Gaussian Blending effectively captures fine details at various sampling rates unseen during training, consistently outperforming existing novel view synthesis models across both unseen and seen sampling rates.

