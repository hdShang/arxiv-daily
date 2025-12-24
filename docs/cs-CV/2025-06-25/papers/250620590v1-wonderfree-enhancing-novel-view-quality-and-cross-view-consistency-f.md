---
layout: default
title: "WonderFree: Enhancing Novel View Quality and Cross-View Consistency for 3D Scene Exploration"
---

# WonderFree: Enhancing Novel View Quality and Cross-View Consistency for 3D Scene Exploration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20590" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20590v1</a>
  <a href="https://arxiv.org/pdf/2506.20590.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20590v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20590v1', 'WonderFree: Enhancing Novel View Quality and Cross-View Consistency for 3D Scene Exploration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaojun Ni, Jie Li, Haoyun Li, Hengyu Liu, Xiaofeng Wang, Zheng Zhu, Guosheng Zhao, Boyuan Wang, Chenxin Li, Guan Huang, Wenjun Mei

**分类**: cs.CV

**发布日期**: 2025-06-25

---

## 💡 一句话要点

**提出WonderFree以解决3D场景探索中的视角一致性和图像质量问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `3D场景生成` `视角一致性` `图像质量` `数据驱动模型` `虚拟现实` `用户体验` `多视角恢复`

## 📋 核心要点

1. 现有3D生成方法在用户进行大幅度视角移动时，无法提供高质量的图像，限制了探索能力。
2. 提出WonderFree模型，通过WorldRestorer和ConsistView解决新视角质量和跨视角一致性问题。
3. 实验结果显示，WonderFree在多视角渲染质量和一致性上显著优于基线模型，用户偏好度达到77.20%。

## 📝 摘要（中文）

基于单幅图像的交互式3D场景生成因其在创建沉浸式虚拟世界中的潜力而受到广泛关注。然而，现有方法在用户进行大幅度视角移动时，无法渲染高质量图像，尤其是在进入未见区域时。为了解决这一挑战，本文提出了WonderFree，这是第一个允许用户从任意角度和方向交互生成3D世界的模型。我们将这一挑战分解为两个关键子问题：新视角质量和视角一致性。通过引入WorldRestorer模型来消除浮动和伪影，并提出ConsistView机制以增强跨视角一致性，实验结果表明WonderFree在多视角渲染质量和全局一致性方面显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决当前3D场景生成方法在用户进行大幅度视角移动时，无法渲染高质量图像的问题，尤其是在进入未见区域时，常出现浮动和伪影现象。

**核心思路**：通过将问题分解为新视角质量和跨视角一致性两个子问题，WonderFree模型采用数据驱动的方法来提升渲染质量和一致性，确保用户能够自由探索3D场景。

**技术框架**：WonderFree的整体架构包括WorldRestorer和ConsistView两个主要模块。WorldRestorer负责消除新视角中的浮动和伪影，而ConsistView则通过多视角联合恢复机制来保持不同视角间的空间一致性。

**关键创新**：最重要的创新在于引入WorldRestorer和ConsistView机制，前者通过数据驱动的方式提升新视角的图像质量，后者确保了不同视角间的时空一致性，这在现有方法中尚未实现。

**关键设计**：在WorldRestorer中，采用了特定的损失函数来优化图像质量，并设计了适应不同场景风格的数据收集管道，以确保模型的泛化能力。ConsistView则通过多视角联合恢复，利用时空信息来增强一致性。

## 📊 实验亮点

实验结果表明，WonderFree在多视角渲染质量上显著提升，用户偏好度达到77.20%，相较于基线模型WonderWorld，表现出更高的全局一致性和视觉质量。这些结果通过CLIP指标得到了验证，显示出其在3D场景生成中的实际应用价值。

## 🎯 应用场景

WonderFree的研究成果在虚拟现实、游戏开发和建筑可视化等领域具有广泛的应用潜力。通过提供高质量的3D场景生成和自由探索能力，用户可以在沉浸式环境中进行更为真实的交互体验，推动相关行业的发展与创新。

## 📄 摘要（原文）

> Interactive 3D scene generation from a single image has gained significant attention due to its potential to create immersive virtual worlds. However, a key challenge in current 3D generation methods is the limited explorability, which cannot render high-quality images during larger maneuvers beyond the original viewpoint, particularly when attempting to move forward into unseen areas. To address this challenge, we propose WonderFree, the first model that enables users to interactively generate 3D worlds with the freedom to explore from arbitrary angles and directions. Specifically, we decouple this challenge into two key subproblems: novel view quality, which addresses visual artifacts and floating issues in novel views, and cross-view consistency, which ensures spatial consistency across different viewpoints. To enhance rendering quality in novel views, we introduce WorldRestorer, a data-driven video restoration model designed to eliminate floaters and artifacts. In addition, a data collection pipeline is presented to automatically gather training data for WorldRestorer, ensuring it can handle scenes with varying styles needed for 3D scene generation. Furthermore, to improve cross-view consistency, we propose ConsistView, a multi-view joint restoration mechanism that simultaneously restores multiple perspectives while maintaining spatiotemporal coherence. Experimental results demonstrate that WonderFree not only enhances rendering quality across diverse viewpoints but also significantly improves global coherence and consistency. These improvements are confirmed by CLIP-based metrics and a user study showing a 77.20% preference for WonderFree over WonderWorld enabling a seamless and immersive 3D exploration experience. The code, model, and data will be publicly available.

