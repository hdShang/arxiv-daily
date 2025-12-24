---
layout: default
title: "GaussianArt: Unified Modeling of Geometry and Motion for Articulated Objects"
---

# GaussianArt: Unified Modeling of Geometry and Motion for Articulated Objects

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14891" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14891v2</a>
  <a href="https://arxiv.org/pdf/2508.14891.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14891v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14891v2', 'GaussianArt: Unified Modeling of Geometry and Motion for Articulated Objects')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Licheng Shen, Saining Zhang, Honghan Li, Peilin Yang, Zihao Huang, Zongzheng Zhang, Hao Zhao

**分类**: cs.CV

**发布日期**: 2025-08-20 (更新: 2025-11-12)

**备注**: 3DV 2026 Project Page: https://sainingzhang.github.io/project/gaussianart/

---

## 💡 一句话要点

**提出GaussianArt以解决关节物体重建中的几何与运动建模问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `关节物体重建` `几何建模` `运动估计` `3D高斯模型` `数字双胞胎` `机器人仿真` `人机交互`

## 📋 核心要点

1. 现有方法通常将几何与运动分开处理，导致重建流程复杂且难以扩展，尤其是对于复杂的多部分关节物体。
2. 本文提出了一种通过关节3D高斯模型的统一表示方法，能够同时建模几何和运动，从而简化重建流程。
3. 实验表明，该方法在部分几何重建和运动估计上显著优于现有方法，支持多达20个部分的关节物体，提升了鲁棒性和准确性。

## 📝 摘要（中文）

重建关节物体对于构建交互环境的数字双胞胎至关重要。然而，现有方法通常将几何与运动分开处理，先重建物体形状，再进行关节估计，这种分离增加了重建流程的复杂性，限制了可扩展性。本文提出了一种统一的表示方法，通过关节3D高斯模型共同建模几何和运动，显著提高了运动分解的鲁棒性，支持多达20个部分的关节物体。我们还提出了MPArt-90基准，包含90个关节物体，广泛评估了可扩展性和泛化能力。实验结果表明，该方法在多种物体类型的部分几何重建和运动估计上均表现出优越的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决关节物体重建中几何与运动建模的分离问题。现有方法在处理复杂多部分关节物体时，往往因初始化脆弱而表现不佳，限制了其可扩展性。

**核心思路**：我们提出了一种统一的表示方法，利用关节3D高斯模型共同建模几何和运动。这种设计旨在提高运动分解的鲁棒性，并支持更复杂的关节结构。

**技术框架**：整体架构包括数据输入、关节3D高斯建模、运动分解和几何重建几个主要模块。通过这些模块的协同工作，实现了对关节物体的高效重建。

**关键创新**：最重要的技术创新在于引入了关节3D高斯模型的统一表示，克服了传统方法在多部分关节物体重建中的局限性，显著提升了鲁棒性和准确性。

**关键设计**：在关键设计方面，我们采用了特定的损失函数以优化几何和运动的联合建模，同时在网络结构上进行了调整，以适应多部分关节物体的复杂性。

## 📊 实验亮点

实验结果显示，GaussianArt在部分几何重建和运动估计上均显著优于现有方法，支持多达20个部分的关节物体，准确性提升幅度超过了以往方法在2-3部分物体上的表现，展示了其在复杂场景下的优越性。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在机器人仿真和人机交互场景建模中。通过提供更准确的关节物体重建，能够提升虚拟环境的交互性和真实感，推动智能机器人与人类的协作。未来，该方法可能在游戏开发、虚拟现实和增强现实等领域产生深远影响。

## 📄 摘要（原文）

> Reconstructing articulated objects is essential for building digital twins of interactive environments. However, prior methods typically decouple geometry and motion by first reconstructing object shape in distinct states and then estimating articulation through post-hoc alignment. This separation complicates the reconstruction pipeline and restricts scalability, especially for objects with complex, multi-part articulation. We introduce a unified representation that jointly models geometry and motion using articulated 3D Gaussians. This formulation improves robustness in motion decomposition and supports articulated objects with up to 20 parts, significantly outperforming prior approaches that often struggle beyond 2--3 parts due to brittle initialization. To systematically assess scalability and generalization, we propose MPArt-90, a new benchmark consisting of 90 articulated objects across 20 categories, each with diverse part counts and motion configurations. Extensive experiments show that our method consistently achieves superior accuracy in part-level geometry reconstruction and motion estimation across a broad range of object types. We further demonstrate applicability to downstream tasks such as robotic simulation and human-scene interaction modeling, highlighting the potential of unified articulated representations in scalable physical modeling.

