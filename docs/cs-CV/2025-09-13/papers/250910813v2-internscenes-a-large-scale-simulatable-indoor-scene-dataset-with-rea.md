---
layout: default
title: "InternScenes: A Large-scale Simulatable Indoor Scene Dataset with Realistic Layouts"
---

# InternScenes: A Large-scale Simulatable Indoor Scene Dataset with Realistic Layouts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10813" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10813v2</a>
  <a href="https://arxiv.org/pdf/2509.10813.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10813v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10813v2', 'InternScenes: A Large-scale Simulatable Indoor Scene Dataset with Realistic Layouts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weipeng Zhong, Peizhou Cao, Yichen Jin, Li Luo, Wenzhe Cai, Jingli Lin, Hanqing Wang, Zhaoyang Lyu, Tai Wang, Bo Dai, Xudong Xu, Jiangmiao Pang

**分类**: cs.CV, cs.RO

**发布日期**: 2025-09-13 (更新: 2025-10-14)

---

## 💡 一句话要点

**InternScenes：一个具有真实布局的大规模可模拟室内场景数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `室内场景数据集` `具身智能` `场景布局生成` `点目标导航` `3D场景` `物理模拟` `数据集成`

## 📋 核心要点

1. 现有3D场景数据集在数据规模、多样性、布局真实性以及避免物体碰撞等方面存在局限性，阻碍了具身智能的发展。
2. InternScenes通过整合真实扫描、程序生成和人工设计三种来源，构建大规模、多样化、包含大量小物件且物理上可行的室内场景数据集。
3. 实验表明，InternScenes为场景布局生成和点目标导航带来了新的挑战，并为相关任务的模型训练提供了数据基础。

## 📝 摘要（中文）

本文提出了InternScenes，一个新型的大规模可模拟室内场景数据集，包含约40,000个多样化的场景。该数据集整合了三种不同的场景来源：真实世界扫描、程序生成场景和设计师创建场景，包括196万个3D对象，覆盖15种常见的场景类型和288个对象类别。InternScenes特别保留了场景中大量的小物件，从而形成了具有真实感和复杂性的布局，平均每个区域有41.5个对象。通过全面的数据处理流程，为真实世界扫描创建了真实到模拟的副本，通过将交互对象整合到这些场景中来增强交互性，并通过物理模拟解决了对象碰撞问题。通过场景布局生成和点目标导航两个基准应用，展示了InternScenes的价值，并揭示了复杂和真实的布局带来的新挑战。更重要的是，InternScenes为扩展模型训练提供了可能，使得在这种复杂场景中的生成和导航成为可能。数据集、模型和基准测试将开源。

## 🔬 方法详解

**问题定义**：现有具身智能研究严重依赖于大规模3D场景数据集，但现有数据集通常在数据规模、场景多样性、布局真实性（缺少小物件）以及物体碰撞问题上存在不足。这些问题限制了智能体在复杂真实环境中的学习和泛化能力。

**核心思路**：InternScenes的核心思路是整合多种来源的场景数据，包括真实世界扫描、程序生成场景和设计师创建场景，从而构建一个大规模、多样化、具有真实布局且物理上可行的室内场景数据集。通过数据处理流程，解决不同来源数据之间的差异，并确保场景的可模拟性。

**技术框架**：InternScenes的数据集构建流程主要包含以下几个阶段：1) 数据收集：从真实世界扫描、程序生成和设计师创建三个来源收集场景数据。2) 数据处理：对真实世界扫描数据进行真实到模拟的转换，添加交互对象，并使用物理模拟解决对象碰撞问题。3) 数据集成：将不同来源的数据集成到一个统一的数据集中，并进行标注。4) 基准测试：在InternScenes上进行场景布局生成和点目标导航两个基准测试。

**关键创新**：InternScenes的关键创新在于：1) 大规模和多样性：包含约40,000个场景，覆盖15种场景类型和288个对象类别。2) 真实布局：保留了场景中大量的小物件，使得布局更加真实和复杂。3) 可模拟性：通过数据处理流程，确保场景可以在物理引擎中进行模拟。4) 多来源集成：整合了真实扫描、程序生成和人工设计三种来源的数据，从而提高了数据集的多样性。

**关键设计**：在数据处理方面，使用了基于物理的模拟来解决对象碰撞问题，并使用启发式方法来添加交互对象。在基准测试方面，使用了标准的评估指标来评估场景布局生成和点目标导航的性能。具体参数设置和网络结构在论文中未详细说明，属于未知信息。

## 📊 实验亮点

在场景布局生成和点目标导航两个基准测试中，InternScenes数据集揭示了复杂和真实的布局带来的新挑战。同时，实验结果表明，使用InternScenes进行模型训练可以显著提升模型在复杂场景中的性能，为相关任务的研究提供了新的方向。

## 🎯 应用场景

InternScenes数据集可广泛应用于具身智能、机器人导航、场景理解、虚拟现实等领域。它为训练更智能、更鲁棒的智能体提供了数据基础，有助于提升机器人在复杂真实环境中的感知、决策和交互能力，并促进相关技术的发展。

## 📄 摘要（原文）

> The advancement of Embodied AI heavily relies on large-scale, simulatable 3D scene datasets characterized by scene diversity and realistic layouts. However, existing datasets typically suffer from limitations in data scale or diversity, sanitized layouts lacking small items, and severe object collisions. To address these shortcomings, we introduce \textbf{InternScenes}, a novel large-scale simulatable indoor scene dataset comprising approximately 40,000 diverse scenes by integrating three disparate scene sources, real-world scans, procedurally generated scenes, and designer-created scenes, including 1.96M 3D objects and covering 15 common scene types and 288 object classes. We particularly preserve massive small items in the scenes, resulting in realistic and complex layouts with an average of 41.5 objects per region. Our comprehensive data processing pipeline ensures simulatability by creating real-to-sim replicas for real-world scans, enhances interactivity by incorporating interactive objects into these scenes, and resolves object collisions by physical simulations. We demonstrate the value of InternScenes with two benchmark applications: scene layout generation and point-goal navigation. Both show the new challenges posed by the complex and realistic layouts. More importantly, InternScenes paves the way for scaling up the model training for both tasks, making the generation and navigation in such complex scenes possible. We commit to open-sourcing the data, models, and benchmarks to benefit the whole community.

