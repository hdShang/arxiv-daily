---
layout: default
title: "AutoScape: Geometry-Consistent Long-Horizon Scene Generation"
---

# AutoScape: Geometry-Consistent Long-Horizon Scene Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20726" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20726v1</a>
  <a href="https://arxiv.org/pdf/2510.20726.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20726v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.20726v1', 'AutoScape: Geometry-Consistent Long-Horizon Scene Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiacheng Chen, Ziyu Jiang, Mingfu Liang, Bingbing Zhuang, Jong-Chyi Su, Sparsh Garg, Ying Wu, Manmohan Chandraker

**分类**: cs.CV

**发布日期**: 2025-10-23

**备注**: ICCV 2025. Project page: https://auto-scape.github.io

---

## 💡 一句话要点

**AutoScape：提出几何一致的长时程驾驶场景生成框架**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `长时程生成` `场景生成` `RGB-D扩散模型` `几何一致性` `自动驾驶仿真`

## 📋 核心要点

1. 现有长时程场景生成方法难以保持几何一致性，导致视频不真实。
2. AutoScape通过RGB-D扩散模型生成几何一致的关键帧，并用warp一致性引导采样。
3. 实验表明，AutoScape生成的20秒驾驶视频在FID和FVD指标上显著优于现有方法。

## 📝 摘要（中文）

本文提出AutoScape，一个长时程驾驶场景生成框架。其核心是一个新颖的RGB-D扩散模型，该模型迭代地生成稀疏的、几何一致的关键帧，作为场景外观和几何形状的可靠锚点。为了保持长程几何一致性，该模型1)在共享潜在空间中联合处理图像和深度，2)显式地以先前生成的关键帧的现有场景几何形状（即，渲染的点云）为条件，并且3)利用warp一致性引导来控制采样过程。给定高质量的RGB-D关键帧，视频扩散模型在它们之间进行插值，以生成密集且连贯的视频帧。AutoScape生成超过20秒的逼真且几何一致的驾驶视频，将长时程FID和FVD分数分别比现有技术水平提高了48.6％和43.0％。

## 🔬 方法详解

**问题定义**：现有长时程驾驶场景生成方法难以维持长时间的几何一致性，导致生成的视频出现扭曲、变形等不真实现象。这是因为长时程生成需要对场景的结构和运动进行建模，而现有方法往往缺乏对几何信息的有效利用和约束。

**核心思路**：AutoScape的核心思路是首先生成稀疏但几何一致的关键帧，然后利用这些关键帧作为锚点，通过视频扩散模型插值生成中间帧。通过在关键帧生成阶段保证几何一致性，可以有效地避免长时程生成中的几何漂移问题。

**技术框架**：AutoScape框架包含两个主要阶段：1) RGB-D关键帧生成阶段：使用RGB-D扩散模型迭代生成稀疏的关键帧，并显式地以先前生成的关键帧的几何信息（点云）为条件。2) 视频插值阶段：使用视频扩散模型在关键帧之间进行插值，生成密集且连贯的视频帧。

**关键创新**：AutoScape的关键创新在于RGB-D扩散模型和warp一致性引导。RGB-D扩散模型能够在共享潜在空间中联合处理图像和深度信息，从而保证生成关键帧的几何一致性。warp一致性引导则通过约束相邻关键帧之间的光流一致性，进一步提高了几何一致性。

**关键设计**：RGB-D扩散模型采用U-Net结构，并使用Transformer进行注意力建模。损失函数包括图像重建损失、深度重建损失和warp一致性损失。warp一致性损失通过计算相邻关键帧之间的光流，并约束光流的反向warp误差来实现。

## 📊 实验亮点

AutoScape在长时程驾驶场景生成任务上取得了显著的性能提升。实验结果表明，AutoScape生成的20秒驾驶视频在FID和FVD指标上分别比现有最佳方法提高了48.6%和43.0%。这些结果表明，AutoScape能够生成更逼真、更几何一致的驾驶场景。

## 🎯 应用场景

AutoScape具有广泛的应用前景，例如自动驾驶仿真、游戏场景生成、电影特效制作等。它可以用于生成逼真的驾驶场景，帮助自动驾驶系统进行训练和测试。此外，AutoScape还可以用于创建各种虚拟环境，为游戏和电影制作提供丰富的素材。

## 📄 摘要（原文）

> This paper proposes AutoScape, a long-horizon driving scene generation framework. At its core is a novel RGB-D diffusion model that iteratively generates sparse, geometrically consistent keyframes, serving as reliable anchors for the scene's appearance and geometry. To maintain long-range geometric consistency, the model 1) jointly handles image and depth in a shared latent space, 2) explicitly conditions on the existing scene geometry (i.e., rendered point clouds) from previously generated keyframes, and 3) steers the sampling process with a warp-consistent guidance. Given high-quality RGB-D keyframes, a video diffusion model then interpolates between them to produce dense and coherent video frames. AutoScape generates realistic and geometrically consistent driving videos of over 20 seconds, improving the long-horizon FID and FVD scores over the prior state-of-the-art by 48.6\% and 43.0\%, respectively.

