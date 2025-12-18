---
layout: default
title: MosaicDoc: A Large-Scale Bilingual Benchmark for Visually Rich Document Understanding
---

# MosaicDoc: A Large-Scale Bilingual Benchmark for Visually Rich Document Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09919" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09919v1</a>
  <a href="https://arxiv.org/pdf/2511.09919.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09919v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.09919v1', 'MosaicDoc: A Large-Scale Bilingual Benchmark for Visually Rich Document Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ketong Chen, Yuhao Chen, Yang Xue

**分类**: cs.CV

**发布日期**: 2025-11-13

---

## 💡 一句话要点

**提出MosaicDoc：一个大规模双语视觉文档理解基准，解决现有基准的局限性。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉文档理解` `多模态学习` `大型语言模型` `基准数据集` `双语文档`

## 📋 核心要点

1. 现有视觉-语言模型基准主要以英文为主，布局简单，任务有限，无法充分评估模型在复杂文档理解方面的能力。
2. 论文提出DocWeaver多智能体流水线，利用大型语言模型自动生成大规模双语（中英文）视觉文档理解基准MosaicDoc。
3. MosaicDoc包含72K图像和600K+ QA对，对现有模型评估表明其在处理真实文档复杂性方面存在局限性。

## 📝 摘要（中文）

尽管视觉-语言模型（VLMs）取得了快速进展，但现有基准对它们能力的评估不足，这些基准主要以英语为中心，布局简单，并且支持的任务有限。因此，它们无法评估模型在视觉丰富文档理解（VRDU）方面的性能，这是一个涉及复杂布局和密集文本的关键挑战。为了解决这个问题，我们引入了DocWeaver，一种新颖的多智能体流水线，它利用大型语言模型来自动生成新的基准。最终成果是MosaicDoc，一个大规模、双语（中文和英文）资源，旨在推动VRDU的边界。MosaicDoc来源于报纸和杂志，具有多样且复杂的布局（包括多列和非曼哈顿布局），来自196家出版商的丰富的风格多样性，以及全面的多任务注释（OCR、VQA、阅读顺序和定位）。MosaicDoc包含72K张图像和超过600K个QA对，是该领域的一个权威基准。我们对最先进模型在该基准上的广泛评估揭示了它们在处理真实世界文档复杂性方面的当前局限性，并为未来的研究指明了明确的道路。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型（VLMs）的评估基准主要集中在英文文档，布局简单，任务类型有限，无法充分评估模型在处理复杂、多语言、视觉丰富的文档理解（VRDU）能力。现有方法难以应对真实世界文档的复杂布局和密集文本。

**核心思路**：论文的核心思路是利用大型语言模型（LLMs）的生成能力，构建一个自动化的数据生成流水线DocWeaver，从而高效地创建大规模、多样化的VRDU基准数据集。通过模拟真实文档的生成过程，克服了人工标注成本高、数据规模受限的问题。

**技术框架**：DocWeaver是一个多智能体流水线，其主要流程包括：1) 从报纸和杂志等来源收集原始文档图像；2) 利用LLMs生成与文档内容相关的多任务标注，包括OCR、VQA、阅读顺序和定位信息；3) 对生成的数据进行清洗和验证，确保数据质量。MosaicDoc数据集由此生成，包含72K图像和600K+ QA对。

**关键创新**：该论文的关键创新在于提出了DocWeaver，一个基于LLM的自动化基准数据集生成框架。与传统的人工标注方法相比，DocWeaver能够以更低的成本和更高的效率生成大规模、多样化的VRDU数据集。此外，MosaicDoc数据集本身也具有创新性，它包含了中英文双语文档，以及复杂的布局和多任务标注。

**关键设计**：DocWeaver流水线中，LLM的选择和prompt的设计至关重要。论文可能采用了特定的LLM（如GPT-3或类似模型），并针对不同的任务（OCR、VQA等）设计了不同的prompt，以提高生成数据的质量。此外，数据清洗和验证环节也可能采用了特定的规则或算法，以过滤掉不准确或不一致的标注。

## 📊 实验亮点

论文通过在MosaicDoc基准上对现有最先进模型进行评估，揭示了它们在处理真实世界文档复杂性方面的局限性。具体性能数据（如OCR准确率、VQA准确率等）以及与现有基线的对比结果，展示了MosaicDoc的挑战性和价值，并为未来的研究方向提供了明确的指导。

## 🎯 应用场景

该研究成果可广泛应用于文档智能处理领域，例如智能文档分析、信息抽取、智能客服、自动化报告生成等。MosaicDoc基准数据集的发布将促进视觉-语言模型在VRDU任务上的研究进展，提升模型在真实世界文档场景中的应用能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Despite the rapid progress of Vision-Language Models (VLMs), their capabilities are inadequately assessed by existing benchmarks, which are predominantly English-centric, feature simplistic layouts, and support limited tasks. Consequently, they fail to evaluate model performance for Visually Rich Document Understanding (VRDU), a critical challenge involving complex layouts and dense text. To address this, we introduce DocWeaver, a novel multi-agent pipeline that leverages Large Language Models to automatically generate a new benchmark. The result is MosaicDoc, a large-scale, bilingual (Chinese and English) resource designed to push the boundaries of VRDU. Sourced from newspapers and magazines, MosaicDoc features diverse and complex layouts (including multi-column and non-Manhattan), rich stylistic variety from 196 publishers, and comprehensive multi-task annotations (OCR, VQA, reading order, and localization). With 72K images and over 600K QA pairs, MosaicDoc serves as a definitive benchmark for the field. Our extensive evaluation of state-of-the-art models on this benchmark reveals their current limitations in handling real-world document complexity and charts a clear path for future research.

