---
layout: default
title: Reinforcement Learning for Out-of-Distribution Reasoning in LLMs: An Empirical Study on Diagnosis-Related Group Coding
---

# Reinforcement Learning for Out-of-Distribution Reasoning in LLMs: An Empirical Study on Diagnosis-Related Group Coding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21908" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21908v2</a>
  <a href="https://arxiv.org/pdf/2505.21908.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21908v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21908v2', 'Reinforcement Learning for Out-of-Distribution Reasoning in LLMs: An Empirical Study on Diagnosis-Related Group Coding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanyin Wang, Zhenbang Wu, Gururaj Kolar, Hariprasad Korsapati, Brian Bartlett, Bryan Hull, Jimeng Sun

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-28 (更新: 2025-10-14)

---

## 💡 一句话要点

**提出DRG-Sapphire以解决临床笔记中的DRG编码问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `诊断相关组` `自动化编码` `临床笔记` `可解释性` `领域特定挑战` `Qwen2.5-7B` `医疗数据分析`

## 📋 核心要点

1. 现有方法在DRG编码中面临的主要挑战是缺乏足够的领域知识，导致LLMs在处理临床数据时表现不佳。
2. 论文提出的DRG-Sapphire利用强化学习和基于规则的奖励机制，旨在提高DRG编码的自动化和准确性。
3. 实验结果表明，DRG-Sapphire在MIMIC-IV基准测试中达到了最先进的准确率，并提供了可解释的推理过程。

## 📝 摘要（中文）

诊断相关组（DRG）编码对医院的报销和运营至关重要，但其分配过程劳动密集。大型语言模型（LLMs）在DRG编码方面面临挑战，因为预训练语料库中很少包含私有临床或账单数据。本文提出DRG-Sapphire，利用大规模强化学习（RL）从临床笔记中自动进行DRG编码。该模型基于Qwen2.5-7B，采用基于规则的奖励进行组相对策略优化（GRPO）训练，针对以往数学任务未见的领域特定挑战引入了一系列RL增强。我们的模型在MIMIC-IV基准测试中实现了最先进的准确性，并生成了经过医生验证的DRG分配推理，显著增强了可解释性。

## 🔬 方法详解

**问题定义**：本文旨在解决DRG编码中的自动化问题，现有方法由于缺乏领域特定的训练数据，导致LLMs在此任务上表现不佳。

**核心思路**：DRG-Sapphire通过大规模强化学习，结合临床笔记中的信息，利用规则奖励机制来优化编码过程，从而提升模型的准确性和可解释性。

**技术框架**：该模型基于Qwen2.5-7B架构，采用组相对策略优化（GRPO）进行训练，整体流程包括数据预处理、模型训练、奖励计算和推理生成等主要模块。

**关键创新**：DRG-Sapphire的创新在于引入了针对领域特定挑战的强化学习增强，解决了以往方法在处理OOD任务时的局限性。

**关键设计**：模型的训练过程中采用了基于规则的奖励机制，设置了适当的超参数以平衡探索与利用，确保模型能够有效学习DRG编码的复杂性。

## 📊 实验亮点

DRG-Sapphire在MIMIC-IV基准测试中实现了最先进的准确率，具体性能数据表明，相较于传统方法，模型的准确性提升了显著的幅度，且生成的推理过程得到了医生的验证，增强了模型的可解释性。

## 🎯 应用场景

该研究的潜在应用领域包括医院管理、医疗账单处理和临床数据分析等。通过自动化DRG编码，医院可以提高运营效率，减少人工成本，同时提升编码的准确性和一致性，未来可能对医疗行业产生深远影响。

## 📄 摘要（原文）

> Diagnosis-Related Group (DRG) codes are essential for hospital reimbursement and operations but require labor-intensive assignment. Large Language Models (LLMs) struggle with DRG coding due to the out-of-distribution (OOD) nature of the task: pretraining corpora rarely contain private clinical or billing data. We introduce DRG-Sapphire, which uses large-scale reinforcement learning (RL) for automated DRG coding from clinical notes. Built on Qwen2.5-7B and trained with Group Relative Policy Optimization (GRPO) using rule-based rewards, DRG-Sapphire introduces a series of RL enhancements to address domain-specific challenges not seen in previous mathematical tasks. Our model achieves state-of-the-art accuracy on the MIMIC-IV benchmark and generates physician-validated reasoning for DRG assignments, significantly enhancing explainability. Our study further sheds light on broader challenges of applying RL to knowledge-intensive, OOD tasks. We observe that RL performance scales approximately linearly with the logarithm of the number of supervised fine-tuning (SFT) examples, suggesting that RL effectiveness is fundamentally constrained by the domain knowledge encoded in the base model. For OOD tasks like DRG coding, strong RL performance requires sufficient knowledge infusion prior to RL. Consequently, scaling SFT may be more effective and computationally efficient than scaling RL alone for such tasks.

