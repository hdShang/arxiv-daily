---
layout: default
title: The Moralization Corpus: Frame-Based Annotation and Analysis of Moralizing Speech Acts across Diverse Text Genres
---

# The Moralization Corpus: Frame-Based Annotation and Analysis of Moralizing Speech Acts across Diverse Text Genres

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15248" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15248v1</a>
  <a href="https://arxiv.org/pdf/2512.15248.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15248v1" onclick="toggleFavorite(this, '2512.15248v1', 'The Moralization Corpus: Frame-Based Annotation and Analysis of Moralizing Speech Acts across Diverse Text Genres')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maria Becker, Mirko Sommer, Lars Tapken, Yi Wan Teh, Bruno Brocai

**分类**: cs.CL

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**构建道德化语料库，用于分析跨文本类型的道德化言语行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `道德化论证` `语料库构建` `框架语义学` `大型语言模型` `自然语言处理` `道德推理` `文本分析`

## 📋 核心要点

1. 现有方法缺乏对道德化论证的深入分析，道德化论证在说服性交流中扮演重要角色。
2. 论文提出基于框架的标注方案，捕捉道德价值、诉求和语篇主角等道德化要素。
3. 构建了多领域德语语料库，并评估了大型语言模型在道德化检测和成分提取方面的性能。

## 📝 摘要（中文）

本文提出了道德化语料库，这是一个新的多领域数据集，旨在分析论证性语篇中道德价值的策略性使用方式。道德化是一种具有语用复杂性且通常是隐性的说服性交流形式，对人工标注和自然语言处理系统都提出了重大挑战。我们开发了一种基于框架的标注方案，该方案捕捉了道德化的构成要素——道德价值、诉求和语篇主角——并将其应用于包括政治辩论、新闻文章和在线讨论在内的各种德语文本。该语料库能够对跨交流形式和领域的道德化语言进行细粒度分析。我们还评估了多个大型语言模型（LLM）在不同提示条件下进行道德化检测和道德化成分提取的任务，并将其与人工标注进行比较，以研究自动和手动分析道德化所面临的挑战。结果表明，详细的提示指令比少样本或基于解释的提示具有更大的效果，并且道德化仍然是一项高度主观和上下文敏感的任务。我们发布所有数据、标注指南和代码，以促进未来关于道德语篇和自然语言处理中道德推理的跨学科研究。

## 🔬 方法详解

**问题定义**：论文旨在解决道德化论证识别与分析的问题。现有方法缺乏对道德化论证的细粒度分析，难以捕捉道德论证中蕴含的道德价值、诉求和论证主体等关键信息。道德化论证通常具有隐蔽性和上下文依赖性，给自动识别带来了挑战。

**核心思路**：论文的核心思路是构建一个带有细粒度标注的道德化语料库，并利用该语料库训练和评估大型语言模型在道德化论证识别和成分提取方面的能力。通过框架语义学的方法，将道德化论证分解为道德价值、诉求和论证主体等要素，从而实现对道德化论证的深入理解。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 定义基于框架的标注方案，明确道德价值、诉求和论证主体的概念和标注规范；2) 构建多领域德语语料库，包括政治辩论、新闻文章和在线讨论等多种文本类型；3) 采用人工标注的方式，对语料库中的道德化论证进行标注；4) 利用标注好的语料库，训练和评估大型语言模型在道德化检测和成分提取方面的性能；5) 分析实验结果，探讨不同提示策略对模型性能的影响，并与人工标注结果进行对比。

**关键创新**：论文的关键创新在于：1) 提出了一个基于框架的道德化论证标注方案，能够捕捉道德化论证中的关键要素；2) 构建了一个多领域德语道德化语料库，为相关研究提供了数据基础；3) 评估了大型语言模型在道德化检测和成分提取方面的性能，并探讨了不同提示策略的影响。

**关键设计**：在实验中，研究者采用了多种提示策略，包括详细的提示指令、少样本学习和基于解释的提示。他们还比较了不同大型语言模型在道德化检测和成分提取方面的性能。此外，研究者还分析了人工标注结果，探讨了道德化论证的主观性和上下文依赖性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15248v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15248v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15248v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，详细的提示指令对大型语言模型在道德化检测和成分提取方面的性能有显著提升，效果优于少样本学习和基于解释的提示。然而，道德化仍然是一项高度主观和上下文敏感的任务，大型语言模型的性能与人工标注之间仍存在差距。

## 🎯 应用场景

该研究成果可应用于政治观点分析、舆情监控、虚假信息检测等领域。通过识别和分析道德化论证，可以更好地理解社会舆论的形成和演变，从而为政策制定和社会治理提供参考。此外，该研究还可以促进自然语言处理领域对道德推理的研究。

## 📄 摘要（原文）

> Moralizations - arguments that invoke moral values to justify demands or positions - are a yet underexplored form of persuasive communication. We present the Moralization Corpus, a novel multi-genre dataset designed to analyze how moral values are strategically used in argumentative discourse. Moralizations are pragmatically complex and often implicit, posing significant challenges for both human annotators and NLP systems. We develop a frame-based annotation scheme that captures the constitutive elements of moralizations - moral values, demands, and discourse protagonists - and apply it to a diverse set of German texts, including political debates, news articles, and online discussions. The corpus enables fine-grained analysis of moralizing language across communicative formats and domains. We further evaluate several large language models (LLMs) under varied prompting conditions for the task of moralization detection and moralization component extraction and compare it to human annotations in order to investigate the challenges of automatic and manual analysis of moralizations. Results show that detailed prompt instructions has a greater effect than few-shot or explanation-based prompting, and that moralization remains a highly subjective and context-sensitive task. We release all data, annotation guidelines, and code to foster future interdisciplinary research on moral discourse and moral reasoning in NLP.

