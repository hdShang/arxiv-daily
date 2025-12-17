---
layout: default
title: Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos
---

# Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14406" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14406</a>
  <a href="https://arxiv.org/pdf/2512.14406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14406" onclick="toggleFavorite(this, '2512.14406', 'Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Le Jiang, Shaotong Zhu, Yedi Luo, Shayda Moezzi, Sarah Ostadabbas

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**ExpanDyNeRF：扩展动态场景视角合成，解决单目视频大角度渲染失真问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态NeRF` `视角合成` `高斯溅射` `单目视频` `伪真值生成`

## 📋 核心要点

1. 现有动态NeRF方法在视角偏差较大时，渲染效果不稳定且不真实，难以满足实际应用需求。
2. ExpanDyNeRF利用高斯溅射先验和伪真值生成策略，优化密度和颜色特征，从而实现大角度下的高质量渲染。
3. 在SynDM和真实数据集上，ExpanDyNeRF显著优于现有方法，尤其在极端视角偏移下，渲染保真度提升明显。

## 📝 摘要（中文）

针对动态神经辐射场（NeRF）系统中，现有视角合成方法在大角度偏差下易产生不稳定和不真实渲染的问题，本文提出扩展动态NeRF（ExpanDyNeRF），这是一个单目NeRF框架，利用高斯溅射先验和伪真值生成策略，实现大角度旋转下的逼真合成。ExpanDyNeRF优化密度和颜色特征，以改善从具有挑战性视角进行场景重建的效果。此外，本文还提出了合成动态多视角（SynDM）数据集，这是首个具有显式侧视监督的动态场景合成多视角数据集，该数据集使用基于GTA V的自定义渲染管线创建。在SynDM和真实世界数据集上的定量和定性结果表明，ExpanDyNeRF在极端视角偏移下的渲染保真度方面显著优于现有的动态NeRF方法。

## 🔬 方法详解

**问题定义**：现有动态NeRF方法在处理单目视频时，当视角发生较大变化时，渲染结果往往出现失真、模糊等问题，难以生成高质量的新视角图像。这是因为单目视频提供的视角信息有限，导致NeRF在学习场景几何和外观时存在歧义性，尤其是在缺乏侧视监督的情况下。

**核心思路**：ExpanDyNeRF的核心思路是利用高斯溅射（Gaussian Splatting）先验来约束NeRF的学习过程，并结合伪真值生成策略来补充视角信息。高斯溅射能够提供更精确的场景几何表示，从而减少NeRF的歧义性。伪真值生成则通过合成额外的视角图像，为NeRF提供更丰富的训练数据。

**技术框架**：ExpanDyNeRF的整体框架包括以下几个主要模块：1) 高斯溅射先验模块：利用高斯溅射算法对输入视频进行场景重建，得到场景的几何和外观先验信息。2) 伪真值生成模块：基于高斯溅射重建结果，通过视角变换生成额外的视角图像，作为伪真值。3) NeRF优化模块：利用高斯溅射先验和伪真值，对NeRF进行优化，学习场景的密度和颜色特征。

**关键创新**：ExpanDyNeRF的关键创新在于：1) 将高斯溅射先验引入到动态NeRF中，从而提高了场景重建的精度和稳定性。2) 提出了伪真值生成策略，有效地补充了视角信息，解决了单目视频视角受限的问题。3) 构建了SynDM数据集，为动态场景新视角合成提供了基准测试平台。

**关键设计**：ExpanDyNeRF的关键设计包括：1) 使用可微分的高斯溅射算法，以便将高斯溅射先验无缝地集成到NeRF的优化过程中。2) 设计了基于深度信息的视角变换算法，以生成高质量的伪真值图像。3) 采用了多尺度损失函数，以平衡重建精度和渲染质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14406/Figures/real.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14406/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14406/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ExpanDyNeRF在SynDM数据集和真实世界数据集上都取得了显著的性能提升。在SynDM数据集上，ExpanDyNeRF在PSNR、SSIM和LPIPS等指标上均优于现有方法，尤其是在极端视角偏移下，PSNR提升超过3dB。在真实世界数据集上，ExpanDyNeRF也能够生成更清晰、更真实的渲染结果，有效地解决了现有方法存在的失真和模糊问题。

## 🎯 应用场景

ExpanDyNeRF在虚拟现实、增强现实、自动驾驶、电影特效等领域具有广泛的应用前景。例如，可以用于创建沉浸式的虚拟现实体验，实现逼真的增强现实效果，提高自动驾驶系统的环境感知能力，以及生成高质量的电影特效。该研究的实际价值在于提升动态场景新视角合成的质量和效率，为相关应用提供更强大的技术支持。未来，可以进一步探索如何将ExpanDyNeRF应用于更复杂的动态场景，并与其他技术相结合，以实现更高级的视觉效果。

## 📄 摘要（原文）

> In dynamic Neural Radiance Fields (NeRF) systems, state-of-the-art novel view synthesis methods often fail under significant viewpoint deviations, producing unstable and unrealistic renderings. To address this, we introduce Expanded Dynamic NeRF (ExpanDyNeRF), a monocular NeRF framework that leverages Gaussian splatting priors and a pseudo-ground-truth generation strategy to enable realistic synthesis under large-angle rotations. ExpanDyNeRF optimizes density and color features to improve scene reconstruction from challenging perspectives. We also present the Synthetic Dynamic Multiview (SynDM) dataset, the first synthetic multiview dataset for dynamic scenes with explicit side-view supervision-created using a custom GTA V-based rendering pipeline. Quantitative and qualitative results on SynDM and real-world datasets demonstrate that ExpanDyNeRF significantly outperforms existing dynamic NeRF methods in rendering fidelity under extreme viewpoint shifts. Further details are provided in the supplementary materials.

