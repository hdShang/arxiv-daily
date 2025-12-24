---
layout: default
title: "SGSimEval: A Comprehensive Multifaceted and Similarity-Enhanced Benchmark for Automatic Survey Generation Systems"
---

# SGSimEval: A Comprehensive Multifaceted and Similarity-Enhanced Benchmark for Automatic Survey Generation Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11310" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11310v1</a>
  <a href="https://arxiv.org/pdf/2508.11310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11310v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11310v1', 'SGSimEval: A Comprehensive Multifaceted and Similarity-Enhanced Benchmark for Automatic Survey Generation Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Beichen Guo, Zhiyuan Wen, Yu Yang, Peng Gao, Ruosong Yang, Jiaxing Shen

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-08-15

**备注**: Accepted to The 21st International Conference on Advanced Data Mining and Applications (ADMA2025)

---

## 💡 一句话要点

**提出SGSimEval以解决自动调查生成系统评估不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动调查生成` `评估方法` `大型语言模型` `多维度评估` `人类偏好`

## 📋 核心要点

1. 现有的自动调查生成评估方法存在偏见和缺乏人类偏好的问题，影响了评估的准确性。
2. 本文提出SGSimEval，通过综合评估大纲、内容和参考文献，构建了一个多维度的评估框架。
3. 实验结果显示，当前ASG系统在大纲生成上与人类相当，但在内容和参考文献生成方面仍需改进。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的进步，自动调查生成（ASG）引起了越来越多的关注。然而，现有评估方法存在偏见指标、缺乏人类偏好和过度依赖LLMs作为评判者等问题。为了解决这些挑战，本文提出了SGSimEval，一个综合性的调查生成基准，结合了大纲、内容和参考文献的评估，并将基于LLMs的评分与定量指标相结合，提供了多维度的评估框架。实验表明，当前的ASG系统在大纲生成上表现出与人类相当的优越性，但在内容和参考文献生成方面仍有显著提升空间，且我们的评估指标与人类评估保持强一致性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动调查生成系统评估方法的不足，包括偏见指标和缺乏人类偏好等痛点。

**核心思路**：SGSimEval通过结合大纲、内容和参考文献的评估，提供了一个综合的评估框架，强调人类偏好和相似性。

**技术框架**：SGSimEval的整体架构包括三个主要模块：大纲评估、内容评估和参考文献评估，结合LLMs评分与定量指标。

**关键创新**：最重要的创新在于引入了人类偏好指标，强调了生成内容的内在质量和与人类的相似性，这与现有方法的单一评估方式有本质区别。

**关键设计**：在参数设置上，SGSimEval采用了多种定量指标与LLMs评分相结合的方式，确保评估的全面性和准确性。具体的损失函数和网络结构设计尚未详细披露，属于未知领域。

## 📊 实验亮点

实验结果表明，当前的ASG系统在大纲生成方面与人类表现相当，但在内容和参考文献生成上仍有显著提升空间。SGSimEval的评估指标与人类评估保持强一致性，显示出其在评估准确性上的优势。

## 🎯 应用场景

SGSimEval的研究成果可广泛应用于教育、市场调研和社会科学等领域，帮助研究人员和从业者更高效地生成和评估调查问卷。未来，该方法可能推动自动化调查生成技术的进一步发展，提高其在实际应用中的可靠性和有效性。

## 📄 摘要（原文）

> The growing interest in automatic survey generation (ASG), a task that traditionally required considerable time and effort, has been spurred by recent advances in large language models (LLMs). With advancements in retrieval-augmented generation (RAG) and the rising popularity of multi-agent systems (MASs), synthesizing academic surveys using LLMs has become a viable approach, thereby elevating the need for robust evaluation methods in this domain. However, existing evaluation methods suffer from several limitations, including biased metrics, a lack of human preference, and an over-reliance on LLMs-as-judges. To address these challenges, we propose SGSimEval, a comprehensive benchmark for Survey Generation with Similarity-Enhanced Evaluation that evaluates automatic survey generation systems by integrating assessments of the outline, content, and references, and also combines LLM-based scoring with quantitative metrics to provide a multifaceted evaluation framework. In SGSimEval, we also introduce human preference metrics that emphasize both inherent quality and similarity to humans. Extensive experiments reveal that current ASG systems demonstrate human-comparable superiority in outline generation, while showing significant room for improvement in content and reference generation, and our evaluation metrics maintain strong consistency with human assessments.

