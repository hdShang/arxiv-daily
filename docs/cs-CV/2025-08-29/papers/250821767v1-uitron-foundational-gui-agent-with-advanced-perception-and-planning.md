---
layout: default
title: "UItron: Foundational GUI Agent with Advanced Perception and Planning"
---

# UItron: Foundational GUI Agent with Advanced Perception and Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.21767" class="toolbar-btn" target="_blank">📄 arXiv: 2508.21767v1</a>
  <a href="https://arxiv.org/pdf/2508.21767.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.21767v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.21767v1', 'UItron: Foundational GUI Agent with Advanced Perception and Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhixiong Zeng, Jing Huang, Liming Zheng, Wenkang Han, Yufeng Zhong, Lei Chen, Longrong Yang, Yingjie Chu, Yuzhi He, Lin Ma

**分类**: cs.CV

**发布日期**: 2025-08-29

**备注**: 24 pages

---

## 💡 一句话要点

**提出UItron以解决GUI代理自动化操作问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `GUI代理` `视觉语言模型` `数据工程` `强化学习` `移动应用` `自动化操作` `感知能力` `规划能力`

## 📋 核心要点

1. 现有的GUI代理方法面临操作轨迹稀缺和交互基础设施不足的挑战，限制了其在实际应用中的有效性。
2. UItron通过引入系统数据工程和交互基础设施，结合监督微调和课程强化学习，提升了GUI代理的感知和规划能力。
3. 实验结果表明，UItron在中国移动应用场景中显著提升了性能，尤其在与顶级中国移动应用的交互能力上取得了突破。

## 📝 摘要（中文）

GUI代理旨在实现移动和PC设备上的自动化操作，这是实现人工通用智能的重要任务。随着视觉语言模型（VLMs）的快速发展，GUI代理的开发得到了加速，因其在视觉理解和任务规划方面的强大能力。然而，由于操作轨迹稀缺、交互基础设施不足以及基础模型初始能力的限制，构建GUI代理仍然是一项挑战。本文介绍了UItron，一个开源的基础模型，具备先进的GUI感知、定位和规划能力。UItron强调了系统数据工程和交互基础设施作为GUI代理发展的基础组件的必要性，并通过一系列数据工程策略提升训练效果，同时建立了连接移动和PC设备的交互环境。通过在各种GUI场景中进行监督微调和课程强化学习框架的开发，UItron在GUI感知、定位和规划的基准测试中取得了优异的表现，尤其在中国移动应用场景中表现突出。

## 🔬 方法详解

**问题定义**：本文旨在解决GUI代理在移动和PC设备上的自动化操作问题，现有方法在操作轨迹和交互基础设施方面存在不足，限制了其应用效果。

**核心思路**：UItron的核心思路是通过系统的数据工程和交互基础设施，结合先进的感知和规划能力，提升GUI代理的整体性能。设计上，UItron采用了监督微调和课程强化学习，以适应复杂的在线环境。

**技术框架**：UItron的整体架构包括数据工程模块、交互环境模块和训练模块。数据工程模块负责收集和处理操作轨迹，交互环境模块连接移动和PC设备，训练模块则通过监督学习和强化学习进行模型训练。

**关键创新**：UItron的关键创新在于其系统化的数据工程策略和交互基础设施的构建，尤其是在中国移动应用场景中的应用，填补了现有方法在这一领域的空白。

**关键设计**：在训练过程中，UItron采用了多种损失函数和网络结构，特别是在感知和规划任务上进行了监督微调，确保模型能够有效地进行复杂推理和探索。

## 📊 实验亮点

实验结果显示，UItron在GUI感知、定位和规划的基准测试中表现优异，尤其在与中国移动应用的交互能力上，性能提升幅度超过了现有最先进的解决方案，标志着GUI代理技术的重大进步。

## 🎯 应用场景

UItron的研究成果在多个领域具有潜在应用价值，尤其是在智能助手、自动化办公和移动应用开发等场景中。通过提升GUI代理的交互能力，UItron能够推动人工智能在日常生活中的实际应用，促进人机交互的智能化进程。

## 📄 摘要（原文）

> GUI agent aims to enable automated operations on Mobile/PC devices, which is an important task toward achieving artificial general intelligence. The rapid advancement of VLMs accelerates the development of GUI agents, owing to their powerful capabilities in visual understanding and task planning. However, building a GUI agent remains a challenging task due to the scarcity of operation trajectories, the availability of interactive infrastructure, and the limitation of initial capabilities in foundation models. In this work, we introduce UItron, an open-source foundational model for automatic GUI agents, featuring advanced GUI perception, grounding, and planning capabilities. UItron highlights the necessity of systemic data engineering and interactive infrastructure as foundational components for advancing GUI agent development. It not only systematically studies a series of data engineering strategies to enhance training effects, but also establishes an interactive environment connecting both Mobile and PC devices. In training, UItron adopts supervised finetuning over perception and planning tasks in various GUI scenarios, and then develop a curriculum reinforcement learning framework to enable complex reasoning and exploration for online environments. As a result, UItron achieves superior performance in benchmarks of GUI perception, grounding, and planning. In particular, UItron highlights the interaction proficiency with top-tier Chinese mobile APPs, as we identified a general lack of Chinese capabilities even in state-of-the-art solutions. To this end, we manually collect over one million steps of operation trajectories across the top 100 most popular apps, and build the offline and online agent evaluation environments. Experimental results demonstrate that UItron achieves significant progress in Chinese app scenarios, propelling GUI agents one step closer to real-world application.

