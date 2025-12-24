---
layout: default
title: "From Directions to Cones: Exploring Multidimensional Representations of Propositional Facts in LLMs"
---

# From Directions to Cones: Exploring Multidimensional Representations of Propositional Facts in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21800" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21800v1</a>
  <a href="https://arxiv.org/pdf/2505.21800.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21800v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21800v1', 'From Directions to Cones: Exploring Multidimensional Representations of Propositional Facts in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stanley Yu, Vaidehi Bulusu, Oscar Yasunaga, Clayton Lau, Cole Blondin, Sean O'Brien, Kevin Zhu, Vasu Sharma

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出多维锥体框架以探讨LLMs中的真理表示问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `真理表示` `多维锥体` `因果干预` `模型泛化` `抽象行为探测`

## 📋 核心要点

1. 现有方法主要依赖单一线性方向来表示命题的真实性，无法充分捕捉其复杂的几何特征。
2. 本研究提出了多维锥体框架，旨在更全面地表示和理解LLMs中的真理相关行为。
3. 实验结果表明，因果干预可以有效改变模型响应，且学习到的锥体在不同模型架构中具有良好的泛化能力。

## 📝 摘要（中文）

大型语言模型（LLMs）展现出强大的对话能力，但常常生成虚假信息。先前的研究表明，简单命题的真实性可以用模型内部激活的单一线性方向表示，但这可能无法完全捕捉其底层几何结构。本研究扩展了最近为建模拒绝而引入的锥体概念框架，应用于真理领域。我们识别出多维锥体，这些锥体在多个LLM家族中因果中介真理相关行为。我们的结果通过三条证据支持：因果干预可靠地翻转模型对事实陈述的响应，学习到的锥体在模型架构间具有泛化能力，锥体干预保留了无关的模型行为。这些发现揭示了在LLMs中支配简单真/假命题的更丰富的多方向结构，并强调了锥体概念作为探测抽象行为的有前景工具。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型中真理表示的不足，现有方法仅用单一线性方向来表示命题的真实性，未能反映其复杂的多维几何特征。

**核心思路**：论文提出了多维锥体的概念，认为这种结构能够更好地捕捉和中介真理相关的行为，进而提升模型的响应准确性。

**技术框架**：整体架构包括三个主要模块：首先，通过因果干预技术识别模型的响应变化；其次，学习多维锥体以表示不同的真理状态；最后，验证锥体干预对模型行为的影响。

**关键创新**：最重要的技术创新在于引入多维锥体概念，突破了传统单线性方向的限制，能够更全面地描述和理解模型的真理相关行为。

**关键设计**：在实验中，采用了特定的因果干预策略，设计了适应不同模型架构的锥体学习算法，并确保干预过程不会影响模型的其他无关行为。

## 📊 实验亮点

实验结果显示，通过因果干预，模型对事实陈述的响应能够可靠地翻转，且学习到的多维锥体在不同模型架构中表现出良好的泛化能力。这一方法在保留无关模型行为的同时，显著提升了对真理相关行为的理解和控制。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和信息检索等。通过更准确地理解和表示真理，能够提升模型在生成准确内容方面的能力，进而提高用户体验和信息的可靠性。未来，该方法可能在多种语言模型的开发和优化中发挥重要作用。

## 📄 摘要（原文）

> Large Language Models (LLMs) exhibit strong conversational abilities but often generate falsehoods. Prior work suggests that the truthfulness of simple propositions can be represented as a single linear direction in a model's internal activations, but this may not fully capture its underlying geometry. In this work, we extend the concept cone framework, recently introduced for modeling refusal, to the domain of truth. We identify multi-dimensional cones that causally mediate truth-related behavior across multiple LLM families. Our results are supported by three lines of evidence: (i) causal interventions reliably flip model responses to factual statements, (ii) learned cones generalize across model architectures, and (iii) cone-based interventions preserve unrelated model behavior. These findings reveal the richer, multidirectional structure governing simple true/false propositions in LLMs and highlight concept cones as a promising tool for probing abstract behaviors.

