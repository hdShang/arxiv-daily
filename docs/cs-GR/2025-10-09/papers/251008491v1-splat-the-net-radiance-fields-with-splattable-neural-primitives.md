---
layout: default
title: "Splat the Net: Radiance Fields with Splattable Neural Primitives"
---

# Splat the Net: Radiance Fields with Splattable Neural Primitives

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08491" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08491v1</a>
  <a href="https://arxiv.org/pdf/2510.08491.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08491v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08491v1', 'Splat the Net: Radiance Fields with Splattable Neural Primitives')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xilong Zhou, Bao-Huy Nguyen, Loïc Magne, Vladislav Golyanik, Thomas Leimkühler, Christian Theobalt

**分类**: cs.GR, cs.CV

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**提出可splatting的神经基元，兼顾神经辐射场的表达能力和splatting的渲染效率。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `神经辐射场` `3D高斯Splatting` `新视角合成` `可微分渲染` `神经基元`

## 📋 核心要点

1. 神经辐射场渲染质量高但渲染速度慢，3D高斯Splatting渲染速度快但表达能力有限，如何兼顾两者是核心问题。
2. 论文提出可splatting的神经基元，每个基元用浅层神经网络参数化一个有界神经密度场，并推导出线积分的解析解。
3. 实验表明，该方法在保证渲染质量和速度的同时，使用的基元数量和参数数量显著减少。

## 📝 摘要（中文）

辐射场已成为建模3D场景外观的主要表示方法。神经辐射场等神经方法具有很高的表达能力，但需要昂贵的射线步进进行渲染。基于图元的方法，如3D高斯Splatting，通过splatting提供实时效率，但牺牲了表达能力。受这两个方向进展的启发，我们引入了可splatting的神经基元，这是一种新的体积表示，它将神经模型的表达能力与基于图元的splatting的效率结合起来。每个基元编码一个由浅层神经网络参数化的有界神经密度场。我们的公式允许对线积分进行精确的解析解，从而能够有效计算透视精确的splatting核。因此，我们的表示支持沿视线积分，而无需昂贵的射线步进。这些基元灵活地适应场景几何，并且比以前的解析基元更大，从而减少了每个场景所需的数量。在新视角合成基准测试中，我们的方法在质量和速度上与3D高斯Splatting相匹配，同时使用的基元数量减少了10倍，参数数量减少了6倍。这些优势直接来自表示本身，而不依赖于复杂的控制或自适应框架。

## 🔬 方法详解

**问题定义**：现有神经辐射场（NeRF）方法渲染质量高，但需要进行耗时的射线步进（ray marching），计算复杂度高。而基于图元的3D高斯Splatting虽然渲染速度快，但表达能力有限，难以捕捉复杂场景的细节。因此，如何在保证渲染质量的同时，提高渲染效率是一个关键问题。

**核心思路**：论文的核心思路是结合神经辐射场的表达能力和3D高斯Splatting的渲染效率，提出一种新的体积表示方法，即可splatting的神经基元。每个基元不再是简单的椭球高斯分布，而是由一个浅层神经网络参数化的有界神经密度场。通过这种方式，每个基元可以表达更复杂的局部几何和外观信息。

**技术框架**：该方法的主要流程如下：首先，将场景表示为一组可splatting的神经基元。然后，对于每个像素，通过splatting操作将相关的神经基元投影到图像平面上。由于每个基元都编码了一个神经密度场，因此可以通过解析方法计算沿视线的积分，得到该像素的颜色值。最后，通过优化神经基元的参数，使得渲染图像与真实图像尽可能接近。

**关键创新**：该方法最重要的技术创新点在于提出了可splatting的神经基元，并推导出了线积分的解析解。与传统的3D高斯Splatting相比，该方法使用的基元数量更少，但表达能力更强。与神经辐射场相比，该方法避免了耗时的射线步进，从而提高了渲染效率。

**关键设计**：每个神经基元由一个浅层神经网络参数化，该网络以3D坐标为输入，输出密度和颜色值。论文推导出了线积分的解析解，使得可以高效地计算splatting核。损失函数包括渲染损失和正则化项，用于约束神经基元的形状和大小。

## 📊 实验亮点

实验结果表明，该方法在新的视角合成基准测试中，在质量和速度上与3D高斯Splatting相匹配，同时使用的基元数量减少了10倍，参数数量减少了6倍。这表明该方法在保证渲染质量的同时，显著提高了渲染效率，并降低了存储成本。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、游戏开发、自动驾驶等领域。通过高效地渲染高质量的3D场景，可以提升用户体验，并为相关应用提供更强大的技术支持。未来，该方法有望进一步扩展到动态场景的建模和渲染，以及更复杂的材质和光照效果的模拟。

## 📄 摘要（原文）

> Radiance fields have emerged as a predominant representation for modeling 3D scene appearance. Neural formulations such as Neural Radiance Fields provide high expressivity but require costly ray marching for rendering, whereas primitive-based methods such as 3D Gaussian Splatting offer real-time efficiency through splatting, yet at the expense of representational power. Inspired by advances in both these directions, we introduce splattable neural primitives, a new volumetric representation that reconciles the expressivity of neural models with the efficiency of primitive-based splatting. Each primitive encodes a bounded neural density field parameterized by a shallow neural network. Our formulation admits an exact analytical solution for line integrals, enabling efficient computation of perspectively accurate splatting kernels. As a result, our representation supports integration along view rays without the need for costly ray marching. The primitives flexibly adapt to scene geometry and, being larger than prior analytic primitives, reduce the number required per scene. On novel-view synthesis benchmarks, our approach matches the quality and speed of 3D Gaussian Splatting while using $10\times$ fewer primitives and $6\times$ fewer parameters. These advantages arise directly from the representation itself, without reliance on complex control or adaptation frameworks. The project page is https://vcai.mpi-inf.mpg.de/projects/SplatNet/.

