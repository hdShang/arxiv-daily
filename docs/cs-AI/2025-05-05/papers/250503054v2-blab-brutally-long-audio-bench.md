---
layout: default
title: BLAB: Brutally Long Audio Bench
---

# BLAB: Brutally Long Audio Bench

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03054" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03054v2</a>
  <a href="https://arxiv.org/pdf/2505.03054.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03054v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03054v2', 'BLAB: Brutally Long Audio Bench')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Orevaoghene Ahia, Martijn Bartelds, Kabir Ahuja, Hila Gonen, Valentin Hofmann, Siddhant Arora, Shuyue Stella Li, Vishal Puttagunta, Mofetoluwa Adeyemi, Charishma Buchireddy, Ben Walls, Noah Bennett, Shinji Watanabe, Noah A. Smith, Yulia Tsvetkov, Sachin Kumar

**分类**: cs.AI, cs.CL, cs.SD, eess.AS

**发布日期**: 2025-05-05 (更新: 2025-05-12)

---

## 💡 一句话要点

**提出BLAB基准以解决长音频理解问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长音频理解` `音频语言模型` `多模态评估` `自然语言处理` `情感识别`

## 📋 核心要点

1. 现有音频语言模型主要在短音频片段上评估，缺乏对长音频理解的研究，导致其在真实场景中的应用受限。
2. 论文提出了BLAB基准，专注于长达51分钟的音频片段，评估音频LM在多个任务上的表现，旨在提升长音频理解能力。
3. 实验结果显示，所有评估的音频LM在BLAB任务上表现不佳，尤其在定位和时长估计等任务上，揭示了长音频理解的挑战。

## 📝 摘要（中文）

开发大型音频语言模型（LMs）以理解多样的口语交互对于适应人类沟通的多模态特性至关重要，并能提高语言技术在不同用户群体中的可及性。现有音频LMs主要在短音频片段（通常不超过30秒）上评估其性能，缺乏对更长对话语音片段的探索。我们提出了Brutally Long Audio Bench（BLAB），这是一个具有挑战性的长音频基准，评估音频LM在定位、时长估计、情感和计数任务上的表现，使用的音频片段平均长度为51分钟。BLAB包含833小时以上的多样化完整音频剪辑，每个剪辑都配有人工标注的文本自然语言问题和答案。我们的音频数据来自许可来源，并经过人工辅助过滤以确保任务合规性。我们在BLAB上评估了六个开源和专有音频LM，发现包括Gemini 2.0 Pro和GPT-4o在内的所有模型在BLAB任务上表现不佳。我们的综合分析揭示了任务难度与音频时长之间的权衡。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有音频语言模型在长音频理解方面的不足，尤其是它们在处理超过30秒的音频片段时的表现不佳。现有方法未能有效评估长对话的语音理解能力，限制了其在实际应用中的有效性。

**核心思路**：论文的核心思路是通过引入BLAB基准，提供一个包含长音频片段的评估框架，专注于音频LM在定位、情感识别和计数等任务上的表现，以此推动模型在长音频理解方面的研究和发展。

**技术框架**：BLAB基准由833小时以上的多样化音频剪辑组成，平均长度为51分钟。每个音频片段都配有人工标注的文本问题和答案，确保任务的合规性和有效性。评估过程中，模型在多个任务上进行测试，以全面了解其性能。

**关键创新**：BLAB基准的最大创新在于其针对长音频片段的设计，填补了现有音频LM评估中的空白。与传统短音频评估方法相比，BLAB提供了更具挑战性的任务，推动了对长音频理解的深入研究。

**关键设计**：在BLAB的设计中，采用了多种任务类型，包括定位、时长估计和情感分析，确保模型在不同维度上的评估。此外，音频数据经过严格的人工过滤，以确保其质量和任务的相关性。

## 📊 实验亮点

实验结果显示，所有评估的音频LM在BLAB任务上表现不佳，尤其在定位和时长估计任务上，性能显著下降。具体而言，随着音频时长的增加，模型的表现普遍下降，揭示了长音频理解的复杂性和挑战。

## 🎯 应用场景

该研究的潜在应用领域包括语音助手、客服机器人和教育技术等。通过提升音频语言模型对长音频的理解能力，可以显著改善用户体验，增强人机交互的自然性和有效性。未来，该基准可能推动更多针对长音频理解的研究，促进相关技术的发展和应用。

## 📄 摘要（原文）

> Developing large audio language models (LMs) capable of understanding diverse spoken interactions is essential for accommodating the multimodal nature of human communication and can increase the accessibility of language technologies across different user populations. Recent work on audio LMs has primarily evaluated their performance on short audio segments, typically under 30 seconds, with limited exploration of long-form conversational speech segments that more closely reflect natural user interactions with these models. We introduce Brutally Long Audio Bench (BLAB), a challenging long-form audio benchmark that evaluates audio LMs on localization, duration estimation, emotion, and counting tasks using audio segments averaging 51 minutes in length. BLAB consists of 833+ hours of diverse, full-length audio clips, each paired with human-annotated, text-based natural language questions and answers. Our audio data were collected from permissively licensed sources and underwent a human-assisted filtering process to ensure task compliance. We evaluate six open-source and proprietary audio LMs on BLAB and find that all of them, including advanced models such as Gemini 2.0 Pro and GPT-4o, struggle with the tasks in BLAB. Our comprehensive analysis reveals key insights into the trade-offs between task difficulty and audio duration. In general, we find that audio LMs struggle with long-form speech, with performance declining as duration increases. They perform poorly on localization, temporal reasoning, counting, and struggle to understand non-phonemic information, relying more on prompts than audio content. BLAB serves as a challenging evaluation framework to develop audio LMs with robust long-form audio understanding capabilities.

