---
layout: default
title: "RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space"
---

# RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08588" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08588v1</a>
  <a href="https://arxiv.org/pdf/2508.08588.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08588v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08588v1', 'RealisMotion: Decomposed Human Motion Control and Video Generation in the World Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyun Liang, Jingkai Zhou, Shikai Li, Chenjie Cao, Lei Sun, Yichen Qian, Weihua Chen, Fan Wang

**分类**: cs.CV, eess.IV

**发布日期**: 2025-08-12

**备注**: Project page: https://jingyunliang.github.io/RealisMotion

---

## 💡 一句话要点

**提出RealisMotion以解决人类运动控制与视频生成的挑战**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `人类动作生成` `视频生成` `3D运动控制` `元素解耦` `文本到视频`

## 📋 核心要点

1. 现有方法在生成视频时无法独立控制前景、背景、轨迹和动作，限制了灵活性。
2. 本文提出的框架通过3D空间中的运动编辑和元素解耦，实现了灵活的组合与控制。
3. 在基准数据集和实际案例中，实验结果显示该方法在可控性和视频质量上均优于现有技术。

## 📝 摘要（中文）

生成具有真实感和可控动作的人类视频是一项具有挑战性的任务。现有方法虽然能够生成视觉上引人注目的视频，但在前景主体、背景视频、人类轨迹和动作模式四个关键视频元素的独立控制上存在不足。本文提出了一种分解的人类运动控制与视频生成框架，明确将运动与外观、主体与背景、动作与轨迹解耦，从而实现这些元素的灵活组合。我们首先构建了一个基于地面的3D世界坐标系统，并在3D空间中直接进行运动编辑。实验结果表明，该方法在元素可控性和整体视频质量上均达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频生成方法在运动控制和元素组合上的不足，特别是无法独立控制视频中的前景、背景、轨迹和动作的问题。

**核心思路**：我们提出的框架通过在3D空间中进行运动编辑，明确解耦各个元素，使得用户可以灵活组合不同的动作和背景，从而实现更高的控制能力。

**技术框架**：整体架构包括三个主要模块：首先构建一个地面感知的3D世界坐标系统；其次，通过将编辑后的2D轨迹反投影到3D空间进行轨迹控制；最后，利用现代文本到视频的扩散变换模型进行视频生成。

**关键创新**：最重要的创新在于将运动与外观、主体与背景、动作与轨迹进行明确解耦，这种设计使得生成的视频在元素组合上具有更高的灵活性和可控性。

**关键设计**：在技术细节上，我们采用了焦距校准和坐标变换来实现2D到3D的轨迹反投影，并通过速度对齐和方向调整来优化运动控制。同时，动作可以通过动作库提供或通过文本生成，确保了多样性和灵活性。

## 📊 实验亮点

实验结果表明，RealisMotion在元素可控性和视频质量上均达到了最先进的性能，相较于基线方法，元素控制能力提升了XX%，整体视频质量评分提高了YY%。

## 🎯 应用场景

该研究的潜在应用领域包括电影制作、游戏开发和虚拟现实等，能够为创作者提供更高效的工具来生成复杂的人类动作视频，提升内容创作的灵活性和效率。未来，该技术可能在社交媒体和在线教育等领域产生深远影响。

## 📄 摘要（原文）

> Generating human videos with realistic and controllable motions is a challenging task. While existing methods can generate visually compelling videos, they lack separate control over four key video elements: foreground subject, background video, human trajectory and action patterns. In this paper, we propose a decomposed human motion control and video generation framework that explicitly decouples motion from appearance, subject from background, and action from trajectory, enabling flexible mix-and-match composition of these elements. Concretely, we first build a ground-aware 3D world coordinate system and perform motion editing directly in the 3D space. Trajectory control is implemented by unprojecting edited 2D trajectories into 3D with focal-length calibration and coordinate transformation, followed by speed alignment and orientation adjustment; actions are supplied by a motion bank or generated via text-to-motion methods. Then, based on modern text-to-video diffusion transformer models, we inject the subject as tokens for full attention, concatenate the background along the channel dimension, and add motion (trajectory and action) control signals by addition. Such a design opens up the possibility for us to generate realistic videos of anyone doing anything anywhere. Extensive experiments on benchmark datasets and real-world cases demonstrate that our method achieves state-of-the-art performance on both element-wise controllability and overall video quality.

