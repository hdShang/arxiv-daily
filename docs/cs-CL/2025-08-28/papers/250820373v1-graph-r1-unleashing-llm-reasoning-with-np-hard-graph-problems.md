---
layout: default
title: "Graph-R1: Unleashing LLM Reasoning with NP-Hard Graph Problems"
---

# Graph-R1: Unleashing LLM Reasoning with NP-Hard Graph Problems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20373" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20373v1</a>
  <a href="https://arxiv.org/pdf/2508.20373.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20373v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20373v1', 'Graph-R1: Unleashing LLM Reasoning with NP-Hard Graph Problems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuyao Wang, Bowen Liu, Jianheng Tang, Nuo Chen, Yuhan Li, Qifan Zhang, Jia Li

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-28

**🔗 代码/项目**: [GITHUB](https://github.com/Graph-Reasoner/Graph-R1)

---

## 💡 一句话要点

**提出NP难度图问题以提升大型语言模型推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `NP难度图` `合成训练` `强化学习` `长链推理` `深度学习`

## 📋 核心要点

1. 现有方法在复杂推理任务上依赖高质量数据集，成本高且难以扩展。
2. 提出使用NP难度图问题作为合成训练语料库，增强模型的长链推理能力。
3. Graph-R1-7B模型在多个领域表现优异，超越了现有基线，提升了推理效率。

## 📝 摘要（中文）

近年来，推理大型语言模型（RLLMs）在复杂推理任务上取得了显著进展，这主要得益于其长链推理（Long CoT）能力。然而，开发这些能力依赖于高质量数据集的后期训练，这些数据集通常成本高且需人工策划。本文提出将NP难度图问题作为一种新型合成训练语料库，因为这些问题本质上需要深度推理、广泛探索和反思策略，这些都是长链推理的核心特征。我们开发了一个两阶段的后期训练框架，显著提升了推理深度和效率。我们的旗舰模型Graph-R1-7B在数学、编程、STEM和逻辑等领域表现出强大的泛化能力，并在NP难度图问题上超越了QwQ-32B，展现了良好的准确性和推理效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型在复杂推理任务中对高质量数据集的依赖问题，这些数据集通常成本高且难以获取。

**核心思路**：通过引入NP难度图问题作为合成训练语料库，利用其深度推理和探索的特性，来增强模型的长链推理能力。

**技术框架**：整体框架分为两个阶段：第一阶段是对拒绝采样的NP难度图实例进行长链推理的监督微调，第二阶段是通过细粒度奖励设计的强化学习来提升推理效率。

**关键创新**：最重要的创新在于将NP难度图问题作为训练数据源，提供了一种可扩展且有效的方式来提升大型语言模型的推理能力，与传统依赖人工策划数据集的方法形成鲜明对比。

**关键设计**：在训练过程中，采用了拒绝采样技术来选择图实例，并设计了细粒度的奖励机制，以优化模型的推理效率和准确性。

## 📊 实验亮点

实验结果显示，Graph-R1-7B在NP难度图问题上超越了QwQ-32B，表现出更高的准确性和推理效率，标志着在数学、编程和逻辑推理等领域的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育、编程辅助、科学研究等，能够为复杂推理任务提供高效的解决方案。通过提升大型语言模型的推理能力，未来可能在自动化决策、智能问答等领域产生深远影响。

## 📄 摘要（原文）

> Reasoning Large Language Models (RLLMs) have recently achieved remarkable progress on complex reasoning tasks, largely enabled by their long chain-of-thought (Long CoT) capabilities. However, developing these Long CoT behaviors relies heavily on post-training with high-quality datasets, which are typically costly and human-curated (e.g., mathematics and code), leaving scalable alternatives unexplored. In this work, we introduce NP-hard (NPH) graph problems as a novel synthetic training corpus, as they inherently require deep reasoning, extensive exploration, and reflective strategies, which are core characteristics of Long CoT reasoning. Building on this insight, we develop a two-stage post-training framework: (i) Long CoT Supervised Fine-Tuning (SFT) on rejection-sampled NPH graph instances, which substantially enhances reasoning depth, and (ii) Reinforcement Learning (RL) with a fine-grained reward design, which sharpens reasoning efficiency. Our flagship model, Graph-R1-7B, demonstrates strong generalization across mathematics, coding, STEM, and logic, and surpasses QwQ-32B on NPH graph problems in both accuracy and reasoning efficiency. These results position NPH graph problems as an effective and scalable resource for advancing Long CoT reasoning in LLMs, opening a new frontier for LLM post-training. Our implementation is available at https://github.com/Graph-Reasoner/Graph-R1, with models and datasets hosted in our Hugging Face collection HKUST-DSAIL/Graph-R1.

