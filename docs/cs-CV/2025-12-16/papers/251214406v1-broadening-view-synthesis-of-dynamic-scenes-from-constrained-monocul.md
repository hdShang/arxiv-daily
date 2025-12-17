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

**提出ExpanDyNeRF框架，利用高斯先验和伪真值生成策略，解决动态NeRF在大视角偏移下渲染不稳定的问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `动态神经辐射场` `新视角合成` `单目视频` `高斯先验` `伪真值生成` `合成数据集` `渲染保真度` `视角泛化`

## 📋 核心要点

1. 现有动态NeRF方法在大视角偏移下渲染不稳定，导致新视角合成失败和失真。
2. ExpanDyNeRF结合高斯先验和伪真值生成，优化特征以提升重建质量。
3. 在SynDM和真实数据集上，ExpanDyNeRF在极端视角下渲染保真度显著超越现有方法。

## 📝 摘要（中文）

在动态神经辐射场（NeRF）系统中，当前最先进的新视角合成方法在显著视角偏差下常失效，产生不稳定和不真实的渲染结果。为解决此问题，我们引入了扩展动态NeRF（ExpanDyNeRF），这是一个单目NeRF框架，利用高斯溅射先验和伪真值生成策略，以实现大角度旋转下的真实合成。ExpanDyNeRF优化密度和颜色特征，以改进从挑战性视角的场景重建。我们还提出了合成动态多视角（SynDM）数据集，这是首个用于动态场景的合成多视角数据集，具有明确的侧视角监督，通过基于GTA V的自定义渲染管线创建。在SynDM和真实世界数据集上的定量和定性结果表明，ExpanDyNeRF在极端视角偏移下的渲染保真度显著优于现有动态NeRF方法。更多细节见补充材料。

## 🔬 方法详解

ExpanDyNeRF是一个基于单目视频的动态NeRF框架，整体架构包括高斯溅射先验模块和伪真值生成策略。关键技术创新在于利用高斯先验增强场景表示稳定性，并通过伪真值生成提供额外监督，优化密度和颜色特征。与现有方法的主要区别在于其能处理大角度旋转，通过先验和策略改进视角泛化能力，而传统动态NeRF常依赖有限视角数据导致性能下降。

## 📊 实验亮点

在SynDM数据集上，ExpanDyNeRF在极端视角偏移下渲染保真度显著优于基线方法，定量指标如PSNR和SSIM有显著提升，定性结果展示更稳定和真实的合成效果。

## 🎯 应用场景

该研究可应用于虚拟现实、增强现实和机器人导航，通过提升动态场景在新视角下的渲染质量，支持更真实的沉浸式体验和精确环境感知。

## 📄 摘要（原文）

> In dynamic Neural Radiance Fields (NeRF) systems, state-of-the-art novel view synthesis methods often fail under significant viewpoint deviations, producing unstable and unrealistic renderings. To address this, we introduce Expanded Dynamic NeRF (ExpanDyNeRF), a monocular NeRF framework that leverages Gaussian splatting priors and a pseudo-ground-truth generation strategy to enable realistic synthesis under large-angle rotations. ExpanDyNeRF optimizes density and color features to improve scene reconstruction from challenging perspectives. We also present the Synthetic Dynamic Multiview (SynDM) dataset, the first synthetic multiview dataset for dynamic scenes with explicit side-view supervision-created using a custom GTA V-based rendering pipeline. Quantitative and qualitative results on SynDM and real-world datasets demonstrate that ExpanDyNeRF significantly outperforms existing dynamic NeRF methods in rendering fidelity under extreme viewpoint shifts. Further details are provided in the supplementary materials.

