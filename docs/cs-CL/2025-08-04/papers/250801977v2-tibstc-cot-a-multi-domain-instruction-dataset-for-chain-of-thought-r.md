---
layout: default
title: "TIBSTC-CoT: A Multi-Domain Instruction Dataset for Chain-of-Thought Reasoning in Language Models"
---

# TIBSTC-CoT: A Multi-Domain Instruction Dataset for Chain-of-Thought Reasoning in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01977" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01977v2</a>
  <a href="https://arxiv.org/pdf/2508.01977.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01977v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01977v2', 'TIBSTC-CoT: A Multi-Domain Instruction Dataset for Chain-of-Thought Reasoning in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Gao, Cheng Huang, Nyima Tashi, Yutong Liu, Xiangxiang Wang, Thupten Tsering, Ban Ma-bao, Renzeg Duojie, Gadeng Luosang, Rinchen Dongrub, Dorje Tashi, Xiao Feng, Hao Wang, Yongbin Yu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-04 (更新: 2025-12-16)

**备注**: We will merge this paper with arXiv:2503.18288

**🔗 代码/项目**: [GITHUB](https://github.com/Vicentvankor/sun-shine)

---

## 💡 一句话要点

**提出TIBSTC-CoT以解决藏语数据稀缺问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `藏语处理` `低资源语言` `数据集构建` `链式思维` `语言模型` `自然语言处理` `智能翻译`

## 📋 核心要点

1. 藏语作为一种低资源语言，面临严重的数据稀缺问题，现有方法难以满足其语言处理需求。
2. 本文提出了TIBSTC-CoT数据集，通过链式思维提示自动构建，提供了多领域的藏语数据，支持语言理解与生成。
3. 基于TIBSTC-CoT训练的Sunshine-thinking LLM在推理和生成性能上表现优异，已接近最先进的多语言模型。

## 📝 摘要（中文）

为了解决藏语这一低资源语言的数据稀缺问题，本文提出了TIBSTC-CoT，一个通过链式思维提示自动构建的大规模多领域藏语数据集。该数据集建立了一个可扩展和可重复的数据集创建框架，涵盖了语言理解和生成所需的多样化领域和推理模式。基于此数据集，我们开发了Sunshine-thinking LLM系列，这些藏语中心的语言模型具备链式思维能力，经过训练后在推理和生成性能上表现出色，已接近当前最先进的多语言LLM。我们的工作为实现包容性人工智能迈出了重要一步，促进了高质量藏语处理的实现。

## 🔬 方法详解

**问题定义**：本文旨在解决藏语数据稀缺的问题，现有方法在低资源语言处理上效果不佳，缺乏足够的高质量数据支持。

**核心思路**：通过链式思维提示，自动生成多领域的藏语数据集TIBSTC-CoT，提供丰富的推理模式和语言理解能力，进而训练出高效的藏语语言模型。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要模块。数据集构建通过大语言模型生成多样化的藏语文本，模型训练则基于生成的数据集进行优化。

**关键创新**：TIBSTC-CoT数据集的自动构建方法是本研究的核心创新，显著提高了低资源语言的数据获取效率，与传统手动标注方法相比，具有更高的可扩展性和可重复性。

**关键设计**：在模型训练中，采用了特定的损失函数和参数设置，以优化链式思维能力的学习，确保模型在推理和生成任务中的表现达到最优。具体的网络结构设计也针对藏语特性进行了调整。

## 📊 实验亮点

实验结果表明，基于TIBSTC-CoT训练的Sunshine-thinking LLM在推理和生成任务上表现出色，其性能与当前最先进的多语言LLM相当，展示了显著的提升幅度，证明了该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括藏语的自然语言处理、智能翻译、语音识别等。通过提供高质量的藏语数据和模型，能够促进藏语相关技术的发展，提升藏语用户的数字体验，具有重要的社会和文化价值。

## 📄 摘要（原文）

> To address the severe data scarcity in Tibetan, a low-resource language spoken by over six million people, we introduce TIBSTC-CoT, the large-scale, multi-domain Tibetan dataset automatically constructed via chain-of-thought prompting with large language models (LLMs). TIBSTC-CoT establishes a scalable and reproducible framework for dataset creation in low-resource settings, covering diverse domains and reasoning patterns essential for language understanding and generation. Building on this dataset, we develop the Sunshine-thinking LLM family, a series of Tibetan-centric LLMs equipped with chain-of-thought capabilities. Trained entirely on TIBSTC-CoT, Sunshine-thinking has demonstrated strong reasoning and generation performance, comparable to state-of-the-art (SOTA) multilingual LLMs. Our work marks a significant step toward inclusive AI by enabling high-quality Tibetan language processing through both resource creation and model innovation. All data are available: https://github.com/Vicentvankor/sun-shine.

