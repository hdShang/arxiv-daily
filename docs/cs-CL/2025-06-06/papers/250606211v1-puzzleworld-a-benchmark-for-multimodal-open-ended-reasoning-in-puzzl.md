---
layout: default
title: "PuzzleWorld: A Benchmark for Multimodal, Open-Ended Reasoning in Puzzlehunts"
---

# PuzzleWorld: A Benchmark for Multimodal, Open-Ended Reasoning in Puzzlehunts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06211" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06211v1</a>
  <a href="https://arxiv.org/pdf/2506.06211.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06211v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06211v1', 'PuzzleWorld: A Benchmark for Multimodal, Open-Ended Reasoning in Puzzlehunts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengzhi Li, Brendon Jiang, Alexander Naehu, Regan Song, Justin Zhang, Megan Tjandrasuwita, Chanakya Ekbote, Steven-Shine Chen, Adithya Balachandran, Wei Dai, Rebecca Chang, Paul Pu Liang

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-06-06

**🔗 代码/项目**: [GITHUB](https://github.com/MIT-MI/PuzzleWorld)

---

## 💡 一句话要点

**提出PuzzleWorld基准以解决多模态开放式推理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `开放式问题` `PuzzleWorld` `推理基准` `认知技能` `科学发现` `数据分析`

## 📋 核心要点

1. 现有推理基准在处理开放式问题时表现不佳，尤其是在多模态和复杂推理任务中。
2. 提出PuzzleWorld基准，通过667个谜题风格问题，评估模型的多模态推理能力和创造性。
3. 实验结果显示，现有模型在PuzzleWorld上表现不佳，微调模型后逐步推理能力显著提升。

## 📝 摘要（中文）

Puzzlehunts是一种复杂的多步骤谜题，缺乏明确的问题定义。与传统推理基准不同，Puzzlehunts要求模型从多模态证据和迭代推理中发现潜在问题结构，反映了科学发现、探索性数据分析或调查性问题解决等现实世界领域的特征。本文提出了PuzzleWorld，一个包含667个谜题风格问题的大规模基准，旨在评估逐步、开放式和创造性的多模态推理。每个谜题都附有最终解决方案、详细推理轨迹和认知技能标签，支持全面基准测试和细致的诊断分析。现有最先进模型的最终答案准确率仅为1-2%，最佳模型仅解决了14%的谜题，逐步准确率达到40%。通过对推理轨迹进行微调，模型的逐步推理能力从4%提升至11%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推理模型在开放式、多模态推理任务中的不足，尤其是在缺乏明确问题定义的情况下，模型的推理能力受到限制。

**核心思路**：通过构建PuzzleWorld基准，提供667个谜题风格问题，模型需从多模态证据中推导出问题结构，促进更具创造性的推理能力。

**技术框架**：PuzzleWorld的整体架构包括问题生成、推理轨迹记录和认知技能标注三个主要模块，支持全面的性能评估和分析。

**关键创新**：PuzzleWorld的最大创新在于其开放式问题设计和详细的推理轨迹注释，使得模型不仅能给出答案，还能展示推理过程，区别于传统的明确指令任务。

**关键设计**：在模型训练中，采用了针对推理轨迹的微调策略，损失函数设计上强调推理过程的重要性，避免仅依赖最终答案，确保模型能够进行有效的逐步推理。

## 📊 实验亮点

实验结果表明，现有最先进模型在PuzzleWorld上的最终答案准确率仅为1-2%，最佳模型解决了14%的谜题，逐步准确率达到40%。通过对推理轨迹进行微调，模型的逐步推理能力从4%提升至11%，显示出推理轨迹的重要性。

## 🎯 应用场景

PuzzleWorld的研究成果可广泛应用于科学发现、数据分析和调查性问题解决等领域，推动多模态推理系统的发展。其开放式的设计理念将促进更具创造性和灵活性的人工智能应用，提升模型在复杂任务中的表现。

## 📄 摘要（原文）

> Puzzlehunts are a genre of complex, multi-step puzzles lacking well-defined problem definitions. In contrast to conventional reasoning benchmarks consisting of tasks with clear instructions, puzzlehunts require models to discover the underlying problem structure from multimodal evidence and iterative reasoning, mirroring real-world domains such as scientific discovery, exploratory data analysis, or investigative problem-solving. Despite recent progress in foundation models, their performance on such open-ended settings remains largely untested. In this paper, we introduce PuzzleWorld, a large-scale benchmark of 667 puzzlehunt-style problems designed to assess step-by-step, open-ended, and creative multimodal reasoning. Each puzzle is annotated with the final solution, detailed reasoning traces, and cognitive skill labels, enabling holistic benchmarking and fine-grained diagnostic analysis. Most state-of-the-art models achieve only 1-2% final answer accuracy, with the best model solving only 14% of puzzles and reaching 40% stepwise accuracy. To demonstrate the value of our reasoning annotations, we show that fine-tuning a small model on reasoning traces improves stepwise reasoning from 4% to 11%, while training on final answers alone degrades performance to near zero. Our error analysis reveals that current models exhibit myopic reasoning, are bottlenecked by the limitations of language-based inference, and lack sketching capabilities crucial for visual and spatial reasoning. We release PuzzleWorld at https://github.com/MIT-MI/PuzzleWorld to support future work on building more general, open-ended, and creative reasoning systems.

