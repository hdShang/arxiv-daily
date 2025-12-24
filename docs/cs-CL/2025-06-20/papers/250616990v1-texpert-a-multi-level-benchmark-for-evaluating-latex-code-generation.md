---
layout: default
title: "TeXpert: A Multi-Level Benchmark for Evaluating LaTeX Code Generation by LLMs"
---

# TeXpert: A Multi-Level Benchmark for Evaluating LaTeX Code Generation by LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16990" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16990v1</a>
  <a href="https://arxiv.org/pdf/2506.16990.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16990v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16990v1', 'TeXpert: A Multi-Level Benchmark for Evaluating LaTeX Code Generation by LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sahil Kale, Vijaykant Nadadur

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-20

**备注**: Accepted to the SDProc Workshop @ ACL 2025

**期刊**: Proceedings of the Fifth Workshop on Scholarly Document Processing (SDP 2025), pages 7-16, 2025

**DOI**: [10.18653/v1/2025.sdp-1.2](https://doi.org/10.18653/v1/2025.sdp-1.2)

**🔗 代码/项目**: [GITHUB](https://github.com/knowledge-verse-ai/TeXpert)

---

## 💡 一句话要点

**提出TeXpert基准以评估LLMs在LaTeX代码生成中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LaTeX生成` `大型语言模型` `基准评估` `开源模型` `科学文档`

## 📋 核心要点

1. 现有的评估基准未能有效衡量LLMs在LaTeX代码生成中的能力，导致研究缺乏针对性。
2. 论文提出了TeXpert基准数据集，包含多层次的自然语言提示，专注于科学文档的LaTeX代码生成。
3. 实验结果表明，LLMs在LaTeX生成任务中的表现与标准基准相悖，且开源模型表现出色。

## 📝 摘要（中文）

LaTeX因其在排版上的精确性和灵活性，成为科学文档准备的黄金标准。大型语言模型（LLMs）为研究人员提供了使用自然语言指令生成出版物所需材料的机会，但现有基准完全缺乏对这一能力的评估。通过引入TeXpert，我们构建了一个包含自然语言提示的基准数据集，专注于科学文档各个组成部分的LaTeX代码生成，并对LLMs在此方面的表现进行了深入分析，识别出常见的错误类型。我们的评估显示，尽管LLMs在标准基准上表现优异，但在LaTeX生成任务中准确率显著下降；开源模型如DeepSeek v3和DeepSeek Coder在LaTeX任务中与闭源模型竞争力强；格式和包错误意外普遍，表明大多数LLMs的训练数据集中缺乏多样化的LaTeX示例。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有方法在评估LLMs生成LaTeX代码能力方面的不足，现有基准无法反映LLMs在复杂任务中的表现。

**核心思路**：通过构建TeXpert基准数据集，提供多层次的自然语言提示，针对科学文档的不同组成部分进行LaTeX代码生成的评估，以此来分析LLMs的性能和常见错误。

**技术框架**：整体架构包括数据集构建、LLMs性能评估和错误类型分析三个主要模块。数据集涵盖不同难度的任务，评估过程则通过对比开源和闭源模型的表现来进行。

**关键创新**：TeXpert基准的提出是本研究的核心创新，填补了LLMs在LaTeX生成能力评估方面的空白，与现有方法相比，提供了更具针对性的评估标准。

**关键设计**：在数据集构建中，设计了多层次的自然语言提示，并在评估中关注格式和包错误等细节，确保评估的全面性和准确性。通过这些设计，能够更好地反映LLMs在实际应用中的表现。

## 📊 实验亮点

实验结果显示，LLMs在LaTeX生成任务中的准确率显著下降，尤其在任务复杂度增加时，表现与标准基准相悖。开源模型如DeepSeek v3和DeepSeek Coder在LaTeX任务中表现出色，显示出与闭源模型的竞争力。此外，格式和包错误的普遍性提示了训练数据集的多样性不足。

## 🎯 应用场景

该研究的潜在应用领域包括学术出版、教育和科研文档自动化生成等。通过提高LLMs在LaTeX代码生成中的准确性，可以极大地提升科研人员的工作效率，降低文档准备的门槛，推动科学交流的便利性与效率。未来，TeXpert基准可能成为评估LLMs在文档生成任务中的标准工具。

## 📄 摘要（原文）

> LaTeX's precision and flexibility in typesetting have made it the gold standard for the preparation of scientific documentation. Large Language Models (LLMs) present a promising opportunity for researchers to produce publication-ready material using LaTeX with natural language instructions, yet current benchmarks completely lack evaluation of this ability. By introducing TeXpert, our benchmark dataset with natural language prompts for generating LaTeX code focused on components of scientific documents across multiple difficulty levels, we conduct an in-depth analysis of LLM performance in this regard and identify frequent error types. Our evaluation across open and closed-source LLMs highlights multiple key findings: LLMs excelling on standard benchmarks perform poorly in LaTeX generation with a significant accuracy drop-off as the complexity of tasks increases; open-source models like DeepSeek v3 and DeepSeek Coder strongly rival closed-source counterparts in LaTeX tasks; and formatting and package errors are unexpectedly prevalent, suggesting a lack of diverse LaTeX examples in the training datasets of most LLMs. Our dataset, code, and model evaluations are available at https://github.com/knowledge-verse-ai/TeXpert.

