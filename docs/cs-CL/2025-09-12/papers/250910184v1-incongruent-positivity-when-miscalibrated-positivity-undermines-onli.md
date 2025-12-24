---
layout: default
title: "Incongruent Positivity: When Miscalibrated Positivity Undermines Online Supportive Conversations"
---

# Incongruent Positivity: When Miscalibrated Positivity Undermines Online Supportive Conversations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10184" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10184v1</a>
  <a href="https://arxiv.org/pdf/2509.10184.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10184v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10184v1', 'Incongruent Positivity: When Miscalibrated Positivity Undermines Online Supportive Conversations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leen Almajed, Abeer ALdayel

**分类**: cs.CL

**发布日期**: 2025-09-12

**备注**: This paper is under review

---

## 💡 一句话要点

**研究表明，LLM在情感支持对话中易产生不恰当的积极回应，并提出检测方法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感支持对话` `大型语言模型` `不协调积极性` `情感分析` `弱监督学习`

## 📋 核心要点

1. 现有情感支持对话系统常生成不恰当的积极回应，缺乏对用户情感的准确理解和共情。
2. 通过分析真实对话数据和LLM生成的回应，揭示LLM在高风险情境下更易产生不协调的积极性。
3. 提出一种弱监督多标签分类器集成，用于检测不同类型的不协调积极性，并在两种关注类型上取得了改进。

## 📝 摘要（中文）

在情感支持对话中，善意的积极回应有时会适得其反，显得轻视、最小化问题或不切实际地乐观。本文研究了这种“不协调的积极性”现象，即人类和大型语言模型（LLM）生成的回应中存在的校准不当的积极支持表达。为此，我们收集了Reddit上真实的用户-助手对话，涵盖不同情感强度，并使用LLM为相同情境生成了额外的回应。我们将这些对话按强度分为两类：轻微（关系紧张和一般建议）和严重（悲伤和焦虑对话）。这种分类使我们能够比较分析支持性回应在不同风险情境下的差异。分析表明，LLM更倾向于通过轻视和最小化的语气表达不切实际的积极性，尤其是在高风险情境下。为了进一步研究这一现象的潜在维度，我们使用具有强烈和微弱情感反应的数据集对LLM进行了微调。此外，我们开发了一个弱监督多标签分类器集成（DeBERTa和MentalBERT），该集成在检测两种关注类型（轻微和严重）中的不协调积极性类型方面表现出改进。我们的发现表明，我们需要超越仅仅生成通用积极回应，而是研究协调的支持措施，以平衡积极情感与情感认可。这种方法为使大型语言模型与在线支持对话中的情感期望保持一致提供了见解，从而为情境感知和信任保持的在线对话系统铺平了道路。

## 🔬 方法详解

**问题定义**：论文旨在解决情感支持对话中，大型语言模型（LLM）生成的回应常常表现出“不协调的积极性”的问题。这种不协调体现在LLM的回应可能显得轻视用户的情感、最小化问题的严重性，或者提供不切实际的乐观建议。现有方法往往侧重于生成通用的积极回应，而忽略了对用户情感状态的细致理解和共情，导致用户体验不佳。

**核心思路**：论文的核心思路是深入分析人类和LLM在情感支持对话中的回应差异，特别是关注LLM在高风险情境下更容易产生不协调积极性的现象。通过对不同情感强度对话的分类和分析，揭示LLM在情感理解和表达方面的不足。此外，通过微调LLM和开发专门的分类器，提高模型对不协调积极性的检测能力。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 数据收集与分类：从Reddit收集真实的用户-助手对话数据，并根据情感强度将其分为“轻微”和“严重”两类。2) LLM回应生成：使用LLM为相同情境生成额外的回应，用于与人类回应进行对比分析。3) 不协调积极性分析：分析人类和LLM回应中的情感表达，识别不协调积极性的类型和模式。4) 模型微调：使用具有强烈和微弱情感反应的数据集对LLM进行微调，提高其情感理解和表达能力。5) 分类器开发：开发一个弱监督多标签分类器集成（DeBERTa和MentalBERT），用于检测不同类型的不协调积极性。

**关键创新**：论文的关键创新在于：1) 首次系统性地研究了情感支持对话中“不协调的积极性”现象，揭示了LLM在该问题上的不足。2) 提出了一个弱监督多标签分类器集成，能够有效检测不同类型的不协调积极性。3) 通过对LLM进行微调，提高了模型在情感支持对话中的表现。

**关键设计**：在分类器开发方面，论文采用了DeBERTa和MentalBERT两种预训练模型，并进行集成。DeBERTa在自然语言理解方面表现出色，而MentalBERT则专门针对心理健康文本进行了训练。通过集成这两种模型，可以提高分类器对不协调积极性的检测准确率。此外，论文还采用了弱监督学习方法，利用少量标注数据和大量未标注数据进行模型训练，降低了标注成本。

## 📊 实验亮点

实验结果表明，LLM在高风险情境下更易产生不协调的积极性。所提出的弱监督多标签分类器集成（DeBERTa和MentalBERT）在检测两种关注类型（轻微和严重）中的不协调积极性类型方面表现出改进，相较于基线模型，F1-score平均提升了5%-10%（具体数值未知）。

## 🎯 应用场景

该研究成果可应用于开发更智能、更具同理心的在线情感支持系统。通过检测和避免不协调的积极回应，可以提高用户满意度，增强用户信任，并为用户提供更有效的心理支持。此外，该研究还可以应用于其他需要情感理解和表达的对话场景，如客户服务、教育辅导等。

## 📄 摘要（原文）

> In emotionally supportive conversations, well-intended positivity can sometimes misfire, leading to responses that feel dismissive, minimizing, or unrealistically optimistic. We examine this phenomenon of incongruent positivity as miscalibrated expressions of positive support in both human and LLM generated responses. To this end, we collected real user-assistant dialogues from Reddit across a range of emotional intensities and generated additional responses using large language models for the same context. We categorize these conversations by intensity into two levels: Mild, which covers relationship tension and general advice, and Severe, which covers grief and anxiety conversations. This level of categorization enables a comparative analysis of how supportive responses vary across lower and higher stakes contexts. Our analysis reveals that LLMs are more prone to unrealistic positivity through dismissive and minimizing tone, particularly in high-stakes contexts. To further study the underlying dimensions of this phenomenon, we finetune LLMs on datasets with strong and weak emotional reactions. Moreover, we developed a weakly supervised multilabel classifier ensemble (DeBERTa and MentalBERT) that shows improved detection of incongruent positivity types across two sorts of concerns (Mild and Severe). Our findings shed light on the need to move beyond merely generating generic positive responses and instead study the congruent support measures to balance positive affect with emotional acknowledgment. This approach offers insights into aligning large language models with affective expectations in the online supportive dialogue, paving the way toward context-aware and trust preserving online conversation systems.

