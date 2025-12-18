---
layout: default
title: Color3D: Controllable and Consistent 3D Colorization with Personalized Colorizer
---

# Color3D: Controllable and Consistent 3D Colorization with Personalized Colorizer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10152" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10152v1</a>
  <a href="https://arxiv.org/pdf/2510.10152.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10152v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.10152v1', 'Color3D: Controllable and Consistent 3D Colorization with Personalized Colorizer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yecong Wan, Mingwen Shao, Renlong Wu, Wangmeng Zuo

**分类**: cs.CV

**发布日期**: 2025-10-11

**备注**: Project Page https://yecongwan.github.io/Color3D/

**🔗 代码/项目**: [PROJECT_PAGE](https://yecongwan.github.io/Color3D/)

---

## 💡 一句话要点

**Color3D：基于个性化着色器的可控一致3D着色框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D着色` `颜色一致性` `个性化着色器` `高斯溅射` `动态场景` `用户控制` `Lab颜色空间`

## 📋 核心要点

1. 现有3D着色方法在保持多视角一致性时，往往牺牲色彩丰富度和用户可控性，限制了应用范围。
2. Color3D通过个性化着色器，学习关键视图的颜色映射，并将其一致地传播到其他视图和时间帧。
3. 实验表明，Color3D在静态和动态场景中均能实现更一致、色彩更丰富的渲染，并支持用户精确控制。

## 📝 摘要（中文）

本文提出Color3D，一个高度适应性的框架，用于从单色输入中着色静态和动态3D场景，提供具有灵活用户引导控制的视觉多样且色彩鲜艳的重建结果。与现有方法仅关注静态场景并通过平均颜色变化来强制多视图一致性（不可避免地牺牲了色度丰富性和可控性）不同，我们的方法能够在确保跨视图和跨时间一致性的同时，保持颜色多样性和可操纵性。我们的核心思想是仅着色单个关键视图，然后微调个性化着色器以将其颜色传播到新视图和时间步。通过个性化，着色器学习参考视图下的场景特定确定性颜色映射，使其能够通过其固有的归纳偏差将相应的颜色一致地投影到新视图和视频帧中的内容。训练完成后，个性化着色器可用于推断所有其他图像的一致色度，从而能够使用专用的Lab颜色空间高斯溅射表示直接重建彩色3D场景。所提出的框架巧妙地将复杂的3D着色重铸为更易于处理的单图像范例，从而可以无缝集成任意图像着色模型，并具有增强的灵活性和可控性。在各种静态和动态3D着色基准上的大量实验证实，我们的方法可以提供更一致和色度丰富的渲染，并具有精确的用户控制。

## 🔬 方法详解

**问题定义**：现有的3D着色方法主要集中在静态场景，并且为了保证多视角一致性，通常采用平均颜色变化的方式，这不可避免地牺牲了色彩的丰富度和用户控制的灵活性。因此，如何在保证跨视角和跨时间一致性的同时，实现色彩多样性和用户可控性，是本文要解决的核心问题。

**核心思路**：Color3D的核心思路是将复杂的3D着色问题转化为一个更易于处理的单图像着色问题。具体来说，该方法首先对单个关键视图进行着色，然后训练一个个性化的着色器，使其能够学习该关键视图的颜色映射，并将该颜色映射一致地传播到其他视图和时间帧。通过这种方式，Color3D能够在保证一致性的同时，保持色彩的多样性和用户控制的灵活性。

**技术框架**：Color3D的整体框架包括以下几个主要步骤：1) 选择一个关键视图；2) 使用任意图像着色模型对该关键视图进行着色；3) 使用关键视图的着色结果来微调一个个性化的着色器；4) 使用训练好的个性化着色器对所有其他视图进行着色；5) 使用着色后的图像重建彩色3D场景，采用Lab颜色空间高斯溅射表示。

**关键创新**：Color3D最重要的技术创新点在于引入了个性化着色器的概念。通过对每个场景训练一个特定的着色器，Color3D能够学习到该场景特有的颜色映射，从而实现更一致和更自然的着色效果。与现有方法相比，Color3D避免了直接平均颜色变化，而是通过学习场景特定的颜色映射来保证一致性，这使得Color3D能够在保持色彩多样性的同时，实现更好的着色效果。

**关键设计**：Color3D的关键设计包括：1) 使用Lab颜色空间进行颜色表示，这有助于更好地分离亮度和色度信息；2) 使用高斯溅射表示3D场景，这使得Color3D能够直接从着色后的图像重建彩色3D场景；3) 个性化着色器的网络结构和损失函数的设计，需要根据具体的图像着色模型进行调整，以保证着色器能够学习到有效的颜色映射。

## 📊 实验亮点

Color3D在多个静态和动态3D着色基准测试中取得了显著的成果。相较于现有方法，Color3D能够生成更一致、色彩更丰富的渲染结果，并且支持用户对颜色进行精确控制。实验结果表明，Color3D在色彩多样性、一致性和用户可控性方面均优于现有方法。

## 🎯 应用场景

Color3D在虚拟现实、增强现实、游戏开发、电影制作等领域具有广泛的应用前景。它可以用于快速生成高质量的彩色3D模型，提升用户体验，并降低内容创作的成本。此外，Color3D还可以应用于文物修复、医学影像等领域，为相关研究提供更丰富的视觉信息。

## 📄 摘要（原文）

> In this work, we present Color3D, a highly adaptable framework for colorizing both static and dynamic 3D scenes from monochromatic inputs, delivering visually diverse and chromatically vibrant reconstructions with flexible user-guided control. In contrast to existing methods that focus solely on static scenarios and enforce multi-view consistency by averaging color variations which inevitably sacrifice both chromatic richness and controllability, our approach is able to preserve color diversity and steerability while ensuring cross-view and cross-time consistency. In particular, the core insight of our method is to colorize only a single key view and then fine-tune a personalized colorizer to propagate its color to novel views and time steps. Through personalization, the colorizer learns a scene-specific deterministic color mapping underlying the reference view, enabling it to consistently project corresponding colors to the content in novel views and video frames via its inherent inductive bias. Once trained, the personalized colorizer can be applied to infer consistent chrominance for all other images, enabling direct reconstruction of colorful 3D scenes with a dedicated Lab color space Gaussian splatting representation. The proposed framework ingeniously recasts complicated 3D colorization as a more tractable single image paradigm, allowing seamless integration of arbitrary image colorization models with enhanced flexibility and controllability. Extensive experiments across diverse static and dynamic 3D colorization benchmarks substantiate that our method can deliver more consistent and chromatically rich renderings with precise user control. Project Page https://yecongwan.github.io/Color3D/.

