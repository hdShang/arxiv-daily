---
layout: default
title: Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks
---

# Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20047" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20047v1</a>
  <a href="https://arxiv.org/pdf/2505.20047.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20047v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20047v1', 'Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Debargha Ganguly, Vikash Singh, Sreehari Sankar, Biyao Zhang, Xuecen Zhang, Srinivasan Iyengar, Xiaotian Han, Amit Sharma, Shivkumar Kalyanaraman, Vipin Chaudhary

**分类**: cs.CL, cs.AI, cs.LO, cs.SE

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出概率上下文无关文法以解决LLM在自动推理中的不确定性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自动推理` `不确定性量化` `概率上下文无关文法` `形式验证` `信号融合`

## 📋 核心要点

1. 现有大型语言模型在生成正式规范时存在不确定性，无法满足形式验证的确定性要求。
2. 本文提出了一种概率上下文无关文法框架，以建模LLM输出并量化不确定性，进而提高自动推理的可靠性。
3. 通过实验，发现信号融合方法能够显著降低错误率，逻辑任务准确率提升34.8%，事实任务下降44.5%。

## 📝 摘要（中文）

大型语言模型（LLMs）在生成正式规范方面展现出显著潜力，但其概率性质与形式验证所需的确定性保证之间存在根本矛盾。本文通过系统评估五种前沿LLM，探讨了LLM生成的正式文档中的失败模式和不确定性量化（UQ）。研究发现，基于可满足性模理论（SMT）的自动形式化在逻辑任务上准确率提高34.8%，而在事实任务上下降44.5%。我们提出了一种概率上下文无关文法（PCFG）框架来建模LLM输出，形成了更精细的不确定性分类。最后，轻量级信号融合方法显著减少了错误（14-100%），将LLM驱动的形式化转变为可靠的工程学科。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在自动推理任务中生成的正式文档的不确定性问题。现有方法在量化不确定性时未能有效识别错误，导致形式验证的可靠性不足。

**核心思路**：提出概率上下文无关文法（PCFG）框架，以建模LLM输出并形成不确定性分类，从而实现更精确的错误识别和选择性验证。

**技术框架**：整体架构包括LLM输出的生成、PCFG建模、不确定性量化和信号融合四个主要模块。首先生成文档，然后通过PCFG分析输出的不确定性，最后融合不同信号进行选择性验证。

**关键创新**：最重要的创新在于引入PCFG框架来量化LLM输出的不确定性，形成了新的不确定性分类体系，与传统的UQ技术相比，能够更有效地识别任务相关的错误。

**关键设计**：在模型设计中，采用了基于语法熵的信号量化方法，并结合AUROC指标进行评估，确保在逻辑任务中达到高于0.93的性能，同时保持较低的误报率。

## 📊 实验亮点

实验结果显示，基于PCFG的信号融合方法能够将错误率降低14-100%，在逻辑任务中准确率提升34.8%，而在事实任务中尽管出现下降，但整体验证过程的可靠性显著增强。

## 🎯 应用场景

该研究的潜在应用领域包括自动化软件验证、智能合约生成和法律文档分析等。通过提高LLM在生成正式文档时的可靠性，能够为工程师提供更可信的工具，推动自动推理技术的广泛应用和发展。

## 📄 摘要（原文）

> Large language models (LLMs) show remarkable promise for democratizing automated reasoning by generating formal specifications. However, a fundamental tension exists: LLMs are probabilistic, while formal verification demands deterministic guarantees. This paper addresses this epistemological gap by comprehensively investigating failure modes and uncertainty quantification (UQ) in LLM-generated formal artifacts. Our systematic evaluation of five frontier LLMs reveals Satisfiability Modulo Theories (SMT) based autoformalization's domain-specific impact on accuracy (from +34.8% on logical tasks to -44.5% on factual ones), with known UQ techniques like the entropy of token probabilities failing to identify these errors. We introduce a probabilistic context-free grammar (PCFG) framework to model LLM outputs, yielding a refined uncertainty taxonomy. We find uncertainty signals are task-dependent (e.g., grammar entropy for logic, AUROC>0.93). Finally, a lightweight fusion of these signals enables selective verification, drastically reducing errors (14-100%) with minimal abstention, transforming LLM-driven formalization into a reliable engineering discipline.

