---
layout: default
title: Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries
---

# Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13796" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13796</a>
  <a href="https://arxiv.org/pdf/2512.13796.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13796" onclick="toggleFavorite(this, '2512.13796', 'Nexels: Neurally-Textured Surfels for Real-Time Novel View Synthesis with Sparse Geometries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Victor Rong, Jan Held, Victor Chu, Daniel Rebain, Marc Van Droogenbroeck, Kiriakos N. Kutulakos, Andrea Tagliasacchi, David B. Lindell

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于神经纹理Surfels的新视角合成方法，在稀疏几何下实现实时渲染。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `新视角合成` `神经渲染` `Surfels` `神经纹理` `实时渲染`

## 📋 核心要点

1. 现有高斯溅射方法在新视角合成中表现出色，但建模高纹理场景需要数百万个图元，即使场景几何结构简单。
2. 论文提出一种基于神经纹理Surfels的表示方法，解耦几何和外观，使用Surfels表示几何，神经场和图元颜色表示外观。
3. 实验表明，该方法在保持感知质量的同时，显著减少了图元数量和内存占用，并提高了渲染速度。

## 📝 摘要（中文）

本文提出了一种超越基于点的渲染的新表示方法，用于新视角合成，旨在解耦几何和外观以实现紧凑的表示。该方法使用Surfels表示几何，并结合全局神经场和每个图元的颜色来表示外观。神经场为每个像素的固定数量的图元进行纹理化，确保计算开销较低。实验结果表明，该表示方法在感知质量上与3D高斯溅射相当，同时在室外场景中使用减少9.7倍的图元和5.5倍的内存，在室内场景中使用减少31倍的图元和3.7倍的内存。此外，该表示方法的渲染速度是现有纹理图元的两倍，同时提高了视觉质量。

## 🔬 方法详解

**问题定义**：现有基于高斯溅射的新视角合成方法，在处理高纹理复杂场景时，需要大量的图元才能达到较好的渲染效果，这导致了巨大的内存占用和计算开销，限制了其在资源受限设备上的应用。即使场景的几何结构相对简单，仍然需要大量的图元来捕捉细节丰富的纹理信息。

**核心思路**：论文的核心思路是将几何表示与外观表示解耦。具体来说，使用Surfels来表示场景的几何结构，Surfels是一种局部平面图元，可以有效地表示表面。然后，使用一个全局神经场和一个per-primitive颜色来表示外观。神经场负责对Surfels进行纹理化，从而减少了对大量图元的依赖。通过这种解耦，可以用更少的图元来表示复杂的场景，从而降低内存占用和计算开销。

**技术框架**：该方法主要包含以下几个阶段：1) 使用Surfels表示场景的几何结构。2) 使用全局神经场对Surfels进行纹理化。神经场将3D空间坐标映射到纹理颜色。3) 使用per-primitive颜色来增强外观表示。4) 通过可微分渲染，将Surfels投影到图像平面上，并合成最终的图像。整体流程是从稀疏几何信息开始，通过神经纹理化生成高质量的新视角图像。

**关键创新**：该方法最重要的创新点在于将神经场应用于Surfels的纹理化。与直接使用神经场表示整个场景不同，该方法使用神经场来增强Surfels的外观表示。这种方法结合了Surfels的几何表示能力和神经场的纹理生成能力，从而实现了更紧凑和高效的场景表示。此外，通过为每个像素固定数量的图元进行纹理化，保证了计算开销的可控性。

**关键设计**：神经场的具体结构未知，但其输入是3D空间坐标，输出是纹理颜色。损失函数可能包含图像重建损失和正则化项，以保证渲染图像的质量和神经场的平滑性。Surfels的数量是一个重要的参数，需要根据场景的复杂程度进行调整。per-primitive颜色可以作为神经场的补充，用于捕捉局部颜色变化。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13796/x1.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13796/img/kernel/kernel_clamped.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13796/x13.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在室外场景中使用减少9.7倍的图元和5.5倍的内存，在室内场景中使用减少31倍的图元和3.7倍的内存，同时保持了与3D高斯溅射相当的感知质量。此外，该方法的渲染速度是现有纹理图元的两倍，并提高了视觉质量。这些结果表明，该方法在效率和质量方面都优于现有方法。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、机器人导航、游戏开发等领域。通过使用更少的图元和内存，该方法可以实现更高效的新视角合成，从而在移动设备和嵌入式系统上实现高质量的渲染效果。此外，该方法还可以用于三维重建和场景编辑，为用户提供更灵活和交互式的体验。

## 📄 摘要（原文）

> Though Gaussian splatting has achieved impressive results in novel view synthesis, it requires millions of primitives to model highly textured scenes, even when the geometry of the scene is simple. We propose a representation that goes beyond point-based rendering and decouples geometry and appearance in order to achieve a compact representation. We use surfels for geometry and a combination of a global neural field and per-primitive colours for appearance. The neural field textures a fixed number of primitives for each pixel, ensuring that the added compute is low. Our representation matches the perceptual quality of 3D Gaussian splatting while using $9.7\times$ fewer primitives and $5.5\times$ less memory on outdoor scenes and using $31\times$ fewer primitives and $3.7\times$ less memory on indoor scenes. Our representation also renders twice as fast as existing textured primitives while improving upon their visual quality.

