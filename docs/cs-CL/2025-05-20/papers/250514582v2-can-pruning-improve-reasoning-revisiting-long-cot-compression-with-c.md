---
layout: default
title: Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning
---

# Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14582" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14582v2</a>
  <a href="https://arxiv.org/pdf/2505.14582.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14582v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14582v2', 'Can Pruning Improve Reasoning? Revisiting Long-CoT Compression with Capability in Mind for Better Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shangziqi Zhao, Jiahao Yuan, Guisong Yang, Usman Naseem

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-08-26)

**备注**: 19 pages,6 figures

---

## 💡 一句话要点

**提出Prune-on-Logic框架以提升长链思维推理效果**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长链思维` `推理优化` `模型蒸馏` `逻辑图` `自我验证` `选择性修剪` `小型语言模型`

## 📋 核心要点

1. 长链思维推理的冗长风格使得其在蒸馏到小型语言模型时效果不佳，影响了模型的实际应用。
2. 提出Prune-on-Logic框架，通过将长链思维转化为逻辑图，选择性修剪低效推理步骤以优化推理效果。
3. 实验结果显示，验证修剪显著提高了模型的准确性，并在多个任务和模型规模上保持一致的性能提升。

## 📝 摘要（中文）

长链思维（Long-CoT）推理提高了大型语言模型（LLMs）的准确性，但其冗长的自我反思风格常常妨碍有效蒸馏到小型语言模型（SLMs）。本文通过能力对齐的视角重新审视Long-CoT压缩，提出Prune-on-Logic框架，将Long-CoT转化为逻辑图，并在自我验证约束下选择性地修剪低效推理步骤。研究表明，验证修剪能持续提高准确性并减少令牌使用，而推理或无差别修剪则会降低性能。有效的修剪策略能够将监督与模型能力对齐，尤其在更大模型中表现更佳。

## 🔬 方法详解

**问题定义**：本文旨在解决长链思维推理在蒸馏过程中由于冗长和低效步骤导致的性能下降问题。现有方法未能有效处理推理步骤的选择性修剪，影响了小型语言模型的表现。

**核心思路**：提出Prune-on-Logic框架，通过将长链思维转化为逻辑图，利用自我验证约束选择性修剪低效推理步骤，从而提升推理的有效性和准确性。

**技术框架**：该框架包括三个主要模块：逻辑图构建、低效步骤识别和验证修剪。首先，将长链思维转化为逻辑图，然后识别出低效推理步骤，最后在验证约束下进行修剪。

**关键创新**：最重要的创新在于通过逻辑图的结构化表示和自我验证机制，实现了对推理步骤的有效选择性修剪，与传统的无差别修剪方法形成鲜明对比。

**关键设计**：在设计中，采用了针对整个链、核心推理和验证的三种修剪策略，验证修剪被证明是最有效的，能够在减少令牌使用的同时提高准确性。

## 📊 实验亮点

实验结果表明，验证修剪策略在多个任务上显著提高了模型的准确性，减少令牌使用，且在较大模型中效果更为显著，提升幅度可达XX%（具体数据需根据实验结果填写）。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和对话生成等。通过优化推理过程，Prune-on-Logic框架能够提升小型语言模型在实际应用中的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Long chain-of-thought (Long-CoT) reasoning improves accuracy in LLMs, yet its verbose, self-reflective style often hinders effective distillation into small language models (SLMs). We revisit Long-CoT compression through the lens of capability alignment and ask: Can pruning improve reasoning? We propose Prune-on-Logic, a structure-aware framework that transforms Long-CoT into logic graphs and selectively prunes low-utility reasoning steps under self-verification constraints. Through systematic analysis across three pruning strategies - targeting entire chains, core reasoning, and verification - we find that verification pruning consistently improves accuracy while reducing token usage, whereas reasoning or indiscriminate pruning degrades performance. Our study reveals that effective pruning aligns supervision with model capacity rather than merely shortening inputs. Gains hold across tasks, model scales, and CoT capability, with larger models benefiting more from pruning due to richer but more redundant reasoning. Our empirical findings highlight pruning as a structural optimization strategy for aligning CoT reasoning with SLM capacity.

