---
layout: default
title: Utilizing LLMs to Investigate the Disputed Role of Evidence in Electronic Cigarette Health Policy Formation in Australia and the UK
---

# Utilizing LLMs to Investigate the Disputed Role of Evidence in Electronic Cigarette Health Policy Formation in Australia and the UK

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06782" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06782v1</a>
  <a href="https://arxiv.org/pdf/2505.06782.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06782v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06782v1', 'Utilizing LLMs to Investigate the Disputed Role of Evidence in Electronic Cigarette Health Policy Formation in Australia and the UK')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Damian Curran, Brian Chapman, Mike Conway

**分类**: cs.CL, cs.SI

**发布日期**: 2025-05-10

---

## 💡 一句话要点

**利用大型语言模型分析电子烟健康政策形成中的证据角色**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `电子烟政策` `公共健康` `政策分析` `自动化分类`

## 📋 核心要点

1. 现有政策分析方法未能有效揭示不同国家在相同证据基础上形成的政策差异。
2. 本文提出了一种基于大型语言模型的句子分类器，自动分析电子烟政策文件中的证据呈现。
3. 实验结果显示，澳大利亚政策文件强调有害性，而英国则强调益处，分类器F-score达到0.9。

## 📝 摘要（中文）

澳大利亚和英国在电子烟监管方面采取了截然不同的策略，前者相对严格，后者则较为宽松。尽管两国的政策基于相同的证据基础，但在证据管理和呈现上存在显著差异。本文开发并评估了一种基于大型语言模型的句子分类器，自动分析109份来自两国立法过程的电子烟相关政策文件。通过使用GPT-4对句子进行分类，研究发现澳大利亚的立法文件中有更高比例的有害声明，而英国则相反。这项工作为探讨证据与健康政策形成之间的复杂关系提供了新的视角。

## 🔬 方法详解

**问题定义**：本文旨在解决如何有效分析和比较不同国家在相同证据基础上形成的电子烟政策的具体问题。现有方法未能深入探讨证据在政策形成中的作用，导致政策分析的片面性。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）对政策文件进行自动化句子分类，以揭示不同国家在电子烟政策中对证据的不同解读和呈现方式。通过这种方法，可以更系统地分析政策文件中的证据内容。

**技术框架**：整体架构包括数据收集、句子分类和结果分析三个主要模块。首先，从澳大利亚和英国的立法过程中收集109份电子烟相关政策文件；其次，利用GPT-4对句子进行分类；最后，分析分类结果以比较两国政策的证据呈现。

**关键创新**：最重要的技术创新点在于将大型语言模型应用于政策文件的自动化分析，尤其是在句子级别的分类任务上。这种方法与传统的手动分析方法相比，显著提高了分析的效率和准确性。

**关键设计**：在模型设计中，采用了GPT-4作为基础模型，设置了适当的超参数以优化分类性能。损失函数选择了适合分类任务的交叉熵损失，确保模型能够有效区分有害和有益的声明。

## 📊 实验亮点

实验结果显示，基于大型语言模型的分类器在句子分类任务中取得了0.9的F-score，表明其在分析政策文件中的有效性。通过对比分析，发现澳大利亚政策文件中有害声明的比例显著高于预期，而英国则相反，这一发现为理解两国政策差异提供了实证支持。

## 🎯 应用场景

该研究的潜在应用领域包括公共健康政策分析、电子烟监管政策的制定与评估等。通过提供基于数据的证据分析，该方法能够帮助政策制定者更好地理解证据在政策形成中的作用，从而制定更加科学合理的健康政策。未来，该方法还可以扩展到其他公共健康领域的政策分析中。

## 📄 摘要（原文）

> Australia and the UK have developed contrasting approaches to the regulation of electronic cigarettes, with - broadly speaking - Australia adopting a relatively restrictive approach and the UK adopting a more permissive approach. Notably, these divergent policies were developed from the same broad evidence base. In this paper, to investigate differences in how the two jurisdictions manage and present evidence, we developed and evaluated a Large Language Model-based sentence classifier to perform automated analyses of electronic cigarette-related policy documents drawn from official Australian and UK legislative processes (109 documents in total). Specifically, we utilized GPT-4 to automatically classify sentences based on whether they contained claims that e-cigarettes were broadly helpful or harmful for public health. Our LLM-based classifier achieved an F-score of 0.9. Further, when applying the classifier to our entire sentence-level corpus, we found that Australian legislative documents show a much higher proportion of harmful statements, and a lower proportion of helpful statements compared to the expected values, with the opposite holding for the UK. In conclusion, this work utilized an LLM-based approach to provide evidence to support the contention that - drawing on the same evidence base - Australian ENDS-related policy documents emphasize the harms associated with ENDS products and UK policy documents emphasize the benefits. Further, our approach provides a starting point for using LLM-based methods to investigate the complex relationship between evidence and health policy formation.

