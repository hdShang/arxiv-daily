---
layout: default
title: "CoDAE: Adapting Large Language Models for Education via Chain-of-Thought Data Augmentation"
---

# CoDAE: Adapting Large Language Models for Education via Chain-of-Thought Data Augmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08386" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08386v1</a>
  <a href="https://arxiv.org/pdf/2508.08386.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08386v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08386v1', 'CoDAE: Adapting Large Language Models for Education via Chain-of-Thought Data Augmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuzhou Yuan, William LaCroix, Hardik Ghoshal, Ercong Nie, Michael Färber

**分类**: cs.CL

**发布日期**: 2025-08-11

---

## 💡 一句话要点

**提出CoDAE框架以解决教育场景中LLM适应性不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `教育技术` `链式思维` `数据增强` `个性化学习` `智能辅导`

## 📋 核心要点

1. 现有的LLMs在教育环境中表现不佳，存在过度顺从、响应适应性低和对情感操控性提示脆弱等问题。
2. 提出CoDAE框架，通过链式思维数据增强，收集真实对话并进行丰富，以促进逐步推理和教育指导。
3. 实验结果表明，微调后的模型在教育场景中提供了更合适的指导，支持推理过程，并有效抵御过早揭示答案。

## 📝 摘要（中文）

大型语言模型（LLMs）因其可扩展性和个性化教学潜力而越来越多地被用作AI辅导员。然而，现成的LLMs在教育环境中表现不佳，常常过于轻易地揭示答案，无法根据学生的不确定性调整响应，并且容易受到情感操控性提示的影响。为了解决这些问题，本文提出了CoDAE框架，通过链式思维（CoT）数据增强来适应LLMs于教育用途。我们收集了学生与基于ChatGPT的辅导员之间的真实对话，并利用CoT提示进行丰富，以促进逐步推理和符合教育目标的指导。此外，我们设计了针对性的对话案例，以明确减轻过度顺从、低响应适应性和威胁脆弱性等三大关键限制。通过在不同变体的增强数据集上微调四个开源LLMs，并在模拟教育场景中进行评估，结果表明，使用CoDAE微调的模型提供了更符合教育要求的指导，更好地支持推理过程，并有效抵御过早揭示答案的问题。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLMs在教育场景中的适应性不足，具体表现为过度顺从、低响应适应性和对情感操控性提示的脆弱性。

**核心思路**：通过链式思维（CoT）数据增强，丰富学生与AI辅导员之间的对话，促进逐步推理和符合教育目标的指导。这样的设计旨在提高模型在教育环境中的表现和适应性。

**技术框架**：CoDAE框架包括数据收集、对话丰富、模型微调和评估四个主要模块。首先收集真实对话，然后通过CoT提示增强数据，接着对四个开源LLMs进行微调，最后在模拟教育场景中进行评估。

**关键创新**：最重要的技术创新在于通过链式思维数据增强来提升LLMs的教育适应性，这与传统的直接使用LLMs的方式有本质区别，后者未能有效解决教育场景中的特定需求。

**关键设计**：在模型微调过程中，采用了特定的损失函数和参数设置，以确保模型能够更好地理解和响应教育场景中的复杂对话需求。

## 📊 实验亮点

实验结果显示，使用CoDAE微调的模型在教育场景中提供了更符合教育要求的指导，支持推理过程的能力显著提升，且有效抵御了过早揭示答案的问题。具体性能数据表明，相较于基线模型，微调后的模型在多个评估指标上均有显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、个性化学习平台和智能辅导系统。通过提升LLMs在教育场景中的适应性，CoDAE框架能够为学生提供更有效的学习支持，促进更深层次的理解与思考，未来可能对教育行业产生深远的影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly employed as AI tutors due to their scalability and potential for personalized instruction. However, off-the-shelf LLMs often underperform in educational settings: they frequently reveal answers too readily, fail to adapt their responses to student uncertainty, and remain vulnerable to emotionally manipulative prompts. To address these challenges, we introduce CoDAE, a framework that adapts LLMs for educational use through Chain-of-Thought (CoT) data augmentation. We collect real-world dialogues between students and a ChatGPT-based tutor and enrich them using CoT prompting to promote step-by-step reasoning and pedagogically aligned guidance. Furthermore, we design targeted dialogue cases to explicitly mitigate three key limitations: over-compliance, low response adaptivity, and threat vulnerability. We fine-tune four open-source LLMs on different variants of the augmented datasets and evaluate them in simulated educational scenarios using both automatic metrics and LLM-as-a-judge assessments. Our results show that models fine-tuned with CoDAE deliver more pedagogically appropriate guidance, better support reasoning processes, and effectively resist premature answer disclosure.

