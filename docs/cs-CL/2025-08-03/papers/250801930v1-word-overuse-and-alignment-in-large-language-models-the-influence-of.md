---
layout: default
title: "Word Overuse and Alignment in Large Language Models: The Influence of Learning from Human Feedback"
---

# Word Overuse and Alignment in Large Language Models: The Influence of Learning from Human Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01930" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01930v1</a>
  <a href="https://arxiv.org/pdf/2508.01930.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01930v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01930v1', 'Word Overuse and Alignment in Large Language Models: The Influence of Learning from Human Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tom S. Juzek, Zina B. Ward

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-03

**备注**: Accepted for publication in the Proceedings of the 5th Workshop on Bias and Fairness in AI (BIAS 2025) at ECML PKDD

**DOI**: [10.17605/OSF.IO/JY48S](https://doi.org/10.17605/OSF.IO/JY48S)

---

## 💡 一句话要点

**提出一种方法以揭示大语言模型的词汇过度使用问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `人类反馈学习` `词汇偏好` `可解释人工智能` `文本生成` `对话系统`

## 📋 核心要点

1. 核心问题：现有研究未能明确解释大语言模型在词汇选择上的过度使用现象，尤其是与人类反馈学习的关系。
2. 方法要点：本研究提出了一种检测大语言模型词汇偏好的新方法，并通过实验验证了人类反馈学习对词汇选择的影响。
3. 实验或效果：实验结果显示，参与者更倾向于选择包含特定词汇的文本变体，揭示了词汇过度使用的潜在原因。

## 📝 摘要（中文）

大语言模型（LLMs）在使用某些术语时表现出过度使用的现象，例如“深入”和“复杂”。然而，这些词汇选择的具体原因尚不明确。本文利用Meta的Llama模型，研究了人类反馈学习（LHF）对词汇偏好的影响。我们提出了一种简单的程序来检测可能由LHF引起的词汇偏好，并通过实验模拟LHF过程，证明参与者系统性地偏好包含某些词的文本变体。这种词汇过度使用可以视为一种不一致现象，研究强调了不同人群（如LHF工作者与LLM用户）之间的词汇期望差异。我们的研究为可解释人工智能的研究提供了贡献，并强调了数据和过程透明性在对齐研究中的重要性。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在词汇选择上存在的过度使用现象，现有方法未能有效解释这种现象的根本原因，尤其是与人类反馈学习的关系。

**核心思路**：研究通过模拟人类反馈学习的过程，探索其对大语言模型词汇偏好的影响，提出了一种新的检测方法，以揭示潜在的词汇过度使用现象。

**技术框架**：整体架构包括数据收集、实验设计和结果分析三个主要模块。首先收集包含不同词汇的文本数据，然后设计实验以评估参与者的偏好，最后分析结果以确认词汇偏好的存在。

**关键创新**：本研究的创新点在于将人类反馈学习与词汇选择的关系进行了系统性探讨，提出了一种新的实验方法来验证这一关系，填补了现有研究的空白。

**关键设计**：在实验设计中，采用了直接偏好优化和强化学习等技术，设置了特定的词汇变体以供参与者选择，确保了实验的有效性和可靠性。参与者的选择偏好被量化并用于分析词汇过度使用的模式。

## 📊 实验亮点

实验结果表明，参与者在选择文本变体时，系统性地偏好包含特定词汇的选项，验证了人类反馈学习对词汇选择的影响。通过模拟LHF过程，研究揭示了词汇过度使用的潜在机制，为后续研究提供了重要的实验数据和理论支持。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等。通过理解大语言模型的词汇偏好，可以优化模型的输出，提高与用户的对话质量，进而提升用户体验。此外，研究结果也为可解释人工智能的发展提供了重要的理论基础，促进了模型的透明性和可控性。

## 📄 摘要（原文）

> Large Language Models (LLMs) are known to overuse certain terms like "delve" and "intricate." The exact reasons for these lexical choices, however, have been unclear. Using Meta's Llama model, this study investigates the contribution of Learning from Human Feedback (LHF), under which we subsume Reinforcement Learning from Human Feedback and Direct Preference Optimization. We present a straightforward procedure for detecting the lexical preferences of LLMs that are potentially LHF-induced. Next, we more conclusively link LHF to lexical overuse by experimentally emulating the LHF procedure and demonstrating that participants systematically prefer text variants that include certain words. This lexical overuse can be seen as a sort of misalignment, though our study highlights the potential divergence between the lexical expectations of different populations -- namely LHF workers versus LLM users. Our work contributes to the growing body of research on explainable artificial intelligence and emphasizes the importance of both data and procedural transparency in alignment research.

