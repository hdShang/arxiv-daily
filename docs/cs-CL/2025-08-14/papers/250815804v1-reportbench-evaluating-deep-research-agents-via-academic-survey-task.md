---
layout: default
title: "ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks"
---

# ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15804" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15804v1</a>
  <a href="https://arxiv.org/pdf/2508.15804.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15804v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15804v1', 'ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minghao Li, Ying Zeng, Zhihao Cheng, Cong Ma, Kai Jia

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-14

**🔗 代码/项目**: [GITHUB](https://github.com/ByteDance-BandAI/ReportBench)

---

## 💡 一句话要点

**提出ReportBench以评估深度研究代理的学术调查任务**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度研究代理` `内容质量评估` `大型语言模型` `自动化框架` `引用文献分析`

## 📋 核心要点

1. 现有的深度研究代理在生成研究报告时，常常面临事实准确性和全面性不足的问题，影响其应用效果。
2. 本文提出ReportBench，通过系统化的基准评估生成报告的内容质量，重点关注引用文献的相关性和陈述的真实性。
3. 实验结果显示，商业深度研究代理生成的报告在质量上优于单独的语言模型，但在研究覆盖和事实一致性方面仍需改进。

## 📝 摘要（中文）

随着深度研究代理的出现，进行广泛研究任务所需的时间显著减少。然而，这些任务对事实准确性和全面性有严格要求，因此在广泛应用之前需要进行彻底评估。本文提出了ReportBench，一个系统化的基准，用于评估大型语言模型生成的研究报告的内容质量。我们的评估集中在两个关键维度：引用文献的质量和相关性，以及生成报告中陈述的真实性和可靠性。ReportBench利用arXiv上高质量的已发布调查论文作为金标准参考，通过反向提示工程提取领域特定提示，建立全面的评估语料库。此外，我们在ReportBench中开发了一个基于代理的自动化框架，系统分析生成的报告，提取引用和陈述，检查引用内容的真实性，并使用网络资源验证未引用的主张。实证评估表明，商业深度研究代理（如OpenAI和Google开发的代理）生成的报告在全面性和可靠性上优于单独的语言模型，但在研究覆盖的广度和深度以及事实一致性方面仍有很大改进空间。

## 🔬 方法详解

**问题定义**：本文旨在解决深度研究代理生成的研究报告在事实准确性和全面性方面的评估问题。现有方法缺乏系统化的评估标准，导致生成内容的质量难以保证。

**核心思路**：我们提出ReportBench作为评估框架，利用高质量的调查论文作为参考，通过反向提示工程生成领域特定的评估提示，从而建立全面的评估语料库。

**技术框架**：ReportBench的整体架构包括数据收集、提示生成、报告分析和结果验证四个主要模块。首先，收集高质量的调查论文作为金标准；其次，应用反向提示工程生成评估提示；然后，分析生成的报告，提取引用和陈述；最后，验证引用内容和未引用主张的真实性。

**关键创新**：ReportBench的主要创新在于其系统化的评估方法和基于代理的自动化框架，能够全面分析生成报告的内容质量，与现有方法相比，提供了更为严格和全面的评估标准。

**关键设计**：在设计中，我们设置了高质量的参考文献库，采用了多种验证机制，包括对引用内容的真实性检查和对未引用主张的网络资源验证，确保评估结果的可靠性。

## 📊 实验亮点

实验结果表明，商业深度研究代理生成的报告在内容的全面性和可靠性上显著优于单独的语言模型，尤其是在引用文献的质量和陈述的真实性方面。具体而言，使用ReportBench评估的代理在多个维度上均表现出较高的性能，提升幅度明显。

## 🎯 应用场景

ReportBench的研究成果可广泛应用于学术研究、自动化文献综述、以及深度学习模型的评估等领域。其系统化的评估框架为研究人员提供了一个可靠的工具，以提高生成报告的质量和可信度，未来可能推动深度研究代理的更广泛应用。

## 📄 摘要（原文）

> The advent of Deep Research agents has substantially reduced the time required for conducting extensive research tasks. However, these tasks inherently demand rigorous standards of factual accuracy and comprehensiveness, necessitating thorough evaluation before widespread adoption. In this paper, we propose ReportBench, a systematic benchmark designed to evaluate the content quality of research reports generated by large language models (LLMs). Our evaluation focuses on two critical dimensions: (1) the quality and relevance of cited literature, and (2) the faithfulness and veracity of the statements within the generated reports. ReportBench leverages high-quality published survey papers available on arXiv as gold-standard references, from which we apply reverse prompt engineering to derive domain-specific prompts and establish a comprehensive evaluation corpus. Furthermore, we develop an agent-based automated framework within ReportBench that systematically analyzes generated reports by extracting citations and statements, checking the faithfulness of cited content against original sources, and validating non-cited claims using web-based resources. Empirical evaluations demonstrate that commercial Deep Research agents such as those developed by OpenAI and Google consistently generate more comprehensive and reliable reports than standalone LLMs augmented with search or browsing tools. However, there remains substantial room for improvement in terms of the breadth and depth of research coverage, as well as factual consistency. The complete code and data will be released at the following link: https://github.com/ByteDance-BandAI/ReportBench

