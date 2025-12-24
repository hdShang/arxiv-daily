---
layout: default
title: "MuSciClaims: Multimodal Scientific Claim Verification"
---

# MuSciClaims: Multimodal Scientific Claim Verification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04585" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04585v2</a>
  <a href="https://arxiv.org/pdf/2506.04585.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04585v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04585v2', 'MuSciClaims: Multimodal Scientific Claim Verification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yash Kumar Lal, Manikanta Bandham, Mohammad Saqib Hasan, Apoorva Kashi, Mahnaz Koupaee, Niranjan Balasubramanian

**分类**: cs.CL

**发布日期**: 2025-06-05 (更新: 2025-07-30)

---

## 💡 一句话要点

**提出MuSciClaims以解决科学声明验证的多模态基准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `科学声明验证` `多模态基准` `视觉-语言模型` `信息提取` `模型评估`

## 📋 核心要点

1. 现有的科学声明验证方法缺乏有效的多模态基准，无法直接测试模型的验证能力。
2. 论文提出了MuSciClaims基准，通过自动提取和手动扰动声明来测试模型的验证能力。
3. 实验结果显示大多数视觉-语言模型的性能较差，最佳模型的F1值仅为0.72，且存在偏向性判断问题。

## 📝 摘要（中文）

评估科学声明需要识别、提取和推理科学文献中信息丰富的图形所表达的多模态数据。尽管在科学问答、图形标题生成和其他基于图表的数据多模态推理任务方面已有大量研究，但目前缺乏直接测试声明验证能力的多模态基准。为此，本文提出了新的基准MuSciClaims，并附带诊断任务。我们自动从科学文章中提取支持的声明，并手动扰动以生成相反的声明。这些扰动旨在测试特定的声明验证能力。我们的结果表明，大多数视觉-语言模型表现不佳（F1值约为0.3-0.5），即使是最佳模型也仅达到0.72 F1，且它们倾向于判断声明为支持，可能误解声明中的细微扰动。我们的诊断显示，模型在定位图形中的正确证据方面表现不佳，难以跨模态聚合信息，并且常常无法理解图形的基本组成部分。

## 🔬 方法详解

**问题定义**：本文旨在解决科学声明验证中的多模态数据处理问题，现有方法在这一领域缺乏有效的基准和测试手段，导致模型性能不佳。

**核心思路**：通过构建MuSciClaims基准，自动提取科学文章中的声明，并通过手动扰动生成相反声明，以测试模型的验证能力和局限性。

**技术框架**：整体流程包括声明的自动提取、扰动生成、模型验证能力测试和诊断任务。主要模块包括数据提取、扰动设计和模型评估。

**关键创新**：MuSciClaims基准的提出是本研究的核心创新，它为科学声明验证提供了一个系统化的测试平台，填补了现有研究的空白。

**关键设计**：在模型评估中，采用了特定的损失函数和评估指标（如F1值），并设计了多种扰动方式以测试模型对声明的理解和判断能力。通过这些设计，能够更全面地评估模型的性能和局限性。

## 📊 实验亮点

实验结果显示，大多数视觉-语言模型在声明验证任务中的F1值仅为0.3-0.5，最佳模型的F1值为0.72，表明当前模型在理解和判断科学声明方面存在显著不足。此外，模型普遍存在偏向性，倾向于将声明判断为支持，显示出对细微扰动的误解。

## 🎯 应用场景

该研究的潜在应用场景包括科学文献的自动化审核、科研成果的可信度评估以及科学教育中的信息验证。通过提供一个标准化的验证基准，MuSciClaims可以帮助研究人员和开发者提升模型在科学声明验证中的表现，推动相关领域的进一步研究与应用。

## 📄 摘要（原文）

> Assessing scientific claims requires identifying, extracting, and reasoning with multimodal data expressed in information-rich figures in scientific literature. Despite the large body of work in scientific QA, figure captioning, and other multimodal reasoning tasks over chart-based data, there are no readily usable multimodal benchmarks that directly test claim verification abilities. To remedy this gap, we introduce a new benchmark MuSciClaims accompanied by diagnostics tasks. We automatically extract supported claims from scientific articles, which we manually perturb to produce contradicted claims. The perturbations are designed to test for a specific set of claim verification capabilities. We also introduce a suite of diagnostic tasks that help understand model failures. Our results show most vision-language models are poor (~0.3-0.5 F1), with even the best model only achieving 0.72 F1. They are also biased towards judging claims as supported, likely misunderstanding nuanced perturbations within the claims. Our diagnostics show models are bad at localizing correct evidence within figures, struggle with aggregating information across modalities, and often fail to understand basic components of the figure.

