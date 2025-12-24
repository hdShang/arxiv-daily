---
layout: default
title: "CoCoA: Confidence and Context-Aware Adaptive Decoding for Resolving Knowledge Conflicts in Large Language Models"
---

# CoCoA: Confidence and Context-Aware Adaptive Decoding for Resolving Knowledge Conflicts in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17670" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17670v2</a>
  <a href="https://arxiv.org/pdf/2508.17670.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17670v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17670v2', 'CoCoA: Confidence and Context-Aware Adaptive Decoding for Resolving Knowledge Conflicts in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anant Khandelwal, Manish Gupta, Puneet Agrawal

**分类**: cs.CL

**发布日期**: 2025-08-25 (更新: 2025-08-27)

**备注**: Accepted to EMNLP'25, Main. 21 pages, 17 tables, 3 Figures

---

## 💡 一句话要点

**提出CoCoA以解决大型语言模型中的知识冲突问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识冲突` `自适应解码` `信心感知` `大型语言模型` `问答系统` `自动摘要` `长文本处理`

## 📋 核心要点

1. 现有的对比解码方法在处理知识冲突时缺乏适应性，尤其在低冲突环境中性能可能下降。
2. CoCoA通过信心感知度量和广义散度来实现冲突解决，保持在低冲突情况下的强性能。
3. 在多个基准测试中，CoCoA的问答准确率平均提升9.2分，摘要和长文本问答的事实性提升2.5分。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成忠实内容时面临来自参数记忆与外部上下文之间的知识冲突。现有的对比解码方法虽然针对冲突进行了调优，但在低冲突环境下的适应性不足，可能导致性能下降。为此，本文提出了一种新颖的基于信心和上下文的自适应解码算法CoCoA，旨在实现原则性的冲突解决和增强的忠实性。CoCoA通过利用信心感知度量（熵差和上下文峰值）以及参数和上下文分布之间的广义散度来解决冲突。大量实验表明，CoCoA在多个问答、摘要和长文本问答基准上表现出色，QA准确率平均提升9.2分，摘要和长文本问答的事实性平均提升2.5分，并对冲突变化表现出更强的敏感性。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型生成内容时的知识冲突问题，现有方法在低冲突环境下的适应性不足，可能导致生成内容的准确性和忠实性下降。

**核心思路**：CoCoA的核心思想是结合信心感知度量（如熵差和上下文峰值）与参数和上下文分布之间的广义散度，以实现更有效的冲突解决。通过这种方式，CoCoA能够在不同冲突程度下保持良好的性能。

**技术框架**：CoCoA的整体架构包括信心感知模块和冲突解决模块。信心感知模块评估生成内容的可信度，而冲突解决模块则根据评估结果调整生成策略，以优化输出质量。

**关键创新**：CoCoA的主要创新在于其自适应解码机制，能够根据上下文和信心动态调整生成策略，与传统的静态解码方法相比，具有更高的灵活性和准确性。

**关键设计**：在参数设置上，CoCoA引入了熵差和上下文峰值作为关键度量指标，并设计了相应的损失函数，以确保生成内容的忠实性和准确性。

## 📊 实验亮点

在实验中，CoCoA在多个基准测试中表现出色，问答准确率平均提升9.2分，相较于强基线AdaCAD，摘要和长文本问答的事实性平均提升2.5分，展现出对冲突变化的优越敏感性。

## 🎯 应用场景

CoCoA的研究成果在多个领域具有潜在应用价值，包括问答系统、自动摘要生成和长文本处理等。通过提高生成内容的准确性和忠实性，CoCoA能够为用户提供更可靠的信息服务，推动智能助手和内容生成工具的发展。

## 📄 摘要（原文）

> Faithful generation in large language models (LLMs) is challenged by knowledge conflicts between parametric memory and external context. Existing contrastive decoding methods tuned specifically to handle conflict often lack adaptability and can degrade performance in low conflict settings. We introduce CoCoA (Confidence- and Context-Aware Adaptive Decoding), a novel token-level algorithm for principled conflict resolution and enhanced faithfulness. CoCoA resolves conflict by utilizing confidence-aware measures (entropy gap and contextual peakedness) and the generalized divergence between the parametric and contextual distributions. Crucially, CoCoA maintains strong performance even in low conflict settings. Extensive experiments across multiple LLMs on diverse Question Answering (QA), Summarization, and Long-Form Question Answering (LFQA) benchmarks demonstrate CoCoA's state-of-the-art performance over strong baselines like AdaCAD. It yields significant gains in QA accuracy, up to 9.2 points on average compared to the strong baseline AdaCAD, and improves factuality in summarization and LFQA by up to 2.5 points on average across key benchmarks. Additionally, it demonstrates superior sensitivity to conflict variations. CoCoA enables more informed, context-aware, and ultimately more faithful token generation.

