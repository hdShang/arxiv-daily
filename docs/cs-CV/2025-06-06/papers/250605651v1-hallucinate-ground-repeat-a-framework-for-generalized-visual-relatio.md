---
layout: default
title: "Hallucinate, Ground, Repeat: A Framework for Generalized Visual Relationship Detection"
---

# Hallucinate, Ground, Repeat: A Framework for Generalized Visual Relationship Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05651" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05651v1</a>
  <a href="https://arxiv.org/pdf/2506.05651.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05651v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05651v1', 'Hallucinate, Ground, Repeat: A Framework for Generalized Visual Relationship Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shanmukha Vellamcheti, Sanjoy Kundu, Sathyanarayanan N. Aakur

**分类**: cs.CV

**发布日期**: 2025-06-06

**备注**: 22 pages, 9 figures, 5 tables

---

## 💡 一句话要点

**提出迭代视觉基础框架以解决视觉关系检测的泛化问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉关系检测` `大型语言模型` `开放世界` `场景理解` `智能系统`

## 📋 核心要点

1. 现有的视觉关系检测模型依赖固定的谓词集，无法有效处理新颖的物体关系，限制了其泛化能力。
2. 本文提出了一种迭代视觉基础框架，结合大型语言模型生成候选关系，并通过视觉模型进行验证，增强了关系理解能力。
3. 实验结果显示，模型在不同设置下的平均召回率分别为15.9、13.1和11.7，显著优于现有的LLM、少样本和去偏基线。

## 📝 摘要（中文）

理解物体之间的关系是视觉智能的核心，广泛应用于具身人工智能、辅助系统和场景理解。然而，大多数视觉关系检测模型依赖固定的谓词集，限制了其对新颖交互的泛化能力。本文提出了一种迭代视觉基础框架，利用大型语言模型作为结构化关系先验。该方法通过生成候选场景图和训练视觉模型交替进行，超越了注释数据的限制，实现了对未见谓词的泛化。此外，本文在Visual Genome上引入了一个新的开放世界视觉关系检测基准，包含21个保留谓词，并在不同设置下进行评估。实验结果表明，该模型在谓词分类上优于现有基线，展示了基于基础的LLM先验在可扩展开放世界视觉理解中的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉关系检测中对新颖交互的泛化能力不足的问题。现有方法通常依赖固定的谓词集，无法有效处理未标注的语义关系，限制了模型的应用范围。

**核心思路**：论文提出的迭代视觉基础框架通过结合大型语言模型（LLM）生成候选关系，并与视觉模型进行对齐，旨在超越传统的注释数据限制，实现对未见谓词的泛化。

**技术框架**：该框架采用类似期望最大化（EM）的方法，交替进行两个主要步骤：首先使用LLM生成候选场景图（期望步骤），然后训练视觉模型以对齐这些假设与感知证据（最大化步骤）。

**关键创新**：最重要的创新在于利用LLM作为结构化关系先验，能够在没有大量标注数据的情况下，推测出语义上合理的关系，从而实现更广泛的泛化能力。

**关键设计**：在模型设计中，关键参数包括候选关系生成的策略、视觉模型的训练损失函数，以及如何有效地整合LLM输出与视觉输入的网络结构。

## 📊 实验亮点

实验结果表明，提出的模型在不同设置下的平均召回率（mR@50）分别为15.9、13.1和11.7，显著优于仅使用LLM、少样本学习和去偏基线，展示了基于LLM的视觉关系检测在开放世界场景中的有效性和潜力。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、智能监控等，能够帮助系统更好地理解复杂场景中的物体关系，提升决策能力和交互效果。未来，该框架有望推动开放世界视觉理解的发展，促进更智能的人工智能系统的构建。

## 📄 摘要（原文）

> Understanding relationships between objects is central to visual intelligence, with applications in embodied AI, assistive systems, and scene understanding. Yet, most visual relationship detection (VRD) models rely on a fixed predicate set, limiting their generalization to novel interactions. A key challenge is the inability to visually ground semantically plausible, but unannotated, relationships hypothesized from external knowledge. This work introduces an iterative visual grounding framework that leverages large language models (LLMs) as structured relational priors. Inspired by expectation-maximization (EM), our method alternates between generating candidate scene graphs from detected objects using an LLM (expectation) and training a visual model to align these hypotheses with perceptual evidence (maximization). This process bootstraps relational understanding beyond annotated data and enables generalization to unseen predicates. Additionally, we introduce a new benchmark for open-world VRD on Visual Genome with 21 held-out predicates and evaluate under three settings: seen, unseen, and mixed. Our model outperforms LLM-only, few-shot, and debiased baselines, achieving mean recall (mR@50) of 15.9, 13.1, and 11.7 on predicate classification on these three sets. These results highlight the promise of grounded LLM priors for scalable open-world visual understanding.

