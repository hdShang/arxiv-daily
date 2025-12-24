---
layout: default
title: Fluid Simulation on Vortex Particle Flow Maps
---

# Fluid Simulation on Vortex Particle Flow Maps

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21946" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21946v1</a>
  <a href="https://arxiv.org/pdf/2505.21946.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21946v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21946v1', 'Fluid Simulation on Vortex Particle Flow Maps')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sinan Wang, Junwei Zhou, Fan Feng, Zhiqi Li, Yuchen Sun, Duowen Chen, Greg Turk, Bo Zhu

**分类**: cs.GR, physics.flu-dyn

**发布日期**: 2025-05-28

**备注**: ACM Transactions on Graphics (SIGGRAPH 2025), 24 pages

**DOI**: [10.1145/3731198](https://doi.org/10.1145/3731198)

---

## 💡 一句话要点

**提出涡旋粒子流图方法以模拟复杂流体动力学**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `流体模拟` `涡旋粒子流图` `涡度演变` `动态边界` `计算流体动力学` `湍流现象` `数值稳定性`

## 📋 核心要点

1. 现有流体模拟方法在处理复杂涡旋演变和动态固体边界时存在流图距离短、涡度保持差等问题。
2. 论文提出的VPFM方法利用涡度作为粒子流图演变的核心量，结合混合的欧拉-拉格朗日表示法，显著提升流图长度。
3. 实验结果表明，VPFM在流图长度上比现有方法提升3到12倍，有效捕捉复杂的涡旋和湍流现象。

## 📝 摘要（中文）

本文提出了涡旋粒子流图（VPFM）方法，用于在动态固体边界下模拟具有复杂涡旋演变的不可压缩流体。我们的方法核心在于利用涡度作为粒子流图演变的理想量，相较于速度或冲量等其他流体量，能够实现显著更长的流图距离。为此，我们开发了一种混合的欧拉-拉格朗日表示法，在涡旋粒子上演变涡度和流图量，同时在背景网格上重构速度。该方法集成了三个关键组件：基于涡度的粒子流图框架、粒子上的准确Hessian演变方案，以及针对VPFM的无穿透和无滑移条件的固体边界处理。这些组件共同使得流图长度比现有技术提升了3到12倍，增强了涡度在扩展时空域上的保持能力。通过多样化的模拟验证了VPFM的性能，有效捕捉复杂涡旋动力学和湍流现象。

## 🔬 方法详解

**问题定义**：本文旨在解决现有流体模拟方法在复杂涡旋演变和动态固体边界下流图距离短、涡度保持差的问题。现有方法往往无法有效捕捉长时间尺度的流动特征。

**核心思路**：我们的方法核心在于利用涡度作为粒子流图演变的理想量，相比于速度或冲量等其他流体量，涡度能够实现更长的流图距离，从而更好地捕捉流体的复杂动态。

**技术框架**：VPFM方法采用混合的欧拉-拉格朗日表示法，主要包括三个模块：1) 基于涡度的粒子流图框架，2) 粒子上的准确Hessian演变方案，3) 针对VPFM的固体边界处理，确保无穿透和无滑移条件。

**关键创新**：VPFM的最重要创新在于其基于涡度的流图框架和长流图长度的实现，使得涡度在扩展时空域上的保持能力显著增强。这一设计与现有方法的本质区别在于对涡度的优先处理。

**关键设计**：在VPFM中，涡度的演变采用了高精度的Hessian演变方案，确保了粒子流图的准确性。同时，固体边界的处理策略确保了流体在边界条件下的物理合理性，避免了常见的数值不稳定性。

## 📊 实验亮点

VPFM方法在流图长度上实现了3到12倍的提升，相较于现有技术显著增强了涡度的保持能力。实验结果表明，该方法能够有效捕捉复杂的涡旋动力学和湍流现象，验证了其在多样化流体场景中的有效性。

## 🎯 应用场景

该研究的VPFM方法具有广泛的应用潜力，特别是在计算流体动力学、动画制作和虚拟现实等领域。通过更准确地模拟复杂流体行为，VPFM能够为工程设计、气候模拟和影视特效等提供更高效的解决方案，推动相关领域的发展。

## 📄 摘要（原文）

> We propose the Vortex Particle Flow Map (VPFM) method to simulate incompressible flow with complex vortical evolution in the presence of dynamic solid boundaries. The core insight of our approach is that vorticity is an ideal quantity for evolution on particle flow maps, enabling significantly longer flow map distances compared to other fluid quantities like velocity or impulse. To achieve this goal, we developed a hybrid Eulerian-Lagrangian representation that evolves vorticity and flow map quantities on vortex particles, while reconstructing velocity on a background grid. The method integrates three key components: (1) a vorticity-based particle flow map framework, (2) an accurate Hessian evolution scheme on particles, and (3) a solid boundary treatment for no-through and no-slip conditions in VPFM. These components collectively allow a substantially longer flow map length (3-12 times longer) than the state-of-the-art, enhancing vorticity preservation over extended spatiotemporal domains. We validated the performance of VPFM through diverse simulations, demonstrating its effectiveness in capturing complex vortex dynamics and turbulence phenomena.

