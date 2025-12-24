---
layout: default
title: "EGOILLUSION: Benchmarking Hallucinations in Egocentric Video Understanding"
---

# EGOILLUSION: Benchmarking Hallucinations in Egocentric Video Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12687" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12687v2</a>
  <a href="https://arxiv.org/pdf/2508.12687.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12687v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12687v2', 'EGOILLUSION: Benchmarking Hallucinations in Egocentric Video Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ashish Seth, Utkarsh Tyagi, Ramaneswaran Selvakumar, Nishit Anand, Sonal Kumar, Sreyan Ghosh, Ramani Duraiswami, Chirag Agarwal, Dinesh Manocha

**分类**: cs.AI, cs.CV

**发布日期**: 2025-08-18 (更新: 2025-08-23)

---

## 💡 一句话要点

**提出EgoIllusion以评估自我中心视频理解中的幻觉问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自我中心视频理解` `多模态大型语言模型` `幻觉评估` `视频分析` `人工智能`

## 📋 核心要点

1. 现有的多模态大型语言模型在自我中心视频理解中存在幻觉问题，导致生成的响应虽然连贯但不准确。
2. 论文提出EgoIllusion基准，通过1400个视频和8000个问题评估MLLM在自我中心视频中的幻觉表现。
3. 实验结果显示，强大的模型如GPT-4o和Gemini的准确率仅为59%，揭示了当前模型在此领域的挑战。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在复杂的多模态任务中表现出色，但在自我中心视频理解中容易产生幻觉，生成连贯但不准确的响应。本文提出EgoIllusion，这是第一个评估MLLM幻觉的基准，包含1400个视频和8000个人工标注的问题，旨在触发视觉和听觉线索中的幻觉。对十个MLLM的评估显示，包括GPT-4o和Gemini在内的强大模型仅达到59%的准确率。EgoIllusion为开发稳健的基准奠定了基础，并促进了更好的自我中心MLLM的开发，减少幻觉率。该基准将开源以便于复现。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型在自我中心视频理解中产生幻觉的问题。现有方法在处理视觉和听觉信息时，容易生成不准确的响应，影响模型的实用性和可靠性。

**核心思路**：EgoIllusion基准通过设计特定的问题来触发模型的幻觉，评估其在自我中心视频中的表现。这种方法能够系统性地揭示模型的弱点，并为后续改进提供依据。

**技术框架**：EgoIllusion基准包括1400个视频和8000个问题，问题分为开放式和封闭式，旨在覆盖多种视觉和听觉线索。评估过程涉及对十个不同的MLLM进行测试，比较其在幻觉生成方面的表现。

**关键创新**：EgoIllusion是首个专门针对自我中心视频理解中幻觉现象的评估基准，填补了现有研究的空白。与以往的评估方法不同，它专注于模型在特定情境下的表现，提供了更具针对性的反馈。

**关键设计**：在设计问题时，考虑了多种视觉和听觉线索的组合，以确保能够有效触发模型的幻觉。此外，评估过程中采用了严格的标注标准，确保问题的质量和有效性。实验中使用的模型包括GPT-4o和Gemini等先进的MLLM。

## 📊 实验亮点

实验结果显示，尽管使用了先进的模型如GPT-4o和Gemini，但在自我中心视频理解中，这些模型的准确率仅为59%。这一发现突显了当前多模态大型语言模型在处理幻觉问题上的显著挑战，为后续研究指明了方向。

## 🎯 应用场景

EgoIllusion基准的提出为多模态大型语言模型的研究提供了新的方向，尤其是在自我中心视频理解领域。该基准不仅可以用于评估现有模型的性能，还能为未来模型的改进提供指导，具有广泛的应用潜力，包括智能监控、虚拟现实和人机交互等领域。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated remarkable performance in complex multimodal tasks. While MLLMs excel at visual perception and reasoning in third-person and egocentric videos, they are prone to hallucinations, generating coherent yet inaccurate responses. We present EgoIllusion, a first benchmark to evaluate MLLM hallucinations in egocentric videos. EgoIllusion comprises 1,400 videos paired with 8,000 human-annotated open and closed-ended questions designed to trigger hallucinations in both visual and auditory cues in egocentric videos. Evaluations across ten MLLMs reveal significant challenges, including powerful models like GPT-4o and Gemini, achieving only 59% accuracy. EgoIllusion lays the foundation in developing robust benchmarks to evaluate the effectiveness of MLLMs and spurs the development of better egocentric MLLMs with reduced hallucination rates. Our benchmark will be open-sourced for reproducibility.

