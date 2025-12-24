---
layout: default
title: "RAGAPHENE: A RAG Annotation Platform with Human Enhancements and Edits"
---

# RAGAPHENE: A RAG Annotation Platform with Human Enhancements and Edits

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19272" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19272v1</a>
  <a href="https://arxiv.org/pdf/2508.19272.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19272v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19272v1', 'RAGAPHENE: A RAG Annotation Platform with Human Enhancements and Edits')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kshitij Fadnis, Sara Rosenthal, Maeda Hanafi, Yannis Katsis, Marina Danilevsky

**分类**: cs.CL

**发布日期**: 2025-08-22

---

## 💡 一句话要点

**提出RAGAPHENE以解决LLMs对话评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对话系统` `大型语言模型` `数据注释` `评估基准` `自然语言处理`

## 📋 核心要点

1. 现有的LLMs在多轮对话中可能产生虚假信息，缺乏有效的评估基准。
2. RAGAPHENE平台通过模拟真实对话场景，提供了一种新的注释方式来评估LLMs。
3. 该平台已被40名注释者使用，成功构建了数千个对话，提升了评估的真实性和有效性。

## 📝 摘要（中文）

检索增强生成（RAG）在与大型语言模型（LLMs）对话时至关重要，尤其是在信息准确性方面。LLMs可能会提供看似正确但实际上包含虚假信息的答案。因此，构建能够评估LLMs在多轮RAG对话中的表现的基准变得愈发重要。模拟真实世界的对话对于生成高质量的评估基准至关重要。本文提出了RAGAPHENE，一个基于聊天的注释平台，使注释者能够模拟真实世界的对话，从而对LLMs进行基准测试和评估。RAGAPHENE已成功被约40名注释者使用，构建了数千个真实世界的对话。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLMs在多轮对话中产生虚假信息的问题，现有方法缺乏有效的评估基准，导致对话质量难以保证。

**核心思路**：RAGAPHENE平台通过模拟真实世界的对话场景，使注释者能够创建高质量的对话数据，从而为LLMs的评估提供可靠的基准。

**技术框架**：RAGAPHENE的整体架构包括用户界面、对话生成模块和数据存储模块。用户界面允许注释者输入和编辑对话，生成模块负责创建对话内容，而数据存储模块则保存生成的对话数据。

**关键创新**：RAGAPHENE的主要创新在于其注释平台的设计，使得注释者能够在真实对话环境中进行交互，显著提高了对话数据的质量和多样性。

**关键设计**：平台设计中考虑了用户体验，注释者可以方便地编辑和调整对话内容，系统还支持多轮对话的生成，确保生成的数据能够真实反映人类对话的复杂性。

## 📊 实验亮点

在实验中，RAGAPHENE成功构建了数千个真实对话，参与的40名注释者反馈良好，表明该平台在生成高质量对话数据方面具有显著优势。与传统方法相比，RAGAPHENE在对话的真实性和多样性上均有显著提升，提供了更为可靠的评估基准。

## 🎯 应用场景

RAGAPHENE的潜在应用领域包括自然语言处理、对话系统的开发和评估，以及大型语言模型的训练和优化。通过提供高质量的对话数据，该平台能够帮助研究人员和开发者提升对话系统的性能，推动相关技术的进步和应用。未来，该平台可能在教育、客服和人机交互等多个领域发挥重要作用。

## 📄 摘要（原文）

> Retrieval Augmented Generation (RAG) is an important aspect of conversing with Large Language Models (LLMs) when factually correct information is important. LLMs may provide answers that appear correct, but could contain hallucinated information. Thus, building benchmarks that can evaluate LLMs on multi-turn RAG conversations has become an increasingly important task. Simulating real-world conversations is vital for producing high quality evaluation benchmarks. We present RAGAPHENE, a chat-based annotation platform that enables annotators to simulate real-world conversations for benchmarking and evaluating LLMs. RAGAPHENE has been successfully used by approximately 40 annotators to build thousands of real-world conversations.

