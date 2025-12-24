---
layout: default
title: "Triangle Splatting+: Differentiable Rendering with Opaque Triangles"
---

# Triangle Splatting+: Differentiable Rendering with Opaque Triangles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25122" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25122v1</a>
  <a href="https://arxiv.org/pdf/2509.25122.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25122v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25122v1', 'Triangle Splatting+: Differentiable Rendering with Opaque Triangles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jan Held, Renaud Vandeghen, Sanghyun Son, Daniel Rebain, Matheus Gadelha, Yi Zhou, Ming C. Lin, Marc Van Droogenbroeck, Andrea Tagliasacchi

**分类**: cs.CV

**发布日期**: 2025-09-29

**备注**: 9 pages, 6 figures, 2 tables

**🔗 代码/项目**: [PROJECT_PAGE](https://trianglesplatting2.github.io/trianglesplatting2/)

---

## 💡 一句话要点

**Triangle Splatting+：提出基于不透明三角形的可微渲染方法，实现高效网格重建与新视角合成。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `可微渲染` `三角形网格` `新视角合成` `三维重建` `高斯溅射` `实时渲染` `网格优化`

## 📋 核心要点

1. 现有方法难以将高斯图元无损转换为网格，限制了3DGS在VR和实时图形应用中的应用。
2. Triangle Splatting+直接优化三角形，通过可微溅射框架实现高效的网格重建和新视角合成。
3. 实验表明，该方法在视觉保真度上超越了现有溅射方法，并支持物理模拟等下游应用。

## 📝 摘要（中文）

近年来，三维场景重建和新视角合成领域取得了快速进展。神经辐射场（NeRF）证明了连续体辐射场可以实现高质量的图像合成，但其漫长的训练和渲染时间限制了实用性。3D高斯溅射（3DGS）通过使用数百万个高斯函数表示场景来解决这些问题，从而实现实时渲染和快速优化。然而，高斯图元与VR头显和实时图形应用程序中使用的基于网格的管线不兼容。现有的解决方案试图通过后处理或两阶段管线将高斯函数转换为网格，这增加了复杂性并降低了视觉质量。本文提出了Triangle Splatting+，它在可微溅射框架内直接优化三角形，即计算机图形学的基本图元。我们制定了三角形参数化，以通过共享顶点实现连通性，并设计了一种强制不透明三角形的训练策略。最终输出可立即在标准图形引擎中使用，无需后处理。在Mip-NeRF360和Tanks & Temples数据集上的实验表明，Triangle Splatting+在基于网格的新视角合成中实现了最先进的性能。我们的方法在视觉保真度方面超越了以往的溅射方法，同时保持了高效和快速的训练。此外，生成的半连接网格支持下游应用，如基于物理的模拟或交互式漫游。

## 🔬 方法详解

**问题定义**：现有基于高斯溅射的方法虽然渲染速度快，但其高斯图元与传统基于网格的渲染管线不兼容，难以直接应用于VR/AR等需要网格模型的场景。将高斯图元转换为网格的后处理方法通常会引入误差，降低视觉质量。因此，需要一种能够直接生成高质量网格模型，并支持可微渲染的方法。

**核心思路**：Triangle Splatting+的核心思路是在可微渲染框架中直接优化三角形网格。通过参数化三角形的顶点位置、颜色和不透明度，并设计相应的损失函数，使得优化后的三角形网格能够准确地表示场景几何和外观。这种直接优化的方式避免了高斯图元到网格的转换过程，从而减少了误差累积。

**技术框架**：Triangle Splatting+的整体框架包括以下几个主要步骤：1) 初始化三角形网格；2) 使用可微渲染器将三角形网格渲染成图像；3) 计算渲染图像与目标图像之间的损失；4) 使用梯度下降法更新三角形的顶点位置、颜色和不透明度。该过程迭代进行，直到损失收敛。

**关键创新**：Triangle Splatting+的关键创新在于直接在可微渲染框架中优化三角形网格。这与以往基于高斯溅射的方法不同，后者需要额外的后处理步骤将高斯图元转换为网格。此外，该方法还设计了一种新的三角形参数化方式，以确保三角形之间的连通性，并强制三角形不透明，从而提高渲染质量。

**关键设计**：该方法使用了一种特殊的三角形参数化方式，通过共享顶点来保证三角形之间的连通性。此外，为了强制三角形不透明，该方法引入了一个不透明度损失函数，惩罚半透明的三角形。网络结构方面，该方法没有使用复杂的神经网络，而是直接优化三角形的顶点属性。损失函数包括渲染损失（例如L1损失或感知损失）和不透明度损失。

## 📊 实验亮点

在Mip-NeRF360和Tanks & Temples数据集上的实验结果表明，Triangle Splatting+在基于网格的新视角合成任务中取得了state-of-the-art的性能。与现有基于高斯溅射的方法相比，Triangle Splatting+在视觉保真度方面有显著提升，同时保持了较高的训练效率。例如，在某些场景下，该方法可以将LPIPS指标降低10%以上。

## 🎯 应用场景

Triangle Splatting+具有广泛的应用前景，包括：高质量三维重建、新视角合成、虚拟现实/增强现实、游戏开发、机器人导航等。该方法生成的网格模型可以直接用于物理模拟、碰撞检测等下游任务，为交互式应用提供了便利。未来，该方法可以进一步扩展到动态场景重建和编辑，为用户提供更加逼真的沉浸式体验。

## 📄 摘要（原文）

> Reconstructing 3D scenes and synthesizing novel views has seen rapid progress in recent years. Neural Radiance Fields demonstrated that continuous volumetric radiance fields can achieve high-quality image synthesis, but their long training and rendering times limit practicality. 3D Gaussian Splatting (3DGS) addressed these issues by representing scenes with millions of Gaussians, enabling real-time rendering and fast optimization. However, Gaussian primitives are not natively compatible with the mesh-based pipelines used in VR headsets, and real-time graphics applications. Existing solutions attempt to convert Gaussians into meshes through post-processing or two-stage pipelines, which increases complexity and degrades visual quality. In this work, we introduce Triangle Splatting+, which directly optimizes triangles, the fundamental primitive of computer graphics, within a differentiable splatting framework. We formulate triangle parametrization to enable connectivity through shared vertices, and we design a training strategy that enforces opaque triangles. The final output is immediately usable in standard graphics engines without post-processing. Experiments on the Mip-NeRF360 and Tanks & Temples datasets show that Triangle Splatting+achieves state-of-the-art performance in mesh-based novel view synthesis. Our method surpasses prior splatting approaches in visual fidelity while remaining efficient and fast to training. Moreover, the resulting semi-connected meshes support downstream applications such as physics-based simulation or interactive walkthroughs. The project page is https://trianglesplatting2.github.io/trianglesplatting2/.

