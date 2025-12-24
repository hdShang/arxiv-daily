---
layout: default
title: "COLLAGE: Adaptive Fusion-based Retrieval for Augmented Policy Learning"
---

# COLLAGE: Adaptive Fusion-based Retrieval for Augmented Policy Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01131" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01131v2</a>
  <a href="https://arxiv.org/pdf/2508.01131.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01131v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01131v2', 'COLLAGE: Adaptive Fusion-based Retrieval for Augmented Policy Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sateesh Kumar, Shivin Dass, Georgios Pavlakos, Roberto Martín-Martín

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-08-02 (更新: 2025-09-07)

**备注**: Accepted at the Conference on Robot Learning (CoRL), 2025. Project page: https://robin-lab.cs.utexas.edu/COLLAGE

---

## 💡 一句话要点

**提出COLLAGE以解决少样本模仿学习中的数据检索问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `少样本学习` `模仿学习` `数据检索` `自适应融合` `策略学习` `机器人技术` `多任务学习`

## 📋 核心要点

1. 现有方法依赖单一特征进行数据检索，可能导致不相关示例的引入，影响学习效果。
2. COLLAGE通过自适应晚期融合机制，结合多种特征来选择与目标任务相关的示例，提高数据检索的准确性。
3. 在广泛的实验中，COLLAGE在模拟环境中比现有方法提升了5.1%，在现实环境中提升了16.6%。

## 📝 摘要（中文）

本研究探讨了少样本模仿学习中的数据检索问题：从大型数据集中选择数据以训练特定任务的高效策略，仅依赖少量目标示例。现有方法使用单一特征距离启发式进行数据检索，可能导致不相关任务的数据被错误检索。我们提出COLLAGE，一种基于自适应晚期融合机制的集体数据聚合方法，能够根据任务特定的多重线索组合来指导相关示例的选择。COLLAGE在多个任务中表现优异，超越了现有的检索和多任务学习方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决少样本模仿学习中的数据检索问题。现有方法通常依赖单一特征进行数据选择，可能导致选择到与目标任务无关的示例，从而影响策略的学习效果。

**核心思路**：COLLAGE的核心思想是使用自适应晚期融合机制，根据任务特定的多重线索组合来选择相关示例。通过为数据集的子集分配权重，COLLAGE能够更有效地引导策略训练。

**技术框架**：COLLAGE的整体架构包括数据子集的预选择、权重分配和重要性采样三个主要模块。首先，使用单一特征（如外观、形状或语言相似性）预选数据子集；然后，根据在目标示例上的策略预测效果为这些子集分配权重；最后，在策略训练过程中进行重要性采样。

**关键创新**：COLLAGE的主要创新在于其自适应的多重线索融合机制，能够灵活结合任意数量的子集和检索启发式，与传统方法相比，显著提高了数据选择的相关性和有效性。

**关键设计**：在COLLAGE中，关键参数包括子集的选择标准和权重分配策略。损失函数设计上，强调了在目标示例上的预测准确性，以确保选择的示例对策略训练的贡献最大化。

## 📊 实验亮点

COLLAGE在实验中表现出色，模拟环境中比现有最先进的检索和多任务学习方法提升了5.1%，而在现实环境中更是提升了16.6%。这些结果表明COLLAGE在数据检索和策略学习中的有效性。

## 🎯 应用场景

COLLAGE在机器人学习、自动驾驶和人机交互等领域具有广泛的应用潜力。通过提高数据检索的准确性，该方法能够加速策略学习过程，提升系统在复杂任务中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> In this work, we study the problem of data retrieval for few-shot imitation learning: selecting data from a large dataset to train a performant policy for a specific task, given only a few target demonstrations. Prior methods retrieve data using a single-feature distance heuristic, assuming that the best demonstrations are those that most closely resemble the target examples in visual, semantic, or motion space. However, this approach captures only a subset of the relevant information and can introduce detrimental demonstrations, e.g., retrieving data from unrelated tasks due to similar scene layouts, or selecting similar motions from tasks with divergent goals. We present COLLAGE, a method for COLLective data AGgrEgation in few-shot imitation learning that uses an adaptive late fusion mechanism to guide the selection of relevant demonstrations based on a task-specific combination of multiple cues. COLLAGE follows a simple, flexible, and efficient recipe: it assigns weights to subsets of the dataset that are pre-selected using a single feature (e.g., appearance, shape, or language similarity), based on how well a policy trained on each subset predicts actions in the target demonstrations. These weights are then used to perform importance sampling during policy training, sampling data more densely or sparsely according to estimated relevance. COLLAGE is general and feature-agnostic, allowing it to combine any number of subsets selected by any retrieval heuristic, and to identify which subsets provide the greatest benefit for the target task. In extensive experiments, COLLAGE outperforms state-of-the-art retrieval and multi-task learning approaches by 5.1% in simulation across 10 tasks, and by 16.6% in the real world across 6 tasks, where we perform retrieval from the large-scale DROID dataset. More information at https://robin-lab.cs.utexas.edu/COLLAGE .

