---
layout: default
title: Towards Physically Executable 3D Gaussian for Embodied Navigation
---

# Towards Physically Executable 3D Gaussian for Embodied Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21307" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21307v2</a>
  <a href="https://arxiv.org/pdf/2510.21307.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21307v2" onclick="toggleFavorite(this, '2510.21307v2', 'Towards Physically Executable 3D Gaussian for Embodied Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingchen Miao, Rong Wei, Zhiqi Ge, Xiaoquan sun, Shiqi Gao, Jingzhe Zhu, Renhan Wang, Siliang Tang, Jun Xiao, Rui Tang, Juncheng Li

**分类**: cs.CV

**发布日期**: 2025-10-24 (更新: 2025-12-15)

**备注**: Project Page: https://sage-3d.github.io/

---

## 💡 一句话要点

**提出SAGE-3D，增强3D高斯表达的语义和物理可执行性，用于具身导航。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D高斯溅射` `视觉语言导航` `具身智能` `语义分割` `物理仿真`

## 📋 核心要点

1. 现有3DGS缺乏细粒度的语义信息和物理可执行性，限制了其在视觉语言导航（VLN）中的应用。
2. SAGE-3D通过对象中心语义grounding和物理感知执行联合，为3DGS赋予了语义理解和物理交互能力。
3. 实验表明，基于3DGS的场景数据具有更强的泛化性，在VLN-CE Unseen任务上性能提升显著。

## 📝 摘要（中文）

本文提出SAGE-3D，一种新的范式，旨在将3D高斯溅射(3DGS)升级为可执行、语义和物理对齐的环境，用于视觉语言导航(VLN)。SAGE-3D包含两个关键组件：(1)面向对象的语义 grounding，为3DGS添加对象级别的细粒度注释；(2)物理感知的执行联合，将碰撞对象嵌入3DGS并构建丰富的物理接口。我们发布了InteriorGS，包含1K个对象注释的3DGS室内场景数据，并推出了SAGE-Bench，这是第一个基于3DGS的VLN基准，包含2M个VLN数据。实验表明，3DGS场景数据更难收敛，但表现出很强的泛化能力，在VLN-CE Unseen任务上将基线性能提高了31%。

## 🔬 方法详解

**问题定义**：现有基于3DGS的方法在具身导航任务中面临两个主要问题：一是缺乏细粒度的语义信息，无法进行对象级别的推理和交互；二是缺乏物理可执行性，无法模拟真实的物理交互过程，导致导航策略难以在真实环境中部署。现有方法难以弥合仿真环境与真实环境之间的差距。

**核心思路**：SAGE-3D的核心思路是将语义信息和物理信息融入到3DGS表示中，使其不仅具有逼真的渲染能力，还具备语义理解和物理交互能力。通过这种方式，可以构建一个更接近真实世界的仿真环境，从而提高导航策略的泛化能力。

**技术框架**：SAGE-3D包含两个主要模块：Object-Centric Semantic Grounding和Physics-Aware Execution Jointing。Object-Centric Semantic Grounding模块负责为3DGS中的每个高斯分布添加对象级别的语义标签，从而实现细粒度的语义理解。Physics-Aware Execution Jointing模块负责将碰撞对象嵌入到3DGS中，并构建物理接口，从而实现物理交互。

**关键创新**：SAGE-3D的关键创新在于将语义信息和物理信息显式地融入到3DGS表示中。与传统的基于几何或体素的表示方法相比，3DGS具有更强的渲染能力和更小的存储空间。与现有的基于3DGS的方法相比，SAGE-3D具有更强的语义理解和物理交互能力。

**关键设计**：Object-Centric Semantic Grounding模块使用预训练的3D对象检测模型为3DGS中的每个高斯分布分配语义标签。Physics-Aware Execution Jointing模块使用物理引擎模拟碰撞检测和物理交互。论文还设计了新的损失函数，用于优化语义标签和物理参数。

## 📊 实验亮点

实验结果表明，SAGE-3D能够显著提高视觉语言导航任务的性能。在VLN-CE Unseen任务上，基于SAGE-3D的导航策略比基线方法提高了31%。此外，SAGE-3D还能够生成高质量的语义分割结果和物理交互效果，验证了其在语义理解和物理交互方面的有效性。

## 🎯 应用场景

SAGE-3D可应用于机器人导航、虚拟现实、增强现实等领域。例如，可以用于训练机器人在复杂室内环境中进行导航，也可以用于构建逼真的虚拟环境，供用户进行交互和体验。该研究有助于提升机器人的自主性和智能化水平，并为虚拟现实和增强现实应用提供更真实、更具交互性的体验。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS), a 3D representation method with photorealistic real-time rendering capabilities, is regarded as an effective tool for narrowing the sim-to-real gap. However, it lacks fine-grained semantics and physical executability for Visual-Language Navigation (VLN). To address this, we propose SAGE-3D (Semantically and Physically Aligned Gaussian Environments for 3D Navigation), a new paradigm that upgrades 3DGS into an executable, semantically and physically aligned environment. It comprises two components: (1) Object-Centric Semantic Grounding, which adds object-level fine-grained annotations to 3DGS; and (2) Physics-Aware Execution Jointing, which embeds collision objects into 3DGS and constructs rich physical interfaces. We release InteriorGS, containing 1K object-annotated 3DGS indoor scene data, and introduce SAGE-Bench, the first 3DGS-based VLN benchmark with 2M VLN data. Experiments show that 3DGS scene data is more difficult to converge, while exhibiting strong generalizability, improving baseline performance by 31% on the VLN-CE Unseen task. Our data and code are available at: https://sage-3d.github.io.

