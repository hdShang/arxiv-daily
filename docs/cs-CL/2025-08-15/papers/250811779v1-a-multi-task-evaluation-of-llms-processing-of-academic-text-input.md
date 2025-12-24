---
layout: default
title: "A Multi-Task Evaluation of LLMs' Processing of Academic Text Input"
---

# A Multi-Task Evaluation of LLMs' Processing of Academic Text Input

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11779" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11779v1</a>
  <a href="https://arxiv.org/pdf/2508.11779.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11779v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11779v1', 'A Multi-Task Evaluation of LLMs\' Processing of Academic Text Input')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyi Li, Yu Qin, Olivia R. Liu Sheng

**分类**: cs.CL, econ.GN

**发布日期**: 2025-08-15

---

## 💡 一句话要点

**评估大型语言模型在学术文本处理中的多任务能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `学术文本处理` `同行评审` `多任务评估` `信息系统`

## 📋 核心要点

1. 当前对LLMs在学术文本处理中的有效性存在争议，尤其是在同行评审中的应用潜力尚未得到充分验证。
2. 本文提出了一种将计算机科学研究任务整合为工作流程的方法，以系统性评估LLMs在学术文本处理中的表现。
3. 实验结果表明，尽管LLMs在某些任务上表现尚可，但在文本评分和反思方面的能力有限，整体性能不佳。

## 📝 摘要（中文）

关于大型语言模型（LLMs）在科学发现中的作用，尤其是在学术同行评审中的辅助能力，存在激烈的争论。本文通过将计算机科学研究中的个别任务整合为一个有指导性的工作流程，评估LLMs对学术文本输入的处理能力。我们设计了四个评估任务，分别考察LLMs在内容再现、比较、评分和反思中的表现。通过对三本顶级期刊的高质量信息系统文章进行评估，结果显示，谷歌的Gemini在学术文本的总结和改写方面表现尚可，但在文本排名和评分中存在明显不足，且其对文本的定性反思缺乏深度。整体上，我们不建议在同行评审中不加限制地使用LLMs。

## 🔬 方法详解

**问题定义**：本文旨在评估大型语言模型在处理学术文本时的能力，尤其是其在同行评审中的应用潜力。现有方法缺乏系统性评估，导致对LLMs的能力存在误解。

**核心思路**：通过将计算机科学研究中的任务整合为一个有指导性的工作流程，本文系统性地评估LLMs在不同学术任务中的表现，确保评估的全面性和准确性。

**技术框架**：研究采用四个评估任务：内容再现、比较、评分和反思，分别对应LLMs的不同角色（如知识仲裁者、合作伙伴等）。通过对三本顶级期刊的文章进行输入，结合多种文本指标进行评估。

**关键创新**：本文的创新在于系统性地将多种学术任务整合为一个评估框架，提供了对LLMs能力的全面分析，尤其是在学术文本处理中的应用。

**关键设计**：在实验中，使用了高质量的学术文章作为输入文本，并设计了详细的提示以指导LLMs的任务执行。评估过程中采用了多种文本度量标准，包括语言评估、与真实情况的比较以及人类评估，以确保结果的可靠性。

## 📊 实验亮点

实验结果显示，谷歌的Gemini在学术文本的总结和改写方面表现尚可，然而在文本排名的可扩展性和评分的区分能力上存在明显不足。整体评估结果表明，LLMs在学术文本处理中的能力并不如预期，尤其在定性反思方面缺乏深度和启发性。

## 🎯 应用场景

该研究的潜在应用领域包括学术评审、科研辅助工具的开发以及教育领域的智能辅导系统。通过对LLMs能力的深入评估，研究为未来在学术界的应用提供了重要参考，促进了对LLMs在科学研究中角色的理解与规范。

## 📄 摘要（原文）

> How much large language models (LLMs) can aid scientific discovery, notably in assisting academic peer review, is in heated debate. Between a literature digest and a human-comparable research assistant lies their practical application potential. We organize individual tasks that computer science studies employ in separate terms into a guided and robust workflow to evaluate LLMs' processing of academic text input. We employ four tasks in the assessment: content reproduction/comparison/scoring/reflection, each demanding a specific role of the LLM (oracle/judgmental arbiter/knowledgeable arbiter/collaborator) in assisting scholarly works, and altogether testing LLMs with questions that increasingly require intellectual capabilities towards a solid understanding of scientific texts to yield desirable solutions. We exemplify a rigorous performance evaluation with detailed instructions on the prompts. Adopting first-rate Information Systems articles at three top journals as the input texts and an abundant set of text metrics, we record a compromised performance of the leading LLM - Google's Gemini: its summary and paraphrase of academic text is acceptably reliable; using it to rank texts through pairwise text comparison is faintly scalable; asking it to grade academic texts is prone to poor discrimination; its qualitative reflection on the text is self-consistent yet hardly insightful to inspire meaningful research. This evidence against an endorsement of LLMs' text-processing capabilities is consistent across metric-based internal (linguistic assessment), external (comparing to the ground truth), and human evaluation, and is robust to the variations of the prompt. Overall, we do not recommend an unchecked use of LLMs in constructing peer reviews.

