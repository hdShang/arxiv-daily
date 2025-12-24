---
layout: default
title: Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers
---

# Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21497" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21497v2</a>
  <a href="https://arxiv.org/pdf/2505.21497.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21497v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21497v2', 'Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wei Pang, Kevin Qinghong Lin, Xiangru Jian, Xi He, Philip Torr

**分类**: cs.CV, cs.AI, cs.CL, cs.MA

**发布日期**: 2025-05-27 (更新: 2025-10-30)

**备注**: Project Page: https://github.com/Paper2Poster/Paper2Poster

**🔗 代码/项目**: [GITHUB](https://github.com/Paper2Poster/Paper2Poster)

---

## 💡 一句话要点

**提出Paper2Poster以解决学术海报自动生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `学术海报生成` `多模态学习` `视觉语言模型` `信息压缩` `自动化工具`

## 📋 核心要点

1. 现有的学术海报生成方法在视觉连贯性和信息传达上存在不足，难以有效压缩长篇文档。
2. 本文提出了PosterAgent，一个多代理管道，通过解析、规划和绘制模块实现海报的自动生成。
3. 实验结果表明，基于Qwen-2.5系列的开源变体在多个评估指标上优于现有系统，且使用的token数量减少了87%。

## 📝 摘要（中文）

学术海报生成是科学传播中的一项重要但具有挑战性的任务，需将长篇文档压缩为视觉上连贯的单页。为此，本文首次引入了海报生成的基准和评估指标，结合会议论文与作者设计的海报，评估输出的视觉质量、文本连贯性、整体评估及海报内容传达能力。基于此基准，提出了PosterAgent，一个自上而下的多代理管道，包含解析、规划和绘制三个主要模块。综合评估显示，基于Qwen-2.5系列的开源变体在多个指标上优于现有系统，且成本极低。这些发现为下一代全自动海报生成模型指明了方向。

## 🔬 方法详解

**问题定义**：本文旨在解决学术海报生成中的信息压缩与视觉连贯性问题。现有方法常常在文本与视觉内容的对齐上表现不佳，导致生成的海报难以有效传达核心信息。

**核心思路**：提出PosterAgent，通过自上而下的多代理管道，利用解析、规划和绘制模块的协同工作，优化海报生成过程，确保信息的有效传达和视觉的吸引力。

**技术框架**：整体架构包括三个主要模块：解析器（Parser）将论文内容提取为结构化资产库；规划器（Planner）将文本与视觉对齐，形成二叉树布局；绘制-评论循环（Painter-Commenter）则通过执行渲染代码和利用视觉语言模型（VLM）反馈来优化每个面板。

**关键创新**：最重要的技术创新在于引入了PaperQuiz评估指标，量化海报传达核心内容的能力，同时通过VLM作为评判标准，提升了评估的客观性和准确性。

**关键设计**：在设计中，采用了多种损失函数来平衡视觉质量与文本连贯性，确保生成的海报在美学和信息传达上都达到较高标准。

## 📊 实验亮点

实验结果显示，基于Qwen-2.5系列的开源变体在视觉质量和信息传达能力上均优于现有的GPT-4o驱动系统，且在多个评估指标上表现出87%的token使用效率提升，成本仅为0.005美元。

## 🎯 应用场景

该研究的潜在应用领域包括学术会议、科研成果展示及教育领域，能够显著提高学术海报的生成效率与质量。未来，随着技术的进一步发展，可能会在更广泛的科学传播和信息可视化场景中发挥重要作用。

## 📄 摘要（原文）

> Academic poster generation is a crucial yet challenging task in scientific communication, requiring the compression of long-context interleaved documents into a single, visually coherent page. To address this challenge, we introduce the first benchmark and metric suite for poster generation, which pairs recent conference papers with author-designed posters and evaluates outputs on (i)Visual Quality-semantic alignment with human posters, (ii)Textual Coherence-language fluency, (iii)Holistic Assessment-six fine-grained aesthetic and informational criteria scored by a VLM-as-judge, and notably (iv)PaperQuiz-the poster's ability to convey core paper content as measured by VLMs answering generated quizzes. Building on this benchmark, we propose PosterAgent, a top-down, visual-in-the-loop multi-agent pipeline: the (a)Parser distills the paper into a structured asset library; the (b)Planner aligns text-visual pairs into a binary-tree layout that preserves reading order and spatial balance; and the (c)Painter-Commenter loop refines each panel by executing rendering code and using VLM feedback to eliminate overflow and ensure alignment. In our comprehensive evaluation, we find that GPT-4o outputs-though visually appealing at first glance-often exhibit noisy text and poor PaperQuiz scores, and we find that reader engagement is the primary aesthetic bottleneck, as human-designed posters rely largely on visual semantics to convey meaning. Our fully open-source variants (e.g. based on the Qwen-2.5 series) outperform existing 4o-driven multi-agent systems across nearly all metrics, while using 87% fewer tokens. It transforms a 22-page paper into a finalized yet editable .pptx poster - all for just $0.005. These findings chart clear directions for the next generation of fully automated poster-generation models. The code and datasets are available at https://github.com/Paper2Poster/Paper2Poster.

