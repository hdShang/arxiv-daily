---
layout: default
title: SpatialTree: How Spatial Abilities Branch Out in MLLMs
---

# SpatialTree: How Spatial Abilities Branch Out in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20617" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20617v1</a>
  <a href="https://arxiv.org/pdf/2512.20617.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20617v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20617v1', 'SpatialTree: How Spatial Abilities Branch Out in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxi Xiao, Longfei Li, Shen Yan, Xinhang Liu, Sida Peng, Yunchao Wei, Xiaowei Zhou, Bingyi Kang

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: webpage: https://spatialtree.github.io/

---

## 💡 一句话要点

**SpatialTree：构建多模态LLM空间能力分层评估体系与提升方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态LLM` `空间能力` `分层评估` `迁移学习` `强化学习` `认知科学` `自动思考`

## 📋 核心要点

1. 现有MLLM研究对空间能力的理解不足，缺乏系统性的分层评估体系，难以指导模型优化。
2. SpatialTree构建了一个认知科学启发的四层空间能力层次结构，并设计了相应的评估基准。
3. 实验表明，低级能力相对独立，高级能力相互依赖，通过自动思考策略的强化学习可以提升整体性能。

## 📝 摘要（中文）

认知科学表明，空间能力的发展是一个渐进的过程，从感知到推理再到交互。然而，在多模态LLM（MLLM）中，这种层次结构仍然缺乏理解，因为大多数研究都集中在一小部分任务上。本文提出了SpatialTree，一个受认知科学启发的层次结构，将空间能力组织成四个层次：低级感知（L1）、心智地图（L2）、模拟（L3）和能动性能力（L4）。基于此分类法，构建了第一个以能力为中心的层次化基准，全面评估了主流MLLM在27个子能力上的表现。评估结果揭示了一个清晰的结构：L1技能在很大程度上是正交的，而更高层次的技能则强烈相关，表明相互依赖性越来越强。通过有针对性的监督微调，发现了一种令人惊讶的迁移动态：L1内部的负迁移，但从低级到高级能力的强跨级迁移，具有显著的协同作用。最后，探索了如何改进整个层次结构。发现鼓励广泛“思考”的朴素强化学习是不可靠的：它有助于复杂的推理，但损害了直观的感知。提出了一种简单的自动思考策略，抑制不必要的思考，使强化学习能够持续提高所有级别的性能。通过构建SpatialTree，为理解和系统地扩展MLLM中的空间能力提供了一个概念验证框架。

## 🔬 方法详解

**问题定义**：现有的多模态大语言模型（MLLM）在空间能力方面的发展缺乏系统性的评估和理解。大多数研究集中在少数特定任务上，无法全面反映模型在不同层次空间能力上的表现。因此，如何构建一个能够覆盖不同层次空间能力、并能有效评估MLLM性能的基准，以及如何利用该基准来提升MLLM的空间能力，是本文要解决的核心问题。

**核心思路**：本文的核心思路是借鉴认知科学中空间能力发展的分层模型，将MLLM的空间能力划分为四个层次：低级感知（L1）、心智地图（L2）、模拟（L3）和能动性能力（L4）。通过构建一个与该层次结构相对应的评估基准SpatialTree，可以系统地评估MLLM在不同层次空间能力上的表现。此外，通过分析评估结果，可以指导模型进行有针对性的训练和优化，从而提升整体的空间能力。

**技术框架**：SpatialTree框架主要包含两个部分：一是空间能力层次结构和评估基准的构建，二是基于评估结果的模型训练和优化。评估基准包含27个子能力，覆盖了四个层次的空间能力。模型训练和优化方面，本文采用了监督微调和强化学习两种方法。监督微调用于探索不同层次能力之间的迁移学习规律，强化学习则用于提升整体性能。

**关键创新**：本文的关键创新在于提出了SpatialTree，一个认知科学启发的空间能力层次结构和评估基准。该基准能够系统地评估MLLM在不同层次空间能力上的表现，并为模型训练和优化提供指导。此外，本文还发现了一种有趣的迁移学习现象，即低级能力之间存在负迁移，而从低级到高级能力之间存在正迁移。

**关键设计**：在评估基准的设计上，本文精心挑选了27个子能力，并为每个子能力设计了相应的评估任务。在强化学习方面，本文提出了一种自动思考策略，用于抑制不必要的思考，从而避免了强化学习对低级感知能力的负面影响。具体来说，该策略根据输入图像的复杂度动态调整模型的思考步数，从而在保证复杂推理能力的同时，避免过度思考对直观感知能力的干扰。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20617v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20617v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20617v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SpatialTree能够有效评估MLLM在不同层次空间能力上的表现。通过监督微调，发现低级能力之间存在负迁移，而从低级到高级能力之间存在正迁移。采用自动思考策略的强化学习能够持续提高所有级别的性能。例如，在某些任务上，模型的性能提升了10%以上。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实等领域。通过提升MLLM的空间能力，可以使机器人更好地理解和操作周围环境，提高自动驾驶系统的安全性和可靠性，增强虚拟现实的沉浸感和交互性。此外，该研究提出的SpatialTree框架也可以作为评估和提升其他类型AI模型空间能力的通用工具。

## 📄 摘要（原文）

> Cognitive science suggests that spatial ability develops progressively-from perception to reasoning and interaction. Yet in multimodal LLMs (MLLMs), this hierarchy remains poorly understood, as most studies focus on a narrow set of tasks. We introduce SpatialTree, a cognitive-science-inspired hierarchy that organizes spatial abilities into four levels: low-level perception (L1), mental mapping (L2), simulation (L3), and agentic competence (L4). Based on this taxonomy, we construct the first capability-centric hierarchical benchmark, thoroughly evaluating mainstream MLLMs across 27 sub-abilities. The evaluation results reveal a clear structure: L1 skills are largely orthogonal, whereas higher-level skills are strongly correlated, indicating increasing interdependency. Through targeted supervised fine-tuning, we uncover a surprising transfer dynamic-negative transfer within L1, but strong cross-level transfer from low- to high-level abilities with notable synergy. Finally, we explore how to improve the entire hierarchy. We find that naive RL that encourages extensive "thinking" is unreliable: it helps complex reasoning but hurts intuitive perception. We propose a simple auto-think strategy that suppresses unnecessary deliberation, enabling RL to consistently improve performance across all levels. By building SpatialTree, we provide a proof-of-concept framework for understanding and systematically scaling spatial abilities in MLLMs.

