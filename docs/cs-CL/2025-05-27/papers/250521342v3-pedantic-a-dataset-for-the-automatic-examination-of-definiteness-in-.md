---
layout: default
title: PEDANTIC: A Dataset for the Automatic Examination of Definiteness in Patent Claims
---

# PEDANTIC: A Dataset for the Automatic Examination of Definiteness in Patent Claims

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21342" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21342v3</a>
  <a href="https://arxiv.org/pdf/2505.21342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21342v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21342v3', 'PEDANTIC: A Dataset for the Automatic Examination of Definiteness in Patent Claims')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Valentin Knappich, Annemarie Friedrich, Anna Hätty, Simon Razniewski

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-06-18)

**备注**: PatentSemTech@SIGIR2025

---

## 💡 一句话要点

**提出PEDANTIC数据集以解决专利索赔不确定性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `专利审查` `自然语言处理` `数据集构建` `自动化检查` `大型语言模型`

## 📋 核心要点

1. 现有方法缺乏针对专利索赔不确定性检查的标注数据集，导致自动化检查效率低下。
2. 论文提出PEDANTIC数据集，利用自动化流程从USPTO获取文件，并通过大型语言模型提取不确定性原因。
3. 实验表明，基于Qwen 2.5的LLM在不确定性预测上未能超越逻辑回归基线，但能正确识别原因。

## 📝 摘要（中文）

专利索赔定义了发明的保护范围，索赔中的模糊性会导致专利申请被拒。在美国，这被称为不确定性，是专利申请拒绝的常见原因之一。本文介绍了PEDANTIC（专利不确定性检查语料库），这是一个包含14000个与自然语言处理相关的美国专利索赔的新数据集，并附有不确定性原因的注释。PEDANTIC通过自动化流程构建，利用大型语言模型提取不确定性原因，并通过人工验证研究确认了注释的准确性。该数据集为专利人工智能研究者提供了宝贵资源，促进先进检查模型的开发。

## 🔬 方法详解

**问题定义**：本文旨在解决专利索赔中的不确定性问题，现有方法缺乏标注数据集，导致专利申请审查效率低下。

**核心思路**：通过构建PEDANTIC数据集，利用自动化流程和大型语言模型提取不确定性原因，从而提高专利审查的自动化程度和准确性。

**技术框架**：整体流程包括从USPTO检索办公室行动文件，使用大型语言模型提取不确定性原因，并进行人工验证以确保注释质量。

**关键创新**：PEDANTIC数据集的构建是一个重要创新，首次提供了针对专利不确定性检查的标注数据，填补了这一领域的空白。

**关键设计**：在模型设计中，采用了大型语言模型进行原因提取，并通过人工验证确保注释的准确性，此外还实现了LLM-as-Judge评估方法以深入分析模型表现。

## 📊 实验亮点

实验结果显示，基于Qwen 2.5的LLM在不确定性预测上未能超越逻辑回归基线，尽管它们在识别原因方面表现良好。这表明当前LLM在专利索赔不确定性检查中的应用仍需进一步优化。

## 🎯 应用场景

该研究的潜在应用领域包括专利审查自动化、知识产权保护和法律技术等。PEDANTIC数据集的发布将促进相关领域的研究，推动智能化专利审查工具的发展，提高专利申请的处理效率和准确性。

## 📄 摘要（原文）

> Patent claims define the scope of protection for an invention. If there are ambiguities in a claim, it is rejected by the patent office. In the US, this is referred to as indefiniteness (35 U.S.C § 112(b)) and is among the most frequent reasons for patent application rejection. The development of automatic methods for patent definiteness examination has the potential to make patent drafting and examination more efficient, but no annotated dataset has been published to date. We introduce PEDANTIC (Patent Definiteness Examination Corpus), a novel dataset of 14k US patent claims from patent applications relating to Natural Language Processing (NLP), annotated with reasons for indefiniteness. We construct PEDANTIC using a fully automatic pipeline that retrieves office action documents from the USPTO and uses Large Language Models (LLMs) to extract the reasons for indefiniteness. A human validation study confirms the pipeline's accuracy in generating high-quality annotations. To gain insight beyond binary classification metrics, we implement an LLM-as-Judge evaluation that compares the free-form reasoning of every model-cited reason with every examiner-cited reason. We show that LLM agents based on Qwen 2.5 32B and 72B struggle to outperform logistic regression baselines on definiteness prediction, even though they often correctly identify the underlying reasons. PEDANTIC provides a valuable resource for patent AI researchers, enabling the development of advanced examination models. We will publicly release the dataset and code.

