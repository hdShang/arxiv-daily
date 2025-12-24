---
layout: default
title: "Multi-Physics: A Comprehensive Benchmark for Multimodal LLMs Reasoning on Chinese Multi-Subject Physics Problems"
---

# Multi-Physics: A Comprehensive Benchmark for Multimodal LLMs Reasoning on Chinese Multi-Subject Physics Problems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15839" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15839v1</a>
  <a href="https://arxiv.org/pdf/2509.15839.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15839v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15839v1', 'Multi-Physics: A Comprehensive Benchmark for Multimodal LLMs Reasoning on Chinese Multi-Subject Physics Problems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhongze Luo, Zhenshuai Yin, Yongxin Guo, Zhichao Wang, Jionghao Zhu, Xiaoying Tang

**分类**: cs.CL

**发布日期**: 2025-09-19

**🔗 代码/项目**: [GITHUB](https://github.com/luozhongze/Multi-Physics)

---

## 💡 一句话要点

**提出Multi-Physics：一个用于评估多模态LLM在中文物理问题上推理能力的综合基准。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `大型语言模型` `物理推理` `中文基准` `科学推理`

## 📋 核心要点

1. 现有物理推理评估基准缺乏细粒度学科覆盖、忽略逐步推理过程，且主要以英文为中心，未能充分评估视觉信息的作用。
2. Multi-Physics基准包含1412道图像关联的中文物理选择题，覆盖11个高中物理学科，并提供5个难度级别。
3. 通过双重评估框架，分析MLLM最终答案准确性和逐步推理的完整性，并研究难度和视觉信息的影响。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在推理方面取得了显著进展，但将其应用于物理等专业科学领域时，现有的评估基准存在明显不足。具体而言，现有基准通常缺乏细粒度的学科覆盖，忽略了逐步推理过程，并且主要以英语为中心，未能系统地评估视觉信息的作用。因此，我们推出了Multi-Physics，一个用于中文物理推理的综合基准，包含5个难度级别，涵盖11个高中物理学科的1412个图像关联的选择题。我们采用双重评估框架来评估20个不同的MLLM，分析最终答案的准确性和逐步推理过程的完整性。此外，我们通过比较改变输入模式前后模型的性能，系统地研究了难度级别和视觉信息的影响。我们的工作不仅为社区提供了细粒度的资源，而且为剖析最先进的MLLM的多模态推理过程提供了一种稳健的方法。我们的数据集和代码已开源：https://github.com/luozhongze/Multi-Physics。

## 🔬 方法详解

**问题定义**：论文旨在解决现有MLLM在中文物理问题推理能力评估中存在的不足。现有基准测试集在学科覆盖范围、推理过程评估以及对视觉信息的利用上存在局限性，无法全面评估MLLM在物理领域的推理能力。

**核心思路**：论文的核心思路是构建一个更全面、细粒度的中文物理推理基准测试集，并设计相应的评估方法，从而更准确地评估MLLM在解决复杂物理问题时的推理能力，特别是视觉信息辅助下的推理能力。

**技术框架**：Multi-Physics基准测试集包含以下几个关键组成部分：1) 涵盖11个高中物理学科的1412道选择题；2) 题目与图像关联，考察模型对视觉信息的理解和利用；3) 题目分为5个难度级别，评估模型在不同难度下的表现；4) 采用双重评估框架，同时评估最终答案的准确性和逐步推理过程的完整性。

**关键创新**：该论文的关键创新在于构建了一个专门针对中文物理推理的多模态基准测试集，并设计了相应的评估方法。该基准测试集不仅涵盖了更广泛的物理学科，而且更加注重对模型推理过程的评估，以及对视觉信息利用的考察。

**关键设计**：在数据集构建方面，作者精心挑选和设计了题目，确保其覆盖了高中物理的主要知识点，并与图像信息相结合，增加了题目的复杂性和挑战性。在评估方法方面，作者采用了双重评估框架，既关注最终答案的准确性，又关注逐步推理过程的完整性，从而更全面地评估模型的推理能力。难度分级也经过精心设计，确保能够区分不同模型的性能水平。

## 📊 实验亮点

论文通过对20个MLLM进行评估，发现现有模型在Multi-Physics基准上的表现仍有较大提升空间。实验结果表明，视觉信息对模型性能有显著影响，但不同模型对视觉信息的利用程度不同。此外，模型在不同难度级别上的表现差异明显，表明模型在处理复杂物理问题时仍面临挑战。

## 🎯 应用场景

该研究成果可应用于教育领域，用于评估和提升AI在物理教学中的应用效果。同时，该基准测试集可促进多模态LLM在科学领域的应用，推动AI在解决实际科学问题方面的能力提升。未来，该研究可扩展到其他科学领域，构建更通用的科学推理基准。

## 📄 摘要（原文）

> While multimodal LLMs (MLLMs) demonstrate remarkable reasoning progress, their application in specialized scientific domains like physics reveals significant gaps in current evaluation benchmarks. Specifically, existing benchmarks often lack fine-grained subject coverage, neglect the step-by-step reasoning process, and are predominantly English-centric, failing to systematically evaluate the role of visual information. Therefore, we introduce \textbf {Multi-Physics} for Chinese physics reasoning, a comprehensive benchmark that includes 5 difficulty levels, featuring 1,412 image-associated, multiple-choice questions spanning 11 high-school physics subjects. We employ a dual evaluation framework to evaluate 20 different MLLMs, analyzing both final answer accuracy and the step-by-step integrity of their chain-of-thought. Furthermore, we systematically study the impact of difficulty level and visual information by comparing the model performance before and after changing the input mode. Our work provides not only a fine-grained resource for the community but also offers a robust methodology for dissecting the multimodal reasoning process of state-of-the-art MLLMs, and our dataset and code have been open-sourced: https://github.com/luozhongze/Multi-Physics.

