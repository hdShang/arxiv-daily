---
layout: default
title: "MinionsLLM: a Task-adaptive Framework For The Training and Control of Multi-Agent Systems Through Natural Language"
---

# MinionsLLM: a Task-adaptive Framework For The Training and Control of Multi-Agent Systems Through Natural Language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08283" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08283v1</a>
  <a href="https://arxiv.org/pdf/2508.08283.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08283v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08283v1', 'MinionsLLM: a Task-adaptive Framework For The Training and Control of Multi-Agent Systems Through Natural Language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andres Garcia Rincon, Eliseo Ferrante

**分类**: cs.CL, cs.AI, cs.LG, cs.MA, cs.RO

**发布日期**: 2025-08-01

---

## 💡 一句话要点

**提出MinionsLLM框架以实现自然语言控制的多智能体系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `自然语言处理` `大型语言模型` `行为树` `合成数据集` `微调技术` `开源框架`

## 📋 核心要点

1. 现有方法在多智能体系统中缺乏有效的自然语言控制，导致用户交互复杂且不直观。
2. MinionsLLM框架通过结合LLMs、BTs和形式语法，提供了标准化接口和合成数据集生成方法，提升了自然语言控制的有效性。
3. 实验结果显示，方法B在语法有效性上达到92.6%，任务性能平均提升33%，尤其是小模型的微调效果显著。

## 📝 摘要（中文）

本文提出了MinionsLLM，一个新颖的框架，将大型语言模型（LLMs）与行为树（BTs）和形式语法结合，支持在用户定义的任意环境中对多智能体系统进行自然语言控制。MinionsLLM提供了标准化接口，用于定义环境、智能体和行为原语，并引入了两种合成数据集生成方法（方法A和方法B），以微调LLMs，提高语法有效性和语义任务相关性。通过在Google的Gemma 3模型系列上进行验证，方法B的语法有效性提高至92.6%，任务性能平均提升33%。实验表明，较小的模型在微调中受益最大，暗示了在资源受限的多智能体控制场景中部署紧凑型本地LLMs的前景。该框架及所有资源已开源，以支持可重复性和未来研究。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多智能体系统在自然语言控制方面的不足，现有方法往往无法有效理解和执行用户的自然语言指令，导致交互效率低下。

**核心思路**：MinionsLLM框架通过将大型语言模型与行为树和形式语法结合，提供了一种新的方式来解析和执行自然语言指令，从而实现更高效的多智能体控制。

**技术框架**：该框架包括三个主要模块：环境定义模块、智能体定义模块和行为原语模块。用户可以通过标准化接口定义这些模块，并利用合成数据集生成方法对LLMs进行微调。

**关键创新**：最重要的创新在于引入了两种合成数据集生成方法（方法A和方法B），特别是方法B显著提高了语法有效性和任务相关性，与传统方法相比，提供了更高的灵活性和适应性。

**关键设计**：在参数设置上，框架支持不同规模的LLMs（1B、4B和12B），并通过特定的损失函数和网络结构优化微调过程，以确保模型在特定任务上的表现最优。

## 📊 实验亮点

实验结果显示，使用方法B后，语法有效性提高至92.6%，任务性能平均提升33%。尤其是较小模型在微调过程中表现出更显著的提升，表明该框架在资源受限环境中的应用潜力。

## 🎯 应用场景

该研究具有广泛的应用潜力，特别是在机器人控制、智能家居和虚拟助手等领域。通过自然语言控制，用户可以更直观地与多智能体系统交互，提升用户体验。此外，框架的开源特性将促进后续研究和开发，推动相关技术的进步。

## 📄 摘要（原文）

> This paper presents MinionsLLM, a novel framework that integrates Large Language Models (LLMs) with Behavior Trees (BTs) and Formal Grammars to enable natural language control of multi-agent systems within arbitrary, user-defined environments. MinionsLLM provides standardized interfaces for defining environments, agents, and behavioral primitives, and introduces two synthetic dataset generation methods (Method A and Method B) to fine-tune LLMs for improved syntactic validity and semantic task relevance. We validate our approach using Google's Gemma 3 model family at three parameter scales (1B, 4B, and 12B) and demonstrate substantial gains: Method B increases syntactic validity to 92.6% and achieves a mean task performance improvement of 33% over baseline. Notably, our experiments show that smaller models benefit most from fine-tuning, suggesting promising directions for deploying compact, locally hosted LLMs in resource-constrained multi-agent control scenarios. The framework and all resources are released open-source to support reproducibility and future research.

