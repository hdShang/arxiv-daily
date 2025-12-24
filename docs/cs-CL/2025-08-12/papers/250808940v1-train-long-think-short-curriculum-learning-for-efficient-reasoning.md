---
layout: default
title: "Train Long, Think Short: Curriculum Learning for Efficient Reasoning"
---

# Train Long, Think Short: Curriculum Learning for Efficient Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08940" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08940v1</a>
  <a href="https://arxiv.org/pdf/2508.08940.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08940v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08940v1', 'Train Long, Think Short: Curriculum Learning for Efficient Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hasan Abed Al Kader Hammoud, Kumail Alhamoud, Abed Hammoud, Elie Bou-Zeid, Marzyeh Ghassemi, Bernard Ghanem

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-12

**备注**: Under Review

**🔗 代码/项目**: [GITHUB](https://github.com/hammoudhasan/curriculum_grpo)

---

## 💡 一句话要点

**提出课程学习策略以提高长语言模型的推理效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `课程学习` `推理能力` `群体相对策略优化` `长度控制` `模型训练`

## 📋 核心要点

1. 现有方法在推理过程中使用固定长度训练预算，未能充分利用学习中的探索与压缩过程。
2. 本文提出了一种课程学习策略，通过逐步收紧标记预算，促进模型从探索到提炼有效推理策略。
3. 实验结果表明，课程学习训练在多个数据集上均优于固定预算基线，准确性和标记效率显著提升。

## 📝 摘要（中文）

近年来，提升大型语言模型（LLMs）推理能力的研究引入了显式长度控制，以在保持准确性的同时降低计算成本。然而，现有方法依赖固定长度的训练预算，未能利用学习过程中的探索与压缩的自然进展。本文提出了一种基于课程学习的长度控制推理策略，使用群体相对策略优化（GRPO）。该方法从宽松的标记预算开始，逐渐收紧，鼓励模型首先发现有效的解决策略，然后将其提炼为更简洁的推理轨迹。通过在多个数据集上的实验，课程学习训练在相同的最终预算下始终优于固定预算基线，显示出更高的准确性和显著的标记效率提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型推理能力提升过程中，固定长度训练预算的局限性，导致模型未能充分利用学习过程中的探索与压缩。

**核心思路**：提出一种基于课程学习的策略，初期使用宽松的标记预算，逐步收紧预算，鼓励模型先探索有效的解决方案，再进行简化。

**技术框架**：整体方法基于群体相对策略优化（GRPO），包含三个主要模块：初始宽松的标记预算、逐步收紧的训练过程、以及平衡任务正确性、长度效率和格式遵循的奖励函数。

**关键创新**：最重要的创新在于引入课程学习策略，通过动态调整标记预算，促进模型在推理过程中逐步优化，区别于传统固定预算方法。

**关键设计**：设计了一个奖励函数，综合考虑任务正确性、长度效率和格式遵循，此外还进行了奖励权重和衰减调度的消融实验，以验证逐步约束的有效性。

## 📊 实验亮点

实验结果显示，课程学习训练在GSM8K、MATH500、SVAMP等数据集上均优于固定预算基线，准确性提升幅度达到X%，标记效率显著提高，展示了该方法在推理任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化问答系统和智能助手等，能够有效提升模型在复杂推理任务中的表现。通过优化推理过程，该方法有望在实际应用中降低计算资源消耗，提高响应速度，未来可能推动更高效的AI系统发展。

## 📄 摘要（原文）

> Recent work on enhancing the reasoning abilities of large language models (LLMs) has introduced explicit length control as a means of constraining computational cost while preserving accuracy. However, existing approaches rely on fixed-length training budgets, which do not take advantage of the natural progression from exploration to compression during learning. In this work, we propose a curriculum learning strategy for length-controlled reasoning using Group Relative Policy Optimization (GRPO). Our method starts with generous token budgets and gradually tightens them over training, encouraging models to first discover effective solution strategies and then distill them into more concise reasoning traces. We augment GRPO with a reward function that balances three signals: task correctness (via verifier feedback), length efficiency, and formatting adherence (via structural tags). Experiments on GSM8K, MATH500, SVAMP, College Math, and GSM+ demonstrate that curriculum-based training consistently outperforms fixed-budget baselines at the same final budget, achieving higher accuracy and significantly improved token efficiency. We further ablate the impact of reward weighting and decay schedule design, showing that progressive constraint serves as a powerful inductive bias for training efficient reasoning models. Our code and checkpoints are released at: https://github.com/hammoudhasan/curriculum_grpo.

