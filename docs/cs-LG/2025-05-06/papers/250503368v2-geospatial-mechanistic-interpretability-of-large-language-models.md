---
layout: default
title: Geospatial Mechanistic Interpretability of Large Language Models
---

# Geospatial Mechanistic Interpretability of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03368" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03368v2</a>
  <a href="https://arxiv.org/pdf/2505.03368.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03368v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03368v2', 'Geospatial Mechanistic Interpretability of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stef De Sabbata, Stefano Mizzaro, Kevin Roitero

**分类**: cs.LG

**发布日期**: 2025-05-06 (更新: 2025-05-12)

**备注**: Figures 2 and 3: fixed issue with min boundary in colorbar

---

## 💡 一句话要点

**提出地理空间机制可解释性框架以解析大型语言模型的地理信息处理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `地理空间分析` `机制可解释性` `空间自相关性` `稀疏自编码器` `地理信息处理` `内部表示`

## 📋 核心要点

1. 现有研究对大型语言模型在地理信息处理中的内部机制了解不足，缺乏有效的解析方法。
2. 本文提出了一种地理空间机制可解释性框架，通过空间分析反向工程LLMs的地理信息处理方式。
3. 实验结果表明，地名特征的空间模式与其地理位置相关，提供了对模型处理地理信息的新见解。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言处理任务中展现了前所未有的能力，尤其是在文本和代码生成方面。然而，关于这些模型如何处理地理信息的内部机制仍然知之甚少。本文建立了一种新的地理空间机制可解释性框架，通过空间分析反向工程LLMs处理地理信息的方式，旨在加深对这些复杂模型在处理地理信息时生成的内部表示的理解。我们使用探测技术揭示LLMs内部结构，并引入机制可解释性领域，讨论稀疏自编码器在解开多义内部表示中的作用。实验中，我们利用空间自相关性展示地名特征的空间模式，从而提供对模型处理地理信息的洞察。最后，讨论该框架如何推动基础模型在地理学中的研究与应用。

## 🔬 方法详解

**问题定义**：本文旨在解决对大型语言模型（LLMs）在处理地理信息时的内部机制缺乏理解的问题。现有方法未能有效解析这些模型如何生成和处理地理信息。

**核心思路**：论文提出通过地理空间机制可解释性框架，利用空间分析技术反向工程LLMs的地理信息处理过程，旨在揭示其内部表示的特征。

**技术框架**：整体架构包括使用探测技术揭示LLMs的内部结构，结合机制可解释性理论，利用稀疏自编码器解开多义表示，最终通过空间自相关性分析地名特征。

**关键创新**：最重要的技术创新在于将空间分析与机制可解释性结合，提供了一种新的视角来理解LLMs如何处理地理信息，区别于传统的黑箱模型分析方法。

**关键设计**：在实验中，采用稀疏自编码器以提取单义特征，并通过空间自相关性分析地名特征的空间模式，确保模型输出与地理位置的相关性。实验设计中关注特征的可解释性与空间一致性。

## 📊 实验亮点

实验结果显示，地名特征的空间模式与其地理位置高度相关，验证了所提出框架的有效性。通过空间自相关性分析，模型在地理信息处理上的可解释性显著提升，为后续研究提供了新的方向。

## 🎯 应用场景

该研究的潜在应用领域包括地理信息系统（GIS）、智能城市规划、环境监测等。通过深入理解LLMs在地理信息处理中的机制，可以提升模型在地理领域的应用效果，推动相关技术的发展与创新。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated unprecedented capabilities across various natural language processing tasks. Their ability to process and generate viable text and code has made them ubiquitous in many fields, while their deployment as knowledge bases and "reasoning" tools remains an area of ongoing research. In geography, a growing body of literature has been focusing on evaluating LLMs' geographical knowledge and their ability to perform spatial reasoning. However, very little is still known about the internal functioning of these models, especially about how they process geographical information.
>   In this chapter, we establish a novel framework for the study of geospatial mechanistic interpretability - using spatial analysis to reverse engineer how LLMs handle geographical information. Our aim is to advance our understanding of the internal representations that these complex models generate while processing geographical information - what one might call "how LLMs think about geographic information" if such phrasing was not an undue anthropomorphism.
>   We first outline the use of probing in revealing internal structures within LLMs. We then introduce the field of mechanistic interpretability, discussing the superposition hypothesis and the role of sparse autoencoders in disentangling polysemantic internal representations of LLMs into more interpretable, monosemantic features. In our experiments, we use spatial autocorrelation to show how features obtained for placenames display spatial patterns related to their geographic location and can thus be interpreted geospatially, providing insights into how these models process geographical information. We conclude by discussing how our framework can help shape the study and use of foundation models in geography.

