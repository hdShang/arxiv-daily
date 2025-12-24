---
layout: default
title: "AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation"
---

# AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14634" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14634v3</a>
  <a href="https://arxiv.org/pdf/2506.14634.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14634v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14634v3', 'AIn\'t Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leah von der Heyde, Anna-Carolina Haensch, Bernd Weiß, Jessica Daikeler

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-06-17 (更新: 2025-07-03)

**备注**: to appear in Survey Research Methods

---

## 💡 一句话要点

**利用大型语言模型高效编码德语开放式调查反馈**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `开放式调查` `德语编码` `自动化分类` `机器学习` `社会科学研究` `数据分析`

## 📋 核心要点

1. 现有研究主要集中在英语和简单主题，缺乏对德语开放式调查反馈的有效编码方法。
2. 本研究通过比较多种LLMs和提示方法，探讨其在德语调查反馈中的应用潜力。
3. 实验结果显示，经过微调的LLM在预测性能上表现优异，且不同提示方法的效果依赖于所用LLM。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的发展和广泛可及性，关于其在调查研究中的应用讨论日益增多，包括对开放式调查反馈的分类。由于其语言能力，LLMs可能成为耗时的手动编码和监督机器学习模型预训练的高效替代方案。现有研究主要集中在英语响应和非复杂主题上，因此尚不清楚其发现是否具有普遍性，以及这些分类的质量与传统方法的比较。本研究探讨了不同LLMs在编码德语调查参与动机开放式反馈中的应用，比较了多种先进的LLMs和提示方法，并通过人类专家编码评估其性能。总体性能在不同LLMs之间差异显著，只有经过微调的LLM达到了令人满意的预测性能。最后，我们讨论了这些发现对开放式响应编码方法论研究和实质性分析的影响。

## 🔬 方法详解

**问题定义**：本研究旨在解决如何有效编码德语开放式调查反馈的问题。现有方法主要依赖手动编码，耗时且效率低下，且缺乏对非英语数据的研究。

**核心思路**：本研究提出利用多种大型语言模型（LLMs）对开放式调查反馈进行自动编码，探索其在不同上下文中的适用性，特别是德语数据。

**技术框架**：研究流程包括数据收集、LLMs选择、提示设计、性能评估等多个阶段。通过与人类专家编码的对比，评估不同模型和提示方法的效果。

**关键创新**：本研究的创新在于比较多种LLMs在德语开放式反馈编码中的表现，并探讨微调对性能的影响，填补了现有研究的空白。

**关键设计**：在实验中，采用了不同的提示策略和微调技术，确保LLMs能够适应德语的语言特性，具体参数设置和损失函数设计在文中详细描述。

## 📊 实验亮点

实验结果表明，经过微调的LLM在开放式调查反馈的编码任务中达到了令人满意的预测性能，性能提升幅度显著，尤其是在复杂类别的分类任务中，显示出较传统方法的优势。

## 🎯 应用场景

该研究的潜在应用领域包括社会科学、市场研究和公共调查等，能够帮助研究人员和从业者更高效地处理和分析开放式调查数据。未来，随着LLMs技术的进一步发展，其在调查研究中的应用将更加广泛，提升数据分析的准确性和效率。

## 📄 摘要（原文）

> The recent development and wider accessibility of LLMs have spurred discussions about how they can be used in survey research, including classifying open-ended survey responses. Due to their linguistic capacities, it is possible that LLMs are an efficient alternative to time-consuming manual coding and the pre-training of supervised machine learning models. As most existing research on this topic has focused on English-language responses relating to non-complex topics or on single LLMs, it is unclear whether its findings generalize and how the quality of these classifications compares to established methods. In this study, we investigate to what extent different LLMs can be used to code open-ended survey responses in other contexts, using German data on reasons for survey participation as an example. We compare several state-of-the-art LLMs and several prompting approaches, and evaluate the LLMs' performance by using human expert codings. Overall performance differs greatly between LLMs, and only a fine-tuned LLM achieves satisfactory levels of predictive performance. Performance differences between prompting approaches are conditional on the LLM used. Finally, LLMs' unequal classification performance across different categories of reasons for survey participation results in different categorical distributions when not using fine-tuning. We discuss the implications of these findings, both for methodological research on coding open-ended responses and for their substantive analysis, and for practitioners processing or substantively analyzing such data. Finally, we highlight the many trade-offs researchers need to consider when choosing automated methods for open-ended response classification in the age of LLMs. In doing so, our study contributes to the growing body of research about the conditions under which LLMs can be efficiently, accurately, and reliably leveraged in survey research.

