---
layout: default
title: "SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling"
---

# SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04179" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04179v1</a>
  <a href="https://arxiv.org/pdf/2506.04179.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04179v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04179v1', 'SkipGPT: Dynamic Layer Pruning Reinvented with Token Awareness and Module Decoupling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anhao Zhao, Fanghua Ye, Yingqi Fan, Junlong Tong, Zhiwei Fei, Hui Su, Xiaoyu Shen

**分类**: cs.CL

**发布日期**: 2025-06-04

**🔗 代码/项目**: [GITHUB](https://github.com/EIT-NLP/SkipGPT)

---

## 💡 一句话要点

**提出SkipGPT以解决大语言模型的动态层修剪问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态层修剪` `大型语言模型` `计算效率` `token感知` `解耦策略` `深度学习` `自然语言处理`

## 📋 核心要点

1. 现有的静态层修剪方法未能考虑LLM推理中的水平和垂直动态性，导致修剪效果不佳。
2. SkipGPT通过全球token感知路由和解耦的修剪策略，针对不同组件进行动态修剪，提高了计算效率。
3. 实验结果显示，SkipGPT在减少超过40%模型参数的同时，性能与原始模型持平或更优，验证了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在多项任务中表现出色，但由于其深层次、多层次的架构，计算成本高昂。层修剪作为一种缓解这些低效的方法，传统的静态修剪方法忽视了LLM推理中固有的两种动态性：水平动态性和垂直动态性。本文提出SkipGPT，一个动态层修剪框架，通过全球token感知路由和解耦的MLP与自注意力组件修剪策略来优化计算资源分配。为缓解训练不稳定性，提出了两阶段优化范式，最终实验表明SkipGPT在减少40%以上模型参数的同时，性能与原始密集模型相当或更优。该研究推动了可扩展、资源感知LLMs的实际部署。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理过程中由于深层架构导致的高计算成本问题。现有的静态层修剪方法未能有效应对模型中token的异质性和不同层的功能差异，导致修剪效果不理想。

**核心思路**：SkipGPT的核心思路是通过动态层修剪来优化计算资源的分配，具体包括全球token感知路由和针对不同组件的解耦修剪策略，以实现更高效的模型推理。

**技术框架**：SkipGPT的整体架构包括两个主要阶段：第一阶段为解耦训练，通过软参数化学习路由策略，避免过早的修剪决策；第二阶段为参数高效的LoRA微调，以恢复因层移除而受到影响的性能。

**关键创新**：SkipGPT的主要创新在于引入了动态的token感知修剪和解耦的修剪策略，这与传统的静态修剪方法形成了鲜明对比，使得模型在保持表达能力的同时实现了动态效率的提升。

**关键设计**：在设计上，SkipGPT采用了软参数化的路由策略和LoRA微调技术，确保了模型在修剪后的性能恢复。此外，针对MLP和自注意力层的不同功能，设计了专门的修剪策略。

## 📊 实验亮点

SkipGPT在实验中成功减少了超过40%的模型参数，同时在多个基准测试中与原始密集模型的性能持平或更优。这一结果表明，SkipGPT在动态修剪方面的创新能够显著提升模型的计算效率，具有重要的实用价值。

## 🎯 应用场景

SkipGPT的研究成果在多个领域具有广泛的应用潜力，包括自然语言处理、对话系统和智能助手等。通过优化计算资源的使用，该框架能够支持更大规模的模型部署，降低运行成本，提升用户体验。未来，SkipGPT有望推动更高效的LLM在实际应用中的普及。

## 📄 摘要（原文）

> Large language models (LLMs) achieve remarkable performance across tasks but incur substantial computational costs due to their deep, multi-layered architectures. Layer pruning has emerged as a strategy to alleviate these inefficiencies, but conventional static pruning methods overlook two critical dynamics inherent to LLM inference: (1) horizontal dynamics, where token-level heterogeneity demands context-aware pruning decisions, and (2) vertical dynamics, where the distinct functional roles of MLP and self-attention layers necessitate component-specific pruning policies. We introduce SkipGPT, a dynamic layer pruning framework designed to optimize computational resource allocation through two core innovations: (1) global token-aware routing to prioritize critical tokens, and (2) decoupled pruning policies for MLP and self-attention components. To mitigate training instability, we propose a two-stage optimization paradigm: first, a disentangled training phase that learns routing strategies via soft parameterization to avoid premature pruning decisions, followed by parameter-efficient LoRA fine-tuning to restore performance impacted by layer removal. Extensive experiments demonstrate that SkipGPT reduces over 40% of model parameters while matching or exceeding the performance of the original dense model across benchmarks. By harmonizing dynamic efficiency with preserved expressivity, SkipGPT advances the practical deployment of scalable, resource-aware LLMs. Our code is publicly available at: https://github.com/EIT-NLP/SkipGPT.

