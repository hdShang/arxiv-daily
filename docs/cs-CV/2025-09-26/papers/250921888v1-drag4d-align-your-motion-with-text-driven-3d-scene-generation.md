---
layout: default
title: "Drag4D: Align Your Motion with Text-Driven 3D Scene Generation"
---

# Drag4D: Align Your Motion with Text-Driven 3D Scene Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21888" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21888v1</a>
  <a href="https://arxiv.org/pdf/2509.21888.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21888v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21888v1', 'Drag4D: Align Your Motion with Text-Driven 3D Scene Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minjun Kang, Inkyu Shin, Taeyeop Lee, In So Kweon, Kuk-Jin Yoon

**分类**: cs.CV

**发布日期**: 2025-09-26

**备注**: version 1

---

## 💡 一句话要点

**Drag4D：提出文本驱动的3D场景生成框架，实现交互式物体运动控制**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景生成` `文本驱动` `运动控制` `视频扩散模型` `高斯溅射`

## 📋 核心要点

1. 现有方法难以在文本驱动的3D场景生成中精确控制物体的运动轨迹，缺乏交互性。
2. Drag4D通过3D复制粘贴、物理感知定位和运动条件视频扩散，实现了用户定义的物体运动与3D场景的融合。
3. 实验结果表明，Drag4D能够生成高质量的3D场景，并精确控制物体的运动轨迹，效果显著。

## 📝 摘要（中文）

Drag4D是一个交互式框架，它将物体运动控制集成到文本驱动的3D场景生成中。该框架允许用户为从单张图像生成的3D物体定义3D轨迹，并将其无缝集成到高质量的3D背景中。Drag4D流程包括三个阶段。首先，通过应用带有全景图像和修复的新视角的2D高斯溅射，增强文本到3D背景的生成，从而实现密集且视觉上完整的3D重建。其次，给定目标物体的参考图像，引入3D复制粘贴方法：使用现成的图像到3D模型在完整的3D网格中提取目标实例，并将其无缝合成到生成的3D场景中。然后通过物理感知的物体位置学习将物体网格定位在3D场景中，确保精确的空间对齐。最后，空间对齐的物体沿着用户定义的3D轨迹进行时间动画处理。为了减轻运动幻觉并确保视角一致的时间对齐，开发了一种部分增强的、运动条件视频扩散模型，该模型处理多视角图像对及其投影的2D轨迹。通过对每个阶段和最终结果的评估，证明了统一架构的有效性，展示了用户控制的物体运动与高质量3D背景的和谐对齐。

## 🔬 方法详解

**问题定义**：现有文本到3D场景生成方法缺乏对场景中物体运动的精确控制，用户难以交互式地指定物体的运动轨迹。此外，将物体无缝集成到3D场景中，并保证运动过程中的视角一致性是一个挑战。

**核心思路**：Drag4D的核心思路是将物体运动控制集成到文本驱动的3D场景生成流程中，通过3D复制粘贴将目标物体添加到场景中，利用物理感知的物体位置学习确保物体在场景中的合理位置，并使用运动条件视频扩散模型生成时间上连贯且视角一致的运动动画。

**技术框架**：Drag4D包含三个主要阶段：1) 3D背景生成：使用2D高斯溅射和全景图像生成高质量的3D背景。2) 3D物体复制粘贴：从参考图像中提取3D物体网格，并将其无缝合成到3D场景中。3) 运动动画生成：根据用户定义的3D轨迹，使用运动条件视频扩散模型生成物体的运动动画。

**关键创新**：Drag4D的关键创新在于：1) 提出了一个完整的交互式框架，将物体运动控制集成到文本驱动的3D场景生成中。2) 使用物理感知的物体位置学习，确保物体在场景中的合理位置。3) 开发了一种部分增强的、运动条件视频扩散模型，用于生成视角一致的运动动画。

**关键设计**：在3D背景生成阶段，使用了2D高斯溅射技术，并结合全景图像和修复的新视角，以提高重建质量。在物体位置学习阶段，使用了物理引擎来模拟物体与场景的交互，并学习一个位置预测器。在运动动画生成阶段，使用了运动条件视频扩散模型，该模型以多视角图像对和投影的2D轨迹作为输入，生成视角一致的运动动画。

## 📊 实验亮点

论文通过实验验证了Drag4D框架的有效性。实验结果表明，Drag4D能够生成高质量的3D场景，并精确控制物体的运动轨迹。与现有方法相比，Drag4D在物体集成和运动动画生成方面取得了显著的提升，能够生成更逼真、更自然的3D场景。

## 🎯 应用场景

Drag4D可应用于游戏开发、电影制作、虚拟现实和增强现实等领域。用户可以利用该框架快速生成带有自定义运动物体的3D场景，例如，在虚拟现实游戏中创建逼真的环境，或在电影制作中添加特效。

## 📄 摘要（原文）

> We introduce Drag4D, an interactive framework that integrates object motion control within text-driven 3D scene generation. This framework enables users to define 3D trajectories for the 3D objects generated from a single image, seamlessly integrating them into a high-quality 3D background. Our Drag4D pipeline consists of three stages. First, we enhance text-to-3D background generation by applying 2D Gaussian Splatting with panoramic images and inpainted novel views, resulting in dense and visually complete 3D reconstructions. In the second stage, given a reference image of the target object, we introduce a 3D copy-and-paste approach: the target instance is extracted in a full 3D mesh using an off-the-shelf image-to-3D model and seamlessly composited into the generated 3D scene. The object mesh is then positioned within the 3D scene via our physics-aware object position learning, ensuring precise spatial alignment. Lastly, the spatially aligned object is temporally animated along a user-defined 3D trajectory. To mitigate motion hallucination and ensure view-consistent temporal alignment, we develop a part-augmented, motion-conditioned video diffusion model that processes multiview image pairs together with their projected 2D trajectories. We demonstrate the effectiveness of our unified architecture through evaluations at each stage and in the final results, showcasing the harmonized alignment of user-controlled object motion within a high-quality 3D background.

