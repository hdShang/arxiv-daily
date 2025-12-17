---
layout: default
title: Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos
---

# Broadening View Synthesis of Dynamic Scenes from Constrained Monocular Videos

**arXiv**: [2512.14406v1](https://arxiv.org/abs/2512.14406) | [PDF](https://arxiv.org/pdf/2512.14406.pdf)

**作者**: Le Jiang, Shaotong Zhu, Yedi Luo, Shayda Moezzi, Sarah Ostadabbas

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出ExpanDyNeRF框架，利用高斯溅射先验和伪真值生成策略，解决动态NeRF在大视角旋转下渲染不稳定的问题。**

**关键词**: `动态神经辐射场` `新视角合成` `单目视频` `高斯溅射先验` `伪真值生成` `合成数据集` `大视角旋转` `渲染保真度`

## 📋 核心要点

1. 现有动态NeRF方法在大视角旋转下渲染不稳定，导致新视角合成失败，产生不真实结果。
2. ExpanDyNeRF结合高斯溅射先验和伪真值生成，优化密度和颜色特征，提升大角度视角下的重建质量。
3. 实验显示，ExpanDyNeRF在SynDM和真实数据集上，渲染保真度显著优于现有方法，尤其在极端视角偏移下。

## 📝 摘要（中文）

在动态神经辐射场（NeRF）系统中，当前最先进的新视角合成方法在显著视角偏差下常失败，产生不稳定和不真实的渲染。为解决此问题，我们引入了扩展动态NeRF（ExpanDyNeRF），这是一个单目NeRF框架，利用高斯溅射先验和伪真值生成策略，以实现大角度旋转下的真实合成。ExpanDyNeRF优化密度和颜色特征，以改进从挑战性视角的场景重建。我们还提出了合成动态多视角（SynDM）数据集，这是首个用于动态场景的合成多视角数据集，具有明确的侧视角监督，通过基于GTA V的自定义渲染管线创建。在SynDM和真实世界数据集上的定量和定性结果表明，ExpanDyNeRF在极端视角偏移下的渲染保真度显著优于现有动态NeRF方法。更多细节见补充材料。

## 🔬 方法详解

ExpanDyNeRF是一个单目NeRF框架，整体基于动态神经辐射场，通过高斯溅射先验提供几何约束，并采用伪真值生成策略增强训练数据。关键技术创新包括：引入高斯溅射先验以稳定大视角下的密度估计，以及设计伪真值生成机制来模拟多视角监督。与现有方法的主要区别在于，它专门针对单目视频输入，通过先验和伪真值策略，有效缓解了视角偏差导致的渲染不稳定性，而无需依赖多摄像头或复杂运动模型。

## 📊 实验亮点

在SynDM数据集上，ExpanDyNeRF在极端视角偏移下的渲染保真度显著提升，定量指标优于现有动态NeRF方法，定性结果展示更稳定和真实的合成效果。

## 🎯 应用场景

该研究可应用于虚拟现实、增强现实和机器人导航等领域，通过单目视频实现动态场景的高质量新视角合成，提升沉浸式体验和场景理解能力。

## 📄 摘要（原文）

> In dynamic Neural Radiance Fields (NeRF) systems, state-of-the-art novel view synthesis methods often fail under significant viewpoint deviations, producing unstable and unrealistic renderings. To address this, we introduce Expanded Dynamic NeRF (ExpanDyNeRF), a monocular NeRF framework that leverages Gaussian splatting priors and a pseudo-ground-truth generation strategy to enable realistic synthesis under large-angle rotations. ExpanDyNeRF optimizes density and color features to improve scene reconstruction from challenging perspectives. We also present the Synthetic Dynamic Multiview (SynDM) dataset, the first synthetic multiview dataset for dynamic scenes with explicit side-view supervision-created using a custom GTA V-based rendering pipeline. Quantitative and qualitative results on SynDM and real-world datasets demonstrate that ExpanDyNeRF significantly outperforms existing dynamic NeRF methods in rendering fidelity under extreme viewpoint shifts. Further details are provided in the supplementary materials.

