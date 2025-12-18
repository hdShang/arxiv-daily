---
layout: default
title: HERO: Hierarchical Traversable 3D Scene Graphs for Embodied Navigation Among Movable Obstacles
---

# HERO: Hierarchical Traversable 3D Scene Graphs for Embodied Navigation Among Movable Obstacles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15047" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15047v1</a>
  <a href="https://arxiv.org/pdf/2512.15047.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15047v1" onclick="toggleFavorite(this, '2512.15047v1', 'HERO: Hierarchical Traversable 3D Scene Graphs for Embodied Navigation Among Movable Obstacles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunheng Wang, Yixiao Feng, Yuetong Fang, Shuning Zhang, Tan Jing, Jian Li, Xiangrui Jiang, Renjing Xu

**分类**: cs.RO, cs.AI, cs.CL, cs.CV

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出HERO框架以解决动态障碍物导航问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景图` `动态障碍物` `导航规划` `机器人导航` `智能体交互` `层次化建模` `可通行性`

## 📋 核心要点

1. 现有方法依赖静态世界假设，无法有效处理可移动障碍物，导致导航效率低下和可达性受限。
2. HERO框架通过将可操作障碍物视为通道，重新定义可通行性，捕捉物理交互性和场景关系层次。
3. 实验结果显示，HERO在部分遮挡环境中路径长度减少35.1%，在完全遮挡环境中成功率提高79.4%。

## 📝 摘要（中文）

3D场景图（3DSGs）是一种强大的物理世界表示方式，能够明确建模实体之间复杂的空间、语义和功能关系，从而使智能体能够与环境智能交互并执行多样化行为。然而，现有方法基于静态世界假设，未能有效处理可移动障碍物，导致在真实场景中的可达性和效率低下。为此，本文提出了HERO框架，通过将可操作障碍物建模为通道，重新定义可通行性，显著提高了在部分和完全遮挡环境中的导航效率和可达性。实验结果表明，HERO在部分遮挡环境中将路径长度减少了35.1%，在完全遮挡环境中提高了79.4%的成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在动态环境中对可移动障碍物处理不足的问题。现有方法仅基于静态空间布局定义可通行区域，导致在真实场景中可达性和效率低下。

**核心思路**：HERO框架的核心思想是将可操作障碍物视为通道，重新定义可通行性，以便更好地捕捉障碍物的物理交互性和功能语义，从而提升导航能力。

**技术框架**：HERO的整体架构包括三个主要模块：场景图构建模块、障碍物交互建模模块和导航规划模块。首先构建3D场景图，然后对可移动障碍物进行交互建模，最后进行基于新定义的可通行性进行导航规划。

**关键创新**：HERO的主要创新在于将可操作障碍物建模为通道，突破了传统方法对静态障碍物的依赖，显著提高了在复杂环境中的导航能力。

**关键设计**：在设计中，HERO采用了新的损失函数来优化障碍物交互的建模，并引入了层次化的场景关系表示，以增强模型的表达能力和推理能力。具体的网络结构和参数设置在实验中经过调优，以确保最佳性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15047v1/figures/figure_2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15047v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15047v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

HERO在实验中表现出显著的性能提升，相较于基线方法，在部分遮挡环境中路径长度减少了35.1%，在完全遮挡环境中成功率提高了79.4%。这些结果表明HERO在复杂环境中的高效性和可达性大幅提升。

## 🎯 应用场景

HERO框架具有广泛的应用潜力，特别是在机器人导航、智能家居、自动驾驶等领域。通过更好地理解和处理动态障碍物，HERO能够提升智能体在复杂环境中的自主导航能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> 3D Scene Graphs (3DSGs) constitute a powerful representation of the physical world, distinguished by their abilities to explicitly model the complex spatial, semantic, and functional relationships between entities, rendering a foundational understanding that enables agents to interact intelligently with their environment and execute versatile behaviors. Embodied navigation, as a crucial component of such capabilities, leverages the compact and expressive nature of 3DSGs to enable long-horizon reasoning and planning in complex, large-scale environments. However, prior works rely on a static-world assumption, defining traversable space solely based on static spatial layouts and thereby treating interactable obstacles as non-traversable. This fundamental limitation severely undermines their effectiveness in real-world scenarios, leading to limited reachability, low efficiency, and inferior extensibility. To address these issues, we propose HERO, a novel framework for constructing Hierarchical Traversable 3DSGs, that redefines traversability by modeling operable obstacles as pathways, capturing their physical interactivity, functional semantics, and the scene's relational hierarchy. The results show that, relative to its baseline, HERO reduces PL by 35.1% in partially obstructed environments and increases SR by 79.4% in fully obstructed ones, demonstrating substantially higher efficiency and reachability.

