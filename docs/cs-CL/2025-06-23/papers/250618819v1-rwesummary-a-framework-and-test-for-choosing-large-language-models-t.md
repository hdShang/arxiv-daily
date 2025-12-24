---
layout: default
title: "RWESummary: A Framework and Test for Choosing Large Language Models to Summarize Real-World Evidence (RWE) Studies"
---

# RWESummary: A Framework and Test for Choosing Large Language Models to Summarize Real-World Evidence (RWE) Studies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18819" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18819v1</a>
  <a href="https://arxiv.org/pdf/2506.18819.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18819v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18819v1', 'RWESummary: A Framework and Test for Choosing Large Language Models to Summarize Real-World Evidence (RWE) Studies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arjun Mukerji, Michael L. Jackson, Jason Jones, Neil Sanghavi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-23

**备注**: 24 pages, 2 figures

---

## 💡 一句话要点

**提出RWESummary框架以评估大语言模型在RWE研究总结中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `真实世界证据` `医学研究` `模型评估` `基准测试` `RWESummary` `数据分析`

## 📋 核心要点

1. 现有方法未能有效评估大语言模型在总结真实世界证据研究中的表现，存在明显的研究空白。
2. RWESummary框架通过引入特定场景和评估标准，旨在填补这一空白，并提供对LLMs的系统性评估。
3. 实验结果显示，Gemini 2.5模型在13个RWE研究中表现最佳，提供了有效的基准参考。

## 📝 摘要（中文）

大语言模型（LLMs）在一般摘要任务和医学研究辅助方面得到了广泛评估，但尚未专门针对从RWE研究结构化输出中总结真实世界证据（RWE）的任务进行评估。我们提出了RWESummary，作为MedHELM框架的补充，以便对LLMs在此任务中的表现进行基准测试。RWESummary包括一个场景和三个评估，涵盖了医学研究摘要中观察到的主要错误类型，并使用Atropos Health专有数据开发。此外，我们利用RWESummary比较了不同LLMs在内部RWE摘要工具中的表现。根据13个不同的RWE研究，发现Gemini 2.5模型在整体表现上最佳（包括Flash和Pro）。我们建议RWESummary作为真实世界证据研究摘要的一个新颖且有用的基础模型基准。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何有效评估大语言模型在总结真实世界证据（RWE）研究中的表现。现有方法缺乏针对RWE研究结构化输出的专门评估，导致无法准确判断模型的有效性和适用性。

**核心思路**：RWESummary框架的核心思路是通过设计特定的评估场景和标准，系统性地比较不同大语言模型在RWE摘要任务中的表现。这种设计旨在提供一个可靠的基准，以便研究人员能够选择最合适的模型。

**技术框架**：RWESummary框架包括一个具体的应用场景和三个主要评估模块，分别针对医学研究摘要中常见的错误类型进行分析。整体流程涵盖数据收集、模型评估和结果分析等阶段。

**关键创新**：RWESummary的主要创新在于其专门针对RWE研究的评估机制，填补了现有文献中的空白。这一框架不仅提供了标准化的评估方法，还为后续研究提供了可重复的基准。

**关键设计**：在RWESummary中，关键设计包括对错误类型的分类、评估指标的设定以及模型性能的比较方法。这些设计确保了评估的全面性和准确性。具体的参数设置和损失函数等技术细节在论文中进行了详细描述。

## 📊 实验亮点

在实验中，RWESummary框架对13个不同的RWE研究进行了评估，结果显示Gemini 2.5模型在整体表现上优于其他模型，包括Flash和Pro版本。这一发现为选择合适的语言模型提供了实证依据，具有重要的参考价值。

## 🎯 应用场景

RWESummary框架具有广泛的应用潜力，特别是在医学研究和临床决策支持领域。通过提供对大语言模型在RWE研究总结中的系统评估，研究人员和临床医生可以更有效地选择适合的工具，从而提高研究成果的可用性和实用性。未来，该框架还可能扩展到其他领域的证据总结和分析。

## 📄 摘要（原文）

> Large Language Models (LLMs) have been extensively evaluated for general summarization tasks as well as medical research assistance, but they have not been specifically evaluated for the task of summarizing real-world evidence (RWE) from structured output of RWE studies. We introduce RWESummary, a proposed addition to the MedHELM framework (Bedi, Cui, Fuentes, Unell et al., 2025) to enable benchmarking of LLMs for this task. RWESummary includes one scenario and three evaluations covering major types of errors observed in summarization of medical research studies and was developed using Atropos Health proprietary data. Additionally, we use RWESummary to compare the performance of different LLMs in our internal RWE summarization tool. At the time of publication, with 13 distinct RWE studies, we found the Gemini 2.5 models performed best overall (both Flash and Pro). We suggest RWESummary as a novel and useful foundation model benchmark for real-world evidence study summarization.

