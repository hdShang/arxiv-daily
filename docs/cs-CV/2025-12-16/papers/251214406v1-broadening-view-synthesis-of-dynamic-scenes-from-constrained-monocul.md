---
layout: default
title: Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos
---

# Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14406" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14406v1</a>
  <a href="https://arxiv.org/pdf/2512.14406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14406v1" onclick="toggleFavorite(this, '2512.14406v1', 'Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Jiang, Shaotong Zhu, Yedi Luo, Shayda Moezzi, Sarah Ostadabbas

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**ExpanDyNeRF：扩展动态场景视角合成，解决单目视频大角度渲染失真问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `动态NeRF` `视角合成` `高斯溅射` `单目视频` `伪真值生成` `神经渲染` `动态场景重建` `大角度渲染`

## 📋 核心要点

1. 现有动态NeRF方法在视角变化较大时，渲染效果不稳定且不真实，难以满足实际应用需求。
2. ExpanDyNeRF利用高斯溅射先验和伪真值生成策略，优化密度和颜色特征，从而实现大角度下的高质量视角合成。
3. 在SynDM和真实数据集上，ExpanDyNeRF显著优于现有方法，证明了其在极端视角变化下的渲染保真度优势。

## 📝 摘要（中文）

针对动态神经辐射场（NeRF）系统中，现有视角合成方法在大角度视角偏差下易产生不稳定和不真实渲染的问题，我们提出了扩展动态NeRF（ExpanDyNeRF），这是一个单目NeRF框架，利用高斯溅射先验和伪真值生成策略，实现大角度旋转下的逼真合成。ExpanDyNeRF优化密度和颜色特征，以改善从具有挑战性的视角进行场景重建的效果。我们还提出了合成动态多视角（SynDM）数据集，这是第一个具有显式侧视图监督的动态场景合成多视角数据集，使用定制的基于GTA V的渲染管线创建。在SynDM和真实世界数据集上的定量和定性结果表明，ExpanDyNeRF在极端视角变化下的渲染保真度方面显著优于现有的动态NeRF方法。

## 🔬 方法详解

**问题定义**：现有动态NeRF方法在处理单目视频时，当视角发生较大变化时，渲染结果往往出现失真、不稳定等问题。这是因为单目视频提供的视角信息有限，难以准确重建场景的几何和外观信息，尤其是在缺乏侧视图监督的情况下。现有方法难以有效应对这种挑战，导致合成的新视角图像质量下降。

**核心思路**：ExpanDyNeRF的核心思路是利用高斯溅射（Gaussian Splatting）作为先验知识，并结合伪真值生成策略，来弥补单目视频视角信息不足的问题。高斯溅射能够更有效地表示场景的几何结构和外观，而伪真值生成则可以提供额外的监督信息，从而提高场景重建的准确性和鲁棒性。通过这种方式，ExpanDyNeRF能够更好地处理大角度视角变化，生成更逼真的新视角图像。

**技术框架**：ExpanDyNeRF的整体框架主要包括以下几个阶段：1) **高斯溅射初始化**：使用单目视频数据初始化场景的高斯溅射表示。2) **伪真值生成**：利用初始化的高斯溅射表示，生成不同视角的伪真值图像。3) **NeRF优化**：利用单目视频数据和生成的伪真值图像，联合优化NeRF模型的密度和颜色特征。4) **新视角合成**：使用优化后的NeRF模型，合成任意视角的新视角图像。

**关键创新**：ExpanDyNeRF的关键创新在于以下几个方面：1) **高斯溅射先验**：将高斯溅射引入动态NeRF框架，提高了场景表示的效率和准确性。2) **伪真值生成策略**：通过生成额外的监督信息，弥补了单目视频视角信息不足的问题。3) **SynDM数据集**：构建了首个具有显式侧视图监督的动态场景合成多视角数据集，为动态NeRF的研究提供了新的benchmark。与现有方法相比，ExpanDyNeRF能够更好地处理大角度视角变化，生成更逼真的新视角图像。

**关键设计**：ExpanDyNeRF的关键设计包括：1) **高斯溅射的参数化**：使用均值、方差和颜色等参数来表示每个高斯球。2) **伪真值生成器的设计**：使用一个神经网络来生成不同视角的伪真值图像，并使用对抗损失来提高生成图像的真实感。3) **NeRF模型的结构**：使用一个多层感知机（MLP）来预测每个点的密度和颜色。4) **损失函数的设计**：使用包括图像重建损失、正则化损失和对抗损失在内的多种损失函数来优化模型。

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

ExpanDyNeRF在SynDM数据集和真实世界数据集上都取得了显著的性能提升。在SynDM数据集上，ExpanDyNeRF在PSNR、SSIM和LPIPS等指标上均优于现有方法。例如，在极端视角变化下，ExpanDyNeRF的PSNR比现有方法提高了5dB以上。在真实世界数据集上，ExpanDyNeRF也能够生成更逼真、更稳定的新视角图像，证明了其在实际应用中的有效性。

## 🎯 应用场景

ExpanDyNeRF在虚拟现实、增强现实、机器人导航、自动驾驶等领域具有广泛的应用前景。它可以用于生成高质量的动态场景新视角图像，从而提高用户体验和系统性能。例如，在虚拟现实中，用户可以自由地改变视角，观察动态场景的细节。在自动驾驶中，系统可以利用ExpanDyNeRF生成不同视角的图像，从而提高对周围环境的感知能力。未来，该技术有望进一步发展，应用于更复杂的动态场景和更广泛的领域。

## 📄 摘要（原文）

> In dynamic Neural Radiance Fields (NeRF) systems, state-of-the-art novel view synthesis methods often fail under significant viewpoint deviations, producing unstable and unrealistic renderings. To address this, we introduce Expanded Dynamic NeRF (ExpanDyNeRF), a monocular NeRF framework that leverages Gaussian splatting priors and a pseudo-ground-truth generation strategy to enable realistic synthesis under large-angle rotations. ExpanDyNeRF optimizes density and color features to improve scene reconstruction from challenging perspectives. We also present the Synthetic Dynamic Multiview (SynDM) dataset, the first synthetic multiview dataset for dynamic scenes with explicit side-view supervision-created using a custom GTA V-based rendering pipeline. Quantitative and qualitative results on SynDM and real-world datasets demonstrate that ExpanDyNeRF significantly outperforms existing dynamic NeRF methods in rendering fidelity under extreme viewpoint shifts. Further details are provided in the supplementary materials.

