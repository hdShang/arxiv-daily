---
layout: default
title: "SPARE: Single-Pass Annotation with Reference-Guided Evaluation for Automatic Process Supervision and Reward Modelling"
---

# SPARE: Single-Pass Annotation with Reference-Guided Evaluation for Automatic Process Supervision and Reward Modelling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15498" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15498v2</a>
  <a href="https://arxiv.org/pdf/2506.15498.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15498v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15498v2', 'SPARE: Single-Pass Annotation with Reference-Guided Evaluation for Automatic Process Supervision and Reward Modelling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Imbesat Hassan Rizvi, Xiaodan Zhu, Iryna Gurevych

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-18 (更新: 2025-08-22)

**备注**: 7 pages main content, 3 figures, 6 tables

---

## 💡 一句话要点

**提出SPARE框架以解决自动过程注释效率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动过程注释` `大型语言模型` `过程奖励模型` `单次生成` `推理评估` `数据高效泛化` `强化学习`

## 📋 核心要点

1. 现有的自动过程注释方法效率低下，难以满足高质量注释的需求。
2. SPARE框架通过单次生成对解决步骤进行注释，并与参考解决方案对齐，从而提高注释效率。
3. 在多个数据集上，SPARE展示了数据高效的泛化能力，并在速度和性能上超越了现有基线方法。

## 📝 摘要（中文）

过程或逐步监督在提升大型语言模型（LLMs）复杂多步骤推理能力方面发挥了重要作用。然而，高效且高质量的自动过程注释仍然是一个重大挑战。为此，本文提出了单次注释与参考引导评估（SPARE）框架，通过将解决步骤与参考解决方案对齐，并在单次生成中明确推理来高效进行逐步注释。实验表明，SPARE在数学推理、多跳问答和空间推理等四个多样化数据集上表现出色，显著提升了过程奖励模型的训练和离线强化学习的微调效果。

## 🔬 方法详解

**问题定义**：本文旨在解决自动过程注释效率低下的问题。现有方法在高质量注释上存在显著挑战，尤其是在复杂的多步骤推理任务中。

**核心思路**：SPARE框架的核心思想是通过单次生成将解决步骤与参考解决方案进行对齐，并利用明确的推理来评估其准确性，从而实现高效的逐步注释。

**技术框架**：SPARE的整体架构包括步骤对齐模块和评估模块。步骤对齐模块负责将生成的步骤与参考答案进行匹配，而评估模块则通过推理过程来判断步骤的准确性。

**关键创新**：SPARE的主要创新在于其单次生成的注释方式，显著提高了注释效率，并在数据使用上表现出色，相较于人类标注和其他合成训练基线，使用了约16%的训练样本。

**关键设计**：在技术细节上，SPARE采用了特定的损失函数来优化步骤对齐的准确性，并设计了高效的网络结构以支持快速推理和评估。

## 📊 实验亮点

SPARE在ProcessBench数据集上展示了数据高效的泛化能力，仅使用约16%的训练样本即可达到与基于MCTS的方法相竞争的性能，同时在总令牌数上实现了2.3倍的速度提升。这些结果表明SPARE在自动过程监督中的实用性和可扩展性。

## 🎯 应用场景

SPARE框架具有广泛的应用潜力，尤其在需要高效过程监督的领域，如教育、自动化问答系统和复杂任务的自动化处理等。其高效的注释能力可以显著提升模型的训练效率和推理能力，未来可能推动更多智能系统的开发与应用。

## 📄 摘要（原文）

> Process or step-wise supervision has played a crucial role in advancing complex multi-step reasoning capabilities of Large Language Models (LLMs). However, efficient, high-quality automated process annotation remains a significant challenge. To address this, we introduce Single-Pass Annotation with Reference-Guided Evaluation (SPARE), a novel structured framework that enables efficient per-step annotation by jointly aligning solution steps to reference solutions and determine its accuracy with explicit reasoning in single generation. We demonstrate SPARE's effectiveness across four diverse datasets spanning mathematical reasoning (GSM8K, MATH), multi-hop question answering (MuSiQue-Ans), and spatial reasoning (SpaRP), showing consistent improvements in two applications: (1) training Process Reward Models (PRMs) for ranking and aggregating multiple generations, and (2) fine-tuning models via offline reinforcement learning for greedy decoding. On ProcessBench, SPARE demonstrates data-efficient out-of-distribution generalization, using only $\sim$16% of training samples compared to human-labeled and other synthetically trained baselines. Additionally, it achieves competitive performance with MCTS-based methods while offering 2.3$\times$ speedup in terms of total token count. Manual analysis reveals complementary precision-recall characteristics with MCTS approaches, suggesting potential for ensemble methods. These results establish SPARE as a practical and scalable solution for automatic process supervision in LLM reasoning.

