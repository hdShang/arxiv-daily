---
layout: default
title: Fine-Tune an SLM or Prompt an LLM? The Case of Generating Low-Code Workflows
---

# Fine-Tune an SLM or Prompt an LLM? The Case of Generating Low-Code Workflows

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24189" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24189v2</a>
  <a href="https://arxiv.org/pdf/2505.24189.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24189v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24189v2', 'Fine-Tune an SLM or Prompt an LLM? The Case of Generating Low-Code Workflows')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Orlando Marquez Ayala, Patrice Bechard, Emily Chen, Maggie Baird, Jingfei Chen

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-30 (更新: 2025-07-16)

**备注**: 8 pages, 7 figures. Accepted to Workshop on Structured Knowledge for Large Language Models (SKnowLLM) at KDD 2025

---

## 💡 一句话要点

**比较SLM微调与LLM提示在低代码工作流生成中的效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `小型语言模型` `大型语言模型` `低代码工作流` `微调` `提示学习` `结构化输出` `错误分析`

## 📋 核心要点

1. 现有方法在生成结构化输出时，LLMs的提示效果与SLMs的微调效果尚不明确，尤其是在特定领域任务中。
2. 论文提出通过比较微调SLMs与提示LLMs来生成低代码工作流，探讨两者在质量和效率上的差异。
3. 实验结果表明，微调SLMs在生成质量上平均提升10%，同时进行的错误分析揭示了模型的局限性。

## 📝 摘要（中文）

大型语言模型（LLMs）如GPT-4o能够通过合适的提示处理多种复杂任务。随着每个token成本的降低，微调小型语言模型（SLMs）在实际应用中的优势可能不再明显。本文提供证据表明，对于需要结构化输出的领域特定任务，SLMs仍具有质量优势。我们比较了在生成JSON格式的低代码工作流任务中微调SLM与提示LLM的效果。结果显示，尽管良好的提示可以产生合理结果，但微调平均提高了10%的质量。此外，我们还进行了系统的错误分析，以揭示模型的局限性。

## 🔬 方法详解

**问题定义**：本文旨在解决在生成低代码工作流时，如何选择SLM微调与LLM提示的最佳策略。现有方法在特定领域任务中可能存在质量不足的问题。

**核心思路**：通过比较微调SLMs与提示LLMs的效果，探讨在生成结构化输出时，SLMs是否仍具有质量优势。设计上，强调微调SLMs在特定任务中的适应性和准确性。

**技术框架**：整体架构包括数据准备、模型训练与微调、提示设计、结果生成与评估。主要模块包括SLM微调模块和LLM提示模块，分别用于生成低代码工作流。

**关键创新**：本研究的创新点在于系统性地比较了SLMs与LLMs在特定任务中的表现，发现微调SLMs在质量上具有明显优势，尤其是在结构化输出方面。

**关键设计**：在微调过程中，采用了特定的损失函数和参数设置，以优化SLMs在生成任务中的表现。网络结构设计上，针对低代码工作流的特点进行了调整，以提高生成质量。

## 📊 实验亮点

实验结果显示，微调SLMs在生成低代码工作流的质量上平均提高了10%，相较于提示LLMs的效果，展现出更高的准确性和可靠性。此外，系统的错误分析揭示了模型在特定任务中的局限性，为后续研究提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、自动化工作流生成和智能助手等。通过优化低代码工作流的生成过程，可以提高开发效率，降低人力成本，推动智能化应用的发展。未来，随着技术的进步，SLMs在更多领域的应用前景将更加广阔。

## 📄 摘要（原文）

> Large Language Models (LLMs) such as GPT-4o can handle a wide range of complex tasks with the right prompt. As per token costs are reduced, the advantages of fine-tuning Small Language Models (SLMs) for real-world applications -- faster inference, lower costs -- may no longer be clear. In this work, we present evidence that, for domain-specific tasks that require structured outputs, SLMs still have a quality advantage. We compare fine-tuning an SLM against prompting LLMs on the task of generating low-code workflows in JSON form. We observe that while a good prompt can yield reasonable results, fine-tuning improves quality by 10% on average. We also perform systematic error analysis to reveal model limitations.

