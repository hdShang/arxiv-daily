---
layout: default
title: Accelerating Large Language Model Reasoning via Speculative Search
---

# Accelerating Large Language Model Reasoning via Speculative Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02865" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02865v2</a>
  <a href="https://arxiv.org/pdf/2505.02865.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02865v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02865v2', 'Accelerating Large Language Model Reasoning via Speculative Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihai Wang, Jie Wang, Jilai Pan, Xilin Xia, Huiling Zhen, Mingxuan Yuan, Jianye Hao, Feng Wu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-03 (更新: 2025-05-24)

**备注**: Accepted by ICML2025

---

## 💡 一句话要点

**提出Speculative Search以加速大语言模型推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理加速` `Speculative Search` `质量保留机制` `树搜索`

## 📋 核心要点

1. 现有基于树搜索的推理方法在生成多个推理思维时存在显著的推理延迟，限制了大语言模型的实际应用。
2. 本文提出的Speculative Search框架通过小模型与大模型的协作，优化思维生成过程，从而加速推理。
3. 实验结果显示，SpecSearch在Qwen和Llama模型上显著优于现有方法，实现了高达2.12倍的速度提升，同时保持了相当的推理质量。

## 📝 摘要（中文）

基于树搜索的推理方法显著提升了大语言模型（LLMs）的推理能力，但由于生成大量推理思维，导致推理延迟显著，限制了其应用。为了解决这一挑战，本文提出了一种新颖的Speculative Search（SpecSearch）框架，通过优化思维生成显著加速LLM推理。SpecSearch利用小模型与大模型在思维和令牌层面进行战略性协作，效率高地生成高质量推理思维。其核心是一个新颖的质量保留拒绝机制，有效过滤掉质量低于大模型输出的思维。实验表明，SpecSearch在保持推理质量的同时，显著超越了现有最先进的方法，实现了高达2.12倍的加速。

## 🔬 方法详解

**问题定义**：本文旨在解决基于树搜索的推理方法在生成多个推理思维时导致的显著推理延迟问题，这一问题严重限制了大语言模型的应用场景。

**核心思路**：提出的Speculative Search框架通过小模型与大模型的协作，优化思维生成过程，旨在提高推理速度而不牺牲推理质量。

**技术框架**：SpecSearch的整体架构包括两个主要模块：小模型负责初步生成推理思维，大模型则对这些思维进行质量评估和筛选。通过这种协作，系统能够高效生成高质量的推理思维。

**关键创新**：SpecSearch的核心创新在于引入了质量保留拒绝机制，该机制能够有效过滤掉质量低于大模型输出的思维，从而确保生成思维的高质量。与现有方法相比，SpecSearch在推理速度和质量上实现了显著提升。

**关键设计**：在设计中，SpecSearch对小模型和大模型的协作进行了精细调节，确保小模型生成的思维能够被大模型有效评估。此外，系统的损失函数和网络结构经过优化，以支持高效的推理过程。

## 📊 实验亮点

实验结果表明，SpecSearch在Qwen和Llama模型上实现了高达2.12倍的推理速度提升，同时保持了与大模型相当的推理质量，显著优于现有最先进的方法，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和对话生成等。通过加速大语言模型的推理过程，Speculative Search能够提升这些应用的响应速度和用户体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Tree-search-based reasoning methods have significantly enhanced the reasoning capability of large language models (LLMs) by facilitating the exploration of multiple intermediate reasoning steps, i.e., thoughts. However, these methods suffer from substantial inference latency, as they have to generate numerous reasoning thoughts, severely limiting LLM applicability. To address this challenge, we propose a novel Speculative Search (SpecSearch) framework that significantly accelerates LLM reasoning by optimizing thought generation. Specifically, SpecSearch utilizes a small model to strategically collaborate with a large model at both thought and token levels, efficiently generating high-quality reasoning thoughts. The major pillar of SpecSearch is a novel quality-preserving rejection mechanism, which effectively filters out thoughts whose quality falls below that of the large model's outputs. Moreover, we show that SpecSearch preserves comparable reasoning quality to the large model. Experiments on both the Qwen and Llama models demonstrate that SpecSearch significantly outperforms state-of-the-art approaches, achieving up to 2.12$\times$ speedup with comparable reasoning quality.

