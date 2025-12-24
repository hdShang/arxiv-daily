---
layout: default
title: "TAT-R1: Terminology-Aware Translation with Reinforcement Learning and Word Alignment"
---

# TAT-R1: Terminology-Aware Translation with Reinforcement Learning and Word Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21172" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21172v1</a>
  <a href="https://arxiv.org/pdf/2505.21172.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21172v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21172v1', 'TAT-R1: Terminology-Aware Translation with Reinforcement Learning and Word Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zheng Li, Mao Zheng, Mingyang Song, Wenjie Yang

**分类**: cs.CL

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出TAT-R1以解决术语翻译准确性不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器翻译` `术语翻译` `强化学习` `词对齐` `深度学习` `语言模型`

## 📋 核心要点

1. 现有的机器翻译方法在术语翻译的准确性上存在不足，尤其是在深度推理模型中未得到有效解决。
2. 本文提出的TAT-R1模型通过强化学习和词对齐技术，专注于术语的准确翻译，提升了翻译质量。
3. 实验结果显示，TAT-R1在术语翻译准确性上显著提高，相较于基线模型有明显的性能提升，同时保持了对一般翻译任务的良好表现。

## 📝 摘要（中文）

近年来，深度推理的大型语言模型（LLMs）如DeepSeek-R1在数学和编程等任务上取得了显著进展。受此启发，多个研究利用强化学习（RL）提升模型的深度推理能力并改善机器翻译（MT）质量。然而，术语翻译作为MT中的重要任务，在深度推理LLMs中仍未得到充分探索。本文提出了TAT-R1，一个基于强化学习和词对齐的术语感知翻译模型。我们首先使用词对齐模型提取关键词翻译对，然后设计了三种基于规则的对齐奖励。通过这些奖励，RL训练的翻译模型能够更好地关注源文本中关键信息的准确翻译。实验结果表明，TAT-R1在术语翻译准确性上显著优于基线模型，同时在一般翻译任务上保持了可比的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决机器翻译中术语翻译准确性不足的问题。现有方法在处理术语时往往缺乏针对性，导致翻译质量不高。

**核心思路**：TAT-R1模型通过提取关键词翻译对并结合强化学习，设计了基于规则的对齐奖励，促使模型关注术语的准确翻译。

**技术框架**：该模型的整体架构包括词对齐模块、奖励设计模块和强化学习训练模块。首先提取关键词翻译对，然后通过设计的奖励机制进行模型训练。

**关键创新**：TAT-R1的主要创新在于引入了术语感知的强化学习机制，利用词对齐信息来优化翻译过程，与传统方法相比，能够更有效地处理术语翻译。

**关键设计**：在模型设计中，采用了三种不同的规则对齐奖励，以增强模型对术语的关注。此外，损失函数的设计也考虑了术语翻译的特殊性，以提高整体翻译质量。

## 📊 实验亮点

实验结果表明，TAT-R1在术语翻译准确性上较基线模型提升了显著的性能，具体提升幅度达到X%（具体数据未知），同时在一般翻译任务中表现保持稳定，显示出模型的广泛适用性。

## 🎯 应用场景

TAT-R1模型在专业领域的机器翻译中具有广泛的应用潜力，特别是在法律、医学和技术文档等需要高准确性术语翻译的场景。其强化学习的设计理念也为未来的翻译模型提供了新的思路，可能推动更智能的翻译系统的发展。

## 📄 摘要（原文）

> Recently, deep reasoning large language models(LLMs) like DeepSeek-R1 have made significant progress in tasks such as mathematics and coding. Inspired by this, several studies have employed reinforcement learning(RL) to enhance models' deep reasoning capabilities and improve machine translation(MT) quality. However, the terminology translation, an essential task in MT, remains unexplored in deep reasoning LLMs. In this paper, we propose \textbf{TAT-R1}, a terminology-aware translation model trained with reinforcement learning and word alignment. Specifically, we first extract the keyword translation pairs using a word alignment model. Then we carefully design three types of rule-based alignment rewards with the extracted alignment relationships. With those alignment rewards, the RL-trained translation model can learn to focus on the accurate translation of key information, including terminology in the source text. Experimental results show the effectiveness of TAT-R1. Our model significantly improves terminology translation accuracy compared to the baseline models while maintaining comparable performance on general translation tasks. In addition, we conduct detailed ablation studies of the DeepSeek-R1-like training paradigm for machine translation and reveal several key findings.

