---
layout: default
title: FiNERweb: Datasets and Artifacts for Scalable Multilingual Named Entity Recognition
---

# FiNERweb: Datasets and Artifacts for Scalable Multilingual Named Entity Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13884" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13884</a>
  <a href="https://arxiv.org/pdf/2512.13884.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13884" onclick="toggleFavorite(this, '2512.13884', 'FiNERweb: Datasets and Artifacts for Scalable Multilingual Named Entity Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonas Golde, Patrick Haller, Alan Akbik

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**FiNERweb：用于可扩展多语言命名实体识别的数据集与工具**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言NER` `命名实体识别` `数据集构建` `Teacher-Student学习` `LLM标注`

## 📋 核心要点

1. 现有的大型语言模型（LLM）可以提供有效的合成监督，但相关数据集通常是更广泛实验的副产品，缺乏系统性和可重用性。
2. FiNERweb通过训练回归模型识别NER相关段落，并利用多语言LLM进行标注，从而大规模生成多语言NER数据集。
3. 实验表明，FiNERweb训练的模型在zero-shot迁移学习中表现出色，且标注质量高，为多语言NER提供了有价值的资源。

## 📝 摘要（中文）

本文介绍FiNERweb，一个数据集创建流程，将teacher-student范式扩展到91种语言和25种文字。该方法基于FineWeb-Edu，训练回归模型以识别与NER相关的段落，并使用多语言LLM对其进行标注，从而产生约22.5万个段落，包含23.5万个不同的实体标签。实验表明，回归模型实现了超过84的F1值，并且在FiNERweb上训练的模型在英语、泰语和斯瓦希里语的zero-shot迁移设置中获得了可比或更高的性能，尽管训练数据比强基线少19倍。此外，我们使用LLM-as-a-judge评估标注质量，观察到保真度（5分制为3.99）和完整性（5分制为4.05）均持续获得高分，表明标注可靠且信息丰富。我们发布了带有英语标签和相应目标语言翻译标签的数据集，因为我们观察到，使用目标语言标签而不是英语标签进行评估时，当前最先进模型的性能会下降0.02到0.09 F1。为了促进更有效的多语言命名实体识别的student-teacher训练，我们向研究社区发布FiNERweb以及所有随附的工具。

## 🔬 方法详解

**问题定义**：论文旨在解决多语言命名实体识别（NER）中缺乏大规模、高质量训练数据的问题。现有的方法要么依赖于人工标注，成本高昂且难以扩展到多种语言，要么依赖于LLM生成的数据，但这些数据通常是副产品，缺乏系统性和质量保证。

**核心思路**：论文的核心思路是利用teacher-student范式，首先训练一个回归模型来识别NER相关的文本段落（teacher），然后使用多语言LLM对这些段落进行标注（student）。这种方法可以高效地生成大规模、多语言的NER数据集，同时保证标注质量。

**技术框架**：FiNERweb的整体流程包括以下几个主要阶段：1) 基于FineWeb-Edu数据集，训练一个回归模型，用于预测文本段落与NER任务的相关性。2) 使用该回归模型从大规模文本语料库中筛选出NER相关的段落。3) 使用多语言LLM对筛选出的段落进行命名实体标注。4) 对标注结果进行质量评估，并发布数据集。

**关键创新**：FiNERweb的关键创新在于其可扩展性。通过训练回归模型来预筛选NER相关的段落，可以显著减少LLM需要处理的文本量，从而降低标注成本，并使其能够扩展到91种语言和25种文字。此外，论文还使用了LLM-as-a-judge来评估标注质量，确保数据集的可靠性。

**关键设计**：回归模型使用F1值作为评估指标，目标是最大化NER相关段落的识别精度。LLM标注过程中，采用了多种prompt工程技术，以提高标注的准确性和一致性。数据集发布时，同时提供了英语标签和目标语言翻译标签，以便研究人员进行更全面的评估。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13884/images/finerweb_approach.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13884/images/preference_classifier_cm.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13884/images/typescript_stacked_normalized_horizontal.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在FiNERweb上训练的模型在英语、泰语和斯瓦希里语的zero-shot迁移设置中获得了可比或更高的性能，尽管训练数据比强基线少19倍。此外，使用LLM-as-a-judge评估标注质量，保真度达到3.99/5，完整性达到4.05/5，表明标注质量高。

## 🎯 应用场景

FiNERweb数据集可用于训练多语言NER模型，应用于跨语言信息检索、机器翻译、多语言知识图谱构建等领域。该数据集的发布将促进多语言自然语言处理技术的发展，并为构建更智能、更全球化的AI系统提供支持。

## 📄 摘要（原文）

> Recent multilingual named entity recognition (NER) work has shown that large language models (LLMs) can provide effective synthetic supervision, yet such datasets have mostly appeared as by-products of broader experiments rather than as systematic, reusable resources. We introduce FiNERweb, a dataset-creation pipeline that scales the teacher-student paradigm to 91 languages and 25 scripts. Building on FineWeb-Edu, our approach trains regression models to identify NER-relevant passages and annotates them with multilingual LLMs, resulting in about 225k passages with 235k distinct entity labels. Our experiments show that the regression model achieves more than 84 F1, and that models trained on FiNERweb obtain comparable or improved performance in zero shot transfer settings on English, Thai, and Swahili, despite being trained on 19x less data than strong baselines. In addition, we assess annotation quality using LLM-as-a-judge and observe consistently high scores for both faithfulness (3.99 out of 5) and completeness (4.05 out of 5), indicating reliable and informative annotations. Further, we release the dataset with both English labels and translated label sets in the respective target languages because we observe that the performance of current state-of-the-art models drops by 0.02 to 0.09 F1 when evaluated using target language labels instead of English ones. We release FiNERweb together with all accompanying artifacts to the research community in order to facilitate more effective student-teacher training for multilingual named entity recognition.

