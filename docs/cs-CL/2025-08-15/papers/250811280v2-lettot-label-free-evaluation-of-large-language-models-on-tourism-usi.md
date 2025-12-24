---
layout: default
title: "LETToT: Label-Free Evaluation of Large Language Models On Tourism Using Expert Tree-of-Thought"
---

# LETToT: Label-Free Evaluation of Large Language Models On Tourism Using Expert Tree-of-Thought

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11280" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11280v2</a>
  <a href="https://arxiv.org/pdf/2508.11280.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11280v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11280v2', 'LETToT: Label-Free Evaluation of Large Language Models On Tourism Using Expert Tree-of-Thought')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruiyan Qi, Congding Wen, Weibo Zhou, Jiwei Li, Shangsong Liang, Lingbo Li

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-15 (更新: 2025-08-25)

---

## 💡 一句话要点

**提出LETToT框架以解决旅游领域LLM评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `旅游领域` `标签自由评估` `专家推理结构` `模型评估` `质量提升` `领域特定评估`

## 📋 核心要点

1. 现有方法在特定领域（如旅游）评估大型语言模型时，面临高昂的标注成本和幻觉等问题。
2. 我们提出的LETToT框架通过专家推理结构进行评估，避免了对标注数据的依赖，提供了一种新的评估思路。
3. 实验结果表明，优化后的专家推理在质量上相较于基线有4.99%-14.15%的提升，且小模型在特定任务中表现优越。

## 📝 摘要（中文）

在特定领域（如旅游）评估大型语言模型（LLMs）面临着标注基准成本高和幻觉等问题。我们提出了标签自由的旅游领域LLM评估框架LETToT，该框架利用专家推理结构而非标注数据来评估LLMs。通过与通用质量维度和专家反馈对齐，我们迭代优化了层次化的推理组件，结果显示优化后的专家推理在基准测试中相较于基线有4.99%-14.15%的相对质量提升。此外，我们将LETToT应用于不同规模（32B-671B参数）的模型评估，发现推理增强的小模型在准确性和简洁性上优于同类模型。我们的工作为领域特定的LLM评估建立了可扩展的标签自由范式，提供了对传统标注基准的有力替代。

## 🔬 方法详解

**问题定义**：本研究旨在解决在旅游领域评估大型语言模型时，缺乏标注数据和高成本的问题。现有方法往往依赖于昂贵的标注基准，且存在模型产生幻觉的风险。

**核心思路**：我们提出LETToT框架，通过专家推理结构代替标注数据进行评估。该方法通过专家反馈和通用质量维度的对齐，逐步优化推理组件，从而实现有效评估。

**技术框架**：LETToT的整体架构包括三个主要阶段：首先，构建层次化的推理结构；其次，进行迭代优化和验证；最后，应用优化后的推理结构评估不同规模的LLMs。

**关键创新**：LETToT的核心创新在于其标签自由的评估方式，利用专家推理结构而非传统的标注数据，显著降低了评估成本并提高了评估的灵活性。

**关键设计**：在设计过程中，我们关注了推理结构的层次化设计，确保其能够有效捕捉领域特定的知识。同时，通过专家反馈不断调整推理组件，以提升评估的准确性和有效性。

## 📊 实验亮点

实验结果显示，优化后的专家推理在质量上相较于基线有4.99%-14.15%的提升。此外，对于小于72B参数的模型，采用显式推理架构的模型在准确性和简洁性上显著优于其他模型，p值小于0.05，表明结果的统计显著性。

## 🎯 应用场景

LETToT框架在旅游领域的潜在应用广泛，可以用于评估旅游相关的对话系统、推荐引擎和信息检索模型等。其标签自由的特性使得在资源有限的情况下，仍然能够进行有效的模型评估，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Evaluating large language models (LLMs) in specific domain like tourism remains challenging due to the prohibitive cost of annotated benchmarks and persistent issues like hallucinations. We propose $\textbf{L}$able-Free $\textbf{E}$valuation of LLM on $\textbf{T}$ourism using Expert $\textbf{T}$ree-$\textbf{o}$f-$\textbf{T}$hought (LETToT), a framework that leverages expert-derived reasoning structures-instead of labeled data-to access LLMs in tourism. First, we iteratively refine and validate hierarchical ToT components through alignment with generic quality dimensions and expert feedback. Results demonstrate the effectiveness of our systematically optimized expert ToT with 4.99-14.15\% relative quality gains over baselines. Second, we apply LETToT's optimized expert ToT to evaluate models of varying scales (32B-671B parameters), revealing: (1) Scaling laws persist in specialized domains (DeepSeek-V3 leads), yet reasoning-enhanced smaller models (e.g., DeepSeek-R1-Distill-Llama-70B) close this gap; (2) For sub-72B models, explicit reasoning architectures outperform counterparts in accuracy and conciseness ($p<0.05$). Our work established a scalable, label-free paradigm for domain-specific LLM evaluation, offering a robust alternative to conventional annotated benchmarks.

