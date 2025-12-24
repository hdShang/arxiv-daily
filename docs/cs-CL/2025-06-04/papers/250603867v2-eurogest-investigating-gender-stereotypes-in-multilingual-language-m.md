---
layout: default
title: "EuroGEST: Investigating gender stereotypes in multilingual language models"
---

# EuroGEST: Investigating gender stereotypes in multilingual language models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03867" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03867v2</a>
  <a href="https://arxiv.org/pdf/2506.03867.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03867v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03867v2', 'EuroGEST: Investigating gender stereotypes in multilingual language models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jacqueline Rowe, Mateusz Klimaszewski, Liane Guillou, Shannon Vallor, Alexandra Birch

**分类**: cs.CL

**发布日期**: 2025-06-04 (更新: 2025-09-20)

**备注**: 9 pages, 5 figures, 1 table. To be published in the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025)

---

## 💡 一句话要点

**提出EuroGEST以评估多语言模型中的性别刻板印象**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `性别偏见` `多语言模型` `数据集` `刻板印象` `自然语言处理` `公平性研究` `机器学习`

## 📋 核心要点

1. 现有的性别偏见基准主要集中在英语，缺乏对多语言模型的全面评估。
2. 论文提出EuroGEST数据集，旨在跨29种欧洲语言测量性别刻板印象，采用翻译工具和质量评估方法生成数据。
3. 实验结果表明，所有模型中女性被刻板印象为“美丽”，男性为“领导者”，且较大模型更强烈地编码这些刻板印象。

## 📝 摘要（中文）

大型语言模型越来越多地支持多种语言，但现有的性别偏见基准大多集中于英语。我们引入了EuroGEST，一个旨在衡量多语言模型中性别刻板印象推理的数据集，涵盖英语及29种欧洲语言。EuroGEST基于现有的专家知情基准，扩展了16种性别刻板印象，并采用翻译工具、质量估计指标和形态学启发式方法进行数据生成。人类评估确认我们的数据生成方法在翻译和性别标签的准确性上表现良好。我们使用EuroGEST评估了来自六个模型家族的24个多语言模型，结果显示所有模型在所有语言中最强的刻板印象是女性被认为“美丽”、“富有同情心”和“整洁”，男性则被认为是“领导者”、“强壮、坚韧”和“专业”。我们还发现，较大的模型更强烈地编码性别刻板印象，而指令微调并不总是能有效减少性别刻板印象。我们的研究强调了对大型语言模型进行更多多语言公平性研究的必要性，并提供了可扩展的方法和资源来审计跨语言的性别偏见。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有性别偏见基准缺乏多语言评估的问题，尤其是针对非英语语言的刻板印象研究不足。

**核心思路**：通过构建EuroGEST数据集，利用翻译工具和质量评估方法，扩展现有的性别刻板印象基准，以便在多语言环境中进行评估。

**技术框架**：EuroGEST的构建包括数据生成、翻译质量评估和性别标签确认三个主要模块。首先，通过翻译工具生成多语言数据，然后使用质量估计指标评估翻译的准确性，最后进行人类评估以确认性别标签的有效性。

**关键创新**：EuroGEST的创新之处在于其跨29种语言的性别刻板印象评估能力，填补了现有研究的空白，并提供了一种可扩展的方法来审计多语言模型中的性别偏见。

**关键设计**：在数据生成过程中，采用了形态学启发式方法来确保性别标签的准确性，并通过人类评估验证了翻译的质量和性别标签的可靠性。

## 📊 实验亮点

实验结果显示，所有评估的多语言模型中，女性的刻板印象主要集中在“美丽”、“富有同情心”和“整洁”，而男性则被视为“领导者”、“强壮、坚韧”和“专业”。此外，较大的模型在性别刻板印象的编码上表现得更为明显，指令微调未能有效减少这些刻板印象。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、社会科学研究和人工智能伦理。通过提供一个多语言的性别偏见评估工具，研究者和开发者可以更好地理解和改进语言模型的公平性，推动多语言环境下的社会公正与平等。

## 📄 摘要（原文）

> Large language models increasingly support multiple languages, yet most benchmarks for gender bias remain English-centric. We introduce EuroGEST, a dataset designed to measure gender-stereotypical reasoning in LLMs across English and 29 European languages. EuroGEST builds on an existing expert-informed benchmark covering 16 gender stereotypes, expanded in this work using translation tools, quality estimation metrics, and morphological heuristics. Human evaluations confirm that our data generation method results in high accuracy of both translations and gender labels across languages. We use EuroGEST to evaluate 24 multilingual language models from six model families, demonstrating that the strongest stereotypes in all models across all languages are that women are 'beautiful', 'empathetic' and 'neat' and men are 'leaders', 'strong, tough' and 'professional'. We also show that larger models encode gendered stereotypes more strongly and that instruction finetuning does not consistently reduce gendered stereotypes. Our work highlights the need for more multilingual studies of fairness in LLMs and offers scalable methods and resources to audit gender bias across languages.

