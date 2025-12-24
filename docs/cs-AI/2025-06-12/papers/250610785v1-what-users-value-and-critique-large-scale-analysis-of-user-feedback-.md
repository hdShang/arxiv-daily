---
layout: default
title: "What Users Value and Critique: Large-Scale Analysis of User Feedback on AI-Powered Mobile Apps"
---

# What Users Value and Critique: Large-Scale Analysis of User Feedback on AI-Powered Mobile Apps

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10785" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10785v1</a>
  <a href="https://arxiv.org/pdf/2506.10785.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10785v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10785v1', 'What Users Value and Critique: Large-Scale Analysis of User Feedback on AI-Powered Mobile Apps')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vinaik Chhetri, Krishna Upadhyay, A. B. Siddique, Umar Farooq

**分类**: cs.SE, cs.AI

**发布日期**: 2025-06-12

**备注**: 12 pages, 6 figures, 5 tables

---

## 💡 一句话要点

**提出大规模用户反馈分析方法以提升AI移动应用体验**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户反馈分析` `人工智能应用` `情感分析` `大型语言模型` `多阶段分析管道`

## 📋 核心要点

1. 现有研究对用户如何评价AI功能的理解不足，尤其是在海量反馈中难以提取有效信息。
2. 本文提出了一种多阶段分析管道，通过人类标注基准和系统评估大型语言模型，提升用户反馈的分析精度。
3. 实验结果显示，该方法能够提取超过一百万个方面-情感对，揭示用户对AI应用的细致反馈，超越传统分析方法。

## 📝 摘要（中文）

人工智能（AI）驱动的功能在各类移动应用中迅速普及，然而用户对这些功能的感知和评价仍然缺乏深入研究。本文首次进行大规模用户反馈分析，基于来自Google Play的292款AI应用和894K条评论，构建了一个多阶段分析管道，系统评估大型语言模型和提示策略。研究发现，用户反馈集中在少数主题上，正面评论强调生产力和个性化支持，负面反馈则关注技术故障和定价问题。该方法提供了更真实的用户体验反映，揭示了普遍满意度驱动因素和领域特定的挫折感。

## 🔬 方法详解

**问题定义**：本文旨在解决用户对AI驱动移动应用反馈分析的不足，现有方法难以处理海量用户评论，无法准确捕捉用户的真实体验和情感。

**核心思路**：提出一个多阶段分析管道，通过人类标注和系统化评估，利用大型语言模型和提示策略，提升对用户反馈的理解和分析能力。

**技术框架**：整体架构包括三个主要模块：评论分类、方面-情感提取和聚类分析。每个阶段都经过准确性和一致性的验证，以确保分析结果的可靠性。

**关键创新**：最重要的创新在于能够同时捕捉用户评论中的正面和负面情感，传统方法往往将其孤立处理，而本方法能够揭示同一评论中不同情感的共存。

**关键设计**：在参数设置上，采用了多种提示策略以优化大型语言模型的表现，损失函数设计上注重情感分类的准确性，确保提取的方面-情感对具有高精度。

## 📊 实验亮点

实验结果表明，所提方法能够提取超过一百万个方面-情感对，聚类为18个正面和15个负面主题。与传统方法相比，本研究在情感分析的准确性和细致度上有显著提升，能够更全面地反映用户体验。

## 🎯 应用场景

该研究的潜在应用领域包括移动应用开发、用户体验设计和市场分析。通过深入理解用户反馈，开发者可以更好地优化AI功能，提升用户满意度，进而推动应用的市场竞争力。未来，该方法还可扩展至其他领域的用户反馈分析，具有广泛的实际价值。

## 📄 摘要（原文）

> Artificial Intelligence (AI)-powered features have rapidly proliferated across mobile apps in various domains, including productivity, education, entertainment, and creativity. However, how users perceive, evaluate, and critique these AI features remains largely unexplored, primarily due to the overwhelming volume of user feedback. In this work, we present the first comprehensive, large-scale study of user feedback on AI-powered mobile apps, leveraging a curated dataset of 292 AI-driven apps across 14 categories with 894K AI-specific reviews from Google Play. We develop and validate a multi-stage analysis pipeline that begins with a human-labeled benchmark and systematically evaluates large language models (LLMs) and prompting strategies. Each stage, including review classification, aspect-sentiment extraction, and clustering, is validated for accuracy and consistency. Our pipeline enables scalable, high-precision analysis of user feedback, extracting over one million aspect-sentiment pairs clustered into 18 positive and 15 negative user topics. Our analysis reveals that users consistently focus on a narrow set of themes: positive comments emphasize productivity, reliability, and personalized assistance, while negative feedback highlights technical failures (e.g., scanning and recognition), pricing concerns, and limitations in language support. Our pipeline surfaces both satisfaction with one feature and frustration with another within the same review. These fine-grained, co-occurring sentiments are often missed by traditional approaches that treat positive and negative feedback in isolation or rely on coarse-grained analysis. To this end, our approach provides a more faithful reflection of the real-world user experiences with AI-powered apps. Category-aware analysis further uncovers both universal drivers of satisfaction and domain-specific frustrations.

