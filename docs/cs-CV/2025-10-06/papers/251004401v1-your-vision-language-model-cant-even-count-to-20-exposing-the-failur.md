---
layout: default
title: Your Vision-Language Model Can't Even Count to 20: Exposing the Failures of VLMs in Compositional Counting
---

# Your Vision-Language Model Can't Even Count to 20: Exposing the Failures of VLMs in Compositional Counting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04401" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04401v1</a>
  <a href="https://arxiv.org/pdf/2510.04401.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04401v1" onclick="toggleFavorite(this, '2510.04401v1', 'Your Vision-Language Model Can\'t Even Count to 20: Exposing the Failures of VLMs in Compositional Counting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuyang Guo, Zekai Huang, Zhenmei Shi, Zhao Song, Jiahao Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-06

---

## 💡 一句话要点

**VLMCountBench揭示视觉语言模型在组合计数任务上的显著缺陷**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `计数能力` `组合计数` `基准测试` `VLMCountBench`

## 📋 核心要点

1. 现有视觉语言模型在复杂视觉推理任务中表现出色，但其基本计数能力仍有待考察。
2. 论文提出VLMCountBench基准，通过控制几何形状的颜色、大小等变量，专注评估VLMs的计数能力。
3. 实验表明，VLMs在单一形状计数上表现良好，但在组合形状计数上存在显著缺陷。

## 📝 摘要（中文）

视觉语言模型（VLMs）因其在网络规模视觉语言数据上训练获得的强大能力而备受关注。这些模型在图像理解、视频理解、复杂视觉推理和具身智能等多种任务中表现出色。然而，一个基本问题仍然存在：VLMs能否正确计数物体？本文提出了一个简单而有效的基准测试VLMCountBench，该基准在极简设置下，仅使用基本几何形状（如三角形、圆形）及其组合，专注于计数任务，避免其他因素的干扰。我们采用严格的自变量控制，并系统地研究了颜色、大小和提示优化等简单属性的影响。实验结果表明，当只存在一种形状时，VLMs可以可靠地计数，但当多种形状组合时（即组合计数），它们会表现出明显的失败。这突出了当前VLMs的一个基本经验限制，并为未来的研究指明了重要方向。

## 🔬 方法详解

**问题定义**：论文旨在评估现有视觉语言模型（VLMs）在组合计数任务中的能力。现有方法虽然在各种视觉语言任务中取得了进展，但其基本的计数能力，尤其是在涉及多种物体组合的场景下，尚未得到充分评估。现有的VQA数据集通常包含复杂的场景和问题，难以隔离和分析VLMs的计数能力。

**核心思路**：论文的核心思路是设计一个简单、可控的基准测试，即VLMCountBench，专注于评估VLMs在基本几何形状组合计数任务中的表现。通过控制形状的颜色、大小等属性，可以系统地研究这些因素对VLMs计数能力的影响。这种方法能够更清晰地揭示VLMs在计数方面的局限性。

**技术框架**：VLMCountBench基准测试包含一系列图像，图像中包含不同数量和类型的基本几何形状（如三角形、圆形）。测试过程包括向VLM提供图像和相应的计数问题，例如“图中共有多少个三角形和圆形？”。然后，评估VLM的回答是否正确。通过改变形状的颜色、大小和组合方式，可以系统地评估VLMs在不同条件下的计数能力。同时，论文还研究了提示工程对计数结果的影响。

**关键创新**：该论文的关键创新在于提出了VLMCountBench，这是一个专门用于评估VLMs计数能力的基准测试。与现有的VQA数据集相比，VLMCountBench更加简单、可控，能够更清晰地揭示VLMs在计数方面的局限性。此外，论文还系统地研究了颜色、大小和提示优化等因素对VLMs计数能力的影响，为未来的研究提供了有价值的见解。

**关键设计**：VLMCountBench的关键设计包括：1）使用基本几何形状（如三角形、圆形）作为计数对象，以简化场景；2）控制形状的颜色、大小和位置，以系统地研究这些因素的影响；3）使用简单的计数问题，避免其他因素的干扰；4）采用严格的评估指标，以确保结果的可靠性。论文还探索了不同的提示策略，例如使用更详细的描述或提供示例，以提高VLMs的计数准确率。

## 📊 实验亮点

实验结果表明，当图像中只包含一种形状时，VLMs可以相对准确地计数。然而，当图像中包含多种形状时，VLMs的计数准确率显著下降。例如，在某些组合计数任务中，VLMs的准确率低于50%。这表明现有的VLMs在组合计数方面存在显著的缺陷，需要进一步改进。

## 🎯 应用场景

该研究成果可应用于评估和改进视觉语言模型的计数能力，尤其是在需要精确计数的场景中，如自动驾驶（车辆和行人计数）、智能零售（商品计数）和医学图像分析（细胞计数）。未来的研究可以基于VLMCountBench开发更强大的计数模型，提高VLMs在实际应用中的可靠性。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have become a central focus of today's AI community, owing to their impressive abilities gained from training on large-scale vision-language data from the Web. These models have demonstrated strong performance across diverse tasks, including image understanding, video understanding, complex visual reasoning, and embodied AI. Despite these noteworthy successes, a fundamental question remains: Can VLMs count objects correctly? In this paper, we introduce a simple yet effective benchmark, VLMCountBench, designed under a minimalist setting with only basic geometric shapes (e.g., triangles, circles) and their compositions, focusing exclusively on counting tasks without interference from other factors. We adopt strict independent variable control and systematically study the effects of simple properties such as color, size, and prompt refinement in a controlled ablation. Our empirical results reveal that while VLMs can count reliably when only one shape type is present, they exhibit substantial failures when multiple shape types are combined (i.e., compositional counting). This highlights a fundamental empirical limitation of current VLMs and motivates important directions for future research.

