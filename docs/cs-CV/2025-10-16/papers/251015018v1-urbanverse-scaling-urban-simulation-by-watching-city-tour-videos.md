---
layout: default
title: UrbanVerse: Scaling Urban Simulation by Watching City-Tour Videos
---

# UrbanVerse: Scaling Urban Simulation by Watching City-Tour Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15018" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15018v1</a>
  <a href="https://arxiv.org/pdf/2510.15018.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15018v1" onclick="toggleFavorite(this, '2510.15018v1', 'UrbanVerse: Scaling Urban Simulation by Watching City-Tour Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingxuan Liu, Honglin He, Elisa Ricci, Wayne Wu, Bolei Zhou

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-10-16

**备注**: Technical report. Project page: https://urbanverseproject.github.io/

---

## 💡 一句话要点

**UrbanVerse：通过城市漫游视频扩展城市模拟规模，用于具身智能体训练。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市模拟` `具身智能` `数据驱动` `真实到模拟` `城市导航`

## 📋 核心要点

1. 现有城市模拟环境构建方法难以兼顾可扩展性和真实世界复杂性，限制了具身智能体训练。
2. UrbanVerse利用城市漫游视频，自动构建具有物理感知和交互性的模拟场景，实现数据驱动的真实到模拟转换。
3. 实验表明，UrbanVerse生成的场景具有高度真实感，且训练的导航策略在模拟和真实环境中均表现出优异的泛化能力。

## 📝 摘要（中文）

城市具身AI智能体，如送货机器人和四足机器人，越来越多地出现在城市中，在复杂的街道上导航以提供最后一公里的连接。训练这些智能体需要多样化、高保真的城市环境，但现有的人工制作或程序生成的模拟场景要么缺乏可扩展性，要么无法捕捉真实世界的复杂性。我们介绍了UrbanVerse，一个数据驱动的真实到模拟系统，它将众包的城市漫游视频转换为具有物理感知、可交互的模拟场景。UrbanVerse包括：（i）UrbanVerse-100K，一个包含10万+带语义和物理属性的城市3D资产的仓库；（ii）UrbanVerse-Gen，一个自动管道，可以从视频中提取场景布局，并使用检索到的资产实例化度量尺度的3D模拟。UrbanVerse在IsaacSim中运行，提供来自24个国家的160个高质量构建场景，以及一个由艺术家设计的10个测试场景的基准。实验表明，UrbanVerse场景保留了真实世界的语义和布局，实现了与手动制作场景相当的人工评估真实感。在城市导航中，在UrbanVerse中训练的策略表现出缩放幂律和强大的泛化能力，与先前方法相比，在模拟中成功率提高了+6.3%，在零样本sim-to-real迁移中提高了+30.1%，仅通过两次干预就完成了300米的真实世界任务。

## 🔬 方法详解

**问题定义**：论文旨在解决城市具身智能体训练中，现有模拟环境构建方法无法同时满足可扩展性和真实世界复杂性的问题。人工构建成本高昂，程序生成则难以捕捉真实世界的细节，导致训练出的智能体在真实环境中表现不佳。

**核心思路**：论文的核心思路是利用众包的城市漫游视频，从中提取场景布局和3D资产，自动构建大规模、高保真的城市模拟环境。通过数据驱动的方式，避免了人工设计的局限性，并能更好地反映真实世界的复杂性。

**技术框架**：UrbanVerse包含两个主要组成部分：UrbanVerse-100K和UrbanVerse-Gen。UrbanVerse-100K是一个包含超过10万个带语义和物理属性的城市3D资产的数据库。UrbanVerse-Gen是一个自动管道，它从城市漫游视频中提取场景布局，并从UrbanVerse-100K中检索相应的3D资产，然后将这些资产实例化到IsaacSim中，生成可交互的3D模拟场景。

**关键创新**：该方法的关键创新在于利用城市漫游视频作为数据源，实现自动化的城市模拟环境构建。与传统的程序生成方法相比，该方法能够更好地捕捉真实世界的语义和布局信息。此外，UrbanVerse-100K的大规模3D资产库为场景的多样性和真实性提供了保障。

**关键设计**：UrbanVerse-Gen管道包含多个关键步骤，包括视频分割、场景布局估计、3D资产检索和场景实例化。视频分割用于将视频分解为独立的片段，场景布局估计用于从视频中推断出场景的几何结构和对象位置。3D资产检索用于从UrbanVerse-100K中找到与场景布局相匹配的3D模型。场景实例化则将检索到的3D模型放置到IsaacSim中，生成最终的模拟场景。具体参数设置和损失函数等细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，UrbanVerse生成的场景具有高度的真实感，与人工制作的场景相当。在城市导航任务中，使用UrbanVerse训练的策略在模拟环境中取得了显著的性能提升（+6.3%），并且在零样本sim-to-real迁移中表现出强大的泛化能力（+30.1%），仅通过两次干预就完成了300米的真实世界任务。这些结果表明，UrbanVerse是一种有效的城市模拟环境构建方法。

## 🎯 应用场景

UrbanVerse可广泛应用于城市具身智能体的训练和测试，例如送货机器人、自动驾驶汽车和巡逻机器人。通过在UrbanVerse中进行训练，可以提高智能体在真实城市环境中的导航和决策能力。此外，UrbanVerse还可以用于城市规划和虚拟现实等领域，为用户提供沉浸式的城市体验。

## 📄 摘要（原文）

> Urban embodied AI agents, ranging from delivery robots to quadrupeds, are increasingly populating our cities, navigating chaotic streets to provide last-mile connectivity. Training such agents requires diverse, high-fidelity urban environments to scale, yet existing human-crafted or procedurally generated simulation scenes either lack scalability or fail to capture real-world complexity. We introduce UrbanVerse, a data-driven real-to-sim system that converts crowd-sourced city-tour videos into physics-aware, interactive simulation scenes. UrbanVerse consists of: (i) UrbanVerse-100K, a repository of 100k+ annotated urban 3D assets with semantic and physical attributes, and (ii) UrbanVerse-Gen, an automatic pipeline that extracts scene layouts from video and instantiates metric-scale 3D simulations using retrieved assets. Running in IsaacSim, UrbanVerse offers 160 high-quality constructed scenes from 24 countries, along with a curated benchmark of 10 artist-designed test scenes. Experiments show that UrbanVerse scenes preserve real-world semantics and layouts, achieving human-evaluated realism comparable to manually crafted scenes. In urban navigation, policies trained in UrbanVerse exhibit scaling power laws and strong generalization, improving success by +6.3% in simulation and +30.1% in zero-shot sim-to-real transfer comparing to prior methods, accomplishing a 300 m real-world mission with only two interventions.

