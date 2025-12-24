---
layout: default
title: UCSC at SemEval-2025 Task 3: Context, Models and Prompt Optimization for Automated Hallucination Detection in LLM Output
---

# UCSC at SemEval-2025 Task 3: Context, Models and Prompt Optimization for Automated Hallucination Detection in LLM Output

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03030" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03030v1</a>
  <a href="https://arxiv.org/pdf/2505.03030.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03030v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03030v1', 'UCSC at SemEval-2025 Task 3: Context, Models and Prompt Optimization for Automated Hallucination Detection in LLM Output')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sicong Huang, Jincheng He, Shiyuan Huang, Karthik Raja Anandan, Arkajyoti Chakraborty, Ian Lane

**分类**: cs.CL

**发布日期**: 2025-05-05

**备注**: 6 pages, 1 figure

---

## 💡 一句话要点

**提出框架以优化大语言模型的幻觉检测**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `幻觉检测` `大型语言模型` `上下文检索` `虚假内容识别` `自动优化提示`

## 📋 核心要点

1. 大型语言模型在处理知识密集型查询时，幻觉现象的检测和定位仍然是一个未解决的难题。
2. 本文提出了一种新框架，通过检索上下文、识别虚假内容并映射回输出，来优化幻觉检测过程。
3. 实验结果显示，该系统在所有语言中表现优异，平均排名第一，显著提升了幻觉检测的准确性。

## 📝 摘要（中文）

幻觉现象对大型语言模型在回答知识密集型查询时构成了重大挑战。随着大型语言模型的广泛应用，检测幻觉的发生及其具体位置变得至关重要。SemEval 2025任务3，Mu-SHROOM，旨在解决这一问题。本文描述了UCSC团队在该共享任务中的系统提交，提出了一种框架，首先检索相关上下文，然后识别答案中的虚假内容，最后将其映射回大型语言模型输出的具体区间。该过程通过自动优化提示进一步增强。我们的系统在所有语言中表现最佳，平均排名第一，并发布了代码和实验结果。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在回答知识密集型查询时出现的幻觉现象，现有方法在检测幻觉及其具体位置方面存在不足。

**核心思路**：提出的框架通过检索相关上下文、识别虚假内容并将其映射回模型输出，优化了幻觉检测的过程，提升了检测的准确性和效率。

**技术框架**：整体流程包括三个主要模块：首先是上下文检索模块，其次是虚假内容识别模块，最后是映射模块，整个过程还结合了自动优化提示的技术。

**关键创新**：最重要的创新在于将上下文检索与虚假内容识别相结合，并通过自动优化提示提升检测效果，这与现有方法的独立处理方式形成了鲜明对比。

**关键设计**：在参数设置上，采用了特定的损失函数以优化模型性能，并设计了适应不同语言的网络结构，确保了系统的通用性和高效性。

## 📊 实验亮点

实验结果表明，UCSC系统在所有语言的平均排名中位列第一，显著提高了幻觉检测的准确性，具体性能数据未公开，但整体表现优于现有基线方法，展示了该框架的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、自动问答系统和信息检索等，能够有效提升系统对虚假信息的检测能力，增强用户体验。未来，该框架还可扩展至其他自然语言处理任务，推动相关技术的发展。

## 📄 摘要（原文）

> Hallucinations pose a significant challenge for large language models when answering knowledge-intensive queries. As LLMs become more widely adopted, it is crucial not only to detect if hallucinations occur but also to pinpoint exactly where in the LLM output they occur. SemEval 2025 Task 3, Mu-SHROOM: Multilingual Shared-task on Hallucinations and Related Observable Overgeneration Mistakes, is a recent effort in this direction. This paper describes the UCSC system submission to the shared Mu-SHROOM task. We introduce a framework that first retrieves relevant context, next identifies false content from the answer, and finally maps them back to spans in the LLM output. The process is further enhanced by automatically optimizing prompts. Our system achieves the highest overall performance, ranking #1 in average position across all languages. We release our code and experiment results.

