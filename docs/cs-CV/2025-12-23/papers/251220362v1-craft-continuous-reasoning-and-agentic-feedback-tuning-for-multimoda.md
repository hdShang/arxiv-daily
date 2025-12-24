---
layout: default
title: CRAFT: Continuous Reasoning and Agentic Feedback Tuning for Multimodal Text-to-Image Generation
---

# CRAFT: Continuous Reasoning and Agentic Feedback Tuning for Multimodal Text-to-Image Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20362" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20362v1</a>
  <a href="https://arxiv.org/pdf/2512.20362.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20362v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20362v1', 'CRAFT: Continuous Reasoning and Agentic Feedback Tuning for Multimodal Text-to-Image Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: V. Kovalev, A. Kuvshinov, A. Buzovkin, D. Pokidov, D. Timonin

**分类**: cs.CV

**发布日期**: 2025-12-23

**备注**: 37 pages, 42 figures

---

## 💡 一句话要点

**CRAFT：用于多模态文图生成的持续推理和Agent反馈调整框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文图生成` `多模态学习` `推理时优化` `Agent反馈` `视觉语言模型`

## 📋 核心要点

1. 现有文图生成方法依赖隐式、整体的评价或无约束的提示重写，行为难以解释、控制和停止。
2. CRAFT框架将提示分解为视觉问题，利用视觉-语言模型验证图像，并通过LLM Agent进行有针对性的提示编辑。
3. 实验表明，CRAFT显著提升了组合准确性、文本渲染和用户偏好，且推理开销极小，使轻量模型性能逼近重型模型。

## 📝 摘要（中文）

本文提出CRAFT（Continuous Reasoning and Agentic Feedback Tuning），一个无需训练、模型无关的框架，旨在将结构化推理范式引入多模态图像生成。CRAFT将提示分解为依赖结构的视觉问题，使用视觉-语言模型验证生成的图像，并仅在约束失败时通过LLM Agent应用有针对性的提示编辑。该过程迭代进行，直到满足所有约束条件，从而产生可解释和可控的推理时细化循环。在多个模型系列和具有挑战性的基准测试中，CRAFT始终如一地提高了组合准确性、文本渲染和基于偏好的评估，对于轻量级生成器而言，收益尤其显著。重要的是，这些改进仅产生可忽略不计的推理时开销，从而使更小或更便宜的模型能够接近更昂贵系统的质量。结果表明，显式结构化、约束驱动的推理时推理是提高多模态生成模型可靠性的关键要素。

## 🔬 方法详解

**问题定义**：现有的文本到图像生成方法在推理时的改进通常依赖于隐式的、整体性的评价，或者是不受约束的提示重写。这导致这些方法的行为难以解释、控制，并且无法可靠地停止。因此，如何设计一种可解释、可控且可靠的推理时改进框架是一个关键问题。

**核心思路**：CRAFT的核心思路是将结构化推理引入到多模态图像生成中。借鉴大型语言模型中基于验证、有针对性的纠正和提前停止的显式、结构化思考方式，CRAFT将复杂的提示分解为更小的、可验证的视觉约束，并迭代地改进图像生成，直到满足所有约束。

**技术框架**：CRAFT框架包含以下几个主要模块：1) 提示分解：将原始文本提示分解为一系列依赖结构的视觉问题。2) 图像生成：使用现有的文本到图像生成模型生成图像。3) 图像验证：使用视觉-语言模型验证生成的图像是否满足分解后的视觉约束。4) 提示编辑：如果图像未能满足约束，则使用LLM Agent对提示进行有针对性的编辑，以纠正图像中的错误。5) 迭代与停止：重复图像生成、验证和编辑的过程，直到所有约束都得到满足，或者达到预设的迭代次数。

**关键创新**：CRAFT的关键创新在于其显式、结构化的推理过程。与现有方法相比，CRAFT不是简单地重写整个提示或进行整体性的评价，而是将提示分解为可验证的约束，并针对性地纠正图像中的错误。这种方法提高了生成过程的可解释性和可控性。

**关键设计**：CRAFT的关键设计包括：1) 使用依赖结构来组织视觉问题，以确保问题之间的逻辑关系。2) 使用视觉-语言模型进行图像验证，以确保验证的准确性。3) 使用LLM Agent进行提示编辑，以确保编辑的有效性和针对性。4) 设计明确的停止准则，以确保生成过程的效率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20362v1/images/image01.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20362v1/images/image02.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20362v1/images/image03.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

CRAFT在多个模型系列和具有挑战性的基准测试中，始终如一地提高了组合准确性、文本渲染和基于偏好的评估。尤其对于轻量级生成器，收益更为显著。值得注意的是，这些改进仅带来了可忽略不计的推理时开销，使得更小或更便宜的模型能够接近更昂贵系统的质量。

## 🎯 应用场景

CRAFT框架可应用于各种需要高质量、可控图像生成的场景，例如：电商产品图生成、游戏美术设计、广告创意生成、教育内容创作等。通过提高生成图像的准确性和可控性，CRAFT可以帮助用户更高效地生成符合需求的图像内容，并降低人工干预的成本。未来，CRAFT有望成为多模态内容生成领域的重要组成部分。

## 📄 摘要（原文）

> Recent work has shown that inference-time reasoning and reflection can improve text-to-image generation without retraining. However, existing approaches often rely on implicit, holistic critiques or unconstrained prompt rewrites, making their behavior difficult to interpret, control, or stop reliably. In contrast, large language models have benefited from explicit, structured forms of **thinking** based on verification, targeted correction, and early stopping.
>   We introduce CRAFT (Continuous Reasoning and Agentic Feedback Tuning), a training-free, model-agnostic framework that brings this structured reasoning paradigm to multimodal image generation. CRAFT decomposes a prompt into dependency-structured visual questions, veries generated images using a vision-language model, and applies targeted prompt edits through an LLM agent only where constraints fail. The process iterates with an explicit stopping criterion once all constraints are satised, yielding an interpretable and controllable inference-time renement loop.
>   Across multiple model families and challenging benchmarks, CRAFT consistently improves compositional accuracy, text rendering, and preference-based evaluations, with particularly strong gains for lightweight generators. Importantly, these improvements incur only a negligible inference-time overhead, allowing smaller or cheaper models to approach the quality of substantially more expensive systems. Our results suggest that explicitly structured, constraint-driven inference-time reasoning is a key ingredient for improving the reliability of multimodal generative models.

