---
layout: default
title: "Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning"
---

# Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04723" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04723v2</a>
  <a href="https://arxiv.org/pdf/2506.04723.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04723v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04723v2', 'Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiayu Wang, Yifei Ming, Zixuan Ke, Caiming Xiong, Shafiq Joty, Aws Albarghouthi, Frederic Sala

**分类**: cs.AI

**发布日期**: 2025-06-05 (更新: 2025-10-24)

**备注**: Accepted to NeurIPS 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://sparkle-reasoning.github.io/)

---

## 💡 一句话要点

**提出SPARKLE框架以深入理解RL对LLMs推理能力的影响**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `语言模型` `推理能力` `知识整合` `SPARKLE框架` `模型鲁棒性` `多阶段管道`

## 📋 核心要点

1. 现有RL方法在提升语言模型推理能力方面缺乏细致的理解，尤其是如何影响模型的执行和知识整合。
2. 本文提出SPARKLE框架，通过分析计划执行、知识整合和子问题链，深入探讨RL对模型推理的影响。
3. 实验结果表明，RL调优的模型在面对困难问题时表现出更好的鲁棒性，并且在知识整合方面取得了一致性提升。

## 📝 摘要（中文）

强化学习（RL）已成为提升语言模型在复杂推理任务中表现的主要方法。尽管RL训练方法如GRPO在实证上取得了显著进展，但对RL如何提升性能的细致理解仍然缺乏。为此，本文提出了SPARKLE框架，从计划执行、知识整合和子问题链三个维度分析RL的影响。研究发现，提供明确的步骤计划可能会降低模型在挑战性基准上的表现，而RL调优的模型则表现出更强的鲁棒性。此外，RL增强了模型将知识整合进推理过程的能力，带来了跨任务的一致性提升。最后，本文提出了SparkleRL-PSS，一个多阶段RL管道，利用部分步骤支架有效指导探索，避免了额外数据生成。

## 🔬 方法详解

**问题定义**：本文旨在解决对强化学习（RL）如何提升语言模型（LLMs）推理能力的理解不足，现有方法未能深入分析RL的具体影响。

**核心思路**：提出SPARKLE框架，从计划执行、知识整合和子问题链三个维度分析RL的影响，强调RL不仅提升了模型的执行能力，还增强了其知识整合能力。

**技术框架**：SPARKLE框架包含三个主要模块：计划执行模块、知识整合模块和子问题链模块。每个模块分别分析RL在不同推理维度上的作用。

**关键创新**：最重要的创新在于通过细致的维度分析，揭示了RL在推理任务中的多重作用，尤其是其在知识整合方面的显著提升，与传统方法相比具有更深层次的理解。

**关键设计**：在实验中，采用了多阶段RL管道SparkleRL-PSS，利用部分步骤支架来指导模型探索，避免了额外的数据生成需求。

## 📊 实验亮点

实验结果显示，RL调优的模型在面对困难问题时表现出更小的性能下降，相较于基线模型和SFT模型，鲁棒性显著增强。此外，模型在知识整合方面的表现也有一致性提升，展示了RL在多任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和教育技术等。通过深入理解RL对模型推理能力的影响，可以为构建更高效、适应性强的推理模型提供理论基础，进而推动相关技术的发展与应用。

## 📄 摘要（原文）

> Reinforcement learning (RL) has become the dominant paradigm for improving the performance of language models on complex reasoning tasks. Despite the substantial empirical gains demonstrated by RL-based training methods like GRPO, a granular understanding of why and how RL enhances performance is still lacking. To bridge this gap, we introduce SPARKLE, a fine-grained analytic framework to dissect the effects of RL across three key dimensions: (1) plan following and execution, (2) knowledge integration, and (3) chain of subproblems. Using this framework, we gain insights beyond mere accuracy. For instance, providing models with explicit human-crafted, step-by-step plans can surprisingly degrade performance on the most challenging benchmarks, yet RL-tuned models exhibit greater robustness, experiencing markedly smaller performance drops than base or SFT models. This suggests that RL may not primarily enhance the execution of external plans but rather empower models to formulate and follow internal strategies better suited to their reasoning processes. Conversely, we observe that RL enhances models' ability to integrate provided knowledge into their reasoning process, yielding consistent gains across diverse tasks. Finally, we study whether difficult problems -- those yielding no RL signals and mixed-quality reasoning traces -- can still be effectively used for training. We introduce SparkleRL-PSS, a multi-stage RL pipeline that reuses hard problems with partial step scaffolding, guiding exploration effectively without additional data generation. Together, our findings provide a principled foundation for understanding how RL shapes model behavior, offering practical insights for building more adaptive, data-efficient, and interpretable RL pipelines for reasoning tasks. Our code, data, and checkpoints are available at: https://sparkle-reasoning.github.io/.

