---
layout: default
title: "JOLT-SQL: Joint Loss Tuning of Text-to-SQL with Confusion-aware Noisy Schema Sampling"
---

# JOLT-SQL: Joint Loss Tuning of Text-to-SQL with Confusion-aware Noisy Schema Sampling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14305" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14305v3</a>
  <a href="https://arxiv.org/pdf/2505.14305.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14305v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14305v3', 'JOLT-SQL: Joint Loss Tuning of Text-to-SQL with Confusion-aware Noisy Schema Sampling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinwang Song, Hongying Zan, Kunli Zhang, Lingling Mu, Yingjie Han, Haobo Hua, Min Peng

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-09-23)

**备注**: Accepted to EMNLP 2025 Main Conference

**🔗 代码/项目**: [GITHUB](https://github.com/Songjw133/JOLT-SQL)

---

## 💡 一句话要点

**提出JOLT-SQL以解决文本到SQL映射中的噪声模式问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到SQL` `监督微调` `噪声模式` `模型鲁棒性` `自然语言处理` `数据库查询` `深度学习`

## 📋 核心要点

1. 现有的文本到SQL方法在处理噪声模式信息时表现不佳，导致鲁棒性不足。
2. JOLT-SQL通过单阶段的监督微调框架，联合优化模式链接与SQL生成，简化了流程。
3. 实验结果显示，JOLT-SQL在Spider和BIRD基准上达到了最先进的执行准确率，且训练和推理效率显著提升。

## 📝 摘要（中文）

文本到SQL的映射任务在大型语言模型的推动下取得了显著进展。然而，现有的监督微调方法面临着复杂的多阶段管道和对噪声模式信息的鲁棒性差等挑战。为了解决这些问题，本文提出了JOLT-SQL，一个简化的单阶段监督微调框架，通过统一损失函数联合优化模式链接和SQL生成。JOLT-SQL采用了带有局部双向注意力的判别式模式链接，并结合了具有选择性注意力的混淆感知噪声模式采样策略，以提高在噪声模式条件下的鲁棒性。在Spider和BIRD基准上的实验表明，JOLT-SQL在同类开源模型中实现了最先进的执行准确率，同时显著提高了训练和推理效率。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到SQL映射中的噪声模式信息对模型鲁棒性造成的影响。现有的监督微调方法通常依赖复杂的多阶段管道，难以有效处理噪声模式，导致性能下降。

**核心思路**：JOLT-SQL的核心思路是通过一个统一的损失函数，联合优化模式链接和SQL生成，简化了模型训练过程，并增强了对噪声模式的适应能力。

**技术框架**：JOLT-SQL的整体架构包括两个主要模块：判别式模式链接和SQL生成。判别式模式链接利用局部双向注意力机制来提高模式识别的准确性，而SQL生成则基于优化后的模式信息生成最终的SQL查询。

**关键创新**：JOLT-SQL的主要创新在于引入了混淆感知的噪声模式采样策略，结合选择性注意力机制，使得模型在面对噪声模式时能够更具鲁棒性。这一设计与传统方法的多阶段处理方式形成鲜明对比。

**关键设计**：在损失函数设计上，JOLT-SQL采用了联合损失函数来同时优化模式链接和SQL生成。此外，局部双向注意力的引入使得模型在处理复杂模式时能够更有效地捕捉上下文信息。

## 📊 实验亮点

在Spider和BIRD基准测试中，JOLT-SQL实现了最先进的执行准确率，相较于同类开源模型，训练和推理效率显著提升，具体性能数据未提供，但提升幅度明显。

## 🎯 应用场景

JOLT-SQL的研究成果在数据库查询生成、自然语言处理和智能问答系统等领域具有广泛的应用潜力。通过提高文本到SQL的映射准确性，该方法能够为用户提供更为精准的数据库查询支持，进而推动智能数据分析和决策支持系统的发展。

## 📄 摘要（原文）

> Text-to-SQL, which maps natural language to SQL queries, has benefited greatly from recent advances in Large Language Models (LLMs). While LLMs offer various paradigms for this task, including prompting and supervised fine-tuning (SFT), SFT approaches still face challenges such as complex multi-stage pipelines and poor robustness to noisy schema information. To address these limitations, we present JOLT-SQL, a streamlined single-stage SFT framework that jointly optimizes schema linking and SQL generation via a unified loss. JOLT-SQL employs discriminative schema linking, enhanced by local bidirectional attention, alongside a confusion-aware noisy schema sampling strategy with selective attention to improve robustness under noisy schema conditions. Experiments on the Spider and BIRD benchmarks demonstrate that JOLT-SQL achieves state-of-the-art execution accuracy among comparable-size open-source models, while significantly improving both training and inference efficiency. Our code is available at https://github.com/Songjw133/JOLT-SQL.

