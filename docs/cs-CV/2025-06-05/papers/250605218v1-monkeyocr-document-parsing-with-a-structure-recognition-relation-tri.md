---
layout: default
title: "MonkeyOCR: Document Parsing with a Structure-Recognition-Relation Triplet Paradigm"
---

# MonkeyOCR: Document Parsing with a Structure-Recognition-Relation Triplet Paradigm

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05218" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05218v1</a>
  <a href="https://arxiv.org/pdf/2506.05218.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05218v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05218v1', 'MonkeyOCR: Document Parsing with a Structure-Recognition-Relation Triplet Paradigm')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhang Li, Yuliang Liu, Qiang Liu, Zhiyin Ma, Ziyang Zhang, Shuo Zhang, Zidun Guo, Jiarui Zhang, Xinyu Wang, Xiang Bai

**分类**: cs.CV

**发布日期**: 2025-06-05

**🔗 代码/项目**: [GITHUB](https://github.com/Yuliang-Liu/MonkeyOCR)

---

## 💡 一句话要点

**提出MonkeyOCR以解决文档解析效率与准确性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文档解析` `视觉语言模型` `结构识别` `多模态学习` `数据集构建` `机器学习`

## 📋 核心要点

1. 现有文档解析方法往往依赖复杂的多工具管道，效率低下且难以扩展。
2. 论文提出的MonkeyOCR通过结构-识别-关系三元组范式，简化了文档解析过程，提高了处理效率和准确性。
3. 实验结果显示，MonkeyOCR在多个任务上超越了MinerU，特别是在处理公式和表格时，提升幅度显著。

## 📝 摘要（中文）

我们介绍了MonkeyOCR，一种用于文档解析的视觉语言模型，通过利用结构-识别-关系（SRR）三元组范式，推动了该领域的最新进展。该设计简化了复杂的多工具管道，避免了使用大型端到端模型处理完整页面的低效。在SRR中，文档解析被抽象为三个基本问题——“它在哪里？”（结构）、“它是什么？”（识别）和“它是如何组织的？”（关系），分别对应布局分析、内容识别和逻辑排序。这种聚焦的分解方法在不牺牲精度的情况下，实现了高效、可扩展的处理。我们引入了MonkeyDoc，这是迄今为止最全面的文档解析数据集，包含390万个实例，涵盖中英文十种文档类型。实验表明，MonkeyOCR在挑战性内容（如公式和表格）上表现出显著提升，整体性能超过了MinerU。

## 🔬 方法详解

**问题定义**：本论文旨在解决文档解析中的效率与准确性问题。现有方法如MinerU依赖复杂的多工具管道，导致处理效率低下，且大型端到端模型在处理完整页面时存在性能瓶颈。

**核心思路**：论文提出的MonkeyOCR通过结构-识别-关系（SRR）三元组范式，将文档解析分解为三个基本问题，从而简化了处理流程并提高了效率。这样的设计使得模型能够专注于每个子任务，避免了全局优化的复杂性。

**技术框架**：MonkeyOCR的整体架构包括三个主要模块：结构分析（确定元素位置）、内容识别（识别文档内容）和关系分析（理解内容之间的逻辑关系）。通过这种模块化设计，模型能够高效处理文档。

**关键创新**：最重要的技术创新在于SRR三元组范式的引入，它与现有方法的本质区别在于将文档解析任务细化为三个独立但相关的子任务，从而实现了更高的处理效率和准确性。

**关键设计**：在模型设计上，MonkeyOCR使用了3B参数的结构，能够在单个NVIDIA 3090 GPU上高效推理。损失函数和网络结构经过优化，以确保在处理复杂文档时的高效性和准确性。具体的参数设置和训练策略将在后续的代码和模型发布中提供。

## 📊 实验亮点

实验结果表明，MonkeyOCR在文档解析任务上平均超越MinerU 5.1%，在处理公式和表格等挑战性内容时分别提升15.0%和8.6%。此外，MonkeyOCR的处理速度为每秒0.84页，显著快于MinerU的0.65页和Qwen2.5-VL-7B的0.12页。

## 🎯 应用场景

MonkeyOCR的潜在应用领域包括文档自动化处理、信息提取、智能搜索引擎等。其高效的文档解析能力可以大幅提升企业在文档管理和数据分析方面的效率，未来可能在法律、金融、教育等行业产生深远影响。

## 📄 摘要（原文）

> We introduce MonkeyOCR, a vision-language model for document parsing that advances the state of the art by leveraging a Structure-Recognition-Relation (SRR) triplet paradigm. This design simplifies what would otherwise be a complex multi-tool pipeline (as in MinerU's modular approach) and avoids the inefficiencies of processing full pages with giant end-to-end models (e.g., large multimodal LLMs like Qwen-VL). In SRR, document parsing is abstracted into three fundamental questions - "Where is it?" (structure), "What is it?" (recognition), and "How is it organized?" (relation) - corresponding to layout analysis, content identification, and logical ordering. This focused decomposition balances accuracy and speed: it enables efficient, scalable processing without sacrificing precision. To train and evaluate this approach, we introduce the MonkeyDoc (the most comprehensive document parsing dataset to date), with 3.9 million instances spanning over ten document types in both Chinese and English. Experiments show that MonkeyOCR outperforms MinerU by an average of 5.1%, with particularly notable improvements on challenging content such as formulas (+15.0%) and tables (+8.6%). Remarkably, our 3B-parameter model surpasses much larger and top-performing models, including Qwen2.5-VL (72B) and Gemini 2.5 Pro, achieving state-of-the-art average performance on English document parsing tasks. In addition, MonkeyOCR processes multi-page documents significantly faster (0.84 pages per second compared to 0.65 for MinerU and 0.12 for Qwen2.5-VL-7B). The 3B model can be efficiently deployed for inference on a single NVIDIA 3090 GPU. Code and models will be released at https://github.com/Yuliang-Liu/MonkeyOCR.

