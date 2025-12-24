---
layout: default
title: Re$^2$: A Consistency-ensured Dataset for Full-stage Peer Review and Multi-turn Rebuttal Discussions
---

# Re$^2$: A Consistency-ensured Dataset for Full-stage Peer Review and Multi-turn Rebuttal Discussions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07920" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07920v1</a>
  <a href="https://arxiv.org/pdf/2505.07920.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07920v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07920v1', 'Re$^2$: A Consistency-ensured Dataset for Full-stage Peer Review and Multi-turn Rebuttal Discussions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daoze Zhang, Zhijian Bao, Sihang Du, Zhiyi Zhao, Kuangling Zhang, Dezheng Bao, Yang Yang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-12

**备注**: 2 figures, 5 tables

---

## 💡 一句话要点

**提出Re^2数据集以解决同行评审和反驳讨论中的数据不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `同行评审` `反驳讨论` `数据集` `多轮对话` `大型语言模型` `评审质量` `自我评估工具`

## 📋 核心要点

1. 现有同行评审数据集面临数据多样性不足和质量不一致的问题，影响了评审效果。
2. 本文提出Re^2数据集，包含大量初始提交和多轮反驳讨论，旨在提升数据质量和多样性。
3. 通过构建多轮对话框架，Re^2为传统评审任务和动态交互助手提供了支持，提升了评审效率。

## 📝 摘要（中文）

同行评审是科学进步的重要组成部分，但随着投稿量的快速增加，评审系统面临压力，导致评审人员短缺和评审质量下降。现有的同行评审数据集存在数据多样性不足、数据质量不一致以及对反驳和作者-评审者互动支持不足等问题。为了解决这些挑战，本文提出了名为Re^2的最大一致性保障的同行评审和反驳数据集，包含19,926个初始提交、70,668条评审评论和53,818条反驳，支持多轮对话范式，旨在为作者提供更实用的指导，减轻评审负担。

## 🔬 方法详解

**问题定义**：本文旨在解决现有同行评审数据集在数据多样性、质量不一致及对反驳支持不足等方面的痛点。这些问题限制了大型语言模型在评审过程中的有效应用。

**核心思路**：提出Re^2数据集，通过收集初始提交和反驳评论，构建一个多轮对话框架，以支持动态交互和传统评审任务，从而提高数据的实用性和质量。

**技术框架**：Re^2数据集的整体架构包括初始提交、评审评论和反驳三个主要模块，采用多轮对话的形式来模拟真实的评审和反驳过程，确保数据的一致性和多样性。

**关键创新**：Re^2数据集的最大创新在于其规模和一致性保障，包含大量初始提交和反驳，填补了现有数据集在多轮互动和反驳支持方面的空白。

**关键设计**：在数据收集过程中，确保了初始提交的多样性和质量，采用了严格的筛选标准，确保每条评论和反驳都具有高质量和一致性。

## 📊 实验亮点

Re^2数据集包含19,926个初始提交和70,668条评审评论，显著提升了数据的多样性和一致性。通过多轮对话框架，支持动态交互，帮助作者更好地完善稿件，减轻评审负担。

## 🎯 应用场景

Re^2数据集的潜在应用领域包括学术论文的同行评审、自动化评审助手的开发以及学术写作的自我评估工具。其实际价值在于提升评审效率和质量，未来可能对科学研究的进展产生积极影响。

## 📄 摘要（原文）

> Peer review is a critical component of scientific progress in the fields like AI, but the rapid increase in submission volume has strained the reviewing system, which inevitably leads to reviewer shortages and declines review quality. Besides the growing research popularity, another key factor in this overload is the repeated resubmission of substandard manuscripts, largely due to the lack of effective tools for authors to self-evaluate their work before submission. Large Language Models (LLMs) show great promise in assisting both authors and reviewers, and their performance is fundamentally limited by the quality of the peer review data. However, existing peer review datasets face three major limitations: (1) limited data diversity, (2) inconsistent and low-quality data due to the use of revised rather than initial submissions, and (3) insufficient support for tasks involving rebuttal and reviewer-author interactions. To address these challenges, we introduce the largest consistency-ensured peer review and rebuttal dataset named Re^2, which comprises 19,926 initial submissions, 70,668 review comments, and 53,818 rebuttals from 24 conferences and 21 workshops on OpenReview. Moreover, the rebuttal and discussion stage is framed as a multi-turn conversation paradigm to support both traditional static review tasks and dynamic interactive LLM assistants, providing more practical guidance for authors to refine their manuscripts and helping alleviate the growing review burden. Our data and code are available in https://anonymous.4open.science/r/ReviewBench_anon/.

