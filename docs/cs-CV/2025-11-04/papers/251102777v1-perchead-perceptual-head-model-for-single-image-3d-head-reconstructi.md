---
layout: default
title: PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction & Editing
---

# PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction & Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02777" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02777v1</a>
  <a href="https://arxiv.org/pdf/2511.02777.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02777v1" onclick="toggleFavorite(this, '2511.02777v1', 'PercHead: Perceptual Head Model for Single-Image 3D Head Reconstruction & Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antonio Oroz, Matthias Nießner, Tobias Kirschstein

**分类**: cs.CV

**发布日期**: 2025-11-04

**备注**: Project Page: https://antoniooroz.github.io/PercHead/ Video: https://www.youtube.com/watch?v=4hFybgTk4kE

**🔗 代码/项目**: [PROJECT_PAGE](https://antoniooroz.github.io/PercHead)

---

## 💡 一句话要点

**PercHead：提出基于感知的头部模型，用于单图像3D头部重建与编辑**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D头部重建` `语义编辑` `单图像重建` `感知监督` `高斯溅射` `ViT解码器` `DINOv2` `SAM2.1`

## 📋 核心要点

1. 单图像3D头部重建和编辑面临视角遮挡、弱监督和编辑模糊性等挑战。
2. PercHead利用双分支编码器和ViT解码器，结合DINOv2和SAM2.1的感知监督，实现高质量重建。
3. 实验表明，PercHead在novel-view synthesis中达到SOTA，并具备强大的3D语义编辑能力。

## 📝 摘要（中文）

本文提出PercHead，一种用于单图像3D头部重建和语义3D编辑的方法。由于严重的视角遮挡、弱感知监督以及3D空间编辑的模糊性，这两项任务都极具挑战性。我们开发了一个统一的基础模型，用于从单个输入图像重建视角一致的3D头部。该模型采用双分支编码器，后接基于ViT的解码器，通过迭代交叉注意力将2D特征提升到3D空间。渲染使用高斯溅射。我们方法的核心是一种基于DINOv2和SAM2.1的新型感知监督策略，它为几何和外观保真度提供了丰富的、泛化的信号。我们的模型在novel-view synthesis中实现了最先进的性能，并且与已建立的基线相比，对极端视角的鲁棒性表现出色。此外，通过交换编码器并微调网络，这个基础模型可以无缝扩展用于语义3D编辑。在这种变体中，我们通过两种不同的输入模态来解耦几何和风格：分割图用于控制几何，文本提示或参考图像用于指定外观。我们通过一个轻量级的交互式GUI突出了我们模型直观而强大的3D编辑能力，用户可以通过绘制分割图轻松地雕刻几何形状，并通过自然语言或图像提示来设计外观。

## 🔬 方法详解

**问题定义**：论文旨在解决单张图像3D头部重建和语义编辑问题。现有方法在处理视角遮挡、缺乏有效的感知监督以及3D编辑的模糊性方面存在不足，导致重建质量和编辑效果不佳。

**核心思路**：论文的核心思路是利用深度学习模型，结合新型的感知监督策略，从单张图像中推断出高质量的3D头部模型，并实现可控的语义编辑。通过解耦几何形状和外观风格，用户可以直观地修改3D头部。

**技术框架**：PercHead模型包含以下主要模块：1) 双分支编码器：提取输入图像的特征。2) 基于ViT的解码器：通过迭代交叉注意力将2D特征提升到3D空间，生成3D头部表示。3) 高斯溅射渲染器：将3D头部表示渲染成图像。4) 感知监督模块：利用DINOv2和SAM2.1提供几何和外观保真度的监督信号。在语义编辑模式下，编码器被替换，输入变为分割图（控制几何）和文本/图像提示（控制外观）。

**关键创新**：论文最重要的技术创新点在于提出了基于DINOv2和SAM2.1的感知监督策略。与传统的像素级或特征级监督相比，这种策略能够提供更丰富、更泛化的监督信号，从而提高重建质量和编辑效果。此外，模型解耦了几何形状和外观风格，使得语义编辑更加灵活和可控。

**关键设计**：模型使用双分支编码器提取图像特征，ViT解码器通过交叉注意力将2D特征提升到3D空间。损失函数包括重建损失、感知损失（基于DINOv2和SAM2.1）等。高斯溅射渲染器用于生成最终图像。在语义编辑模式下，分割图和文本/图像提示被分别编码，用于控制几何形状和外观风格。

## 📊 实验亮点

PercHead在novel-view synthesis任务上取得了state-of-the-art的性能。实验结果表明，PercHead在极端视角下具有更强的鲁棒性，能够生成高质量的3D头部模型。通过交互式GUI，用户可以轻松地进行3D头部语义编辑，例如改变发型、表情等。

## 🎯 应用场景

PercHead具有广泛的应用前景，包括虚拟现实/增强现实、游戏开发、数字内容创作、个性化头像生成、以及人脸识别和分析等领域。该技术可以用于创建逼真的3D虚拟形象，为用户提供更沉浸式的体验，并促进相关领域的发展。

## 📄 摘要（原文）

> We present PercHead, a method for single-image 3D head reconstruction and semantic 3D editing - two tasks that are inherently challenging due to severe view occlusions, weak perceptual supervision, and the ambiguity of editing in 3D space. We develop a unified base model for reconstructing view-consistent 3D heads from a single input image. The model employs a dual-branch encoder followed by a ViT-based decoder that lifts 2D features into 3D space through iterative cross-attention. Rendering is performed using Gaussian Splatting. At the heart of our approach is a novel perceptual supervision strategy based on DINOv2 and SAM2.1, which provides rich, generalized signals for both geometric and appearance fidelity. Our model achieves state-of-the-art performance in novel-view synthesis and, furthermore, exhibits exceptional robustness to extreme viewing angles compared to established baselines. Furthermore, this base model can be seamlessly extended for semantic 3D editing by swapping the encoder and finetuning the network. In this variant, we disentangle geometry and style through two distinct input modalities: a segmentation map to control geometry and either a text prompt or a reference image to specify appearance. We highlight the intuitive and powerful 3D editing capabilities of our model through a lightweight, interactive GUI, where users can effortlessly sculpt geometry by drawing segmentation maps and stylize appearance via natural language or image prompts.
>   Project Page: https://antoniooroz.github.io/PercHead Video: https://www.youtube.com/watch?v=4hFybgTk4kE

