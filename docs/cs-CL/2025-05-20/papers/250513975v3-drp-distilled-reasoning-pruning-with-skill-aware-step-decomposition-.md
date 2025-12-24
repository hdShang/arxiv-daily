---
layout: default
title: "DRP: Distilled Reasoning Pruning with Skill-aware Step Decomposition for Efficient Large Reasoning Models"
---

# DRP: Distilled Reasoning Pruning with Skill-aware Step Decomposition for Efficient Large Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13975" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13975v3</a>
  <a href="https://arxiv.org/pdf/2505.13975.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13975v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13975v3', 'DRP: Distilled Reasoning Pruning with Skill-aware Step Decomposition for Efficient Large Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Jiang, Dawei Li, Frank Ferraro

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-08-22)

---

## 💡 一句话要点

**提出DRP以解决大型推理模型的效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型推理模型` `推理效率` `蒸馏训练` `技能感知` `内容剪枝` `数学推理` `知识转移`

## 📋 核心要点

1. 现有大型推理模型在推理时产生冗长的推理轨迹，导致效率低下和资源浪费。
2. 本文提出的DRP框架通过教师模型进行技能感知的步骤分解和内容剪枝，提升推理效率。
3. 实验结果表明，DRP在GSM8K数据集上将平均令牌使用量从917减少到328，同时准确率从91.7%提升至94.1%。

## 📝 摘要（中文）

大型推理模型（LRMs）在复杂推理任务中取得了成功，但其推理过程往往涉及冗长的推理轨迹，导致效率低下。为了解决这一问题，本文提出了蒸馏推理剪枝（DRP），这是一个结合了推理时剪枝和基于调优的蒸馏的混合框架。DRP利用教师模型进行技能感知的步骤分解和内容剪枝，然后将剪枝后的推理路径蒸馏到学生模型中，使其能够高效且准确地进行推理。在多个具有挑战性的数学推理数据集上，使用DRP训练的模型在令牌效率上取得了显著提升，同时保持了准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在推理过程中产生冗长推理轨迹的问题，现有方法在效率上存在明显不足。

**核心思路**：DRP框架结合了推理时剪枝与基于调优的蒸馏，通过教师模型的技能感知步骤分解来优化推理路径，从而提高推理效率。

**技术框架**：DRP的整体架构包括教师模型和学生模型两个主要模块。教师模型负责进行步骤分解和内容剪枝，而学生模型则通过蒸馏学习优化推理过程。

**关键创新**：DRP的核心创新在于技能感知的步骤分解与内容剪枝的结合，这一设计使得推理过程更加高效，与传统方法相比，显著减少了令牌使用量。

**关键设计**：在模型训练中，采用了特定的损失函数来平衡准确性与效率，同时在网络结构上进行了优化，以确保学生模型能够有效吸收教师模型的知识。

## 📊 实验亮点

实验结果显示，使用DRP训练的模型在GSM8K数据集上实现了917到328的令牌使用量减少，同时准确率从91.7%提升至94.1%。在AIME数据集上，DRP实现了43%的令牌减少，且没有性能下降，展现了其优越的效率和准确性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和科学研究等需要复杂推理的场景。通过提高大型推理模型的效率，DRP能够在资源有限的情况下，支持更广泛的应用，提升决策质量和速度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> While Large Reasoning Models (LRMs) have demonstrated success in complex reasoning tasks through long chain-of-thought (CoT) reasoning, their inference often involves excessively verbose reasoning traces, resulting in substantial inefficiency. To address this, we propose Distilled Reasoning Pruning (DRP), a hybrid framework that combines inference-time pruning with tuning-based distillation, two widely used strategies for efficient reasoning. DRP uses a teacher model to perform skill-aware step decomposition and content pruning, and then distills the pruned reasoning paths into a student model, enabling it to reason both efficiently and accurately. Across several challenging mathematical reasoning datasets, we find that models trained with DRP achieve substantial improvements in token efficiency without sacrificing accuracy. Specifically, DRP reduces average token usage on GSM8K from 917 to 328 while improving accuracy from 91.7% to 94.1%, and achieves a 43% token reduction on AIME with no performance drop. Further analysis shows that aligning the reasoning structure of training CoTs with the student's reasoning capacity is critical for effective knowledge transfer and performance gains.

