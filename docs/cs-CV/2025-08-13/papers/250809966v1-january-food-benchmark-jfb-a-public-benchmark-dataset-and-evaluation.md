---
layout: default
title: "January Food Benchmark (JFB): A Public Benchmark Dataset and Evaluation Suite for Multimodal Food Analysis"
---

# January Food Benchmark (JFB): A Public Benchmark Dataset and Evaluation Suite for Multimodal Food Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09966" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09966v1</a>
  <a href="https://arxiv.org/pdf/2508.09966.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09966v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09966v1', 'January Food Benchmark (JFB): A Public Benchmark Dataset and Evaluation Suite for Multimodal Food Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Amir Hosseinian, Ashkan Dehghani Zahedani, Umer Mansoor, Noosheen Hashemi, Mark Woodward

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出January Food Benchmark以解决营养分析标准化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `食品分析` `营养评估` `多模态学习` `基准数据集` `视觉-语言模型`

## 📋 核心要点

1. 现有的自动营养分析方法缺乏标准化的评估方法和高质量的数据集，限制了研究的进展。
2. 本文提出了January Food Benchmark (JFB)数据集及全面的评估框架，以提供高质量的评估标准和模型性能评估。
3. 实验结果显示，专门模型january/food-vision-v1的整体得分为86.2，较最佳通用模型提升了12.1分，验证了方法的有效性。

## 📝 摘要（中文）

随着人工智能在自动营养分析领域的进展，缺乏标准化的评估方法和高质量的真实基准数据集严重制约了这一领域的发展。为此，本文提出了三个主要贡献。首先，推出了January Food Benchmark (JFB)，这是一个包含1000张经过人工验证注释的食品图像的公开数据集。其次，详细描述了一个全面的基准评估框架，包括稳健的评估指标和一种新颖的、面向应用的整体评分，旨在全面评估模型性能。最后，提供了通用视觉-语言模型和我们专门模型january/food-vision-v1的基线结果。评估结果表明，专门模型的整体得分为86.2，比表现最佳的通用配置提高了12.1分。这项工作为研究社区提供了一个有价值的新评估数据集和严格的框架，以指导和基准未来的自动营养分析发展。

## 🔬 方法详解

**问题定义**：本文旨在解决自动营养分析领域中缺乏标准化评估方法和高质量数据集的问题。现有方法往往依赖于有限的数据和不一致的评估标准，导致结果的可比性差。

**核心思路**：论文的核心思路是构建一个公开的食品图像数据集（JFB）和一个全面的评估框架，以提供一致的评估标准和高质量的基准数据，从而推动自动营养分析的研究进展。

**技术框架**：整体架构包括数据集构建、评估指标设计和模型性能评估三个主要模块。数据集包含1000张食品图像，评估指标包括稳健的性能指标和整体评分。

**关键创新**：最重要的技术创新点在于提出了一个应用导向的整体评分方法，能够全面评估模型性能，而不仅仅依赖于单一指标。这与现有方法的评估方式有本质区别。

**关键设计**：在模型评估中，采用了多种稳健的评估指标，并通过与通用视觉-语言模型的对比，验证了专门模型的优越性。

## 📊 实验亮点

实验结果显示，专门模型january/food-vision-v1在整体评分上达到了86.2，相较于最佳通用模型提升了12.1分，表明该模型在食品图像分析中的显著优势，为未来的研究提供了强有力的基准。

## 🎯 应用场景

该研究的潜在应用领域包括食品营养分析、健康管理和智能饮食推荐等。通过提供高质量的数据集和评估框架，研究者和开发者可以更有效地开发和优化自动营养分析系统，推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> Progress in AI for automated nutritional analysis is critically hampered by the lack of standardized evaluation methodologies and high-quality, real-world benchmark datasets. To address this, we introduce three primary contributions. First, we present the January Food Benchmark (JFB), a publicly available collection of 1,000 food images with human-validated annotations. Second, we detail a comprehensive benchmarking framework, including robust metrics and a novel, application-oriented overall score designed to assess model performance holistically. Third, we provide baseline results from both general-purpose Vision-Language Models (VLMs) and our own specialized model, january/food-vision-v1. Our evaluation demonstrates that the specialized model achieves an Overall Score of 86.2, a 12.1-point improvement over the best-performing general-purpose configuration. This work offers the research community a valuable new evaluation dataset and a rigorous framework to guide and benchmark future developments in automated nutritional analysis.

