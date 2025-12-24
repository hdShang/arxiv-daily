---
layout: default
title: "Part$^{2}$GS: Part-aware Modeling of Articulated Objects using 3D Gaussian Splatting"
---

# Part$^{2}$GS: Part-aware Modeling of Articulated Objects using 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17212" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17212v1</a>
  <a href="https://arxiv.org/pdf/2506.17212.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17212v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17212v1', 'Part$^{2}$GS: Part-aware Modeling of Articulated Objects using 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianjiao Yu, Vedant Shah, Muntasir Wahed, Ying Shen, Kiet A. Nguyen, Ismini Lourentzou

**分类**: cs.CV, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出Part²GS以解决关节物体建模问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `关节物体建模` `3D重建` `高保真几何` `物理一致性` `机器学习` `计算机视觉` `数字双胞胎`

## 📋 核心要点

1. 现有的3D重建方法在建模关节物体的结构和运动时面临挑战，尤其是在保持高保真几何和物理一致性方面。
2. Part²GS框架通过部件感知的3D高斯表示，结合物理约束，实现了高效的关节物体建模，确保了运动的一致性和稳定性。
3. 在合成和真实数据集上的实验结果显示，Part²GS在Chamfer距离上相较于基线方法提升了多达10倍，表现出显著的优势。

## 📝 摘要（中文）

关节物体在现实世界中普遍存在，但其结构和运动的建模仍然是3D重建方法面临的挑战。本文提出了Part²GS，一个新颖的框架，用于高保真几何和物理一致性关节的多部件物体数字双胞胎建模。Part²GS利用了一种部件感知的3D高斯表示，编码具有可学习属性的关节组件，从而实现结构化、解耦的变换，保持高保真几何。为确保物理一致的运动，提出了一种运动感知的规范表示，受物理约束指导，包括接触强制、速度一致性和矢量场对齐。此外，引入了排斥点场以防止部件碰撞并保持稳定的关节路径，显著提高了运动一致性。大量在合成和真实世界数据集上的评估表明，Part²GS在可移动部件的Chamfer距离上，性能比现有最先进的方法提高了多达10倍。

## 🔬 方法详解

**问题定义**：本文旨在解决关节物体建模中的结构和运动一致性问题。现有方法在处理多部件物体时，常常无法保持高保真几何和物理一致性，导致运动不连贯。

**核心思路**：Part²GS框架采用部件感知的3D高斯表示，能够对关节组件进行编码并赋予可学习属性，从而实现结构化和解耦的变换，保持几何的高保真性。

**技术框架**：该框架包括多个模块，首先通过部件感知的3D高斯表示对物体进行建模，然后引入运动感知的规范表示，最后通过排斥点场来防止部件之间的碰撞，确保运动路径的稳定性。

**关键创新**：Part²GS的主要创新在于其部件感知的3D高斯表示和运动感知的规范表示，这使得模型能够在物理约束下实现高效的关节物体建模，与现有方法相比，显著提高了运动一致性。

**关键设计**：在设计中，采用了接触强制、速度一致性和矢量场对齐等物理约束，确保了运动的物理一致性。此外，排斥点场的引入有效防止了部件碰撞，增强了模型的稳定性。

## 📊 实验亮点

在合成和真实数据集上的评估结果显示，Part²GS在可移动部件的Chamfer距离上，相较于现有最先进的方法提升了多达10倍，展现出显著的性能优势，证明了其在关节物体建模中的有效性和可靠性。

## 🎯 应用场景

Part²GS框架在机器人、动画制作、虚拟现实等领域具有广泛的应用潜力。通过高保真的关节物体建模，可以实现更真实的物体交互和运动模拟，提升用户体验。未来，该技术可能推动智能机器人在复杂环境中的自主操作能力。

## 📄 摘要（原文）

> Articulated objects are common in the real world, yet modeling their structure and motion remains a challenging task for 3D reconstruction methods. In this work, we introduce Part$^{2}$GS, a novel framework for modeling articulated digital twins of multi-part objects with high-fidelity geometry and physically consistent articulation. Part$^{2}$GS leverages a part-aware 3D Gaussian representation that encodes articulated components with learnable attributes, enabling structured, disentangled transformations that preserve high-fidelity geometry. To ensure physically consistent motion, we propose a motion-aware canonical representation guided by physics-based constraints, including contact enforcement, velocity consistency, and vector-field alignment. Furthermore, we introduce a field of repel points to prevent part collisions and maintain stable articulation paths, significantly improving motion coherence over baselines. Extensive evaluations on both synthetic and real-world datasets show that Part$^{2}$GS consistently outperforms state-of-the-art methods by up to 10$\times$ in Chamfer Distance for movable parts.

