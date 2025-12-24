---
layout: default
title: "VF-Eval: Evaluating Multimodal LLMs for Generating Feedback on AIGC Videos"
---

# VF-Eval: Evaluating Multimodal LLMs for Generating Feedback on AIGC Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23693" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23693v1</a>
  <a href="https://arxiv.org/pdf/2505.23693.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23693v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23693v1', 'VF-Eval: Evaluating Multimodal LLMs for Generating Feedback on AIGC Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tingyu Song, Tongyan Hu, Guo Gan, Yilun Zhao

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-05-29

**备注**: ACL 2025 Main

---

## 💡 一句话要点

**提出VF-Eval以评估多模态LLM在AIGC视频反馈生成中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `合成视频` `AI生成内容` `视频生成` `评估基准` `连贯性验证` `错误检测` `推理评估`

## 📋 核心要点

1. 现有方法主要集中在自然视频的评估，缺乏对合成视频（如AIGC）的深入研究，导致MLLMs在此领域的能力未被充分探索。
2. 论文提出VF-Eval基准，通过四个任务全面评估MLLMs在AIGC视频上的表现，填补了这一研究空白。
3. 实验结果显示，尽管GPT-4.1表现最佳，但在所有任务中仍难以实现一致的优异表现，强调了基准的挑战性和重要性。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在视频问答领域得到了广泛研究，但现有评估主要集中在自然视频上，忽视了合成视频（如AI生成内容，AIGC）。本研究提出了一个新基准VF-Eval，包含四个任务：连贯性验证、错误意识、错误类型检测和推理评估，以全面评估MLLMs在AIGC视频上的能力。我们对13个前沿的MLLMs进行了评估，发现即使是表现最好的模型GPT-4.1在所有任务上也难以保持一致的良好表现，突显了基准的挑战性。此外，我们通过实验RePrompt探讨了VF-Eval在改善视频生成中的实际应用，表明更紧密地与人类反馈对齐的MLLMs可以提升视频生成质量。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有评估方法对合成视频（AIGC）能力的忽视，现有方法在评估MLLMs时主要集中于自然视频，导致对合成视频的理解和反馈生成能力评估不足。

**核心思路**：提出VF-Eval基准，通过设计连贯性验证、错误意识、错误类型检测和推理评估四个任务，全面评估MLLMs在AIGC视频上的能力，旨在填补这一领域的研究空白。

**技术框架**：VF-Eval基准的整体架构包括四个主要模块：1) 连贯性验证，评估视频内容的逻辑连贯性；2) 错误意识，检测生成视频中的错误；3) 错误类型检测，识别错误的具体类型；4) 推理评估，考察模型对视频内容的推理能力。

**关键创新**：VF-Eval的最大创新在于其针对AIGC视频的专门设计，提供了一个全面的评估框架，区别于以往仅针对自然视频的评估方法，填补了研究空白。

**关键设计**：在实验中，采用了多种评估指标和损失函数，以确保对各个任务的准确评估，模型选择涵盖了13个前沿的MLLMs，确保了结果的广泛性和代表性。实验设计中还考虑了与人类反馈的对齐，以提升视频生成的质量。

## 📊 实验亮点

实验结果显示，尽管GPT-4.1在评估中表现最佳，但在连贯性验证、错误意识等任务上仍未能达到一致的优异表现，突显了VF-Eval基准的挑战性。该基准的设计为未来的研究提供了重要参考。

## 🎯 应用场景

VF-Eval基准的提出为AIGC视频生成和评估提供了新的工具，能够帮助研究人员和开发者更好地理解和优化多模态大语言模型在视频生成中的应用。未来，该基准有望推动AIGC领域的进一步研究，提升生成视频的质量和用户体验。

## 📄 摘要（原文）

> MLLMs have been widely studied for video question answering recently. However, most existing assessments focus on natural videos, overlooking synthetic videos, such as AI-generated content (AIGC). Meanwhile, some works in video generation rely on MLLMs to evaluate the quality of generated videos, but the capabilities of MLLMs on interpreting AIGC videos remain largely underexplored. To address this, we propose a new benchmark, VF-Eval, which introduces four tasks-coherence validation, error awareness, error type detection, and reasoning evaluation-to comprehensively evaluate the abilities of MLLMs on AIGC videos. We evaluate 13 frontier MLLMs on VF-Eval and find that even the best-performing model, GPT-4.1, struggles to achieve consistently good performance across all tasks. This highlights the challenging nature of our benchmark. Additionally, to investigate the practical applications of VF-Eval in improving video generation, we conduct an experiment, RePrompt, demonstrating that aligning MLLMs more closely with human feedback can benefit video generation.

