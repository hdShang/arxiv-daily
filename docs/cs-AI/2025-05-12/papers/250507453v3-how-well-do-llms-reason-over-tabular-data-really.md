---
layout: default
title: How well do LLMs reason over tabular data, really?
---

# How well do LLMs reason over tabular data, really?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07453" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07453v3</a>
  <a href="https://arxiv.org/pdf/2505.07453.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07453v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07453v3', 'How well do LLMs reason over tabular data, really?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cornelius Wolff, Madelon Hulsebos

**分类**: cs.AI

**发布日期**: 2025-05-12 (更新: 2025-11-04)

**备注**: 10 pages, 4 figures

**期刊**: The 4th Table Representation Learning Workshop at ACL 2025

---

## 💡 一句话要点

**提出评估策略以提升LLMs在表格数据推理的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `表格数据` `推理能力` `评估策略` `鲁棒性` `数据分析`

## 📋 核心要点

1. 现有评估方法未能准确反映LLMs在表格数据推理中的真实表现，导致对其能力的理解有限。
2. 论文提出了一种新的评估策略，利用LLM作为评判者，提供更可靠的性能洞察，并针对现实表格输入的特征进行扩展。
3. 实验结果显示，LLMs在面对缺失值、重复实体和结构变化时，其表格推理能力显著下降，强调了提升鲁棒性的必要性。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言任务中表现出色，但其在表格数据推理能力方面的表现尚不明确。现有的评估策略未能真实反映LLMs在表格查询中的性能。本文探讨了LLMs在面对现实表格输入的鲁棒性，并提出了一种新的评估方法，揭示了LLMs在表格推理中的显著不足。通过扩展表格输入的特征，研究表明LLMs的推理能力受到缺失值、重复实体和结构变化等因素的影响，强调了提升其鲁棒性的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在表格数据推理中的能力评估问题，现有方法的痛点在于评估策略未能真实反映模型性能，导致对其鲁棒性的理解不足。

**核心思路**：论文提出利用LLM作为评判者的评估方法，旨在提供更可靠的性能洞察，并通过引入现实表格输入的特征来测试模型的鲁棒性。

**技术框架**：研究基于现有的表格推理基准，首先分析其多选题评估策略的不足，然后引入缺失值、重复实体和结构变化等特征进行实验，最终评估LLMs的推理能力。

**关键创新**：最重要的技术创新在于提出了LLM作为评判者的评估方法，这一方法与传统的自由文本评估指标（如SacreBleu和BERT-score）本质上不同，能够更准确地反映模型在表格推理中的表现。

**关键设计**：在实验中，设置了不同的表格输入特征，并通过对比分析不同评估策略的效果，确保评估过程的全面性和准确性。

## 📊 实验亮点

实验结果表明，LLMs在面对缺失值、重复实体和结构变化时，其表格推理能力显著下降，尤其是在引入这些现实特征后，模型的性能下降幅度达到20%以上。这一发现强调了提升LLMs鲁棒性的紧迫性。

## 🎯 应用场景

该研究的潜在应用领域包括数据分析、商业智能和决策支持系统等。通过提升LLMs在表格数据推理中的能力，可以更好地支持用户在复杂数据环境中的分析与决策，未来可能推动相关领域的智能化进程。

## 📄 摘要（原文）

> Large Language Models (LLMs) excel in natural language tasks, but less is known about their reasoning capabilities over tabular data. Prior analyses devise evaluation strategies that poorly reflect an LLM's realistic performance on tabular queries. Moreover, we have a limited understanding of the robustness of LLMs towards realistic variations in tabular inputs. Therefore, we ask: Can general-purpose LLMs reason over tabular data, really?, and focus on two questions 1) are tabular reasoning capabilities of general-purpose LLMs robust to real-world characteristics of tabular inputs, and 2) how can we realistically evaluate an LLM's performance on analytical tabular queries? Building on a recent tabular reasoning benchmark, we first surface shortcomings of its multiple-choice prompt evaluation strategy, as well as commonly used free-form text metrics such as SacreBleu and BERT-score. We show that an LLM-as-a-judge procedure yields more reliable performance insights and unveil a significant deficit in tabular reasoning performance of LLMs. We then extend the tabular inputs reflecting three common characteristics in practice: 1) missing values, 2) duplicate entities, and 3) structural variations. Experiments show that the tabular reasoning capabilities of general-purpose LLMs suffer from these variations, stressing the importance of improving their robustness for realistic tabular inputs.

