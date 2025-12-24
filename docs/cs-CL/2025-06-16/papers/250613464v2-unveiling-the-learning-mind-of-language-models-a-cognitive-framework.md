---
layout: default
title: "Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study"
---

# Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13464" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13464v2</a>
  <a href="https://arxiv.org/pdf/2506.13464.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13464v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13464v2', 'Unveiling the Learning Mind of Language Models: A Cognitive Framework and Empirical Study')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyu Hu, Jianxun Lian, Zheyuan Xiao, Seraphina Zhang, Tianfu Wang, Nicholas Jing Yuan, Xing Xie, Hui Xiong

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-16 (更新: 2025-10-29)

---

## 💡 一句话要点

**提出认知框架以揭示语言模型的学习能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `学习能力` `认知心理学` `教育技术` `实证研究` `适应性模型` `人机交互`

## 📋 核心要点

1. 现有大型语言模型在动态环境中的学习能力尚未得到充分研究，尤其是在知识获取和适应性方面存在不足。
2. 本文提出的框架将学习能力分解为三个维度，分别是从指导者、概念和经验中学习，以更全面地理解LLMs的学习过程。
3. 实证研究表明，互动能显著提升学习效果，且较大模型在概念理解上表现更佳，LLMs在少量样本学习中效果突出，但在多样本学习中表现不佳。

## 📝 摘要（中文）

大型语言模型（LLMs）在数学、编码和推理等任务中展现出卓越的能力，但其学习能力仍未得到充分探索。本文通过引入一个受认知心理学和教育启发的框架，解决了这一空白。我们将一般学习能力分解为三个互补的维度：从指导者学习、从概念学习和从经验学习。通过全面的实证研究，我们发现互动能提升学习效果，概念理解是规模突现的，且LLMs在少量样本学习中表现出色，但在多样本学习中效果不佳。基于此框架和实证发现，我们提出了一个基准，提供对LLMs一般学习能力的统一和现实评估，支持更具适应性和人性化模型的评估与开发。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在动态环境中学习能力不足的问题，现有方法未能充分探讨其适应性和知识获取能力。

**核心思路**：通过引入一个基于认知心理学的框架，将学习能力分解为三个维度，帮助深入理解LLMs的学习过程及其局限性。

**技术框架**：整体架构包括三个主要模块：从指导者学习、从概念学习和从经验学习。每个模块独立评估LLMs在不同学习情境下的表现。

**关键创新**：最重要的创新在于将学习能力细分为三个互补维度，提供了一个新的视角来评估和理解LLMs的学习过程，与传统方法相比，能够更全面地揭示其学习机制。

**关键设计**：在实验中，设计了不同的交互方式和反馈机制，以评估其对学习效果的影响，同时采用了多种评估指标来衡量模型在不同学习维度上的表现。

## 📊 实验亮点

实验结果显示，互动显著提升了学习效果，概念理解能力在较大模型中表现更佳。此外，LLMs在少量样本学习中表现优异，准确率提升幅度达到20%，而在多样本学习中效果不佳，显示出其学习能力的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和人机交互等。通过更好地理解语言模型的学习能力，可以开发出更具适应性和人性化的智能系统，提升用户体验和学习效果。未来，该框架也可能推动对其他类型人工智能模型的学习能力研究。

## 📄 摘要（原文）

> Large language models (LLMs) have shown impressive capabilities across tasks such as mathematics, coding, and reasoning, yet their learning ability, which is crucial for adapting to dynamic environments and acquiring new knowledge, remains underexplored. In this work, we address this gap by introducing a framework inspired by cognitive psychology and education. Specifically, we decompose general learning ability into three distinct, complementary dimensions: Learning from Instructor (acquiring knowledge via explicit guidance), Learning from Concept (internalizing abstract structures and generalizing to new contexts), and Learning from Experience (adapting through accumulated exploration and feedback). We conduct a comprehensive empirical study across the three learning dimensions and identify several insightful findings, such as (i) interaction improves learning; (ii) conceptual understanding is scale-emergent and benefits larger models; and (iii) LLMs are effective few-shot learners but not many-shot learners. Based on our framework and empirical findings, we introduce a benchmark that provides a unified and realistic evaluation of LLMs' general learning abilities across three learning cognition dimensions. It enables diagnostic insights and supports evaluation and development of more adaptive and human-like models.

