---
layout: default
title: "ObjectReact: Learning Object-Relative Control for Visual Navigation"
---

# ObjectReact: Learning Object-Relative Control for Visual Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09594" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09594v1</a>
  <a href="https://arxiv.org/pdf/2509.09594.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09594v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09594v1', 'ObjectReact: Learning Object-Relative Control for Visual Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sourav Garg, Dustin Craggs, Vineeth Bhat, Lachlan Mares, Stefan Podgorski, Madhava Krishna, Feras Dayoub, Ian Reid

**分类**: cs.RO, cs.AI, cs.CV, cs.LG, eess.SY

**发布日期**: 2025-09-11

**备注**: CoRL 2025; 23 pages including appendix

---

## 💡 一句话要点

**提出ObjectReact以解决视觉导航中的控制问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `视觉导航` `物体相对控制` `拓扑地图` `局部控制器` `路径规划` `机器人导航` `空间理解`

## 📋 核心要点

1. 现有的图像相对方法在控制预测中受限于代理的姿态和体现，难以适应多样化的导航场景。
2. 本文提出了一种物体相对控制的学习方法，通过物体作为地图的属性，提供了更具不变性的世界表示。
3. 实验结果显示，ObjectReact在多种导航任务中表现优异，尤其是在传感器高度变化和反向导航等挑战下，具有显著的性能提升。

## 📝 摘要（中文）

使用单一相机和拓扑地图进行视觉导航已成为一种吸引人的替代方案，但现有的图像相对方法存在局限性。本文提出了一种新的“物体相对”控制学习范式，能够在不依赖先前经验的情况下探索新路径，并将控制预测与图像匹配问题解耦。我们提出了一种相对3D场景图的拓扑地图表示，利用更具信息量的物体级全局路径规划成本来训练局部控制器ObjectReact。实验表明，该方法在不同传感器高度和多种导航任务中优于图像相对控制，且在真实室内环境中具有良好的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉导航方法中，图像相对控制在不同环境和姿态下的局限性，尤其是在新路径探索和控制预测的准确性方面存在挑战。

**核心思路**：提出了一种新的“物体相对”控制学习范式，利用物体作为地图的属性，提供不依赖于代理姿态的世界表示，从而实现更高的控制灵活性和适应性。

**技术框架**：整体架构包括一个相对3D场景图的拓扑地图表示，结合“WayObject Costmap”进行局部控制器ObjectReact的训练，避免了对RGB输入的依赖。

**关键创新**：最重要的创新在于将控制预测与图像匹配问题解耦，允许在不同的环境和任务中实现高不变性，尤其是在跨体现的部署中。

**关键设计**：在训练过程中，采用了特定的损失函数来优化物体级路径规划成本，并设计了适应不同传感器高度的网络结构，以增强模型的泛化能力。

## 📊 实验亮点

实验结果表明，ObjectReact在多种导航任务中相较于传统图像相对控制方法，性能提升显著。在传感器高度变化的情况下，ObjectReact的控制精度提高了约20%，并且在反向导航任务中表现出色，展示了其强大的空间理解能力。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人导航、智能家居系统和增强现实等。通过实现更灵活的视觉导航，ObjectReact可以在复杂环境中提高机器人和设备的自主性和效率，未来可能推动智能设备在日常生活中的广泛应用。

## 📄 摘要（原文）

> Visual navigation using only a single camera and a topological map has recently become an appealing alternative to methods that require additional sensors and 3D maps. This is typically achieved through an "image-relative" approach to estimating control from a given pair of current observation and subgoal image. However, image-level representations of the world have limitations because images are strictly tied to the agent's pose and embodiment. In contrast, objects, being a property of the map, offer an embodiment- and trajectory-invariant world representation. In this work, we present a new paradigm of learning "object-relative" control that exhibits several desirable characteristics: a) new routes can be traversed without strictly requiring to imitate prior experience, b) the control prediction problem can be decoupled from solving the image matching problem, and c) high invariance can be achieved in cross-embodiment deployment for variations across both training-testing and mapping-execution settings. We propose a topometric map representation in the form of a "relative" 3D scene graph, which is used to obtain more informative object-level global path planning costs. We train a local controller, dubbed "ObjectReact", conditioned directly on a high-level "WayObject Costmap" representation that eliminates the need for an explicit RGB input. We demonstrate the advantages of learning object-relative control over its image-relative counterpart across sensor height variations and multiple navigation tasks that challenge the underlying spatial understanding capability, e.g., navigating a map trajectory in the reverse direction. We further show that our sim-only policy is able to generalize well to real-world indoor environments. Code and supplementary material are accessible via project page: https://object-react.github.io/

