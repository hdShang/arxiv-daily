---
layout: default
title: Beyond Accuracy: A Geometric Stability Analysis of Large Language Models in Chess Evaluation
---

# Beyond Accuracy: A Geometric Stability Analysis of Large Language Models in Chess Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15033" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15033v1</a>
  <a href="https://arxiv.org/pdf/2512.15033.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15033v1" onclick="toggleFavorite(this, '2512.15033v1', 'Beyond Accuracy: A Geometric Stability Analysis of Large Language Models in Chess Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xidan Song, Weiqi Wang, Ruifeng Cao, Qingya Hu

**分类**: cs.AI

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出几何稳定性框架，评估大语言模型在棋类评估中的推理能力，揭示准确率与鲁棒性悖论。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `几何稳定性` `棋类评估` `鲁棒性` `推理能力` `不变变换` `准确率-稳定性悖论`

## 📋 核心要点

1. 现有LLM在复杂推理任务中，仅依赖准确率评估，无法区分模型是真正理解还是简单记忆。
2. 提出几何稳定性框架，通过对棋盘进行几何变换，考察模型在变换下评估结果的一致性。
3. 实验表明，高准确率模型在几何变换下性能显著下降，揭示了准确率与鲁棒性之间的悖论。

## 📝 摘要（中文）

大型语言模型（LLM）在复杂推理领域的评估通常依赖于与真实标准答案的性能对齐。在国际象棋领域，这种标准体现为针对Stockfish等强大引擎的准确性基准。然而，高标量准确率并不一定意味着稳健的概念理解。本文认为，标准准确性指标无法区分真正的几何推理和对规范棋盘状态的表面记忆。为了解决这一差距，我们提出了一种几何稳定性框架，这是一种新颖的评估方法，严格测试模型在不变变换（包括棋盘旋转、镜像对称、颜色反转和格式转换）下的一致性。我们利用约3,000个位置的数据集，将该框架应用于对包括GPT-5.1、Claude Sonnet 4.5和Kimi K2 Turbo在内的六个最先进的LLM的比较分析。我们的结果揭示了一个显著的准确率-稳定性悖论。虽然GPT-5.1等模型在标准位置上实现了接近最优的准确率，但它们在几何扰动下表现出灾难性的退化，特别是在旋转任务中，错误率飙升超过600%。这种差异表明模型依赖于模式匹配而非抽象空间逻辑。相反，Claude Sonnet 4.5和Kimi K2 Turbo表现出卓越的双重鲁棒性，在所有变换轴上保持高度一致性。此外，我们分析了有用性和安全性之间的权衡，确定Gemini 2.5 Flash在非法状态拒绝方面处于领先地位（96.0%）。我们得出结论，几何稳定性为AI评估提供了一个正交且必不可少的指标，为区分大规模模型中的推理能力与数据污染和过度拟合提供了一个必要的代理。

## 🔬 方法详解

**问题定义**：现有的大语言模型在国际象棋等复杂推理任务中的评估，主要依赖于与标准答案（如Stockfish引擎的评估）的准确率对齐。然而，仅仅追求高准确率无法区分模型是真正理解了棋局的几何关系和策略，还是仅仅记忆了大量的棋盘状态。这种记忆性的学习方式缺乏泛化能力，在面对稍作变化的棋局时，性能会显著下降。因此，如何更有效地评估LLM在复杂推理任务中的真正理解能力是一个关键问题。

**核心思路**：论文的核心思路是通过引入几何变换来评估LLM的稳定性。具体来说，就是对棋盘进行旋转、镜像、颜色反转等变换，然后让LLM对变换后的棋局进行评估。如果LLM真正理解了棋局的本质，那么它在变换前后的评估结果应该是一致的。如果LLM只是记忆了棋盘状态，那么在变换后，它的评估结果可能会出现显著的偏差。通过这种方式，可以有效地衡量LLM的推理能力，并区分其是基于真正的理解还是简单的记忆。

