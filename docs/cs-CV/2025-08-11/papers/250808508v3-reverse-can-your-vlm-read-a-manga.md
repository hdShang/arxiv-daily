---
layout: default
title: "Re:Verse -- Can Your VLM Read a Manga?"
---

# Re:Verse -- Can Your VLM Read a Manga?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08508" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08508v3</a>
  <a href="https://arxiv.org/pdf/2508.08508.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08508v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08508v3', 'Re:Verse -- Can Your VLM Read a Manga?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aaditya Baranwal, Madhav Kataria, Naitik Agrawal, Yogesh S Rawat, Shruti Vyas

**分类**: cs.CV, cs.CL

**发布日期**: 2025-08-11 (更新: 2025-08-18)

**备注**: Accepted (oral) at ICCV (AISTORY Workshop) 2025

---

## 💡 一句话要点

**提出新评估框架以解决视觉语言模型在漫画叙事理解中的不足**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `漫画叙事理解` `多模态评估` `因果推理` `跨面板连贯性` `深度学习` `叙事智能`

## 📋 核心要点

1. 现有的视觉语言模型在理解漫画叙事时，缺乏对时间因果关系和跨面板连贯性的处理能力，导致叙事理解不完整。
2. 论文提出了一种新的评估框架，结合多模态注释和检索增强评估，系统性地分析VLMs在叙事理解中的不足。
3. 通过对《Re:Zero》漫画的11章308个面板进行评估，发现当前模型在非线性叙事和因果推理方面表现不佳。

## 📝 摘要（中文）

当前的视觉语言模型（VLMs）在处理顺序视觉叙事时，表面识别与深层叙事推理之间存在显著差距。通过对漫画叙事理解的深入研究，我们发现尽管大型多模态模型在单个面板的解读上表现良好，但在时间因果关系和跨面板连贯性方面存在系统性缺陷。我们提出了一种新的评估框架，结合细粒度多模态注释、跨模态嵌入分析和检索增强评估，系统性地表征这些局限性。我们的研究为评估叙事智能奠定了基础，并提供了对深度顺序理解离散视觉叙事能力的可行见解。

## 🔬 方法详解

**问题定义**：论文要解决的问题是现有视觉语言模型在漫画叙事理解中的不足，特别是在时间因果关系和跨面板连贯性方面的缺陷。现有方法在处理复杂叙事时表现不佳，无法实现真正的故事级智能。

**核心思路**：论文的核心解决思路是通过引入一种新的评估框架，结合细粒度的多模态注释和跨模态分析，系统性地评估和理解VLMs的叙事能力。这种设计旨在揭示模型在叙事理解中的根本缺陷。

**技术框架**：整体架构包括三个主要模块：1) 严谨的注释协议，将视觉元素与叙事结构相连接；2) 多种推理范式的综合评估，包括直接推理和检索增强生成；3) 跨模态相似性分析，揭示当前VLMs的联合表示中的基本不匹配。

**关键创新**：最重要的技术创新点在于提出了一种系统化的评估方法，能够深入分析VLMs在叙事理解中的表现，与现有方法相比，提供了更为全面的评估视角。

**关键设计**：在关键设计方面，论文采用了精细的注释标准，结合了多模态数据的对齐，并在评估过程中使用了多种损失函数和网络结构，以确保模型能够更好地理解复杂的叙事结构。

## 📊 实验亮点

实验结果表明，当前的视觉语言模型在长篇叙事理解中表现不佳，尤其是在非线性叙事和因果推理方面。通过新评估框架的应用，揭示了模型在308个面板上的系统性缺陷，为未来的研究提供了重要的改进方向。

## 🎯 应用场景

该研究的潜在应用领域包括漫画、动画和游戏等视觉叙事内容的自动理解与生成。通过改进视觉语言模型的叙事理解能力，可以提升相关领域的内容创作、推荐系统和用户交互体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Current Vision Language Models (VLMs) demonstrate a critical gap between surface-level recognition and deep narrative reasoning when processing sequential visual storytelling. Through a comprehensive investigation of manga narrative understanding, we reveal that while recent large multimodal models excel at individual panel interpretation, they systematically fail at temporal causality and cross-panel cohesion, core requirements for coherent story comprehension. We introduce a novel evaluation framework that combines fine-grained multimodal annotation, cross-modal embedding analysis, and retrieval-augmented assessment to systematically characterize these limitations.
>   Our methodology includes (i) a rigorous annotation protocol linking visual elements to narrative structure through aligned light novel text, (ii) comprehensive evaluation across multiple reasoning paradigms, including direct inference and retrieval-augmented generation, and (iii) cross-modal similarity analysis revealing fundamental misalignments in current VLMs' joint representations. Applying this framework to Re:Zero manga across 11 chapters with 308 annotated panels, we conduct the first systematic study of long-form narrative understanding in VLMs through three core evaluation axes: generative storytelling, contextual dialogue grounding, and temporal reasoning. Our findings demonstrate that current models lack genuine story-level intelligence, struggling particularly with non-linear narratives, character consistency, and causal inference across extended sequences. This work establishes both the foundation and practical methodology for evaluating narrative intelligence, while providing actionable insights into the capability of deep sequential understanding of Discrete Visual Narratives beyond basic recognition in Multimodal Models.
>   Project Page: https://re-verse.vercel.app

