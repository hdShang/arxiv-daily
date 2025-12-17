---
layout: default
title: Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning
---

# Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18395" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18395</a>
  <a href="https://arxiv.org/pdf/2508.18395.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18395" onclick="toggleFavorite(this, '2508.18395', 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jungsuk Oh, Jay-Yoon Lee

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出潜在自一致性方法以解决长短答案推理中的一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自一致性` `长短答案推理` `大型语言模型` `语义一致性` `机器学习` `问答系统` `模型优化`

## 📋 核心要点

1. 现有方法在处理复杂或长形式问题时，输出结果常常不一致，影响了问答系统的可靠性。
2. 本文提出的潜在自一致性（LSC）方法，通过可学习的标记嵌入选择最语义一致的响应，克服了现有方法的不足。
3. 在多个短形式和长形式推理基准上，LSC的性能超越了现有的自一致性方法，同时保持了较低的计算开销。

## 📝 摘要（中文）

在大型语言模型（LLMs）的概率解码中，输出结果常常不一致，尤其是在复杂或长形式问题上。自一致性（SC）通过对短形式问答进行多数投票来缓解这一问题，而通用自一致性（USC）和加权单元一致性评分（WUCS）虽然扩展到长形式响应，但在短形式基准上准确性下降。本文提出了潜在自一致性（LSC），通过可学习的标记嵌入选择最语义一致的响应。LSC在标准解码的基础上仅引入了最多0.9%的运行时开销，且无需更改模型架构。在6个短形式和5个长形式推理基准上，LSC在短形式和长形式的平均性能上均超越了SC、USC和WUCS，同时在原始推理上增加的计算开销微乎其微。这些结果使LSC成为一种可靠的一致性选择方法，能够有效处理各种答案格式。此外，LSC提供了良好的置信度估计，在两种答案格式下保持低预期校准误差。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂问题上的输出不一致性，现有的自一致性方法在短形式和长形式问答中表现不均，导致准确性下降。

**核心思路**：潜在自一致性（LSC）通过学习标记的嵌入来选择语义上最一致的响应，避免了传统方法的局限性，且不需要改变模型架构。

**技术框架**：LSC的整体架构包括输入标记的嵌入、语义一致性评分和最终响应选择三个主要模块。首先，通过可学习的嵌入将输入标记转化为向量表示，然后计算语义一致性，最后选择得分最高的响应。

**关键创新**：LSC的主要创新在于其使用可学习的标记嵌入来评估语义一致性，这与传统的基于字符串的多数投票方法有本质区别，能够更好地处理复杂的长形式问题。

**关键设计**：LSC在设计上保持轻量级，运行时开销仅为0.9%，并且采用了适应性损失函数来优化语义一致性评分，确保在不同类型的问答中均能保持高效性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2508.18395/overview.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2508.18395/llama3_MATH_major_plot.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2508.18395/lsc_MATH_calib.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在6个短形式和5个长形式推理基准上，LSC的平均性能超越了SC、USC和WUCS，尤其在短形式问答中表现优异，且在计算开销上几乎可以忽略不计。这表明LSC在不同答案格式下均具备良好的适应性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、教育辅助工具和客户服务自动化等。通过提高长短答案推理的一致性，LSC能够显著提升用户体验和系统的可靠性，未来可能在更多实际场景中得到广泛应用。

## 📄 摘要（原文）

> Probabilistic decoding in Large Language Models (LLMs) often yields inconsistent outputs, particularly on complex or long-form questions. Self-Consistency (SC) mitigates this for short-form QA by majority voting over exact strings, whereas Universal Self-Consistency (USC) and Weighted Unigram Consistency Score (WUCS) extend to long-form responses but lose accuracy on short-form benchmarks.We introduce \textbf{Latent Self-Consistency (LSC)}, which selects the most semantically consistent response using learnable token embeddings. LSC's lightweight forward processing of summary tokens only introduces negligible runtime overhead (at most $0.9\%$) on top of standard decoding of the base LLM, and requires no changes to the model architecture.Across 6 short-form and 5 long-form reasoning benchmarks (e.g., MATH, MMLU, TruthfulQA), LSC surpasses SC, USC, and WUCS on both short-form and long-form on average performance, while adding negligible computational overhead on vanilla inference. These results position LSC as a reliable consistency-selection method that works effectively across various answer formats. Additionally, LSC provides well-calibrated confidence estimates, maintaining low expected calibration error across both answer formats.

