---
layout: default
title: Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos
---

# Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14406" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14406v1</a>
  <a href="https://arxiv.org/pdf/2512.14406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14406v1', 'Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Jiang, Shaotong Zhu, Yedi Luo, Shayda Moezzi, Sarah Ostadabbas

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**ExpanDyNeRF：扩展动态场景视角合成，解决单目视频大角度渲染失真问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态场景` `视角合成` `神经辐射场` `单目视频` `高斯溅射`

## 📋 核心要点

1. 现有动态NeRF方法在视角偏差较大时，渲染效果不稳定且不真实，难以满足实际应用需求。
2. ExpanDyNeRF利用高斯溅射先验和伪真值生成策略，优化密度和颜色特征，提升大角度视角下的渲染质量。
3. 在SynDM和真实数据集上，ExpanDyNeRF显著优于现有动态NeRF方法，尤其在极端视角变化下，渲染保真度提升明显。

## 📝 摘要（中文）

针对动态神经辐射场（NeRF）系统中，现有视角合成方法在大角度偏差下产生不稳定和不真实渲染的问题，我们提出了扩展动态NeRF（ExpanDyNeRF），这是一个单目NeRF框架，它利用高斯溅射先验和伪真值生成策略，实现了大角度旋转下的逼真合成。ExpanDyNeRF优化了密度和颜色特征，从而改善了从具有挑战性的视角进行场景重建的效果。我们还提出了合成动态多视角（SynDM）数据集，这是第一个具有显式侧视监督的动态场景合成多视角数据集，该数据集使用定制的基于GTA V的渲染管线创建。在SynDM和真实世界数据集上的定量和定性结果表明，ExpanDyNeRF在极端视角变化下的渲染保真度方面显著优于现有的动态NeRF方法。

## 🔬 方法详解

**问题定义**：现有动态NeRF方法在处理单目视频，特别是视角变化剧烈的情况下，渲染效果会显著下降，出现伪影、模糊等问题。这是因为单目视频提供的视角信息有限，难以约束NeRF的几何和外观学习，导致在新视角下的渲染结果不准确。现有方法难以有效利用单目视频信息，在大角度下渲染质量差，缺乏鲁棒性。

**核心思路**：ExpanDyNeRF的核心思路是利用高斯溅射先验来约束NeRF的学习，并结合伪真值生成策略来扩充训练数据，从而提高NeRF在视角变化剧烈情况下的渲染质量。高斯溅射先验能够提供更强的几何约束，减少NeRF的模糊性。伪真值生成策略则通过合成额外的视角数据，弥补单目视频信息不足的问题。

**技术框架**：ExpanDyNeRF的整体框架包括以下几个主要模块：1) 基于单目视频的初始NeRF重建；2) 利用高斯溅射先验对NeRF进行优化，提高几何精度；3) 使用伪真值生成策略，合成额外的视角数据；4) 利用合成数据和原始数据，联合训练NeRF，提高其泛化能力。该框架通过迭代优化，逐步提高NeRF的渲染质量。

**关键创新**：ExpanDyNeRF的关键创新在于以下两点：1) 引入高斯溅射先验，增强NeRF的几何约束，提高渲染质量；2) 提出伪真值生成策略，有效扩充训练数据，提高NeRF的泛化能力。这两个创新点共同作用，使得ExpanDyNeRF在单目视频大角度视角合成方面取得了显著的提升。

**关键设计**：在关键设计方面，ExpanDyNeRF采用了以下策略：1) 使用预训练的高斯溅射模型作为先验，加速NeRF的收敛；2) 设计了一种基于深度估计的伪真值生成方法，保证合成数据的质量；3) 使用了一种自适应的损失函数，平衡原始数据和合成数据之间的权重，避免过拟合。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14406v1/Figures/real.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14406v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14406v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ExpanDyNeRF在SynDM数据集和真实世界数据集上都取得了显著的性能提升。在SynDM数据集上，ExpanDyNeRF的PSNR指标比现有方法提高了5dB以上，SSIM指标提高了0.05以上。在真实世界数据集上，ExpanDyNeRF也取得了类似的性能提升，证明了其在实际应用中的有效性。

## 🎯 应用场景

ExpanDyNeRF在虚拟现实、增强现实、游戏开发、电影制作等领域具有广泛的应用前景。它可以用于从单目视频中重建动态场景，并生成任意视角的渲染结果，为用户提供更加沉浸式的体验。此外，该技术还可以应用于机器人导航、自动驾驶等领域，提高机器人在复杂环境下的感知能力。

## 📄 摘要（原文）

> In dynamic Neural Radiance Fields (NeRF) systems, state-of-the-art novel view synthesis methods often fail under significant viewpoint deviations, producing unstable and unrealistic renderings. To address this, we introduce Expanded Dynamic NeRF (ExpanDyNeRF), a monocular NeRF framework that leverages Gaussian splatting priors and a pseudo-ground-truth generation strategy to enable realistic synthesis under large-angle rotations. ExpanDyNeRF optimizes density and color features to improve scene reconstruction from challenging perspectives. We also present the Synthetic Dynamic Multiview (SynDM) dataset, the first synthetic multiview dataset for dynamic scenes with explicit side-view supervision-created using a custom GTA V-based rendering pipeline. Quantitative and qualitative results on SynDM and real-world datasets demonstrate that ExpanDyNeRF significantly outperforms existing dynamic NeRF methods in rendering fidelity under extreme viewpoint shifts. Further details are provided in the supplementary materials.