**技术框架**：该论文提出的几何稳定性框架主要包含以下几个阶段：1. **数据集构建**：构建包含大量国际象棋棋局的数据集。2. **几何变换**：对数据集中的棋局进行一系列几何变换，包括旋转、镜像、颜色反转和格式转换。3. **模型评估**：使用待评估的LLM对原始棋局和变换后的棋局进行评估，得到相应的评估结果。4. **稳定性分析**：比较LLM在原始棋局和变换后的棋局上的评估结果，计算稳定性指标，例如评估结果的一致性程度。5. **性能分析**：分析LLM在不同变换下的性能表现，揭示其在不同方面的优势和不足。

**关键创新**：该论文最重要的技术创新点在于提出了几何稳定性这一概念，并将其应用于LLM的评估中。与传统的准确率评估方法相比，几何稳定性评估能够更有效地衡量LLM的推理能力，并区分其是基于真正的理解还是简单的记忆。这种评估方法为我们更全面地了解LLM的性能提供了新的视角。

**关键设计**：在几何变换方面，论文考虑了多种变换方式，包括棋盘旋转（例如旋转90度、180度、270度）、镜像对称（水平镜像和垂直镜像）、颜色反转（黑白棋子颜色互换）以及格式转换（例如将FEN格式转换为另一种棋局表示格式）。这些变换旨在考察LLM在不同方面的鲁棒性。在稳定性指标方面，论文可能使用了评估结果的差异程度、一致性比例等指标来衡量LLM在变换前后的评估结果的一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15033v1/images/Chart_Stacked_Bar.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15033v1/images/consistency_board_mark.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15033v1/images/tactical_board_mark.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，GPT-5.1在标准棋局上表现出接近最优的准确率，但在旋转变换下错误率飙升超过600%，揭示了其对模式匹配的过度依赖。相反，Claude Sonnet 4.5和Kimi K2 Turbo在所有变换轴上保持了较高的稳定性。Gemini 2.5 Flash在非法状态拒绝方面表现出色，达到了96.0%的准确率。

## 🎯 应用场景

该研究提出的几何稳定性评估框架可广泛应用于评估LLM在各种复杂推理任务中的能力，例如数学问题求解、代码生成、逻辑推理等。通过该框架，可以更有效地识别LLM的优势和不足，并指导模型的设计和训练，提高其在实际应用中的可靠性和泛化能力。此外，该研究也为AI安全评估提供了一种新的思路，有助于发现模型潜在的风险。

## 📄 摘要（原文）

> The evaluation of Large Language Models (LLMs) in complex reasoning domains typically relies on performance alignment with ground-truth oracles. In the domain of chess, this standard manifests as accuracy benchmarks against strong engines like Stockfish. However, high scalar accuracy does not necessarily imply robust conceptual understanding. This paper argues that standard accuracy metrics fail to distinguish between genuine geometric reasoning and the superficial memorization of canonical board states. To address this gap, we propose a Geometric Stability Framework, a novel evaluation methodology that rigorously tests model consistency under invariant transformations-including board rotation, mirror symmetry, color inversion, and format conversion. We applied this framework to a comparative analysis of six state-of-the-art LLMs including GPT-5.1, Claude Sonnet 4.5, and Kimi K2 Turbo, utilizing a dataset of approximately 3,000 positions. Our results reveal a significant Accuracy-Stability Paradox. While models such as GPT-5.1 achieve near-optimal accuracy on standard positions, they exhibit catastrophic degradation under geometric perturbation, specifically in rotation tasks where error rates surge by over 600%. This disparity suggests a reliance on pattern matching over abstract spatial logic. Conversely, Claude Sonnet 4.5 and Kimi K2 Turbo demonstrate superior dual robustness, maintaining high consistency across all transformation axes. Furthermore, we analyze the trade-off between helpfulness and safety, identifying Gemini 2.5 Flash as the leader in illegal state rejection (96.0%). We conclude that geometric stability provides an orthogonal and essential metric for AI evaluation, offering a necessary proxy for disentangling reasoning capabilities from data contamination and overfitting in large-scale models.

