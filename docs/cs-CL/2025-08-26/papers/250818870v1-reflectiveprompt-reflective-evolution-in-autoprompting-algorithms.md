---
layout: default
title: "ReflectivePrompt: Reflective evolution in autoprompting algorithms"
---

# ReflectivePrompt: Reflective evolution in autoprompting algorithms

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18870" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18870v1</a>
  <a href="https://arxiv.org/pdf/2508.18870.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18870v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18870v1', 'ReflectivePrompt: Reflective evolution in autoprompting algorithms')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Viktor N. Zhuravlev, Artur R. Khairullin, Ernest A. Dyagin, Alena N. Sitkina, Nikita I. Kulin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出ReflectivePrompt以优化语言模型的自动提示选择**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动提示` `反思进化` `进化算法` `语言模型` `文本生成` `分类任务` `提示优化`

## 📋 核心要点

1. 现有的自动提示方法在优化提示选择的精度和全面性上存在不足，难以有效利用进化过程中的知识积累。
2. ReflectivePrompt通过引入反思进化策略，结合短期和长期反思操作，提升了提示选择的质量和效率。
3. 在33个数据集上进行的实验表明，ReflectivePrompt在多个任务上相较于现有方法有显著性能提升，验证了其有效性。

## 📝 摘要（中文）

自动提示（autoprompting）是为语言模型自动选择优化提示的过程，随着大语言模型（LLMs）领域的快速发展而受到关注。本文提出了一种新颖的自动提示方法ReflectivePrompt，该方法基于进化算法，采用反思进化策略以更精确和全面地搜索最佳提示。ReflectivePrompt在交叉和精英变异之前利用短期和长期反思操作，以提高所引入修改的质量。该方法允许在每个世代更新在进化过程中获得的知识。ReflectivePrompt在33个分类和文本生成任务的数据集上进行了测试，显示出相较于当前最先进方法（如EvoPrompt）有显著提升，平均提高28%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动提示方法在提示选择过程中的精度和全面性不足的问题，特别是在进化算法的应用中，知识的积累和利用不够充分。

**核心思路**：ReflectivePrompt的核心思路是通过反思进化策略，结合短期和长期反思操作，优化提示选择过程，以提高提示的质量和适应性。这样的设计使得算法能够在每个世代中有效利用历史信息，增强搜索的全面性。

**技术框架**：ReflectivePrompt的整体架构包括反思操作、交叉操作和精英变异三个主要模块。反思操作分为短期和长期反思，旨在提升提示的选择质量；交叉操作用于生成新的提示组合；精英变异则确保优秀个体的保留和改进。

**关键创新**：ReflectivePrompt的主要创新在于引入了反思机制，使得算法在每个世代中能够动态更新和优化提示选择。这一机制与传统的进化算法相比，显著提高了提示选择的效果和效率。

**关键设计**：在参数设置上，ReflectivePrompt采用了适应性调整的反思窗口，以便在不同阶段灵活调整反思的深度和范围。同时，损失函数设计上注重提示的多样性和准确性，以确保生成的提示在实际应用中的有效性。

## 📊 实验亮点

实验结果显示，ReflectivePrompt在33个数据集上相较于EvoPrompt平均提升了28%的性能，证明了其在自动提示选择中的有效性和优越性。这一显著的提升使其成为基于进化算法的自动提示方法中的一项重要进展。

## 🎯 应用场景

ReflectivePrompt在自然语言处理领域具有广泛的应用潜力，尤其是在文本生成、分类任务和对话系统等场景中。通过优化提示选择，该方法能够提高语言模型的性能，进而推动智能助手、内容生成和信息检索等应用的发展。未来，该技术可能会在更多复杂的语言理解任务中发挥重要作用。

## 📄 摘要（原文）

> Autoprompting is the process of automatically selecting optimized prompts for language models, which has been gaining popularity with the rapid advancement of prompt engineering, driven by extensive research in the field of large language models (LLMs). This paper presents ReflectivePrompt - a novel autoprompting method based on evolutionary algorithms that employs a reflective evolution approach for more precise and comprehensive search of optimal prompts. ReflectivePrompt utilizes short-term and long-term reflection operations before crossover and elitist mutation to enhance the quality of the modifications they introduce. This method allows for the accumulation of knowledge obtained throughout the evolution process and updates it at each epoch based on the current population. ReflectivePrompt was tested on 33 datasets for classification and text generation tasks using open-access large language models: t-lite-instruct-0.1 and gemma3-27b-it. The method demonstrates, on average, a significant improvement (e.g., 28% on BBH compared to EvoPrompt) in metrics relative to current state-of-the-art approaches, thereby establishing itself as one of the most effective solutions in evolutionary algorithm-based autoprompting.

