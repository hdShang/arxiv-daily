---
layout: default
title: "AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment"
---

# AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04089" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04089v1</a>
  <a href="https://arxiv.org/pdf/2506.04089.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04089v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04089v1', 'AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anastasiia Ivanova, Eva Bakaeva, Zoya Volovikova, Alexey K. Kovalev, Aleksandr I. Panov

**分类**: cs.LG, cs.AI, cs.CL, cs.RO

**发布日期**: 2025-06-04

**备注**: ACL 2025 (Main Conference)

**🔗 代码/项目**: [GITHUB](https://github.com/cog-model/AmbiK-dataset)

---

## 💡 一句话要点

**提出AmbiK数据集以解决厨房环境中的任务模糊性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `模糊任务` `厨房环境` `大型语言模型` `数据集` `人机交互` `机器人导航` `智能家居`

## 📋 核心要点

1. 现有方法在处理现实环境中的模糊指令时面临挑战，缺乏统一的基准数据集进行比较。
2. 论文提出AmbiK数据集，包含厨房环境中模糊指令的文本数据，旨在为模糊性检测提供标准化测试平台。
3. AmbiK数据集经过人工验证，包含2000个任务，涵盖多种模糊性类型，促进研究的系统性和可比性。

## 📝 摘要（中文）

在具身智能体中，大型语言模型（LLMs）通常用于根据用户的自然语言指令进行行为规划。然而，处理现实环境中的模糊指令仍然是LLMs面临的挑战。为此，本文提出了AmbiK（厨房环境中的模糊任务数据集），这是一个完全基于文本的模糊指令数据集，专门针对厨房环境中的机器人。AmbiK数据集由LLMs协助收集，并经过人工验证，包含1000对模糊任务及其明确对应任务，按模糊性类型（人类偏好、常识知识、安全性）分类，提供环境描述、澄清问题及答案、用户意图和任务计划，总计2000个任务。我们希望AmbiK能够帮助研究人员对模糊性检测方法进行统一比较。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在厨房环境中处理模糊指令的能力不足，现有方法缺乏统一的数据集进行有效比较。

**核心思路**：通过构建AmbiK数据集，提供标准化的模糊任务指令，帮助研究人员评估和比较不同的模糊性检测方法。

**技术框架**：AmbiK数据集由1000对模糊任务及其明确对应任务组成，分类为人类偏好、常识知识和安全性，包含环境描述、澄清问题及答案、用户意图和任务计划。

**关键创新**：AmbiK数据集的创新在于其全面性和系统性，提供了一个统一的基准，使得不同模糊性检测方法的比较成为可能。

**关键设计**：数据集的设计包括对模糊性类型的详细分类，并通过LLMs生成和人工验证，确保数据的准确性和有效性。数据集可在GitHub上获取。

## 📊 实验亮点

AmbiK数据集包含2000个任务，涵盖多种模糊性类型，提供了一个统一的基准，促进了模糊性检测方法的比较。该数据集的构建为未来的研究提供了重要的实验基础，推动了相关领域的发展。

## 🎯 应用场景

AmbiK数据集的潜在应用领域包括机器人导航、智能家居系统和人机交互等。通过提供标准化的模糊任务指令，研究人员可以更好地训练和评估机器人在复杂环境中的决策能力，推动智能体的实际应用和发展。

## 📄 摘要（原文）

> As a part of an embodied agent, Large Language Models (LLMs) are typically used for behavior planning given natural language instructions from the user. However, dealing with ambiguous instructions in real-world environments remains a challenge for LLMs. Various methods for task ambiguity detection have been proposed. However, it is difficult to compare them because they are tested on different datasets and there is no universal benchmark. For this reason, we propose AmbiK (Ambiguous Tasks in Kitchen Environment), the fully textual dataset of ambiguous instructions addressed to a robot in a kitchen environment. AmbiK was collected with the assistance of LLMs and is human-validated. It comprises 1000 pairs of ambiguous tasks and their unambiguous counterparts, categorized by ambiguity type (Human Preferences, Common Sense Knowledge, Safety), with environment descriptions, clarifying questions and answers, user intents, and task plans, for a total of 2000 tasks. We hope that AmbiK will enable researchers to perform a unified comparison of ambiguity detection methods. AmbiK is available at https://github.com/cog-model/AmbiK-dataset.

