---
layout: default
title: "XFinBench: Benchmarking LLMs in Complex Financial Problem Solving and Reasoning"
---

# XFinBench: Benchmarking LLMs in Complex Financial Problem Solving and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15861" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15861v1</a>
  <a href="https://arxiv.org/pdf/2508.15861.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15861v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15861v1', 'XFinBench: Benchmarking LLMs in Complex Financial Problem Solving and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihan Zhang, Yixin Cao, Lizi Liao

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-20

**🔗 代码/项目**: [GITHUB](https://github.com/Zhihan72/XFinBench)

---

## 💡 一句话要点

**提出XFinBench以评估LLMs在复杂金融问题解决中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `金融问题解决` `大型语言模型` `多模态数据处理` `知识增强` `基准评估`

## 📋 核心要点

1. 现有大型语言模型在处理复杂金融问题时面临推理能力不足和多模态数据处理的挑战。
2. 论文提出XFinBench基准，通过4235个示例评估LLMs在金融领域的多种能力，特别关注知识密集型问题。
3. 实验表明，尽管o1模型在文本处理上表现最佳，但在时间推理和情景规划方面仍显著低于人类专家。

## 📝 摘要（中文）

解决金融问题需要复杂的推理、多模态数据处理和广泛的技术理解，这对当前的大型语言模型（LLMs）提出了独特的挑战。我们引入了XFinBench，这是一个包含4235个示例的新基准，旨在评估LLMs在多样化的研究生级金融主题中解决复杂、知识密集型金融问题的能力。通过XFinBench，我们识别了LLMs的五个核心能力：术语理解、时间推理、未来预测、情景规划和数值建模。实验结果显示，o1是表现最佳的文本模型，整体准确率为67.3%，但仍显著低于人类专家，尤其是在时间推理和情景规划能力方面。我们还构建了一个包含3032个金融术语的知识库进行知识增强分析，发现相关知识对问题的准确性提升主要体现在小型开源模型上。此外，错误分析显示，计算中的舍入误差和对图像中曲线位置及交点的盲点是导致模型在计算和视觉上下文问题上表现不佳的主要原因。

## 🔬 方法详解

**问题定义**：本论文旨在解决当前大型语言模型在复杂金融问题解决中的能力不足，尤其是在推理和多模态数据处理方面的挑战。现有方法在处理知识密集型金融问题时表现不佳，无法满足实际需求。

**核心思路**：论文提出XFinBench基准，通过设计多样化的金融问题示例，评估LLMs在术语理解、时间推理等方面的能力，旨在为金融领域的LLMs提供系统性的评估标准。

**技术框架**：XFinBench的整体架构包括数据集构建、模型评估和知识增强分析三个主要模块。数据集包含4235个多模态示例，涵盖多个金融主题，模型评估则通过18个领先模型的实验进行。

**关键创新**：XFinBench是首个专注于金融领域的LLMs评估基准，识别了LLMs在处理复杂金融问题时的五个核心能力，填补了现有基准在金融领域的空白。

**关键设计**：在实验中，构建了一个包含3032个金融术语的知识库用于知识增强分析，发现相关知识对小型开源模型的准确性提升显著。此外，针对模型的错误分析揭示了计算和视觉上下文问题的主要误差来源。

## 📊 实验亮点

实验结果显示，o1模型在文本处理上的整体准确率为67.3%，但仍比人类专家低12.5%。尤其在时间推理和情景规划能力方面，模型表现显著不足，指出了当前LLMs在复杂金融问题处理中的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括金融分析、投资决策支持和教育培训等。通过提升LLMs在复杂金融问题解决中的能力，XFinBench为金融科技公司和教育机构提供了一个有效的工具，帮助其更好地利用人工智能技术。未来，随着模型能力的提升，可能会在金融行业的自动化和智能决策中发挥更大作用。

## 📄 摘要（原文）

> Solving financial problems demands complex reasoning, multimodal data processing, and a broad technical understanding, presenting unique challenges for current large language models (LLMs). We introduce XFinBench, a novel benchmark with 4,235 examples designed to evaluate LLM's ability in solving complex, knowledge-intensive financial problems across diverse graduate-level finance topics with multi-modal context. We identify five core capabilities of LLMs using XFinBench, i.e, terminology understanding, temporal reasoning, future forecasting, scenario planning, and numerical modelling. Upon XFinBench, we conduct extensive experiments on 18 leading models. The result shows that o1 is the best-performing text-only model with an overall accuracy of 67.3%, but still lags significantly behind human experts with 12.5%, especially in temporal reasoning and scenario planning capabilities. We further construct a knowledge bank with 3,032 finance terms for knowledge augmentation analysis, and find that relevant knowledge to the question only brings consistent accuracy improvements to small open-source model. Additionally, our error analysis reveals that rounding errors during calculation and blindness to position and intersection of curves in the image are two primary issues leading to model's poor performance in calculating and visual-context questions, respectively. Code and dataset are accessible via GitHub: https://github.com/Zhihan72/XFinBench.

