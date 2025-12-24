---
layout: default
title: LCES: Zero-shot Automated Essay Scoring via Pairwise Comparisons Using Large Language Models
---

# LCES: Zero-shot Automated Essay Scoring via Pairwise Comparisons Using Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08498" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08498v2</a>
  <a href="https://arxiv.org/pdf/2505.08498.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08498v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08498v2', 'LCES: Zero-shot Automated Essay Scoring via Pairwise Comparisons Using Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Takumi Shibata, Yuichi Miyamura

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-13 (更新: 2025-09-21)

**备注**: Accepted to EMNLP 2025 (Main Conference)

---

## 💡 一句话要点

**提出LCES方法以解决零-shot自动化作文评分的偏差问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动化评分` `大型语言模型` `成对比较` `教育技术` `机器学习`

## 📋 核心要点

1. 现有的零-shot自动化作文评分方法依赖于LLMs直接生成分数，容易受到模型偏差影响，导致评分不一致。
2. 本文提出LCES方法，将作文评分转化为成对比较任务，通过判断两篇作文的优劣来生成分数，提升评分的准确性。
3. 实验结果显示，LCES在多个AES基准数据集上表现优于传统方法，且在不同LLM基础上具有良好的鲁棒性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步使得零-shot自动化作文评分（AES）成为可能，这为减少人工评分的成本和工作量提供了有希望的解决方案。然而，现有的零-shot方法通常依赖LLMs直接生成绝对分数，这些分数往往因模型偏差和评分不一致而与人类评估相悖。为了解决这些问题，本文提出了一种基于LLM的比较作文评分（LCES）方法，将AES形式化为成对比较任务。具体而言，我们指示LLMs判断两个作文中哪个更好，收集大量这样的比较，并将其转换为连续分数。通过采用RankNet，我们提高了可扩展性，实验结果表明，LCES在准确性上优于传统的零-shot方法，同时保持计算效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有零-shot自动化作文评分方法中，由于直接生成绝对分数而导致的评分偏差和不一致性问题。

**核心思路**：LCES方法通过将作文评分转化为成对比较任务，指示LLMs判断两篇作文的优劣，从而避免了直接评分的偏差。

**技术框架**：整体流程包括：首先收集大量作文对的比较结果，然后利用RankNet将LLM的偏好转化为标量分数，最后生成连续的评分结果。

**关键创新**：LCES的主要创新在于将评分任务转化为成对比较，显著提高了评分的准确性和鲁棒性，与传统方法相比，避免了绝对评分的偏差问题。

**关键设计**：在RankNet的应用中，设置了适当的损失函数以优化模型的比较能力，同时确保了模型在不同LLM基础上的适用性。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，LCES在多个AES基准数据集上表现优于传统零-shot方法，准确性提升幅度达到XX%，同时保持了良好的计算效率，显示出在不同LLM基础上的鲁棒性。

## 🎯 应用场景

该研究的潜在应用领域包括教育评估、在线学习平台和自动化评分系统等。通过提高作文评分的准确性和效率，LCES方法能够显著减轻教师的评分负担，并为学生提供更及时的反馈，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled zero-shot automated essay scoring (AES), providing a promising way to reduce the cost and effort of essay scoring in comparison with manual grading. However, most existing zero-shot approaches rely on LLMs to directly generate absolute scores, which often diverge from human evaluations owing to model biases and inconsistent scoring. To address these limitations, we propose LLM-based Comparative Essay Scoring (LCES), a method that formulates AES as a pairwise comparison task. Specifically, we instruct LLMs to judge which of two essays is better, collect many such comparisons, and convert them into continuous scores. Considering that the number of possible comparisons grows quadratically with the number of essays, we improve scalability by employing RankNet to efficiently transform LLM preferences into scalar scores. Experiments using AES benchmark datasets show that LCES outperforms conventional zero-shot methods in accuracy while maintaining computational efficiency. Moreover, LCES is robust across different LLM backbones, highlighting its applicability to real-world zero-shot AES.

