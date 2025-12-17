---
layout: default
title: ESCA: Contextualizing Embodied Agents via Scene-Graph Generation
---

# ESCA: Contextualizing Embodied Agents via Scene-Graph Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15963" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15963v2</a>
  <a href="https://arxiv.org/pdf/2510.15963.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15963v2" onclick="toggleFavorite(this, '2510.15963v2', 'ESCA: Contextualizing Embodied Agents via Scene-Graph Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiani Huang, Amish Sethi, Matthew Kuo, Mayank Keoliya, Neelay Velingker, JungHo Jung, Ser-Nam Lim, Ziyang Li, Mayur Naik

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-11 (更新: 2025-10-27)

**备注**: Accepted as a Spotlight Paper at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/video-fm/LASER) | [GITHUB](https://github.com/video-fm/ESCA)

---

## 💡 一句话要点

**提出ESCA框架，通过场景图生成增强具身智能体的上下文感知能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能体` `场景图生成` `多模态学习` `上下文感知` `开放域视频`

## 📋 核心要点

1. 现有MLLM在具身智能体中存在视觉特征与文本语义关联不足的问题，导致感知能力较弱。
2. ESCA框架通过将智能体的感知 grounding 在时空场景图中，增强了其上下文感知能力。
3. SGCLIP模型在场景图生成和动作定位任务上取得了SOTA结果，并提升了具身智能体的感知性能。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）在通用具身智能体方面取得了快速进展。然而，现有的MLLM无法可靠地捕捉低层视觉特征和高层文本语义之间的细粒度联系，导致弱 grounding 和不准确的感知。为了克服这一挑战，我们提出了ESCA，一个通过将具身智能体的感知 grounding 在时空场景图中来情境化具身智能体的框架。其核心是SGCLIP，一种新颖的、开放域的、可提示的场景图生成基础模型，它基于CLIP。SGCLIP使用神经符号管道在87K+开放域视频上进行训练，该管道将自动生成的字幕与模型自身生成的场景图对齐，从而消除了对人工标注的需求。我们证明了SGCLIP在基于 prompt 的推理和特定任务微调方面都表现出色，在场景图生成和动作定位基准测试中取得了最先进的结果。ESCA与SGCLIP改进了基于开源和商业MLLM的具身智能体的感知能力，在两个具身环境中实现了最先进的性能。值得注意的是，ESCA显著减少了智能体感知错误，并使开源模型能够超越专有基线。我们发布了SGCLIP模型训练的源代码在https://github.com/video-fm/LASER，以及具身智能体的代码在https://github.com/video-fm/ESCA。

## 🔬 方法详解

**问题定义**：现有具身智能体依赖的MLLM无法准确捕捉视觉特征和文本语义之间的细粒度联系，导致感知能力不足，容易产生错误。这限制了智能体在复杂环境中的有效交互和决策。

**核心思路**：论文的核心思路是通过引入场景图来增强智能体的上下文感知能力。场景图能够显式地表示场景中的物体、关系以及它们之间的交互，从而为智能体提供更丰富的环境信息，帮助其更好地理解和推理。

**技术框架**：ESCA框架的核心是SGCLIP模型，它是一个基于CLIP的、开放域的、可提示的场景图生成模型。SGCLIP通过神经符号管道在大量开放域视频上进行训练，该管道自动将生成的字幕与场景图对齐。ESCA框架将SGCLIP生成的场景图作为智能体的输入，从而增强其感知能力。整体流程包括：视频输入 -> SGCLIP生成场景图 -> 场景图与视觉信息输入MLLM -> 智能体决策。

**关键创新**：SGCLIP模型是关键创新点。它无需人工标注，而是通过神经符号管道自动生成训练数据，从而降低了训练成本。此外，SGCLIP是可提示的，可以根据不同的任务进行定制。SGCLIP与现有方法的本质区别在于，它能够生成更准确、更丰富的场景图，从而为智能体提供更全面的环境信息。

**关键设计**：SGCLIP的训练使用了对比学习损失，以鼓励模型学习视觉特征和文本语义之间的对应关系。神经符号管道包含一个 captioning 模型和一个场景图生成模型，它们共同生成训练数据。模型使用了Transformer架构，并针对场景图生成任务进行了优化。具体参数设置和网络结构细节可在论文附录中找到。

## 📊 实验亮点

实验结果表明，ESCA框架显著减少了智能体的感知错误，并使开源模型能够超越专有基线。SGCLIP在场景图生成和动作定位基准测试中取得了SOTA结果。在具身环境中，ESCA与SGCLIP的结合显著提升了智能体的性能。

## 🎯 应用场景

该研究成果可应用于机器人导航、智能家居、自动驾驶等领域。通过增强智能体的上下文感知能力，可以提高其在复杂环境中的适应性和交互能力，使其能够更好地完成各种任务。未来，该技术有望推动具身智能体在现实世界中的广泛应用。

## 📄 摘要（原文）

> Multi-modal large language models (MLLMs) are making rapid progress toward general-purpose embodied agents. However, existing MLLMs do not reliably capture fine-grained links between low-level visual features and high-level textual semantics, leading to weak grounding and inaccurate perception. To overcome this challenge, we propose ESCA, a framework that contextualizes embodied agents by grounding their perception in spatial-temporal scene graphs. At its core is SGCLIP, a novel, open-domain, promptable foundation model for generating scene graphs that is based on CLIP. SGCLIP is trained on 87K+ open-domain videos using a neurosymbolic pipeline that aligns automatically generated captions with scene graphs produced by the model itself, eliminating the need for human-labeled annotations. We demonstrate that SGCLIP excels in both prompt-based inference and task-specific fine-tuning, achieving state-of-the-art results on scene graph generation and action localization benchmarks. ESCA with SGCLIP improves perception for embodied agents based on both open-source and commercial MLLMs, achieving state of-the-art performance across two embodied environments. Notably, ESCA significantly reduces agent perception errors and enables open-source models to surpass proprietary baselines. We release the source code for SGCLIP model training at https://github.com/video-fm/LASER and for the embodied agent at https://github.com/video-fm/ESCA.

