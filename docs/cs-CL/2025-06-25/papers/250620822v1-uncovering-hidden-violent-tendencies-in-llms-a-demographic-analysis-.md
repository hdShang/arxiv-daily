---
layout: default
title: "Uncovering Hidden Violent Tendencies in LLMs: A Demographic Analysis via Behavioral Vignettes"
---

# Uncovering Hidden Violent Tendencies in LLMs: A Demographic Analysis via Behavioral Vignettes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20822" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20822v1</a>
  <a href="https://arxiv.org/pdf/2506.20822.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20822v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20822v1', 'Uncovering Hidden Violent Tendencies in LLMs: A Demographic Analysis via Behavioral Vignettes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Quintin Myers, Yanjun Gao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-25

**备注**: Under review

---

## 💡 一句话要点

**通过行为情景分析揭示大型语言模型中的隐藏暴力倾向**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `暴力倾向` `社会科学` `角色化提示` `偏见评估`

## 📋 核心要点

1. 现有的LLMs在处理道德模糊的现实场景时能力不足，特别是在暴力内容的生成和响应方面。
2. 本文提出通过角色化提示来评估LLMs的暴力倾向，考虑不同的种族、年龄和地理身份，以揭示潜在的偏见。
3. 实验结果表明，LLMs的文本生成与其内在偏好存在差异，且暴力倾向在不同人群中表现出显著的变化。

## 📝 摘要（中文）

大型语言模型（LLMs）在检测和响应在线暴力内容方面的应用日益增多，但其在道德模糊的现实场景中的推理能力仍未得到充分检验。本文首次使用经过验证的社会科学工具——暴力行为情景问卷（VBVQ）来评估LLMs。为评估潜在偏见，研究引入了基于角色的提示，考虑了美国的种族、年龄和地理身份。研究结果显示，LLMs的表面文本生成往往与其内在的暴力响应偏好存在差异，且其暴力倾向在不同人群中存在显著差异，常常与犯罪学、社会科学和心理学的既定发现相悖。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在道德模糊场景中对暴力内容的推理能力不足的问题。现有方法未能充分评估LLMs在不同人群中的表现差异，导致潜在偏见未被揭示。

**核心思路**：研究通过引入基于角色的提示，考虑种族、年龄和地理身份的变化，来系统评估LLMs对暴力行为的反应。这种设计旨在揭示LLMs在处理复杂社会情境时的内在偏好。

**技术框架**：整体架构包括数据收集、角色化提示生成、LLMs评估和结果分析四个主要模块。首先，收集多样化的情景数据，然后生成不同角色的提示，接着在统一的零-shot设置下评估六种不同的LLMs，最后分析结果以识别偏见。

**关键创新**：本文的主要创新在于使用经过验证的社会科学工具（VBVQ）来评估LLMs的暴力倾向，并通过角色化提示揭示其在不同人群中的表现差异。这与传统的评估方法有本质区别。

**关键设计**：在实验中，使用了多种角色化提示，确保涵盖不同的种族、年龄和地理身份。评估过程中采用统一的零-shot设置，以确保结果的可比性。

## 📊 实验亮点

实验结果显示，LLMs的文本生成与其内在的暴力倾向存在显著差异，且在不同人群中的暴力倾向表现出不一致性。这一发现挑战了传统的犯罪学和社会科学理论，提示我们在使用LLMs时需谨慎考虑其潜在偏见。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容监控、在线社区管理和暴力行为预测等。通过揭示LLMs的偏见，研究可以帮助开发更公正和有效的内容过滤系统，减少在线暴力内容的传播。未来，这一研究可能对社会科学、心理学和人工智能伦理等领域产生深远影响。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly proposed for detecting and responding to violent content online, yet their ability to reason about morally ambiguous, real-world scenarios remains underexamined. We present the first study to evaluate LLMs using a validated social science instrument designed to measure human response to everyday conflict, namely the Violent Behavior Vignette Questionnaire (VBVQ). To assess potential bias, we introduce persona-based prompting that varies race, age, and geographic identity within the United States. Six LLMs developed across different geopolitical and organizational contexts are evaluated under a unified zero-shot setting. Our study reveals two key findings: (1) LLMs surface-level text generation often diverges from their internal preference for violent responses; (2) their violent tendencies vary across demographics, frequently contradicting established findings in criminology, social science, and psychology.

