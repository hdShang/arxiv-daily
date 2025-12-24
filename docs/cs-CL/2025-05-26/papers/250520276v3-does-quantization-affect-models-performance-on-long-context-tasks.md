---
layout: default
title: "Does quantization affect models' performance on long-context tasks?"
---

# Does quantization affect models' performance on long-context tasks?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20276" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20276v3</a>
  <a href="https://arxiv.org/pdf/2505.20276.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20276v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20276v3', 'Does quantization affect models\' performance on long-context tasks?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anmol Mekala, Anirudh Atmakuru, Yixiao Song, Marzena Karpinska, Mohit Iyyer

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26 (更新: 2025-09-20)

**备注**: to appear in EMNLP 2025

---

## 💡 一句话要点

**系统评估量化对长上下文任务的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文任务` `量化模型` `性能评估` `大型语言模型` `自然语言处理`

## 📋 核心要点

1. 现有的长上下文任务处理方法在量化后可能会显著降低性能，尤其是在非英语输入时。
2. 本研究通过系统评估不同量化方法对长输入任务的影响，提出了量化模型的性能评估框架。
3. 实验结果显示，8位量化对准确性影响较小，而4位量化方法在长上下文任务中损失严重，强调了任务特异性评估的重要性。

## 📝 摘要（中文）

大型语言模型（LLMs）现在支持超过128K标记的上下文窗口，但这带来了显著的内存需求和高推理延迟。量化可以缓解这些成本，但可能会降低性能。本研究首次系统评估了量化LLMs在长输入（>64K标记）和长输出任务上的表现。我们的评估涵盖了9.7K个测试示例、五种量化方法（FP8、GPTQ-int8、AWQ-int4、GPTQ-int4、BNB-nf4）和五个模型（Llama-3.1 8B和70B；Qwen-2.5 7B、32B和72B）。结果表明，8位量化平均保持准确性（约0.8%的下降），而4位方法则导致显著损失，尤其是在涉及长上下文输入的任务中（下降高达59%）。

## 🔬 方法详解

**问题定义**：本研究旨在解决量化对大型语言模型在长上下文任务中性能影响的问题。现有方法在处理长输入时，量化可能导致显著的性能下降，尤其是在非英语输入的情况下。

**核心思路**：论文通过系统评估不同量化方法（如FP8、GPTQ-int8等）对长输入任务的影响，提供了量化模型性能的全面分析，强调了任务特异性的重要性。

**技术框架**：研究设计了一个评估框架，涵盖了9.7K个测试示例，使用五种量化方法和五个不同的模型，比较它们在长上下文任务中的表现。

**关键创新**：本研究首次系统性地评估了量化LLMs在长输入任务中的表现，揭示了不同量化方法、模型和任务之间的复杂关系，提供了量化模型使用的指导。

**关键设计**：在实验中，使用了多种量化方法，并对比了不同模型的表现，特别关注了8位和4位量化对任务性能的影响，发现8位量化保持了约0.8%的准确性，而4位量化在长上下文任务中可能导致高达59%的性能下降。

## 📊 实验亮点

实验结果显示，8位量化方法在长上下文任务中仅导致约0.8%的性能下降，而4位量化方法则在某些任务中导致高达59%的性能损失。不同模型在相同量化方法下表现差异显著，强调了任务特异性评估的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等，尤其是在需要处理长文本的场景中。通过优化量化方法，可以在降低内存需求和推理延迟的同时，保持模型的性能，从而提升实际应用的效率和效果。

## 📄 摘要（原文）

> Large language models (LLMs) now support context windows exceeding 128K tokens, but this comes with significant memory requirements and high inference latency. Quantization can mitigate these costs, but may degrade performance. In this work, we present the first systematic evaluation of quantized LLMs on tasks with long inputs (>64K tokens) and long-form outputs. Our evaluation spans 9.7K test examples, five quantization methods (FP8, GPTQ-int8, AWQ-int4, GPTQ-int4, BNB-nf4), and five models (Llama-3.1 8B and 70B; Qwen-2.5 7B, 32B, and 72B). We find that, on average, 8-bit quantization preserves accuracy (~0.8% drop), whereas 4-bit methods lead to substantial losses, especially for tasks involving long-context inputs (drops of up to 59%). This degradation tends to worsen when the input is in a language other than English. Crucially, the effects of quantization depend heavily on the quantization method, model, and task. For instance, while Qwen-2.5 72B remains robust under BNB-nf4, Llama-3.1 70B experiences a 32% performance drop on the same task. These findings highlight the importance of a careful, task-specific evaluation before deploying quantized LLMs, particularly in long-context scenarios and for languages other than English.

