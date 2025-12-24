---
layout: default
title: "Learning to Rank Chain-of-Thought: Using a Small Model"
---

# Learning to Rank Chain-of-Thought: Using a Small Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14999" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14999v3</a>
  <a href="https://arxiv.org/pdf/2505.14999.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14999v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14999v3', 'Learning to Rank Chain-of-Thought: Using a Small Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eric Hanchen Jiang, Haozheng Luo, Shengyuan Pang, Xiaomin Li, Zhenting Qi, Hengli Li, Cheng-Fu Yang, Zongyu Lin, Xinfeng Li, Hao Xu, Kai-Wei Chang, Ying Nian Wu

**分类**: cs.LG, cs.AI, cs.CL, stat.ML

**发布日期**: 2025-05-21 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出能量结果奖励模型以提高数学推理的准确性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `能量结果奖励模型` `链式思维` `数学推理` `轻量级验证器` `高效推理` `模型泛化` `人工智能`

## 📋 核心要点

1. 现有的大型语言模型在数学推理方面表现不佳，且验证方法计算成本高，限制了其应用。
2. 本文提出的EORM通过能量框架对链式思维解决方案进行排序，利用简单的结果标签进行学习，避免了昂贵的标注。
3. EORM在GSM8k和MATH数据集上分别达到了90.7%和63.7%的准确率，显著提升了模型性能，并具备良好的泛化能力。

## 📝 摘要（中文）

大型语言模型（LLMs）在可靠的数学推理方面存在困难，现有的验证方法通常计算成本高昂。本文提出了一种高效、轻量级的后验验证器——能量结果奖励模型（EORM），旨在解决这一挑战。EORM采用基于能量的框架对链式思维（CoT）解决方案进行排序，仅使用简单的结果标签来区分正确与错误的推理，从而消除昂贵的标注需求。EORM参数仅为5500万，比典型奖励模型小127倍，显著提高了Llama 3 8B在GSM8k和MATH上的准确率，分别达到了90.7%和63.7%。该模型通过有效选择候选推理路径，能够匹配或超越资源密集型的最佳N采样技术的准确性。实验表明，EORM对分布外问题和未见模型具有良好的泛化能力，表明其学习了有效推理的基本原则。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在数学推理中的可靠性问题，现有验证方法计算成本高，难以广泛应用。

**核心思路**：EORM通过能量框架对推理结果进行排序，仅依赖简单的结果标签，避免了复杂的标注过程，从而提高了效率和准确性。

**技术框架**：EORM的整体架构包括输入链式思维解决方案，经过能量计算模块进行排序，最终输出最佳推理路径。主要模块包括能量计算、排序和结果评估。

**关键创新**：EORM的最大创新在于其轻量级设计和高效的能量排序机制，使其在准确性上能够与资源密集型的最佳N采样技术相媲美。

**关键设计**：EORM仅使用5500万参数，采用简单的损失函数和网络结构，确保在保持高效性的同时，能够有效学习推理的基本原则。通过优化参数设置，提升了模型的整体性能。

## 📊 实验亮点

EORM在GSM8k和MATH数据集上分别达到了90.7%和63.7%的准确率，显著优于传统的验证方法。与资源密集型的最佳N采样技术相比，EORM在准确性上匹配或超越，展示了其高效的推理能力和良好的泛化性能。

## 🎯 应用场景

EORM的研究成果在多个领域具有潜在应用价值，尤其是在教育、金融和科学计算等需要高可靠性推理的场景中。其高效性和准确性使其成为部署更可靠的语言模型的实用工具，能够在复杂的现实应用中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) struggle with reliable mathematical reasoning, and current verification methods are often computationally expensive. This paper introduces the Energy Outcome Reward Model (EORM), a highly efficient, lightweight post-hoc verifier designed to address this challenge. EORM uses an energy-based framework to rank Chain-of-Thought (CoT) solutions, learning to distinguish correct from incorrect reasoning using only simple outcome labels, thus eliminating the need for expensive annotations. With only 55M parameters, over 127 times smaller than typical reward models, EORM boosts the accuracy of Llama 3 8B to 90.7\% on GSM8k and 63.7\% on MATH. This performance is achieved by efficiently selecting the optimal reasoning path from a pool of candidates, allowing it to match or exceed the accuracy of far more resource-intensive Best-of-N sampling techniques. Crucially, our experiments show that EORM generalizes effectively to out-of-distribution problems and unseen models, indicating it learns fundamental principles of valid reasoning. This robustness, combined with its efficiency, establishes EORM as a practical tool for deploying more dependable LLMs in complex, real-world applications.

