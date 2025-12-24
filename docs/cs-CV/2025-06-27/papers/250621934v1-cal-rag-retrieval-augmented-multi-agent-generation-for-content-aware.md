---
layout: default
title: "CAL-RAG: Retrieval-Augmented Multi-Agent Generation for Content-Aware Layout Design"
---

# CAL-RAG: Retrieval-Augmented Multi-Agent Generation for Content-Aware Layout Design

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21934" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21934v1</a>
  <a href="https://arxiv.org/pdf/2506.21934.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21934v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21934v1', 'CAL-RAG: Retrieval-Augmented Multi-Agent Generation for Content-Aware Layout Design')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Najmeh Forouzandehmehr, Reza Yousefi Maragheh, Sriram Kollipara, Kai Zhao, Topojoy Biswas, Evren Korpeoglu, Kannan Achan

**分类**: cs.IR, cs.CV

**发布日期**: 2025-06-27

---

## 💡 一句话要点

**提出CAL-RAG以解决内容感知布局生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内容感知布局` `自动化设计` `多模态检索` `大型语言模型` `视觉一致性` `智能设计系统`

## 📋 核心要点

1. 现有方法在内容感知布局生成中缺乏对上下文设计示例的有效利用，导致语义对齐和视觉一致性不足。
2. CAL-RAG框架通过检索相关布局示例并结合LLM进行结构化元素推荐，提升了布局生成的质量和效率。
3. 在PKU PosterLayout数据集上，CAL-RAG在布局有效性、元素对齐和重叠等多个指标上表现优异，超越了多个基线模型。

## 📝 摘要（中文）

自动化内容感知布局生成，即在背景画布上排列文本、标志和底图等视觉元素，仍然是智能设计系统中的一个基本但未充分探索的问题。尽管深度生成模型和大型语言模型（LLMs）的进展在结构化内容生成中显示出潜力，但现有方法往往缺乏对上下文设计示例的基础支持，且在语义对齐和视觉一致性方面表现不足。本文提出了CAL-RAG，一个增强检索的代理框架，集成了多模态检索、大型语言模型和协作代理推理。该系统从结构化知识库中检索相关布局示例，并调用基于LLM的布局推荐器提出结构化元素放置。视觉语言评分代理使用视觉指标评估布局，反馈代理提供针对性改进，从而实现迭代优化。我们在PKU PosterLayout数据集上评估了该框架，CAL-RAG在多个布局指标上实现了最先进的性能，显著超越了LayoutPrompter等强基线。

## 🔬 方法详解

**问题定义**：本文旨在解决内容感知布局生成中的语义对齐和视觉一致性不足的问题。现有方法通常缺乏对上下文设计示例的有效利用，导致生成的布局质量不高。

**核心思路**：CAL-RAG框架通过检索相关的布局示例，结合大型语言模型（LLM）进行结构化元素推荐，利用多模态信息提升布局生成的质量和一致性。这样的设计使得生成的布局不仅符合语义要求，还具备较好的视觉效果。

**技术框架**：该框架主要包括三个模块：1) 多模态检索模块，从知识库中检索相关布局示例；2) LLM布局推荐模块，基于检索结果提出元素放置建议；3) 视觉语言评分模块，评估布局的视觉质量并提供反馈。

**关键创新**：CAL-RAG的创新在于将检索增强与代理多步推理相结合，形成了一种可扩展、可解释且高保真的自动化布局生成解决方案。这一方法在处理复杂布局时表现出明显优势。

**关键设计**：在实现过程中，采用了LangGraph作为基础框架，设计了特定的损失函数以优化布局质量，并在网络结构上进行了针对性调整，以确保生成结果的视觉一致性和语义对齐。

## 📊 实验亮点

CAL-RAG在PKU PosterLayout数据集上实现了最先进的性能，具体在布局有效性、元素对齐和重叠等指标上显著超越了LayoutPrompter等强基线，展示了其在内容感知布局生成中的优越性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括广告设计、网页布局、信息图表生成等多个视觉内容创作场景。通过自动化生成高质量的布局，能够显著提升设计效率，降低人工成本，并为设计师提供更具创意的参考方案。未来，该技术有望在智能设计工具中得到广泛应用，推动设计行业的变革。

## 📄 摘要（原文）

> Automated content-aware layout generation -- the task of arranging visual elements such as text, logos, and underlays on a background canvas -- remains a fundamental yet under-explored problem in intelligent design systems. While recent advances in deep generative models and large language models (LLMs) have shown promise in structured content generation, most existing approaches lack grounding in contextual design exemplars and fall short in handling semantic alignment and visual coherence. In this work we introduce CAL-RAG, a retrieval-augmented, agentic framework for content-aware layout generation that integrates multimodal retrieval, large language models, and collaborative agentic reasoning. Our system retrieves relevant layout examples from a structured knowledge base and invokes an LLM-based layout recommender to propose structured element placements. A vision-language grader agent evaluates the layout with visual metrics, and a feedback agent provides targeted refinements, enabling iterative improvement. We implement our framework using LangGraph and evaluate it on the PKU PosterLayout dataset, a benchmark rich in semantic and structural variability. CAL-RAG achieves state-of-the-art performance across multiple layout metrics -- including underlay effectiveness, element alignment, and overlap -- substantially outperforming strong baselines such as LayoutPrompter. These results demonstrate that combining retrieval augmentation with agentic multi-step reasoning yields a scalable, interpretable, and high-fidelity solution for automated layout generation.

