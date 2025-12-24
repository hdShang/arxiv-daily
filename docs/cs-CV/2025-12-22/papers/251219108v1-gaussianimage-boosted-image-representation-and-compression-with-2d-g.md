---
layout: default
title: "GaussianImage++: Boosted Image Representation and Compression with 2D Gaussian Splatting"
---

# GaussianImage++: Boosted Image Representation and Compression with 2D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19108" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19108v1</a>
  <a href="https://arxiv.org/pdf/2512.19108.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19108v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19108v1', 'GaussianImage++: Boosted Image Representation and Compression with 2D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tiantian Li, Xinjie Zhang, Xingtong Ge, Tongda Xu, Dailan He, Jun Zhang, Yan Wang

**分类**: cs.CV

**发布日期**: 2025-12-22

**备注**: Accepted to AAAI 2026.Code URL:https://github.com/Sweethyh/GaussianImage_plus.git

---

## 💡 一句话要点

**GaussianImage++：利用2D高斯溅射增强图像表示与压缩性能**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `图像表示` `图像压缩` `高斯溅射` `隐式神经表示` `量化感知训练`

## 📋 核心要点

1. 现有基于高斯溅射的图像表示方法需要大量高斯图元以保证视觉质量，计算和存储成本高昂。
2. GaussianImage++通过失真驱动的密集化、上下文感知高斯滤波器和属性分离量化等技术，使用更少图元实现高效表示。
3. 实验表明，GaussianImage++在图像表示和压缩方面优于GaussianImage和COIN，同时保持实时解码和低内存占用。

## 📝 摘要（中文）

隐式神经表示(INRs)在图像表示和压缩方面取得了显著成功，但它们需要大量的训练时间和内存。同时，最近的2D高斯溅射(GS)方法(例如，GaussianImage)通过高效的基于图元的渲染提供了有希望的替代方案。然而，这些方法需要过多的高斯图元来维持高视觉保真度。为了挖掘基于GS的方法的潜力，我们提出了GaussianImage++，它利用有限的高斯图元来实现令人印象深刻的表示和压缩性能。首先，我们引入了一种失真驱动的密集化机制，它根据信号强度逐步分配高斯图元。其次，我们为每个图元采用上下文感知高斯滤波器，这有助于密集化，以基于不同的图像内容优化高斯图元。第三，我们集成了属性分离的可学习标量量化器和量化感知训练，从而能够高效地压缩图元属性。实验结果表明了我们方法的有效性。特别是，GaussianImage++在表示和压缩性能方面优于GaussianImage和基于INRs的COIN，同时保持了实时解码和低内存使用。

## 🔬 方法详解

**问题定义**：现有基于2D高斯溅射的图像表示方法，如GaussianImage，为了达到较高的视觉保真度，需要使用大量的Gaussian primitives。这导致了计算和存储成本的显著增加，限制了其在资源受限环境中的应用。因此，如何在保证图像质量的前提下，减少Gaussian primitives的数量，是本论文要解决的核心问题。

**核心思路**：GaussianImage++的核心思路是通过智能地分配和优化Gaussian primitives，以及高效地压缩其属性，从而在有限数量的primitives下实现高质量的图像表示和压缩。具体来说，该方法通过失真驱动的密集化机制，将更多的primitives分配到图像中信号强度较高的区域，同时利用上下文感知的高斯滤波器来优化primitives的形状和位置。此外，该方法还采用了属性分离的可学习标量量化器和量化感知训练，以实现对primitives属性的高效压缩。

**技术框架**：GaussianImage++的整体框架主要包含三个阶段：1) **失真驱动的密集化**：根据图像信号强度自适应地增加Gaussian primitives的数量。2) **上下文感知高斯滤波**：利用上下文信息优化每个primitive的形状和位置。3) **属性分离量化与量化感知训练**：对primitive的属性进行高效压缩，并在训练过程中考虑量化的影响。

**关键创新**：GaussianImage++的关键创新在于以下几个方面：1) **失真驱动的密集化机制**：不同于传统的均匀分配primitives的方法，该方法能够根据图像内容自适应地分配primitives，从而在保证图像质量的同时，减少primitives的总数。2) **上下文感知高斯滤波器**：利用图像的上下文信息来优化primitives的形状和位置，从而提高图像的表示能力。3) **属性分离量化与量化感知训练**：通过对primitive的属性进行高效压缩，降低了存储成本，同时通过量化感知训练保证了图像质量。

**关键设计**：在失真驱动的密集化机制中，论文定义了一个失真度量，用于衡量图像的局部失真程度，并根据该失真度量来决定是否需要增加primitives。在上下文感知高斯滤波器中，论文使用了一个卷积神经网络来预测每个primitive的滤波器参数，该网络以primitive周围的图像区域作为输入。在属性分离量化中，论文将primitive的属性分为多个组，并对每个组使用不同的量化器。此外，论文还采用了量化感知训练，即在训练过程中模拟量化的过程，从而使模型能够更好地适应量化的影响。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19108v1/fig/teaser_kodak_psnr_v3.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19108v1/fig/framework_v5.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19108v1/fig/figure3_v2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GaussianImage++在图像表示和压缩方面取得了显著的性能提升。实验结果表明，GaussianImage++在保持实时解码和低内存占用的前提下，优于GaussianImage和基于INRs的COIN等方法。具体来说，GaussianImage++在图像质量方面取得了显著提升，同时减少了所需的Gaussian primitives的数量，从而降低了计算和存储成本。

## 🎯 应用场景

GaussianImage++在图像压缩、图像传输、图像编辑等领域具有广泛的应用前景。它可以用于开发更高效的图像压缩算法，降低图像存储和传输的成本。此外，它还可以用于图像编辑，例如图像修复、图像增强等。未来，该技术有望应用于移动设备、云计算、虚拟现实等领域，为用户提供更好的图像体验。

## 📄 摘要（原文）

> Implicit neural representations (INRs) have achieved remarkable success in image representation and compression, but they require substantial training time and memory. Meanwhile, recent 2D Gaussian Splatting (GS) methods (\textit{e.g.}, GaussianImage) offer promising alternatives through efficient primitive-based rendering. However, these methods require excessive Gaussian primitives to maintain high visual fidelity. To exploit the potential of GS-based approaches, we present GaussianImage++, which utilizes limited Gaussian primitives to achieve impressive representation and compression performance. Firstly, we introduce a distortion-driven densification mechanism. It progressively allocates Gaussian primitives according to signal intensity. Secondly, we employ context-aware Gaussian filters for each primitive, which assist in the densification to optimize Gaussian primitives based on varying image content. Thirdly, we integrate attribute-separated learnable scalar quantizers and quantization-aware training, enabling efficient compression of primitive attributes. Experimental results demonstrate the effectiveness of our method. In particular, GaussianImage++ outperforms GaussianImage and INRs-based COIN in representation and compression performance while maintaining real-time decoding and low memory usage.

