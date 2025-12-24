---
layout: default
title: "Visual-CoG: Stage-Aware Reinforcement Learning with Chain of Guidance for Text-to-Image Generation"
---

# Visual-CoG: Stage-Aware Reinforcement Learning with Chain of Guidance for Text-to-Image Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18032" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18032v2</a>
  <a href="https://arxiv.org/pdf/2508.18032.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18032v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18032v2', 'Visual-CoG: Stage-Aware Reinforcement Learning with Chain of Guidance for Text-to-Image Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaqi Li, Peng Chen, Mingyang Han, Pi Bu, Haoxiang Shi, Runzhou Zhao, Yang Yao, Xuan Zhang, Jun Song, Bo Zheng

**分类**: cs.CV

**发布日期**: 2025-08-25 (更新: 2025-08-26)

---

## 💡 一句话要点

**提出Visual-CoG以解决文本到图像生成中的多属性和模糊提示问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `强化学习` `链式思维` `阶段感知` `视觉合成` `语义推理` `生成模型`

## 📋 核心要点

1. 现有文本到图像生成模型在处理多属性和模糊提示时存在显著局限，难以有效识别各阶段的贡献。
2. 本文提出Visual-CoG框架，通过引入阶段感知奖励机制，优化生成过程中的每个阶段，提升推理能力。
3. 在GenEval、T2I-CompBench和VisCog-Bench等基准测试中，Visual-CoG分别提升了15%、5%和19%的性能，验证了其有效性。

## 📝 摘要（中文）

尽管近年来自回归模型在文本到图像生成（T2I）方面取得了显著进展，但其处理多属性和模糊提示的能力仍然有限。为了解决这些局限性，现有研究应用了链式思维（CoT）以实现阶段感知的视觉合成，并采用强化学习（RL）来提升推理能力。然而，大多数模型仅在生成阶段结束时提供奖励信号，这种单一的最终指导使得难以识别哪些阶段对最终结果有积极贡献，并可能导致次优策略。为此，本文提出了一种视觉指导链（Visual-CoG）范式，包含语义推理、过程优化和结果评估三个阶段，通过阶段感知的奖励在整个图像生成过程中提供即时指导。综合评估结果显示，Visual-CoG在多个基准测试中均有显著提升。

## 🔬 方法详解

**问题定义**：本文旨在解决现有文本到图像生成模型在处理多属性和模糊提示时的不足，尤其是奖励信号仅在生成结束时提供导致的次优策略问题。

**核心思路**：提出Visual-CoG框架，通过阶段感知奖励机制，在生成过程中对每个阶段进行即时指导，从而提升模型的推理能力和生成质量。

**技术框架**：Visual-CoG包括三个主要阶段：语义推理、过程优化和结果评估。每个阶段都配备相应的奖励机制，以确保生成过程的每一步都能得到有效反馈。

**关键创新**：最重要的创新在于引入了阶段感知的奖励机制，使得模型能够在生成的每个阶段获得反馈，从而优化每个阶段的决策过程，与传统的最终奖励机制形成鲜明对比。

**关键设计**：在设计上，模型采用了多层次的网络结构，并在损失函数中引入了阶段性奖励，以确保每个阶段的输出都能得到有效评估和优化。

## 📊 实验亮点

在多个基准测试中，Visual-CoG展示了显著的性能提升：在GenEval上提升了15%，在T2I-CompBench上提升了5%，在VisCog-Bench上提升了19%。这些结果表明，Visual-CoG在文本到图像生成任务中具有优越的表现。

## 🎯 应用场景

该研究的潜在应用领域包括艺术创作、广告设计和虚拟现实等，能够帮助用户更好地生成符合特定需求的图像。通过提升模型的推理能力，Visual-CoG有望在多模态生成任务中发挥更大作用，推动相关领域的发展。

## 📄 摘要（原文）

> Despite the promising progress of recent autoregressive models in text-to-image (T2I) generation, their ability to handle multi-attribute and ambiguous prompts remains limited. To address these limitations, existing works have applied chain-of-thought (CoT) to enable stage-aware visual synthesis and employed reinforcement learning (RL) to improve reasoning capabilities. However, most models provide reward signals only at the end of the generation stage. This monolithic final-only guidance makes it difficult to identify which stages contribute positively to the final outcome and may lead to suboptimal policies. To tackle this issue, we propose a Visual-Chain of Guidance (Visual-CoG) paradigm consisting of three stages: semantic reasoning, process refining, and outcome evaluation, with stage-aware rewards providing immediate guidance throughout the image generation pipeline. We further construct a visual cognition benchmark, VisCog-Bench, which comprises four subtasks to evaluate the effectiveness of semantic reasoning. Comprehensive evaluations on GenEval, T2I-CompBench, and the proposed VisCog-Bench show improvements of 15%, 5%, and 19%, respectively, demonstrating the superior performance of the proposed Visual-CoG. We will release all the resources soon.

