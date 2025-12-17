---
layout: default
title: GASPACHO: Gaussian Splatting for Controllable Humans and Objects
---

# GASPACHO: Gaussian Splatting for Controllable Humans and Objects

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2503.09342" class="toolbar-btn" target="_blank">📄 arXiv: 2503.09342</a>
  <a href="https://arxiv.org/pdf/2503.09342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2503.09342" onclick="toggleFavorite(this, '2503.09342', 'GASPACHO: Gaussian Splatting for Controllable Humans and Objects')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aymen Mir, Arthur Moreau, Helisa Dhamo, Zhensong Zhang, Gerard Pons-Moll, Eduardo Pérez-Pellitero

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**GASPACHO：基于高斯溅射的可控人与物体交互渲染**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `高斯溅射` `神经渲染` `人与物体交互` `可控渲染` `动态物体重建`

## 📋 核心要点

1. 现有方法难以同时重建可控的人体和交互物体，限制了人与物体交互场景的真实感和可控性。
2. GASPACHO 通过将人体和物体建模为独立的高斯集合，并引入 2D 表面流形上的物体高斯学习，实现精细的动态物体重建。
3. 实验表明，GASPACHO 在多个基准测试中实现了高质量的重建，并支持对新型人与物体交互的可控合成。

## 📝 摘要（中文）

GASPACHO 是一种从多视角 RGB 视频中生成逼真且可控的人与物体交互渲染的方法。与以往仅重建人体并将物体视为背景的工作不同，GASPACHO 同时恢复人体和交互物体的可动画模板，并将它们表示为不同的高斯集合，从而允许在新的相机视角下，对不同姿势的新型人与物体交互进行可控渲染。该方法提出了一种新的公式，在底层 2D 表面流形上学习物体高斯分布，而不是在 3D 体积中，从而为动态物体重建产生更清晰、更精细的物体细节。此外，还提出了一种高斯空间中的接触约束，用于规范人与物体之间的关系，并实现自然、物理上合理的动画。在 BEHAVE、NeuralDome 和 DNA-Rendering 三个基准测试中，GASPACHO 在严重遮挡下实现了高质量的重建，并支持对新型人与物体交互的可控合成。该方法还允许在 3D 场景中组合人和物体，并首次展示了神经渲染可用于在不同场景中可控地生成与动态物体交互的逼真人。

## 🔬 方法详解

**问题定义**：现有方法在处理人与物体交互时，通常只关注人体重建，将物体视为静态背景，无法实现对交互物体的精细控制和动画。此外，直接在 3D 体积中学习物体高斯分布容易导致细节模糊。

**核心思路**：GASPACHO 的核心在于同时重建人体和交互物体，并将它们建模为独立的可动画高斯集合。通过在 2D 表面流形上学习物体高斯分布，可以获得更清晰、更精细的物体细节。此外，引入高斯空间中的接触约束，可以规范人与物体之间的关系，实现更自然的交互动画。

**技术框架**：GASPACHO 的整体框架包括以下几个主要阶段：1) 多视角 RGB 视频输入；2) 人体和物体的高斯表示初始化；3) 在 2D 表面流形上学习物体高斯分布；4) 引入高斯空间中的接触约束；5) 优化高斯参数，实现高质量的重建和可控渲染。

**关键创新**：GASPACHO 的关键创新在于：1) 同时重建人体和交互物体，并将它们建模为独立的可动画高斯集合；2) 在 2D 表面流形上学习物体高斯分布，从而获得更清晰、更精细的物体细节；3) 引入高斯空间中的接触约束，用于规范人与物体之间的关系，实现更自然的交互动画。

**关键设计**：GASPACHO 的关键设计包括：1) 使用 3D 高斯溅射进行渲染；2) 定义了在 2D 表面流形上学习物体高斯分布的损失函数，鼓励高斯分布与表面对齐；3) 设计了高斯空间中的接触约束，通过惩罚高斯之间的穿透来规范人与物体之间的关系；4) 使用 Adam 优化器优化高斯参数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.09342/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.09342/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2503.09342/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

GASPACHO 在 BEHAVE、NeuralDome 和 DNA-Rendering 三个基准测试中取得了显著的成果。实验结果表明，GASPACHO 在严重遮挡下实现了高质量的重建，并支持对新型人与物体交互的可控合成。与现有方法相比，GASPACHO 能够生成更逼真、更精细的人与物体交互场景。

## 🎯 应用场景

GASPACHO 在虚拟现实、增强现实、游戏开发和电影制作等领域具有广泛的应用前景。它可以用于生成逼真且可控的人与物体交互场景，例如虚拟试穿、人机协作模拟、以及电影特效制作。该技术还可以用于创建更具沉浸感和互动性的虚拟体验。

## 📄 摘要（原文）

> We present GASPACHO, a method for generating photorealistic, controllable renderings of human-object interactions from multi-view RGB video. Unlike prior work that reconstructs only the human and treats objects as background, GASPACHO simultaneously recovers animatable templates for both the human and the interacting object as distinct sets of Gaussians, thereby allowing for controllable renderings of novel human object interactions in different poses from novel-camera viewpoints. We introduce a novel formulation that learns object Gaussians on an underlying 2D surface manifold rather than in 3D volume, yielding sharper, fine-grained object details for dynamic object reconstruction. We further propose a contact constraint in Gaussian space that regularizes human-object relations and enables natural, physically plausible animation. Across three benchmarks - BEHAVE, NeuralDome, and DNA-Rendering - GASPACHO achieves high-quality reconstructions under heavy occlusion and supports controllable synthesis of novel human-object interactions. We also demonstrate that our method allows for composition of humans and objects in 3D scenes and for the first time showcase that neural rendering can be used for the controllable generation of photoreal humans interacting with dynamic objects in diverse scenes. Our results are available at:this https URL

