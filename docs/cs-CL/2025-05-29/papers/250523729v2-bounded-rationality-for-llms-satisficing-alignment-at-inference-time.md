---
layout: default
title: "Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time"
---

# Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23729" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23729v2</a>
  <a href="https://arxiv.org/pdf/2505.23729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23729v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23729v2', 'Bounded Rationality for LLMs: Satisficing Alignment at Inference-Time')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamad Chehade, Soumya Suvra Ghosal, Souradip Chakraborty, Avinash Reddy, Dinesh Manocha, Hao Zhu, Amrit Singh Bedi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-29 (更新: 2025-05-31)

**备注**: Accepted at ICML 2025

---

## 💡 一句话要点

**提出SITAlign框架以解决大型语言模型的对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `对齐问题` `满意化策略` `多目标优化` `推理框架`

## 📋 核心要点

1. 现有大型语言模型对齐方法通常忽视人类决策的复杂性，导致效果不佳。
2. 本文提出SITAlign框架，通过最大化主要目标并满足次要目标的阈值约束，实现满意化对齐。
3. 在PKU-SafeRLHF数据集上，SITAlign在有用性和无害性之间取得了显著的性能提升。

## 📝 摘要（中文）

对大型语言模型与人类的对齐问题具有挑战性，现有方法往往将其视为多目标优化问题，但忽视了人类决策的实际过程。研究表明，人类决策遵循满意化策略，即在优化主要目标的同时确保其他目标达到可接受的阈值。为此，本文提出了SITAlign框架，旨在通过最大化主要目标并满足次要标准的阈值约束来实现满意化对齐。我们通过理论推导提供了满意化推理对齐方法的次优性界限，并通过多项基准实验验证了SITAlign的有效性。以PKU-SafeRLHF数据集为例，SITAlign在最大化有用性并确保无害性阈值的情况下，较现有多目标解码策略提升了22.3%的GPT-4胜平率。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型与人类对齐的复杂性，现有方法往往将其简化为多目标优化，未能有效捕捉人类的满意化决策过程。

**核心思路**：SITAlign框架的核心思想是通过最大化一个主要目标（如有用性），同时确保次要目标（如无害性）满足特定的阈值，从而实现更符合人类决策的对齐方式。

**技术框架**：SITAlign的整体架构包括目标函数的设计、约束条件的设置以及推理过程的优化。主要模块包括目标优化模块和约束验证模块，确保在推理时同时考虑主要和次要目标。

**关键创新**：该研究的主要创新在于引入满意化对齐的概念，通过理论推导提供了次优性界限，显著区别于传统的多目标优化方法。

**关键设计**：在参数设置上，SITAlign设计了特定的损失函数以平衡主要和次要目标，采用了适应性阈值策略来动态调整次要目标的约束条件。

## 📊 实验亮点

在PKU-SafeRLHF数据集上，SITAlign在最大化有用性并确保无害性阈值的情况下，较现有的多目标解码策略提升了22.3%的GPT-4胜平率，显示出其在实际应用中的显著优势。

## 🎯 应用场景

SITAlign框架在大型语言模型的应用中具有广泛的潜力，尤其是在需要人机协作的场景，如智能助手、内容生成和对话系统等。通过更好地对齐人类偏好，该方法能够提升用户体验和系统的实用性，未来可能推动更智能的交互方式和应用场景的拓展。

## 📄 摘要（原文）

> Aligning large language models with humans is challenging due to the inherently multifaceted nature of preference feedback. While existing approaches typically frame this as a multi-objective optimization problem, they often overlook how humans actually make decisions. Research on bounded rationality suggests that human decision making follows satisficing strategies-optimizing primary objectives while ensuring others meet acceptable thresholds. To bridge this gap and operationalize the notion of satisficing alignment, we propose SITAlign: an inference time framework that addresses the multifaceted nature of alignment by maximizing a primary objective while satisfying threshold-based constraints on secondary criteria. We provide theoretical insights by deriving sub-optimality bounds of our satisficing based inference alignment approach. We empirically validate SITAlign's performance through extensive experimentation on multiple benchmarks. For instance, on the PKU-SafeRLHF dataset with the primary objective of maximizing helpfulness while ensuring a threshold on harmlessness, SITAlign outperforms the state-of-the-art multi objective decoding strategy by a margin of 22.3% in terms of GPT-4 win-tie rate for helpfulness reward while adhering to the threshold on harmlessness.

