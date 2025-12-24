---
layout: default
title: "STEM: Efficient Relative Capability Evaluation of LLMs through Structured Transition Samples"
---

# STEM: Efficient Relative Capability Evaluation of LLMs through Structured Transition Samples

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12096" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12096v2</a>
  <a href="https://arxiv.org/pdf/2508.12096.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12096v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12096v2', 'STEM: Efficient Relative Capability Evaluation of LLMs through Structured Transition Samples')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haiquan Hu, Jiazhi Jiang, Shiyou Xu, Ruhan Zeng, Tian Wang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-16 (更新: 2025-08-20)

**备注**: Submit to AAAI 2026

---

## 💡 一句话要点

**提出STEM方法以高效评估大型语言模型的相对能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `能力评估` `结构化过渡` `显著过渡样本` `性能分析` `自然语言处理` `模型优化`

## 📋 核心要点

1. 现有评估方法在快速发展的LLMs能力面前显得不足，无法有效区分模型间的真实差异。
2. STEM方法通过识别显著过渡样本，利用不同参数规模的同架构模型之间的性能变化来评估模型能力。
3. 实验结果表明，STEM能够准确捕捉模型性能趋势，并与真实能力排名高度一致，展示了其有效性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）能力的快速提升，评估这些模型的能力变得愈发困难。尽管新模型在标准基准测试中通常获得更高分数，但这些提升并不总能反映出真实世界的推理能力。此外，公共基准的过拟合和全面评估的高计算成本使得区分模型之间的有意义差异变得昂贵且低效。为了解决这些挑战，本文提出了结构化过渡评估方法（STEM），这是一个轻量且可解释的评估框架，旨在高效估计LLMs的相对能力。STEM通过分析同一架构但参数规模不同的LLMs之间的一致性能过渡，识别出显著过渡样本（STS），从而有效估计未知模型的能力位置。实验结果表明，STEM能够可靠捕捉性能趋势，并与模型能力的真实排名一致，展示了其作为一种实用且可扩展的细粒度、架构无关的LLMs评估方法的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型评估中的挑战，现有方法在快速发展的模型能力面前难以有效区分模型间的真实差异，且存在过拟合和高计算成本的问题。

**核心思路**：STEM方法的核心思想是通过分析同一架构但不同参数规模的模型之间的一致性能过渡，识别出显著过渡样本（STS），从而高效估计未知模型的能力位置。

**技术框架**：STEM的整体架构包括样本选择、性能分析和能力估计三个主要模块。首先，通过对不同规模模型的性能进行分析，识别出显著过渡样本；然后，利用这些样本进行能力位置的估计。

**关键创新**：STEM的主要创新在于其轻量级和可解释性，能够在不依赖全面评估的情况下，通过显著过渡样本有效捕捉模型能力的相对位置。这与传统方法的全面评估方式形成了鲜明对比。

**关键设计**：在关键设计方面，STEM通过选择合适的基准和样本，确保显著过渡样本的代表性。此外，损失函数和评估指标的设计也经过精心调整，以提高能力估计的准确性。

## 📊 实验亮点

实验结果显示，STEM方法能够可靠捕捉模型性能趋势，并与真实能力排名高度一致。具体而言，STEM在多个基准测试中表现出色，能够有效区分不同模型的能力，提升了评估的准确性和效率。

## 🎯 应用场景

STEM方法在大型语言模型的评估中具有广泛的应用潜力，能够为模型开发者提供更为精准的能力评估，帮助优化模型设计和选择。此外，该方法的可扩展性使其适用于不同架构的模型评估，推动了自然语言处理领域的研究进展。

## 📄 摘要（原文）

> Evaluating large language models (LLMs) has become increasingly challenging as model capabilities advance rapidly. While recent models often achieve higher scores on standard benchmarks, these improvements do not consistently reflect enhanced real-world reasoning capabilities. Moreover, widespread overfitting to public benchmarks and the high computational cost of full evaluations have made it both expensive and less effective to distinguish meaningful differences between models. To address these challenges, we propose the \textbf{S}tructured \textbf{T}ransition \textbf{E}valuation \textbf{M}ethod (STEM), a lightweight and interpretable evaluation framework for efficiently estimating the relative capabilities of LLMs. STEM identifies \textit{significant transition samples} (STS) by analyzing consistent performance transitions among LLMs of the same architecture but varying parameter scales. These samples enable STEM to effectively estimate the capability position of an unknown model. Qwen3 model family is applied to construct the STS pool on six diverse and representative benchmarks. To assess generalizability. Experimental results indicate that STEM reliably captures performance trends, aligns with ground-truth rankings of model capability. These findings highlight STEM as a practical and scalable method for fine-grained, architecture-agnostic evaluation of LLMs.

