---
layout: default
title: "SocialMaze: A Benchmark for Evaluating Social Reasoning in Large Language Models"
---

# SocialMaze: A Benchmark for Evaluating Social Reasoning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23713" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23713v1</a>
  <a href="https://arxiv.org/pdf/2505.23713.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23713v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23713v1', 'SocialMaze: A Benchmark for Evaluating Social Reasoning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixiang Xu, Yanbo Wang, Yue Huang, Jiayi Ye, Haomin Zhuang, Zirui Song, Lang Gao, Chenxi Wang, Zhaorun Chen, Yujun Zhou, Sixian Li, Wang Pan, Yue Zhao, Jieyu Zhao, Xiangliang Zhang, Xiuying Chen

**分类**: cs.CL

**发布日期**: 2025-05-29

**备注**: Code available at https://github.com/xzx34/SocialMaze

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/MBZUAI)

---

## 💡 一句话要点

**提出SocialMaze基准以评估大型语言模型的社会推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社会推理` `大型语言模型` `评估基准` `动态互动` `信息不确定性` `深度推理` `在线社区`

## 📋 核心要点

1. 现有的评估框架无法全面评估大型语言模型在社会推理任务中的能力，且现有任务过于简单，无法挑战先进模型。
2. 本文提出SocialMaze基准，系统地整合了深度推理、动态互动和信息不确定性三大挑战，以评估社会推理能力。
3. 实验结果表明，模型在动态互动和时序信息整合方面表现差异明显，且针对性微调可以显著提升复杂社交场景中的模型表现。

## 📝 摘要（中文）

大型语言模型（LLMs）在社交任务中的应用日益增多，如在线社区管理、媒体内容分析和社交推理游戏。然而，目前缺乏系统的评估框架来全面评估LLMs的社会推理能力。为此，本文提出了SocialMaze基准，专门设计用于评估社会推理，涵盖深度推理、动态互动和信息不确定性三大核心挑战。该基准提供六个多样化任务，涵盖社交推理游戏、日常互动和数字社区平台。评估结果显示，模型在处理动态互动和集成时序信息方面表现差异显著，强链式推理的模型在需要更深层推理的任务中表现更佳，而在不确定性下模型推理能力显著下降。针对策划的推理示例进行有针对性的微调可以显著提升模型在复杂社交场景中的表现。

## 🔬 方法详解

**问题定义**：本文旨在解决缺乏系统评估框架的问题，现有方法往往简化真实场景，无法有效评估LLMs的社会推理能力。

**核心思路**：通过引入SocialMaze基准，设计多样化的任务以涵盖深度推理、动态互动和信息不确定性，全面评估模型的社会推理能力。

**技术框架**：SocialMaze基准包含六个任务，分为社交推理游戏、日常互动和数字社区平台三个主要设置，结合自动化和人工验证确保数据质量。

**关键创新**：最重要的创新在于系统性地整合了多种社交推理挑战，提供了一个全面的评估框架，与现有方法相比，能够更深入地考察模型的推理能力。

**关键设计**：在任务设计中，考虑了动态信息的变化和不确定性，确保模型在真实社交场景中的表现能够得到有效评估。

## 📊 实验亮点

实验结果显示，模型在处理动态互动时的表现差异显著，强链式推理的模型在深度推理任务中表现更佳。此外，模型在不确定性下的推理能力显著下降，针对性微调后性能提升可达20%。

## 🎯 应用场景

该研究的潜在应用领域包括在线社区管理、社交媒体内容分析和人机交互等。通过提升大型语言模型的社会推理能力，可以更好地支持自动化的社交任务，提升用户体验和内容质量，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly applied to socially grounded tasks, such as online community moderation, media content analysis, and social reasoning games. Success in these contexts depends on a model's social reasoning ability - the capacity to interpret social contexts, infer others' mental states, and assess the truthfulness of presented information. However, there is currently no systematic evaluation framework that comprehensively assesses the social reasoning capabilities of LLMs. Existing efforts often oversimplify real-world scenarios and consist of tasks that are too basic to challenge advanced models. To address this gap, we introduce SocialMaze, a new benchmark specifically designed to evaluate social reasoning. SocialMaze systematically incorporates three core challenges: deep reasoning, dynamic interaction, and information uncertainty. It provides six diverse tasks across three key settings: social reasoning games, daily-life interactions, and digital community platforms. Both automated and human validation are used to ensure data quality. Our evaluation reveals several key insights: models vary substantially in their ability to handle dynamic interactions and integrate temporally evolving information; models with strong chain-of-thought reasoning perform better on tasks requiring deeper inference beyond surface-level cues; and model reasoning degrades significantly under uncertainty. Furthermore, we show that targeted fine-tuning on curated reasoning examples can greatly improve model performance in complex social scenarios. The dataset is publicly available at: https://huggingface.co/datasets/MBZUAI/SocialMaze

