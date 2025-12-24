---
layout: default
title: Creative Preference Optimization
---

# Creative Preference Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14442" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14442v2</a>
  <a href="https://arxiv.org/pdf/2505.14442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14442v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14442v2', 'Creative Preference Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mete Ismayilzada, Antonio Laverghetta, Simone A. Luchini, Reet Patel, Antoine Bosselut, Lonneke van der Plas, Roger Beaty

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-09-19)

**备注**: Accepted to EMNLP 2025 Findings

---

## 💡 一句话要点

**提出创意偏好优化方法以提升LLM的创造力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `创造力优化` `偏好学习` `自然语言生成` `心理评估`

## 📋 核心要点

1. 现有方法在提升大型语言模型的创造力方面存在局限，往往只关注单一维度，未能全面考虑创造力的多样性和复杂性。
2. 本文提出创意偏好优化（CrPO）方法，通过模块化方式将多种创造力维度的信号整合到偏好优化目标中，以提升模型的创造性。
3. 实验结果表明，使用CrPO的模型在新颖性、多样性和惊喜性方面均优于强基线模型，且输出质量保持高水平。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）在自然语言生成任务中表现出色，但其生成真正具有创造性的内容的能力仍然有限。现有增强LLM创造力的方法往往过于关注多样性或特定任务，未能全面解决创造力的多维特性。本文提出了一种新颖的对齐方法——创意偏好优化（CrPO），通过模块化方式将多个创造力维度的信号注入偏好优化目标中。我们使用CrPO和一个新的大规模人类偏好数据集MuCE训练和评估了多个增强创造力的模型，结果显示这些模型在自动和人工评估中均优于强基线模型GPT-4o，生成的内容在新颖性、多样性和惊喜性上表现更佳，同时保持高输出质量。进一步的NoveltyBench评估进一步确认了我们方法的普适性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成创造性内容时的局限性，现有方法往往只关注多样性或特定任务，未能全面提升创造力的多维特性。

**核心思路**：提出创意偏好优化（CrPO）方法，通过将多个创造力维度的信号注入偏好优化目标，增强模型的创造性表现。该方法的设计旨在全面提升生成内容的质量和多样性。

**技术框架**：整体架构包括数据收集、模型训练和评估三个主要阶段。首先，构建一个包含超过20万个响应和来自30多种心理创造力评估的数据集MuCE；然后，利用CrPO对多个模型进行训练；最后，通过自动和人工评估对生成结果进行验证。

**关键创新**：CrPO方法的核心创新在于其模块化的信号注入方式，能够同时考虑多个创造力维度，从而实现更全面的优化。这与现有方法的单一维度优化形成了鲜明对比。

**关键设计**：在模型训练中，采用特定的损失函数来平衡不同创造力维度的影响，同时优化生成内容的质量。模型结构上，结合了最新的LLM架构，以确保在生成过程中能够有效捕捉创造性特征。

## 📊 实验亮点

实验结果显示，使用CrPO的模型在新颖性、多样性和惊喜性方面均显著优于基线模型GPT-4o，具体表现为生成内容的质量提升，同时在NoveltyBench评估中也验证了方法的普适性。

## 🎯 应用场景

该研究的潜在应用领域包括创意写作、广告文案生成、游戏内容创作等，能够为这些领域提供更具创新性和吸引力的内容生成方案。未来，该方法可能推动更广泛的人工智能创意应用，提升人机协作的创造力水平。

## 📄 摘要（原文）

> While Large Language Models (LLMs) have demonstrated impressive performance across natural language generation tasks, their ability to generate truly creative content-characterized by novelty, diversity, surprise, and quality-remains limited. Existing methods for enhancing LLM creativity often focus narrowly on diversity or specific tasks, failing to address creativity's multifaceted nature in a generalizable way. In this work, we propose Creative Preference Optimization (CrPO), a novel alignment method that injects signals from multiple creativity dimensions into the preference optimization objective in a modular fashion. We train and evaluate creativity-augmented versions of several models using CrPO and MuCE, a new large-scale human preference dataset spanning over 200,000 human-generated responses and ratings from more than 30 psychological creativity assessments. Our models outperform strong baselines, including GPT-4o, on both automated and human evaluations, producing more novel, diverse, and surprising generations while maintaining high output quality. Additional evaluations on NoveltyBench further confirm the generalizability of our approach. Together, our results demonstrate that directly optimizing for creativity within preference frameworks is a promising direction for advancing the creative capabilities of LLMs without compromising output quality.

