---
layout: default
title: Streaming Drag-Oriented Interactive Video Manipulation: Drag Anything, Anytime!
---

# Streaming Drag-Oriented Interactive Video Manipulation: Drag Anything, Anytime!

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03550" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03550v2</a>
  <a href="https://arxiv.org/pdf/2510.03550.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03550v2" onclick="toggleFavorite(this, '2510.03550v2', 'Streaming Drag-Oriented Interactive Video Manipulation: Drag Anything, Anytime!')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junbao Zhou, Yuan Zhou, Kesen Zhao, Qingshan Xu, Beier Zhu, Richang Hong, Hanwang Zhang

**分类**: cs.CV

**发布日期**: 2025-10-03 (更新: 2025-10-20)

---

## 💡 一句话要点

**提出DragStream，实现基于拖拽的流式交互视频编辑，支持任意对象、任意时刻的精细控制。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视频编辑` `交互式操作` `流式生成` `扩散模型` `拖拽操作`

## 📋 核心要点

1. 现有自回归视频扩散模型难以实现流式、精细的控制，无法保证输出与用户期望一致。
2. 提出DragStream，通过自适应分布自校正和空间-频率选择性优化，解决潜在分布漂移和上下文干扰问题。
3. 实验证明DragStream能有效集成到现有模型中，实现高质量的流式拖拽交互视频编辑。

## 📝 摘要（中文）

本文提出了一项新的任务：流式拖拽导向的交互视频编辑(REVEL)，旨在让用户能够通过精细的交互式拖拽，在任意时刻修改生成的视频中的任意对象。与DragVideo和SG-I2V相比，REVEL统一了拖拽式视频操作，将其视为编辑和动画视频帧，支持用户指定的平移、变形和旋转效果，使拖拽操作更加通用。在解决REVEL任务时，我们观察到：(i)拖拽引起的扰动在潜在空间中累积，导致严重的潜在分布漂移，从而停止拖拽过程；(ii)流式拖拽容易受到上下文帧的干扰，从而产生视觉上不自然的结果。因此，我们提出了一种无需训练的方法DragStream，包括：(i)一种自适应分布自校正策略，利用相邻帧的统计信息来有效地约束潜在嵌入的漂移；(ii)一种空间-频率选择性优化机制，允许模型充分利用上下文信息，同时通过选择性地传播视觉线索来减轻其干扰。我们的方法可以无缝集成到现有的自回归视频扩散模型中，并且大量的实验有力地证明了DragStream的有效性。

## 🔬 方法详解

**问题定义**：现有方法在流式视频生成中，难以实现用户交互式的精细控制，尤其是在视频生成过程中进行实时的、基于拖拽的编辑。现有的DragVideo和SG-I2V方法虽然支持拖拽，但功能有限，无法支持复杂的形变和旋转，并且在流式生成中容易出现潜在分布漂移和上下文干扰，导致生成结果不自然或拖拽失败。

**核心思路**：DragStream的核心思路是通过两个关键策略来解决流式拖拽编辑中的问题：一是自适应分布自校正，用于约束潜在空间中的漂移；二是空间-频率选择性优化，用于在利用上下文信息的同时，减轻其干扰。通过这两个策略，DragStream能够在流式生成过程中保持编辑的稳定性和自然性。

**技术框架**：DragStream是一个训练无关的方法，可以集成到现有的自回归视频扩散模型中。其主要流程包括：首先，利用视频扩散模型生成初始视频帧；然后，用户通过拖拽指定编辑目标；接下来，DragStream利用自适应分布自校正策略来约束潜在空间，并利用空间-频率选择性优化机制来优化生成过程；最后，模型生成经过编辑的视频帧，并重复该过程以实现流式编辑。

**关键创新**：DragStream的关键创新在于其自适应分布自校正策略和空间-频率选择性优化机制。自适应分布自校正能够根据相邻帧的统计信息动态调整潜在空间的分布，从而避免漂移；空间-频率选择性优化则能够根据图像的空间和频率特征，选择性地传播上下文信息，从而在利用上下文的同时，避免不必要的干扰。

**关键设计**：自适应分布自校正策略通过计算相邻帧的潜在嵌入的均值和方差，并利用这些统计信息来约束当前帧的潜在嵌入。空间-频率选择性优化机制则通过对图像进行傅里叶变换，并在频域上选择性地保留或抑制某些频率分量，从而实现对上下文信息的选择性利用。具体的参数设置和损失函数细节在论文中有详细描述（未知）。

## 📊 实验亮点

实验结果表明，DragStream能够有效地解决流式拖拽编辑中的潜在分布漂移和上下文干扰问题，生成高质量的编辑视频。与现有的DragVideo和SG-I2V方法相比，DragStream在编辑的稳定性和自然性方面均有显著提升（具体数据未知）。此外，DragStream无需训练，可以方便地集成到现有的自回归视频扩散模型中。

## 🎯 应用场景

DragStream具有广泛的应用前景，例如视频游戏开发、电影特效制作、在线教育、社交媒体内容创作等。用户可以利用DragStream轻松地对生成的视频进行个性化编辑，创造出更符合自己需求的视频内容。该技术还可以应用于虚拟现实和增强现实等领域，为用户提供更具沉浸感的交互体验。

## 📄 摘要（原文）

> Achieving streaming, fine-grained control over the outputs of autoregressive video diffusion models remains challenging, making it difficult to ensure that they consistently align with user expectations. To bridge this gap, we propose \textbf{stReaming drag-oriEnted interactiVe vidEo manipuLation (REVEL)}, a new task that enables users to modify generated videos \emph{anytime} on \emph{anything} via fine-grained, interactive drag. Beyond DragVideo and SG-I2V, REVEL unifies drag-style video manipulation as editing and animating video frames with both supporting user-specified translation, deformation, and rotation effects, making drag operations versatile. In resolving REVEL, we observe: \emph{i}) drag-induced perturbations accumulate in latent space, causing severe latent distribution drift that halts the drag process; \emph{ii}) streaming drag is easily disturbed by context frames, thereby yielding visually unnatural outcomes. We thus propose a training-free approach, \textbf{DragStream}, comprising: \emph{i}) an adaptive distribution self-rectification strategy that leverages neighboring frames' statistics to effectively constrain the drift of latent embeddings; \emph{ii}) a spatial-frequency selective optimization mechanism, allowing the model to fully exploit contextual information while mitigating its interference via selectively propagating visual cues along generation. Our method can be seamlessly integrated into existing autoregressive video diffusion models, and extensive experiments firmly demonstrate the effectiveness of our DragStream.

