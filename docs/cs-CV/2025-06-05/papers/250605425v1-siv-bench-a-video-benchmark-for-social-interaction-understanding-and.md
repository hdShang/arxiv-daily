---
layout: default
title: "SIV-Bench: A Video Benchmark for Social Interaction Understanding and Reasoning"
---

# SIV-Bench: A Video Benchmark for Social Interaction Understanding and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05425" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05425v1</a>
  <a href="https://arxiv.org/pdf/2506.05425.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05425v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05425v1', 'SIV-Bench: A Video Benchmark for Social Interaction Understanding and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fanqi Kong, Weiqin Zu, Xinyu Chen, Yaodong Yang, Song-Chun Zhu, Xue Feng

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-05

**🔗 代码/项目**: [PROJECT_PAGE](https://kfq20.github.io/sivbench/)

---

## 💡 一句话要点

**提出SIV-Bench以解决社交互动理解与推理问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社交互动理解` `多模态大语言模型` `视频基准` `社交状态推理` `关系推理` `动态预测` `人机交互`

## 📋 核心要点

1. 现有方法在理解和推理社交互动时面临多模态线索和动态行为的复杂性，导致性能不足。
2. 论文提出SIV-Bench基准，通过2792个视频和8792个问答对，系统评估多模态大语言模型在社交理解和推理中的能力。
3. 实验结果显示，尽管模型在社交场景理解上表现良好，但在社交状态推理和动态预测上存在显著不足，尤其在关系推理方面。

## 📝 摘要（中文）

人类社交互动的丰富多样性，包括多模态线索、不可观察的关系和心理状态，以及动态行为，为人工智能带来了巨大的挑战。为推动该领域的研究，我们提出了SIV-Bench，这是一个新的视频基准，用于严格评估多模态大语言模型（MLLMs）在社交场景理解（SSU）、社交状态推理（SSR）和社交动态预测（SDP）方面的能力。SIV-Bench包含2792个视频片段和8792对精心生成的问题-答案对，数据来源于人类与LLM的协作流程，涵盖了TikTok和YouTube上的多种视频类型和文化背景。我们的实验表明，尽管模型在SSU方面表现良好，但在SSR和SDP方面存在显著困难，关系推理（RI）是一个明显的瓶颈。研究还确认了转录对话在理解复杂社交互动中的关键作用。

## 🔬 方法详解

**问题定义**：本论文旨在解决社交互动理解与推理的挑战，现有方法在处理多模态线索和动态行为时表现不佳，尤其是在关系推理方面存在明显瓶颈。

**核心思路**：通过构建SIV-Bench基准，系统性地评估多模态大语言模型在社交场景理解、社交状态推理和社交动态预测中的能力，旨在识别模型的优势与不足。

**技术框架**：SIV-Bench的整体架构包括视频数据收集、问题生成和答案对的构建，涵盖多种视频类型和文化背景，并设置不同的文本线索分析。

**关键创新**：SIV-Bench的创新点在于其综合性的数据集和评估框架，特别是通过人类与LLM的协作生成问题-答案对，提供了更为真实的社交互动场景。

**关键设计**：在数据集构建中，采用了多样化的视频来源和问答生成策略，同时关注文本线索的影响，确保评估的全面性和准确性。实验中还分析了转录对话对理解复杂社交互动的帮助。

## 📊 实验亮点

实验结果显示，尽管多模态大语言模型在社交场景理解（SSU）方面表现良好，但在社交状态推理（SSR）和社交动态预测（SDP）方面的表现显著不足，尤其在关系推理（RI）上存在明显瓶颈。模型在SSU任务中的准确率高达XX%，而在SSR和SDP任务中则下降至YY%。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、智能客服和人机交互等，能够提升人工智能在理解和推理人类社交行为方面的能力，推动更智能的社交AI系统的发展。未来，SIV-Bench可能成为社交智能AI研究的重要基准，促进相关技术的进步。

## 📄 摘要（原文）

> The rich and multifaceted nature of human social interaction, encompassing multimodal cues, unobservable relations and mental states, and dynamical behavior, presents a formidable challenge for artificial intelligence. To advance research in this area, we introduce SIV-Bench, a novel video benchmark for rigorously evaluating the capabilities of Multimodal Large Language Models (MLLMs) across Social Scene Understanding (SSU), Social State Reasoning (SSR), and Social Dynamics Prediction (SDP). SIV-Bench features 2,792 video clips and 8,792 meticulously generated question-answer pairs derived from a human-LLM collaborative pipeline. It is originally collected from TikTok and YouTube, covering a wide range of video genres, presentation styles, and linguistic and cultural backgrounds. It also includes a dedicated setup for analyzing the impact of different textual cues-original on-screen text, added dialogue, or no text. Our comprehensive experiments on leading MLLMs reveal that while models adeptly handle SSU, they significantly struggle with SSR and SDP, where Relation Inference (RI) is an acute bottleneck, as further examined in our analysis. Our study also confirms the critical role of transcribed dialogue in aiding comprehension of complex social interactions. By systematically identifying current MLLMs' strengths and limitations, SIV-Bench offers crucial insights to steer the development of more socially intelligent AI. The dataset and code are available at https://kfq20.github.io/sivbench/.

