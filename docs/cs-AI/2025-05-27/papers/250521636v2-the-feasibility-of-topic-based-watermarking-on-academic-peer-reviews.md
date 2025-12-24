---
layout: default
title: The Feasibility of Topic-Based Watermarking on Academic Peer Reviews
---

# The Feasibility of Topic-Based Watermarking on Academic Peer Reviews

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21636" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21636v2</a>
  <a href="https://arxiv.org/pdf/2505.21636.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21636v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21636v2', 'The Feasibility of Topic-Based Watermarking on Academic Peer Reviews')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexander Nemecek, Yuzhou Jiang, Erman Ayday

**分类**: cs.CR, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-11-11)

**备注**: Accepted at AACL 25 Findings

---

## 💡 一句话要点

**提出基于主题的水印技术以解决学术同行评审中的归属问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `同行评审` `水印技术` `文本生成` `学术诚信`

## 📋 核心要点

1. 现有方法在同行评审中使用LLMs面临机密性泄露和评估不一致等挑战，限制了其应用。
2. 论文提出基于主题的水印（TBW）技术，通过嵌入可检测信号来解决LLM生成文本的归属问题。
3. 实验结果显示，TBW在保持评审质量的同时，具备强大的检测能力，能够有效应对文本改写。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在学术工作流程中的广泛应用，许多会议和期刊允许其用于语言润色和文献总结等任务。然而，由于对机密性泄露、虚构内容和评估不一致的担忧，LLMs在同行评审中的使用仍然受到禁止。随着LLM生成的文本与人类写作愈加难以区分，迫切需要可靠的归属机制以维护评审过程的完整性。本研究评估了一种语义感知的技术——基于主题的水印（TBW），旨在将可检测信号嵌入LLM生成的文本中。我们对多种LLM配置进行了系统评估，包括基础、少量示例和微调变体，使用来自学术会议的真实同行评审数据。结果表明，TBW在保持评审质量的同时，表现出在改写下的强大检测性能。这些发现突显了TBW作为一种最小干扰且实用的LLM归属解决方案在同行评审环境中的可行性。

## 🔬 方法详解

**问题定义**：本论文旨在解决在学术同行评审中使用LLMs所带来的归属问题，现有方法面临机密性泄露和评估不一致的挑战，限制了LLMs的应用。

**核心思路**：论文提出了一种基于主题的水印（TBW）技术，旨在将可检测信号嵌入LLM生成的文本中，以确保文本的归属性和可追溯性。通过这种方式，TBW能够在不显著影响文本质量的情况下，提供可靠的归属机制。

**技术框架**：整体架构包括三个主要模块：首先是LLM生成文本的基础模块，其次是水印嵌入模块，最后是水印检测模块。该流程确保了生成文本的质量和水印的有效性。

**关键创新**：TBW的主要创新在于其语义感知能力，能够在保持文本自然流畅的同时，嵌入可检测的水印信号。这与传统的水印技术不同，后者往往会显著影响文本的可读性和质量。

**关键设计**：在技术细节上，TBW采用了特定的参数设置和损失函数，以优化水印的嵌入效果。同时，网络结构经过微调，以确保在不同LLM配置下均能实现良好的性能。实验中使用了真实的同行评审数据，以验证方法的有效性。

## 📊 实验亮点

实验结果表明，TBW在保持评审质量方面与未加水印的输出相当，同时在文本改写情况下展现出强大的检测性能。这一技术的有效性为LLM在同行评审中的应用提供了新的可能性，显示出其在实际场景中的可行性。

## 🎯 应用场景

该研究的潜在应用领域包括学术出版、同行评审和文本生成等场景。通过提供一种有效的归属机制，TBW能够帮助维护学术诚信，防止抄袭和不当使用LLMs生成的内容。未来，TBW可能在其他需要文本归属的领域中发挥重要作用。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly integrated into academic workflows, with many conferences and journals permitting their use for tasks such as language refinement and literature summarization. However, their use in peer review remains prohibited due to concerns around confidentiality breaches, hallucinated content, and inconsistent evaluations. As LLM-generated text becomes more indistinguishable from human writing, there is a growing need for reliable attribution mechanisms to preserve the integrity of the review process. In this work, we evaluate topic-based watermarking (TBW), a semantic-aware technique designed to embed detectable signals into LLM-generated text. We conduct a systematic assessment across multiple LLM configurations, including base, few-shot, and fine-tuned variants, using authentic peer review data from academic conferences. Our results show that TBW maintains review quality relative to non-watermarked outputs, while demonstrating robust detection performance under paraphrasing. These findings highlight the viability of TBW as a minimally intrusive and practical solution for LLM attribution in peer review settings.

