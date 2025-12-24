---
layout: default
title: MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs
---

# MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21693" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21693v3</a>
  <a href="https://arxiv.org/pdf/2505.21693.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21693v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21693v3', 'MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raoyuan Zhao, Beiduo Chen, Barbara Plank, Michael A. Hedderich

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-09-22)

**备注**: Accepted by EMNLP 2025 Findings, 33 pages, 30 figures

---

## 💡 一句话要点

**提出MAKIEval框架以评估LLMs的文化意识**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文化意识评估` `大型语言模型` `多语言框架` `Wikidata` `自动化评估` `跨语言差异` `模型优化`

## 📋 核心要点

1. 现有的多语言评估方法面临基准有限和翻译质量可疑的问题，导致文化意识评估困难。
2. MAKIEval框架通过利用Wikidata的多语言结构，自动识别和链接文化实体，实现无人工标注的评估。
3. 实验结果显示，7个LLMs在英语中表现出更强的文化意识，提示英语在激活文化知识方面的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在全球范围内被广泛使用，但其以英语为中心的预训练引发了对跨语言文化意识差异的担忧，常导致偏见输出。为更好地评估这些差异，本文提出了MAKIEval，一个自动化的多语言框架，用于评估LLMs在不同语言、地区和主题下的文化意识。MAKIEval利用Wikidata的多语言结构作为跨语言锚点，自动识别模型输出中的文化实体，并将其链接到结构化知识，实现无须人工标注或翻译的可扩展评估。我们还引入了四个度量标准，捕捉文化意识的不同维度：细粒度、多样性、文化特异性和跨语言共识。通过对7个来自不同地区的LLMs进行评估，发现模型在英语中表现出更强的文化意识。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在文化意识评估中的跨语言差异问题。现有方法由于缺乏有效的基准和翻译质量不高，难以全面评估文化意识。

**核心思路**：MAKIEval框架通过自动化手段，利用Wikidata的多语言特性，识别模型输出中的文化实体，并将其与结构化知识链接，从而实现高效的文化意识评估。

**技术框架**：MAKIEval的整体架构包括数据输入、文化实体识别、知识链接和评估指标计算四个主要模块。数据输入阶段收集多语言文本，文化实体识别模块自动提取相关文化信息，知识链接模块将提取的信息与Wikidata进行匹配，最后通过评估指标计算模块生成评估结果。

**关键创新**：MAKIEval的主要创新在于其自动化的文化意识评估能力，避免了传统方法中对人工标注和翻译的依赖，提升了评估的可扩展性和准确性。

**关键设计**：在设计上，MAKIEval引入了四个评估指标：细粒度、多样性、文化特异性和跨语言共识，能够全面反映模型的文化意识水平。

## 📊 实验亮点

实验结果表明，7个不同地区的LLMs在文化意识评估中，英语模型的表现显著优于其他语言，提示英语在激活文化知识方面的有效性。这一发现为未来的模型优化提供了重要参考。

## 🎯 应用场景

MAKIEval框架可广泛应用于多语言大型语言模型的评估，尤其是在跨文化交流、国际化产品开发和教育领域。其自动化特性使得研究人员和开发者能够快速识别模型的文化偏见，从而优化模型的训练和应用，提升其在多语言环境中的表现。

## 📄 摘要（原文）

> Large language models (LLMs) are used globally across many languages, but their English-centric pretraining raises concerns about cross-lingual disparities for cultural awareness, often resulting in biased outputs. However, comprehensive multilingual evaluation remains challenging due to limited benchmarks and questionable translation quality. To better assess these disparities, we introduce MAKIEval, an automatic multilingual framework for evaluating cultural awareness in LLMs across languages, regions, and topics. MAKIEval evaluates open-ended text generation, capturing how models express culturally grounded knowledge in natural language. Leveraging Wikidata's multilingual structure as a cross-lingual anchor, it automatically identifies cultural entities in model outputs and links them to structured knowledge, enabling scalable, language-agnostic evaluation without manual annotation or translation. We then introduce four metrics that capture complementary dimensions of cultural awareness: granularity, diversity, cultural specificity, and consensus across languages. We assess 7 LLMs developed from different parts of the world, encompassing both open-source and proprietary systems, across 13 languages, 19 countries and regions, and 6 culturally salient topics (e.g., food, clothing). Notably, we find that models tend to exhibit stronger cultural awareness in English, suggesting that English prompts more effectively activate culturally grounded knowledge.

