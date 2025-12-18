---
layout: default
title: PISA-Bench: The PISA Index as a Multilingual and Multimodal Metric for the Evaluation of Vision-Language Models
---

# PISA-Bench: The PISA Index as a Multilingual and Multimodal Metric for the Evaluation of Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.24792" class="toolbar-btn" target="_blank">📄 arXiv: 2510.24792v2</a>
  <a href="https://arxiv.org/pdf/2510.24792.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.24792v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.24792v2', 'PISA-Bench: The PISA Index as a Multilingual and Multimodal Metric for the Evaluation of Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Patrick Haller, Fabio Barth, Jonas Golde, Georg Rehm, Alan Akbik

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-27 (更新: 2025-11-12)

**备注**: 8 pages, 11 tables and figures

---

## 💡 一句话要点

**PISA-Bench：一个多语言多模态基准，用于评估视觉-语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `多模态学习` `多语言` `基准测试` `PISA` `教育` `推理能力`

## 📋 核心要点

1. 现有视觉-语言模型基准测试数据集缺乏高质量、人工验证的多语言示例，且依赖于合成数据，限制了模型评估的可靠性。
2. PISA-Bench利用专家设计的PISA测试题，构建了一个包含六种语言的平行语料库，为多语言多模态推理提供更可靠的评估。
3. 实验表明，现有视觉-语言模型在PISA-Bench上表现不佳，尤其是在非英语语种和空间几何推理任务中，突显了进一步研究的必要性。

## 📝 摘要（中文）

视觉-语言模型（VLMs）在多模态推理方面取得了显著进展。然而，现有的基准测试在高质量、人工验证的示例方面仍然有限。许多当前的数据集依赖于大型语言模型（LLMs）合成生成的内容。此外，大多数数据集仅限于英语，因为翻译样本的手动质量保证既耗时又昂贵。为了填补这一空白，我们推出了PISA-Bench，这是一个多语言基准，源自专家创建的PISA测试的英语示例，PISA测试是一个统一的框架，用于评估八十多个国家学生的胜任力。每个示例都包含人工提取的指令、问题、答案选项和图像，并丰富了问题类型类别，并且已从英语翻译成其他五种语言（西班牙语、德语、中文、法语和意大利语），从而形成了一个涵盖六种语言的完全平行的语料库。我们评估了PISA-Bench上最先进的视觉-语言模型，发现特别是小型模型（<20B参数）未能获得高测试分数。我们进一步发现非英语拆分时的性能显着下降，以及当模型执行空间和几何推理任务时的高错误率。通过发布数据集和评估框架，我们为推进多语言多模态推理研究提供资源。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型（VLM）的评估基准存在以下痛点：一是数据集质量不高，依赖大型语言模型（LLM）合成数据，缺乏人工验证；二是数据集语种单一，主要集中在英语，缺乏多语言支持，限制了模型在不同语言环境下的泛化能力。因此，需要一个高质量、多语言的基准数据集来更全面地评估VLM的性能。

**核心思路**：论文的核心思路是利用PISA（国际学生评估项目）测试题作为构建基准数据集的基础。PISA测试题由专家设计，具有高质量、人工验证的特点，并且涵盖多种语言。通过将PISA测试题转化为视觉-语言任务，可以构建一个更可靠、更具挑战性的多语言VLM评估基准。

**技术框架**：PISA-Bench的构建流程主要包括以下几个步骤：1) 从PISA测试题中提取英语示例，包括指令、问题、答案选项和图像；2) 对提取的示例进行标注，添加问题类型类别等信息；3) 将英语示例翻译成五种其他语言（西班牙语、德语、中文、法语和意大利语），形成一个完全平行的六种语言语料库；4) 构建评估框架，用于评估VLM在PISA-Bench上的性能。

**关键创新**：PISA-Bench的关键创新在于：1) 数据集质量高：使用专家设计的PISA测试题，避免了LLM合成数据带来的质量问题；2) 多语言支持：提供六种语言的平行语料库，可以评估VLM在不同语言环境下的性能；3) 任务多样性：PISA测试题涵盖多种问题类型，可以评估VLM在不同任务上的能力。

**关键设计**：PISA-Bench的关键设计包括：1) 问题的类型标注，方便针对特定类型的推理能力进行评估；2) 严格的翻译流程，保证多语言版本的一致性和准确性；3) 评估指标的选择，能够全面反映VLM在不同语言和任务上的性能。

## 📊 实验亮点

实验结果表明，现有视觉-语言模型在PISA-Bench上的表现与模型规模相关，小模型（<20B参数）表现较差。非英语语种的性能明显低于英语，且在空间和几何推理任务中错误率较高。这些结果突显了现有模型在多语言和复杂推理方面的不足，为未来的研究方向提供了重要参考。

## 🎯 应用场景

PISA-Bench可用于评估和提升视觉-语言模型在多语言环境下的推理能力，尤其是在教育、信息检索和跨文化交流等领域。高质量的多语言理解能力有助于开发更智能的教育辅助工具，提升跨语言信息检索的准确性，并促进不同文化背景下的有效沟通。

## 📄 摘要（原文）

> Vision-language models (VLMs) have demonstrated remarkable progress in multimodal reasoning. However, existing benchmarks remain limited in terms of high-quality, human-verified examples. Many current datasets rely on synthetically generated content by large language models (LLMs). Furthermore, most datasets are limited to English, as manual quality assurance of translated samples is time-consuming and costly. To fill this gap, we introduce PISA-Bench, a multilingual benchmark derived from English examples of the expert-created PISA tests, a unified framework for the assessment of student competencies in over eighty countries. Each example consists of human-extracted instructions, questions, answer options, and images, enriched with question type categories, and has been translated from English into five additional languages (Spanish, German, Chinese, French, and Italian), resulting in a fully parallel corpus covering six languages. We evaluate state-of-the-art vision-language models on PISA-Bench and find that especially small models (<20B parameters) fail to achieve high test scores. We further find substantial performance degradation on non-English splits as well as high error-rates when models are tasked with spatial and geometric reasoning. By releasing the dataset and evaluation framework, we provide a resource for advancing research on multilingual multimodal reasoning.

