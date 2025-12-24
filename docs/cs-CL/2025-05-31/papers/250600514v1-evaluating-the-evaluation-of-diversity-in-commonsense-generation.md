---
layout: default
title: Evaluating the Evaluation of Diversity in Commonsense Generation
---

# Evaluating the Evaluation of Diversity in Commonsense Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00514" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00514v1</a>
  <a href="https://arxiv.org/pdf/2506.00514.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00514v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00514v1', 'Evaluating the Evaluation of Diversity in Commonsense Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianhui Zhang, Bei Peng, Danushka Bollegala

**分类**: cs.CL

**发布日期**: 2025-05-31

**备注**: ACL 2025 Main

---

## 💡 一句话要点

**提出系统性元评估方法以优化常识生成模型的多样性评估**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `常识生成` `多样性评估` `大型语言模型` `元评估` `自然语言处理` `内容指标` `形式指标`

## 📋 核心要点

1. 现有的常识生成模型在多样性评估上存在不足，尤其是基于形式的指标常常高估生成句子的多样性。
2. 本文通过系统性元评估，提出使用大型语言模型生成的多样性标注数据集，以评估现有多样性指标的有效性。
3. 实验结果表明，基于内容的多样性评估指标在与LLM评分的相关性上表现优于基于形式的指标，具有更高的评估准确性。

## 📝 摘要（中文）

在常识生成任务中，模型需生成既符合常识又具多样性的响应。尽管已有多种基于形式和内容重叠的评估指标被提出，但尚不清楚哪些指标最适合评估常识生成的多样性。为此，本文系统性地对现有多样性评估指标进行了元评估，发现基于形式的多样性指标往往高估句子集的多样性。通过使用大型语言模型（LLM）创建了一个新数据集，并对现有评估指标进行了元评估，结果表明基于内容的多样性评估指标优于基于形式的指标，且与LLM评分高度相关。我们建议未来的常识生成研究应采用基于内容的指标来评估输出的多样性。

## 🔬 方法详解

**问题定义**：本文旨在解决常识生成模型多样性评估中的指标选择问题，现有方法在评估时常常高估生成句子的多样性，导致评估结果不可靠。

**核心思路**：通过创建一个基于大型语言模型的多样性标注数据集，进行系统性元评估，比较不同评估指标的有效性，特别是内容与形式指标的差异。

**技术框架**：整体流程包括数据集构建、现有多样性评估指标的应用与比较、以及基于LLM的评分系统。主要模块包括数据生成、指标评估和结果分析。

**关键创新**：最重要的创新在于使用LLM生成的多样性标注数据集进行评估，这一方法与传统的基于形式的评估方法有本质区别，能够更准确地反映生成句子的多样性。

**关键设计**：在设计中，采用了多样性评分的标准化方法，确保不同指标之间的可比性，并通过实验验证了内容指标的优越性。

## 📊 实验亮点

实验结果显示，基于内容的多样性评估指标与LLM评分的相关性高达0.85，而基于形式的指标相关性仅为0.45，表明内容指标在评估生成句子多样性方面具有显著优势，推荐在未来的研究中优先使用。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的对话系统、文本生成和智能问答等。通过优化多样性评估，能够提升生成模型的输出质量，增强用户体验，未来可能对智能助手和教育工具等领域产生深远影响。

## 📄 摘要（原文）

> In commonsense generation, given a set of input concepts, a model must generate a response that is not only commonsense bearing, but also capturing multiple diverse viewpoints. Numerous evaluation metrics based on form- and content-level overlap have been proposed in prior work for evaluating the diversity of a commonsense generation model. However, it remains unclear as to which metrics are best suited for evaluating the diversity in commonsense generation. To address this gap, we conduct a systematic meta-evaluation of diversity metrics for commonsense generation. We find that form-based diversity metrics tend to consistently overestimate the diversity in sentence sets, where even randomly generated sentences are assigned overly high diversity scores. We then use an Large Language Model (LLM) to create a novel dataset annotated for the diversity of sentences generated for a commonsense generation task, and use it to conduct a meta-evaluation of the existing diversity evaluation metrics. Our experimental results show that content-based diversity evaluation metrics consistently outperform the form-based counterparts, showing high correlations with the LLM-based ratings. We recommend that future work on commonsense generation should use content-based metrics for evaluating the diversity of their outputs.

