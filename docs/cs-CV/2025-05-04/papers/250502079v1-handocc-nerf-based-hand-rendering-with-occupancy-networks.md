---
layout: default
title: HandOcc: NeRF-based Hand Rendering with Occupancy Networks
---

# HandOcc: NeRF-based Hand Rendering with Occupancy Networks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02079" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02079v1</a>
  <a href="https://arxiv.org/pdf/2505.02079.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02079v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02079v1', 'HandOcc: NeRF-based Hand Rendering with Occupancy Networks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maksym Ivashechkin, Oscar Mendez, Richard Bowden

**分类**: cs.CV

**发布日期**: 2025-05-04

---

## 💡 一句话要点

**提出HandOcc框架以解决手部渲染中的网格依赖问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `手部渲染` `占用网络` `NeRF` `3D骨架` `虚拟现实` `增强现实` `人机交互`

## 📋 核心要点

1. 现有的手部渲染方法依赖于参数化网格，导致在网格保真度与模型复杂性之间的权衡，限制了其泛化能力。
2. 我们提出了一种无网格3D渲染管道，通过3D骨架和卷积模型提取手部外观，结合占用网络和NeRF渲染器。
3. 在InterHand2.6M数据集上，我们的方法实现了最先进的渲染效果，显著提升了手部外观的真实感和渲染速度。

## 📝 摘要（中文）

我们提出了HandOcc，一个基于占用网络的手部渲染新框架。现有的渲染方法如NeRF通常与参数化网格结合，以提供可变形的手部模型。然而，这种方法在网格的保真度与参数模型的复杂性和维度之间存在权衡。我们的方法通过仅提供3D骨架，利用卷积模型提取所需外观，采用基于占用的表示条件化NeRF渲染器。该方法利用手部占用信息解决手部间的交互，进一步提升渲染效果，实现快速渲染和优异的手部外观传递。在InterHand2.6M基准数据集上，我们取得了最先进的结果。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有手部渲染方法对参数化网格的依赖问题。现有方法在网格保真度与模型复杂性之间存在权衡，且难以泛化到没有参数模型的对象。

**核心思路**：我们提出的HandOcc框架通过仅使用3D骨架，结合卷积模型和占用网络，来实现无网格的手部渲染。这种设计使得渲染过程不再依赖于网格初始化，提升了泛化能力。

**技术框架**：整体架构包括三个主要模块：首先是3D骨架输入，其次是卷积模型用于外观提取，最后是条件化的NeRF渲染器，利用占用表示进行渲染。

**关键创新**：本研究的核心创新在于引入占用网络来处理手部间的交互，显著提升了渲染效果和速度。这一方法与传统的网格依赖方法本质上不同，避免了网格分辨率和拟合精度的限制。

**关键设计**：在网络结构上，我们设计了特定的卷积层以提取手部特征，并使用占用网络来增强手部交互的建模能力。损失函数的设计也考虑了渲染效果的真实感与准确性。

## 📊 实验亮点

在InterHand2.6M数据集上，HandOcc框架实现了最先进的渲染效果，相较于传统方法，渲染速度显著提升，同时手部外观的真实感得到了极大增强，展示了该方法的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和人机交互等场景，能够为手部动作捕捉和渲染提供更高效和真实的解决方案。未来，该技术可能在游戏开发、动画制作以及医疗模拟等领域产生深远影响。

## 📄 摘要（原文）

> We propose HandOcc, a novel framework for hand rendering based upon occupancy. Popular rendering methods such as NeRF are often combined with parametric meshes to provide deformable hand models. However, in doing so, such approaches present a trade-off between the fidelity of the mesh and the complexity and dimensionality of the parametric model. The simplicity of parametric mesh structures is appealing, but the underlying issue is that it binds methods to mesh initialization, making it unable to generalize to objects where a parametric model does not exist. It also means that estimation is tied to mesh resolution and the accuracy of mesh fitting. This paper presents a pipeline for meshless 3D rendering, which we apply to the hands. By providing only a 3D skeleton, the desired appearance is extracted via a convolutional model. We do this by exploiting a NeRF renderer conditioned upon an occupancy-based representation. The approach uses the hand occupancy to resolve hand-to-hand interactions further improving results, allowing fast rendering, and excellent hand appearance transfer. On the benchmark InterHand2.6M dataset, we achieved state-of-the-art results.

