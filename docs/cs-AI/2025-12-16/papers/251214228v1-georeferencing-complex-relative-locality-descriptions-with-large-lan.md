---
layout: default
title: Georeferencing complex relative locality descriptions with large language models
---

# Georeferencing complex relative locality descriptions with large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14228" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14228v1</a>
  <a href="https://arxiv.org/pdf/2512.14228.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14228v1" onclick="toggleFavorite(this, '2512.14228v1', 'Georeferencing complex relative locality descriptions with large language models')" title="添加到收藏夹">☆ 收藏</button>
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

1. 现有地理定位方法难以处理包含空间关系的相对位置描述，尤其是在生物标本采集记录中。
2. 利用大型语言模型，通过有效的提示模式和量化低秩适应微调，实现自动地理定位。
3. 实验结果表明，该方法优于现有基线，在多个数据集上均取得了显著的定位精度提升。

## 📝 摘要（中文）

本文探讨了使用大型语言模型（LLM）自动地理定位复杂位置描述的潜力，重点关注生物多样性收藏领域。传统的地理定位方法依赖于地名词典或语言模型，但在处理包含空间关系的相对位置描述时精度不足。针对生物标本采集记录中常见的位置描述问题，我们首先确定了有效的提示模式，然后使用量化低秩适应（QLoRA）在来自多个地区和语言的生物多样性数据集上微调LLM。结果表明，对于固定数量的训练数据，我们的方法优于现有基线，平均有65%的记录位于10公里半径范围内。在纽约州数据集上取得了最佳结果，85%的记录位于10公里范围内，67%的记录位于1公里范围内。该LLM在处理冗长、复杂的位置描述方面表现良好，突显了其在地理定位复杂位置描述方面的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决生物多样性研究中，由于历史生物标本采集记录常使用复杂、相对的位置描述而非精确坐标，导致难以进行准确地理定位的问题。现有基于地名词典或语言模型的方法无法有效处理这些包含空间关系的描述，导致定位精度不足。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的语言理解和推理能力，通过学习生物多样性数据集中的位置描述模式，自动推断出位置的地理坐标。通过微调LLM，使其能够理解和处理复杂的相对位置描述，从而实现更精确的地理定位。

**技术框架**：整体框架包括以下几个主要步骤：1) 数据准备：收集和整理包含复杂位置描述的生物多样性数据集。2) 提示工程：设计有效的提示模式，引导LLM理解和生成地理坐标。3) 模型微调：使用量化低秩适应（QLoRA）技术，在生物多样性数据集上微调LLM。4) 评估：使用距离误差指标（如10公里半径内定位精度）评估模型的性能。

**关键创新**：最重要的技术创新点在于将大型语言模型应用于解决复杂相对位置描述的地理定位问题。与传统方法相比，LLM能够更好地理解和推理自然语言描述中的空间关系，从而实现更精确的地理定位。QLoRA的使用降低了微调LLM的计算成本。

**关键设计**：论文的关键设计包括：1) 提示模式的设计，旨在引导LLM理解位置描述并生成坐标。2) 使用QLoRA进行模型微调，降低计算资源需求。3) 针对不同地区和语言的数据集进行微调，提高模型的泛化能力。4) 使用10公里和1公里半径内的定位精度作为评估指标。

## 📊 实验亮点

实验结果表明，该方法在生物多样性数据集上优于现有基线，平均有65%的记录位于10公里半径范围内。在纽约州数据集上取得了最佳结果，85%的记录位于10公里范围内，67%的记录位于1公里范围内。这些结果表明，大型语言模型在处理复杂位置描述的地理定位问题上具有显著优势。

## 🎯 应用场景

该研究成果可应用于生物多样性研究、生态环境保护、自然资源管理等领域。通过自动地理定位历史生物标本采集记录，可以更准确地了解物种分布、气候变化影响等信息，为相关研究和决策提供支持。该方法还可扩展到其他领域，如考古学、历史地理学等，具有广泛的应用前景。

## 📄 摘要（原文）

> Georeferencing text documents has typically relied on either gazetteer-based methods to assign geographic coordinates to place names, or on language modelling approaches that associate textual terms with geographic locations. However, many location descriptions specify positions relatively with spatial relationships, making geocoding based solely on place names or geo-indicative words inaccurate. This issue frequently arises in biological specimen collection records, where locations are often described through narratives rather than coordinates if they pre-date GPS. Accurate georeferencing is vital for biodiversity studies, yet the process remains labour-intensive, leading to a demand for automated georeferencing solutions. This paper explores the potential of Large Language Models (LLMs) to georeference complex locality descriptions automatically, focusing on the biodiversity collections domain. We first identified effective prompting patterns, then fine-tuned an LLM using Quantized Low-Rank Adaptation (QLoRA) on biodiversity datasets from multiple regions and languages. Our approach outperforms existing baselines with an average, across datasets, of 65% of records within a 10 km radius, for a fixed amount of training data. The best results (New York state) were 85% within 10km and 67% within 1km. The selected LLM performs well for lengthy, complex descriptions, highlighting its potential for georeferencing intricate locality descriptions.

