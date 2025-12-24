---
layout: default
title: "Toward Socially Aware Vision-Language Models: Evaluating Cultural Competence Through Multimodal Story Generation"
---

# Toward Socially Aware Vision-Language Models: Evaluating Cultural Competence Through Multimodal Story Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16762" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16762v1</a>
  <a href="https://arxiv.org/pdf/2508.16762.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16762v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16762v1', 'Toward Socially Aware Vision-Language Models: Evaluating Cultural Competence Through Multimodal Story Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arka Mukherjee, Shreya Ghosh

**分类**: cs.CL, cs.CY

**发布日期**: 2025-08-22

**备注**: Accepted at ASI @ ICCV 2025

**🔗 代码/项目**: [GITHUB](https://github.com/ArkaMukherjee0/mmCultural)

---

## 💡 一句话要点

**提出多模态框架评估视觉语言模型的文化能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `文化能力` `多模态生成` `故事生成` `文化适应性` `跨文化交流` `人工智能伦理`

## 📋 核心要点

1. 现有研究缺乏对视觉语言模型在生成任务中如何适应文化身份线索的系统评估。
2. 本文提出了一种新颖的多模态框架，通过扰动文化身份来评估VLM的文化能力，重点在于故事生成任务。
3. 实验结果显示，模型在文化适应能力上表现出丰富的文化特定词汇，但不同架构间的文化能力差异显著。

## 📝 摘要（中文）

随着视觉语言模型（VLMs）在多元文化背景下的广泛应用，确保其文化能力变得至关重要。尽管之前的研究评估了文本模型和VLM物体识别任务中的文化意识，但尚无系统性研究评估VLM在生成任务中如何适应文化身份线索。本文首次通过多模态故事生成全面评估VLM的文化能力，开发了一种新颖的多模态框架，扰动文化身份并评估五种现代VLM在故事生成任务中的表现。分析显示，模型在文化适应能力上表现显著，但也发现了一些令人担忧的局限性，如不同架构间的文化能力差异和自动化指标与人类评估的矛盾。交叉模态评估表明，文化特征输出可通过视觉-语义相似性检测，但视觉文化理解仍然有限。我们公开发布了代码库和数据。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型在生成任务中对文化身份线索的适应能力不足的问题。现有方法未能系统性评估VLM在多模态输入下的文化适应性。

**核心思路**：论文通过开发一种新颖的多模态框架，扰动文化身份线索，评估不同VLM在故事生成任务中的表现，以此来探讨其文化能力。

**技术框架**：整体架构包括输入文本和视觉信息的多模态融合，文化身份的扰动模块，以及生成故事的输出模块。评估阶段则通过对比不同模型的生成结果来分析文化适应性。

**关键创新**：最重要的技术创新在于首次系统性地评估VLM的文化能力，尤其是在生成任务中如何处理文化身份线索，填补了现有研究的空白。

**关键设计**：在模型设计中，采用了特定的损失函数来优化文化适应性，并通过丰富的文化特定词汇（如姓名、家庭称谓、地理标记）来增强模型的文化理解能力。

## 📊 实验亮点

实验结果显示，模型在文化适应能力上表现出显著的差异，尤其在文化特定词汇的使用上，某些模型在同一国籍的召回率达到28.7%，而跨国籍的召回率仅为0.2%。这表明文化适应能力在不同架构间存在显著差异。

## 🎯 应用场景

该研究的潜在应用领域包括文化敏感的AI生成内容、跨文化交流工具以及教育领域的多模态学习系统。通过提升模型的文化能力，可以更好地满足不同文化背景用户的需求，促进多元文化的理解与交流。

## 📄 摘要（原文）

> As Vision-Language Models (VLMs) achieve widespread deployment across diverse cultural contexts, ensuring their cultural competence becomes critical for responsible AI systems. While prior work has evaluated cultural awareness in text-only models and VLM object recognition tasks, no research has systematically assessed how VLMs adapt outputs when cultural identity cues are embedded in both textual prompts and visual inputs during generative tasks. We present the first comprehensive evaluation of VLM cultural competence through multimodal story generation, developing a novel multimodal framework that perturbs cultural identity and evaluates 5 contemporary VLMs on a downstream task: story generation. Our analysis reveals significant cultural adaptation capabilities, with rich culturally-specific vocabulary spanning names, familial terms, and geographic markers. However, we uncover concerning limitations: cultural competence varies dramatically across architectures, some models exhibit inverse cultural alignment, and automated metrics show architectural bias contradicting human assessments. Cross-modal evaluation shows that culturally distinct outputs are indeed detectable through visual-semantic similarity (28.7% within-nationality vs. 0.2% cross-nationality recall), yet visual-cultural understanding remains limited. In essence, we establish the promise and challenges of cultural competence in multimodal AI. We publicly release our codebase and data: https://github.com/ArkaMukherjee0/mmCultural

