---
layout: default
title: TRATES: Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring
---

# TRATES: Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14577" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14577v2</a>
  <a href="https://arxiv.org/pdf/2505.14577.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14577v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14577v2', 'TRATES: Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sohaila Eltanbouly, Salam Albatarni, Tamer Elsayed

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-05-31)

**备注**: Accepted at ACL 2025 Findings

---

## 💡 一句话要点

**提出TRATES以解决个体特征评估不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化作文评分` `特征评估` `大型语言模型` `回归模型` `教育技术` `文本分析`

## 📋 核心要点

1. 现有的自动化作文评分方法缺乏对个体特征的细致评估，导致评分的准确性和可靠性不足。
2. TRATES框架通过结合特征评分标准和大型语言模型，生成特征并进行针对性评估，从而实现个体特征的准确评分。
3. 实验结果显示，TRATES在各个特征上均达到了新的最优性能，尤其是生成的LLM特征对评分的贡献显著。

## 📝 摘要（中文）

自动化作文评分（AES）研究历史悠久，但在根据个体特征评估作文方面的关注明显不足。本文提出TRATES，一个新颖的特征特定和基于评分标准的跨提示AES框架，既通用又针对特定特征。该框架利用大型语言模型（LLM），通过特征评分标准生成特征，随后对这些特征进行评估。最终，特征与通用写作质量和提示特定特征结合，训练简单的经典回归模型，以预测未见提示下的作文特征分数。实验表明，TRATES在广泛使用的数据集上实现了所有特征的新状态，生成的基于LLM的特征是最重要的。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动化作文评分方法在个体特征评估上的不足，现有方法往往无法有效区分和评估不同特征。

**核心思路**：TRATES框架的核心在于利用大型语言模型生成特征评分标准，并结合这些特征进行针对性评估，从而提高评分的准确性。

**技术框架**：该框架包括特征生成模块、特征评估模块和回归模型训练模块。特征生成模块利用LLM生成特征，评估模块对特征进行评分，最后通过回归模型预测特征分数。

**关键创新**：TRATES的创新在于其特征特定的评分方法，通过结合通用写作质量和特征特定特征，显著提升了评分的准确性和可靠性。

**关键设计**：在模型设计中，采用了特征评分标准作为输入，结合通用特征和提示特定特征，使用经典回归模型进行训练，确保模型的简洁性和高效性。

## 📊 实验亮点

实验结果表明，TRATES在所有特征上均达到了新的状态，尤其是在生成的LLM特征方面，其对评分的贡献显著，提升幅度超过了现有基线方法，展示了其在自动化评分领域的强大潜力。

## 🎯 应用场景

TRATES框架具有广泛的应用潜力，特别是在教育领域的作文评分和反馈系统中。通过提供更为细致的特征评估，教师和学生可以获得更具针对性的反馈，从而提升写作能力。此外，该方法也可扩展至其他文本分析任务，如内容生成和文本理解等。

## 📄 摘要（原文）

> Research on holistic Automated Essay Scoring (AES) is long-dated; yet, there is a notable lack of attention for assessing essays according to individual traits. In this work, we propose TRATES, a novel trait-specific and rubric-based cross-prompt AES framework that is generic yet specific to the underlying trait. The framework leverages a Large Language Model (LLM) that utilizes the trait grading rubrics to generate trait-specific features (represented by assessment questions), then assesses those features given an essay. The trait-specific features are eventually combined with generic writing-quality and prompt-specific features to train a simple classical regression model that predicts trait scores of essays from an unseen prompt. Experiments show that TRATES achieves a new state-of-the-art performance across all traits on a widely-used dataset, with the generated LLM-based features being the most significant.

