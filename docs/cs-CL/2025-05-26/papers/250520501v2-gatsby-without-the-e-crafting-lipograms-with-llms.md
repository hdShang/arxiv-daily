---
layout: default
title: Gatsby Without the 'E': Crafting Lipograms with LLMs
---

# Gatsby Without the 'E': Crafting Lipograms with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20501" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20501v2</a>
  <a href="https://arxiv.org/pdf/2505.20501.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20501v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20501v2', 'Gatsby Without the \'E\': Crafting Lipograms with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rohan Balasubramanian, Nitish Gokulakrishnan, Syeda Jannatus Saba, Steven Skiena

**分类**: cs.CL

**发布日期**: 2025-05-26 (更新: 2025-10-25)

---

## 💡 一句话要点

**利用大型语言模型生成无'e'的文本**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `限制性写作` `文本生成` `创造性表达` `自然语言处理`

## 📋 核心要点

1. 核心问题：现有的文本生成方法在处理限制性写作时面临挑战，尤其是在保持文本意义的同时排除特定字母。
2. 方法要点：本研究利用大型语言模型，通过同义词替换和生成模型等技术，实现了无字母'e'的文本生成。
3. 实验或效果：实验结果表明，排除常用字母对文本意义影响有限，但在更强的限制下，翻译保真度显著下降。

## 📝 摘要（中文）

本研究探讨了限制性写作形式——无字母的文本，特别是通过现代大型语言模型（LLMs）将F. Scott Fitzgerald的《了不起的盖茨比》转化为完全不含字母'e'的文本。我们尝试了多种技术，从同义词替换到增强的生成模型，展示了在排除高达3.6%的常用字母（包括字母'u'）时，文本意义的影响微乎其微，尽管在更强的限制下，翻译的保真度迅速下降。我们的工作揭示了在严格约束下，英语的灵活性和创造性。

## 🔬 方法详解

**问题定义**：本研究旨在解决如何在文本生成中排除特定字母（如'e'）的问题。现有方法在处理此类限制性写作时，往往无法有效保持文本的原意和流畅性。

**核心思路**：论文提出利用大型语言模型的强大生成能力，通过多种技术手段实现无字母的文本生成，探索语言在严格约束下的适应性和创造性。

**技术框架**：整体架构包括数据预处理、同义词替换、生成模型训练和后处理等多个阶段。主要模块包括基线方法和增强的生成模型，后者结合了束搜索和命名实体分析。

**关键创新**：最重要的技术创新在于将大型语言模型应用于限制性写作，展示了其在保持文本意义方面的灵活性，与传统方法相比，能够更好地适应语言的创造性表达。

**关键设计**：在模型训练中，采用了特定的损失函数以优化文本的流畅性和意义保留，同时设置了参数以控制生成文本的约束程度。

## 📊 实验亮点

实验结果显示，在排除高达3.6%的常用字母时，文本的意义保持基本不变，表明语言在严格约束下的适应性。相比基线方法，使用增强生成模型的文本质量显著提升，展示了大型语言模型在处理复杂语言任务中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括创意写作、游戏设计和教育等。通过探索语言的限制性表达，能够激发创作者的灵感，并为语言学习者提供新的练习方式，提升其语言能力和创造力。未来，类似的方法还可以扩展到其他语言和文本生成任务中。

## 📄 摘要（原文）

> Lipograms are a unique form of constrained writing where all occurrences of a particular letter are excluded from the text, typified by the novel Gadsby, which daringly avoids all usage of the letter 'e'. In this study, we explore the power of modern large language models (LLMs) by transforming the novel F. Scott Fitzgerald's The Great Gatsby into a fully 'e'-less text. We experimented with a range of techniques, from baseline methods like synonym replacement to sophisticated generative models enhanced with beam search and named entity analysis. We show that excluding up to 3.6% of the most common letters (up to the letter 'u') had minimal impact on the text's meaning, although translation fidelity rapidly and predictably decays with stronger lipogram constraints. Our work highlights the surprising flexibility of English under strict constraints, revealing just how adaptable and creative language can be.

