---
layout: default
title: "AutoArabic: A Three-Stage Framework for Localizing Video-Text Retrieval Benchmarks"
---

# AutoArabic: A Three-Stage Framework for Localizing Video-Text Retrieval Benchmarks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16438" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16438v1</a>
  <a href="https://arxiv.org/pdf/2509.16438.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16438v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16438v1', 'AutoArabic: A Three-Stage Framework for Localizing Video-Text Retrieval Benchmarks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamed Eltahir, Osamah Sarraj, Abdulrahman Alfrihidi, Taha Alshatiri, Mohammed Khurd, Mohammed Bremoo, Tanveer Hussain

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-19

**备注**: Accepted at ArabicNLP 2025 (EMNLP 2025 workshop)

**🔗 代码/项目**: [GITHUB](https://github.com/Tahaalshatiri/AutoArabic)

---

## 💡 一句话要点

**AutoArabic：提出三阶段框架，用于视频-文本检索基准的阿拉伯语本地化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频文本检索` `阿拉伯语本地化` `大型语言模型` `自动化翻译` `错误检测`

## 📋 核心要点

1. 现有视频-文本检索基准主要集中于英语，阿拉伯语缺乏本地化评估指标，阻碍了相关研究。
2. AutoArabic框架利用大型语言模型自动翻译非阿拉伯语基准，并包含错误检测模块，大幅减少人工修订。
3. 实验表明，生成的阿拉伯语基准保留了原数据集的难度，且后编辑能进一步提升性能，零预算输出也可用。

## 📝 摘要（中文）

视频到文本和文本到视频的检索任务主要集中在英语基准数据集（如DiDeMo、MSR-VTT）和新兴的多语言语料库（如RUDDER）上，而阿拉伯语领域缺乏本地化的评估指标。本文提出了一个三阶段框架AutoArabic，利用最先进的大型语言模型（LLMs）将非阿拉伯语基准数据集翻译成现代标准阿拉伯语，从而将所需的人工修订工作减少了近四倍。该框架包含一个错误检测模块，能够以97%的准确率自动标记潜在的翻译错误。通过将该框架应用于视频检索基准数据集DiDeMo，生成了DiDeMo-AR，这是一个包含40144个流畅阿拉伯语描述的变体。本文还对翻译错误进行了分析，并将其组织成一个富有洞察力的分类法，以指导未来的阿拉伯语本地化工作。我们在阿拉伯语和英语变体的基准数据集上，使用相同的超参数训练了一个CLIP风格的基线模型，发现存在适度的性能差距（在Recall@1上约为3个百分点），表明阿拉伯语本地化保留了基准数据集的难度。我们评估了三种后编辑预算（零/仅标记/完全），发现性能随着更多后编辑而单调提高，而原始LLM输出（零预算）仍然可用。为了确保其他语言的可重复性，我们在https://github.com/Tahaalshatiri/AutoArabic上提供了代码。

## 🔬 方法详解

**问题定义**：现有视频-文本检索基准数据集主要以英语为主，缺乏针对阿拉伯语的本地化数据集和评估标准。这限制了阿拉伯语视频内容理解和检索技术的发展，也难以评估现有模型在阿拉伯语环境下的性能。人工翻译成本高昂，且难以保证翻译质量的一致性。

**核心思路**：利用大型语言模型（LLMs）强大的翻译能力，自动化地将现有的英语视频-文本检索基准数据集翻译成阿拉伯语。通过引入错误检测模块，自动识别并标记潜在的翻译错误，从而减少人工校对的工作量，提高翻译效率和质量。

**技术框架**：AutoArabic框架包含三个主要阶段：1) **翻译阶段**：使用LLM将英语文本描述翻译成现代标准阿拉伯语。2) **错误检测阶段**：训练一个错误检测模型，自动识别并标记潜在的翻译错误。3) **后编辑阶段**：根据不同的预算，对标记的错误进行人工校对和修改。最终生成阿拉伯语本地化的视频-文本检索基准数据集。

**关键创新**：该框架的关键创新在于自动化翻译和错误检测的结合。传统的翻译方法依赖大量的人工工作，效率低下且成本高昂。AutoArabic通过LLM的自动化翻译和错误检测模块，显著减少了人工干预的需求，提高了翻译效率和质量。错误检测模块的准确率高达97%，能够有效识别潜在的翻译问题。

**关键设计**：错误检测模块使用监督学习方法，训练一个二分类器来判断翻译结果是否正确。训练数据包括人工标注的翻译错误样本和自动生成的伪错误样本。损失函数采用交叉熵损失函数。在实验中，作者评估了三种后编辑预算：零预算（不进行任何人工校对）、仅标记预算（只对错误检测模块标记的错误进行校对）和完全预算（对所有翻译结果进行校对）。

## 📊 实验亮点

AutoArabic框架能够以97%的准确率自动检测翻译错误，显著减少人工修订工作。在DiDeMo数据集上的实验表明，生成的DiDeMo-AR数据集保留了原数据集的难度，CLIP风格模型在两个数据集上的性能差距仅为3%。后编辑能进一步提升性能，零预算输出也具备可用性。

## 🎯 应用场景

该研究成果可应用于阿拉伯语视频内容理解、视频检索、视频字幕生成等领域。通过提供高质量的阿拉伯语视频-文本检索基准数据集，促进相关算法的开发和评估。该框架也可推广到其他低资源语言的本地化任务中，加速多语言视频内容理解技术的发展。

## 📄 摘要（原文）

> Video-to-text and text-to-video retrieval are dominated by English benchmarks (e.g. DiDeMo, MSR-VTT) and recent multilingual corpora (e.g. RUDDER), yet Arabic remains underserved, lacking localized evaluation metrics. We introduce a three-stage framework, AutoArabic, utilizing state-of-the-art large language models (LLMs) to translate non-Arabic benchmarks into Modern Standard Arabic, reducing the manual revision required by nearly fourfold. The framework incorporates an error detection module that automatically flags potential translation errors with 97% accuracy. Applying the framework to DiDeMo, a video retrieval benchmark produces DiDeMo-AR, an Arabic variant with 40,144 fluent Arabic descriptions. An analysis of the translation errors is provided and organized into an insightful taxonomy to guide future Arabic localization efforts. We train a CLIP-style baseline with identical hyperparameters on the Arabic and English variants of the benchmark, finding a moderate performance gap (about 3 percentage points at Recall@1), indicating that Arabic localization preserves benchmark difficulty. We evaluate three post-editing budgets (zero/ flagged-only/ full) and find that performance improves monotonically with more post-editing, while the raw LLM output (zero-budget) remains usable. To ensure reproducibility to other languages, we made the code available at https://github.com/Tahaalshatiri/AutoArabic.

