---
layout: default
title: "Prompting Strategies for Language Model-Based Item Generation in K-12 Education: Bridging the Gap Between Small and Large Language Models"
---

# Prompting Strategies for Language Model-Based Item Generation in K-12 Education: Bridging the Gap Between Small and Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20217" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20217v1</a>
  <a href="https://arxiv.org/pdf/2508.20217.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20217v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20217v1', 'Prompting Strategies for Language Model-Based Item Generation in K-12 Education: Bridging the Gap Between Small and Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Amini, Babak Ahmadi, Xiaomeng Xiong, Yilin Zhang, Christopher Qiao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出结构化提示策略以提升K-12教育中的题目生成质量**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动生成题目` `语言模型` `K-12教育` `结构化提示` `微调策略` `评估工具` `机器学习`

## 📋 核心要点

1. 现有的手动测试开发方法成本高且不一致，难以满足K-12教育的需求。
2. 本研究提出通过结构化提示策略来优化中型语言模型的题目生成能力，尤其是结合思维链和顺序设计。
3. 实验结果表明，Gemma模型在生成的题目质量上显著优于GPT-3.5，且提示设计对模型性能至关重要。

## 📝 摘要（中文）

本研究探讨了利用语言模型自动生成多项选择题（MCQs）以进行形态评估，旨在降低人工测试开发的成本和不一致性。研究采用了双重方法，首先比较了经过微调的中型模型（Gemma, 2B）与未调优的大型模型（GPT-3.5, 175B）。其次，评估了七种结构化提示策略，包括零-shot、few-shot、思维链、角色基础、顺序和组合。生成的题目通过自动化指标和专家评分在五个维度上进行评估。结果显示，结构化提示，尤其是结合思维链和顺序设计的策略，显著改善了Gemma的输出。Gemma通常生成的题目在构建对齐和教学适宜性方面优于GPT-3.5的零-shot响应，提示设计在中型模型性能中起到了关键作用。该研究展示了结构化提示和高效微调如何在有限数据条件下提升中型模型的自动生成能力。

## 🔬 方法详解

**问题定义**：本研究旨在解决K-12教育中手动测试开发的高成本和不一致性问题。现有方法在题目生成上缺乏效率和一致性，导致教育评估的质量受到影响。

**核心思路**：论文提出通过结构化提示策略来提升中型语言模型（Gemma）的题目生成能力，尤其是结合思维链和顺序设计，以提高生成题目的质量和适应性。

**技术框架**：研究采用双重方法，首先比较了微调的中型模型与未调优的大型模型，其次评估了七种不同的结构化提示策略。生成的题目通过自动化指标和专家评分进行评估，确保其质量和适应性。

**关键创新**：最重要的创新点在于提出了多种结构化提示策略，特别是思维链与顺序设计的结合，显著提升了中型模型在题目生成上的表现，与传统的零-shot方法相比，效果更佳。

**关键设计**：在实验中，采用了多种提示策略，设置了不同的参数以适应模型的微调过程，使用自动化评分与专家评分相结合的方式来评估生成题目的质量。

## 📊 实验亮点

实验结果显示，Gemma模型在生成的题目质量上显著优于GPT-3.5的零-shot响应，尤其在构建对齐和教学适宜性方面表现突出。结合思维链和顺序设计的结构化提示策略使Gemma的输出质量提升了显著的幅度，验证了提示设计的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括K-12教育的评估工具开发，能够为教师提供高质量的自动生成测试题目，减轻其工作负担。此外，研究成果可推广至其他教育领域，提升教育评估的效率和一致性。

## 📄 摘要（原文）

> This study explores automatic generation (AIG) using language models to create multiple choice questions (MCQs) for morphological assessment, aiming to reduce the cost and inconsistency of manual test development. The study used a two-fold approach. First, we compared a fine-tuned medium model (Gemma, 2B) with a larger untuned one (GPT-3.5, 175B). Second, we evaluated seven structured prompting strategies, including zero-shot, few-shot, chain-of-thought, role-based, sequential, and combinations. Generated items were assessed using automated metrics and expert scoring across five dimensions. We also used GPT-4.1, trained on expert-rated samples, to simulate human scoring at scale. Results show that structured prompting, especially strategies combining chain-of-thought and sequential design, significantly improved Gemma's outputs. Gemma generally produced more construct-aligned and instructionally appropriate items than GPT-3.5's zero-shot responses, with prompt design playing a key role in mid-size model performance. This study demonstrates that structured prompting and efficient fine-tuning can enhance midsized models for AIG under limited data conditions. We highlight the value of combining automated metrics, expert judgment, and large-model simulation to ensure alignment with assessment goals. The proposed workflow offers a practical and scalable way to develop and validate language assessment items for K-12.

