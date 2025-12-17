---
layout: default
title: Georeferencing complex relative locality descriptions with large language models
---

# Georeferencing complex relative locality descriptions with large language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14228" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14228</a>
  <a href="https://arxiv.org/pdf/2512.14228.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14228" onclick="toggleFavorite(this, '2512.14228', 'Georeferencing complex relative locality descriptions with large language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aneesha Fernando, Surangika Ranathunga, Kristin Stock, Raj Prasanna, Christopher B. Jones

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**利用大型语言模型解决生物多样性领域复杂相对位置描述的地理定位问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `地理定位` `大型语言模型` `生物多样性` `位置描述` `量化低秩适应`

## 📋 核心要点

1. 现有地理定位方法难以处理基于空间关系的复杂相对位置描述，尤其是在生物多样性标本记录等领域。
2. 该论文提出利用大型语言模型（LLM）理解和处理复杂的位置描述，实现自动地理定位。
3. 通过QLoRA微调LLM，在生物多样性数据集上取得了显著的性能提升，优于现有基线方法。

## 📝 摘要（中文）

地理定位文本通常依赖于地名词典方法或语言建模方法，前者将地理坐标分配给地名，后者将文本术语与地理位置相关联。然而，许多位置描述通过空间关系相对地指定位置，使得仅基于地名或地理指示词的地理编码不准确。生物标本采集记录中经常出现这个问题，因为早于GPS时代的位置通常通过叙述而非坐标描述。准确的地理定位对于生物多样性研究至关重要，但该过程仍然是劳动密集型的，因此需要自动化的地理定位解决方案。本文探讨了大型语言模型（LLM）自动地理定位复杂位置描述的潜力，重点关注生物多样性收藏领域。我们首先确定了有效的提示模式，然后使用量化低秩适应（QLoRA）在来自多个地区和语言的生物多样性数据集上微调LLM。我们的方法优于现有基线，对于固定数量的训练数据，平均而言，跨数据集有65%的记录位于10公里半径内。最佳结果（纽约州）为85%在10公里内，67%在1公里内。所选的LLM对于冗长、复杂的描述表现良好，突出了其地理定位复杂位置描述的潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决生物多样性领域中，由于历史原因或缺乏精确GPS数据，标本采集记录中存在大量复杂、相对的位置描述，导致传统地理定位方法失效的问题。现有方法依赖于地名词典或简单的语言模型，无法有效理解和处理这些复杂的空间关系描述，人工地理定位耗时耗力。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的语言理解和推理能力，将复杂的位置描述转化为地理坐标。LLM能够学习和理解文本中蕴含的空间关系，从而更准确地推断出位置信息。通过微调LLM，使其适应生物多样性领域的特定语言和描述习惯，进一步提高地理定位的准确性。

**技术框架**：整体框架包括以下几个阶段：1) 数据准备：收集和整理包含复杂位置描述的生物多样性数据集。2) 提示工程：设计有效的提示模式，引导LLM理解和生成地理坐标。3) 模型微调：使用量化低秩适应（QLoRA）方法，在预训练的LLM上进行微调，使其适应特定领域的数据。4) 评估：使用距离误差等指标评估模型的地理定位准确性。

**关键创新**：该论文的关键创新在于将大型语言模型应用于复杂相对位置描述的地理定位问题，并探索了有效的提示模式和微调策略。与传统方法相比，LLM能够更好地理解和处理自然语言描述中的空间关系，从而提高地理定位的准确性。QLoRA的使用降低了微调LLM的计算成本。

**关键设计**：论文中使用了量化低秩适应（QLoRA）方法进行模型微调，这是一种参数高效的微调技术，可以在资源有限的情况下对大型语言模型进行微调。具体的提示模式设计和损失函数选择等细节在论文中未详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14228/figures/1_fig_sample-prompt.jpeg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14228/figures/2_fig_methodology_overview.jpeg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14228/figures/3_fig_distance_histogram.jpeg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在生物多样性数据集上优于现有基线方法，平均而言，跨数据集有65%的记录位于10公里半径内。在纽约州数据集上，最佳结果为85%在10公里内，67%在1公里内。这些结果表明，大型语言模型在处理复杂位置描述方面具有显著的优势。

## 🎯 应用场景

该研究成果可应用于生物多样性保护、生态学研究、历史地理学等领域。通过自动地理定位生物标本采集记录，可以加速生物多样性数据的整合和分析，为物种分布建模、气候变化影响评估等研究提供支持。此外，该方法还可以应用于其他包含复杂位置描述的文本数据，例如历史文献、考古报告等。

## 📄 摘要（原文）

> Georeferencing text documents has typically relied on either gazetteer-based methods to assign geographic coordinates to place names, or on language modelling approaches that associate textual terms with geographic locations. However, many location descriptions specify positions relatively with spatial relationships, making geocoding based solely on place names or geo-indicative words inaccurate. This issue frequently arises in biological specimen collection records, where locations are often described through narratives rather than coordinates if they pre-date GPS. Accurate georeferencing is vital for biodiversity studies, yet the process remains labour-intensive, leading to a demand for automated georeferencing solutions. This paper explores the potential of Large Language Models (LLMs) to georeference complex locality descriptions automatically, focusing on the biodiversity collections domain. We first identified effective prompting patterns, then fine-tuned an LLM using Quantized Low-Rank Adaptation (QLoRA) on biodiversity datasets from multiple regions and languages. Our approach outperforms existing baselines with an average, across datasets, of 65% of records within a 10 km radius, for a fixed amount of training data. The best results (New York state) were 85% within 10km and 67% within 1km. The selected LLM performs well for lengthy, complex descriptions, highlighting its potential for georeferencing intricate locality descriptions.

