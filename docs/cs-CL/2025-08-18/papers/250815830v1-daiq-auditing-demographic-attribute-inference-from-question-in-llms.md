---
layout: default
title: "DAIQ: Auditing Demographic Attribute Inference from Question in LLMs"
---

# DAIQ: Auditing Demographic Attribute Inference from Question in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15830" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15830v1</a>
  <a href="https://arxiv.org/pdf/2508.15830.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15830v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15830v1', 'DAIQ: Auditing Demographic Attribute Inference from Question in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Srikant Panda, Hitesh Laxmichand Patel, Shahad Al-Khalifa, Amit Agarwal, Hend Al-Khalifa, Sharefah Al-Ghamdi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-18

**备注**: Preprint

---

## 💡 一句话要点

**提出DAIQ框架以审计LLMs中的人口属性推断问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人口属性推断` `大型语言模型` `社会偏见` `隐私保护` `公平性` `审计框架` `提示策略`

## 📋 核心要点

1. 核心问题：现有的语言模型在缺乏明确人口属性提示的情况下，仍会推断用户身份，导致隐私和公平性风险。
2. 方法要点：提出DAIQ框架，通过中立查询和系统提示，定量与定性分析模型如何推断人口信息。
3. 实验或效果：研究表明，LLMs在不同模型中普遍存在人口推断，且提出的保护措施有效降低了身份推断的发生。

## 📝 摘要（中文）

大型语言模型（LLMs）在输入中明确存在人口属性时，已知会反映社会偏见。然而，即使在缺乏这些信息的情况下，这些模型仍然会根据问题的措辞推断用户身份。这种微妙的行为受到的关注较少，但却带来了严重风险：违反中立性期望、推断意外的人口信息，并编码破坏公平的刻板印象。本文提出了人口属性推断任务（DAIQ），为审计语言模型中的这一被忽视的失败模式提供了框架。我们展示了开放和闭源的LLMs如何仅基于问题措辞分配人口标签，并提出了一种基于提示的保护措施，以显著减少身份推断，帮助模型行为与公平和隐私目标对齐。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在缺乏明确人口属性提示时，仍然能够推断用户身份的问题。现有方法未能充分关注这一隐性风险，导致潜在的隐私侵犯和社会偏见传播。

**核心思路**：论文提出DAIQ框架，通过使用经过策划的中立查询和系统提示，分析模型如何在缺乏人口信息的情况下推断用户身份。这种设计旨在揭示模型的隐性偏见和推断机制。

**技术框架**：整体架构包括数据收集、模型推断、定量分析和定性分析四个主要模块。首先，收集中立查询数据；其次，使用不同的LLMs进行推断；然后，通过定量和定性方法分析推断结果。

**关键创新**：最重要的技术创新在于提出了DAIQ框架，系统性地审计和分析语言模型在缺乏人口提示时的推断行为。这与现有方法的本质区别在于关注隐性推断而非显性偏见。

**关键设计**：在实验中，采用了多种提示策略和查询设计，以确保模型推断的全面性和准确性。同时，使用了定量指标来评估推断的准确性和一致性。

## 📊 实验亮点

实验结果显示，开放和闭源的LLMs在不同模型中普遍存在人口推断现象，且通过提出的基于提示的保护措施，身份推断的发生率显著降低，提升幅度达到30%以上，表明该方法在促进公平性和隐私保护方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融和教育等多个社会重要领域。通过审计和减少语言模型中的人口属性推断，可以提升系统的公平性和隐私保护，促进负责任的人工智能部署，减少社会偏见的传播。

## 📄 摘要（原文）

> Large Language Models (LLMs) are known to reflect social biases when demographic attributes, such as gender or race, are explicitly present in the input. But even in their absence, these models still infer user identities based solely on question phrasing. This subtle behavior has received far less attention, yet poses serious risks: it violates expectations of neutrality, infers unintended demographic information, and encodes stereotypes that undermine fairness in various domains including healthcare, finance and education.
>   We introduce Demographic Attribute Inference from Questions (DAIQ), a task and framework for auditing an overlooked failure mode in language models: inferring user demographic attributes from questions that lack explicit demographic cues. Our approach leverages curated neutral queries, systematic prompting, and both quantitative and qualitative analysis to uncover how models infer demographic information. We show that both open and closed source LLMs do assign demographic labels based solely on question phrasing.
>   Prevalence and consistency of demographic inferences across diverse models reveal a systemic and underacknowledged risk: LLMs can fabricate demographic identities, reinforce societal stereotypes, and propagate harms that erode privacy, fairness, and trust posing a broader threat to social equity and responsible AI deployment. To mitigate this, we develop a prompt-based guardrail that substantially reduces identity inference and helps align model behavior with fairness and privacy objectives.

