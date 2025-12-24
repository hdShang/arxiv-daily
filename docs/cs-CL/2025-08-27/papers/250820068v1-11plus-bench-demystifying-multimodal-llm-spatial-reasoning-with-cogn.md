---
layout: default
title: "11Plus-Bench: Demystifying Multimodal LLM Spatial Reasoning with Cognitive-Inspired Analysis"
---

# 11Plus-Bench: Demystifying Multimodal LLM Spatial Reasoning with Cognitive-Inspired Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20068" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20068v1</a>
  <a href="https://arxiv.org/pdf/2508.20068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20068v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20068v1', '11Plus-Bench: Demystifying Multimodal LLM Spatial Reasoning with Cognitive-Inspired Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengzu Li, Wenshan Wu, Huanyu Zhang, Qingtao Li, Zeyu Gao, Yan Xia, José Hernández-Orallo, Ivan Vulić, Furu Wei

**分类**: cs.CL, cs.CV, cs.LG

**发布日期**: 2025-08-27

**备注**: 9 pages, 4 figures (22 pages, 7 figures, 7 tables including references and appendices)

---

## 💡 一句话要点

**提出11Plus-Bench以评估多模态大语言模型的空间推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `空间推理` `认知科学` `标准化测试` `专家注释` `模型评估` `人工智能`

## 📋 核心要点

1. 现有的多模态大语言模型在空间推理能力评估上缺乏系统性框架，难以与人类表现进行有效比较。
2. 本文提出11Plus-Bench基准，结合现实标准测试与专家注释，系统评估MLLMs的空间推理能力。
3. 实验结果显示，尽管MLLMs在空间认知上表现出早期迹象，但其实例级表现仍然随机，与人类的可预测性存在显著差异。

## 📝 摘要（中文）

在人类认知过程中，空间推理与感知密切相关，但这一关系在多模态大语言模型（MLLMs）的评估中仍未得到充分探讨。尽管近期MLLMs在推理方面表现出色，但其人类般的空间认知能力仍然是一个未解之谜。本文提出了一个系统的评估框架，以评估最先进的MLLMs在空间推理能力上的表现，并引入了11Plus-Bench，一个基于现实标准空间能力测试的高质量基准。该基准还提供了感知复杂性和推理过程的细粒度专家注释，支持对模型行为的详细实例级分析。通过对14个MLLMs和人类评估的广泛实验，我们发现当前的MLLMs展现出空间认知的早期迹象，尽管与人类相比存在较大性能差距，但MLLMs的认知特征与人类相似，认知努力与推理相关复杂性之间存在强相关性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在空间推理能力评估中的不足，现有方法未能有效捕捉人类的认知过程与模型表现之间的关系。

**核心思路**：通过引入11Plus-Bench基准，结合标准化空间能力测试与专家注释，系统评估MLLMs的空间推理能力，揭示其与人类认知的相似性与差异性。

**技术框架**：整体架构包括数据收集、专家注释、模型评估和结果分析四个主要模块。数据收集阶段使用标准化测试，专家注释阶段提供细粒度的感知复杂性与推理过程分析，模型评估阶段对14个MLLMs进行系统测试，最后通过结果分析总结模型表现。

**关键创新**：11Plus-Bench基准的引入是本文的核心创新，它通过结合标准化测试与专家注释，提供了一个全面评估MLLMs空间推理能力的新方法，区别于以往单一的性能评估。

**关键设计**：在设计中，采用了细粒度的专家注释来评估感知复杂性与推理过程，确保评估的全面性与准确性，同时在模型评估中引入了多样化的测试实例，以增强评估的代表性。

## 📊 实验亮点

实验结果表明，当前的MLLMs在空间认知方面展现出早期迹象，但与人类的表现相比，存在显著的性能差距。具体而言，MLLMs的认知努力与推理复杂性之间存在强相关性，但实例级表现仍然随机，缺乏人类的可预测性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、机器人导航和人机交互等。通过深入理解MLLMs的空间推理能力，可以为智能系统的设计与优化提供重要参考，推动人工智能在复杂环境中的应用与发展。

## 📄 摘要（原文）

> For human cognitive process, spatial reasoning and perception are closely entangled, yet the nature of this interplay remains underexplored in the evaluation of multimodal large language models (MLLMs). While recent MLLM advancements show impressive performance on reasoning, their capacity for human-like spatial cognition remains an open question. In this work, we introduce a systematic evaluation framework to assess the spatial reasoning abilities of state-of-the-art MLLMs relative to human performance. Central to our work is 11Plus-Bench, a high-quality benchmark derived from realistic standardized spatial aptitude tests. 11Plus-Bench also features fine-grained expert annotations of both perceptual complexity and reasoning process, enabling detailed instance-level analysis of model behavior. Through extensive experiments across 14 MLLMs and human evaluation, we find that current MLLMs exhibit early signs of spatial cognition. Despite a large performance gap compared to humans, MLLMs' cognitive profiles resemble those of humans in that cognitive effort correlates strongly with reasoning-related complexity. However, instance-level performance in MLLMs remains largely random, whereas human correctness is highly predictable and shaped by abstract pattern complexity. These findings highlight both emerging capabilities and limitations in current MLLMs' spatial reasoning capabilities and provide actionable insights for advancing model design.

