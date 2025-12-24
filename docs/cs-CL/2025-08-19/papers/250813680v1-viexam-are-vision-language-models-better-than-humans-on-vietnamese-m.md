---
layout: default
title: "ViExam: Are Vision Language Models Better than Humans on Vietnamese Multimodal Exam Questions?"
---

# ViExam: Are Vision Language Models Better than Humans on Vietnamese Multimodal Exam Questions?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13680" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13680v1</a>
  <a href="https://arxiv.org/pdf/2508.13680.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13680v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13680v1', 'ViExam: Are Vision Language Models Better than Humans on Vietnamese Multimodal Exam Questions?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vy Tuong Dang, An Vo, Quang Tau, Duc Dm, Daeyoung Kim

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出ViExam基准以评估视觉语言模型在越南多模态考试中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `多模态学习` `越南语` `教育评估` `跨语言推理` `基准测试` `人工智能`

## 📋 核心要点

1. 现有的视觉语言模型在处理低资源语言的多模态教育内容时表现不足，尤其是在越南语环境中。
2. 本研究提出了ViExam基准，通过2548个多模态问题评估VLMs在越南教育评估中的能力。
3. 实验结果显示，最先进的VLMs表现低于人类考生，只有少数模型在特定条件下有所提升。

## 📝 摘要（中文）

视觉语言模型（VLMs）在英语多模态任务中表现出色，但在低资源语言的多模态教育内容上的表现尚未得到充分探索。本研究测试了VLMs在越南教育评估中的表现，探讨了以英语数据为主训练的VLMs是否能够处理真实的跨语言多模态推理。我们提出了ViExam基准，包含2548个多模态问题，首次全面评估VLM在越南多模态考试中的能力。结果显示，最先进的VLMs平均准确率仅为57.74%，而开源模型为27.70%，大多数VLMs的表现低于平均人类考生（66.54%），仅有思维VLM o3（74.07%）超过人类平均表现，但仍远低于人类最佳表现（99.60%）。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉语言模型在越南多模态教育评估中的表现不足问题。现有方法主要集中在英语任务上，缺乏对低资源语言的有效评估。

**核心思路**：通过构建ViExam基准，论文评估了VLMs在越南语多模态考试中的能力，探索其跨语言推理的有效性。

**技术框架**：ViExam基准包含2548个多模态问题，覆盖数学、物理、化学等七个学科。模型在这些问题上进行评估，比较其表现与人类考生的差异。

**关键创新**：本研究首次系统性地评估了VLMs在越南多模态考试中的表现，揭示了其在低资源语言环境下的局限性。

**关键设计**：在实验中，使用了多种VLMs进行对比，包括最先进的模型和开源模型，设置了不同的提示方式以测试其对表现的影响。

## 📊 实验亮点

实验结果显示，最先进的VLMs在越南多模态考试中的平均准确率仅为57.74%，而开源模型为27.70%。大多数模型的表现低于人类考生的平均水平（66.54%），仅有思维VLM o3的表现（74.07%）超过了人类平均，但仍远低于最佳人类表现（99.60%）。

## 🎯 应用场景

该研究为视觉语言模型在教育领域的应用提供了重要的基准，尤其是在低资源语言环境中。未来，ViExam基准可以帮助研究者改进VLMs的设计，使其更好地适应多语言和多模态的教育需求，推动教育技术的发展。

## 📄 摘要（原文）

> Vision language models (VLMs) demonstrate remarkable capabilities on English multimodal tasks, but their performance on low-resource languages with genuinely multimodal educational content remains largely unexplored. In this work, we test how VLMs perform on Vietnamese educational assessments, investigating whether VLMs trained predominantly on English data can handle real-world cross-lingual multimodal reasoning. Our work presents the first comprehensive evaluation of VLM capabilities on multimodal Vietnamese exams through proposing ViExam, a benchmark containing 2,548 multimodal questions. We find that state-of-the-art VLMs achieve only 57.74% while open-source models achieve 27.70% mean accuracy across 7 academic domains, including Mathematics, Physics, Chemistry, Biology, Geography, Driving Test, and IQ Test. Most VLMs underperform average human test-takers (66.54%), with only the thinking VLM o3 (74.07%) exceeding human average performance, yet still falling substantially short of human best performance (99.60%). Cross-lingual prompting with English instructions while maintaining Vietnamese content fails to improve performance, decreasing accuracy by 1 percentage point for SOTA VLMs. Human-in-the-loop collaboration can partially improve VLM performance by 5 percentage points. Code and data are available at: https://vi-exam.github.io.

