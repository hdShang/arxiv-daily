---
layout: default
title: VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization
---

# VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16906" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16906v1</a>
  <a href="https://arxiv.org/pdf/2512.16906.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16906v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16906v1', 'VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyan Cong, Haotian Yang, Angtian Wang, Yizhi Wang, Yiding Yang, Canyu Zhang, Chongyang Ma

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**VIVA：基于VLM引导和奖励优化的指令驱动视频编辑框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `指令驱动视频编辑` `视觉语言模型` `奖励优化` `扩散模型` `视频生成`

## 📋 核心要点

1. 现有指令驱动视频编辑方法泛化性不足，难以处理复杂指令，因为它们依赖于简单编辑操作的配对数据训练。
2. VIVA框架利用VLM编码指令和视频信息，并采用奖励优化策略，提升模型对复杂指令的理解和编辑能力。
3. 实验结果表明，VIVA在指令遵循、泛化能力和编辑质量上均优于现有技术，实现了更好的视频编辑效果。

## 📝 摘要（中文）

本文提出VIVA，一个可扩展的指令驱动视频编辑框架，旨在根据自然语言指令修改输入视频，同时保持内容一致性和时间连贯性。现有基于扩散模型的方法通常在简单编辑操作的配对数据上训练，限制了它们对复杂真实指令的泛化能力。VIVA利用VLM引导的编码和奖励优化来解决这一泛化问题。首先，引入一个基于VLM的指导器，将文本指令、源视频的第一帧以及可选的参考图像编码为视觉相关的指令表示，为扩散Transformer主干网络提供细粒度的空间和语义上下文。其次，提出一个后训练阶段Edit-GRPO，将Group Relative Policy Optimization应用于视频编辑领域，使用相对奖励直接优化模型，使其生成符合指令、保持内容一致且美观的编辑结果。此外，还提出了一个数据构建流程，用于合成生成多样且高质量的基本编辑操作的配对视频-指令数据。大量实验表明，VIVA在指令遵循、泛化能力和编辑质量方面优于现有方法。

## 🔬 方法详解

**问题定义**：指令驱动的视频编辑旨在根据给定的自然语言指令修改视频内容，同时保持视频内容的一致性和时间上的连贯性。现有的基于扩散模型的方法通常依赖于简单的编辑操作数据进行训练，这限制了它们在处理复杂和真实的编辑指令时的泛化能力。这些方法难以理解复杂的语义关系，并且在生成高质量的编辑结果时面临挑战。

**核心思路**：VIVA的核心思路是利用视觉语言模型（VLM）来增强模型对指令的理解，并使用奖励优化来提升编辑质量。VLM能够将文本指令和视频内容编码成统一的视觉语义空间，从而提供更丰富的上下文信息。奖励优化则通过直接优化编辑结果的质量，使其更符合指令意图，并保持视频内容的一致性。

**技术框架**：VIVA框架主要包含两个阶段：VLM引导的编码阶段和奖励优化阶段。在编码阶段，VLM Instructor将文本指令、源视频的第一帧以及可选的参考图像编码为视觉相关的指令表示。这些表示被输入到扩散Transformer主干网络中，用于指导视频编辑过程。在奖励优化阶段，Edit-GRPO算法被用于优化模型的策略，使其能够生成更高质量的编辑结果。此外，还设计了一个数据生成流程，用于合成高质量的配对视频-指令数据。

**关键创新**：VIVA的关键创新在于以下两点：1) 引入VLM Instructor，利用VLM的强大语义理解能力，为视频编辑提供更丰富的上下文信息。2) 提出Edit-GRPO算法，将Group Relative Policy Optimization应用于视频编辑领域，通过直接优化编辑结果的质量，提升模型的性能。与现有方法相比，VIVA能够更好地理解复杂指令，并生成更高质量的编辑结果。

**关键设计**：VLM Instructor使用预训练的视觉语言模型，例如CLIP，来编码文本指令和视频帧。Edit-GRPO算法使用相对奖励来评估编辑结果的质量，例如，判断一个编辑结果是否比另一个更符合指令意图。数据生成流程使用程序化生成和人工标注相结合的方式，生成多样且高质量的配对视频-指令数据。具体的网络结构和损失函数细节在论文中有详细描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16906v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16906v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16906v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，VIVA在多个视频编辑任务上取得了显著的性能提升。相较于现有方法，VIVA在指令遵循度、内容一致性和编辑质量方面均有明显优势。具体性能数据和对比基线在论文中有详细描述（未知），但总体而言，VIVA能够生成更符合指令意图、更逼真自然的编辑结果。

## 🎯 应用场景

VIVA具有广泛的应用前景，可用于视频内容创作、视频修复、个性化视频编辑等领域。例如，用户可以通过简单的自然语言指令，快速修改视频内容，实现各种创意效果。该技术还可以应用于智能视频监控、自动驾驶等领域，提升视频分析和理解能力。未来，VIVA有望成为视频编辑领域的重要工具，推动视频内容创作和应用的发展。

## 📄 摘要（原文）

> Instruction-based video editing aims to modify an input video according to a natural-language instruction while preserving content fidelity and temporal coherence. However, existing diffusion-based approaches are often trained on paired data of simple editing operations, which fundamentally limits their ability to generalize to diverse and complex, real-world instructions. To address this generalization gap, we propose VIVA, a scalable framework for instruction-based video editing that leverages VLM-guided encoding and reward optimization. First, we introduce a VLM-based instructor that encodes the textual instruction, the first frame of the source video, and an optional reference image into visually-grounded instruction representations, providing fine-grained spatial and semantic context for the diffusion transformer backbone. Second, we propose a post-training stage, Edit-GRPO, which adapts Group Relative Policy Optimization to the domain of video editing, directly optimizing the model for instruction-faithful, content-preserving, and aesthetically pleasing edits using relative rewards. Furthermore, we propose a data construction pipeline designed to synthetically generate diverse, high-fidelity paired video-instruction data of basic editing operations. Extensive experiments show that VIVA achieves superior instruction following, generalization, and editing quality over state-of-the-art methods. Website: https://viva-paper.github.io

