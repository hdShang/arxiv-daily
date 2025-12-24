---
layout: default
title: "ELLIS Alicante at CQs-Gen 2025: Winning the critical thinking questions shared task: LLM-based question generation and selection"
---

# ELLIS Alicante at CQs-Gen 2025: Winning the critical thinking questions shared task: LLM-based question generation and selection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14371" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14371v1</a>
  <a href="https://arxiv.org/pdf/2506.14371.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14371v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14371v1', 'ELLIS Alicante at CQs-Gen 2025: Winning the critical thinking questions shared task: LLM-based question generation and selection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lucile Favero, Daniel Frases, Juan Antonio Pérez-Ortiz, Tanja Käser, Nuria Oliver

**分类**: cs.CL, cs.HC

**发布日期**: 2025-06-17

**备注**: Proceedings of the 12th Workshop on Argument Mining

---

## 💡 一句话要点

**提出基于LLM的批判性问题生成与选择方法以促进深度思考**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `批判性思维` `问题生成` `自动化评估` `论证挖掘`

## 📋 核心要点

1. 现有基于LLMs的方法可能导致学习的肤浅化，无法有效促进批判性思维能力的培养。
2. 本研究提出了一种两步框架，利用提问者生成候选问题，并通过评判者选择最相关的问题，以促进深度思考。
3. 实验结果显示，该方法在共享任务中排名第一，证明了其在促进批判性参与方面的有效性。

## 📝 摘要（中文）

随着基于大型语言模型（LLMs）聊天界面的广泛应用，人们对其可能促进肤浅学习和削弱批判性思维能力的担忧日益加剧。本研究探索了LLMs在生成挑战性批判性问题方面的潜力，以促进更深层次的推理，特别是在辩论干预中质疑不支持或模糊的主张。该研究作为第12届论证挖掘研讨会的共享任务的一部分，提出了一种两步框架，利用两个小规模的开源语言模型：一个生成多个候选问题的提问者和一个选择最相关问题的评判者。我们的系统在共享任务竞赛中排名第一，展示了所提LLM方法在鼓励对论证文本进行批判性参与方面的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有LLMs在促进批判性思维方面的不足，特别是其在生成有效批判性问题方面的局限性。现有方法往往侧重于信息检索，而忽视了深度推理的需求。

**核心思路**：论文提出的核心思路是通过生成挑战性问题来促进批判性思维，而不仅仅是提供事实信息。通过这种方式，用户能够更深入地分析和质疑论证内容。

**技术框架**：整体架构包括两个主要模块：提问者和评判者。提问者负责生成多个候选问题，而评判者则从中选择最相关的问题。该框架的设计旨在通过分步处理提高问题生成的质量和相关性。

**关键创新**：最重要的技术创新在于将LLMs应用于批判性问题的生成与选择，形成了一个新的研究方向，与传统的信息检索方法有本质区别。

**关键设计**：在参数设置上，提问者和评判者均采用小规模的开源语言模型，具体的损失函数和网络结构设计尚未详细披露，需进一步研究。实验中对候选问题的选择标准进行了优化，以确保生成问题的相关性和挑战性。

## 📊 实验亮点

在共享任务竞赛中，该系统表现优异，成功排名第一，显示出其在批判性问题生成和选择方面的有效性。相较于基线方法，所提方法在问题相关性和挑战性上有显著提升，具体性能数据尚未披露。

## 🎯 应用场景

该研究的潜在应用领域包括教育、辩论训练和在线讨论平台。通过促进批判性思维能力的培养，该方法可以帮助学生和参与者更有效地分析和评估论证，从而提高整体学习效果和参与质量。未来，该技术有望在更多领域推广，推动深度学习和思维能力的结合。

## 📄 摘要（原文）

> The widespread adoption of chat interfaces based on Large Language Models (LLMs) raises concerns about promoting superficial learning and undermining the development of critical thinking skills. Instead of relying on LLMs purely for retrieving factual information, this work explores their potential to foster deeper reasoning by generating critical questions that challenge unsupported or vague claims in debate interventions. This study is part of a shared task of the 12th Workshop on Argument Mining, co-located with ACL 2025, focused on automatic critical question generation. We propose a two-step framework involving two small-scale open source language models: a Questioner that generates multiple candidate questions and a Judge that selects the most relevant ones. Our system ranked first in the shared task competition, demonstrating the potential of the proposed LLM-based approach to encourage critical engagement with argumentative texts.

