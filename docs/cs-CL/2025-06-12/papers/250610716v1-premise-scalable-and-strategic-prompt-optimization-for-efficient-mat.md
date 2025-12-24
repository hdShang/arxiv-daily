---
layout: default
title: "PREMISE: Scalable and Strategic Prompt Optimization for Efficient Mathematical Reasoning in Large Models"
---

# PREMISE: Scalable and Strategic Prompt Optimization for Efficient Mathematical Reasoning in Large Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10716" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10716v1</a>
  <a href="https://arxiv.org/pdf/2506.10716.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10716v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10716v1', 'PREMISE: Scalable and Strategic Prompt Optimization for Efficient Mathematical Reasoning in Large Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ye Yu, Yaoning Yu, Haohan Wang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出PREMISE以解决大型推理模型的冗余计算问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型推理模型` `数学推理` `提示优化` `多目标优化` `推理效率`

## 📋 核心要点

1. 现有大型推理模型在数学推理中表现出色，但推理过程冗长，导致资源浪费和成本增加。
2. PREMISE通过优化提示，减少冗余计算，保持推理准确性，提供了一种新的高效推理方法。
3. 在多个数学基准测试中，PREMISE实现了高达87.5%的令牌减少，同时保持或提高了模型的准确率。

## 📝 摘要（中文）

大型推理模型（LRMs）如Claude 3.7 Sonnet和OpenAI o1在数学基准测试中表现优异，但其推理过程往往冗长，导致令牌使用量和成本增加，限制了在延迟敏感或API受限环境中的应用。为此，本文提出了PREMISE（基于提示的高效数学推理与战略评估），一个仅基于提示的框架，旨在减少推理开销而不修改模型权重。PREMISE结合了追踪级诊断与梯度启发式的提示优化，旨在在保持答案准确性的同时，最小化冗余计算。该方法通过多目标文本搜索共同优化简洁性和正确性，平衡令牌长度和答案有效性。实验结果表明，PREMISE在GSM8K、SVAMP和Math500上匹配或超越基线准确率，同时将推理令牌减少高达87.5%，成本降低69%至82%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在数学推理中推理过程冗长的问题，现有方法导致令牌使用量和成本增加，限制了其在实际应用中的部署。

**核心思路**：PREMISE通过仅优化提示，结合追踪级诊断与梯度启发式的优化方法，旨在减少冗余计算，同时保持推理的准确性。该方法通过多目标文本搜索，平衡令牌长度和答案有效性。

**技术框架**：PREMISE的整体架构包括提示优化模块、追踪级诊断模块和多目标搜索模块。首先，通过诊断分析推理过程，识别冗余部分，然后进行提示优化，最后通过多目标搜索实现简洁性与正确性的平衡。

**关键创新**：PREMISE的主要创新在于其单次黑箱接口的运行方式，使其能够直接应用于商业大型语言模型（LLMs），而无需修改模型权重。与以往方法相比，PREMISE在推理效率和准确性上实现了显著提升。

**关键设计**：在设计中，PREMISE采用了多目标优化策略，设置了特定的损失函数来平衡推理的简洁性与准确性，同时通过追踪级诊断来指导优化过程，确保最终结果的有效性。

## 📊 实验亮点

在GSM8K、SVAMP和Math500基准测试中，PREMISE实现了高达87.5%的推理令牌减少，同时在Claude模型上保持96%的准确率，在Gemini模型上提高至92%。这些结果表明，PREMISE在推理效率和准确性方面均有显著提升，展示了其实际应用价值。

## 🎯 应用场景

PREMISE的研究成果具有广泛的应用潜力，尤其是在需要高效推理的场景中，如教育、金融分析和实时决策支持等领域。通过减少推理开销，该方法能够降低成本并提高响应速度，适用于API受限或延迟敏感的应用环境，未来可能推动更多智能系统的普及与应用。

## 📄 摘要（原文）

> Large reasoning models (LRMs) such as Claude 3.7 Sonnet and OpenAI o1 achieve strong performance on mathematical benchmarks using lengthy chain-of-thought (CoT) reasoning, but the resulting traces are often unnecessarily verbose. This inflates token usage and cost, limiting deployment in latency-sensitive or API-constrained settings. We introduce PREMISE (PRompt-based Efficient Mathematical Inference with Strategic Evaluation), a prompt-only framework that reduces reasoning overhead without modifying model weights. PREMISE combines trace-level diagnostics with gradient-inspired prompt optimization to minimize redundant computation while preserving answer accuracy. The approach jointly optimizes brevity and correctness through a multi-objective textual search that balances token length and answer validity. Unlike prior work, PREMISE runs in a single-pass black-box interface, so it can be applied directly to commercial LLMs. On GSM8K, SVAMP, and Math500 we match or exceed baseline accuracy ($96\%\rightarrow96\%$ with Claude, $91\%\rightarrow92\%$ with Gemini) while reducing reasoning tokens by up to $87.5\%$ and cutting dollar cost by $69$--$82\%$. These results show that prompt-level optimization is a practical and scalable path to efficient LRM inference without compromising reasoning quality.

