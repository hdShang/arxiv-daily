---
layout: default
title: Evaluation of LLMs for mathematical problem solving
---

# Evaluation of LLMs for mathematical problem solving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00309" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00309v3</a>
  <a href="https://arxiv.org/pdf/2506.00309.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00309v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00309v3', 'Evaluation of LLMs for mathematical problem solving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruonan Wang, Runxi Wang, Yunwen Shen, Chengfeng Wu, Qinglin Zhou, Rohitash Chandra

**分类**: cs.AI

**发布日期**: 2025-05-30 (更新: 2025-06-28)

---

## 💡 一句话要点

**评估大型语言模型在数学问题求解中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数学问题求解` `结构化思维链` `模型评估` `教育技术` `智能辅导系统`

## 📋 核心要点

1. 现有大型语言模型在数学问题求解中的表现尚未得到充分研究，存在准确性和稳定性不足的问题。
2. 本研究通过比较三种主要的LLMs，采用结构化思维链框架，从多个维度评估其数学问题求解能力。
3. 实验结果表明，GPT-4o在各数据集中的表现最为稳定，尤其在高难度问题上表现优异，其他模型则在特定领域表现出色但存在不足。

## 📝 摘要（中文）

大型语言模型（LLMs）在多种教育任务中表现出色，但其在数学问题求解中的潜力仍未得到充分研究。本研究比较了三种主要的LLMs，包括GPT-4o、DeepSeek-V3和Gemini-2.0，使用GSM8K、MATH500和MIT开放课程等三种不同复杂度的数学数据集。我们基于结构化思维链（SCoT）框架，从最终答案正确性、步骤完整性、步骤有效性、中间计算准确性和问题理解五个维度进行评估。结果显示，GPT-4o在所有数据集中表现最为稳定，尤其在MIT开放课程数据集的高难度问题上表现突出。DeepSeek-V3在结构良好的领域如优化中表现强劲，但在统计推断任务中准确性波动较大。Gemini-2.0在结构良好的问题中展现出强大的语言理解能力，但在多步骤推理和符号逻辑方面表现不佳。

## 🔬 方法详解

**问题定义**：本研究旨在评估大型语言模型在数学问题求解中的表现，现有方法在准确性和稳定性方面存在不足，尤其在复杂问题上表现不佳。

**核心思路**：通过比较三种主流的LLMs，采用结构化思维链（SCoT）框架，从多个维度进行评估，以全面了解模型在数学问题求解中的能力。

**技术框架**：整体架构包括数据集选择、模型比较、评估维度设定等，主要模块包括答案正确性、步骤完整性、步骤有效性、中间计算准确性和问题理解。

**关键创新**：本研究的创新点在于采用结构化思维链框架进行多维度评估，提供了更全面的模型性能分析，与传统单一维度评估方法有本质区别。

**关键设计**：在评估过程中，设置了具体的评估标准和指标，确保每个维度的评估具有可操作性和可重复性，确保结果的可靠性。

## 📊 实验亮点

实验结果显示，GPT-4o在所有数据集中的表现最为稳定，尤其在MIT开放课程数据集的高难度问题上表现突出，准确率显著高于其他模型。DeepSeek-V3在优化领域表现强劲，但在统计推断任务中准确性波动较大。Gemini-2.0在语言理解方面表现良好，但在多步骤推理中存在明显不足。

## 🎯 应用场景

该研究的结果对教育技术、智能辅导系统和数学教育领域具有重要的应用价值。通过提升大型语言模型在数学问题求解中的能力，可以为学生提供更智能的学习支持，促进个性化教育的发展。未来，这些模型有潜力在更广泛的学科领域中应用，推动教育技术的进步。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown impressive performance on a range of educational tasks, but are still understudied for their potential to solve mathematical problems. In this study, we compare three prominent LLMs, including GPT-4o, DeepSeek-V3, and Gemini-2.0, on three mathematics datasets of varying complexities (GSM8K, MATH500, and MIT Open Courseware datasets). We take a five-dimensional approach based on the Structured Chain-of-Thought (SCoT) framework to assess final answer correctness, step completeness, step validity, intermediate calculation accuracy, and problem comprehension. The results show that GPT-4o is the most stable and consistent in performance across all the datasets, but particularly it performs outstandingly in high-level questions of the MIT Open Courseware dataset. DeepSeek-V3 is competitively strong in well-structured domains such as optimisation, but suffers from fluctuations in accuracy in statistical inference tasks. Gemini-2.0 shows strong linguistic understanding and clarity in well-structured problems but performs poorly in multi-step reasoning and symbolic logic. Our error analysis reveals particular deficits in each model: GPT-4o is at times lacking in sufficient explanation or precision; DeepSeek-V3 leaves out intermediate steps; and Gemini-2.0 is less flexible in mathematical reasoning in higher dimensions.

