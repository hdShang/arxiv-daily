---
layout: default
title: "From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology"
---

# From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16697" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16697v1</a>
  <a href="https://arxiv.org/pdf/2506.16697.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16697v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16697v1', 'From Prompts to Constructs: A Dual-Validity Framework for LLM Research in Psychology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhicheng Lin

**分类**: cs.CY, cs.AI, cs.CL, cs.HC

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出双有效性框架以解决心理学中LLM研究的测量问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `心理学研究` `测量标准` `因果推断` `统计分析` `验证策略`

## 📋 核心要点

1. 现有方法在将人类测量工具应用于LLM时，常导致矛盾结果，产生统计伪影。
2. 论文提出双有效性框架，整合可靠测量与因果推断标准，以指导心理学研究中的LLM应用。
3. 通过明确不同心理构念的验证策略，提升了对LLM在心理学应用中的科学性和有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在心理学领域的应用日益广泛，作为研究工具、实验对象和认知模型。然而，将人类测量工具应用于这些系统可能导致矛盾结果，产生测量幻影，即统计伪影而非真实心理现象。本文提出双有效性框架，旨在整合可靠测量原则与因果推断标准，明确支持科学主张所需证据的规模。使用LLM进行文本分类可能只需基本准确性检查，而声称其能够模拟焦虑则需更严格的验证过程。当前实践未能满足这些要求，常将统计模式匹配视为心理现象的证据。

## 🔬 方法详解

**问题定义**：本文解决的问题是如何在心理学研究中有效应用大型语言模型（LLMs），避免因测量工具不当使用而导致的统计伪影。现有方法未能满足对心理现象的严格验证要求，导致结果的可信度降低。

**核心思路**：论文的核心思路是提出一个双有效性框架，强调在不同科学主张下所需的证据规模差异。通过将可靠测量原则与因果推断标准结合，确保对LLM的应用进行科学验证。

**技术框架**：该框架包括两个主要模块：一是对心理构念的计算类比，二是建立清晰、可扩展的证据标准。研究者需根据不同的心理构念，选择合适的验证策略。

**关键创新**：最重要的技术创新点在于提出了双有效性框架，明确了在不同科学主张下，所需的验证程度与方法的差异。这与现有方法的本质区别在于强调了验证的层次性和科学性。

**关键设计**：在框架中，关键设计包括对心理构念的定义、验证策略的选择以及统计分析方法的应用。具体参数设置和损失函数的选择需根据不同的实验目标进行调整。通过这种方式，确保了对LLM输出的科学解读。

## 📊 实验亮点

论文提出的双有效性框架在理论上为LLM的心理学应用提供了新的验证标准，强调了不同心理构念的验证策略差异。通过这一框架，研究者能够更科学地评估LLM的输出，提升了心理学研究的严谨性与可信度。

## 🎯 应用场景

该研究的潜在应用领域包括心理学实验设计、心理健康评估和人机交互等。通过建立更为严谨的验证标准，能够提升LLM在心理学研究中的有效性和可靠性，推动心理学与人工智能的交叉发展。未来可能影响心理学研究方法的标准化与科学性。

## 📄 摘要（原文）

> Large language models (LLMs) are rapidly being adopted across psychology, serving as research tools, experimental subjects, human simulators, and computational models of cognition. However, the application of human measurement tools to these systems can produce contradictory results, raising concerns that many findings are measurement phantoms--statistical artifacts rather than genuine psychological phenomena. In this Perspective, we argue that building a robust science of AI psychology requires integrating two of our field's foundational pillars: the principles of reliable measurement and the standards for sound causal inference. We present a dual-validity framework to guide this integration, which clarifies how the evidence needed to support a claim scales with its scientific ambition. Using an LLM to classify text may require only basic accuracy checks, whereas claiming it can simulate anxiety demands a far more rigorous validation process. Current practice systematically fails to meet these requirements, often treating statistical pattern matching as evidence of psychological phenomena. The same model output--endorsing "I am anxious"--requires different validation strategies depending on whether researchers claim to measure, characterize, simulate, or model psychological constructs. Moving forward requires developing computational analogues of psychological constructs and establishing clear, scalable standards of evidence rather than the uncritical application of human measurement tools.

