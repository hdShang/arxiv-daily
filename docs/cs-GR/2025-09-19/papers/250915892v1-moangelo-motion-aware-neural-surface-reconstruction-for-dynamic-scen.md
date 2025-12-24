---
layout: default
title: "MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes"
---

# MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15892" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15892v1</a>
  <a href="https://arxiv.org/pdf/2509.15892.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15892v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15892v1', 'MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamed Ebbed, Zorah Lähner

**分类**: cs.GR, cs.AI, cs.CV

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**MoAngelo：用于动态场景的运动感知神经表面重建**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态场景重建` `神经表面重建` `变形场` `多视角视频` `NeuralAngelo` `几何重建` `运动跟踪` `三维重建`

## 📋 核心要点

1. 动态场景重建面临计算和表示挑战，现有方法在新视角合成上表现较好，但在几何细节上存在不足，重建的网格易产生噪声或过于平滑。
2. MoAngelo的核心思想是利用高质量的静态重建结果作为模板，通过优化变形场来跟踪和细化动态场景，从而实现高精度的动态重建。
3. 该方法在ActorsHQ数据集上取得了优于现有技术的重建精度，验证了其在动态场景重建方面的有效性。

## 📝 摘要（中文）

从多视角视频中重建动态场景是计算机视觉领域的一个根本性挑战。虽然最近的神经表面重建方法在静态3D重建中取得了显著成果，但将这些方法扩展到动态场景并保持相当的质量，会带来巨大的计算和表示挑战。现有的动态方法侧重于新视角合成，因此，它们提取的网格往往存在噪声。即使是旨在实现几何保真度的方法，由于问题的不适定性，也经常导致过于平滑的网格。我们提出了一个用于高细节动态重建的新框架，该框架扩展了静态3D重建方法NeuralAngelo以在动态设置中工作。为此，我们首先使用NeuralAngelo从初始帧进行高质量的模板场景重建，然后联合优化变形场，以跟踪模板并根据时间序列对其进行细化。这种灵活的模板允许更新几何体，以包括无法用变形场建模的变化，例如遮挡部分或拓扑结构的变化。我们在ActorsHQ数据集上展示了与先前最先进方法相比的卓越重建精度。

## 🔬 方法详解

**问题定义**：论文旨在解决从多视角视频中进行高精度动态场景重建的问题。现有方法，特别是那些侧重于新视角合成的方法，在动态场景下重建的几何细节不足，容易产生噪声或过于平滑的网格，难以满足对几何精度要求高的应用。

**核心思路**：论文的核心思路是利用静态场景重建方法NeuralAngelo生成的高质量初始帧重建作为模板，然后通过优化变形场来跟踪和细化该模板，使其适应动态场景的变化。这种方法结合了静态重建的精度和动态跟踪的灵活性。

**技术框架**：MoAngelo框架主要包含以下几个阶段：1) 使用NeuralAngelo从初始帧重建高质量的静态场景模板；2) 引入变形场，用于跟踪模板并使其适应后续帧中的动态变化；3) 联合优化变形场和模板几何体，以提高重建精度；4) 允许在模板上进行几何更新，以处理变形场无法建模的情况，如遮挡或拓扑变化。

**关键创新**：该方法最重要的创新点在于将静态重建和动态跟踪相结合，利用高质量的静态重建结果作为动态重建的先验信息，并通过变形场进行精细的动态调整。此外，允许对模板进行几何更新，增强了对复杂动态变化的适应性。

**关键设计**：具体的参数设置、损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。但可以推测，变形场的优化可能涉及到正则化项，以保证变形场的平滑性。几何更新的策略可能涉及到对重建结果的置信度评估，以及对遮挡区域的特殊处理。

## 📊 实验亮点

论文在ActorsHQ数据集上进行了实验，结果表明，MoAngelo在动态场景重建精度方面优于现有的state-of-the-art方法。具体的性能数据和提升幅度在摘要中未给出，属于未知信息，但强调了其在重建精度上的优势。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、电影特效、游戏开发等领域。高精度的动态场景重建能够为用户提供更逼真的沉浸式体验，并为动画制作和视觉特效提供更强大的工具。此外，该技术还可用于机器人导航、自动驾驶等领域，帮助机器人更好地理解和感知周围环境。

## 📄 摘要（原文）

> Dynamic scene reconstruction from multi-view videos remains a fundamental challenge in computer vision. While recent neural surface reconstruction methods have achieved remarkable results in static 3D reconstruction, extending these approaches with comparable quality for dynamic scenes introduces significant computational and representational challenges. Existing dynamic methods focus on novel-view synthesis, therefore, their extracted meshes tend to be noisy. Even approaches aiming for geometric fidelity often result in too smooth meshes due to the ill-posedness of the problem. We present a novel framework for highly detailed dynamic reconstruction that extends the static 3D reconstruction method NeuralAngelo to work in dynamic settings. To that end, we start with a high-quality template scene reconstruction from the initial frame using NeuralAngelo, and then jointly optimize deformation fields that track the template and refine it based on the temporal sequence. This flexible template allows updating the geometry to include changes that cannot be modeled with the deformation field, for instance occluded parts or the changes in the topology. We show superior reconstruction accuracy in comparison to previous state-of-the-art methods on the ActorsHQ dataset.

