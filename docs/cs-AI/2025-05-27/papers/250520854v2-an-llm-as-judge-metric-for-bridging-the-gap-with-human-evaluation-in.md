---
layout: default
title: An LLM-as-Judge Metric for Bridging the Gap with Human Evaluation in SE Tasks
---

# An LLM-as-Judge Metric for Bridging the Gap with Human Evaluation in SE Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20854" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20854v2</a>
  <a href="https://arxiv.org/pdf/2505.20854.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20854v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20854v2', 'An LLM-as-Judge Metric for Bridging the Gap with Human Evaluation in SE Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Zhou, Kisub Kim, Ting Zhang, Martin Weyssow, Luis F. Gomes, Guang Yang, Kui Liu, Xin Xia, David Lo

**分类**: cs.SE, cs.AI, cs.CL

**发布日期**: 2025-05-27 (更新: 2025-10-10)

**备注**: 13 pages

---

## 💡 一句话要点

**提出SE-Jury以解决软件工程任务中生成软件工件评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `软件工程` `自动评估` `集成评估` `代码生成` `程序修复` `代码摘要`

## 📋 核心要点

1. 现有的自动评估指标无法准确反映生成软件工件的正确性，且人类评估劳动密集且难以扩展。
2. 论文提出SE-Jury，通过定义五种独立评估策略和动态团队选择机制，准确评估生成软件工件的正确性。
3. 实验结果显示，SE-Jury在与人类评估一致性方面显著提升，尤其在代码生成和程序修复任务中表现突出。

## 📝 摘要（中文）

随着大型语言模型（LLMs）和其他自动化技术在软件开发中的应用日益增加，生成软件工件（如代码片段、补丁和注释）的正确性评估仍然是一个重大挑战。人类评估虽然准确，但劳动密集且缺乏可扩展性；而许多自动评估指标虽然可扩展且人力需求少，但往往无法准确反映生成工件的实际正确性。本文提出了SE-Jury，这是首个专门设计用于准确评估生成软件工件正确性的LLM作为集成评估者的评估指标。SE-Jury定义了五种独立评估策略，并通过动态团队选择机制确定最合适的评估者子集，最终通过集成产生正确性评分。实验结果表明，SE-Jury与人类判断的一致性显著提高，提升幅度在29.6%到140.8%之间，显示出其作为人类评估可扩展且可靠的替代方案的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决生成软件工件（如代码片段、补丁和注释）评估中的准确性问题。现有方法在自动评估时常常无法反映真实的正确性，而人类评估则面临可扩展性不足的挑战。

**核心思路**：SE-Jury的核心思路是通过集成多个独立评估者的判断，利用动态选择机制来确定最合适的评估者组合，从而提高评估的准确性和可靠性。

**技术框架**：SE-Jury的整体架构包括五种独立的评估策略，每种策略由一个独立的评估者实现。通过动态团队选择机制，系统能够根据任务需求选择最合适的评估者组合，最终生成一个综合的正确性评分。

**关键创新**：SE-Jury的主要创新在于将多个评估者的判断进行集成，克服了单一评估者可能带来的偏差。这种集成方法与现有的单一自动评估指标形成了鲜明对比。

**关键设计**：在设计中，SE-Jury采用了动态选择机制，以确保在不同的任务中选择最优的评估者组合。此外，评估策略的多样性和独立性也是其设计的关键要素，确保了评估结果的全面性和准确性。

## 📊 实验亮点

实验结果表明，SE-Jury在与人类评估的一致性方面显著提高，提升幅度在29.6%到140.8%之间。特别是在代码生成和程序修复任务中，SE-Jury的评估结果与人类标注者的协议水平接近，显示出其作为人类评估的可扩展替代方案的有效性。

## 🎯 应用场景

SE-Jury的研究成果在软件工程领域具有广泛的应用潜力，尤其是在代码生成、自动程序修复和代码摘要等任务中。其可扩展性和高准确性使其成为开发者在评估自动生成工件时的可靠工具，未来可能推动软件开发流程的自动化和智能化。

## 📄 摘要（原文）

> Large Language Models (LLMs) and other automated techniques have been increasingly used to support software developers by generating software artifacts such as code snippets, patches, and comments. However, accurately assessing the correctness of these generated artifacts remains a significant challenge. On one hand, human evaluation provides high accuracy but is labor-intensive and lacks scalability. On the other hand, many automatic evaluation metrics are scalable and require minimal human effort, but they often fail to accurately reflect the actual correctness of generated software artifacts.
>   In this paper, we present SE-Jury, the first evaluation metric for LLM-as-Ensemble-Judge specifically designed to accurately assess the correctness of generated software artifacts. SE-Jury first defines five distinct evaluation strategies, each implemented by an independent judge. A dynamic team selection mechanism then identifies the most appropriate subset of judges as a team to produce a final correctness score through ensembling. We evaluate SE-Jury across a diverse set of software engineering (SE) benchmarks that span three popular SE tasks: code generation, automated program repair, and code summarization. Results demonstrate that SE-Jury consistently achieves a higher correlation with human judgments, with improvements ranging from 29.6% to 140.8% over existing automatic metrics. SE-Jury reaches agreement levels with human annotators that are close to inter-annotator agreement in code generation and program repair. These findings underscore SE-Jury's potential as a scalable and reliable alternative to human evaluation in these SE tasks.

