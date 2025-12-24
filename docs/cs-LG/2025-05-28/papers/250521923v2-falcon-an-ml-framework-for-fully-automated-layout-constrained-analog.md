---
layout: default
title: FALCON: An ML Framework for Fully Automated Layout-Constrained Analog Circuit Design
---

# FALCON: An ML Framework for Fully Automated Layout-Constrained Analog Circuit Design

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21923" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21923v2</a>
  <a href="https://arxiv.org/pdf/2505.21923.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21923v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21923v2', 'FALCON: An ML Framework for Fully Automated Layout-Constrained Analog Circuit Design')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Asal Mehradfar, Xuzhe Zhao, Yilun Huang, Emir Ceyani, Yankai Yang, Shihao Han, Hamidreza Aghasi, Salman Avestimehr

**分类**: cs.LG, cs.AI, cs.AR, cs.CE

**发布日期**: 2025-05-28 (更新: 2025-10-27)

**备注**: Accepted at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**提出FALCON框架以实现全自动化的模拟电路设计**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模拟电路设计` `机器学习` `图神经网络` `自动化设计` `性能预测` `布局优化` `电路拓扑` `深度学习`

## 📋 核心要点

1. 现有的模拟电路设计方法复杂且多阶段，难以实现完全自动化，尤其在拓扑选择和布局优化方面存在挑战。
2. FALCON框架通过性能驱动的分类器选择电路拓扑，并利用图神经网络进行参数推断，结合可微分布局成本进行优化。
3. 在大规模数据集上，FALCON实现了超过99%的拓扑推断准确率和小于10%的性能预测误差，展示了其高效性和实用性。

## 📝 摘要（中文）

设计模拟电路从性能规格出发是一个复杂的多阶段过程，包括拓扑选择、参数推断和布局可行性。本文介绍了FALCON，一个统一的机器学习框架，能够通过拓扑选择和布局约束优化，实现完全自动化的规格驱动模拟电路合成。FALCON首先使用性能驱动分类器选择合适的电路拓扑，然后利用训练好的边缘中心图神经网络，将电路拓扑和参数映射到性能，从而实现基于梯度的参数推断。推断过程受到可微分布局成本的指导，该成本源自捕捉寄生和频率依赖效应的解析方程，并受到设计规则的约束。FALCON在一个包含100万模拟毫米波电路的大规模自定义数据集上进行训练和评估，结果显示其在拓扑推断中准确率超过99%，性能预测的相对误差小于10%，并且每个实例的布局感知设计在1秒内完成。这些结果使FALCON成为端到端模拟电路设计自动化的实用且可扩展的基础模型。

## 🔬 方法详解

**问题定义**：本文旨在解决模拟电路设计中的自动化问题，现有方法在拓扑选择和布局优化上存在复杂性和效率低下的痛点。

**核心思路**：FALCON通过结合性能驱动的分类器和图神经网络，自动选择电路拓扑并进行参数推断，从而实现高效的电路设计。

**技术框架**：FALCON的整体架构包括两个主要模块：首先是拓扑选择模块，使用分类器根据性能规格选择电路拓扑；其次是参数推断模块，利用图神经网络进行性能映射和优化。

**关键创新**：FALCON的核心创新在于结合了可微分布局成本与图神经网络，使得电路设计不仅考虑性能，还考虑布局的可行性，这在现有方法中是较为少见的。

**关键设计**：在设计中，FALCON使用了边缘中心的图神经网络结构，训练过程中采用了特定的损失函数来优化性能预测，同时布局约束通过解析方程进行建模。

## 📊 实验亮点

FALCON在实验中展现出超过99%的拓扑推断准确率和小于10%的性能预测误差，且每个实例的设计时间不超过1秒。这些结果表明FALCON在电路设计自动化方面的显著提升，具有较强的实用性和效率。

## 🎯 应用场景

FALCON框架在模拟电路设计领域具有广泛的应用潜力，能够显著提高电路设计的自动化程度和效率。其实际价值体现在能够快速生成符合性能要求的电路布局，适用于通信、消费电子等多个行业。未来，FALCON有望扩展到更复杂的电路设计任务，推动电路设计的智能化进程。

## 📄 摘要（原文）

> Designing analog circuits from performance specifications is a complex, multi-stage process encompassing topology selection, parameter inference, and layout feasibility. We introduce FALCON, a unified machine learning framework that enables fully automated, specification-driven analog circuit synthesis through topology selection and layout-constrained optimization. Given a target performance, FALCON first selects an appropriate circuit topology using a performance-driven classifier guided by human design heuristics. Next, it employs a custom, edge-centric graph neural network trained to map circuit topology and parameters to performance, enabling gradient-based parameter inference through the learned forward model. This inference is guided by a differentiable layout cost, derived from analytical equations capturing parasitic and frequency-dependent effects, and constrained by design rules. We train and evaluate FALCON on a large-scale custom dataset of 1M analog mm-wave circuits, generated and simulated using Cadence Spectre across 20 expert-designed topologies. Through this evaluation, FALCON demonstrates >99% accuracy in topology inference, <10% relative error in performance prediction, and efficient layout-aware design that completes in under 1 second per instance. Together, these results position FALCON as a practical and extensible foundation model for end-to-end analog circuit design automation.

