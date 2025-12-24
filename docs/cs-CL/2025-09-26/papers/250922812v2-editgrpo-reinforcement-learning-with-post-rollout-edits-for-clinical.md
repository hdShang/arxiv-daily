---
layout: default
title: "EditGRPO: Reinforcement Learning with Post-Rollout Edits for Clinically Accurate Chest X-Ray Report Generation"
---

# EditGRPO: Reinforcement Learning with Post-Rollout Edits for Clinically Accurate Chest X-Ray Report Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22812" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22812v2</a>
  <a href="https://arxiv.org/pdf/2509.22812.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22812v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22812v2', 'EditGRPO: Reinforcement Learning with Post-Rollout Edits for Clinically Accurate Chest X-Ray Report Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Zhang, Christopher Malon, Lichao Sun, Martin Renqiang Min

**分类**: cs.CL

**发布日期**: 2025-09-26 (更新: 2025-11-10)

**备注**: AACL 2025

---

## 💡 一句话要点

**EditGRPO：结合后验编辑的强化学习，用于临床准确的胸部X光报告生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `放射学报告生成` `强化学习` `多模态学习` `临床准确性` `域外泛化`

## 📋 核心要点

1. 现有放射学报告生成方法缺乏与临床疗效的直接对齐，监督微调目标存在局限性。
2. EditGRPO通过混合策略强化学习，结合on-policy探索和off-policy指导，优化报告生成过程。
3. 实验表明，EditGRPO在临床指标和域外泛化能力上均优于现有方法，提升显著。

## 📝 摘要（中文）

放射学报告生成需要先进的医学图像分析、有效的时间推理和准确的文本生成。尽管最近的创新，特别是多模态大型语言模型，已经显示出性能的提升，但它们的监督微调（SFT）目标并没有明确地与临床疗效对齐。本文提出了EditGRPO，一种混合策略强化学习算法，专门设计用于通过临床驱动的奖励来优化生成过程。EditGRPO通过在训练过程中注入句子级别的详细修正，将on-policy探索与off-policy指导相结合。这种混合策略方法解决了RL中常见的探索困境和采样效率问题。应用于Qwen2.5-VL-3B模型，EditGRPO优于SFT和vanilla GRPO基线，在四个主要数据集上实现了平均3.4%的临床指标提升。值得注意的是，EditGRPO还表现出卓越的域外泛化能力，在未见数据集上的平均性能提升为5.9%。

## 🔬 方法详解

**问题定义**：放射学报告生成任务旨在根据医学图像自动生成准确且具有临床价值的报告。现有方法，特别是基于监督微调的多模态大型语言模型，虽然在文本生成方面有所提升，但其优化目标与临床疗效并不直接相关，导致生成的报告可能在临床上不够准确或实用。此外，强化学习在该领域的应用面临探索困境和采样效率低下的问题。

**核心思路**：EditGRPO的核心思路是通过强化学习直接优化报告的临床疗效。它采用一种混合策略，结合了on-policy探索和off-policy指导。On-policy探索允许模型学习新的策略，而off-policy指导则通过注入句子级别的详细修正来引导模型生成更准确的报告。这种混合策略旨在解决传统强化学习中的探索-利用平衡问题，并提高采样效率。

**技术框架**：EditGRPO的技术框架主要包括以下几个部分：1) 一个多模态大型语言模型（例如Qwen2.5-VL-3B）作为报告生成器；2) 一个奖励函数，用于评估生成报告的临床准确性；3) 一个混合策略强化学习算法，用于优化生成器的策略。在训练过程中，模型首先使用on-policy探索生成报告，然后通过off-policy指导注入句子级别的修正。修正后的报告用于更新模型的策略。

**关键创新**：EditGRPO的关键创新在于其混合策略强化学习算法，该算法结合了on-policy探索和off-policy指导。传统的强化学习方法要么只进行on-policy探索，要么只进行off-policy学习，而EditGRPO将两者结合起来，既能探索新的策略，又能利用已有的知识。此外，EditGRPO还引入了句子级别的详细修正，这使得模型能够更精确地学习如何生成准确的报告。

**关键设计**：EditGRPO的关键设计包括：1) 奖励函数的设计，需要能够准确评估报告的临床准确性；2) 混合策略的实现，需要平衡on-policy探索和off-policy指导；3) 句子级别修正的注入方式，需要确保修正能够有效地引导模型学习。具体的参数设置、损失函数和网络结构等细节可能需要根据具体的应用场景进行调整。

## 📊 实验亮点

EditGRPO在四个主要数据集上实现了平均3.4%的临床指标提升，显著优于SFT和vanilla GRPO基线。更重要的是，EditGRPO展现出卓越的域外泛化能力，在未见数据集上的平均性能提升高达5.9%。这些结果表明，EditGRPO能够有效地学习生成临床准确的放射学报告，并且具有良好的泛化能力。

## 🎯 应用场景

EditGRPO具有广泛的应用前景，可用于辅助放射科医生进行报告生成，提高诊断效率和准确性。该技术可以应用于各种医学影像报告生成任务，例如胸部X光、CT扫描和MRI等。此外，EditGRPO还可以用于医学教育和培训，帮助医学生学习如何撰写准确的放射学报告。未来，该技术有望与远程医疗相结合，为偏远地区的患者提供高质量的医疗服务。

## 📄 摘要（原文）

> Radiology report generation requires advanced medical image analysis, effective temporal reasoning, and accurate text generation. Although recent innovations, particularly multimodal large language models, have shown improved performance, their supervised fine-tuning (SFT) objective is not explicitly aligned with clinical efficacy. In this work, we introduce EditGRPO, a mixed-policy reinforcement learning algorithm designed specifically to optimize the generation through clinically motivated rewards. EditGRPO integrates on-policy exploration with off-policy guidance by injecting sentence-level detailed corrections during training rollouts. This mixed-policy approach addresses the exploration dilemma and sampling efficiency issues typically encountered in RL. Applied to a Qwen2.5-VL-3B, EditGRPO outperforms both SFT and vanilla GRPO baselines, achieving an average improvement of 3.4\% in clinical metrics across four major datasets. Notably, EditGRPO also demonstrates superior out-of-domain generalization, with an average performance gain of 5.9\% on unseen datasets.

