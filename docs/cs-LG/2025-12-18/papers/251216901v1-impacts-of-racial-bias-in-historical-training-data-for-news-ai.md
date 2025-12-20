---
layout: default
title: Impacts of Racial Bias in Historical Training Data for News AI
---

# Impacts of Racial Bias in Historical Training Data for News AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16901" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16901v1</a>
  <a href="https://arxiv.org/pdf/2512.16901.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16901v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16901v1', 'Impacts of Racial Bias in Historical Training Data for News AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rahul Bhargava, Malene Hornstrup Jespersen, Emily Boardman Ndulue, Vivica Dsouza

**分类**: cs.LG, cs.AI, cs.CL, cs.CY

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**揭示新闻AI中历史数据偏见：以纽约时报语料库为例，分析种族标签的影响。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `新闻AI` `偏见分析` `历史数据` `可解释AI` `种族偏见`

## 📋 核心要点

1. 现有新闻AI模型训练于历史数据，可能内嵌过时的偏见和刻板印象，导致不公平或不准确的结果。
2. 该研究通过分析《纽约时报》语料库训练的多标签分类器，揭示了“黑人”标签的潜在偏见及其影响。
3. 实验表明该标签在某些情况下充当“种族主义检测器”，但在现代反歧视事件中表现不佳，突显了偏见的复杂性。

## 📝 摘要（中文）

人工智能技术已迅速应用于涉及大型文本语料库的商业和研究应用，包括计算新闻研究和新闻编辑室环境。这些模型在来自各种来源的现有数据上进行训练，可以被概念化为编码了几十年前的态度和刻板印象的历史产物。本文研究了一个这样的例子，该例子在广泛使用的《纽约时报》注释语料库上训练，以创建一个多标签分类器。我们在研究环境中的使用浮现了令人担忧的“黑人”主题标签。通过定量和定性的方法，我们调查了该标签在训练语料库中的使用情况，它可能在训练的分类器中编码了哪些概念，以及这些概念如何影响我们的模型使用。通过应用可解释的人工智能方法，我们发现“黑人”标签在一定程度上充当了针对一些少数群体的通用“种族主义检测器”。然而，它在现代例子（如COVID-19时代的反亚裔仇恨故事和关于“黑人的命也是命”运动的报道）上的表现不符合预期。这个调查模型中嵌入偏见的案例研究揭示了新闻编辑室环境中类似的应用如何导致意想不到的输出，这些输出可能会影响任何大型语言模型的各种潜在用途——故事发现、受众定位、摘要等。这为新闻编辑室暴露出的根本矛盾是，如何在采用人工智能支持的工作流程工具的同时，降低在新闻报道中重现历史偏见的风险。

## 🔬 方法详解

**问题定义**：论文旨在解决新闻AI模型中由于历史训练数据偏差而导致的不公平或不准确的问题。现有方法未能充分识别和减轻这些偏差，导致模型在处理涉及种族、性别等敏感话题时可能产生歧视性结果。特别是，论文关注的是《纽约时报》注释语料库中“黑人”标签的使用，以及该标签可能在模型中编码的潜在偏见。

**核心思路**：论文的核心思路是通过定量和定性分析相结合的方式，深入挖掘训练数据中存在的偏见，并评估这些偏见对模型行为的影响。通过可解释AI方法，揭示模型如何使用“黑人”标签，以及该标签在不同情境下的表现。这种方法旨在帮助新闻编辑室等机构更好地理解和减轻AI模型中的偏见。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 数据分析：对《纽约时报》注释语料库中“黑人”标签的使用情况进行统计分析，了解其在不同时间段和主题下的分布。2) 模型训练：使用该语料库训练一个多标签分类器，用于预测新闻文章的主题标签。3) 可解释AI：应用可解释AI方法（具体方法未知），分析模型如何使用“黑人”标签进行预测，并识别与该标签相关的关键特征。4) 案例研究：选择COVID-19时代的反亚裔仇恨故事和关于“黑人的命也是命”运动的报道作为案例，评估模型在这些现代情境下的表现。

**关键创新**：该研究的关键创新在于将可解释AI方法应用于新闻AI模型的偏见分析，从而能够更深入地理解模型内部的决策过程。通过结合定量和定性分析，揭示了“黑人”标签在不同情境下的复杂表现，并指出了模型在处理现代反歧视事件时的局限性。这种方法为新闻编辑室等机构提供了一种评估和减轻AI模型偏见的有效途径。

**关键设计**：论文中没有明确说明关键的参数设置、损失函数、网络结构等技术细节。但是，可以推断，模型训练可能使用了常见的文本分类算法，例如基于Transformer的模型。可解释AI方法的选择和应用是关键，但具体方法未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16901v1/figures/fig1-blacks-use.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16901v1/figures/fig2-boxplots.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16901v1/figures/fig3-terms-grid.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

研究发现，《纽约时报》语料库训练的AI模型中，“黑人”标签在某些情况下充当“种族主义检测器”，但对COVID-19时代的反亚裔仇恨故事和“黑人的命也是命”运动等现代案例表现不佳。这表明历史数据中的偏见可能导致模型在处理现代问题时出现偏差。

## 🎯 应用场景

该研究成果可应用于新闻编辑室、内容推荐系统、情感分析等领域，帮助识别和减轻AI模型中的偏见，提高模型的公平性和准确性。通过理解历史数据中的偏见，可以避免在新闻报道、内容推荐等方面重现这些偏见，从而促进更加公正和包容的社会。

## 📄 摘要（原文）

> AI technologies have rapidly moved into business and research applications that involve large text corpora, including computational journalism research and newsroom settings. These models, trained on extant data from various sources, can be conceptualized as historical artifacts that encode decades-old attitudes and stereotypes. This paper investigates one such example trained on the broadly-used New York Times Annotated Corpus to create a multi-label classifier. Our use in research settings surfaced the concerning "blacks" thematic topic label. Through quantitative and qualitative means we investigate this label's use in the training corpus, what concepts it might be encoding in the trained classifier, and how those concepts impact our model use. Via the application of explainable AI methods, we find that the "blacks" label operates partially as a general "racism detector" across some minoritized groups. However, it performs poorly against expectations on modern examples such as COVID-19 era anti-Asian hate stories, and reporting on the Black Lives Matter movement. This case study of interrogating embedded biases in a model reveals how similar applications in newsroom settings can lead to unexpected outputs that could impact a wide variety of potential uses of any large language model-story discovery, audience targeting, summarization, etc. The fundamental tension this exposes for newsrooms is how to adopt AI-enabled workflow tools while reducing the risk of reproducing historical biases in news coverage.

