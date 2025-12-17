---
layout: default
title: Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting
---

# Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.05113" class="toolbar-btn" target="_blank">📄 arXiv: 2512.05113v2</a>
  <a href="https://arxiv.org/pdf/2512.05113.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.05113v2" onclick="toggleFavorite(this, '2512.05113v2', 'Splannequin: Freezing Monocular Mannequin-Challenge Footage with Dual-Detection Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao-Jen Chien, Yi-Chuan Huang, Chung-Ho Wu, Wei-Lun Chao, Yu-Lun Liu

**分类**: cs.CV

**发布日期**: 2025-12-04 (更新: 2025-12-08)

**备注**: WACV 2026. Project page: https://chien90190.github.io/splannequin/

**🔗 代码/项目**: [PROJECT_PAGE](https://chien90190.github.io/splannequin/)

---

## 💡 一句话要点

**Splannequin：利用双重检测 Splatting 冻结单目人体雕塑挑战视频**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `动态高斯Splatting` `人体雕塑挑战` `单目视频重建` `时间锚定` `冻结时间渲染`

## 📋 核心要点

1. 现有方法难以在单目人体雕塑挑战视频中，既冻结场景又保留细微动态，导致用户无法灵活选择时间点。
2. Splannequin通过动态高斯Splatting建模场景，并根据高斯状态（隐藏或缺陷）进行时间锚定，从而保留动态并减少伪影。
3. 该方法易于集成到现有pipeline，无需修改架构，且推理无额外开销，显著提升视觉质量，用户偏好度高达96%。

## 📝 摘要（中文）

本研究针对单目人体雕塑挑战(Mannequin-Challenge, MC)视频，提出了一种合成高保真冻结3D场景的新方法，这与标准的动态场景重建问题有所不同。我们的目标不是建模运动，而是创建冻结场景，同时策略性地保留细微的动态，以实现用户可控的即时选择。为此，我们引入了动态高斯Splatting的一种新应用：动态地建模场景，保留附近的 temporal variation，并通过固定模型的时间参数来渲染静态场景。然而，在这种使用方式下，单目捕获和稀疏的时间监督会导致伪影，例如在高斯变得未观察到或在弱监督时间戳处被遮挡时出现重影和模糊。我们提出了Splannequin，一种与架构无关的正则化方法，用于检测高斯基元的两种状态：隐藏和缺陷，并应用时间锚定。在主要为前向相机运动的情况下，隐藏状态被锚定到它们最近的良好观察到的过去状态，而缺陷状态被锚定到具有更强监督的未来状态。我们的方法通过简单的损失项集成到现有的动态高斯管道中，不需要架构更改，并且增加了零推理开销。这显著提高了视觉质量，实现了高保真、用户可选择的冻结时间渲染，并通过96%的用户偏好验证。

## 🔬 方法详解

**问题定义**：论文旨在解决从单目人体雕塑挑战视频中重建高质量冻结3D场景的问题。现有方法在处理此类视频时，由于单目视觉的固有局限性和时间监督的稀疏性，容易产生重影、模糊等伪影，难以同时保证场景的静态和动态细节。

**核心思路**：论文的核心思路是利用动态高斯Splatting来建模场景，并根据高斯基元的状态（隐藏或缺陷）进行时间锚定。通过动态建模，可以保留场景中的细微动态变化；通过时间锚定，可以减少由于遮挡或弱监督导致的高斯基元质量下降，从而减少伪影。

**技术框架**：Splannequin方法可以集成到现有的动态高斯Splatting pipeline中，无需修改pipeline的架构。其主要流程包括：1) 使用动态高斯Splatting建模场景；2) 检测高斯基元的状态（隐藏或缺陷）；3) 根据高斯基元的状态进行时间锚定；4) 渲染冻结的3D场景。

**关键创新**：该方法最重要的创新点在于提出了双重检测 Splatting 的概念，即根据高斯基元的状态（隐藏或缺陷）进行不同的时间锚定策略。对于隐藏状态的高斯基元，锚定到其最近的良好观察到的过去状态；对于缺陷状态的高斯基元，锚定到具有更强监督的未来状态。这种策略能够有效地减少伪影，并保留场景中的动态细节。

**关键设计**：Splannequin方法通过简单的损失项集成到现有的动态高斯Splatting pipeline中。具体来说，对于隐藏状态的高斯基元，添加一个损失项，使其位置和颜色尽可能接近其最近的良好观察到的过去状态；对于缺陷状态的高斯基元，添加一个损失项，使其位置和颜色尽可能接近具有更强监督的未来状态。这些损失项的设计旨在约束高斯基元的运动，从而减少伪影。

## 📊 实验亮点

Splannequin方法在人体雕塑挑战视频数据集上取得了显著的视觉质量提升，用户偏好度高达96%。该方法无需修改现有动态高斯Splatting pipeline的架构，且推理无额外开销，易于部署和应用。实验结果表明，Splannequin能够有效地减少重影、模糊等伪影，并保留场景中的动态细节。

## 🎯 应用场景

Splannequin技术可应用于虚拟现实、增强现实、游戏等领域，例如创建可交互的冻结时间场景，允许用户自由选择视角和时间点，从而获得更沉浸式的体验。该技术还可用于运动分析、动作捕捉等领域，例如分析运动员的动作细节，或捕捉演员的表演瞬间。

## 📄 摘要（原文）

> Synthesizing high-fidelity frozen 3D scenes from monocular Mannequin-Challenge (MC) videos is a unique problem distinct from standard dynamic scene reconstruction. Instead of focusing on modeling motion, our goal is to create a frozen scene while strategically preserving subtle dynamics to enable user-controlled instant selection. To achieve this, we introduce a novel application of dynamic Gaussian splatting: the scene is modeled dynamically, which retains nearby temporal variation, and a static scene is rendered by fixing the model's time parameter. However, under this usage, monocular capture with sparse temporal supervision introduces artifacts like ghosting and blur for Gaussians that become unobserved or occluded at weakly supervised timestamps. We propose Splannequin, an architecture-agnostic regularization that detects two states of Gaussian primitives, hidden and defective, and applies temporal anchoring. Under predominantly forward camera motion, hidden states are anchored to their recent well-observed past states, while defective states are anchored to future states with stronger supervision. Our method integrates into existing dynamic Gaussian pipelines via simple loss terms, requires no architectural changes, and adds zero inference overhead. This results in markedly improved visual quality, enabling high-fidelity, user-selectable frozen-time renderings, validated by a 96% user preference. Project page: https://chien90190.github.io/splannequin/

