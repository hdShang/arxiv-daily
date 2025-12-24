---
layout: default
title: "Beyond Single-User Dialogue: Assessing Multi-User Dialogue State Tracking Capabilities of Large Language Models"
---

# Beyond Single-User Dialogue: Assessing Multi-User Dialogue State Tracking Capabilities of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10504" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10504v1</a>
  <a href="https://arxiv.org/pdf/2506.10504.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10504v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10504v1', 'Beyond Single-User Dialogue: Assessing Multi-User Dialogue State Tracking Capabilities of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangmin Song, Juhwan Choi, JungMin Yun, YoungBin Kim

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**评估大型语言模型在多用户对话状态跟踪中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对话状态跟踪` `大型语言模型` `多用户交互` `言语行为理论` `数据集扩展` `性能评估`

## 📋 核心要点

1. 现有的对话状态跟踪方法主要集中在单用户场景，无法有效应对多用户交互的复杂性。
2. 本研究通过生成第二用户的发言，扩展现有数据集，以便对LLMs在多用户环境中的表现进行系统评估。
3. 实验结果表明，LLMs在多用户DST中的性能显著低于单用户DST，显示出当前模型的局限性。

## 📝 摘要（中文）

大型语言模型（LLMs）在零样本对话状态跟踪（DST）中表现出色，减少了对特定任务训练的需求。然而，传统的DST基准主要集中在结构化的用户-代理对话上，未能捕捉现实世界多用户交互的复杂性。本研究评估了LLMs在多用户DST中的鲁棒性，同时降低数据集构建成本。我们基于言语行为理论，扩展现有DST数据集，通过生成第二用户的发言来实现。实验结果显示，与单用户DST相比，性能显著下降，突显了当前LLMs在多发言者环境中提取和跟踪对话状态的局限性。这一发现强调了未来研究在多用户DST场景中增强LLMs的必要性，为更现实和鲁棒的DST模型铺平了道路。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在多用户对话状态跟踪中的能力不足，现有方法主要针对单用户场景，无法适应多发言者的复杂对话环境。

**核心思路**：通过生成第二用户的发言，基于言语行为理论扩展现有DST数据集，从而实现对多用户对话状态跟踪的评估。此设计旨在模拟真实的多用户对话场景。

**技术框架**：研究首先对现有DST数据集进行扩展，生成第二用户的发言，然后将这些发言整合到对话中，最后使用LLMs进行对话状态跟踪的评估。主要模块包括数据集扩展、对话生成和性能评估。

**关键创新**：本研究的创新在于通过引入第二用户的发言，系统性地评估LLMs在多用户对话中的表现，填补了现有研究的空白。与传统方法相比，这种方法更贴近真实的对话场景。

**关键设计**：在数据集扩展过程中，采用了言语行为理论来生成第二用户的发言，确保生成内容的合理性和多样性。实验中使用了标准的评估指标来量化模型性能。

## 📊 实验亮点

实验结果显示，LLMs在多用户对话状态跟踪中的性能显著下降，具体表现为与单用户DST相比，性能下降幅度达到XX%（具体数据待补充）。这一结果强调了当前模型在处理多发言者对话时的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、社交机器人和多用户协作系统等。通过提升LLMs在多用户对话中的表现，可以实现更自然和高效的人机交互，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated remarkable performance in zero-shot dialogue state tracking (DST), reducing the need for task-specific training. However, conventional DST benchmarks primarily focus on structured user-agent conversations, failing to capture the complexities of real-world multi-user interactions. In this study, we assess the robustness of LLMs in multi-user DST while minimizing dataset construction costs. Inspired by recent advances in LLM-based data annotation, we extend an existing DST dataset by generating utterances of a second user based on speech act theory. Our methodology systematically incorporates a second user's utterances into conversations, enabling a controlled evaluation of LLMs in multi-user settings. Experimental results reveal a significant performance drop compared to single-user DST, highlighting the limitations of current LLMs in extracting and tracking dialogue states amidst multiple speakers. Our findings emphasize the need for future research to enhance LLMs for multi-user DST scenarios, paving the way for more realistic and robust DST models.

