---
layout: default
title: LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering
---

# LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22669" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22669v1</a>
  <a href="https://arxiv.org/pdf/2510.22669.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22669v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22669v1', 'LVD-GS: Gaussian Splatting SLAM for Dynamic Scenes via Hierarchical Explicit-Implicit Representation Collaboration Rendering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenkai Zhu, Xu Li, Qimin Xu, Benwu Wang, Kun Wei, Yiming Peng, Zihang Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-26

---

## 💡 一句话要点

**LVD-GS：面向动态场景，基于分层显隐式表达协同渲染的Gaussian Splatting SLAM**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `SLAM` `3D Gaussian Splatting` `动态场景` `LiDAR-Visual融合` `分层表示` `动态物体分割` `位姿优化`

## 📋 核心要点

1. 现有3D Gaussian Splatting SLAM方法在大型动态户外场景中表现不佳，存在累积位姿误差和尺度模糊问题。
2. LVD-GS通过分层协同表示模块，利用LiDAR和视觉信息的互补性，增强了地图构建的鲁棒性，并减轻了尺度漂移。
3. LVD-GS融合开放世界分割和隐式残差约束，生成精细的动态掩码，有效消除了动态对象对SLAM系统的影响，并在多个数据集上取得了SOTA性能。

## 📝 摘要（中文）

本文提出了一种新颖的LiDAR-Visual 3D Gaussian Splatting SLAM系统，名为LVD-GS，旨在解决现有方法在大型动态户外场景中性能受限以及累积位姿误差和尺度模糊的问题。受人类链式思考信息寻求过程的启发，我们引入了一个分层协同表示模块，该模块促进了映射优化的相互增强，有效地减轻了尺度漂移并增强了重建的鲁棒性。此外，为了有效消除动态对象的影响，我们提出了一个联合动态建模模块，该模块通过融合开放世界分割与隐式残差约束来生成细粒度的动态掩码，并由DINO-Depth特征的不确定性估计引导。在KITTI、nuScenes和自采集数据集上的大量评估表明，与现有方法相比，我们的方法实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有基于3D Gaussian Splatting的SLAM方法在处理大型动态户外场景时面临挑战。由于场景的复杂性和动态性，这些方法容易产生累积位姿误差和尺度模糊，导致地图构建的精度和鲁棒性下降。现有的方法通常依赖单一的表达方式，难以充分利用不同传感器（如LiDAR和相机）的信息，也难以有效地处理动态物体的影响。

**核心思路**：LVD-GS的核心思路是引入一种分层显隐式表达协同渲染框架，结合LiDAR和视觉信息，实现更鲁棒和精确的SLAM。通过模仿人类链式思考的信息寻求过程，利用不同传感器数据的互补性，相互增强，从而减轻尺度漂移，提高重建质量。同时，通过联合动态建模模块，有效消除动态物体的影响。

**技术框架**：LVD-GS系统主要包含以下几个模块：1) **分层协同表示模块**：该模块利用LiDAR点云和视觉图像，构建分层的地图表示。显式表示采用3D Gaussian Splatting，隐式表示则用于约束和优化。2) **位姿优化模块**：该模块利用分层表示进行位姿优化，减轻尺度漂移。3) **联合动态建模模块**：该模块融合开放世界分割和隐式残差约束，生成精细的动态掩码，用于滤除动态物体的影响。4) **渲染模块**：该模块基于优化后的Gaussian Splatting参数进行场景渲染。

**关键创新**：LVD-GS的关键创新在于：1) **分层协同表示**：结合显式的3D Gaussian Splatting和隐式的约束，充分利用LiDAR和视觉信息的互补性。2) **联合动态建模**：融合开放世界分割和隐式残差约束，生成精细的动态掩码，有效消除动态物体的影响。3) **模仿人类链式思考的信息寻求过程**：通过分层协同表示，实现信息的相互增强，提高SLAM系统的鲁棒性。

**关键设计**：1) **分层表示的融合方式**：具体如何将LiDAR和视觉信息融合到分层表示中，以及如何设计损失函数来优化分层表示的参数（例如，Gaussian Splatting的均值、方差、颜色等）。2) **动态掩码的生成方式**：如何设计开放世界分割和隐式残差约束的融合策略，以及如何利用DINO-Depth特征的不确定性估计来指导动态掩码的生成。3) **位姿优化的策略**：如何利用分层表示进行位姿优化，以及如何设计损失函数来减轻尺度漂移。

## 📊 实验亮点

LVD-GS在KITTI、nuScenes和自采集数据集上进行了广泛的评估，实验结果表明，LVD-GS在地图构建的精度和鲁棒性方面均优于现有的SLAM方法。具体而言，LVD-GS能够有效地减轻尺度漂移，并生成更精细的动态掩码，从而提高SLAM系统的整体性能。论文中给出了具体的性能数据和对比基线，证明了LVD-GS的优越性。

## 🎯 应用场景

LVD-GS在自动驾驶、机器人导航、增强现实等领域具有广泛的应用前景。该系统能够构建高精度、鲁棒的三维地图，并有效处理动态场景，为自动驾驶车辆提供可靠的环境感知信息。此外，该系统还可以应用于机器人导航，帮助机器人在复杂环境中进行自主导航和避障。在增强现实领域，LVD-GS可以用于构建逼真的虚拟场景，并实现虚拟物体与真实环境的无缝融合。

## 📄 摘要（原文）

> 3D Gaussian Splatting SLAM has emerged as a widely used technique for high-fidelity mapping in spatial intelligence. However, existing methods often rely on a single representation scheme, which limits their performance in large-scale dynamic outdoor scenes and leads to cumulative pose errors and scale ambiguity. To address these challenges, we propose \textbf{LVD-GS}, a novel LiDAR-Visual 3D Gaussian Splatting SLAM system. Motivated by the human chain-of-thought process for information seeking, we introduce a hierarchical collaborative representation module that facilitates mutual reinforcement for mapping optimization, effectively mitigating scale drift and enhancing reconstruction robustness. Furthermore, to effectively eliminate the influence of dynamic objects, we propose a joint dynamic modeling module that generates fine-grained dynamic masks by fusing open-world segmentation with implicit residual constraints, guided by uncertainty estimates from DINO-Depth features. Extensive evaluations on KITTI, nuScenes, and self-collected datasets demonstrate that our approach achieves state-of-the-art performance compared to existing methods.

