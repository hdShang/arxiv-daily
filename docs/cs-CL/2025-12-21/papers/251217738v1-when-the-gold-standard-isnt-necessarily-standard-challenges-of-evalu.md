---
layout: default
title: "When the Gold Standard isn't Necessarily Standard: Challenges of Evaluating the Translation of User-Generated Content"
---

# When the Gold Standard isn't Necessarily Standard: Challenges of Evaluating the Translation of User-Generated Content

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17738" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17738v1</a>
  <a href="https://arxiv.org/pdf/2512.17738.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17738v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17738v1', 'When the Gold Standard isn\'t Necessarily Standard: Challenges of Evaluating the Translation of User-Generated Content')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lydia Nishimwe, Benoît Sagot, Rachel Bawden

**分类**: cs.CL

**发布日期**: 2025-12-19

**备注**: 10 pages, 19 pages with references and appendices

---

## 💡 一句话要点

**针对用户生成内容翻译评估标准不统一问题，提出一套非标准现象分类和翻译行为规范。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户生成内容翻译` `非标准语言处理` `机器翻译评估` `大型语言模型` `翻译指南`

## 📋 核心要点

1. 现有UGC翻译评估缺乏统一标准，不同数据集对非标准语言的处理方式各异，导致评估结果不稳定。
2. 论文提出一套包含非标准现象分类和翻译行为规范的体系，旨在弥合UGC翻译评估标准上的差异。
3. 实验表明，大型语言模型的翻译质量受翻译指令影响显著，与数据集指南对齐的指令能提升翻译效果。

## 📝 摘要（中文）

用户生成内容(UGC)的特点是频繁使用非标准语言，包括拼写错误、俚语、字符重复和表情符号等表达方式。这使得UGC翻译的评估极具挑战性：何为“好的”翻译取决于输出中期望的标准程度。为了探讨这一点，我们研究了四个UGC数据集的人工翻译指南，并推导出包含十二种非标准现象和五种翻译行为（标准化、复制、转移、省略、审查）的分类体系。我们的分析揭示了UGC处理方式的显著差异，导致参考翻译中存在标准程度的差异。通过对大型语言模型(LLM)的案例研究，我们表明翻译分数对带有明确UGC翻译指令的提示非常敏感，并且当这些指令与数据集的指南一致时，翻译分数会提高。我们认为，当保持UGC风格很重要时，公平的评估需要模型和指标都了解翻译指南。最后，我们呼吁在数据集创建过程中制定明确的指南，并为UGC翻译开发可控的、感知指南的评估框架。

## 🔬 方法详解

**问题定义**：现有用户生成内容（UGC）翻译评估面临的主要问题是缺乏统一的标准。不同数据集在处理UGC中常见的非标准语言现象（如拼写错误、俚语、表情符号等）时，采取了不同的翻译策略，导致评估结果难以比较，且无法准确反映翻译模型的真实性能。现有方法未能充分考虑UGC的特殊性，简单地沿用标准文本的评估方法，无法满足实际需求。

**核心思路**：论文的核心思路是正视UGC的非标准性，并将其纳入翻译评估的考量范围。通过分析现有UGC数据集的翻译指南，归纳出常见的非标准现象和对应的翻译行为，从而建立一套更贴合UGC特点的评估体系。这种方法强调了翻译策略的选择应与数据集的翻译指南相一致，以确保评估的公平性和有效性。

**技术框架**：论文的技术框架主要包含以下几个步骤：1) 收集并分析四个UGC数据集的人工翻译指南；2) 基于分析结果，构建一个包含十二种非标准现象和五种翻译行为（NORMALISE, COPY, TRANSFER, OMIT, CENSOR）的分类体系；3) 通过案例研究，评估大型语言模型在不同翻译指令下的表现；4) 分析评估结果，并提出改进UGC翻译评估的建议。

**关键创新**：论文的关键创新在于提出了一个针对UGC翻译的非标准现象和翻译行为的分类体系。该体系能够帮助研究人员更好地理解UGC的特殊性，并指导翻译模型的训练和评估。此外，论文还强调了翻译指令对模型性能的影响，并呼吁在数据集创建过程中制定明确的翻译指南。

**关键设计**：论文的关键设计包括：1) 对四个UGC数据集的翻译指南进行深入分析，提取出共性的非标准现象和翻译行为；2) 构建了一个包含十二种非标准现象（如拼写错误、语法错误、俚语、表情符号等）和五种翻译行为（标准化、复制、转移、省略、审查）的分类体系；3) 设计了一系列实验，通过改变翻译指令，评估大型语言模型在不同设置下的翻译性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17738v1/figures/ugc-translation-example.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17738v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17738v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，大型语言模型在UGC翻译任务中的表现对翻译指令非常敏感。当翻译指令与数据集的翻译指南对齐时，翻译质量显著提升。这强调了在UGC翻译评估中，必须考虑翻译指令和数据集指南的一致性，以确保评估的公平性和有效性。具体性能提升幅度未知，但结论明确。

## 🎯 应用场景

该研究成果可应用于提升用户生成内容的机器翻译质量和评估标准。在社交媒体、在线论坛等领域，能够更准确地翻译非标准语言，保留原文风格，并为数据集构建和模型训练提供指导，最终提升用户体验和跨文化交流效率。未来，可进一步开发可控的、感知指南的UGC翻译评估框架。

## 📄 摘要（原文）

> User-generated content (UGC) is characterised by frequent use of non-standard language, from spelling errors to expressive choices such as slang, character repetitions, and emojis. This makes evaluating UGC translation particularly challenging: what counts as a "good" translation depends on the level of standardness desired in the output. To explore this, we examine the human translation guidelines of four UGC datasets, and derive a taxonomy of twelve non-standard phenomena and five translation actions (NORMALISE, COPY, TRANSFER, OMIT, CENSOR). Our analysis reveals notable differences in how UGC is treated, resulting in a spectrum of standardness in reference translations. Through a case study on large language models (LLMs), we show that translation scores are highly sensitive to prompts with explicit translation instructions for UGC, and that they improve when these align with the dataset's guidelines. We argue that when preserving UGC style is important, fair evaluation requires both models and metrics to be aware of translation guidelines. Finally, we call for clear guidelines during dataset creation and for the development of controllable, guideline-aware evaluation frameworks for UGC translation.

