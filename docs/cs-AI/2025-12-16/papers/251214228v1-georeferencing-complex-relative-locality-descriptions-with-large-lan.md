---
layout: default
title: Georeferencing complex relative locality descriptions with large language models
---

# Georeferencing complex relative locality descriptions with large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14228" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14228v1</a>
  <a href="https://arxiv.org/pdf/2512.14228.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14228v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14228v1', 'Georeferencing complex relative locality descriptions with large language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aneesha Fernando, Surangika Ranathunga, Kristin Stock, Raj Prasanna, Christopher B. Jones

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: Provisionally accepted for publication in the International Journal of Geographical Information Science

---

## 💡 一句话要点

**利用大型语言模型解决生物多样性领域复杂相对位置描述的地理定位问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `地理定位` `大型语言模型` `生物多样性` `位置描述` `量化低秩适应`

## 📋 核心要点

1. 现有地理定位方法在处理包含空间关系的相对位置描述时存在精度不足的问题，尤其是在生物标本采集记录中。
2. 论文提出利用大型语言模型（LLM）理解和处理复杂的位置描述，并通过微调来提升LLM在特定领域的地理定位能力。
3. 实验结果表明，该方法在生物多样性数据集上优于现有基线，显著提高了地理定位的准确性，尤其是在处理复杂描述时。

## 📝 摘要（中文）

本文探讨了使用大型语言模型（LLM）自动地理定位复杂位置描述的潜力，重点关注生物多样性收藏领域。传统的地理定位方法依赖于地名词典或语言模型，但在处理包含空间关系的相对位置描述时精度不足。针对生物标本采集记录中常见的位置描述问题，我们首先确定了有效的提示模式，然后使用量化低秩适应（QLoRA）在来自多个地区和语言的生物多样性数据集上微调LLM。结果表明，对于固定量的训练数据，我们的方法优于现有基线，平均有65%的记录位于10公里半径范围内。在纽约州数据集上取得了最佳结果，85%的记录位于10公里范围内，67%的记录位于1公里范围内。该LLM在处理冗长、复杂的位置描述方面表现良好，突显了其在地理定位复杂位置描述方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决生物多样性研究中，由于历史标本采集记录缺乏精确坐标，而仅包含复杂相对位置描述，导致地理定位困难的问题。现有方法，如基于地名词典或简单语言模型的方法，难以有效处理这些复杂描述，导致定位精度低，人工成本高。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的语言理解和推理能力，将复杂的位置描述转化为地理坐标。通过微调LLM，使其能够更好地理解生物多样性领域的特定术语和描述方式，从而提高地理定位的准确性。

**技术框架**：整体框架包括以下几个阶段：1) 数据准备：收集包含复杂位置描述的生物多样性数据集；2) 提示工程：设计有效的提示模式，引导LLM理解位置描述并生成坐标；3) 模型微调：使用QLoRA（Quantized Low-Rank Adaptation）方法在生物多样性数据集上微调LLM；4) 评估：使用距离误差（如10公里半径内）作为指标评估地理定位的准确性。

**关键创新**：最重要的技术创新点在于将大型语言模型应用于复杂相对位置描述的地理定位问题，并采用QLoRA进行高效的领域自适应微调。与传统方法相比，该方法能够更好地理解和处理自然语言描述中的空间关系和上下文信息。

**关键设计**：论文的关键设计包括：1) 提示模式的设计，需要能够有效地引导LLM提取位置信息；2) QLoRA微调方法的选择，能够在有限的计算资源下实现模型的快速适应；3) 评估指标的选择，使用距离误差能够更直观地反映地理定位的准确性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14228v1/figures/1_fig_sample-prompt.jpeg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14228v1/figures/2_fig_methodology_overview.jpeg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14228v1/figures/3_fig_distance_histogram.jpeg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在生物多样性数据集上优于现有基线，平均有65%的记录位于10公里半径范围内。在纽约州数据集上取得了最佳结果，85%的记录位于10公里范围内，67%的记录位于1公里范围内。这些结果表明，该方法能够显著提高复杂位置描述的地理定位准确性。

## 🎯 应用场景

该研究成果可广泛应用于生物多样性研究、生态保护、环境监测等领域。通过自动地理定位历史标本采集记录，可以更准确地了解物种分布、气候变化对生物的影响等，为科学研究和决策提供重要支持。此外，该方法还可以应用于其他领域，如考古学、历史地理学等，具有重要的实际价值和潜在影响。

## 📄 摘要（原文）

> Georeferencing text documents has typically relied on either gazetteer-based methods to assign geographic coordinates to place names, or on language modelling approaches that associate textual terms with geographic locations. However, many location descriptions specify positions relatively with spatial relationships, making geocoding based solely on place names or geo-indicative words inaccurate. This issue frequently arises in biological specimen collection records, where locations are often described through narratives rather than coordinates if they pre-date GPS. Accurate georeferencing is vital for biodiversity studies, yet the process remains labour-intensive, leading to a demand for automated georeferencing solutions. This paper explores the potential of Large Language Models (LLMs) to georeference complex locality descriptions automatically, focusing on the biodiversity collections domain. We first identified effective prompting patterns, then fine-tuned an LLM using Quantized Low-Rank Adaptation (QLoRA) on biodiversity datasets from multiple regions and languages. Our approach outperforms existing baselines with an average, across datasets, of 65% of records within a 10 km radius, for a fixed amount of training data. The best results (New York state) were 85% within 10km and 67% within 1km. The selected LLM performs well for lengthy, complex descriptions, highlighting its potential for georeferencing intricate locality descriptions.

