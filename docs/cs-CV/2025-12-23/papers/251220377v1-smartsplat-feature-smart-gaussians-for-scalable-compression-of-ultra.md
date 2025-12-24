---
layout: default
title: SmartSplat: Feature-Smart Gaussians for Scalable Compression of Ultra-High-Resolution Images
---

# SmartSplat: Feature-Smart Gaussians for Scalable Compression of Ultra-High-Resolution Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20377" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20377v1</a>
  <a href="https://arxiv.org/pdf/2512.20377.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20377v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20377v1', 'SmartSplat: Feature-Smart Gaussians for Scalable Compression of Ultra-High-Resolution Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linfei Li, Lin Zhang, Zhong Wang, Ying Shen

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: Accepted by AAAI 2026

**🔗 代码/项目**: [GITHUB](https://github.com/lif314/SmartSplat)

---

## 💡 一句话要点

**SmartSplat：提出特征感知的GS图像压缩框架，实现超高分辨率图像的高效压缩与高质量重建。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `图像压缩` `高斯溅射` `超高分辨率图像` `特征感知` `变分采样`

## 📋 核心要点

1. 现有图像压缩方法在高分辨率场景下难以平衡压缩率和重建质量，导致性能瓶颈。
2. SmartSplat利用图像特征引导高斯采样，并自适应调整高斯颜色，从而更有效地表征图像。
3. 实验表明，SmartSplat在DIV8K和16K数据集上超越现有方法，实现了更高的压缩率和重建质量。

## 📝 摘要（中文）

随着生成式AI的快速发展，超高分辨率视觉内容的产生对高效压缩和终端设备上的实时解码提出了巨大挑战。受3D高斯溅射的启发，近期的2D高斯图像模型提高了表征效率，但现有方法难以在超高分辨率场景中平衡压缩率和重建保真度。为了解决这个问题，我们提出了SmartSplat，一个高度自适应且特征感知的基于高斯溅射的图像压缩框架，支持任意图像分辨率和压缩率。SmartSplat利用图像感知特征，如梯度和颜色方差，引入了一种梯度-颜色引导的变分采样策略以及一种基于排除的均匀采样方案，以改善像素空间中高斯基元的非重叠覆盖。此外，我们提出了一种尺度自适应的高斯颜色采样方法，以增强跨尺度的颜色初始化。通过空间布局、尺度和颜色初始化的联合优化，SmartSplat使用有限数量的高斯有效地捕获局部结构和全局纹理，从而在强压缩下实现高重建质量。在DIV8K和一个新构建的16K数据集上的大量实验表明，SmartSplat在可比的压缩率下始终优于最先进的方法，并超过了它们的压缩限制，显示出强大的可扩展性和实际适用性。

## 🔬 方法详解

**问题定义**：论文旨在解决超高分辨率图像压缩中，现有方法无法兼顾高压缩率和高质量重建的问题。现有方法在高分辨率图像上，要么压缩率低，要么重建质量差，难以满足实际应用需求。

**核心思路**：SmartSplat的核心思路是利用图像的特征信息（如梯度和颜色方差）来引导高斯基元的采样和初始化，从而更有效地表示图像内容。通过关注图像的关键区域和细节，减少冗余信息，提高压缩效率。

**技术框架**：SmartSplat的整体框架包含以下几个主要阶段：1) 特征提取：提取图像的梯度和颜色方差等特征。2) 高斯采样：采用梯度-颜色引导的变分采样和基于排除的均匀采样相结合的策略，生成高斯基元。3) 颜色初始化：使用尺度自适应的高斯颜色采样方法，初始化高斯基元的颜色。4) 联合优化：联合优化高斯基元的空间布局、尺度和颜色，以最小化重建误差。

**关键创新**：SmartSplat的关键创新在于其特征感知的采样策略和尺度自适应的颜色初始化方法。梯度-颜色引导的变分采样能够使高斯基元更密集地分布在图像的关键区域，而基于排除的均匀采样则保证了高斯基元在像素空间中的非重叠覆盖。尺度自适应的颜色初始化方法能够更好地捕捉跨尺度的颜色信息。

**关键设计**：梯度-颜色引导的变分采样策略使用梯度和颜色方差作为概率分布的权重，引导高斯基元的采样。基于排除的均匀采样通过维护一个已覆盖像素的集合，避免高斯基元之间的重叠。尺度自适应的颜色初始化方法通过在不同尺度上采样颜色信息，并将其融合到高斯基元的颜色初始化中。损失函数通常包括重建损失和正则化项，以保证重建质量和高斯基元的平滑性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20377v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20377v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20377v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SmartSplat在DIV8K和16K数据集上进行了广泛的实验，结果表明，在可比的压缩率下，SmartSplat始终优于现有的最先进方法。更重要的是，SmartSplat能够突破现有方法的压缩限制，在更高的压缩率下仍然保持较高的重建质量，展现了强大的可扩展性和实际应用价值。

## 🎯 应用场景

SmartSplat可应用于各种需要高效压缩和高质量重建的超高分辨率图像场景，例如：高清视频流媒体、遥感图像处理、医学图像存储与传输、以及虚拟现实/增强现实等应用。该技术能够降低存储成本、减少带宽需求，并提升用户体验，具有广阔的应用前景。

## 📄 摘要（原文）

> Recent advances in generative AI have accelerated the production of ultra-high-resolution visual content, posing significant challenges for efficient compression and real-time decoding on end-user devices. Inspired by 3D Gaussian Splatting, recent 2D Gaussian image models improve representation efficiency, yet existing methods struggle to balance compression ratio and reconstruction fidelity in ultra-high-resolution scenarios. To address this issue, we propose SmartSplat, a highly adaptive and feature-aware GS-based image compression framework that supports arbitrary image resolutions and compression ratios. SmartSplat leverages image-aware features such as gradients and color variances, introducing a Gradient-Color Guided Variational Sampling strategy together with an Exclusion-based Uniform Sampling scheme to improve the non-overlapping coverage of Gaussian primitives in pixel space. In addition, we propose a Scale-Adaptive Gaussian Color Sampling method to enhance color initialization across scales. Through joint optimization of spatial layout, scale, and color initialization, SmartSplat efficiently captures both local structures and global textures using a limited number of Gaussians, achieving high reconstruction quality under strong compression. Extensive experiments on DIV8K and a newly constructed 16K dataset demonstrate that SmartSplat consistently outperforms state-of-the-art methods at comparable compression ratios and exceeds their compression limits, showing strong scalability and practical applicability. The code is publicly available at https://github.com/lif314/SmartSplat.

