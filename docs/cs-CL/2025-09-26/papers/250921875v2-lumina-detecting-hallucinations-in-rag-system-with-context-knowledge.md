---
layout: default
title: "LUMINA: Detecting Hallucinations in RAG System with Context-Knowledge Signals"
---

# LUMINA: Detecting Hallucinations in RAG System with Context-Knowledge Signals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21875" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21875v2</a>
  <a href="https://arxiv.org/pdf/2509.21875.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21875v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21875v2', 'LUMINA: Detecting Hallucinations in RAG System with Context-Knowledge Signals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samuel Yeh, Sharon Li, Tanwi Mallick

**分类**: cs.CL

**发布日期**: 2025-09-26 (更新: 2025-10-14)

---

## 💡 一句话要点

**LUMINA：利用上下文-知识信号检测RAG系统中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `幻觉检测` `上下文利用率` `知识利用率` `大型语言模型`

## 📋 核心要点

1. 现有RAG系统仍存在幻觉问题，现有检测方法依赖大量超参数调整，泛化性受限。
2. LUMINA通过量化外部上下文和内部知识的利用率来检测幻觉，无需大量超参数调整。
3. 实验表明，LUMINA在多个基准测试中优于现有方法，且对检索质量和模型匹配具有鲁棒性。

## 📝 摘要（中文）

检索增强生成（RAG）旨在通过将响应建立在检索到的文档上来减轻大型语言模型（LLM）中的幻觉。然而，即使提供了正确且充分的上下文，基于RAG的LLM仍然会产生幻觉。越来越多的研究表明，这源于模型使用外部上下文和内部知识之间的不平衡，并且一些方法试图量化这些信号以进行幻觉检测。然而，现有方法需要大量的超参数调整，限制了它们的泛化性。我们提出了LUMINA，这是一个新颖的框架，通过上下文-知识信号检测RAG系统中的幻觉：外部上下文利用率通过分布距离来量化，而内部知识利用率通过跟踪预测的token在transformer层中的演变来衡量。我们进一步引入了一个框架来统计验证这些测量结果。在常见的RAG幻觉基准和四个开源LLM上的实验表明，LUMINA实现了始终如一的高AUROC和AUPRC分数，在HalluRAG上优于先前的基于利用率的方法高达+13% AUROC。此外，LUMINA在关于检索质量和模型匹配的宽松假设下仍然具有鲁棒性，提供了有效性和实用性。

## 🔬 方法详解

**问题定义**：论文旨在解决RAG系统中LLM产生的幻觉问题。现有方法，如基于利用率的方法，通常需要大量的超参数调整，这限制了它们在不同场景和模型上的泛化能力。此外，如何有效地量化外部上下文和内部知识的利用率仍然是一个挑战。

**核心思路**：LUMINA的核心思路是通过量化外部上下文和内部知识的利用率来判断是否存在幻觉。如果模型过度依赖内部知识而忽略检索到的上下文，则更有可能产生幻觉。通过分别衡量上下文利用率和知识利用率，并结合统计验证，可以更准确地检测幻觉。

**技术框架**：LUMINA框架包含两个主要模块：上下文利用率量化和内部知识利用率量化。上下文利用率通过计算生成文本的token分布与检索文档的token分布之间的距离来衡量。内部知识利用率通过跟踪预测token在Transformer层中的变化来衡量，如果token在早期层就确定，则表明模型更多地依赖内部知识。最后，使用统计验证框架来评估这些测量结果的显著性。

**关键创新**：LUMINA的关键创新在于提出了一种无需大量超参数调整即可有效量化上下文和知识利用率的方法。通过使用分布距离来衡量上下文利用率，并跟踪token在Transformer层中的演变来衡量知识利用率，LUMINA能够更准确地检测幻觉。此外，统计验证框架进一步提高了检测的可靠性。

**关键设计**：上下文利用率的量化使用了Jensen-Shannon散度来计算生成文本和检索文档的token分布之间的距离。内部知识利用率的量化通过计算每个token在不同Transformer层之间的预测概率变化来衡量。统计验证框架使用bootstrap方法来评估测量结果的显著性，并设置阈值来判断是否存在幻觉。

## 📊 实验亮点

LUMINA在HalluRAG等基准测试中取得了显著的性能提升，AUROC指标最高提升了13%。实验结果表明，LUMINA优于现有的基于利用率的方法，并且在检索质量和模型匹配的宽松假设下仍然具有鲁棒性。这表明LUMINA具有很强的泛化能力和实用价值。

## 🎯 应用场景

LUMINA可应用于各种基于RAG的LLM应用中，例如问答系统、文本摘要和对话生成。通过检测和减少幻觉，可以提高这些应用的可靠性和准确性。该研究对于构建更值得信赖和实用的LLM系统具有重要意义，并有助于推动LLM在实际场景中的广泛应用。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) aims to mitigate hallucinations in large language models (LLMs) by grounding responses in retrieved documents. Yet, RAG-based LLMs still hallucinate even when provided with correct and sufficient context. A growing line of work suggests that this stems from an imbalance between how models use external context and their internal knowledge, and several approaches have attempted to quantify these signals for hallucination detection. However, existing methods require extensive hyperparameter tuning, limiting their generalizability. We propose LUMINA, a novel framework that detects hallucinations in RAG systems through context-knowledge signals: external context utilization is quantified via distributional distance, while internal knowledge utilization is measured by tracking how predicted tokens evolve across transformer layers. We further introduce a framework for statistically validating these measurements. Experiments on common RAG hallucination benchmarks and four open-source LLMs show that LUMINA achieves consistently high AUROC and AUPRC scores, outperforming prior utilization-based methods by up to +13% AUROC on HalluRAG. Moreover, LUMINA remains robust under relaxed assumptions about retrieval quality and model matching, offering both effectiveness and practicality.

