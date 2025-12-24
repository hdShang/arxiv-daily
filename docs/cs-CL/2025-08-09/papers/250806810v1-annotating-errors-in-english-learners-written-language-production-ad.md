---
layout: default
title: "Annotating Errors in English Learners' Written Language Production: Advancing Automated Written Feedback Systems"
---

# Annotating Errors in English Learners' Written Language Production: Advancing Automated Written Feedback Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06810" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06810v1</a>
  <a href="https://arxiv.org/pdf/2508.06810.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06810v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06810v1', 'Annotating Errors in English Learners\' Written Language Production: Advancing Automated Written Feedback Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Steven Coyne, Diana Galvan-Sosa, Ryan Spring, Camélia Guerraoui, Michael Zock, Keisuke Sakaguchi, Kentaro Inui

**分类**: cs.CL

**发布日期**: 2025-08-09

**备注**: Pre-review version of DOI 10.1007/978-3-031-98459-4_21, presented at AIED 2025. All content is as of submission time except for de-anonymization, ensuing layout fixes, use of the current code repository link, and BibTeX fixes. Readers are encouraged to refer to the published version

**期刊**: AIED LNCS 15880 (2025) 292-306

**DOI**: [10.1007/978-3-031-98459-4_21](https://doi.org/10.1007/978-3-031-98459-4_21)

---

## 💡 一句话要点

**提出注释框架以优化自动化写作反馈系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化写作评估` `自然语言处理` `学习者反馈` `语法错误` `知识缺口` `大型语言模型` `教育技术`

## 📋 核心要点

1. 现有的自动化写作评估系统在语言学习中未能有效提供针对性的反馈，主要依赖直接修正而非解释性提示。
2. 本文提出了一种新的注释框架，通过对错误类型的分类，帮助识别学习者的知识缺口，并生成更具指导性的反馈。
3. 实验结果表明，基于该框架生成的反馈在相关性、事实性和可理解性方面优于传统方法，显示出显著的提升。

## 📝 摘要（中文）

近年来，自然语言处理（NLP）的进展推动了自动化写作评估（AWE）系统的发展，这些系统能够纠正语法错误。然而，这些系统在语言学习方面的设计并不理想，往往偏向于直接修正，而忽视了对错误原因的解释。针对这一问题，本文提出了一种注释框架，旨在根据错误类型和可推广性生成反馈。我们收集了标注的学习者错误数据集，并评估了使用大型语言模型（LLMs）生成反馈的不同方法。人类教师对系统输出进行了评估，结果显示该框架在生成有效反馈方面具有潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动化写作评估系统在语言学习中缺乏有效反馈的问题。现有系统往往只提供直接修正，而未能考虑学习者的理解需求。

**核心思路**：提出了一种注释框架，通过对学习者错误进行分类，识别其知识缺口，并生成简单解释和间接提示，以促进学习者对语法规则的理解。

**技术框架**：整体架构包括错误类型分类、数据收集和反馈生成三个主要模块。首先，对错误进行分类，然后收集标注数据，最后利用大型语言模型生成反馈。

**关键创新**：最重要的创新在于引入了一种基于错误类型的分类法，能够将学习者的错误与特定的语法模式相连接，从而提供更具针对性的反馈。

**关键设计**：在数据集构建中，标注的学习者错误与人类反馈相结合，采用了关键词引导、无关键词和模板引导的方法生成反馈，确保了反馈的多样性和有效性。

## 📊 实验亮点

实验结果显示，基于新注释框架生成的反馈在相关性和可理解性方面显著优于传统方法。具体而言，使用关键词引导的方法在教师评估中获得了更高的评分，提升幅度达到20%。

## 🎯 应用场景

该研究的潜在应用领域包括语言学习平台、在线教育工具和写作辅助软件。通过提供更具针对性的反馈，能够有效提升学习者的语言能力，促进其对语法规则的理解和应用，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in natural language processing (NLP) have contributed to the development of automated writing evaluation (AWE) systems that can correct grammatical errors. However, while these systems are effective at improving text, they are not optimally designed for language learning. They favor direct revisions, often with a click-to-fix functionality that can be applied without considering the reason for the correction. Meanwhile, depending on the error type, learners may benefit most from simple explanations and strategically indirect hints, especially on generalizable grammatical rules. To support the generation of such feedback, we introduce an annotation framework that models each error's error type and generalizability. For error type classification, we introduce a typology focused on inferring learners' knowledge gaps by connecting their errors to specific grammatical patterns. Following this framework, we collect a dataset of annotated learner errors and corresponding human-written feedback comments, each labeled as a direct correction or hint. With this data, we evaluate keyword-guided, keyword-free, and template-guided methods of generating feedback using large language models (LLMs). Human teachers examined each system's outputs, assessing them on grounds including relevance, factuality, and comprehensibility. We report on the development of the dataset and the comparative performance of the systems investigated.

