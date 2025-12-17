---
layout: default
title: DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context
---

# DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.17399" class="toolbar-btn" target="_blank">📄 arXiv: 2509.17399</a>
  <a href="https://arxiv.org/pdf/2509.17399.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.17399" onclick="toggleFavorite(this, '2509.17399', 'DIWALI: Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pramit Sahoo, Maharaj Brahma, Maunendra Sankar Desarkar

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**DIWALI：提出印度文化特定项数据集，并评估LLM在印度文化文本适应任务中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文化适应` `文化特定项` `印度文化` `数据集` `文本生成` `文化评估`

## 📋 核心要点

1. 现有LLM缺乏文化知识，导致生成内容存在文化偏差，难以适应特定文化语境。
2. DIWALI提出一个包含17个文化方面、36个次区域的印度文化特定项数据集，用于评估LLM的文化适应能力。
3. 通过CSI、LLM评判和人工评估，定量分析表明现有LLM在次区域覆盖和文化适应方面存在不足。

## 📝 摘要（中文）

大型语言模型（LLM）被广泛应用于各种任务和应用中。然而，尽管它们具有广泛的能力，但由于缺乏文化知识和能力，它们在文化一致性方面表现出不足，并产生有偏见的生成结果。评估LLM的文化意识和一致性尤其具有挑战性，因为缺乏适当的评估指标和具有文化基础的数据集，这些数据集能够代表区域和次区域层面文化的复杂性。现有的文化特定项（CSI）数据集主要关注区域层面的概念，并且可能包含误报。为了解决这个问题，我们引入了一个新的印度文化CSI数据集，属于17个文化方面。该数据集包含来自36个次区域的约8000个文化概念。为了衡量LLM在文化文本适应任务中的文化能力，我们使用创建的CSI、LLM作为评判者以及来自不同社会人口区域的人工评估来评估适应情况。此外，我们进行了定量分析，表明所有考虑的LLM都存在选择性的次区域覆盖和表面层面的适应。我们的数据集、项目网页和包含模型输出的代码库均已公开。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理文化相关的任务时，由于缺乏对特定文化的深入理解，容易产生偏差和不准确的结果。现有的文化特定项数据集通常只关注区域层面的概念，并且可能包含错误信息，无法充分代表文化的复杂性和多样性。因此，如何构建一个高质量、细粒度的文化数据集，并利用该数据集有效评估和提升LLM的文化适应能力，是一个亟待解决的问题。

**核心思路**：本研究的核心思路是构建一个专门针对印度文化的、包含多个文化方面和次区域的文化特定项数据集（DIWALI）。通过该数据集，可以更准确地评估LLM在文化文本适应任务中的表现，并发现其在文化理解方面的不足。同时，利用LLM作为评判者和人工评估相结合的方式，可以更全面地评估LLM的文化能力。

**技术框架**：该研究的技术框架主要包括以下几个部分：1)构建DIWALI数据集，该数据集包含17个文化方面和36个次区域的约8000个文化概念；2)设计文化文本适应任务，要求LLM根据给定的文本和文化背景进行适应性修改；3)使用DIWALI数据集、LLM作为评判者和人工评估三种方式，对LLM的文化适应能力进行评估；4)对评估结果进行定量分析，揭示LLM在不同文化方面和次区域的表现差异。

**关键创新**：本研究的关键创新在于：1)提出了一个细粒度的印度文化特定项数据集（DIWALI），该数据集覆盖了多个文化方面和次区域，能够更准确地反映印度文化的复杂性和多样性；2)采用了LLM作为评判者和人工评估相结合的方式，对LLM的文化适应能力进行评估，避免了单一评估方式的局限性；3)通过定量分析，揭示了LLM在不同文化方面和次区域的表现差异，为后续的研究提供了有价值的参考。

**关键设计**：DIWALI数据集的关键设计包括：1)选择17个具有代表性的文化方面，如节日、食物、服饰等；2)覆盖36个印度次区域，以反映不同地区的文化差异；3)收集约8000个文化概念，并进行标注和验证，以保证数据的质量和准确性。在评估方面，采用了LLM作为评判者，并结合人工评估，以提高评估的客观性和可靠性。具体参数设置和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.17399/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.17399/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2509.17399/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该研究构建了一个包含约8000个文化概念的印度文化特定项数据集，覆盖17个文化方面和36个次区域。实验结果表明，现有的LLM在文化文本适应任务中表现出选择性的次区域覆盖和表面层面的适应，表明其文化理解能力仍有待提高。具体性能数据和提升幅度在摘要中未明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于提升LLM在文化相关任务中的表现，例如文化内容生成、跨文化交流和文化遗产保护。通过提高LLM的文化意识和适应能力，可以减少文化误解和偏见，促进不同文化之间的理解和尊重。此外，该数据集也可以作为其他研究人员进行文化相关研究的基础资源。

## 📄 摘要（原文）

> Large language models (LLMs) are widely used in various tasks and applications. However, despite their wide capabilities, they are shown to lack cultural alignment \citep{ryan-etal-2024-unintended, alkhamissi-etal-2024-investigating} and produce biased generations \cite{naous-etal-2024-beer} due to a lack of cultural knowledge and competence. Evaluation of LLMs for cultural awareness and alignment is particularly challenging due to the lack of proper evaluation metrics and unavailability of culturally grounded datasets representing the vast complexity of cultures at the regional and sub-regional levels. Existing datasets for culture specific items (CSIs) focus primarily on concepts at the regional level and may contain false positives. To address this issue, we introduce a novel CSI dataset for Indian culture, belonging to 17 cultural facets. The dataset comprises ~8k cultural concepts from 36 sub-regions. To measure the cultural competence of LLMs on a cultural text adaptation task, we evaluate the adaptations using the CSIs created, LLM as Judge, and human evaluations from diverse socio-demographic region. Furthermore, we perform quantitative analysis demonstrating selective sub-regional coverage and surface-level adaptations across all considered LLMs. Our dataset is available here:this https URL, project webpagethis https URL, and our codebase with model outputs can be found here:this https URL

