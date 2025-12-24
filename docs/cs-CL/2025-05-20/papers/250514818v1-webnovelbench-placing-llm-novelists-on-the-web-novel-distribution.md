---
layout: default
title: "WebNovelBench: Placing LLM Novelists on the Web Novel Distribution"
---

# WebNovelBench: Placing LLM Novelists on the Web Novel Distribution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14818" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14818v1</a>
  <a href="https://arxiv.org/pdf/2505.14818.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14818v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14818v1', 'WebNovelBench: Placing LLM Novelists on the Web Novel Distribution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leon Lin, Jun Zheng, Haidong Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出WebNovelBench以解决长篇小说生成评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长篇小说生成` `大型语言模型` `叙事质量评估` `数据集构建` `自动化评估`

## 📋 核心要点

1. 现有的长篇小说生成评估方法缺乏足够的规模和多样性，难以客观衡量LLMs的创作能力。
2. 本文提出WebNovelBench，通过大规模中文网络小说数据集，构建从概要到故事生成的评估框架。
3. 实验结果显示WebNovelBench能够有效区分人类创作与LLM生成的内容，并提供了对24个LLM的叙事能力排名。

## 📝 摘要（中文）

长篇故事创作能力的评估是大型语言模型（LLMs）面临的重要挑战，现有基准往往缺乏规模、多样性或客观性。为此，本文提出WebNovelBench，一个专门用于评估长篇小说生成的新基准。WebNovelBench利用超过4000部中文网络小说的大规模数据集，将评估框架设定为从概要到故事生成的任务。我们提出了一个多维度框架，涵盖八个叙事质量维度，通过LLM作为评判者的方式自动评估。得分通过主成分分析进行聚合，并与人类创作的作品进行百分位排名。实验表明，WebNovelBench能够有效区分人类创作的杰作、受欢迎的网络小说和LLM生成的内容。我们对24个最先进的LLM进行了全面分析，排名其叙事能力，并为未来的发展提供了见解。

## 🔬 方法详解

**问题定义**：本文旨在解决现有长篇小说生成评估方法缺乏规模和客观性的问题，现有基准无法全面评估LLMs的叙事能力。

**核心思路**：提出WebNovelBench基准，通过大规模中文网络小说数据集，构建从概要到故事生成的评估任务，采用多维度叙事质量评估框架。

**技术框架**：整体架构包括数据集构建、评估任务设计、叙事质量维度定义、LLM评判者的自动评估、得分聚合与排名等主要模块。

**关键创新**：最重要的创新在于将评估框架与LLM作为评判者结合，自动化评估叙事质量，并通过主成分分析聚合得分，提供与人类作品的对比。

**关键设计**：在评估过程中，定义了八个叙事质量维度，采用主成分分析方法对得分进行聚合，确保评估结果的客观性与可靠性。通过这种设计，能够有效区分不同质量的文本。

## 📊 实验亮点

实验结果表明，WebNovelBench能够有效区分人类创作的杰作与LLM生成的内容，且在对24个LLM的叙事能力排名中，提供了清晰的性能对比，展示了该基准的有效性与实用性。

## 🎯 应用场景

WebNovelBench的潜在应用领域包括文学创作、游戏剧情生成、教育等。它为评估和提升LLM在长篇叙事生成中的能力提供了数据驱动的方法，未来可能推动相关领域的技术进步与应用落地。

## 📄 摘要（原文）

> Robustly evaluating the long-form storytelling capabilities of Large Language Models (LLMs) remains a significant challenge, as existing benchmarks often lack the necessary scale, diversity, or objective measures. To address this, we introduce WebNovelBench, a novel benchmark specifically designed for evaluating long-form novel generation. WebNovelBench leverages a large-scale dataset of over 4,000 Chinese web novels, framing evaluation as a synopsis-to-story generation task. We propose a multi-faceted framework encompassing eight narrative quality dimensions, assessed automatically via an LLM-as-Judge approach. Scores are aggregated using Principal Component Analysis and mapped to a percentile rank against human-authored works. Our experiments demonstrate that WebNovelBench effectively differentiates between human-written masterpieces, popular web novels, and LLM-generated content. We provide a comprehensive analysis of 24 state-of-the-art LLMs, ranking their storytelling abilities and offering insights for future development. This benchmark provides a scalable, replicable, and data-driven methodology for assessing and advancing LLM-driven narrative generation.

