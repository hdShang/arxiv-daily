---
layout: default
title: "Yet another algorithmic bias: A Discursive Analysis of Large Language Models Reinforcing Dominant Discourses on Gender and Race"
---

# Yet another algorithmic bias: A Discursive Analysis of Large Language Models Reinforcing Dominant Discourses on Gender and Race

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10304" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10304v1</a>
  <a href="https://arxiv.org/pdf/2508.10304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10304v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10304v1', 'Yet another algorithmic bias: A Discursive Analysis of Large Language Models Reinforcing Dominant Discourses on Gender and Race')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gustavo Bonil, Simone Hashiguti, Jhessica Silva, João Gondim, Helena Maia, Nádia Silva, Helio Pedrini, Sandra Avila

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-14

**备注**: 29 pages, 3 figures

---

## 💡 一句话要点

**提出定性框架以解决大语言模型中的性别与种族偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `算法偏见` `定性分析` `性别偏见` `种族偏见` `话语分析` `人工智能伦理`

## 📋 核心要点

1. 现有的偏见检测方法主要依赖定量分析，无法捕捉到自然语言中偏见的细微表现。
2. 本研究提出了一种定性的话语分析框架，通过手动分析生成的文本，深入探讨性别和种族偏见。
3. 实验结果表明，黑人女性和白人女性在语言模型生成的故事中被描绘的方式存在显著差异，反映了固化的社会话语。

## 📝 摘要（中文）

随着人工智能的发展，大型语言模型（LLMs）在多个领域中得到广泛应用。然而，这些模型可能会重现偏见，如歧视和种族化，并维持霸权话语。现有的偏见检测方法主要依赖定量的自动化手段，往往忽视了偏见在自然语言中细微的表现方式。本研究提出了一种定性的话语框架，以补充这些方法。通过对生成的短篇故事进行手动分析，我们探讨了性别和种族偏见。结果显示，黑人女性常被描绘为与祖先和抵抗相关，而白人女性则出现在自我发现的过程中。这些模式反映了语言模型如何复制固化的话语表现，强化了本质化和社会流动性的缺失。我们的研究强调了算法的意识形态功能，对人工智能的伦理使用和开发具有重要意义。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型中性别与种族偏见的再现问题。现有方法主要依赖定量分析，无法深入理解偏见在语言中的细微表现。

**核心思路**：本研究提出了一种定性的话语分析框架，通过对生成文本的手动分析，揭示偏见的具体表现形式，以帮助开发者和用户更好地识别和缓解这些偏见。

**技术框架**：研究采用定性分析方法，首先收集由大型语言模型生成的短篇故事，然后对这些故事进行逐篇分析，重点关注性别和种族的表现。

**关键创新**：本研究的主要创新在于引入定性分析作为补充手段，强调了对语言模型输出的深度理解，区别于传统的定量偏见检测方法。

**关键设计**：在分析过程中，研究者关注文本中的角色描绘、情节发展和语言使用等方面，识别出黑人女性与白人女性在故事中的不同表现，揭示了潜在的社会偏见。

## 📊 实验亮点

实验结果显示，黑人女性在生成故事中常常被描绘为与祖先和抵抗相关，而白人女性则更倾向于自我发现的主题。这种表现反映了语言模型在生成内容时的偏见，且在尝试纠正时，模型提供的修改往往表面化，未能有效消除问题。

## 🎯 应用场景

该研究的潜在应用领域包括人工智能伦理、语言模型的开发与评估、以及社会科学研究。通过提供定性分析框架，开发者可以更有效地识别和缓解模型中的偏见，从而促进更公平和包容的AI应用。未来，这种方法可能推动跨学科的合作，提升AI系统的社会责任感。

## 📄 摘要（原文）

> With the advance of Artificial Intelligence (AI), Large Language Models (LLMs) have gained prominence and been applied in diverse contexts. As they evolve into more sophisticated versions, it is essential to assess whether they reproduce biases, such as discrimination and racialization, while maintaining hegemonic discourses. Current bias detection approaches rely mostly on quantitative, automated methods, which often overlook the nuanced ways in which biases emerge in natural language. This study proposes a qualitative, discursive framework to complement such methods. Through manual analysis of LLM-generated short stories featuring Black and white women, we investigate gender and racial biases. We contend that qualitative methods such as the one proposed here are fundamental to help both developers and users identify the precise ways in which biases manifest in LLM outputs, thus enabling better conditions to mitigate them. Results show that Black women are portrayed as tied to ancestry and resistance, while white women appear in self-discovery processes. These patterns reflect how language models replicate crystalized discursive representations, reinforcing essentialization and a sense of social immobility. When prompted to correct biases, models offered superficial revisions that maintained problematic meanings, revealing limitations in fostering inclusive narratives. Our results demonstrate the ideological functioning of algorithms and have significant implications for the ethical use and development of AI. The study reinforces the need for critical, interdisciplinary approaches to AI design and deployment, addressing how LLM-generated discourses reflect and perpetuate inequalities.

