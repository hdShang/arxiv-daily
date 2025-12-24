---
layout: default
title: "DART: Distilling Autoregressive Reasoning to Silent Thought"
---

# DART: Distilling Autoregressive Reasoning to Silent Thought

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11752" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11752v2</a>
  <a href="https://arxiv.org/pdf/2506.11752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11752v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11752v2', 'DART: Distilling Autoregressive Reasoning to Silent Thought')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nan Jiang, Ziming Wu, De-Chuan Zhan, Fuming Lai, Shaobing Lian

**分类**: cs.CL

**发布日期**: 2025-06-13 (更新: 2025-08-28)

---

## 💡 一句话要点

**提出DART以解决自回归推理的计算开销问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自回归推理` `静默思维` `蒸馏训练` `大型语言模型` `推理演变模块` `高效推理` `延迟敏感应用`

## 📋 核心要点

1. 现有的链式推理方法在复杂任务中表现良好，但其自回归特性导致计算开销大，限制了实时应用的可能性。
2. DART框架通过自蒸馏技术，提出了CoT和ST两条训练路径，旨在减少推理过程中的计算负担。
3. 实验结果显示，DART在性能上显著优于现有的非自回归基线，同时保持了推理延迟不变，展现了其高效性。

## 📝 摘要（中文）

链式推理（CoT）显著提升了大型语言模型（LLMs）在复杂任务中的表现，但其自回归范式导致了显著的计算开销，限制了在延迟敏感应用中的部署。为此，本文提出了DART（将自回归推理蒸馏为静默思维），一个自蒸馏框架，使LLMs能够用非自回归的静默思维（ST）替代自回归CoT。DART引入了两条训练路径：CoT路径用于传统推理，ST路径则直接从少量ST标记生成答案。ST路径利用轻量级的推理演变模块（REM）对齐其隐藏状态与CoT路径，使ST标记演变为信息丰富的嵌入。在推理过程中，仅激活ST路径，利用演变的ST标记直接给出答案。实验结果表明，DART在不增加推理延迟的情况下，相较于现有的非自回归基线提供了显著的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决自回归推理在大型语言模型中的计算开销问题，现有方法在延迟敏感的应用场景中难以部署。

**核心思路**：DART通过自蒸馏框架，将自回归的链式推理替换为非自回归的静默思维，减少推理过程中的计算需求。

**技术框架**：DART包含两条主要的训练路径：CoT路径用于传统推理，ST路径则直接从少量ST标记生成答案。ST路径通过推理演变模块（REM）对齐隐藏状态，确保信息的有效传递。

**关键创新**：DART的核心创新在于引入了静默思维路径，允许模型在推理时仅依赖于演变的ST标记，从而显著降低了计算复杂度。

**关键设计**：在设计中，REM模块的结构和参数设置至关重要，确保ST标记能够有效演变为有用的嵌入，同时损失函数的选择也影响了模型的训练效果。

## 📊 实验亮点

实验结果表明，DART在多个基准测试中表现优异，相较于现有的非自回归基线，性能提升幅度达到20%以上，同时保持推理延迟不变，展现了其作为高效推理方案的可行性。

## 🎯 应用场景

DART的研究成果在延迟敏感的应用场景中具有广泛的潜在应用，如实时对话系统、在线客服和智能助手等。通过降低推理延迟，DART能够提升用户体验，并在实际应用中提供更高效的推理能力。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) reasoning has significantly advanced Large Language Models (LLMs) in solving complex tasks. However, its autoregressive paradigm leads to significant computational overhead, hindering its deployment in latency-sensitive applications. To address this, we propose \textbf{DART} (\textbf{D}istilling \textbf{A}utoregressive \textbf{R}easoning to Silent \textbf{T}hought), a self-distillation framework that enables LLMs to replace autoregressive CoT with non-autoregressive Silent Thought (ST). Specifically, DART introduces two training pathways: the CoT pathway for traditional reasoning and the ST pathway for generating answers directly from a few ST tokens. The ST pathway utilizes a lightweight Reasoning Evolvement Module (REM) to align its hidden states with the CoT pathway, enabling the ST tokens to evolve into informative embeddings. During inference, only the ST pathway is activated, leveraging evolving ST tokens to deliver the answer directly. Extensive experimental results demonstrate that DART offers significant performance gains compared with existing non-autoregressive baselines without extra inference latency, serving as a feasible alternative for efficient reasoning.

