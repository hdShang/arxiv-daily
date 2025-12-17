---
layout: default
title: Dynamic Avatar-Scene Rendering from Human-centric Context
---

# Dynamic Avatar-Scene Rendering from Human-centric Context

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10539" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10539v1</a>
  <a href="https://arxiv.org/pdf/2511.10539.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10539v1" onclick="toggleFavorite(this, '2511.10539v1', 'Dynamic Avatar-Scene Rendering from Human-centric Context')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenqing Wang, Haosen Yang, Josef Kittler, Xiatian Zhu

**分类**: cs.CV

**发布日期**: 2025-11-13

**备注**: 13 pages, 8 figures

---

## 💡 一句话要点

**提出Separate-then-Map策略，解决单目视频中动态人与场景交互的神经渲染问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `神经渲染` `动态场景重建` `人体建模` `单目视频` `人机交互`

## 📋 核心要点

1. 现有方法在单目视频中重建动态人与场景交互时，难以兼顾人体运动特性和场景一致性。
2. Separate-then-Map策略通过信息映射机制连接独立建模的人体和场景，实现高效且连贯的渲染。
3. 实验证明，StM在视觉质量和渲染精度上超越现有技术，尤其在人体-场景交互边界表现突出。

## 📝 摘要（中文）

本文旨在解决从单目视频中重建与真实环境交互的动态人体这一重要且具有挑战性的任务。尽管4D神经渲染取得了显著进展，但现有方法要么整体建模动态场景，要么分别建模场景和背景，并引入参数化的人体先验。然而，这些方法要么忽略了场景中各个组成部分（特别是人体）的不同运动特征，导致重建不完整，要么忽略了单独建模的组件之间的信息交换，导致人体-场景边界处出现空间不一致和视觉伪影。为了解决这个问题，我们提出了Separate-then-Map (StM)策略，该策略引入了一种专门的信息映射机制来桥接单独定义和优化的模型。我们的方法为每个高斯属性采用共享变换函数来统一单独建模的组件，通过避免详尽的成对交互来提高计算效率，同时确保人体及其周围环境之间的空间和视觉连贯性。在单目视频数据集上的大量实验表明，StM在视觉质量和渲染精度方面均显著优于现有的最先进方法，尤其是在具有挑战性的人体-场景交互边界处。

## 🔬 方法详解

**问题定义**：论文旨在解决从单目视频中重建动态人体与真实场景交互的问题。现有方法的痛点在于，要么整体建模忽略了人体运动的特殊性，导致重建不完整；要么分别建模，忽略了人体和场景之间的信息交互，导致边界处出现伪影和不一致性。

**核心思路**：论文的核心思路是“Separate-then-Map”，即先分别建模人体和场景，然后通过信息映射机制将二者桥接起来。这种设计允许对人体和场景进行更精细的优化，同时保证它们之间的空间和视觉一致性。

**技术框架**：整体框架包含两个主要阶段：首先，分别对人体和场景进行建模和优化。然后，引入一个信息映射模块，该模块使用共享的变换函数来统一独立建模的组件。这个变换函数作用于每个高斯属性，从而在人体和场景之间建立对应关系。

**关键创新**：最重要的创新点在于Separate-then-Map策略以及共享变换函数的设计。与现有方法相比，StM能够更好地捕捉人体运动的特殊性，同时保证人体和场景之间的空间一致性。共享变换函数避免了详尽的成对交互，提高了计算效率。

**关键设计**：论文使用高斯表示来建模人体和场景。共享变换函数的具体形式未知，但其目标是统一不同组件的高斯属性。损失函数的设计也至关重要，需要同时考虑重建精度、视觉质量和空间一致性。具体的参数设置和网络结构在论文中应该有详细描述，此处未知。

## 📊 实验亮点

实验结果表明，StM方法在视觉质量和渲染精度方面显著优于现有方法。尤其是在人体与场景交互的边界区域，StM能够生成更清晰、更自然的渲染结果，有效减少了视觉伪影。具体的性能数据和对比基线需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于虚拟现实、增强现实、游戏开发等领域，实现更逼真、自然的虚拟人与真实环境的交互。例如，在VR游戏中，可以利用该技术将玩家的虚拟化身无缝地融入到游戏场景中，提升沉浸感和交互体验。此外，该技术还可用于电影制作、远程协作等场景。

## 📄 摘要（原文）

> Reconstructing dynamic humans interacting with real-world environments from monocular videos is an important and challenging task. Despite considerable progress in 4D neural rendering, existing approaches either model dynamic scenes holistically or model scenes and backgrounds separately aim to introduce parametric human priors. However, these approaches either neglect distinct motion characteristics of various components in scene especially human, leading to incomplete reconstructions, or ignore the information exchange between the separately modeled components, resulting in spatial inconsistencies and visual artifacts at human-scene boundaries. To address this, we propose {\bf Separate-then-Map} (StM) strategy that introduces a dedicated information mapping mechanism to bridge separately defined and optimized models. Our method employs a shared transformation function for each Gaussian attribute to unify separately modeled components, enhancing computational efficiency by avoiding exhaustive pairwise interactions while ensuring spatial and visual coherence between humans and their surroundings. Extensive experiments on monocular video datasets demonstrate that StM significantly outperforms existing state-of-the-art methods in both visual quality and rendering accuracy, particularly at challenging human-scene interaction boundaries.

