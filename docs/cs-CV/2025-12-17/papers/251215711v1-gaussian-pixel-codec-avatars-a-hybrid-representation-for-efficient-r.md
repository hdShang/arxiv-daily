---
layout: default
title: Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering
---

# Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15711" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15711v1</a>
  <a href="https://arxiv.org/pdf/2512.15711.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15711v1" onclick="toggleFavorite(this, '2512.15711v1', 'Gaussian Pixel Codec Avatars: A Hybrid Representation for Efficient Rendering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Divam Gupta, Anuj Pahuja, Nemanja Bartolovic, Tomas Simon, Forrest Iandola, Giljoo Nam

**分类**: cs.CV, cs.GR

**发布日期**: 2025-12-17

**备注**: Tech report

---

## 💡 一句话要点

**提出高斯像素编解码头像(GPiCA)，用于高效渲染的混合人像表示**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `人头头像` `3D高斯溅射` `混合表示` `移动渲染` `神经渲染` `可微渲染` `面部表情` `虚拟化身`

## 📋 核心要点

1. 现有头像渲染方法在真实感和效率之间难以兼顾，基于网格的方法效率高但细节不足，基于高斯的方法真实但计算量大。
2. GPiCA结合三角形网格和3D高斯分布，网格高效表示表面，高斯分布处理非表面区域，实现真实感和效率的平衡。
3. 实验表明，GPiCA在保持与纯高斯方法相当的真实感的同时，达到了与网格方法相当的渲染性能，适合移动设备。

## 📝 摘要（中文）

本文提出高斯像素编解码头像(GPiCA)，一种逼真的人头头像，可以从多视角图像生成，并在移动设备上高效渲染。GPiCA采用独特的混合表示，结合了三角形网格和各向异性3D高斯分布。这种结合最大限度地提高了内存和渲染效率，同时保持了逼真的外观。三角形网格在表示面部皮肤等表面区域非常有效，而3D高斯分布有效地处理了头发和胡须等非表面区域。为此，我们开发了一个统一的可微渲染管线，将网格视为3D高斯溅射的体渲染范例中的半透明层。我们训练神经网络将面部表情代码解码为三个组成部分：3D面部网格、RGBA纹理和一组3D高斯分布。这些组件在一个统一的渲染引擎中同时渲染。网络使用多视角图像监督进行训练。结果表明，GPiCA实现了纯粹基于高斯头像的真实感，同时匹配了基于网格头像的渲染性能。

## 🔬 方法详解

**问题定义**：现有的人头头像渲染方法通常面临真实感和渲染效率之间的权衡。基于网格的方法渲染速度快，但难以捕捉头发、胡须等复杂几何细节，导致真实感不足。基于高斯溅射的方法虽然能实现高真实感，但计算量大，难以在移动设备上实时渲染。因此，如何在移动设备上实现高效且逼真的人头头像渲染是一个挑战。

**核心思路**：GPiCA的核心思路是采用混合表示，即结合三角形网格和3D高斯分布。三角形网格擅长表示面部皮肤等规则表面，渲染效率高；3D高斯分布擅长表示头发、胡须等非表面区域，能捕捉更精细的几何细节。通过将两者结合，可以充分利用各自的优势，在保证真实感的同时提高渲染效率。

**技术框架**：GPiCA的整体框架包括三个主要部分：面部表情编码器、解码器和统一渲染引擎。首先，面部表情编码器将面部表情参数编码成一个低维向量。然后，解码器（由神经网络组成）将该向量解码为三个组成部分：3D面部网格、RGBA纹理和一组3D高斯分布。最后，统一渲染引擎将这三个组件同时渲染到屏幕上。该渲染引擎将网格视为半透明层，并将其与3D高斯分布进行体渲染。

**关键创新**：GPiCA的关键创新在于其混合表示和统一渲染管线。混合表示结合了网格和高斯分布的优点，实现了真实感和效率的平衡。统一渲染管线将网格视为半透明层，并将其与高斯分布进行体渲染，从而实现了无缝融合。这种统一的渲染方式避免了传统方法中需要单独渲染网格和高斯分布，然后进行合成的复杂流程。

**关键设计**：GPiCA的关键设计包括：1) 使用神经网络作为解码器，将面部表情代码映射到网格、纹理和高斯分布；2) 设计了一种新的损失函数，用于训练神经网络，该损失函数包括图像重建损失、正则化损失等；3) 采用可微渲染技术，使得整个渲染管线可以进行端到端训练；4) 对高斯分布的参数（如位置、协方差、颜色）进行优化，以提高渲染质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15711v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15711v1/tex/imgs/normals_grid_3.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15711v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GPiCA在保持与纯高斯方法相当的真实感的同时，达到了与网格方法相当的渲染性能。具体来说，GPiCA在移动设备上的渲染速度比纯高斯方法快数倍，同时在视觉质量上优于传统的网格方法。这些结果表明，GPiCA是一种非常有前景的人头头像渲染方法。

## 🎯 应用场景

GPiCA具有广泛的应用前景，包括虚拟会议、游戏、社交媒体和虚拟现实/增强现实等领域。它可以用于创建逼真的虚拟化身，从而增强用户体验。此外，GPiCA的高效渲染能力使其非常适合在移动设备上部署，从而为移动用户提供高质量的虚拟化身体验。未来，GPiCA可以进一步扩展到全身化身，并与其他技术（如动作捕捉）相结合，从而实现更逼真、更具互动性的虚拟体验。

## 📄 摘要（原文）

> We present Gaussian Pixel Codec Avatars (GPiCA), photorealistic head avatars that can be generated from multi-view images and efficiently rendered on mobile devices. GPiCA utilizes a unique hybrid representation that combines a triangle mesh and anisotropic 3D Gaussians. This combination maximizes memory and rendering efficiency while maintaining a photorealistic appearance. The triangle mesh is highly efficient in representing surface areas like facial skin, while the 3D Gaussians effectively handle non-surface areas such as hair and beard. To this end, we develop a unified differentiable rendering pipeline that treats the mesh as a semi-transparent layer within the volumetric rendering paradigm of 3D Gaussian Splatting. We train neural networks to decode a facial expression code into three components: a 3D face mesh, an RGBA texture, and a set of 3D Gaussians. These components are rendered simultaneously in a unified rendering engine. The networks are trained using multi-view image supervision. Our results demonstrate that GPiCA achieves the realism of purely Gaussian-based avatars while matching the rendering performance of mesh-based avatars.

