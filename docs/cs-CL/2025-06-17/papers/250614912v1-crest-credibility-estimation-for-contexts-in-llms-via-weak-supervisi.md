---
layout: default
title: "CrEst: Credibility Estimation for Contexts in LLMs via Weak Supervision"
---

# CrEst: Credibility Estimation for Contexts in LLMs via Weak Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14912" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14912v1</a>
  <a href="https://arxiv.org/pdf/2506.14912.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14912v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14912v1', 'CrEst: Credibility Estimation for Contexts in LLMs via Weak Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dyah Adila, Shuai Zhang, Boran Han, Bonan Min, Yuyang Wang

**分类**: cs.CL, cs.LG

**发布日期**: 2025-06-17

---

## 💡 一句话要点

**提出CrEst框架以解决LLMs上下文可信度评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `上下文可信度` `弱监督学习` `大型语言模型` `信息检索` `知识问答` `自动内容生成`

## 📋 核心要点

1. 现有方法在处理上下文文档的可信度时存在不足，可能导致不可靠信息的传播。
2. CrEst框架通过弱监督方式评估上下文文档的可信度，利用文档间的一致性进行自动化评估。
3. 实验结果显示，CrEst在多个模型和数据集上均表现优异，准确率和F1分数均有显著提升。

## 📝 摘要（中文）

上下文信息的整合显著提升了大型语言模型（LLMs）在知识密集型任务中的表现。然而，现有方法往往忽视了一个关键挑战：上下文文档的可信度可能差异很大，导致不可靠信息的传播。本文提出了CrEst，一个新颖的弱监督框架，用于在LLM推理过程中评估上下文文档的可信度，无需手动标注。我们的研究基于一个洞察，即可信文档往往与其他可信文档具有更高的语义一致性，从而通过文档间一致性实现自动化的可信度评估。我们提出了两种集成策略：一种是针对无法访问内部权重或激活的黑箱方法，另一种是直接修改注意力机制的白箱方法。大量实验表明，CrEst在三种模型架构和五个数据集上均优于强基线，准确率提升高达26.86%，F1分数提高3.49%。进一步分析显示，CrEst在高噪声条件下仍保持稳健性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在推理过程中对上下文文档可信度评估的不足，现有方法未能有效处理文档可信度的差异性，可能导致不准确的信息传播。

**核心思路**：CrEst框架的核心思想是通过弱监督学习评估上下文文档的可信度，依赖于可信文档之间的语义一致性来实现自动化的可信度估计。

**技术框架**：CrEst的整体架构包括两个主要模块：黑箱方法和白箱方法。黑箱方法适用于无法访问模型内部状态的情况，而白箱方法则通过直接修改注意力机制来整合可信度信息。

**关键创新**：CrEst的主要创新在于其弱监督学习框架，能够在没有手动标注的情况下实现文档可信度的自动评估，这与传统方法依赖于大量标注数据的做法有本质区别。

**关键设计**：在设计中，CrEst采用了文档间一致性作为可信度评估的基础，并通过特定的损失函数来优化模型性能，确保在高噪声环境下仍能保持稳健的表现。

## 📊 实验亮点

CrEst在三种不同的模型架构和五个数据集上进行了广泛的实验，结果显示其在准确率上最高提升了26.86%，F1分数提升了3.49%。这些结果表明，CrEst在处理上下文文档可信度评估方面具有显著优势，尤其在高噪声条件下仍能保持良好的性能。

## 🎯 应用场景

CrEst框架的潜在应用领域包括信息检索、知识问答系统和自动内容生成等。通过提高上下文文档的可信度评估能力，该研究能够有效减少不可靠信息的传播，提升用户体验和系统的整体性能。未来，CrEst有望在更多实际应用中发挥重要作用，推动智能系统的可信性和可靠性。

## 📄 摘要（原文）

> The integration of contextual information has significantly enhanced the performance of large language models (LLMs) on knowledge-intensive tasks. However, existing methods often overlook a critical challenge: the credibility of context documents can vary widely, potentially leading to the propagation of unreliable information. In this paper, we introduce CrEst, a novel weakly supervised framework for assessing the credibility of context documents during LLM inference--without requiring manual annotations. Our approach is grounded in the insight that credible documents tend to exhibit higher semantic coherence with other credible documents, enabling automated credibility estimation through inter-document agreement. To incorporate credibility into LLM inference, we propose two integration strategies: a black-box approach for models without access to internal weights or activations, and a white-box method that directly modifies attention mechanisms. Extensive experiments across three model architectures and five datasets demonstrate that CrEst consistently outperforms strong baselines, achieving up to a 26.86% improvement in accuracy and a 3.49% increase in F1 score. Further analysis shows that CrEst maintains robust performance even under high-noise conditions.

