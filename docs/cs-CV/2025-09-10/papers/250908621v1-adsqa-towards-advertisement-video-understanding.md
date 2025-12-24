---
layout: default
title: "AdsQA: Towards Advertisement Video Understanding"
---

# AdsQA: Towards Advertisement Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08621" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08621v1</a>
  <a href="https://arxiv.org/pdf/2509.08621.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08621v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08621v1', 'AdsQA: Towards Advertisement Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinwei Long, Kai Tian, Peng Xu, Guoli Jia, Jingxuan Li, Sa Yang, Yihua Shao, Kaiyan Zhang, Che Jiang, Hao Xu, Yang Liu, Jiaheng Ma, Bowen Zhou

**分类**: cs.CV

**发布日期**: 2025-09-10

**备注**: ICCV-2025

---

## 💡 一句话要点

**提出AdsQA广告视频理解基准，并设计ReAd-R模型提升LLM在广告领域的应用能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `广告视频理解` `大型语言模型` `问答系统` `强化学习` `数据集构建`

## 📋 核心要点

1. 现有方法难以充分理解广告视频中蕴含的营销逻辑、说服策略和受众参与等深层信息。
2. 提出ReAd-R模型，该模型基于强化学习，能够反思问题并通过奖励驱动优化生成答案。
3. 实验表明，ReAd-R在AdsQA基准测试中优于其他配备长链推理能力的LLM，取得了SOTA效果。

## 📝 摘要（中文）

大型语言模型（LLMs）在通用人工智能（AGI）方面取得了显著进展。同时，数学和编程等领域特定问题的涌现推动了这些通用模型通过学习更深层次的专业知识不断发展。现在是进一步扩展知识型LLM专业应用多样性的时候了，尽管收集具有意外性和信息性任务的高质量数据具有挑战性。在本文中，我们建议使用广告（ad）视频作为一个具有挑战性的测试平台，以探测LLM在感知常见视觉领域客观物理内容之外的能力。我们的动机是充分利用线索丰富、信息密集的广告视频的特性，例如营销逻辑、说服策略和受众参与。我们的贡献有三方面：（1）据我们所知，这是首次尝试使用带有精心设计的任务的广告视频来评估LLM。我们贡献了AdsQA，这是一个具有挑战性的广告视频问答基准，源自1,544个广告视频，包含10,962个片段，总计22.7小时，并提供5个具有挑战性的任务。（2）我们提出了ReAd-R，一个Deepseek-R1风格的RL模型，它可以反思问题，并通过奖励驱动的优化生成答案。（3）我们在AdsQA上对14个顶级LLM进行了基准测试，我们的\texttt{ReAd-R}取得了最先进的成果，明显优于配备长链推理能力的强大竞争对手。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在理解广告视频方面存在的不足。现有方法难以有效捕捉广告视频中蕴含的复杂信息，如营销逻辑、说服策略和受众参与度，导致LLMs无法充分理解广告的意图和目标。

**核心思路**：论文的核心思路是利用广告视频作为测试平台，设计具有挑战性的问答任务，以评估和提升LLMs在理解广告视频方面的能力。通过构建高质量的广告视频问答数据集（AdsQA）和提出一种新的模型（ReAd-R），来推动LLMs在广告领域的应用。

**技术框架**：整体框架包括两个主要部分：AdsQA数据集的构建和ReAd-R模型的提出。AdsQA数据集包含1544个广告视频，共计10962个片段，总时长22.7小时，并设计了5个具有挑战性的问答任务。ReAd-R模型是一个基于Deepseek-R1风格的强化学习模型，它通过反思问题并利用奖励驱动的优化来生成答案。

**关键创新**：论文的关键创新在于首次将广告视频作为测试平台来评估LLMs，并提出了ReAd-R模型，该模型能够通过强化学习的方式，更好地理解广告视频中的复杂信息。与现有方法相比，ReAd-R模型能够更有效地捕捉广告的营销逻辑和说服策略。

**关键设计**：ReAd-R模型的关键设计包括：(1) 使用Deepseek-R1风格的架构，使其具有强大的推理能力；(2) 采用强化学习框架，通过奖励函数来引导模型生成更准确和相关的答案；(3) 设计了特定的奖励函数，以鼓励模型捕捉广告视频中的关键信息，如营销目标和受众参与度。

## 📊 实验亮点

ReAd-R模型在AdsQA基准测试中取得了最先进的成果，显著优于其他配备长链推理能力的LLM。具体而言，ReAd-R模型在多个问答任务上都取得了明显的性能提升，证明了其在理解广告视频方面的优越性。实验结果表明，ReAd-R模型能够更有效地捕捉广告视频中的关键信息，并生成更准确和相关的答案。

## 🎯 应用场景

该研究成果可应用于智能广告分析、广告效果评估、广告内容生成等领域。通过提升LLMs对广告视频的理解能力，可以更准确地分析广告的营销效果，为广告主提供更有效的投放策略，并辅助生成更具吸引力的广告内容。未来，该技术有望应用于个性化广告推荐、智能客服等领域。

## 📄 摘要（原文）

> Large language models (LLMs) have taken a great step towards AGI. Meanwhile, an increasing number of domain-specific problems such as math and programming boost these general-purpose models to continuously evolve via learning deeper expertise. Now is thus the time further to extend the diversity of specialized applications for knowledgeable LLMs, though collecting high quality data with unexpected and informative tasks is challenging. In this paper, we propose to use advertisement (ad) videos as a challenging test-bed to probe the ability of LLMs in perceiving beyond the objective physical content of common visual domain. Our motivation is to take full advantage of the clue-rich and information-dense ad videos' traits, e.g., marketing logic, persuasive strategies, and audience engagement. Our contribution is three-fold: (1) To our knowledge, this is the first attempt to use ad videos with well-designed tasks to evaluate LLMs. We contribute AdsQA, a challenging ad Video QA benchmark derived from 1,544 ad videos with 10,962 clips, totaling 22.7 hours, providing 5 challenging tasks. (2) We propose ReAd-R, a Deepseek-R1 styled RL model that reflects on questions, and generates answers via reward-driven optimization. (3) We benchmark 14 top-tier LLMs on AdsQA, and our \texttt{ReAd-R}~achieves the state-of-the-art outperforming strong competitors equipped with long-chain reasoning capabilities by a clear margin.

