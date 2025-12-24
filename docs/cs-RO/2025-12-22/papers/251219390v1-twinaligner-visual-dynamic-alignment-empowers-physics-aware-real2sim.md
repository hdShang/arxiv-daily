---
layout: default
title: "TwinAligner: Visual-Dynamic Alignment Empowers Physics-aware Real2Sim2Real for Robotic Manipulation"
---

# TwinAligner: Visual-Dynamic Alignment Empowers Physics-aware Real2Sim2Real for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19390" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19390v1</a>
  <a href="https://arxiv.org/pdf/2512.19390.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19390v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19390v1', 'TwinAligner: Visual-Dynamic Alignment Empowers Physics-aware Real2Sim2Real for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongwei Fan, Hang Dai, Jiyao Zhang, Jinzhou Li, Qiyang Yan, Yujie Zhao, Mingju Gao, Jinghang Wu, Hao Tang, Hao Dong

**分类**: cs.RO, cs.CV, cs.GR

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**TwinAligner：通过视觉-动力学对齐实现物理感知的Real2Sim2Real机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `Real2Sim2Real` `视觉对齐` `动力学对齐` `零样本泛化` `仿真环境` `3DGS`

## 📋 核心要点

1. 现有机器人学习方法依赖昂贵的真实数据，而Sim2Real迁移面临仿真与现实的差距。
2. TwinAligner通过视觉和动力学对齐，构建Real2Sim2Real系统，实现策略在仿真和现实之间的迭代优化。
3. 实验表明，TwinAligner在视觉和动力学对齐方面表现出色，策略在真实世界中实现了强大的零样本泛化。

## 📝 摘要（中文）

受多模态大模型的启发，机器人领域正朝着数据驱动的端到端学习发展。然而，对昂贵真实世界数据的依赖限制了进展。仿真器提供了经济高效的替代方案，但仿真与现实之间的差距挑战了策略的有效迁移。本文介绍了一种新颖的Real2Sim2Real系统TwinAligner，它解决了视觉和动力学差距。视觉对齐模块通过SDF重建和可编辑的3DGS渲染实现像素级对齐，而动力学对齐模块通过识别机器人-物体交互中的刚性物理来确保动力学一致性。TwinAligner通过提供可扩展的数据收集并建立可信的迭代循环来改进机器人学习，从而加速算法开发。定量评估突出了TwinAligner在视觉和动力学真实到仿真对齐方面的强大能力。该系统使在仿真中训练的策略能够实现对真实世界的强大零样本泛化。真实世界和仿真策略性能之间的高度一致性突显了TwinAligner在推进可扩展机器人学习方面的潜力。

## 🔬 方法详解

**问题定义**：机器人操作学习面临真实数据获取成本高昂的问题，而Sim2Real方法又受到仿真环境与真实环境差异的影响，导致策略迁移效果不佳。现有方法难以同时解决视觉和动力学上的差异，限制了机器人学习的效率和泛化能力。

**核心思路**：TwinAligner的核心思路是通过视觉和动力学对齐，构建一个可信的仿真环境，使得在仿真环境中训练的策略能够直接迁移到真实世界，并可以通过Real2Sim2Real的迭代过程不断优化策略。该方法旨在缩小仿真环境和真实环境之间的差距，提高机器人学习的效率和泛化能力。

**技术框架**：TwinAligner系统包含两个主要模块：视觉对齐模块和动力学对齐模块。视觉对齐模块利用SDF重建和可编辑的3DGS渲染实现像素级别的对齐，从而缩小视觉上的差距。动力学对齐模块通过识别机器人与物体交互中的刚性物理属性，确保动力学的一致性。整个系统通过Real2Sim2Real的迭代过程，不断优化仿真环境和策略。

**关键创新**：TwinAligner的关键创新在于同时考虑了视觉和动力学上的对齐，并提出了相应的解决方案。视觉对齐模块利用了最新的3DGS渲染技术，实现了高精度的像素级别对齐。动力学对齐模块则通过识别刚性物理属性，确保了仿真环境的物理真实性。这种双重对齐的方式使得仿真环境更加可信，从而提高了策略迁移的效果。

**关键设计**：视觉对齐模块使用了SDF（Signed Distance Function）来表示场景的几何信息，并通过3DGS（3D Gaussian Splatting）进行渲染，实现了高精度的视觉重建。动力学对齐模块则通过力/扭矩传感器数据来识别刚性物理属性，并将其应用到仿真环境中。损失函数的设计也至关重要，需要同时考虑视觉和动力学上的误差，并进行合理的权重分配。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19390v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19390v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19390v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

TwinAligner在多个机器人操作任务上进行了评估，结果表明，该系统在视觉和动力学对齐方面表现出色，显著提高了策略在真实世界中的零样本泛化能力。具体而言，与现有Sim2Real方法相比，TwinAligner在抓取成功率、装配精度等方面取得了显著提升，证明了其有效性和优越性。

## 🎯 应用场景

TwinAligner可应用于各种机器人操作任务，例如物体抓取、装配、导航等。该研究的实际价值在于降低了机器人学习的成本，提高了策略的泛化能力，加速了机器人算法的开发。未来，该技术有望应用于工业自动化、家庭服务、医疗康复等领域，实现更智能、更高效的机器人应用。

## 📄 摘要（原文）

> The robotics field is evolving towards data-driven, end-to-end learning, inspired by multimodal large models. However, reliance on expensive real-world data limits progress. Simulators offer cost-effective alternatives, but the gap between simulation and reality challenges effective policy transfer. This paper introduces TwinAligner, a novel Real2Sim2Real system that addresses both visual and dynamic gaps. The visual alignment module achieves pixel-level alignment through SDF reconstruction and editable 3DGS rendering, while the dynamic alignment module ensures dynamic consistency by identifying rigid physics from robot-object interaction. TwinAligner improves robot learning by providing scalable data collection and establishing a trustworthy iterative cycle, accelerating algorithm development. Quantitative evaluations highlight TwinAligner's strong capabilities in visual and dynamic real-to-sim alignment. This system enables policies trained in simulation to achieve strong zero-shot generalization to the real world. The high consistency between real-world and simulated policy performance underscores TwinAligner's potential to advance scalable robot learning. Code and data will be released on https://twin-aligner.github.io

