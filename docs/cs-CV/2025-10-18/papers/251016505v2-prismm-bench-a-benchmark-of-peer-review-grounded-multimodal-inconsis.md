---
layout: default
title: PRISMM-Bench: A Benchmark of Peer-Review Grounded Multimodal Inconsistencies
---

# PRISMM-Bench: A Benchmark of Peer-Review Grounded Multimodal Inconsistencies

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.16505" target="_blank" class="toolbar-btn">arXiv: 2510.16505v2</a>
    <a href="https://arxiv.org/pdf/2510.16505.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16505v2" 
            onclick="toggleFavorite(this, '2510.16505v2', 'PRISMM-Bench: A Benchmark of Peer-Review Grounded Multimodal Inconsistencies')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Lukas Selch, Yufang Hou, M. Jehanzeb Mirza, Sivan Doveh, James Glass, Rogerio Feris, Wei Lin

**分类**: cs.CV

**发布日期**: 2025-10-18 (更新: 2025-10-21)

---

## 💡 一句话要点

**PRISMM-Bench：首个基于同行评审的多模态不一致性基准，用于评估LMMs的科学推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `科学推理` `不一致性检测` `同行评审` `基准测试`

## 📋 核心要点

1. 现有LMMs在科学论文理解中面临多模态信息不一致性检测的挑战，现有基准测试未能充分捕捉真实世界复杂性。
2. PRISMM-Bench通过挖掘同行评审意见，构建包含真实不一致性的数据集，并设计任务评估LMMs的检测、纠正和推理能力。
3. 实验结果表明，现有LMMs在PRISMM-Bench上的表现不佳（26.1-54.2%），揭示了多模态科学推理的巨大挑战。

## 📝 摘要（中文）

大型多模态模型（LMMs）越来越多地应用于科学研究，但它们是否能可靠地理解和推理论文中复杂的多模态信息仍不清楚。一个核心挑战在于检测和解决文本、图表、公式等之间的不一致性，这些问题通常很微妙，具有领域特异性，并最终损害清晰度、可重复性和信任度。现有基准忽略了这个问题，要么孤立地处理单一模态，要么依赖于未能捕捉真实世界复杂性的合成错误。我们推出了PRISMM-Bench（多模态模型同行评审来源不一致性集），这是第一个基于科学论文中真实评审员标记的不一致性的基准。通过评审挖掘、LLM辅助过滤和人工验证的多阶段流程，我们从242篇论文中整理出262个不一致性。基于此，我们设计了三个任务，即不一致性识别、补救和配对匹配，以评估模型检测、纠正和推理不同模态之间不一致性的能力。此外，为了解决多项选择评估中臭名昭著的“仅凭选择”的捷径问题，我们进一步引入了基于JSON的结构化答案表示，通过减少对表面文体线索的依赖来最小化语言偏差。我们对21个领先的LMM进行了基准测试，包括大型开源模型（GLM-4.5V 106B、InternVL3 78B）和专有模型（Gemini 2.5 Pro、具有高推理能力的GPT-5）。结果显示性能非常低（26.1-54.2%），突显了多模态科学推理的挑战，并推动了对值得信赖的科学助手的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决大型多模态模型（LMMs）在理解和推理科学论文时，难以检测和解决文本、图表、公式等模态间不一致性的问题。现有基准测试要么只关注单一模态，要么使用合成数据，无法真实反映科学论文中复杂且细微的不一致性，导致模型难以应用于实际科研场景。

**核心思路**：论文的核心思路是构建一个基于真实同行评审意见的数据集PRISMM-Bench，其中包含评审员在实际论文中发现的不一致性。通过这个数据集，可以更真实地评估LMMs在多模态科学推理方面的能力，并推动模型朝着更可靠的科学助手方向发展。

**技术框架**：PRISMM-Bench的构建流程包括：1) 从公开的同行评审数据中挖掘潜在的不一致性；2) 使用LLM辅助过滤，初步筛选出可能的不一致性；3) 通过人工验证，确认最终的不一致性样本。基于PRISMM-Bench，论文设计了三个任务：不一致性识别（Inconsistency Identification）、补救（Remedy）和配对匹配（Pair Matching），用于全面评估LMMs的能力。

**关键创新**：该论文最重要的创新点在于构建了一个基于真实同行评审意见的多模态不一致性基准PRISMM-Bench。与以往的合成数据或单一模态基准相比，PRISMM-Bench更贴近实际科研场景，能够更有效地评估LMMs在多模态科学推理方面的能力。此外，论文还引入了基于JSON的结构化答案表示，以减少多项选择题中的语言偏差。

**关键设计**：在数据构建方面，论文采用了多阶段的过滤和验证流程，以确保数据集的质量。在任务设计方面，论文设计了三个不同难度的任务，以全面评估LMMs的能力。为了减少多项选择题中的语言偏差，论文使用了结构化的JSON答案表示，避免模型仅仅依赖于表面文体线索进行选择。

## 📊 实验亮点

实验结果表明，包括GLM-4.5V 106B、InternVL3 78B、Gemini 2.5 Pro和GPT-5在内的21个领先LMMs在PRISMM-Bench上的表现均不佳，最高性能仅为54.2%，最低为26.1%。这突显了现有LMMs在多模态科学推理方面存在的巨大挑战，并为未来的研究指明了方向。

## 🎯 应用场景

该研究成果可应用于开发更可靠的科学助手，辅助科研人员进行文献阅读、论文撰写和实验设计。通过检测和解决多模态信息的不一致性，提高科研成果的清晰度、可重复性和可信度，加速科学发现的进程。未来，该基准可以扩展到其他科学领域，并用于评估和改进更多类型的多模态模型。

## 📄 摘要（原文）

> Large Multimodal Models (LMMs) are increasingly applied to scientific research, yet it remains unclear whether they can reliably understand and reason over the multimodal complexity of papers. A central challenge lies in detecting and resolving inconsistencies across text, figures, tables, and equations, issues that are often subtle, domain-specific, and ultimately undermine clarity, reproducibility, and trust. Existing benchmarks overlook this issue, either isolating single modalities or relying on synthetic errors that fail to capture real-world complexity. We introduce PRISMM-Bench (Peer-Review-sourced Inconsistency Set for Multimodal Models), the first benchmark grounded in real reviewer-flagged inconsistencies in scientific papers. Through a multi-stage pipeline of review mining, LLM-assisted filtering and human verification, we curate 262 inconsistencies from 242 papers. Based on this set, we design three tasks, namely inconsistency identification, remedy and pair matching, which assess a model's capacity to detect, correct, and reason over inconsistencies across different modalities. Furthermore, to address the notorious problem of choice-only shortcuts in multiple-choice evaluation, where models exploit answer patterns without truly understanding the question, we further introduce structured JSON-based answer representations that minimize linguistic biases by reducing reliance on superficial stylistic cues. We benchmark 21 leading LMMs, including large open-weight models (GLM-4.5V 106B, InternVL3 78B) and proprietary models (Gemini 2.5 Pro, GPT-5 with high reasoning). Results reveal strikingly low performance (26.1-54.2%), underscoring the challenge of multimodal scientific reasoning and motivating progress towards trustworthy scientific assistants.

