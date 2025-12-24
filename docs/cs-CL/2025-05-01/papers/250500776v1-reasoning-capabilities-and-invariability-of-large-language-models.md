---
layout: default
title: Reasoning Capabilities and Invariability of Large Language Models
---

# Reasoning Capabilities and Invariability of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00776" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00776v1</a>
  <a href="https://arxiv.org/pdf/2505.00776.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00776v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00776v1', 'Reasoning Capabilities and Invariability of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alessandro Raganato, Rafael Peñaloza, Marco Viviani, Gabriella Pasi

**分类**: cs.CL

**发布日期**: 2025-05-01

**备注**: Accepted for publication in the Proceedings of the 23rd IEEE/WIC International Conference on Web Intelligence and Intelligent Agent Technology (WI-IAT 2024)

---

## 💡 一句话要点

**提出新的基准数据集以评估大型语言模型的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `推理能力` `基准数据集` `逻辑推理` `提示依赖性` `认知心理学` `实验分析`

## 📋 核心要点

1. 现有大型语言模型在处理简单推理任务时表现不佳，尤其在提示依赖性方面存在显著挑战。
2. 本研究通过引入新的基准数据集，专注于简单的几何推理问题，以评估LLMs的推理能力。
3. 实验结果显示，尽管参数较大的模型在零-shot设置中表现较好，但仍有提升空间，链式推理提示的效果因使用时机而异。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言处理的多个应用中展现了显著的能力，但其处理简单推理任务的能力常受到质疑。本研究旨在全面分析LLMs的推理能力，特别关注其对提示的依赖性。我们引入了一个新的基准数据集，包含一系列要求浅层逻辑推理的简单推理问题，问题设计符合认知心理学标准，确保回答仅依赖于推理而非先前的直觉。通过对24个不同规模的LLMs进行零-shot和few-shot提示的实证分析，发现尽管参数超过700亿的模型在零-shot设置中表现更佳，但仍有很大的改进空间。此外，针对22个LLMs的链式推理提示测试表明，该提示的有效性取决于推理是在答案之前还是之后进行。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在简单推理任务中的能力不足，尤其是其对提示的依赖性问题。现有方法未能有效评估模型的推理能力，且缺乏标准化的测试数据集。

**核心思路**：论文提出了一个新的基准数据集，包含简单的几何推理问题，确保模型的回答仅依赖于逻辑推理，而非外部知识或直觉。通过这种方式，能够更准确地评估LLMs的推理能力。

**技术框架**：研究采用零-shot和few-shot提示方法，对24个不同规模的LLMs进行评估。实验分为两个主要阶段：首先是基于新数据集的推理能力测试，其次是链式推理提示的效果分析。

**关键创新**：最重要的创新在于引入了符合认知心理学标准的推理问题数据集，能够有效隔离模型的推理能力与其对外部知识的依赖。这一设计与现有方法的本质区别在于强调逻辑推理的独立性。

**关键设计**：在实验中，采用了不同的提示策略，包括零-shot和few-shot提示，链式推理提示的使用时机也进行了细致的设计，以评估其对模型性能的影响。

## 📊 实验亮点

实验结果表明，参数超过700亿的LLMs在零-shot设置中表现优于其他模型，但仍有显著的改进空间。链式推理提示的效果因使用时机不同而异，显示出在推理任务中提示设计的重要性。

## 🎯 应用场景

该研究的潜在应用场景包括教育、智能问答系统和自动化推理工具等领域。通过提升大型语言模型的推理能力，可以在更广泛的应用中实现更高的准确性和可靠性，推动自然语言处理技术的发展。未来，这一研究成果可能会影响模型设计和评估标准的制定。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown remarkable capabilities in manipulating natural language across multiple applications, but their ability to handle simple reasoning tasks is often questioned. In this work, we aim to provide a comprehensive analysis of LLMs' reasoning competence, specifically focusing on their prompt dependency. In particular, we introduce a new benchmark dataset with a series of simple reasoning questions demanding shallow logical reasoning. Aligned with cognitive psychology standards, the questions are confined to a basic domain revolving around geometric figures, ensuring that responses are independent of any pre-existing intuition about the world and rely solely on deduction. An empirical analysis involving zero-shot and few-shot prompting across 24 LLMs of different sizes reveals that, while LLMs with over 70 billion parameters perform better in the zero-shot setting, there is still a large room for improvement. An additional test with chain-of-thought prompting over 22 LLMs shows that this additional prompt can aid or damage the performance of models, depending on whether the rationale is required before or after the answer.

